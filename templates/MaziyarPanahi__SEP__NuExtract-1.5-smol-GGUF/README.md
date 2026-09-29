---
base_model: numind/NuExtract-1.5-smol
inference: false
model_creator: numind
model_name: NuExtract-1.5-smol-GGUF
pipeline_tag: text-generation
quantized_by: MaziyarPanahi
tags:
- quantized
- 2-bit
- 3-bit
- 4-bit
- 5-bit
- 6-bit
- 8-bit
- GGUF
- text-generation
---
# [MaziyarPanahi/NuExtract-1.5-smol-GGUF](https://huggingface.co/MaziyarPanahi/NuExtract-1.5-smol-GGUF)
- Model creator: [numind](https://huggingface.co/numind)
- Original model: [numind/NuExtract-1.5-smol](https://huggingface.co/numind/NuExtract-1.5-smol)

## Description
[MaziyarPanahi/NuExtract-1.5-smol-GGUF](https://huggingface.co/MaziyarPanahi/NuExtract-1.5-smol-GGUF) contains GGUF format model files for [numind/NuExtract-1.5-smol](https://huggingface.co/numind/NuExtract-1.5-smol).

### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplete list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration. Linux available, in beta as of 27/11/2023.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [GPT4All](https://gpt4all.io/index.html), a free and open source local running GUI, supporting Windows, Linux and macOS with full GPU accel.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server. Note, as of time of writing (November 27th 2023), ctransformers has not been updated in a long time and does not support many recent models.

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.