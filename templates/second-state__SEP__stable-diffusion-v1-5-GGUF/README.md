---
base_model: runwayml/stable-diffusion-v1-5
license: creativeml-openrail-m
inference: true
model_creator: runwayml
model_name: stable-diffusion-v1-5
quantized_by: Second State Inc.
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# stable-diffusion-v1-5-GGUF

## Original Model

[runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)

## Run with LlamaEdge-StableDiffusion

- Version: [v0.2.0](https://github.com/LlamaEdge/sd-api-server/releases/tag/0.2.0)

- Run as LlamaEdge service

  ```bash
  wasmedge --dir .:. sd-api-server.wasm \
    --model-name sd-v1.5 \
    --model stable-diffusion-v1-5-pruned-emaonly-Q8_0.gguf
  ```

## Quantized GGUF Models

Using formats of different precisions will yield results of varying quality.

| f32  | f16  |q8_0  |q5_0  |q5_1  |q4_0  |q4_1  |
| ----  |----  |----  |----  |----  |----  |----  |
| ![](https://github.com/leejet/stable-diffusion.cpp/blob/master/assets/f32.png?raw=true) |![](https://github.com/leejet/stable-diffusion.cpp/blob/master/assets/f16.png?raw=true) |![](https://github.com/leejet/stable-diffusion.cpp/blob/master/assets/q8_0.png?raw=true) |![](https://github.com/leejet/stable-diffusion.cpp/blob/master/assets/q5_0.png?raw=true) |![](https://github.com/leejet/stable-diffusion.cpp/blob/master/assets/q5_1.png?raw=true) |![](https://github.com/leejet/stable-diffusion.cpp/blob/master/assets/q4_0.png?raw=true) |![](https://github.com/leejet/stable-diffusion.cpp/blob/master/assets/q4_1.png?raw=true) |

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [stable-diffusion-v1-5-pruned-emaonly-Q4_0.gguf](https://huggingface.co/second-state/stable-diffusion-v1-5-GGUF/blob/main/stable-diffusion-v1-5-pruned-emaonly-Q4_0.gguf) | Q4_0 | 2 | 1.57 GB | |
| [stable-diffusion-v1-5-pruned-emaonly-Q4_1.gguf](https://huggingface.co/second-state/stable-diffusion-v1-5-GGUF/blob/main/stable-diffusion-v1-5-pruned-emaonly-Q4_1.gguf) | Q4_1 | 3 | 1.59 GB | |
| [stable-diffusion-v1-5-pruned-emaonly-Q5_0.gguf](https://huggingface.co/second-state/stable-diffusion-v1-5-GGUF/blob/main/stable-diffusion-v1-5-pruned-emaonly-Q5_0.gguf) | Q5_0 | 3 | 1.62 GB | |
| [stable-diffusion-v1-5-pruned-emaonly-Q5_1.gguf](https://huggingface.co/second-state/stable-diffusion-v1-5-GGUF/blob/main/stable-diffusion-v1-5-pruned-emaonly-Q5_1.gguf) | Q5_1 | 3 | 1.64 GB | |
| [stable-diffusion-v1-5-pruned-emaonly-Q8_0.gguf](https://huggingface.co/second-state/stable-diffusion-v1-5-GGUF/blob/main/stable-diffusion-v1-5-pruned-emaonly-Q8_0.gguf) | Q8_0 | 4 | 1.76 GB | |
| [stable-diffusion-v1-5-pruned-emaonly-f16.gguf](https://huggingface.co/second-state/stable-diffusion-v1-5-GGUF/blob/main/stable-diffusion-v1-5-pruned-emaonly-f16.gguf)   | f16  | 4 | 2.13 GB | |
| [stable-diffusion-v1-5-pruned-emaonly-f32.gguf](https://huggingface.co/second-state/stable-diffusion-v1-5-GGUF/blob/main/stable-diffusion-v1-5-pruned-emaonly-f32.gguf)   | f32  | 4 | 4.27 GB | |