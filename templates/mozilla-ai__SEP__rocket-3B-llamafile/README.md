---
base_model: pansophic/rocket-3B
inference: false
language:
- en
license: cc-by-sa-4.0
model-index:
- name: rocket-3b
  results: []
model_creator: pansophic
model_name: Rocket 3B
model_type: stablelm
prompt_template: |
  <|im_start|>system
  {system_message}<|im_end|>
  <|im_start|>user
  {prompt}<|im_end|>
  <|im_start|>assistant
quantized_by: TheBloke
tags:
- llamafile
---
<!-- markdownlint-disable MD041 -->

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://discord.gg/FwAVVu7eJ4">Chat & support: jartine's Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
    </div>
</div>
<div style="text-align:center; margin-top: 0em; margin-bottom: 0em"><p style="margin-top: 0.25em; margin-bottom: 0em;">jartine's LLM work is generously supported by a grant from <a href="https://mozilla.org">mozilla</a></p></div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Rocket 3B - llamafile
- Model creator: [pansophic](https://huggingface.co/pansophic)
- Original model: [Rocket 3B](https://huggingface.co/pansophic/rocket-3B)

<!-- description start -->
## Description

This repo contains llamafile format model files for [pansophic's Rocket 3B](https://huggingface.co/pansophic/rocket-3B).

These files were quantised using hardware kindly provided by [Massed Compute](https://massedcompute.com/).

WARNING: This README may contain inaccuracies. It was generated automatically by forking <a href=/TheBloke/rocket-3B-GGUF>TheBloke/rocket-3B-GGUF</a> and piping the README through sed. Errors should be reported to jartine, and do not reflect TheBloke. You can also support his work on [Patreon](https://www.patreon.com/TheBlokeAI).
<!-- README_llamafile.md-about-llamafile start -->
### About llamafile

llamafile is a new format introduced by Mozilla Ocho on Nov 20th 2023. It uses Cosmopolitan Libc to turn LLM weights into runnable llama.cpp binaries that run on the stock installs of six OSes for both ARM64 and AMD64.

Here is an incomplete list of clients and libraries that are known to support llamafile:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for llamafile. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.

<!-- README_llamafile.md-about-llamafile end -->
<!-- repositories-available start -->
## Repositories available

* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/jartine/rocket-3B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit llamafile models for CPU+GPU inference](https://huggingface.co/jartine/rocket-3B-llamafile)
* [pansophic's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/pansophic/rocket-3B)
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


<!-- compatibility_llamafile start -->
## Compatibility

These quantised llamafilev2 files are compatible with llama.cpp from August 27th onwards, as of commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221)

They are also compatible with many third party UIs and libraries - please see the list at the top of this README.

## Explanation of quantisation methods

<details>
  <summary>Click to see details</summary>

The new methods available are:

* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw

Refer to the Provided Files table below to see what files use which methods, and how.
</details>
<!-- compatibility_llamafile end -->

<!-- README_llamafile.md-provided-files start -->
## Provided files

| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [rocket-3b.Q2_K.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q2_K.llamafile) | Q2_K | 2 | 1.20 GB| 3.70 GB | smallest, significant quality loss - not recommended for most purposes |
| [rocket-3b.Q3_K_S.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q3_K_S.llamafile) | Q3_K_S | 3 | 1.25 GB| 3.75 GB | very small, high quality loss |
| [rocket-3b.Q3_K_M.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q3_K_M.llamafile) | Q3_K_M | 3 | 1.39 GB| 3.89 GB | very small, high quality loss |
| [rocket-3b.Q3_K_L.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q3_K_L.llamafile) | Q3_K_L | 3 | 1.51 GB| 4.01 GB | small, substantial quality loss |
| [rocket-3b.Q4_0.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q4_0.llamafile) | Q4_0 | 4 | 1.61 GB| 4.11 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [rocket-3b.Q4_K_S.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q4_K_S.llamafile) | Q4_K_S | 4 | 1.62 GB| 4.12 GB | small, greater quality loss |
| [rocket-3b.Q4_K_M.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q4_K_M.llamafile) | Q4_K_M | 4 | 1.71 GB| 4.21 GB | medium, balanced quality - recommended |
| [rocket-3b.Q5_0.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q5_0.llamafile) | Q5_0 | 5 | 1.94 GB| 4.44 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [rocket-3b.Q5_K_S.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q5_K_S.llamafile) | Q5_K_S | 5 | 1.94 GB| 4.44 GB | large, low quality loss - recommended |
| [rocket-3b.Q5_K_M.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q5_K_M.llamafile) | Q5_K_M | 5 | 1.99 GB| 4.49 GB | large, very low quality loss - recommended |
| [rocket-3b.Q6_K.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q6_K.llamafile) | Q6_K | 6 | 2.30 GB| 4.80 GB | very large, extremely low quality loss |
| [rocket-3b.Q8_0.llamafile](https://huggingface.co/jartine/rocket-3B-llamafile/blob/main/rocket-3b.Q8_0.llamafile) | Q8_0 | 8 | 2.97 GB| 5.47 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.



<!-- README_llamafile.md-provided-files end -->

<!-- README_llamafile.md-how-to-download start -->
## How to download llamafile files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:

* LM Studio
* LoLLMS Web UI
* Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: jartine/rocket-3B-llamafile and below it, a specific filename to download, such as: rocket-3b.Q4_K_M.llamafile.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download jartine/rocket-3B-llamafile rocket-3b.Q4_K_M.llamafile --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download jartine/rocket-3B-llamafile --local-dir . --local-dir-use-symlinks False --include='*Q4_K*llamafile'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download jartine/rocket-3B-llamafile rocket-3b.Q4_K_M.llamafile --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_llamafile.md-how-to-download end -->

<!-- README_llamafile.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 32 -m rocket-3b.Q4_K_M.llamafile --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<|im_start|>system\n{system_message}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 2048` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the llamafile file and set by llama.cpp automatically.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions can be found in the text-generation-webui documentation, here: [text-generation-webui/docs/04 ‐ Model Tab.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/04%20%E2%80%90%20Model%20Tab.md#llamacpp).

## How to run from Python code

You can use llamafile models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries.

### How to load this model in Python code, using ctransformers

#### First install the package

Run one of the following commands, according to your system:

```shell
# Base ctransformers with no GPU acceleration
pip install ctransformers
# Or with CUDA GPU acceleration
pip install ctransformers[cuda]
# Or with AMD ROCm GPU acceleration (Linux only)
CT_HIPBLAS=1 pip install ctransformers --no-binary ctransformers
# Or with Metal GPU acceleration for macOS systems only
CT_METAL=1 pip install ctransformers --no-binary ctransformers
```

#### Simple ctransformers example code

```python
from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("jartine/rocket-3B-llamafile", model_file="rocket-3b.Q4_K_M.llamafile", model_type="stablelm", gpu_layers=50)

print(llm("AI is going to"))
```

## How to use with LangChain

Here are guides on using llama-cpp-python and ctransformers with LangChain:

* [LangChain + llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp)
* [LangChain + ctransformers](https://python.langchain.com/docs/integrations/providers/ctransformers)

<!-- README_llamafile.md-how-to-run end -->

<!-- footer start -->
<!-- 200823 -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[jartine AI's Discord server](https://discord.gg/FwAVVu7eJ4)

## Thanks, and how to contribute



I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.







And thank you again to mozilla for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: pansophic's Rocket 3B


<img src="https://cdn-uploads.huggingface.co/production/uploads/6501bfe0493fd9c8c2e32402/BmbkjOkcTm-YMa-unolmJ.png" alt="Rocket Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

# Rocket-3B 🦝
<b>Rocket</b> 🦝 is a 3 billion large language model that was trained on a mix of publicly available datasets using [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290). The prompt format used is <b>ChatML</b>.


## Model description
- **Model type:** A 3B parameter GPT-like model fine-tuned on a mix of publicly available datasets using DPO.
- **Language(s) (NLP):** Primarily English
- **License:** CC-BY-SA-4.0
- **Finetuned from model:** [Stability AI](https://huggingface.co/stabilityai/stablelm-3b-4e1t)


## Performance
Despite its compact dimensions, the model achieves outstanding scores in both MT-Bench [MT-Bench](https://huggingface.co/spaces/lmsys/mt-bench) and [AlpacaEval](https://tatsu-lab.github.io/alpaca_eval/) benchmarks, surpassing the performance of considerably larger models.

| Model | Size | Alignment | MT-Bench (score) | AlpacaEval (win rate %) |
|-------------|-----|----|---------------|--------------|
| StableLM-Tuned-α 🦜| 7B | SFT |2.75| -|
| MPT-Chat |  7B | SFT |5.42| -|
| Falcon-Instruct 🦅|  40B | SFT |5.17 |45.71|
| Orca-2|  13B | SFT |6.15 |-|
| Xwin-LMv0.1 | 7B| PPO | 6.19| 87.83|
| Llama2-Chat 🦙| 7B |RLHF |6.26| 71.37|
| TÜLU 2 🐫|  7B | DPO |6.27| 85.1|
| Guanaco 🦙| 65B | SFT |6.41| 71.80|
| **Rocket** 🦝 | **3B** | **DPO** | **6.56** | **79.75** |
| Llama2-Chat 🦙| 13B |RLHF |6.65| 81.09|
| Zephyr-7b-α 🪁 |7B|  DPO| 6.88| -|
| Vicuna v1.3 🦙| 33B | SFT |7.12 |88.99|
| Zephyr-7b-β 🪁 |7B|  DPO| 7.34| 90.60|
| WizardLM v1.0 🦙| 70B |SFT |7.71 |-|
| GPT-3.5-turbo | - |RLHF |7.94 |89.37|

Specifically, across various categories within the MT-Bench evaluation, Rocket-3B demonstrates impressive performance when compared to larger open models such as Llama2-Chat-7B, Falcon-40B-Instruct, and Guanaco-65B.


![MT-Bench results](https://cdn-uploads.huggingface.co/production/uploads/6501bfe0493fd9c8c2e32402/5Tv4-4w4zNKAAjiLNGu7A.png)

## MT-Bench detailed score for first and second turn
In MT-Bench, Rocket 🦝 scores 6.99 in the first turn and 6.13 in the second turn, with an average score of 6.56. These scores reflect the model's performance in understanding and generating text during different parts of a conversation.

| Model | First turn | Second turn | Average |
|-------------|-----|----|---------------|
| **Rocket** 🦝 | **6.99** | **6.13** | **6.56** |


## AlpacaEval detailed scores
In AlpacaEval, Rocket 🦝 achieves a near 80% win rate, coupled with an average response length of 1,242 tokens, indicating its effectiveness in producing detailed responses.

| Model | Win rate | Std error | Average length |
|-------------|-----|----|---------------|
| **Rocket** 🦝 | **79.75** | **1.42** | **1242** |


## Other benchmarks

| Metric                | Value                     |
|-----------------------|---------------------------|
| Average               | 51.00             |
| ARC (25-shot)         | 50.51          |
| HellaSwag (10-shot)   | 76.45    |
| MMLU (5-shot)        | 45.51        |
| TruthfulQA (0-shot)   | 54.38   |
| Winogrande (5-shot)   | 67.8   |
| GSM8K (5-shot)        | 37.91        |
| DROP (3-shot)        | 24.49        |


## Intended uses & limitations
Initially, we fine-tuned the model using a dataset created by merging and curating multiple datasets, available on the HuggingFace Hub. This dataset will be released to the public soon. We further enhanced the model's performance using DPO, selecting samples from the [openbmb/UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) and [BAAI/JudgeLM-100K](https://huggingface.co/datasets/BAAI/JudgeLM-100K) datasets. The outcome is a highly effective chat model with a 3 billion parameter scale.


## Input Format
The model is trained with the ChatML format:

```
<|im_start|>system
System message here.<|im_end|>
<|im_start|>user
Your message here!<|im_end|>
<|im_start|>assistant
```

Here's how you can run the model using 🤗 Transformers:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model = AutoModelForCausalLM.from_pretrained("pansophic/rocket-3B", trust_remote_code=True, torch_dtype=torch.bfloat16).to("cuda")
tokenizer = AutoTokenizer.from_pretrained("pansophic/rocket-3B", trust_remote_code=True, torch_dtype=torch.bfloat16)
streamer = TextStreamer(tokenizer)

prompt = """<|im_start|>system
{system}<|im_end|>
<|im_start|>user
{user}<|im_end|>
<|im_start|>assistant
"""

system = "You are a helpful assistant."
user = "How are you?"

# Apply the ChatML format
prompt = prompt.format(system=system, user=user)

# Tokenize the prompt
inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False).to("cuda")
generated_text = model.generate(**inputs, max_length=3084, top_p=0.95, do_sample=True, temperature=0.7, use_cache=True, streamer=streamer)

# <|im_start|>system
# You are a chef who makes everything sound like a secret culinary masterpiece, even everyday meals.<|im_end|>
# <|im_start|>user
# How to cook an omelette?<|im_end|>
# <|im_start|>assistant
# Ah, the art of crafting the perfect omelette, a secret culinary masterpiece indeed.
# Begin by gently whisking two to three eggs in a mixing bowl, and then pour the silky liquid into a non-stick pan.
# Allow the eggs to dance and sizzle as you swiftly tilt the pan to spread the joy throughout the entire omelette universe.
# As the edges begin to set, fold the omelette in half with a gentle flourish, and you'll witness a stunning display of culinary prowess.
# Enjoy this enchanting creation, and you'll be transported to a world of secret culinary mastery.<|im_end|>
```

## Bias, Risks, and Limitations
Unlike ChatGPT, which incorporates in-the-loop filtering of responses and is aligned during the RLHF phase for safe completions, our model lacks these features. Consequently, it may generate problematic outputs, particularly when prompted in certain ways. Below is the score of the model on Toxigen benchmark.

The pretraining dataset is comprised of a filtered mixture of open-source large-scale datasets available on the [HuggingFace Hub](https://huggingface.co/datasets): Falcon RefinedWeb extract ([Penedo et al., 2023](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)), RedPajama-Data ([Together Computer., 2023](https://github.com/togethercomputer/RedPajama-Data)) and The Pile ([Gao et al., 2020](https://arxiv.org/abs/2101.00027)) both without the *Books3* subset, and StarCoder ([Li et al., 2023](https://arxiv.org/abs/2305.06161)).

| Metric                | Value                     |
|-----------------------|---------------------------|
| Toxigen (0-shot)         | 43.40          |

**The model name is inspired by the small but formidable character from 'Guardians of the Galaxy'. Similar to its namesake, this model, with its 3 billion parameters, showcases remarkable efficiency and effectiveness, challenging larger models despite its smaller size."*

*Model card adapted from [Zephyr Beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta/blob/main/README.md) and [Tulu-2-7B](https://huggingface.co/allenai/tulu-2-7b/blob/main/README.md)*

<!-- original-model-card end -->