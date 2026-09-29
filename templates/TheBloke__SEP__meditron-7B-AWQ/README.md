---
base_model: epfl-llm/meditron-7b
datasets:
- epfl-llm/guidelines
inference: false
language:
- en
license: llama2
metrics:
- accuracy
- perplexity
model_creator: EPFL LLM Team
model_name: Meditron 7B
model_type: llama
prompt_template: '<|im_start|>system

  {system_message}<|im_end|>

  <|im_start|>user

  {prompt}<|im_end|>

  <|im_start|>assistant

  '
quantized_by: TheBloke
---
<!-- markdownlint-disable MD041 -->

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://discord.gg/theblokeai">Chat & support: TheBloke's Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<div style="text-align:center; margin-top: 0em; margin-bottom: 0em"><p style="margin-top: 0.25em; margin-bottom: 0em;">TheBloke's LLM work is generously supported by a grant from <a href="https://a16z.com">andreessen horowitz (a16z)</a></p></div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Meditron 7B - AWQ
- Model creator: [EPFL LLM Team](https://huggingface.co/epfl-llm)
- Original model: [Meditron 7B](https://huggingface.co/epfl-llm/meditron-7b)

<!-- description start -->
## Description

This repo contains AWQ model files for [EPFL LLM Team's Meditron 7B](https://huggingface.co/epfl-llm/meditron-7b).

These files were quantised using hardware kindly provided by [Massed Compute](https://massedcompute.com/).


### About AWQ

AWQ is an efficient, accurate and blazing-fast low-bit weight quantization method, currently supporting 4-bit quantization. Compared to GPTQ, it offers faster Transformers-based inference with equivalent or better quality compared to the most commonly used GPTQ settings.

It is supported by:

- [Text Generation Webui](https://github.com/oobabooga/text-generation-webui) - using Loader: AutoAWQ
- [vLLM](https://github.com/vllm-project/vllm) - Llama and Mistral models only
- [Hugging Face Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference)
- [Transformers](https://huggingface.co/docs/transformers) version 4.35.0 and later, from any code or client that supports Transformers
- [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) - for use from Python code

<!-- description end -->
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/meditron-7B-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/meditron-7B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/meditron-7B-GGUF)
* [EPFL LLM Team's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/epfl-llm/meditron-7b)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: ChatML

```
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

<!-- prompt-template end -->


<!-- README_AWQ.md-provided-files start -->
## Provided files, and AWQ parameters

I currently release 128g GEMM models only. The addition of group_size 32 models, and GEMV kernel models, is being actively considered.

Models are released as sharded safetensors files.

| Branch | Bits | GS | AWQ Dataset | Seq Len | Size |
| ------ | ---- | -- | ----------- | ------- | ---- |
| [main](https://huggingface.co/TheBloke/meditron-7B-AWQ/tree/main) | 4 | 128 | [Medical Medaow WikiDoc](https://huggingface.co/datasets/medalpaca/medical_meadow_wikidoc/viewer/) | 4096 | 3.89 GB

<!-- README_AWQ.md-provided-files end -->

<!-- README_AWQ.md-text-generation-webui start -->
## How to easily download and use this model in [text-generation-webui](https://github.com/oobabooga/text-generation-webui)

Please make sure you're using the latest version of [text-generation-webui](https://github.com/oobabooga/text-generation-webui).

It is strongly recommended to use the text-generation-webui one-click-installers unless you're sure you know how to make a manual install.

1. Click the **Model tab**.
2. Under **Download custom model or LoRA**, enter `TheBloke/meditron-7B-AWQ`.
3. Click **Download**.
4. The model will start downloading. Once it's finished it will say "Done".
5. In the top left, click the refresh icon next to **Model**.
6. In the **Model** dropdown, choose the model you just downloaded: `meditron-7B-AWQ`
7. Select **Loader: AutoAWQ**.
8. Click Load, and the model will load and is now ready for use.
9. If you want any custom settings, set them and then click **Save settings for this model** followed by **Reload the Model** in the top right.
10. Once you're ready, click the **Text Generation** tab and enter a prompt to get started!
<!-- README_AWQ.md-text-generation-webui end -->

<!-- README_AWQ.md-use-from-vllm start -->
## Multi-user inference server: vLLM

Documentation on installing and using vLLM [can be found here](https://vllm.readthedocs.io/en/latest/).

- Please ensure you are using vLLM version 0.2 or later.
- When using vLLM as a server, pass the `--quantization awq` parameter.

For example:

```shell
python3 -m vllm.entrypoints.api_server --model TheBloke/meditron-7B-AWQ --quantization awq --dtype auto
```

- When using vLLM from Python code, again set `quantization=awq`.

For example:

```python
from vllm import LLM, SamplingParams

prompts = [
    "Tell me about AI",
    "Write a story about llamas",
    "What is 291 - 150?",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
]
prompt_template=f'''<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
'''

prompts = [prompt_template.format(prompt=prompt) for prompt in prompts]

sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="TheBloke/meditron-7B-AWQ", quantization="awq", dtype="auto")

outputs = llm.generate(prompts, sampling_params)

# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```
<!-- README_AWQ.md-use-from-vllm start -->

<!-- README_AWQ.md-use-from-tgi start -->
## Multi-user inference server: Hugging Face Text Generation Inference (TGI)

Use TGI version 1.1.0 or later. The official Docker container is: `ghcr.io/huggingface/text-generation-inference:1.1.0`

Example Docker parameters:

```shell
--model-id TheBloke/meditron-7B-AWQ --port 3000 --quantize awq --max-input-length 3696 --max-total-tokens 4096 --max-batch-prefill-tokens 4096
```

Example Python code for interfacing with TGI (requires [huggingface-hub](https://github.com/huggingface/huggingface_hub) 0.17.0 or later):

```shell
pip3 install huggingface-hub
```

```python
from huggingface_hub import InferenceClient

endpoint_url = "https://your-endpoint-url-here"

prompt = "Tell me about AI"
prompt_template=f'''<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
'''

client = InferenceClient(endpoint_url)
response = client.text_generation(prompt,
                                  max_new_tokens=128,
                                  do_sample=True,
                                  temperature=0.7,
                                  top_p=0.95,
                                  top_k=40,
                                  repetition_penalty=1.1)

print(f"Model output: ", response)
```
<!-- README_AWQ.md-use-from-tgi end -->

<!-- README_AWQ.md-use-from-python start -->
## Inference from Python code using Transformers

### Install the necessary packages

- Requires: [Transformers](https://huggingface.co/docs/transformers) 4.35.0 or later.
- Requires: [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) 0.1.6 or later.

```shell
pip3 install --upgrade "autoawq>=0.1.6" "transformers>=4.35.0"
```

Note that if you are using PyTorch 2.0.1, the above AutoAWQ command will automatically upgrade you to PyTorch 2.1.0.

If you are using CUDA 11.8 and wish to continue using PyTorch 2.0.1, instead run this command:

```shell
pip3 install https://github.com/casper-hansen/AutoAWQ/releases/download/v0.1.6/autoawq-0.1.6+cu118-cp310-cp310-linux_x86_64.whl
```

If you have problems installing [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) using the pre-built wheels, install it from source instead:

```shell
pip3 uninstall -y autoawq
git clone https://github.com/casper-hansen/AutoAWQ
cd AutoAWQ
pip3 install .
```

### Transformers example code (requires Transformers 4.35.0 and later)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_name_or_path = "TheBloke/meditron-7B-AWQ"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path,
    low_cpu_mem_usage=True,
    device_map="cuda:0"
)

# Using the text streamer to stream output one token at a time
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

prompt = "Tell me about AI"
prompt_template=f'''<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
'''

# Convert prompt to tokens
tokens = tokenizer(
    prompt_template,
    return_tensors='pt'
).input_ids.cuda()

generation_params = {
    "do_sample": True,
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_new_tokens": 512,
    "repetition_penalty": 1.1
}

# Generate streamed output, visible one token at a time
generation_output = model.generate(
    tokens,
    streamer=streamer,
    **generation_params
)

# Generation without a streamer, which will include the prompt in the output
generation_output = model.generate(
    tokens,
    **generation_params
)

# Get the tokens from the output, decode them, print them
token_output = generation_output[0]
text_output = tokenizer.decode(token_output)
print("model.generate output: ", text_output)

# Inference is also possible via Transformers' pipeline
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    **generation_params
)

pipe_output = pipe(prompt_template)[0]['generated_text']
print("pipeline output: ", pipe_output)

```
<!-- README_AWQ.md-use-from-python end -->

<!-- README_AWQ.md-compatibility start -->
## Compatibility

The files provided are tested to work with:

- [text-generation-webui](https://github.com/oobabooga/text-generation-webui) using `Loader: AutoAWQ`.
- [vLLM](https://github.com/vllm-project/vllm) version 0.2.0 and later.
- [Hugging Face Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference) version 1.1.0 and later.
- [Transformers](https://huggingface.co/docs/transformers) version 4.35.0 and later.
- [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) version 0.1.1 and later.

<!-- README_AWQ.md-compatibility end -->

<!-- footer start -->
<!-- 200823 -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/theblokeai)

## Thanks, and how to contribute

Thanks to the [chirper.ai](https://chirper.ai) team!

Thanks to Clay from [gpus.llm-utils.org](llm-utils)!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Special thanks to**: Aemon Algiz.

**Patreon special mentions**: Brandon Frisco, LangChain4j, Spiking Neurons AB, transmissions 11, Joseph William Delisle, Nitin Borwankar, Willem Michiel, Michael Dempsey, vamX, Jeffrey Morgan, zynix, jjj, Omer Bin Jawed, Sean Connelly, jinyuan sun, Jeromy Smith, Shadi, Pawan Osman, Chadd, Elijah Stavena, Illia Dulskyi, Sebastain Graf, Stephen Murray, terasurfer, Edmond Seymore, Celu Ramasamy, Mandus, Alex, biorpg, Ajan Kanaga, Clay Pascal, Raven Klaugh, 阿明, K, ya boyyy, usrbinkat, Alicia Loh, John Villwock, ReadyPlayerEmma, Chris Smitley, Cap'n Zoog, fincy, GodLy, S_X, sidney chen, Cory Kujawski, OG, Mano Prime, AzureBlack, Pieter, Kalila, Spencer Kim, Tom X Nguyen, Stanislav Ovsiannikov, Michael Levine, Andrey, Trailburnt, Vadim, Enrico Ros, Talal Aujan, Brandon Phillips, Jack West, Eugene Pentland, Michael Davis, Will Dee, webtim, Jonathan Leane, Alps Aficionado, Rooh Singh, Tiffany J. Kim, theTransient, Luke @flexchar, Elle, Caitlyn Gatomon, Ari Malik, subjectnull, Johann-Peter Hartmann, Trenton Dambrowitz, Imad Khwaja, Asp the Wyvern, Emad Mostaque, Rainer Wilmers, Alexandros Triantafyllidis, Nicholas, Pedro Madruga, SuperWojo, Harry Royden McLaughlin, James Bentley, Olakabola, David Ziegler, Ai Maven, Jeff Scroggin, Nikolai Manek, Deo Leter, Matthew Berman, Fen Risland, Ken Nordquist, Manuel Alberto Morcote, Luke Pendergrass, TL, Fred von Graf, Randy H, Dan Guido, NimbleBox.ai, Vitor Caleffi, Gabriel Tamborski, knownsqashed, Lone Striker, Erik Bjäreholt, John Detwiler, Leonard Tan, Iucharbius


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

# Original model card: EPFL LLM Team's Meditron 7B

<img width=50% src="meditron_LOGO.png" alt="Alt text" title="Meditron-logo">

# Model Card for Meditron-7B-v1.0
Meditron is a suite of open-source medical Large Language Models (LLMs).
Meditron-7B is a 7 billion parameters model adapted to the medical domain from Llama-2-7B through continued pretraining on a comprehensively curated medical corpus, including selected PubMed articles, abstracts, a [new dataset](https://huggingface.co/datasets/epfl-llm/guidelines) of internationally-recognized medical guidelines, and general domain data from [RedPajama-v1](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T).
Meditron-7B, finetuned on relevant training data, outperforms Llama-2-7B and PMC-Llama on multiple medical reasoning tasks.

<details open>
  <summary><strong>Advisory Notice</strong></summary>

  <blockquote style="padding: 10px; margin: 0 0 10px; border-left: 5px solid #ddd;">
    While Meditron is designed to encode medical knowledge from sources of high-quality evidence, it is not yet adapted to deliver this knowledge appropriately, safely, or within professional actionable constraints. 
  We recommend against deploying Meditron in medical applications without extensive use-case alignment, as well as additional testing, specifically including randomized controlled trials in real-world practice settings.
  </blockquote>
</details>

## Model Details

- **Developed by:** [EPFL LLM Team](https://huggingface.co/epfl-llm)
- **Model type:** Causal decoder-only transformer language model
- **Language(s):** English (mainly)
- **Model License:** [LLAMA 2 COMMUNITY LICENSE AGREEMENT](https://huggingface.co/meta-llama/Llama-2-70b/raw/main/LICENSE.txt)
- **Code License:** [APACHE 2.0 LICENSE](LICENSE)
- **Continue-pretrained from model:** [Llama-2-7B](https://huggingface.co/meta-llama/Llama-2-7b)
- **Context length:**  2K tokens
- **Input:**  Text-only data
- **Output:**  Model generates text only
- **Status:** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we enhance model's performance.
- **Knowledge Cutoff:** August 2023


### Model Sources

- **Repository:** [epflLLM/meditron](https://github.com/epfLLM/meditron)
- **Trainer:** [epflLLM/Megatron-LLM](https://github.com/epfLLM/Megatron-LLM)
- **Paper:** *[MediTron-70B: Scaling Medical Pretraining for Large Language Models](https://arxiv.org/abs/2311.16079)*

## Uses

Meditron-7B is being made available for further testing and assessment as an AI assistant to enhance clinical decision-making and enhance access to an LLM for healthcare use. Potential use cases may include but are not limited to:
-  Medical exam question answering
-  Supporting differential diagnosis
-  Disease information (symptoms, cause, treatment) query
-  General health information query

### Direct Use

It is possible to use this model to generate text, which is useful for experimentation and understanding its capabilities. 
It should not be used directly for production or work that may impact people.

### Downstream Use
Meditron-7B is a foundation model that can be finetuned, instruction-tuned, or RLHF-tuned for specific downstream tasks and applications.
The main way we have used this model is finetuning for downstream question-answering tasks, but we encourage using this model for additional applications.

Specific formatting needs to be followed to prompt our finetuned models, including the  `<|im_start|>`, `<|im_end|>` tags, and  `system`, `question`, `answer`  identifiers.
    
    """
    <|im_start|>system
    {system_message}<|im_end|>
    <|im_start|>question
    {prompt}<|im_end|>
    <|im_start|>answer  
    """
**Note 1**: The above formatting is not required for running the base model (this repository)

**Note 2**: the above formatting is just an example of a finetuning template. This format is not a requirement if you use your own formatting option for the finetuning of the model.

To run proper generation with this base model, we recommend using a high-throughput and memory-efficient inference engine, such as [vLLM](https://github.com/vllm-project/vllm), with a UI that supports chat and text generation, such as [BetterChatGPT](https://github.com/ztjhz/BetterChatGPT)
To see more details about model deployment and generation, please see our [documentation](https://github.com/epfLLM/meditron/blob/main/deployment/README.md).

### Out-of-Scope Use

We do not recommend using this model for natural language generation in a production environment, finetuned or otherwise.

## Truthfulness, Helpfulness, Risk, and Bias

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

We did an initial assessment of Meditron models' **Truthfulness** against baseline models and consumer-level medical models. 
We use TruthfulQA (multiple choice) as the main evaluation benchmark.
We only focus on the categories that are relevant to the medical domain, including Health, Nutrition, Psychology, and Science.
For 7B models, we perform one-shot evaluations for consistent answer generation.
For 70B models, the evaluations are under the zero-shot setting.
Below, we report the detailed truthfulness performance of each category.

|     |        |      |      |      |      |      |      |
| --- | ------ |----- |----- |----- |----- |----- |----- |
|Category  | meditron-70b | llama-2-70b | med42-70b* | meditron-7b | llama-2-7b | PMC-llama-7b |
|Health    |      81.8    |    69.1     |    83.6    | 27.3        |   16.4     |      3.6     |
|Nutrition |      77.9    |    68.8     |    62.5    | 31.1        |   12.5     |      6.3     |
|Psychology|      47.4    |    36.8     |    52.6    | 21.1        |   10.5     |      0.0     |
|Science   |      77.8    |    44.4     |    33.3    | 33.3        |   11.1     |      0.0     |
|Avg       |      71.2    |    54.8     |    58.0    | 28.3        |   12.6     |      2.5     |
|          |              |             |            |             |            |              |

For a more detailed performance analysis, please see our paper. 

Significant research is still required to fully explore potential bias, fairness, and safety issues with this language model. 
Please recognize that our evaluation on Meditron-7B's helpfulness, risk, and bias are highly limited. 
Thus, as we noted in the safety notice, we strongly against any deployment in medical applications without further alignment process and rigorous evaluation!

### Recommendations

**IMPORTANT!**
Users (both direct and downstream) should be made aware of the risks, biases, and limitations of the model.
While this model is capable of generating natural language text, we have only begun to explore this capability and its limitations. 
Understanding these limitations is especially important in a domain like medicine. 
Therefore, we strongly recommend against using this model in production for natural language generation or for professional purposes related to health and medicine.

## Training Details

### Training Data
Meditron’s domain-adaptive pre-training corpus GAP-Replay  combines 48.1B tokens from four corpora:
- [**Clinical  Guidelines**](https://huggingface.co/datasets/epfl-llm/guidelines): a new dataset of 46K internationally-recognized clinical practice guidelines from various healthcare-related sources, including hospitals and international organizations.
- **Medical Paper Abstracts**: 16.1M abstracts extracted from closed-access PubMed and PubMed Central papers.
- **Medical Papers**: full-text articles extracted from 5M publicly available PubMed and PubMed Central papers.
- **Replay Data**: 400M tokens of general domain pretraining data sampled from [RedPajama-v1](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)

<img width=75% src="gap-replay.png" alt="Alt text" title="Meditron-logo">

#### Data Preprocessing

Please see the detailed preprocessing procedure in our paper. 

### Training Procedure 

We used the [Megatron-LLM](https://github.com/epfLLM/Megatron-LLM) distributed training library, a derivative of Nvidia's Megatron LM project, to optimize training efficiency. 
Hardware consists of 1 node of 8x NVIDIA A100 (80GB) SXM GPUs connected by NVLink and NVSwitch with a single Nvidia ConnectX-6 DX network card and equipped with 2 x AMD EPYC 7543 32-Core Processors and 512 GB of RAM. 

Our three way parallelism scheme uses:
 - Data Parallelism (DP -- different GPUs process different subsets of the batches) of 2,
 - Pipeline Parallelism (PP -- different GPUs process different layers) of 4,
 - Tensor Parallelism (TP -- different GPUs process different subtensors for matrix multiplication) of 1.
   

#### Training Hyperparameters

|  |  |
| --- | ------ |
| bf16 | true |
| lr  | 3e-4 |
| eps | 1e-5       |
| betas | \[0.9, 0.95\] |
| clip_grad | 1 |
| weight decay | 0.1 |
| DP size | 16 |
| TP size | 4 |
| PP size | 1 |
| seq length | 2048 |
| lr scheduler | cosine|
| min lr | 1e-6 |
| warmup iteration | 2000 |
| micro batch size | 10 |
| global batch size | 1600 |
|  |  |

#### Sizes
The model was trained in September 2023.

The model architecture is exactly Llama 2, meaning

|     |        |
| --- | ------ |
| Model size           | 7B   |
| Hidden dimension     | 4096 |
| Num. attention heads |   32 |
| Num. layers          |   32 |
|  |  |

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data & Metrics

#### Testing Data
- [MedQA (USMLE)](https://huggingface.co/datasets/bigbio/med_qa)
- [MedMCQA](https://huggingface.co/datasets/medmcqa)
- [PubMedQA](https://huggingface.co/datasets/bigbio/pubmed_qa)
- [MMLU-Medical](https://huggingface.co/datasets/lukaemon/mmlu)
- [MedQA-4-Option](https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options)

#### Metrics
- Accuracy: suite the evaluation of multiple-choice question-answering tasks.

### Results
We finetune meditron-7b, llama-2-7b, pmc-llama-7b on each benchmark (pubmedqa, medmcqa, medqa)'s training data individually. 
We report the finetuned models' performance with top token selection as the inference mode.
For MMLU-Medical, models finetuned on MedMCQA are used for inference.
For MedQA-4-Option, models finetuned on MedQA are used for inference.
For a more detailed performance analysis, please see our paper. 

|     |        |      |      |      |      |
| --- | ------ |----- |----- |----- |----- |
|Dataset       | meditron-7b | llama-2-7b  | pmc-llama-7b | Zephyr-7B-beta* | Mistral-7B-instruct* |
|MMLU-Medical  | 54.2        |    53.7     |    56.4      |      63.3       |        60.0          |
|PubMedQA      | 74.4        |    61.8     |    59.2      |      46.0       |        17.8          |
|MedMCQA       | 59.2        |    54.4     |    57.6      |      43.0       |        40.2          |
|MedQA         | 47.9        |    44.0     |    42.4      |      42.8       |        32.4          |
|MedQA-4-Option| 52.0        |    49.6     |    49.2      |      48.5       |        41.1          |
|Avg           | 57.5        |    52.7     |    53.0      |      48.7       |        38.3          |
|              |             |             |              |                 |                      |

**Note**: models with * are already instruction-tuned, so we exclude them from further finetuning on any training data.


## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

- **Hardware Type:** 8 x NVIDIA A100 (80GB) SXM
- **Total GPU hours:** 588.8
- **Hardware Provider:** EPFL Research Computing Platform
- **Compute Region:** Switzerland
- **Carbon Emitted:** Switzerland has a carbon efficiency of 0.016 kgCO2/kWh (https://www.carbonfootprint.com/docs/2018_8_electricity_factors_august_2018_-_online_sources.pdf). 73.6 hours of 8 A100s means 588.8 hours at a TDP of 400W. Assuming a Power Usage effectiveness of 1.5, total emissions are estimated to be: 
    
   (400W / 1000W/kWh / GPU * 0.016 kgCO2/kWh * 73.6 h * 8 GPU) * 1.8 PUE = 6.8 kgCO2.

## Citation

**BibTeX:**
If you use Meditron or its training data, please cite our work:

```
@misc{chen2023meditron70b,
      title={MEDITRON-70B: Scaling Medical Pretraining for Large Language Models}, 
      author={Zeming Chen and Alejandro Hernández-Cano and Angelika Romanou and Antoine Bonnet and Kyle Matoba and Francesco Salvi and Matteo Pagliardini and Simin Fan and Andreas Köpf and Amirkeivan Mohtashami and Alexandre Sallinen and Alireza Sakhaeirad and Vinitra Swamy and Igor Krawczuk and Deniz Bayazit and Axel Marmet and Syrielle Montariol and Mary-Anne Hartley and Martin Jaggi and Antoine Bosselut},
      year={2023},
      eprint={2311.16079},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@software{epfmedtrn,
  author = {Zeming Chen and Alejandro Hernández-Cano and Angelika Romanou and Antoine Bonnet and Kyle Matoba and Francesco Salvi and Matteo Pagliardini and Simin Fan and Andreas Köpf and Amirkeivan Mohtashami and Alexandre Sallinen and Alireza Sakhaeirad and Vinitra Swamy and Igor Krawczuk and Deniz Bayazit and Axel Marmet and Syrielle Montariol and Mary-Anne Hartley and Martin Jaggi and Antoine Bosselut},
  title = {MediTron-70B: Scaling Medical Pretraining for Large Language Models},
  month = November,
  year = 2023,
  url = {https://github.com/epfLLM/meditron}
}
```
