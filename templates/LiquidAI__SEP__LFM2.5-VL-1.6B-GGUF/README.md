---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ja
- ko
- fr
- es
- de
- it
- pt
- ar
- zh
pipeline_tag: image-text-to-text
tags:
- liquid
- edge
- lfm2.5-vl
- lfm2.5
- edge
- llama.cpp
- gguf
base_model:
- LiquidAI/LFM2.5-VL-1.6B
---

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" alt="Liquid AI" style="width: 100%; max-width: 100%;">

  <p>
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> •
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> •
    <a href="https://www.liquid.ai/blog/"><strong>Blog</strong></a>
  </p>
</div>

# LFM2.5-VL-1.6B

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2.5-VL-1.6B

## 🏃 How to run LFM2.5-VL-1.6B

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```
llama-cli -hf LiquidAI/LFM2.5-VL-1.6B-GGUF:Q4_0
```

```
llama-cli -hf LiquidAI/LFM2.5-VL-1.6B-GGUF:F16
```