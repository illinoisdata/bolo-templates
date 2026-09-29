---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
pipeline_tag: image-text-to-text
tags:
- vision
- vlm
- liquid
- lfm2
- lfm2-vl
- edge
- llama.cpp
- gguf
base_model:
- LiquidAI/LFM2-VL-450M
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
  <a href="https://playground.liquid.ai/chat">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a></a>
</div>
</center>

# LFM2-VL-450M-GGUF

LFM2-VL is a new generation of vision models developed by [Liquid AI](https://www.liquid.ai/), specifically designed for edge AI and on-device deployment. It sets a new standard in terms of quality, speed, and memory efficiency.

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2-VL-450M

## 🏃 How to run LFM2-VL

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

full precision (F16/F16):

```
llama-mtmd-cli -hf LiquidAI/LFM2-VL-450M-GGUF:F16
```

fastest inference (Q4_0/Q8_0):

```
llama-mtmd-cli -hf LiquidAI/LFM2-VL-450M-GGUF:Q4_0
```