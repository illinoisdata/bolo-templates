---
language:
- en
- vi
- zh
base_model:
- google/gemma-2-9b-it
- dangvansam/gemma-2-9b-it-fix-system-role
pipeline_tag: text-generation
tags:
- vllm
- system-role
- langchain
- awq
- gemma2
- gemma
- AWQ
license: gemma
---

# gemma-2-9b-it-fix-system-role-awq

Modified and 4 bit quantized version of [gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) and update **`chat_template`** for support **`system`** role to handle cases:
- `Conversation roles must alternate user/assistant/user/assistant/...`
- `System role not supported`

## Model Overview
- **Model Architecture:** Gemma 2
  - **Input:** Text
  - **Output:** Text
- **Release Date:** 04/12/2024
- **Version:** 1.0
- **Quantiz method:** 4 bit [AutoAWQ](https://github.com/casper-hansen/AutoAWQ)

## Deployment

### Use with vLLM

This model can be deployed efficiently using the [vLLM](https://docs.vllm.ai/en/latest/) backend, as shown in the example below.

With CLI:
```bash
vllm serve --model dangvansam/gemma-2-9b-it-fix-system-role-awq
```

vLLM also supports OpenAI-compatible serving. See the [documentation](https://docs.vllm.ai/en/latest/) for more details.
```bash
curl http://localhost:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "model": "dangvansam/gemma-2-9b-it-fix-system-role-awq",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who are you?"}
  ]
}'
```

With Python:
```python
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model_id = "dangvansam/gemma-2-9b-it-fix-system-role-awq"

sampling_params = SamplingParams(temperature=0.6, top_p=0.9, max_tokens=256)

tokenizer = AutoTokenizer.from_pretrained(model_id)

messages = [
  {"role": "system", "content": "You are helpfull assistant."},
  {"role": "user", "content": "Who are you?"}
]

prompts = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

llm = LLM(model=model_id)

outputs = llm.generate(prompts, sampling_params)

generated_text = outputs[0].outputs[0].text
print(generated_text)
```

With docker:
```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=<secret>" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model dangvansam/gemma-2-9b-it-fix-system-role-awq
```

With docker-compose:
```
services:
vllm:
  image: vllm/vllm-openai:latest
  restart: always
  shm_size: '48gb'
  volumes:
    - ~/.cache/huggingface:/root/.cache/huggingface
  entrypoint: python3
  command: -m vllm.entrypoints.openai.api_server --port=8000 --host=0.0.0.0 --model dangvansam/gemma-2-9b-it-fix-system-role-awq --gpu-memory-utilization 1.0 --max-model-len 4096
  healthcheck:
    test: [ "CMD", "curl", "-f", "http://0.0.0.0:8000/v1/models" ]
    interval: 30s
    timeout: 10s
    retries: 10
  deploy:
    resources:
      reservations:
        devices:
        - driver: nvidia
          device_ids: ['0']
          capabilities: [gpu]
  ports:
    - 8000:8000
```