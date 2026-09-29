---
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
tags:
- llamafile
- facebook
- meta
- pytorch
- llama
- llama-3
license: llama3.2
license_link: LICENSE
quantized_by: jartine
---

# LLaMA 3.2 3B Instruct - llamafile

This is a large language model that was released by Meta on 2024-09-25.
This edition of LLaMA packs a lot of quality in a size small enough to
run on most computers with 8GB+ of RAM. See also its sister model
[Llama-3.2-1B-Instruct-llamafile](https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile).

- Model creator: [Meta](https://huggingface.co/meta-llama/)
- Original model: [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)

Mozilla packaged the LLaMA 3.2 models into executable weights that we
call [llamafiles](https://github.com/Mozilla-Ocho/llamafile). This gives
you the easiest fastest way to use the model on Linux, MacOS, Windows,
FreeBSD, OpenBSD and NetBSD systems you control on both AMD64 and ARM64.

*Software Last Updated: 2025-03-31*

*Llamafile Version: 0.9.2*

## Quickstart

To get started, you need both the LLaMA 3.2 weights, and the llamafile
software. Both of them are included in a single file, which can be
downloaded and run as follows:

```
wget https://huggingface.co/Mozilla/Llama-3.2-3B-Instruct-llamafile/resolve/main/Llama-3.2-3B-Instruct.Q6_K.llamafile
chmod +x Llama-3.2-3B-Instruct.Q6_K.llamafile
./Llama-3.2-3B-Instruct.Q6_K.llamafile
```

The default mode of operation for these llamafiles is our new command
line chatbot interface. It looks like this:

![Screenshot of LLaMA 3.2 3B on Windows.](llamafile-llama-3.2.png)

## Usage

You can use triple quotes to ask questions on multiple lines. You can
pass commands like `/stats` and `/context` to see runtime status
information. You can change the system prompt by passing the `-p "new
system prompt"` flag. You can press CTRL-C to interrupt the model.
Finally CTRL-D may be used to exit.

If you prefer to use a web GUI, then a `--server` mode is provided, that
will open a tab with a chatbot and completion interface in your browser.
For additional help on how it may be used, pass the `--help` flag. The
server also has an OpenAI API compatible completions endpoint that can
be accessed via Python using the `openai` pip package.

```
./Llama-3.2-3B-Instruct.Q6_K.llamafile --server
```

An advanced CLI mode is provided that's useful for shell scripting. You
can use it by passing the `--cli` flag. For additional help on how it
may be used, pass the `--help` flag.

```
./Llama-3.2-3B-Instruct.Q6_K.llamafile --cli -p 'four score and seven' --log-disable
```

## Troubleshooting

Having **trouble?** See the ["Gotchas"
section](https://github.com/mozilla-ocho/llamafile/?tab=readme-ov-file#gotchas-and-troubleshooting)
of the README.

On Linux, the way to avoid run-detector errors is to install the APE
interpreter.

```sh
sudo wget -O /usr/bin/ape https://cosmo.zip/pub/cosmos/bin/ape-$(uname -m).elf
sudo chmod +x /usr/bin/ape
sudo sh -c "echo ':APE:M::MZqFpD::/usr/bin/ape:' >/proc/sys/fs/binfmt_misc/register"
sudo sh -c "echo ':APE-jart:M::jartsr::/usr/bin/ape:' >/proc/sys/fs/binfmt_misc/register"
```

On Windows there's a 4GB limit on executable sizes. This means you
should download the Q6\_K llamafile.

## Context Window

This model has a max context window size of 128k tokens. By default, a
context window size of 8192 tokens is used, which for Q6\_K requires
3.4GB of RSS RAM in addition to the 2.8GB of memory needed by the
weights. You can ask llamafile to use the maximum context size by
passing the `-c 0` flag, which for LLaMA 3.2 is 131072 tokens and that
requires 16.4GB of RSS RAM. That's big enough for a small book. If you
want to be able to have a conversation with your book, you can use the
`-f book.txt` flag.

## GPU Acceleration

On GPUs with sufficient RAM, the `-ngl 999` flag may be passed to use
the system's NVIDIA or AMD GPU(s). On Windows, only the graphics card
driver needs to be installed if you own an NVIDIA GPU. On Windows, if
you have an AMD GPU, you should install the ROCm SDK v6.1 and then pass
the flags `--recompile --gpu amd` the first time you run your llamafile.

On NVIDIA GPUs, by default, the prebuilt tinyBLAS library is used to
perform matrix multiplications. This is open source software, but it
doesn't go as fast as closed source cuBLAS. If you have the CUDA SDK
installed on your system, then you can pass the `--recompile` flag to
build a GGML CUDA library just for your system that uses cuBLAS. This
ensures you get maximum performance.

For further information, please see the [llamafile
README](https://github.com/mozilla-ocho/llamafile/).

## CPU Benchmarks

Here's how fast you can expect these llamafiles to go on flagship CPUs.

- The "pp512" benchmark measures prompt processing speed. In other
  words, this tells you how quickly the llamafile reads text (higher is
  better).

- The "tg16" benchmark measures token generation speed. In other words,
  this tells you how quickly the llamafile writes text (higher is
  better).

| cpu\_info                                      | model\_filename                          | size       | test          | t/s             |
| :-----------------------------------------     | :--------------------------------------- | ---------: | ------------: | --------------: |
| AMD Ryzen Threadripper PRO 7995WX (znver4)     | Llama-3.2-3B-Instruct.BF16               | 6.72 GiB   | pp512         | 1230.02         |
| AMD Ryzen Threadripper PRO 7995WX (znver4)     | Llama-3.2-3B-Instruct.BF16               | 6.72 GiB   | tg16          | 34.17           |
| AMD Ryzen Threadripper PRO 7995WX (znver4)     | Llama-3.2-3B-Instruct.F16                | 6.72 GiB   | pp512         | 789.97          |
| AMD Ryzen Threadripper PRO 7995WX (znver4)     | Llama-3.2-3B-Instruct.F16                | 6.72 GiB   | tg16          | 33.97           |
| AMD Ryzen Threadripper PRO 7995WX (znver4)     | Llama-3.2-3B-Instruct.Q6\_K              | 2.76 GiB   | pp512         | 1192.03         |
| AMD Ryzen Threadripper PRO 7995WX (znver4)     | Llama-3.2-3B-Instruct.Q6\_K              | 2.76 GiB   | tg16          | 60.57           |
| Apple M2 Ultra (+fp16+dotprod)                 | Llama-3.2-3B-Instruct.BF16               | 6.72 GiB   | pp512         | 171.40          |
| Apple M2 Ultra (+fp16+dotprod)                 | Llama-3.2-3B-Instruct.BF16               | 6.72 GiB   | tg16          | 30.06           |
| Apple M2 Ultra (+fp16+dotprod)                 | Llama-3.2-3B-Instruct.F16                | 6.72 GiB   | pp512         | 405.41          |
| Apple M2 Ultra (+fp16+dotprod)                 | Llama-3.2-3B-Instruct.F16                | 6.72 GiB   | tg16          | 33.73           |
| Apple M2 Ultra (+fp16+dotprod)                 | Llama-3.2-3B-Instruct.Q6\_K              | 2.76 GiB   | pp512         | 240.36          |
| Apple M2 Ultra (+fp16+dotprod)                 | Llama-3.2-3B-Instruct.Q6\_K              | 2.76 GiB   | tg16          | 60.76           |
| Intel Core i9-14900K (alderlake)               | Llama-3.2-3B-Instruct.BF16               | 6.72 GiB   | pp512         | 136.95          |
| Intel Core i9-14900K (alderlake)               | Llama-3.2-3B-Instruct.BF16               | 6.72 GiB   | tg16          | 14.41           |
| Intel Core i9-14900K (alderlake)               | Llama-3.2-3B-Instruct.F16                | 6.72 GiB   | pp512         | 142.71          |
| Intel Core i9-14900K (alderlake)               | Llama-3.2-3B-Instruct.F16                | 6.72 GiB   | tg16          | 14.48           |
| Intel Core i9-14900K (alderlake)               | Llama-3.2-3B-Instruct.Q6\_K              | 2.76 GiB   | pp512         | 223.48          |
| Intel Core i9-14900K (alderlake)               | Llama-3.2-3B-Instruct.Q6\_K              | 2.76 GiB   | tg16          | 27.50           |
| Raspberry Pi 5 Model B Rev 1.0 (+fp16+dotprod) | Llama-3.2-3B-Instruct.BF16               | 6.72 GiB   | pp512         | 10.10           |
| Raspberry Pi 5 Model B Rev 1.0 (+fp16+dotprod) | Llama-3.2-3B-Instruct.BF16               | 6.72 GiB   | tg16          | 1.50            |
| Raspberry Pi 5 Model B Rev 1.0 (+fp16+dotprod) | Llama-3.2-3B-Instruct.F16                | 6.72 GiB   | pp512         | 17.31           |
| Raspberry Pi 5 Model B Rev 1.0 (+fp16+dotprod) | Llama-3.2-3B-Instruct.F16                | 6.72 GiB   | tg16          | 1.67            |
| Raspberry Pi 5 Model B Rev 1.0 (+fp16+dotprod) | Llama-3.2-3B-Instruct.Q6\_K              | 2.76 GiB   | pp512         | 15.79           |
| Raspberry Pi 5 Model B Rev 1.0 (+fp16+dotprod) | Llama-3.2-3B-Instruct.Q6\_K              | 2.76 GiB   | tg16          | 4.03            |

We see from these benchmarks that the Q6\_K weights are usually the best
choice, since they're both very high quality and always fast. In some
cases, the full quality BF16 and F16 might go faster or slower,
depending on your hardware platform. F16 is particularly good for
example on GPU and Raspberry Pi 5+. BF16 shines on AMD Zen 4+.

## About llamafile

llamafile is a new format introduced by Mozilla on Nov 20th 2023. It
uses Cosmopolitan Libc to turn LLM weights into runnable llama.cpp
binaries that run on the stock installs of six OSes for both ARM64 and
AMD64.

---

## Model Information

The Meta Llama 3.2 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction-tuned generative models in 1B and 3B sizes (text in/text out). The Llama 3.2 instruction-tuned text only models are optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks. They outperform many of the available open source and closed chat models on common industry benchmarks.

**Model Developer:** Meta

**Model Architecture:** Llama 3.2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for helpfulness and safety. 

|  | Training Data | Params | Input modalities | Output modalities | Context Length | GQA | Shared Embeddings | Token count | Knowledge cutoff |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Llama 3.2 (text only)  | A new mix of publicly available online data. | 1B (1.23B) | Multilingual Text | Multilingual Text and code  | 128k | Yes | Yes | Up to 9T tokens | December 2023 |
|  |  | 3B (3.21B) | Multilingual Text | Multilingual Text and code  |  |  |  |  |  |

**Supported Languages:** English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai are officially supported. Llama 3.2 has been trained on a broader collection of languages than these 8 supported languages. Developers may fine-tune Llama 3.2 models for languages beyond these supported languages, provided they comply with the Llama 3.2 Community License and the Acceptable Use Policy. Developers are always expected to ensure that their deployments, including those that involve additional languages, are completed safely and responsibly.

**Llama 3.2 Model Family:** Token counts refer to pretraining data only. All model versions use Grouped-Query Attention (GQA) for improved inference scalability.

**Model Release Date:** Sept 25, 2024

**Status:** This is a static model trained on an offline dataset. Future versions may be released that improve model capabilities and safety. 

**License:** Use of Llama 3.2 is governed by the [Llama 3.2 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE) (a custom, commercial license agreement).

**Feedback:** Where to send questions or comments about the model Instructions on how to provide feedback or comments on the model can be found in the model [README](https://github.com/meta-llama/llama-models/tree/main/models/llama3_2). For more technical information about generation parameters and recipes for how to use Llama 3.2 in applications, please go [here](https://github.com/meta-llama/llama-recipes). 

## Intended Use

**Intended Use Cases:** Llama 3.2 is intended for commercial and research use in multiple languages. Instruction tuned text only models are intended for assistant-like chat and agentic applications like knowledge retrieval and summarization, mobile AI powered writing assistants and query and prompt rewriting. Pretrained models can be adapted for a variety of additional natural language generation tasks. 

**Out of Scope:** Use in any manner that violates applicable laws or regulations (including trade compliance laws). Use in any other way that is prohibited by the Acceptable Use Policy and Llama 3.2 Community License. Use in languages beyond those explicitly referenced as supported in this model card.

## How to use

This repository contains two versions of Llama-3.2-1B, for use with transformers and with the original `llama` codebase.

### Use with transformers

Starting with transformers >= 4.43.0 onward, you can run conversational inference using the Transformers pipeline abstraction or by leveraging the Auto classes with the generate() function.

Make sure to update your transformers installation via pip install --upgrade transformers.

```python
import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-1B"

pipe = pipeline(
    "text-generation", 
    model=model_id, 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

pipe("The key to life is")
```

### Use with `llama`

Please, follow the instructions in the [repository](https://github.com/meta-llama/llama).

To download Original checkpoints, see the example command below leveraging `huggingface-cli`:

```
huggingface-cli download meta-llama/Llama-3.2-1B --include "original/*" --local-dir Llama-3.2-1B
```

## Hardware and Software

**Training Factors:** We used custom training libraries, Meta's custom built GPU cluster, and production infrastructure for pretraining. Fine-tuning, annotation, and evaluation were also performed on production infrastructure.

**Training Energy Use:** Training utilized a cumulative of **916k** GPU hours of computation on H100-80GB (TDP of 700W) type hardware, per the table below. Training time is the total GPU time required for training each model and power consumption is the peak power capacity per GPU device used, adjusted for power usage efficiency. 

## 

**Training Greenhouse Gas Emissions:** Estimated total location-based greenhouse gas emissions were **240** tons CO2eq for training. Since 2020, Meta has maintained net zero greenhouse gas emissions in its global operations and matched 100% of its electricity use with renewable energy; therefore, the total market-based greenhouse gas emissions for training were 0 tons CO2eq.

|  | Training Time (GPU hours) | Logit Generation Time (GPU Hours) | Training Power Consumption (W) | Training Location-Based Greenhouse Gas Emissions (tons CO2eq) | Training Market-Based Greenhouse Gas Emissions (tons CO2eq) |
| :---- | :---: | ----- | :---: | :---: | :---: |
| Llama 3.2 1B | 370k | \- | 700 | 107 | 0 |
| Llama 3.2 3B | 460k | \- | 700 | 133 | 0 |
| Total | 830k |         86k |  | 240 | 0 |

The methodology used to determine training energy use and greenhouse gas emissions can be found [here](https://arxiv.org/pdf/2204.05149). Since Meta is openly releasing these models, the training energy use and greenhouse gas emissions will not be incurred by others.

## Training Data

**Overview:** Llama 3.2 was pretrained on up to 9 trillion tokens of data from publicly available sources. For the 1B and 3B Llama 3.2 models, we incorporated logits from the Llama 3.1 8B and 70B models into the pretraining stage of the model development, where outputs (logits) from these larger models were used as token-level targets. Knowledge distillation was used after pruning to recover performance. In post-training we used a similar recipe as Llama 3.1 and produced final chat models by doing several rounds of alignment on top of the pre-trained model. Each round involved Supervised Fine-Tuning (SFT), Rejection Sampling (RS), and Direct Preference Optimization (DPO).

**Data Freshness:** The pretraining data has a cutoff of December 2023\.

## Benchmarks \- English Text

In this section, we report the results for Llama 3.2 models on standard automatic benchmarks. For all these evaluations, we used our internal evaluations library. 

### Base Pretrained Models 

| Category | Benchmark | \# Shots | Metric | Llama 3.2 1B | Llama 3.2 3B | Llama 3.1 8B |
| ----- | ----- | :---: | :---: | :---: | :---: | :---: |
| General | MMLU | 5 | macro\_avg/acc\_char | 32.2 | 58 | 66.7 |
|  | AGIEval English | 3-5 | average/acc\_char | 23.3 | 39.2 | 47.8 |
|  | ARC-Challenge | 25 | acc\_char | 32.8 | 69.1 | 79.7 |
| Reading comprehension | SQuAD | 1 | em | 49.2 | 67.7 | 77 |
|  | QuAC (F1) | 1 | f1 | 37.9 | 42.9 | 44.9 |
|  | DROP (F1) | 3 | f1 | 28.0 | 45.2 | 59.5 |
| Long Context | Needle in Haystack | 0 | em | 96.8 | 1 | 1 |

### Instruction Tuned Models

| Capability |  | Benchmark | \# Shots | Metric | Llama 3.2 1B | Llama 3.2 3B | Llama 3.1 8B |
| :---: | ----- | :---: | :---: | :---: | :---: | :---: | :---: |
| General |  | MMLU | 5 | macro\_avg/acc | 49.3 | 63.4 | 69.4 |
| Re-writing |  | Open-rewrite eval | 0 | micro\_avg/rougeL | 41.6 | 40.1 | 40.9 |
| Summarization |  | TLDR9+ (test) | 1 | rougeL | 16.8 | 19.0 | 17.2 |
| Instruction following |  | IFEval | 0 | avg(prompt/instruction acc loose/strict) | 59.5 | 77.4 | 80.4 |
| Math |  | GSM8K (CoT) | 8 | em\_maj1@1 | 44.4 | 77.7 | 84.5 |
|  |  | MATH (CoT) | 0 | final\_em | 30.6 | 47.3 | 51.9 |
| Reasoning |  | ARC-C | 0 | acc | 59.4 | 78.6 | 83.4 |
|  |  | GPQA | 0 | acc | 27.2 | 32.8 | 32.8 |
|  |  | Hellaswag | 0 | acc | 41.2 | 69.8 | 78.7 |
| Tool Use |  | BFCL V2 | 0 | acc | 25.7 | 67.0 | 70.9 |
|  |  | Nexus | 0 | macro\_avg/acc | 13.5 | 34.3 | 38.5 |
| Long Context |  | InfiniteBench/En.QA | 0 | longbook\_qa/f1 | 20.3 | 19.8 | 27.3 |
|  |  | InfiniteBench/En.MC | 0 | longbook\_choice/acc | 38.0 | 63.3 | 72.2 |
|  |  | NIH/Multi-needle | 0 | recall | 75.0 | 84.7 | 98.8 |
| Multilingual |  | MGSM (CoT) | 0 | em | 24.5 | 58.2 | 68.9 |

### Multilingual Benchmarks

| Category | Benchmark | Language | Llama 3.2 1B | Llama 3.2 3B | Llama 3.1 8B |
| :---: | :---: | :---: | :---: | :---: | :---: |
| General | MMLU (5-shot, macro\_avg/acc) | Portuguese | 39.82 | 54.48 | 62.12 |
|  |  | Spanish | 41.5 | 55.1 | 62.5 |
|  |  | Italian | 39.8 | 53.8 | 61.6 |
|  |  | German | 39.2 | 53.3 | 60.6 |
|  |  | French | 40.5 | 54.6 | 62.3 |
|  |  | Hindi | 33.5 | 43.3 | 50.9 |
|  |  | Thai | 34.7 | 44.5 | 50.3 |

## Responsibility & Safety

As part of our Responsible release approach, we followed a three-pronged strategy to managing trust & safety risks:

1. Enable developers to deploy helpful, safe and flexible experiences for their target audience and for the use cases supported by Llama   
2. Protect developers against adversarial users aiming to exploit Llama capabilities to potentially cause harm  
3. Provide protections for the community to help prevent the misuse of our models

### Responsible Deployment 

**Approach:** Llama is a foundational technology designed to be used in a variety of use cases. Examples on how Meta’s Llama models have been responsibly deployed can be found in our [Community Stories webpage](https://llama.meta.com/community-stories/). Our approach is to build the most helpful models, enabling the world to benefit from the technology power, by aligning our model safety for generic use cases and addressing a standard set of harms. Developers are then in the driver’s seat to tailor safety for their use cases, defining their own policies and deploying the models with the necessary safeguards in their Llama systems. Llama 3.2 was developed following the best practices outlined in our [Responsible Use Guide](https://llama.meta.com/responsible-use-guide/). 

#### Llama 3.2 Instruct 

**Objective:** Our main objectives for conducting safety fine-tuning are to provide the research community with a valuable resource for studying the robustness of safety fine-tuning, as well as to offer developers a readily available, safe, and powerful model for various applications to reduce the developer workload to deploy safe AI systems. We implemented the same set of safety mitigations as in Llama 3, and you can learn more about these in the Llama 3 [paper](https://ai.meta.com/research/publications/the-llama-3-herd-of-models/). 

**Fine-Tuning Data:** We employ a multi-faceted approach to data collection, combining human-generated data from our vendors with synthetic data to mitigate potential safety risks. We’ve developed many large language model (LLM)-based classifiers that enable us to thoughtfully select high-quality prompts and responses, enhancing data quality control. 

**Refusals and Tone:** Building on the work we started with Llama 3, we put a great emphasis on model refusals to benign prompts as well as refusal tone. We included both borderline and adversarial prompts in our safety data strategy, and modified our safety data responses to follow tone guidelines. 

#### Llama 3.2 Systems

**Safety as a System:** Large language models, including Llama 3.2, **are not designed to be deployed in isolation** but instead should be deployed as part of an overall AI system with additional safety guardrails as required. Developers are expected to deploy system safeguards when building agentic systems. Safeguards are key to achieve the right helpfulness-safety alignment as well as mitigating safety and security risks inherent to the system and any integration of the model or system with external tools. As part of our responsible release approach, we provide the community with [safeguards](https://llama.meta.com/trust-and-safety/) that developers should deploy with Llama models or other LLMs, including Llama Guard, Prompt Guard and Code Shield. All our [reference implementations](https://github.com/meta-llama/llama-agentic-system) demos contain these safeguards by default so developers can benefit from system-level safety out-of-the-box. 

### New Capabilities and Use Cases

**Technological Advancement:** Llama releases usually introduce new capabilities that require specific considerations in addition to the best practices that generally apply across all Generative AI use cases. For prior release capabilities also supported by Llama 3.2, see [Llama 3.1 Model Card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md), as the same considerations apply here as well.

**Constrained Environments:** Llama 3.2 1B and 3B models are expected to be deployed in highly constrained environments, such as mobile devices. LLM Systems using smaller models will have a different alignment profile and safety/helpfulness tradeoff than more complex, larger systems. Developers should ensure the safety of their system meets the requirements of their use case. We recommend using lighter system safeguards for such use cases, like Llama Guard 3-1B or its mobile-optimized version. 

### Evaluations

**Scaled Evaluations:** We built dedicated, adversarial evaluation datasets and evaluated systems composed of Llama models and Purple Llama safeguards to filter input prompt and output response. It is important to evaluate applications in context, and we recommend building dedicated evaluation dataset for your use case.

**Red Teaming:** We conducted recurring red teaming exercises with the goal of discovering risks via adversarial prompting and we used the learnings to improve our benchmarks and safety tuning datasets. We partnered early with subject-matter experts in critical risk areas to understand the nature of these real-world harms and how such models may lead to unintended harm for society. Based on these conversations, we derived a set of adversarial goals for the red team to attempt to achieve, such as extracting harmful information or reprogramming the model to act in a potentially harmful capacity. The red team consisted of experts in cybersecurity, adversarial machine learning, responsible AI, and integrity in addition to multilingual content specialists with background in integrity issues in specific geographic markets.

### Critical Risks 

In addition to our safety work above, we took extra care on measuring and/or mitigating the following critical risk areas:

**1\. CBRNE (Chemical, Biological, Radiological, Nuclear, and Explosive Weapons):** Llama 3.2 1B and 3B models are smaller and less capable derivatives of Llama 3.1. For Llama 3.1 70B and 405B, to assess risks related to proliferation of chemical and biological weapons, we performed uplift testing designed to assess whether use of Llama 3.1 models could meaningfully increase the capabilities of malicious actors to plan or carry out attacks using these types of weapons and have determined that such testing also applies to the smaller 1B and 3B models. 

**2\. Child Safety:** Child Safety risk assessments were conducted using a team of experts, to assess the model’s capability to produce outputs that could result in Child Safety risks and inform on any necessary and appropriate risk mitigations via fine tuning. We leveraged those expert red teaming sessions to expand the coverage of our evaluation benchmarks through Llama 3 model development. For Llama 3, we conducted new in-depth sessions using objective based methodologies to assess the model risks along multiple attack vectors including the additional languages Llama 3 is trained on. We also partnered with content specialists to perform red teaming exercises assessing potentially violating content while taking account of market specific nuances or experiences. 

**3\. Cyber Attacks:** For Llama 3.1 405B, our cyber attack uplift study investigated whether LLMs can enhance human capabilities in hacking tasks, both in terms of skill level and speed.
Our attack automation study focused on evaluating the capabilities of LLMs when used as autonomous agents in cyber offensive operations, specifically in the context of ransomware attacks. This evaluation was distinct from previous studies that considered LLMs as interactive assistants. The primary objective was to assess whether these models could effectively function as independent agents in executing complex cyber-attacks without human intervention. Because Llama 3.2’s 1B and 3B models are smaller and less capable models than Llama 3.1 405B, we broadly believe that the testing conducted for the 405B model also applies to Llama 3.2 models.

### Community 

**Industry Partnerships:** Generative AI safety requires expertise and tooling, and we believe in the strength of the open community to accelerate its progress. We are active members of open consortiums, including the AI Alliance, Partnership on AI and MLCommons, actively contributing to safety standardization and transparency. We encourage the community to adopt taxonomies like the MLCommons Proof of Concept evaluation to facilitate collaboration and transparency on safety and content evaluations. Our Purple Llama tools are open sourced for the community to use and widely distributed across ecosystem partners including cloud service providers. We encourage community contributions to our [Github repository](https://github.com/meta-llama/PurpleLlama).

**Grants:** We also set up the [Llama Impact Grants](https://llama.meta.com/llama-impact-grants/) program to identify and support the most compelling applications of Meta’s Llama model for societal benefit across three categories: education, climate and open innovation. The 20 finalists from the hundreds of applications can be found [here](https://llama.meta.com/llama-impact-grants/#finalists). 

**Reporting:** Finally, we put in place a set of resources including an [output reporting mechanism](https://developers.facebook.com/llama_output_feedback) and [bug bounty program](https://www.facebook.com/whitehat) to continuously improve the Llama technology with the help of the community.

## Ethical Considerations and Limitations

**Values:** The core values of Llama 3.2 are openness, inclusivity and helpfulness. It is meant to serve everyone, and to work for a wide range of use cases. It is thus designed to be accessible to people across many different backgrounds, experiences and perspectives. Llama 3.2 addresses users and their needs as they are, without insertion unnecessary judgment or normativity, while reflecting the understanding that even content that may appear problematic in some cases can serve valuable purposes in others. It respects the dignity and autonomy of all users, especially in terms of the values of free thought and expression that power innovation and progress. 

**Testing:** Llama 3.2 is a new technology, and like any new technology, there are risks associated with its use. Testing conducted to date has not covered, nor could it cover, all scenarios. For these reasons, as with all LLMs, Llama 3.2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 3.2 models, developers should perform safety testing and tuning tailored to their specific applications of the model. Please refer to available resources including our [Responsible Use Guide](https://llama.meta.com/responsible-use-guide), [Trust and Safety](https://llama.meta.com/trust-and-safety/) solutions, and other [resources](https://llama.meta.com/docs/get-started/) to learn more about responsible development.