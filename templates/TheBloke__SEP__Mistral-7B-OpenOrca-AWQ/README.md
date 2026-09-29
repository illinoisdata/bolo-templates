---
base_model: Open-Orca/Mistral-7B-OpenOrca
datasets:
- Open-Orca/OpenOrca
inference: false
language:
- en
library_name: transformers
license: apache-2.0
model_creator: OpenOrca
model_name: Mistral 7B OpenOrca
model_type: mistral
pipeline_tag: text-generation
prompt_template: '<|im_start|>system

  {system_message}<|im_end|>

  <|im_start|>user

  {prompt}<|im_end|>

  <|im_start|>assistant

  '
quantized_by: TheBloke
---

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

# Mistral 7B OpenOrca - AWQ
- Model creator: [OpenOrca](https://huggingface.co/Open-Orca)
- Original model: [Mistral 7B OpenOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca)

<!-- description start -->
## Description

This repo contains AWQ model files for [OpenOrca's Mistral 7B OpenOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca).


### About AWQ

AWQ is an efficient, accurate and blazing-fast low-bit weight quantization method, currently supporting 4-bit quantization. Compared to GPTQ, it offers faster Transformers-based inference.

It is also now supported by continuous batching server [vLLM](https://github.com/vllm-project/vllm), allowing use of Llama AWQ models for high-throughput concurrent inference in multi-user server scenarios.

As of September 25th 2023, preliminary Llama-only AWQ support has also been added to [Huggingface Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference).

Note that, at the time of writing, overall throughput is still lower than running vLLM or TGI with unquantised models, however using AWQ enables using much smaller GPUs which can lead to easier deployment and overall cost savings. For example, a 70B model can be run on 1 x 48GB GPU instead of 2 x 80GB.
<!-- description end -->
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF)
* [OpenOrca's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: ChatML

```
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

<!-- prompt-template end -->


<!-- README_AWQ.md-provided-files start -->
## Provided files, and AWQ parameters

For my first release of AWQ models, I am releasing 128g models only. I will consider adding 32g as well if there is interest, and once I have done perplexity and evaluation comparisons, but at this time 32g models are still not fully tested with AutoAWQ and vLLM.

Models are released as sharded safetensors files.

| Branch | Bits | GS | AWQ Dataset | Seq Len | Size |
| ------ | ---- | -- | ----------- | ------- | ---- |
| [main](https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-AWQ/tree/main) | 4 | 128 | [wikitext](https://huggingface.co/datasets/wikitext/viewer/wikitext-2-v1/test) | 32768 | 4.15 GB

<!-- README_AWQ.md-provided-files end -->

<!-- README_AWQ.md-use-from-vllm start -->
## Serving this model from vLLM

Documentation on installing and using vLLM [can be found here](https://vllm.readthedocs.io/en/latest/).

Note: at the time of writing, vLLM has not yet done a new release with AWQ support.

If you try the vLLM examples below and get an error about `quantization` being unrecognised, or other AWQ-related issues, please install vLLM from Github source.

- When using vLLM as a server, pass the `--quantization awq` parameter, for example:

```shell
python3 python -m vllm.entrypoints.api_server --model TheBloke/Mistral-7B-OpenOrca-AWQ --quantization awq --dtype half
```

When using vLLM from Python code, pass the `quantization=awq` parameter, for example:

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(model="TheBloke/Mistral-7B-OpenOrca-AWQ", quantization="awq", dtype="half")

outputs = llm.generate(prompts, sampling_params)

# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```
<!-- README_AWQ.md-use-from-vllm start -->

<!-- README_AWQ.md-use-from-tgi start -->
## Serving this model from Text Generation Inference (TGI)

Use TGI version 1.1.0 or later. The official Docker container is: `ghcr.io/huggingface/text-generation-inference:1.1.0`

Example Docker parameters:

```shell
--model-id TheBloke/Mistral-7B-OpenOrca-AWQ --port 3000 --quantize awq --max-input-length 3696 --max-total-tokens 4096 --max-batch-prefill-tokens 4096
```

Example Python code for interfacing with TGI (requires huggingface-hub 0.17.0 or later):

```shell
pip3 install huggingface-hub
```

```python
from huggingface_hub import InferenceClient

endpoint_url = "https://your-endpoint-url-here"

prompt = "Tell me about AI"
prompt_template=f'''<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

'''

client = InferenceClient(endpoint_url)
response = client.text_generation(prompt,
                                  max_new_tokens=128,
                                  do_sample=True,
                                  temperature=0.7,
                                  top_p=0.95,
                                  top_k=40,
                                  repetition_penalty=1.1)

print(f"Model output: {response}")
```
<!-- README_AWQ.md-use-from-tgi end -->

<!-- README_AWQ.md-use-from-python start -->
## How to use this AWQ model from Python code

### Install the necessary packages

Requires: [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) 0.1.1 or later

```shell
pip3 install autoawq
```

If you have problems installing [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) using the pre-built wheels, install it from source instead:

```shell
pip3 uninstall -y autoawq
git clone https://github.com/casper-hansen/AutoAWQ
cd AutoAWQ
pip3 install .
```

### You can then try the following example code

```python
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

model_name_or_path = "TheBloke/Mistral-7B-OpenOrca-AWQ"

# Load model
model = AutoAWQForCausalLM.from_quantized(model_name_or_path, fuse_layers=True,
                                          trust_remote_code=False, safetensors=True)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=False)

prompt = "Tell me about AI"
prompt_template=f'''<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

'''

print("\n\n*** Generate:")

tokens = tokenizer(
    prompt_template,
    return_tensors='pt'
).input_ids.cuda()

# Generate output
generation_output = model.generate(
    tokens,
    do_sample=True,
    temperature=0.7,
    top_p=0.95,
    top_k=40,
    max_new_tokens=512
)

print("Output: ", tokenizer.decode(generation_output[0]))

"""
# Inference should be possible with transformers pipeline as well in future
# But currently this is not yet supported by AutoAWQ (correct as of September 25th 2023)
from transformers import pipeline

print("*** Pipeline:")
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_p=0.95,
    top_k=40,
    repetition_penalty=1.1
)

print(pipe(prompt_template)[0]['generated_text'])
"""
```
<!-- README_AWQ.md-use-from-python end -->

<!-- README_AWQ.md-compatibility start -->
## Compatibility

The files provided are tested to work with:

- [AutoAWQ](https://github.com/casper-hansen/AutoAWQ)
- [vLLM](https://github.com/vllm-project/vllm)
- [Huggingface Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference)

TGI merged AWQ support on September 25th, 2023: [TGI PR #1054](https://github.com/huggingface/text-generation-inference/pull/1054).  Use the `:latest` Docker container until the next TGI release is made.

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

**Patreon special mentions**: Pierre Kircher, Stanislav Ovsiannikov, Michael Levine, Eugene Pentland, Andrey, 준교 김, Randy H, Fred von Graf, Artur Olbinski, Caitlyn Gatomon, terasurfer, Jeff Scroggin, James Bentley, Vadim, Gabriel Puliatti, Harry Royden McLaughlin, Sean Connelly, Dan Guido, Edmond Seymore, Alicia Loh, subjectnull, AzureBlack, Manuel Alberto Morcote, Thomas Belote, Lone Striker, Chris Smitley, Vitor Caleffi, Johann-Peter Hartmann, Clay Pascal, biorpg, Brandon Frisco, sidney chen, transmissions 11, Pedro Madruga, jinyuan sun, Ajan Kanaga, Emad Mostaque, Trenton Dambrowitz, Jonathan Leane, Iucharbius, usrbinkat, vamX, George Stoitzev, Luke Pendergrass, theTransient, Olakabola, Swaroop Kallakuri, Cap'n Zoog, Brandon Phillips, Michael Dempsey, Nikolai Manek, danny, Matthew Berman, Gabriel Tamborski, alfie_i, Raymond Fosdick, Tom X Nguyen, Raven Klaugh, LangChain4j, Magnesian, Illia Dulskyi, David Ziegler, Mano Prime, Luis Javier Navarrete Lozano, Erik Bjäreholt, 阿明, Nathan Dryer, Alex, Rainer Wilmers, zynix, TL, Joseph William Delisle, John Villwock, Nathan LeClaire, Willem Michiel, Joguhyik, GodLy, OG, Alps Aficionado, Jeffrey Morgan, ReadyPlayerEmma, Tiffany J. Kim, Sebastain Graf, Spencer Kim, Michael Davis, webtim, Talal Aujan, knownsqashed, John Detwiler, Imad Khwaja, Deo Leter, Jerry Meng, Elijah Stavena, Rooh Singh, Pieter, SuperWojo, Alexandros Triantafyllidis, Stephen Murray, Ai Maven, ya boyyy, Enrico Ros, Ken Nordquist, Deep Realms, Nicholas, Spiking Neurons AB, Elle, Will Dee, Jack West, RoA, Luke @flexchar, Viktor Bowallius, Derek Yates, Subspace Studios, jjj, Toran Billups, Asp the Wyvern, Fen Risland, Ilya, NimbleBox.ai, Chadd, Nitin Borwankar, Emre, Mandus, Leonard Tan, Kalila, K, Trailburnt, S_X, Cory Kujawski


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

# Original model card: OpenOrca's Mistral 7B OpenOrca


<p><h1>🐋 TBD 🐋</h1></p>


![OpenOrca Logo](https://huggingface.co/datasets/Open-Orca/OpenOrca/resolve/main/OpenOrcaLogo.png "OpenOrca Logo")
[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)


# OpenOrca - Mistral - 7B - 8k

We have used our own [OpenOrca dataset](https://huggingface.co/datasets/Open-Orca/OpenOrca) to fine-tune on top of [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1). 
This dataset is our attempt to reproduce the dataset generated for Microsoft Research's [Orca Paper](https://arxiv.org/abs/2306.02707).
We use [OpenChat](https://huggingface.co/openchat) packing, trained with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl).

This release is trained on a curated filtered subset of most of our GPT-4 augmented data.
It is the same subset of our data as was used in our [OpenOrcaxOpenChat-Preview2-13B model](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B).

HF Leaderboard evals place this model as #2 for all models smaller than 30B at release time, outperforming all but one 13B model.

TBD

Want to visualize our full (pre-filtering) dataset? Check out our [Nomic Atlas Map](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2).

[<img src="https://huggingface.co/Open-Orca/OpenOrca-Preview1-13B/resolve/main/OpenOrca%20Nomic%20Atlas.png" alt="Atlas Nomic Dataset Map" width="400" height="400" />](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2)


We are in-process with training more models, so keep a look out on our org for releases coming soon with exciting partners.

We will also give sneak-peak announcements on our Discord, which you can find here:

https://AlignmentLab.ai

or on the OpenAccess AI Collective Discord for more information about Axolotl trainer here:

https://discord.gg/5y8STgB3P3

# Prompt Template

We used [OpenAI's Chat Markup Language (ChatML)](https://github.com/openai/openai-python/blob/main/chatml.md) format, with `<|im_start|>` and `<|im_end|>` tokens added to support this.

## Example Prompt Exchange

TBD

# Evaluation

We have evaluated using the methodology and tools for the HuggingFace Leaderboard, and find that we have significantly improved upon the base model.

TBD

## HuggingFaceH4 Open LLM Leaderboard Performance

TBD

## GPT4ALL Leaderboard Performance

TBD

# Dataset

We used a curated, filtered selection of most of the GPT-4 augmented data from our OpenOrca dataset, which aims to reproduce the Orca Research Paper dataset.


# Training

We trained with 8x A6000 GPUs for 62 hours, completing 4 epochs of full fine tuning on our dataset in one training run.
Commodity cost was ~$400.

# Citation

```bibtex
@misc{mukherjee2023orca,
      title={Orca: Progressive Learning from Complex Explanation Traces of GPT-4}, 
      author={Subhabrata Mukherjee and Arindam Mitra and Ganesh Jawahar and Sahaj Agarwal and Hamid Palangi and Ahmed Awadallah},
      year={2023},
      eprint={2306.02707},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@misc{longpre2023flan,
      title={The Flan Collection: Designing Data and Methods for Effective Instruction Tuning}, 
      author={Shayne Longpre and Le Hou and Tu Vu and Albert Webson and Hyung Won Chung and Yi Tay and Denny Zhou and Quoc V. Le and Barret Zoph and Jason Wei and Adam Roberts},
      year={2023},
      eprint={2301.13688},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
