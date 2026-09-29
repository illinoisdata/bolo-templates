---
base_model: mistralai/Mistral-Small-Instruct-2409
license: other
license_name: mrl
license_link: https://mistral.ai/licenses/MRL-0.1.md
tags:
- unsloth
- mistral
---

# Finetune Llama 3.1, Gemma 2, Mistral 2-5x faster with 70% less memory via Unsloth!

We have a free Google Colab Tesla T4 notebook for Mistral-Small-Instruct-2409 here: https://colab.research.google.com/drive/1Ys44kVvmeZtnICzWz0xgpRnrIOjZAuxp?usp=sharing

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/Discord%20button.png" width="200"/>](https://discord.gg/unsloth)
[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

## ✨ Finetune for Free

All notebooks are **beginner friendly**! Add your dataset, click "Run All", and you'll get a 2x faster finetuned model which can be exported to GGUF, vLLM or uploaded to Hugging Face.

| Unsloth supports          |    Free Notebooks                                                                                           | Performance | Memory use |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|-------------|----------|
| **Llama-3.2 (3B)**      | [▶️ Start on Colab](https://colab.research.google.com/drive/1Ys44kVvmeZtnICzWz0xgpRnrIOjZAuxp?usp=sharing)               | 2.4x faster | 58% less |
| **Llama-3.2 (11B vision)**      | [▶️ Start on Colab](https://colab.research.google.com/drive/1j0N4XTY1zXXy7mPAhOC1_gMYZ2F2EBlk?usp=sharing)               | 2x faster | 60% less |
| **Llama-3.1 (8B)**      | [▶️ Start on Colab](https://colab.research.google.com/drive/1Ys44kVvmeZtnICzWz0xgpRnrIOjZAuxp?usp=sharing)               | 2.4x faster | 58% less |
| **Qwen2 VL (7B)**      | [▶️ Start on Colab](https://colab.research.google.com/drive/1whHb54GNZMrNxIsi2wm2EY_-Pvo2QyKh?usp=sharing)               | 1.8x faster | 60% less |
| **Qwen2.5 (7B)**      | [▶️ Start on Colab](https://colab.research.google.com/drive/1Kose-ucXO1IBaZq5BvbwWieuubP7hxvQ?usp=sharing)               | 2x faster | 60% less |
| **Phi-3.5 (mini)** | [▶️ Start on Colab](https://colab.research.google.com/drive/1lN6hPQveB_mHSnTOYifygFcrO8C1bxq4?usp=sharing)               | 2x faster | 50% less |
| **Gemma 2 (9B)**      | [▶️ Start on Colab](https://colab.research.google.com/drive/1vIrqH5uYDQwsJ4-OO3DErvuv4pBgVwk4?usp=sharing)               | 2.4x faster | 58% less |
| **Mistral (7B)**    | [▶️ Start on Colab](https://colab.research.google.com/drive/1Dyauq4kTZoLewQ1cApceUQVNcnnNTzg_?usp=sharing)               | 2.2x faster | 62% less |
| **DPO - Zephyr**     | [▶️ Start on Colab](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP?usp=sharing)               | 1.9x faster | 19% less |

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/images/documentation%20green%20button.png" width="200"/>](https://docs.unsloth.ai)


- This [conversational notebook](https://colab.research.google.com/drive/1Aau3lgPzeZKQ-98h69CCu1UJcvIBLmy2?usp=sharing) is useful for ShareGPT ChatML / Vicuna templates.
- This [text completion notebook](https://colab.research.google.com/drive/1ef-tab5bhkvWmBOObepl1WgJvfvSzn5Q?usp=sharing) is for raw text. This [DPO notebook](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP?usp=sharing) replicates Zephyr.
- \* Kaggle has 2x T4s, but we use 1. Due to overhead, 1x T4 is 5x faster.


# Model Card for Mistral-Small-Instruct-2409

Mistral-Small-Instruct-2409 is an instruct fine-tuned version with the following characteristics:

- 22B parameters
- Vocabulary to 32768
- Supports function calling
- 128k sequence length

  
## Usage Examples

### vLLM (recommended)

We recommend using this model with the [vLLM library](https://github.com/vllm-project/vllm)
to implement production-ready inference pipelines.

**_Installation_**

Make sure you install `vLLM >= v0.6.1.post1`:

```
pip install --upgrade vllm
```

Also make sure you have `mistral_common >= 1.4.1` installed:

```
pip install --upgrade mistral_common
```

You can also make use of a ready-to-go [docker image](https://hub.docker.com/layers/vllm/vllm-openai/latest/images/sha256-de9032a92ffea7b5c007dad80b38fd44aac11eddc31c435f8e52f3b7404bbf39?context=explore).


**_Offline_**

```py
from vllm import LLM
from vllm.sampling_params import SamplingParams

model_name = "mistralai/Mistral-Small-Instruct-2409"

sampling_params = SamplingParams(max_tokens=8192)

# note that running Mistral-Small on a single GPU requires at least 44 GB of GPU RAM
# If you want to divide the GPU requirement over multiple devices, please add *e.g.* `tensor_parallel=2`
llm = LLM(model=model_name, tokenizer_mode="mistral", config_format="mistral", load_format="mistral")

prompt = "How often does the letter r occur in Mistral?"

messages = [
    {
        "role": "user",
        "content": prompt
    },
]

outputs = llm.chat(messages, sampling_params=sampling_params)

print(outputs[0].outputs[0].text)
```

**_Server_**

You can also use Mistral Small in a server/client setting. 

1. Spin up a server:


```
vllm serve mistralai/Mistral-Small-Instruct-2409 --tokenizer_mode mistral --config_format mistral --load_format mistral
```

**Note:** Running Mistral-Small on a single GPU requires at least 44 GB of GPU RAM. 

If you want to divide the GPU requirement over multiple devices, please add *e.g.* `--tensor_parallel=2`

2. And ping the client:

```
curl --location 'http://<your-node-url>:8000/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer token' \
--data '{
    "model": "mistralai/Mistral-Small-Instruct-2409",
    "messages": [
      {
        "role": "user",
        "content": "How often does the letter r occur in Mistral?"
      }
    ]
}'

```

### Mistral-inference

We recommend using [mistral-inference](https://github.com/mistralai/mistral-inference) to quickly try out / "vibe-check" the model.


**_Install_**

Make sure to have `mistral_inference >= 1.4.1` installed.

```
pip install mistral_inference --upgrade
```

**_Download_**

```py
from huggingface_hub import snapshot_download
from pathlib import Path

mistral_models_path = Path.home().joinpath('mistral_models', '22B-Instruct-Small')
mistral_models_path.mkdir(parents=True, exist_ok=True)

snapshot_download(repo_id="mistralai/Mistral-Small-Instruct-2409", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_models_path)
```

### Chat

After installing `mistral_inference`, a `mistral-chat` CLI command should be available in your environment. You can chat with the model using

```
mistral-chat $HOME/mistral_models/22B-Instruct-Small --instruct --max_tokens 256
```

### Instruct following

```py
from mistral_inference.transformer import Transformer
from mistral_inference.generate import generate

from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest


tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tokenizer.model.v3")
model = Transformer.from_folder(mistral_models_path)

completion_request = ChatCompletionRequest(messages=[UserMessage(content="How often does the letter r occur in Mistral?")])

tokens = tokenizer.encode_chat_completion(completion_request).tokens

out_tokens, _ = generate([tokens], model, max_tokens=64, temperature=0.0, eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id)
result = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])

print(result)
```

### Function calling

```py
from mistral_common.protocol.instruct.tool_calls import Function, Tool
from mistral_inference.transformer import Transformer
from mistral_inference.generate import generate

from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest


tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tokenizer.model.v3")
model = Transformer.from_folder(mistral_models_path)

completion_request = ChatCompletionRequest(
    tools=[
        Tool(
            function=Function(
                name="get_current_weather",
                description="Get the current weather",
                parameters={
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "format": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit to use. Infer this from the users location.",
                        },
                    },
                    "required": ["location", "format"],
                },
            )
        )
    ],
    messages=[
        UserMessage(content="What's the weather like today in Paris?"),
        ],
)

tokens = tokenizer.encode_chat_completion(completion_request).tokens

out_tokens, _ = generate([tokens], model, max_tokens=64, temperature=0.0, eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id)
result = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])

print(result)
```

### Usage in Hugging Face Transformers

You can also use Hugging Face `transformers` library to run inference using various chat templates, or fine-tune the model.
Example for inference:

```python
from transformers import LlamaTokenizerFast, MistralForCausalLM
import torch

device = "cuda"
tokenizer = LlamaTokenizerFast.from_pretrained('mistralai/Mistral-Small-Instruct-2409')
tokenizer.pad_token = tokenizer.eos_token

model = MistralForCausalLM.from_pretrained('mistralai/Mistral-Small-Instruct-2409', torch_dtype=torch.bfloat16)
model = model.to(device)

prompt = "How often does the letter r occur in Mistral?"

messages = [
    {"role": "user", "content": prompt},
 ]

model_input = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(device)
gen = model.generate(model_input, max_new_tokens=150)
dec = tokenizer.batch_decode(gen)
print(dec)
```

And you should obtain 
```text
<s>
  [INST]
  How often does the letter r occur in Mistral?
  [/INST]
  To determine how often the letter "r" occurs in the word "Mistral,"
  we can simply count the instances of "r" in the word.
  The word "Mistral" is broken down as follows:
    - M
    - i
    - s
    - t
    - r
    - a
    - l
  Counting the "r"s, we find that there is only one "r" in "Mistral."
  Therefore, the letter "r" occurs once in the word "Mistral."
</s>
```

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Alok Kothari, Antoine Roux, Arthur Mensch, Audrey Herblin-Stoop, Augustin Garreau, Austin Birky, Bam4d, Baptiste Bout, Baudouin de Monicault, Blanche Savary, Carole Rambaud, Caroline Feldman, Devendra Singh Chaplot, Diego de las Casas, Diogo Costa, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger, Gaspard Blanchet, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona, Henri Roussez, Hichem Sattouf, Ian Mack, Jean-Malo Delignon, Jessica Chudnovsky, Justus Murke, Kartik Khandelwal, Lawrence Stewart, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat, Marie Torelli, Marie-Anne Lachaux, Marjorie Janiewicz, Mickaël Seznec, Nicolas Schuhl, Niklas Muhs, Olivier de Garrigues, Patrick von Platen, Paul Jacob, Pauline Buche, Pavan Kumar Reddy, Perry Savas, Pierre Stock, Romain Sauvestre, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Sophia Yang, Szymon Antoniak, Teven Le Scao, Thibault Schueller, Thibaut Lavril, Thomas Wang, Théophile Gervet, Timothée Lacroix, Valera Nemychnikova, Wendy Shang, William El Sayed, William Marshall