---
license: llama3
---


## Installation from source

```bash
git clone https://github.com/foundation-model-stack/fms-extras
cd fms-extras
pip install -e .
```


## Description

This model is intended to be used as an accelerator for [llama3 70b (instruct)](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) and takes inspiration 
from the Medusa speculative decoding architecture. It is also applicable for [llama3.1 70b (instruct)](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct).
This accelerator modifies the MLP into a multi-stage MLP, where each stage predicts 
a single token in the draft based on both a state vector and sampled token
from the prior stage (the base model can be considered stage 0).
The state vector from the base model provides contextual information to the accelerator, 
while conditioning on prior sampled tokens allows it to produce higher-quality draft n-grams.

Note: The underlying MLP speculator is a generic architecture that can be trained with any generative model to accelerate inference. 
Training is light-weight and can be completed in only a few days depending on base model size and speed.

## Repository Links

1. [Paged Attention KV-Cache / Speculator](https://github.com/foundation-model-stack/fms-extras)
2. [Production Server with speculative decoding](https://github.com/IBM/text-generation-inference.git)
3. [Speculator training](https://github.com/foundation-model-stack/fms-fsdp/pull/35)

## Samples

_Note: For all samples, your environment must have access to cuda_

### Use in IBM Production TGIS

*To try this out running in a production-like environment, please use the pre-built docker image:*

#### Setup

```bash
HF_HUB_CACHE=/hf_hub_cache
chmod a+w $HF_HUB_CACHE
HF_HUB_TOKEN="your huggingface hub token"
TGIS_IMAGE=quay.io/wxpe/text-gen-server:main.ddc56ee

docker pull $TGIS_IMAGE

# optionally download llama3-70b-instruct if the weights do not already exist
docker run --rm \
    -v $HF_HUB_CACHE:/models \
    -e HF_HUB_CACHE=/models \
    -e TRANSFORMERS_CACHE=/models \
    $TGIS_IMAGE \
    text-generation-server download-weights \
    meta-llama/Meta-Llama-3-70B-Instruct \
    --token $HF_HUB_TOKEN

# optionally download the speculator model if the weights do not already exist
docker run --rm \
    -v $HF_HUB_CACHE:/models \
    -e HF_HUB_CACHE=/models \
    -e TRANSFORMERS_CACHE=/models \
    $TGIS_IMAGE \
    text-generation-server download-weights \
    ibm-fms/llama3-70b-accelerator \
    --token $HF_HUB_TOKEN

# note: if the weights were downloaded separately (not with the above commands), please place them in the HF_HUB_CACHE directory and refer to them with /models/<model_name>
docker run -d --rm --gpus all \
    --name my-tgis-server \
    -p 8033:8033 \
    -v $HF_HUB_CACHE:/models \
    -e HF_HUB_CACHE=/models \
    -e TRANSFORMERS_CACHE=/models \
    -e MODEL_NAME=meta-llama/Meta-Llama-3-70B-Instruct \
    -e SPECULATOR_NAME=ibm-fms/llama3-70b-accelerator \
    -e FLASH_ATTENTION=true \
    -e PAGED_ATTENTION=true \
    -e DTYPE=float16 \
    $TGIS_IMAGE

# check logs and wait for "gRPC server started on port 8033" and "HTTP server started on port 3000"
docker logs my-tgis-server -f

# get the client sample (Note: The first prompt will take longer as there is a warmup time)
conda create -n tgis-client-env python=3.11
conda activate tgis-client-env
git clone --branch main --single-branch https://github.com/IBM/text-generation-inference.git
cd text-generation-inference/integration_tests
make gen-client
pip install . --no-cache-dir
```

#### Run Sample

```bash
python sample_client.py
```

_Note: first prompt may be slower as there is a slight warmup time_

### Use in Huggingface TGI

#### start the server

```bash
model=ibm-fms/llama3-70b-accelerator
volume=$PWD/data # share a volume with the Docker container to avoid downloading weights every run

docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data ghcr.io/huggingface/text-generation-inference:latest --model-id $model
```

_note: for tensor parallel, add --num-shard_

#### make a request

```bash
curl 127.0.0.1:8080/generate_stream \
    -X POST \
    -d '{"inputs":"What is Deep Learning?","parameters":{"max_new_tokens":20}}' \
    -H 'Content-Type: application/json'
```

### Use in vLLM
```from vllm import LLM, SamplingParams

# Sample prompts.
prompts = [
    "The president of the United States is",
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.0)

# Create an LLM.
llm = LLM(
    model="/path/to/Meta-Llama-3-70B-Instruct",
    tensor_parallel_size=4,
    speculative_model="/path/to/llama3-70b-accelerator",
    speculative_draft_tensor_parallel_size=1,
    use_v2_block_manager=True,
)
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```