---
thumbnail: "https://assets-global.website-files.com/646b351987a8d8ce158d1940/64ec9e96b4334c0e1ac41504_Logo%20with%20white%20text.svg"
base_model: gpt2
metrics:
- memory_disk
- memory_inference
- inference_latency
- inference_throughput
- inference_CO2_emissions
- inference_energy_consumption
tags:
- pruna-ai
---
<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
    <a href="https://www.pruna.ai/" target="_blank" rel="noopener noreferrer">
        <img src="https://i.imgur.com/eDAlcgk.png" alt="PrunaAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
    </a>
</div>
<!-- header end -->

[![Twitter](https://img.shields.io/twitter/follow/PrunaAI?style=social)](https://twitter.com/PrunaAI)
[![GitHub](https://img.shields.io/github/followers/PrunaAI?label=Follow%20%40PrunaAI&style=social)](https://github.com/PrunaAI)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/company/93832878/admin/feed/posts/?feedType=following)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-blue?style=social&logo=discord)](https://discord.com/invite/vb6SmA3hxu)

## This repo contains GGUF versions of the gpt2 model.

# Simply make AI models cheaper, smaller, faster, and greener!

- Give a thumbs up if you like this model!
- Contact us and tell us which model to compress next [here](https://www.pruna.ai/contact).
- Request access to easily compress your *own* AI models [here](https://z0halsaff74.typeform.com/pruna-access?typeform-source=www.pruna.ai).
- Read the documentations to know more [here](https://pruna-ai-pruna.readthedocs-hosted.com/en/latest/)
- Join Pruna AI community on Discord [here](https://discord.gg/rskEr4BZJx) to share feedback/suggestions or get help.

**Frequently Asked Questions**
- ***How does the compression work?*** The model is compressed with GGUF.
- ***How does the model quality change?*** The quality of the model output might vary compared to the base model.
- ***What is the model format?*** We use GGUF format.
- ***What calibration data has been used?*** If needed by the compression method, we used WikiText as the calibration data.
- ***How to compress my own models?*** You can request premium access to more compression methods and tech support for your specific use-cases [here](https://z0halsaff74.typeform.com/pruna-access?typeform-source=www.pruna.ai).

# Downloading and running the models

You can download the individual files from the Files & versions section. Here is a list of the different versions we provide. For more info checkout [this chart](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9) and [this guide](https://www.reddit.com/r/LocalLLaMA/comments/1ba55rj/overview_of_gguf_quantization_methods/):

| Quant type | Description                                                                                |
|------------|--------------------------------------------------------------------------------------------|
| Q5_K_M     | High quality, recommended.                                                                 |
| Q5_K_S     | High quality, recommended.                                                                 |
| Q4_K_M     | Good quality, uses about 4.83 bits per weight, recommended.                                |
| Q4_K_S     | Slightly lower quality with more space savings, recommended.                               |
| IQ4_NL     | Decent quality, slightly smaller than Q4_K_S with similar performance, recommended.        |
| IQ4_XS     | Decent quality, smaller than Q4_K_S with similar performance, recommended.                 |
| Q3_K_L     | Lower quality but usable, good for low RAM availability.                                   |
| Q3_K_M     | Even lower quality.                                                                        |
| IQ3_M      | Medium-low quality, new method with decent performance comparable to Q3_K_M.               |
| IQ3_S      | Lower quality, new method with decent performance, recommended over Q3_K_S quant, same size with better performance. |
| Q3_K_S     | Low quality, not recommended.                                                              |
| IQ3_XS     | Lower quality, new method with decent performance, slightly better than Q3_K_S.            |
| Q2_K       | Very low quality but surprisingly usable.                                                  |


## How to download GGUF files ?

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:

* LM Studio
* LoLLMS Web UI
* Faraday.dev

- **Option A** - Downloading in `text-generation-webui`:
- **Step 1**: Under Download Model, you can enter the model repo: gpt2-GGUF-smashed and below it, a specific filename to download, such as: phi-2.IQ3_M.gguf.
- **Step 2**: Then click Download.

- **Option B** - Downloading on the command line (including multiple files at once):
- **Step 1**: We recommend using the `huggingface-hub` Python library:
```shell
pip3 install huggingface-hub
```
- **Step 2**: Then you can download any individual model file to the current directory, at high speed, with a command like this:
```shell
huggingface-cli download gpt2-GGUF-smashed gpt2.IQ3_M.gguf --local-dir . --local-dir-use-symlinks False
```
<details>
    <summary>More advanced huggingface-cli download usage (click to read)</summary>
Alternatively, you can also download multiple files at once with a pattern:

```shell
huggingface-cli download gpt2-GGUF-smashed --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download gpt2-GGUF-smashed gpt2.IQ3_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->

## How to run model in GGUF format?
- **Option A** - Introductory example with `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 35 -m gpt2.IQ3_M.gguf --color -c 32768 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<s>[INST] {{prompt\}} [/INST]"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 32768` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically. Note that longer sequence lengths require much more resources, so you may need to reduce this value.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

- **Option B** - Running in `text-generation-webui`

Further instructions can be found in the text-generation-webui documentation, here: [text-generation-webui/docs/04 ‐ Model Tab.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/04%20-%20Model%20Tab.md#llamacpp).

- **Option C** - Running from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries. Note that at the time of writing (Nov 27th 2023), ctransformers has not been updated for some time and is not compatible with some recent models. Therefore I recommend you use llama-cpp-python.

    ### How to load this model in Python code, using llama-cpp-python
    
    For full documentation, please see: [llama-cpp-python docs](https://abetlen.github.io/llama-cpp-python/).
    
    #### First install the package
    
    Run one of the following commands, according to your system:
    
    ```shell
    # Base ctransformers with no GPU acceleration
    pip install llama-cpp-python
    # With NVidia CUDA acceleration
    CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
    # Or with OpenBLAS acceleration
    CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
    # Or with CLBLast acceleration
    CMAKE_ARGS="-DLLAMA_CLBLAST=on" pip install llama-cpp-python
    # Or with AMD ROCm GPU acceleration (Linux only)
    CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python
    # Or with Metal GPU acceleration for macOS systems only
    CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
    
    # In windows, to set the variables CMAKE_ARGS in PowerShell, follow this format; eg for NVidia CUDA:
    $env:CMAKE_ARGS = "-DLLAMA_OPENBLAS=on"
    pip install llama-cpp-python
    ```
    
    #### Simple llama-cpp-python example code
    
    ```python
    from llama_cpp import Llama
    
    # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
    llm = Llama(
    model_path="./gpt2.IQ3_M.gguf",  # Download the model file first
    n_ctx=32768,  # The max sequence length to use - note that longer sequence lengths require much more resources
    n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
    n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
    )
    
    # Simple inference example
    output = llm(
    "<s>[INST] {{prompt}} [/INST]", # Prompt
    max_tokens=512,  # Generate up to 512 tokens
    stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
    echo=True        # Whether to echo the prompt
    )
    
    # Chat Completion API
    
    llm = Llama(model_path="./gpt2.IQ3_M.gguf", chat_format="llama-2")  # Set chat_format according to the model you are using
    llm.create_chat_completion(
        messages = [
            {{"role": "system", "content": "You are a story writing assistant."}},
            {{
                "role": "user",
                "content": "Write a story about llamas."
            }}
        ]
    )
    ```

- **Option D** - Running with LangChain

Here are guides on using llama-cpp-python and ctransformers with LangChain:

* [LangChain + llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp)
* [LangChain + ctransformers](https://python.langchain.com/docs/integrations/providers/ctransformers)

## Configurations

The configuration info are in `smash_config.json`.

## Credits & License

The license of the smashed model follows the license of the original model. Please check the license of the original model before using this model which provided the base model. The license  of the `pruna-engine` is [here](https://pypi.org/project/pruna-engine/) on Pypi.

## Want to compress other models?

- Contact us and tell us which model to compress next [here](https://www.pruna.ai/contact).
- Request access to easily compress your own AI models [here](https://z0halsaff74.typeform.com/pruna-access?typeform-source=www.pruna.ai).