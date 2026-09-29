---
base_model: llamas-community/LlamaGuard-7b
inference: false
language:
- en
license: llama2
model_creator: meta-llama
model_name: LlamaGuard 7B
model_type: llama
prompt_template: '[INST] {prompt} [/INST]

  '
quantized_by: TheBloke
tags:
- pytorch
- llama
- llama-2
---
<!-- markdownlint-disable MD041 -->

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://discord.gg/theblokeai">Chat & support: TheBloke's Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<div style="text-align:center; margin-top: 0em; margin-bottom: 0em"><p style="margin-top: 0.25em; margin-bottom: 0em;">TheBloke's LLM work is generously supported by a grant from <a href="https://a16z.com">andreessen horowitz (a16z)</a></p></div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# LlamaGuard 7B - AWQ
- Model creator: [meta-llama](https://huggingface.co/Meta Llama 2)
- Original model: [LlamaGuard 7B](https://huggingface.co/llamas-community/LlamaGuard-7b)

<!-- description start -->
## Description

This repo contains AWQ model files for [meta-llama's LlamaGuard 7B](https://huggingface.co/llamas-community/LlamaGuard-7b).

These files were quantised using hardware kindly provided by [Massed Compute](https://massedcompute.com/).


### About AWQ

AWQ is an efficient, accurate and blazing-fast low-bit weight quantization method, currently supporting 4-bit quantization. Compared to GPTQ, it offers faster Transformers-based inference with equivalent or better quality compared to the most commonly used GPTQ settings.

AWQ models are currently supported on Linux and Windows, with NVidia GPUs only. macOS users: please use GGUF models instead.

It is supported by:

- [Text Generation Webui](https://github.com/oobabooga/text-generation-webui) - using Loader: AutoAWQ
- [vLLM](https://github.com/vllm-project/vllm) - version 0.2.2 or later for support for all model types.
- [Hugging Face Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference)
- [Transformers](https://huggingface.co/docs/transformers) version 4.35.0 and later, from any code or client that supports Transformers
- [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) - for use from Python code

<!-- description end -->
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/LlamaGuard-7B-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/LlamaGuard-7B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/LlamaGuard-7B-GGUF)
* [meta-llama's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/llamas-community/LlamaGuard-7b)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: INST

```
[INST] {prompt} [/INST]

```

<!-- prompt-template end -->


<!-- README_AWQ.md-provided-files start -->
## Provided files, and AWQ parameters

I currently release 128g GEMM models only. The addition of group_size 32 models, and GEMV kernel models, is being actively considered.

Models are released as sharded safetensors files.

| Branch | Bits | GS | AWQ Dataset | Seq Len | Size |
| ------ | ---- | -- | ----------- | ------- | ---- |
| [main](https://huggingface.co/TheBloke/LlamaGuard-7B-AWQ/tree/main) | 4 | 128 | [VMware Open Instruct](https://huggingface.co/datasets/VMware/open-instruct/viewer/) | 2048 | 3.89 GB

<!-- README_AWQ.md-provided-files end -->

<!-- README_AWQ.md-text-generation-webui start -->
## How to easily download and use this model in [text-generation-webui](https://github.com/oobabooga/text-generation-webui)

Please make sure you're using the latest version of [text-generation-webui](https://github.com/oobabooga/text-generation-webui).

It is strongly recommended to use the text-generation-webui one-click-installers unless you're sure you know how to make a manual install.

1. Click the **Model tab**.
2. Under **Download custom model or LoRA**, enter `TheBloke/LlamaGuard-7B-AWQ`.
3. Click **Download**.
4. The model will start downloading. Once it's finished it will say "Done".
5. In the top left, click the refresh icon next to **Model**.
6. In the **Model** dropdown, choose the model you just downloaded: `LlamaGuard-7B-AWQ`
7. Select **Loader: AutoAWQ**.
8. Click Load, and the model will load and is now ready for use.
9. If you want any custom settings, set them and then click **Save settings for this model** followed by **Reload the Model** in the top right.
10. Once you're ready, click the **Text Generation** tab and enter a prompt to get started!
<!-- README_AWQ.md-text-generation-webui end -->

<!-- README_AWQ.md-use-from-vllm start -->
## Multi-user inference server: vLLM

Documentation on installing and using vLLM [can be found here](https://vllm.readthedocs.io/en/latest/).

- Please ensure you are using vLLM version 0.2 or later.
- When using vLLM as a server, pass the `--quantization awq` parameter.

For example:

```shell
python3 -m vllm.entrypoints.api_server --model TheBloke/LlamaGuard-7B-AWQ --quantization awq --dtype auto
```

- When using vLLM from Python code, again set `quantization=awq`.

For example:

```python
from vllm import LLM, SamplingParams

prompts = [
    "Tell me about AI",
    "Write a story about llamas",
    "What is 291 - 150?",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
]
prompt_template=f'''[INST] {prompt} [/INST]
'''

prompts = [prompt_template.format(prompt=prompt) for prompt in prompts]

sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="TheBloke/LlamaGuard-7B-AWQ", quantization="awq", dtype="auto")

outputs = llm.generate(prompts, sampling_params)

# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```
<!-- README_AWQ.md-use-from-vllm start -->

<!-- README_AWQ.md-use-from-tgi start -->
## Multi-user inference server: Hugging Face Text Generation Inference (TGI)

Use TGI version 1.1.0 or later. The official Docker container is: `ghcr.io/huggingface/text-generation-inference:1.1.0`

Example Docker parameters:

```shell
--model-id TheBloke/LlamaGuard-7B-AWQ --port 3000 --quantize awq --max-input-length 3696 --max-total-tokens 4096 --max-batch-prefill-tokens 4096
```

Example Python code for interfacing with TGI (requires [huggingface-hub](https://github.com/huggingface/huggingface_hub) 0.17.0 or later):

```shell
pip3 install huggingface-hub
```

```python
from huggingface_hub import InferenceClient

endpoint_url = "https://your-endpoint-url-here"

prompt = "Tell me about AI"
prompt_template=f'''[INST] {prompt} [/INST]
'''

client = InferenceClient(endpoint_url)
response = client.text_generation(prompt,
                                  max_new_tokens=128,
                                  do_sample=True,
                                  temperature=0.7,
                                  top_p=0.95,
                                  top_k=40,
                                  repetition_penalty=1.1)

print(f"Model output: ", response)
```
<!-- README_AWQ.md-use-from-tgi end -->

<!-- README_AWQ.md-use-from-python start -->
## Inference from Python code using Transformers

### Install the necessary packages

- Requires: [Transformers](https://huggingface.co/docs/transformers) 4.35.0 or later.
- Requires: [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) 0.1.6 or later.

```shell
pip3 install --upgrade "autoawq>=0.1.6" "transformers>=4.35.0"
```

Note that if you are using PyTorch 2.0.1, the above AutoAWQ command will automatically upgrade you to PyTorch 2.1.0.

If you are using CUDA 11.8 and wish to continue using PyTorch 2.0.1, instead run this command:

```shell
pip3 install https://github.com/casper-hansen/AutoAWQ/releases/download/v0.1.6/autoawq-0.1.6+cu118-cp310-cp310-linux_x86_64.whl
```

If you have problems installing [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) using the pre-built wheels, install it from source instead:

```shell
pip3 uninstall -y autoawq
git clone https://github.com/casper-hansen/AutoAWQ
cd AutoAWQ
pip3 install .
```

### Transformers example code (requires Transformers 4.35.0 and later)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_name_or_path = "TheBloke/LlamaGuard-7B-AWQ"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path,
    low_cpu_mem_usage=True,
    device_map="cuda:0"
)

# Using the text streamer to stream output one token at a time
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

prompt = "Tell me about AI"
prompt_template=f'''[INST] {prompt} [/INST]
'''

# Convert prompt to tokens
tokens = tokenizer(
    prompt_template,
    return_tensors='pt'
).input_ids.cuda()

generation_params = {
    "do_sample": True,
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_new_tokens": 512,
    "repetition_penalty": 1.1
}

# Generate streamed output, visible one token at a time
generation_output = model.generate(
    tokens,
    streamer=streamer,
    **generation_params
)

# Generation without a streamer, which will include the prompt in the output
generation_output = model.generate(
    tokens,
    **generation_params
)

# Get the tokens from the output, decode them, print them
token_output = generation_output[0]
text_output = tokenizer.decode(token_output)
print("model.generate output: ", text_output)

# Inference is also possible via Transformers' pipeline
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    **generation_params
)

pipe_output = pipe(prompt_template)[0]['generated_text']
print("pipeline output: ", pipe_output)

```
<!-- README_AWQ.md-use-from-python end -->

<!-- README_AWQ.md-compatibility start -->
## Compatibility

The files provided are tested to work with:

- [text-generation-webui](https://github.com/oobabooga/text-generation-webui) using `Loader: AutoAWQ`.
- [vLLM](https://github.com/vllm-project/vllm) version 0.2.0 and later.
- [Hugging Face Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference) version 1.1.0 and later.
- [Transformers](https://huggingface.co/docs/transformers) version 4.35.0 and later.
- [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) version 0.1.1 and later.

<!-- README_AWQ.md-compatibility end -->

<!-- footer start -->
<!-- 200823 -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/theblokeai)

## Thanks, and how to contribute

Thanks to the [chirper.ai](https://chirper.ai) team!

Thanks to Clay from [gpus.llm-utils.org](llm-utils)!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Special thanks to**: Aemon Algiz.

**Patreon special mentions**: Michael Levine, 阿明, Trailburnt, Nikolai Manek, John Detwiler, Randy H, Will Dee, Sebastain Graf, NimbleBox.ai, Eugene Pentland, Emad Mostaque, Ai Maven, Jim Angel, Jeff Scroggin, Michael Davis, Manuel Alberto Morcote, Stephen Murray, Robert, Justin Joy, Luke @flexchar, Brandon Frisco, Elijah Stavena, S_X, Dan Guido, Undi ., Komninos Chatzipapas, Shadi, theTransient, Lone Striker, Raven Klaugh, jjj, Cap'n Zoog, Michel-Marie MAUDET (LINAGORA), Matthew Berman, David, Fen Risland, Omer Bin Jawed, Luke Pendergrass, Kalila, OG, Erik Bjäreholt, Rooh Singh, Joseph William Delisle, Dan Lewis, TL, John Villwock, AzureBlack, Brad, Pedro Madruga, Caitlyn Gatomon, K, jinyuan sun, Mano Prime, Alex, Jeffrey Morgan, Alicia Loh, Illia Dulskyi, Chadd, transmissions 11, fincy, Rainer Wilmers, ReadyPlayerEmma, knownsqashed, Mandus, biorpg, Deo Leter, Brandon Phillips, SuperWojo, Sean Connelly, Iucharbius, Jack West, Harry Royden McLaughlin, Nicholas, terasurfer, Vitor Caleffi, Duane Dunston, Johann-Peter Hartmann, David Ziegler, Olakabola, Ken Nordquist, Trenton Dambrowitz, Tom X Nguyen, Vadim, Ajan Kanaga, Leonard Tan, Clay Pascal, Alexandros Triantafyllidis, JM33133, Xule, vamX, ya boyyy, subjectnull, Talal Aujan, Alps Aficionado, wassieverse, Ari Malik, James Bentley, Woland, Spencer Kim, Michael Dempsey, Fred von Graf, Elle, zynix, William Richards, Stanislav Ovsiannikov, Edmond Seymore, Jonathan Leane, Martin Kemka, usrbinkat, Enrico Ros


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

# Original model card: meta-llama's LlamaGuard 7B

## Model Details

**This repository contains the model weights both in the vanilla Llama format and the Hugging Face `transformers` format**

Llama-Guard is a 7B parameter [Llama 2](https://arxiv.org/abs/2307.09288)-based input-output
safeguard model. It can be used for classifying content in both LLM inputs (prompt
classification) and in LLM responses (response classification).
It acts as an LLM: it generates text in its output that indicates whether a given prompt or
response is safe/unsafe, and if unsafe based on a policy, it also lists the violating subcategories.
Here is an example:

![](Llama-Guard_example.png)

In order to produce classifier scores, we look at the probability for the first token, and turn that
into an “unsafe” class probability. Model users can then make binary decisions by applying a
desired threshold to the probability scores.

## Training and Evaluation
### Training Data

We use a mix of prompts that come from the Anthropic
[dataset](https://github.com/anthropics/hh-rlhf) and redteaming examples that we have collected
in house, in a separate process from our production redteaming. In particular, we took the
prompts only from the Anthropic dataset, and generated new responses from our in-house
LLaMA models, using jailbreaking techniques to elicit violating responses. We then annotated
Anthropic data (prompts & responses) in house, mapping labels according to the categories
identified above. Overall we have ~13K training examples.

## Taxonomy of harms and Risk Guidelines

As automated content risk mitigation relies on classifiers to make decisions
about content in real time, a prerequisite to building these systems is to have
the following components:
- A **taxonomy** of risks that are of interest – these become the classes of a
classifier.
- A **risk guideline** that determines where we put the line between encouraged
and discouraged outputs for each risk category in the taxonomy.
Together with this model, we release an open taxonomy inspired by existing open
taxonomies such as those employed by Google, Microsoft and OpenAI in the hope
that it can be useful to the community. This taxonomy does not necessarily reflect Meta's
own internal policies and is meant to demonstrate the value of our method to
tune LLMs into classifiers that show high performance and high degrees of adaptability to different policies.

### The Llama-Guard Safety Taxonomy & Risk Guidelines

Below, we provide both the harm types themselves under this taxonomy and also examples of
the specific kinds of content that would be considered harmful under each category:

- **Violence & Hate** encompasses statements that encourage or could help people
plan or engage in violence. Similarly, statements that advocate
discrimination, contain slurs, or voice hateful sentiments against people
based on their sensitive personal characteristics (ex: race, color, religion,
national origin, sexual orientation, gender, gender identity, or disability)
would also be considered inappropriate under this category.
- **Sexual Content** encompasses statements encouraging someone (who could be
underage) to engage in specific sex acts. Similarly, sexually explicit (i.e.,
erotic) statements would also be considered inappropriate under this category.
- **Guns & Illegal Weapons** encompasses statements that specifically encourage,
condone, or could help people plan or execute specific crimes involving the
illegal acquisition, creation, or use of guns or illegal weapons (ex:
explosives, biological agents, or chemical weapons), including instructions on
how to create or use them.
- **Regulated or Controlled Substances** encompasses statements that
specifically encourage or could help people to illegally produce, transfer, or
consume regulated or controlled substances like illegal drugs, tobacco,
alcohol, or cannabis.
- **Suicide & Self Harm** encompasses statements that encourage, condone, or
enable people to harm themselves (ex: by providing instructions or information
on methods of self-harm). When people express or imply an intent to harm
themselves, any response other than one that provides links to appropriate
health resources would be considered inappropriate (even if entirely
supportive).
- **Criminal Planning** encompasses miscellaneous statements that encourage,
condone, or could help people plan or execute specific criminal activities,
like arson, kidnapping, or theft. Items should only be considered harmful
under this category when they could not be read as violating any of the other
harm types above (ex: statements that encourage violence should be considered
violating under Violence & Hate rather than this category).


## How to Use in `transformers`

```py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "meta-llama/LlamaGuard-7b"
device = "cuda"
dtype = torch.bfloat16

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype, device_map=device)

def moderate(chat):
    input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt").to(device)
    output = model.generate(input_ids=input_ids, max_new_tokens=100, pad_token_id=0)
    prompt_len = input_ids.shape[-1]
    return tokenizer.decode(output[0][prompt_len:], skip_special_tokens=True)

moderate([
    {"role": "user", "content": "I forgot how to kill a process in Linux, can you help?"},
    {"role": "assistant", "content": "Sure! To kill a process in Linux, you can use the kill command followed by the process ID (PID) of the process you want to terminate."},
])
# `safe`
```

You need to be logged in to the Hugging Face Hub to use the model.

For more details, see [this Colab notebook](https://colab.research.google.com/drive/16s0tlCSEDtczjPzdIK3jq0Le5LlnSYGf?usp=sharing).

## Evaluation results

We compare the performance of the model against standard content moderation APIs
in the industry, including
[OpenAI](https://platform.openai.com/docs/guides/moderation/overview), [Azure Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/harm-categories),and [PerspectiveAPI](https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages?language=en_US) from Google on both public and in-house benchmarks. The public benchmarks
include [ToxicChat](https://huggingface.co/datasets/lmsys/toxic-chat) and
[OpenAI Moderation](https://github.com/openai/moderation-api-release).

Note: comparisons are not exactly apples-to-apples due to mismatches in each
taxonomy. The interested reader can find a more detailed discussion about this
in our paper: [LINK TO PAPER].

| | Our Test Set (Prompt) | OpenAI Mod | ToxicChat | Our Test Set (Response) |
| --------------- | --------------------- | ---------- | --------- | ----------------------- |
| Llama-Guard | **0.945** | 0.847 | **0.626** | **0.953** |
| OpenAI API | 0.764 | **0.856** | 0.588 | 0.769 |
| Perspective API | 0.728 | 0.787 | 0.532 | 0.699 |
