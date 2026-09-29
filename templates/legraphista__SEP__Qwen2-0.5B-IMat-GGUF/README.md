---
base_model: Qwen/Qwen2-0.5B
inference: false
language:
- en
library_name: gguf
license: apache-2.0
pipeline_tag: text-generation
quantized_by: legraphista
tags:
- pretrained
- quantized
- GGUF
- imatrix
- quantization
- imat
- imatrix
- static
- 16bit
- 8bit
- 6bit
- 5bit
- 4bit
- 3bit
- 2bit
- 1bit
---

# Qwen2-0.5B-IMat-GGUF
_Llama.cpp imatrix quantization of Qwen/Qwen2-0.5B_

Original Model: [Qwen/Qwen2-0.5B](https://huggingface.co/Qwen/Qwen2-0.5B)    
Original dtype: `BF16` (`bfloat16`)  
Quantized by:  llama.cpp [b3091](https://github.com/ggerganov/llama.cpp/releases/tag/b3091)  
IMatrix dataset: [here](https://gist.githubusercontent.com/bartowski1182/eb213dccb3571f863da82e99418f81e8/raw/b2869d80f5c16fd7082594248e80144677736635/calibration_datav3.txt)  

- [Files](#files)
    - [IMatrix](#imatrix)
    - [Common Quants](#common-quants)
    - [All Quants](#all-quants)
- [Downloading using huggingface-cli](#downloading-using-huggingface-cli)
- [Inference](#inference)
    - [Simple chat template](#simple-chat-template)
    - [Chat template with system prompt](#chat-template-with-system-prompt)
    - [Llama.cpp](#llama-cpp)
- [FAQ](#faq)
    - [Why is the IMatrix not applied everywhere?](#why-is-the-imatrix-not-applied-everywhere)
    - [How do I merge a split GGUF?](#how-do-i-merge-a-split-gguf)

---

## Files

### IMatrix
Status: ✅ Available  
Link: [here](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/imatrix.dat) 

### Common Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [Qwen2-0.5B.Q8_0.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q8_0.gguf) | Q8_0 | 531.07MB | ✅ Available | ⚪ Static | 📦 No
| [Qwen2-0.5B.Q6_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q6_K.gguf) | Q6_K | 505.73MB | ✅ Available | ⚪ Static | 📦 No
| [Qwen2-0.5B.Q4_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q4_K.gguf) | Q4_K | 397.81MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.Q3_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q3_K.gguf) | Q3_K | 355.46MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.Q2_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q2_K.gguf) | Q2_K | 338.60MB | ✅ Available | 🟢 IMatrix | 📦 No


### All Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [Qwen2-0.5B.BF16.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.BF16.gguf) | BF16 | 994.15MB | ✅ Available | ⚪ Static | 📦 No
| [Qwen2-0.5B.FP16.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.FP16.gguf) | F16 | 994.15MB | ✅ Available | ⚪ Static | 📦 No
| [Qwen2-0.5B.Q8_0.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q8_0.gguf) | Q8_0 | 531.07MB | ✅ Available | ⚪ Static | 📦 No
| [Qwen2-0.5B.Q6_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q6_K.gguf) | Q6_K | 505.73MB | ✅ Available | ⚪ Static | 📦 No
| [Qwen2-0.5B.Q5_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q5_K.gguf) | Q5_K | 420.08MB | ✅ Available | ⚪ Static | 📦 No
| [Qwen2-0.5B.Q5_K_S.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q5_K_S.gguf) | Q5_K_S | 412.71MB | ✅ Available | ⚪ Static | 📦 No
| [Qwen2-0.5B.Q4_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q4_K.gguf) | Q4_K | 397.81MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.Q4_K_S.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q4_K_S.gguf) | Q4_K_S | 385.47MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ4_NL.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ4_NL.gguf) | IQ4_NL | 352.67MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ4_XS.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ4_XS.gguf) | IQ4_XS | 349.40MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.Q3_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q3_K.gguf) | Q3_K | 355.46MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.Q3_K_L.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q3_K_L.gguf) | Q3_K_L | 369.36MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.Q3_K_S.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q3_K_S.gguf) | Q3_K_S | 338.26MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ3_M.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ3_M.gguf) | IQ3_M | 342.75MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ3_S.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ3_S.gguf) | IQ3_S | 338.60MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ3_XS.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ3_XS.gguf) | IQ3_XS | 338.60MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ3_XXS.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ3_XXS.gguf) | IQ3_XXS | 333.70MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.Q2_K.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q2_K.gguf) | Q2_K | 338.60MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.Q2_K_S.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.Q2_K_S.gguf) | Q2_K_S | 331.05MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ2_M.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ2_M.gguf) | IQ2_M | 328.59MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ2_S.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ2_S.gguf) | IQ2_S | 325.73MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ2_XS.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ2_XS.gguf) | IQ2_XS | 324.41MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ2_XXS.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ2_XXS.gguf) | IQ2_XXS | 321.55MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ1_M.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ1_M.gguf) | IQ1_M | 317.97MB | ✅ Available | 🟢 IMatrix | 📦 No
| [Qwen2-0.5B.IQ1_S.gguf](https://huggingface.co/legraphista/Qwen2-0.5B-IMat-GGUF/blob/main/Qwen2-0.5B.IQ1_S.gguf) | IQ1_S | 315.83MB | ✅ Available | 🟢 IMatrix | 📦 No


## Downloading using huggingface-cli
If you do not have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"
```
Download the specific file you want:
```
huggingface-cli download legraphista/Qwen2-0.5B-IMat-GGUF --include "Qwen2-0.5B.Q8_0.gguf" --local-dir ./
```
If the model file is big, it has been split into multiple files. In order to download them all to a local folder, run:
```
huggingface-cli download legraphista/Qwen2-0.5B-IMat-GGUF --include "Qwen2-0.5B.Q8_0/*" --local-dir ./
# see FAQ for merging GGUF's
```

---

## Inference

### Simple chat template
```
<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
{user_prompt}<|im_end|>
<|im_start|>assistant
{assistant_response}<|im_end|>
<|im_start|>user
{next_user_prompt}<|im_end|>

```

### Chat template with system prompt
```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{user_prompt}<|im_end|>
<|im_start|>assistant
{assistant_response}<|im_end|>
<|im_start|>user
{next_user_prompt}<|im_end|>

```

### Llama.cpp
```
llama.cpp/main -m Qwen2-0.5B.Q8_0.gguf --color -i -p "prompt here (according to the chat template)"
```

---

## FAQ

### Why is the IMatrix not applied everywhere?
According to [this investigation](https://www.reddit.com/r/LocalLLaMA/comments/1993iro/ggufs_quants_can_punch_above_their_weights_now/), it appears that lower quantizations are the only ones that benefit from the imatrix input (as per hellaswag results). 

### How do I merge a split GGUF?
1. Make sure you have `gguf-split` available
    - To get hold of `gguf-split`, navigate to https://github.com/ggerganov/llama.cpp/releases
    - Download the appropriate zip for your system from the latest release
    - Unzip the archive and you should be able to find `gguf-split`
2. Locate your GGUF chunks folder (ex: `Qwen2-0.5B.Q8_0`)
3. Run `gguf-split --merge Qwen2-0.5B.Q8_0/Qwen2-0.5B.Q8_0-00001-of-XXXXX.gguf Qwen2-0.5B.Q8_0.gguf`
    - Make sure to point `gguf-split` to the first chunk of the split.

---

Got a suggestion? Ping me [@legraphista](https://x.com/legraphista)!