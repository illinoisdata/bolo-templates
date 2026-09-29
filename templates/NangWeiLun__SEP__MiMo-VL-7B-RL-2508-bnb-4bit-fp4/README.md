---
base_model:
- XiaomiMiMo/MiMo-VL-7B-RL-2508
base_model_relation: "quantized"
library_name: transformers
license: mit
pipeline_tag: image-text-to-text
tags:
- quantization
- 4bit
- bitsandbytes
- bnb
- memory-efficient
quantization_config:
  quantization_method: bitsandbytes
  quantization_dtype: fp4
  compute_dtype: bfloat16
---

# MiMo-VL-7B-RL-2508 — 4-bit BitsAndBytes Quantized

This is a **4-bit quantized** version of [XiaomiMiMo/MiMo-VL-7B-RL-2508](https://huggingface.co/XiaomiMiMo/MiMo-VL-7B-RL-2508),  
using the [BitsAndBytes](https://github.com/TimDettmers/bitsandbytes) library.

Quantization reduces memory usage and makes it possible to run this model on consumer GPUs  
(≤ 12 GB VRAM), at the cost of a small reduction in generation quality.

---

## Quantization Details

- **Method**: BitsAndBytes (bnb)  
- **Precision**: 4-bit (`fp4`)  
- **Compute dtype**: bfloat16  
- **Double quantization**: disabled  
- **Format**: `safetensors`  