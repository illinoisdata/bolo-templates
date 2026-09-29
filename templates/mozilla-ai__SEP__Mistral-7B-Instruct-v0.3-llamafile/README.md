---
license: apache-2.0
quantized_by: jartine
model_creator: mistralai
base_model: mistralai/Mistral-7B-Instruct-v0.3
prompt_template: |
  [INST] {{prompt}} [/INST]
tags:
- llamafile
---

# Mistral 7B Instruct v0.3 - llamafile

This repository contains executable weights (which we call
[llamafiles](https://github.com/Mozilla-Ocho/llamafile)) that run on
Linux, MacOS, Windows, FreeBSD, OpenBSD, and NetBSD for AMD64 and ARM64.

- Model creator: [MistralAI](https://hf.co/mistralai)
- Original model: [mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
- Base model: [mistralai/Mistral-7B-v0.3](https://huggingface.co/mistralai/Mistral-7B-v0.3)

The third edition of Mistral 7B was released on May 22th, 2024. It
increases the vocabulary size to 32768, supports the v3 tokenizer, and
introduces support for function calling.

*Software Last Updated: 2025-03-31*

*Llamafile Version: 0.9.2*

## Quickstart

Assuming your system has at least 16GB of RAM, you can try running the
following command which download, concatenate, and execute the model.

```
wget https://huggingface.co/Mozilla/Mistral-7B-Instruct-v0.3-llamafile/resolve/main/Mistral-7B-Instruct-v0.3.Q6_K.llamafile
chmod +x Mistral-7B-Instruct-v0.3.Q6_K.llamafile
./Mistral-7B-Instruct-v0.3.Q6_K.llamafile --help   # view manual
./Mistral-7B-Instruct-v0.3.Q6_K.llamafile          # launch web gui + oai api
./Mistral-7B-Instruct-v0.3.Q6_K.llamafile -p ...   # cli interface (scriptable)
```

Alternatively, you may download an official `llamafile` executable from
Mozilla Ocho on GitHub, in which case you can use the Granite llamafiles
as a simple weights data file.

```
llamafile -m Mistral-7B-Instruct-v0.3.Q6_K.llamafile ...
```

For further information, please see the [llamafile
README](https://github.com/mozilla-ocho/llamafile/).

Having **trouble?** See the ["Gotchas"
section](https://github.com/mozilla-ocho/llamafile/?tab=readme-ov-file#gotchas)
of the README.

## Prompting

Prompt template:

```
[INST] {{prompt}} [/INST]
```

Command template:

```
./Mistral-7B-Instruct-v0.3.Q6_K.llamafile -p "[INST]{{prompt}}[/INST]"
```

The maximum context size of this model is 32768 tokens. These llamafiles
use a default context size of 4096 tokens. Whenever you need the maximum
context size to be available with llamafile for any given model, you can
pass the `-c 0` flag. The default temperature for these llamafiles is
0.8 because it helps for this model. It can be tuned, e.g. `--temp 0`.

## Benchmarks

| hardware                                   | model\_filename                          | size       | test          | t/s             |
| :----------------------------------------- | :--------------------------------------- | ---------: | ------------: | --------------: |
| NVIDIA GeForce RTX 4090 (cuBLAS)           | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | pp512         | 7264.74         |
| NVIDIA GeForce RTX 4090 (cuBLAS)           | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | tg16          | 58.27           |
| NVIDIA GeForce RTX 4090 (cuBLAS)           | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | pp512         | 4236.95         |
| NVIDIA GeForce RTX 4090 (cuBLAS)           | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | tg16          | 114.65          |
| NVIDIA GeForce RTX 4090 (tinyBLAS)         | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | pp512         | 3457.31         |
| NVIDIA GeForce RTX 4090 (tinyBLAS)         | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | tg16          | 85.20           |
| NVIDIA GeForce RTX 4090 (tinyBLAS)         | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | pp512         | 1284.87         |
| NVIDIA GeForce RTX 4090 (tinyBLAS)         | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | tg16          | 49.76           |
| AMD Radeon RX 7900 XTX (hipBLAS)           | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | pp512         | 3239.27         |
| AMD Radeon RX 7900 XTX (hipBLAS)           | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | tg16          | 37.41           |
| AMD Radeon RX 7900 XTX (hipBLAS)           | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | pp512         | 2647.72         |
| AMD Radeon RX 7900 XTX (hipBLAS)           | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | tg16          | 85.42           |
| AMD Radeon RX 7900 XTX (tinyBLAS)          | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | pp512         | 1226.20         |
| AMD Radeon RX 7900 XTX (tinyBLAS)          | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | tg16          | 76.29           |
| AMD Radeon RX 7900 XTX (tinyBLAS)          | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | pp512         | 1033.91         |
| AMD Radeon RX 7900 XTX (tinyBLAS)          | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | tg16          | 35.41           |
| Apple M2 Ultra (60-core Metal GPU)         | mistral-7b-instruct-v0.3.Q6\_K           | 5.54 GiB   | pp512         | 761.88          |
| Apple M2 Ultra (60-core Metal GPU)         | mistral-7b-instruct-v0.3.Q6\_K           | 5.54 GiB   | tg16          | 64.15           |
| Apple M2 Ultra (ARMv8+fp16+dotprod)        | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | pp512         | 109.18          |
| Apple M2 Ultra (ARMv8+fp16+dotprod)        | Mistral-7B-Instruct-v0.3.F16             | 13.50 GiB  | tg16          | 15.17           |
| Intel Core i9-14900K (alderlake)           | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | pp512         | 95.87           |
| Intel Core i9-14900K (alderlake)           | Mistral-7B-Instruct-v0.3.Q6\_K           | 5.54 GiB   | tg16          | 12.66           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.BF16            | 13.50 GiB  | pp512         | 759.25          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.BF16            | 13.50 GiB  | tg16          | 19.29           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.F16             | 13.50 GiB  | pp512         | 559.94          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.F16             | 13.50 GiB  | tg16          | 19.26           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q8\_0           | 7.17 GiB   | pp512         | 518.76          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q8\_0           | 7.17 GiB   | tg16          | 26.31           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q6\_K           | 5.54 GiB   | pp512         | 726.13          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q6\_K           | 5.54 GiB   | tg16          | 38.65           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q5\_1           | 5.07 GiB   | pp512         | 534.04          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q5\_1           | 5.07 GiB   | tg16          | 38.68           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q5\_K\_M        | 4.78 GiB   | pp512         | 723.25          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q5\_K\_M        | 4.78 GiB   | tg16          | 41.13           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q5\_0           | 4.65 GiB   | pp512         | 536.67          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q5\_0           | 4.65 GiB   | tg16          | 42.46           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q5\_K\_S        | 4.65 GiB   | pp512         | 651.05          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q5\_K\_S        | 4.65 GiB   | tg16          | 42.14           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q4\_1           | 4.24 GiB   | pp512         | 572.67          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q4\_1           | 4.24 GiB   | tg16          | 43.19           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q4\_K\_M        | 4.07 GiB   | pp512         | 728.48          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q4\_K\_M        | 4.07 GiB   | tg16          | 44.29           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q4\_K\_S        | 3.86 GiB   | pp512         | 666.82          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q4\_K\_S        | 3.86 GiB   | tg16          | 45.18           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q4\_0           | 3.83 GiB   | pp512         | 562.96          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q4\_0           | 3.83 GiB   | tg16          | 48.02           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q3\_K\_L        | 3.56 GiB   | pp512         | 706.64          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q3\_K\_L        | 3.56 GiB   | tg16          | 46.82           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q3\_K\_M        | 3.28 GiB   | pp512         | 715.62          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q3\_K\_M        | 3.28 GiB   | tg16          | 48.29           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q3\_K\_S        | 2.95 GiB   | pp512         | 722.11          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q3\_K\_S        | 2.95 GiB   | tg16          | 49.76           |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q2\_K           | 2.53 GiB   | pp512         | 739.28          |
| AMD Threadripper PRO 7995WX (znver4)       | mistral-7b-instruct-v0.3.Q2\_K           | 2.53 GiB   | tg16          | 53.01           |

## About llamafile

llamafile is a new format introduced by Mozilla Ocho on Nov 20th 2023.
It uses Cosmopolitan Libc to turn LLM weights into runnable llama.cpp
binaries that run on the stock installs of six OSes for both ARM64 and
AMD64.

In addition to being executables, llamafiles are also zip archives. Each
llamafile contains a GGUF file, which you can extract using the `unzip`
command. If you want to change or add files to your llamafiles, then the
`zipalign` command (distributed on the llamafile github) should be used
instead of the traditional `zip` command.

---

# Model Card for Mistral-7B-Instruct-v0.3

The Mistral-7B-Instruct-v0.3 Large Language Model (LLM) is an instruct fine-tuned version of the Mistral-7B-v0.3.

Mistral-7B-v0.3 has the following changes compared to [Mistral-7B-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2/edit/main/README.md)
- Extended vocabulary to 32768
- Supports v3 Tokenizer
- Supports function calling

## Installation

It is recommended to use `mistralai/Mistral-7B-Instruct-v0.3` with [mistral-inference](https://github.com/mistralai/mistral-inference). For HF transformers code snippets, please keep scrolling.

```
pip install mistral_inference
```

## Download

```py
from huggingface_hub import snapshot_download
from pathlib import Path

mistral_models_path = Path.home().joinpath('mistral_models', '7B-Instruct-v0.3')
mistral_models_path.mkdir(parents=True, exist_ok=True)

snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_models_path)
```

### Chat

After installing `mistral_inference`, a `mistral-chat` CLI command should be available in your environment. You can chat with the model using

```
mistral-chat $HOME/mistral_models/7B-Instruct-v0.3 --instruct --max_tokens 256
```

### Instruct following

```py
from mistral_inference.model import Transformer
from mistral_inference.generate import generate

from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest


tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tokenizer.model.v3")
model = Transformer.from_folder(mistral_models_path)

completion_request = ChatCompletionRequest(messages=[UserMessage(content="Explain Machine Learning to me in a nutshell.")])

tokens = tokenizer.encode_chat_completion(completion_request).tokens

out_tokens, _ = generate([tokens], model, max_tokens=64, temperature=0.0, eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id)
result = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])

print(result)
```

### Function calling

```py
from mistral_common.protocol.instruct.tool_calls import Function, Tool
from mistral_inference.model import Transformer
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

## Generate with `transformers`

If you want to use Hugging Face `transformers` to generate text, you can do something like this.

```py
from transformers import pipeline

messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
chatbot(messages)
```

## Limitations

The Mistral 7B Instruct model is a quick demonstration that the base model can be easily fine-tuned to achieve compelling performance. 
It does not have any moderation mechanisms. We're looking forward to engaging with the community on ways to
make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs.

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Antoine Roux, Arthur Mensch, Audrey Herblin-Stoop, Baptiste Bout, Baudouin de Monicault, Blanche Savary, Bam4d, Caroline Feldman, Devendra Singh Chaplot, Diego de las Casas, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona, Jean-Malo Delignon, Jia Li, Justus Murke, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat, Marie Torelli, Marie-Anne Lachaux, Nicolas Schuhl, Patrick von Platen, Pierre Stock, Sandeep Subramanian, Sophia Yang, Szymon Antoniak, Teven Le Scao, Thibaut Lavril, Timothée Lacroix, Théophile Gervet, Thomas Wang, Valera Nemychnikova, William El Sayed, William Marshall