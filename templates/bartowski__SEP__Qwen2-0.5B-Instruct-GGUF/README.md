---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
tags:
- chat
quantized_by: bartowski
---

## Llamacpp imatrix Quantizations of Qwen2-0.5B-Instruct

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3086">b3086</a> for quantization.

Original model: https://huggingface.co/Qwen/Qwen2-0.5B-Instruct

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

## Prompt format

```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [Qwen2-0.5B-Instruct-Q8_0.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-Q8_0.gguf) | Q8_0 | .53GB | Extremely high quality, generally unneeded but max available quant. |
| [Qwen2-0.5B-Instruct-Q6_K.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-Q6_K.gguf) | Q6_K | .50GB | Very high quality, near perfect, *recommended*. |
| [Qwen2-0.5B-Instruct-Q5_K_M.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-Q5_K_M.gguf) | Q5_K_M | .42GB | High quality, *recommended*. |
| [Qwen2-0.5B-Instruct-Q5_K_S.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-Q5_K_S.gguf) | Q5_K_S | .41GB | High quality, *recommended*. |
| [Qwen2-0.5B-Instruct-Q4_K_M.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-Q4_K_M.gguf) | Q4_K_M | .39GB | Good quality, uses about 4.83 bits per weight, *recommended*. |
| [Qwen2-0.5B-Instruct-Q4_K_S.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-Q4_K_S.gguf) | Q4_K_S | .38GB | Slightly lower quality with more space savings, *recommended*. |
| [Qwen2-0.5B-Instruct-IQ4_XS.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-IQ4_XS.gguf) | IQ4_XS | .34GB | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Qwen2-0.5B-Instruct-Q3_K_L.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-Q3_K_L.gguf) | Q3_K_L | .36GB | Lower quality but usable, good for low RAM availability. |
| [Qwen2-0.5B-Instruct-IQ3_M.gguf](https://huggingface.co/bartowski/Qwen2-0.5B-Instruct-GGUF/blob/main/Qwen2-0.5B-Instruct-IQ3_M.gguf) | IQ3_M | .34GB | Medium-low quality, new method with decent performance comparable to Q3_K_M. |

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/Qwen2-0.5B-Instruct-GGUF --include "Qwen2-0.5B-Instruct-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/Qwen2-0.5B-Instruct-GGUF --include "Qwen2-0.5B-Instruct-Q8_0.gguf/*" --local-dir Qwen2-0.5B-Instruct-Q8_0
```

You can either specify a new local-dir (Qwen2-0.5B-Instruct-Q8_0) or download them all in place (./)

## Which file should I choose?

A great write up with charts showing various performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.

If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.

If you want to get more into the weeds, you can check out this extremely useful feature chart:

[llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU and Apple Metal, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

The I-quants are *not* compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski