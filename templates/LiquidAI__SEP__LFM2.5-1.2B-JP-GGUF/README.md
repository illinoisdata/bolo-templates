---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ja
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- llama.cpp
- gguf
base_model:
- LiquidAI/LFM2.5-1.2B-JP
---

<div align="center">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI" 
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • 
    <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> • 
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a>
  </div>
</div>

# LFM2.5-1.2B-JP

LFM2.5-JP is a Japanese language model based on the LFM2.5 hybrid architecture, optimized for Japanese text generation and completion tasks.

Find more details in the original model card: [https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP)

## 🏃 How to run

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```
llama-cli -hf LiquidAI/LFM2.5-1.2B-JP-GGUF --repeat_penalty 1.05
```