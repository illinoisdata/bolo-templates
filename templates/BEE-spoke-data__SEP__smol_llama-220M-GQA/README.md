---
language:
- en
license: apache-2.0
tags:
- smol_llama
- llama2
datasets:
- JeanKaddour/minipile
- pszemraj/simple_wikipedia_LM
- mattymchen/refinedweb-3m
- BEE-spoke-data/knowledge-inoc-concat-v1
inference:
  parameters:
    max_new_tokens: 64
    do_sample: true
    temperature: 0.8
    repetition_penalty: 1.05
    no_repeat_ngram_size: 4
    eta_cutoff: 0.0006
    renormalize_logits: true
widget:
- text: My name is El Microondas the Wise, and
  example_title: El Microondas
- text: Kennesaw State University is a public
  example_title: Kennesaw State University
- text: Bungie Studios is an American video game developer. They are most famous for
    developing the award winning Halo series of video games. They also made Destiny.
    The studio was founded
  example_title: Bungie
- text: The Mona Lisa is a world-renowned painting created by
  example_title: Mona Lisa
- text: The Harry Potter series, written by J.K. Rowling, begins with the book titled
  example_title: Harry Potter Series
- text: 'Question: I have cities, but no houses. I have mountains, but no trees. I
    have water, but no fish. What am I?

    Answer:'
  example_title: Riddle
- text: The process of photosynthesis involves the conversion of
  example_title: Photosynthesis
- text: Jane went to the store to buy some groceries. She picked up apples, oranges,
    and a loaf of bread. When she got home, she realized she forgot
  example_title: Story Continuation
- text: 'Problem 2: If a train leaves Station A at 9:00 AM and travels at 60 mph,
    and another train leaves Station B at 10:00 AM and travels at 80 mph, when will
    they meet if the distance between the stations is 300 miles?

    To determine'
  example_title: Math Problem
- text: In the context of computer programming, an algorithm is
  example_title: Algorithm Definition
pipeline_tag: text-generation
model-index:
- name: smol_llama-220M-GQA
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: AI2 Reasoning Challenge (25-Shot)
      type: ai2_arc
      config: ARC-Challenge
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: acc_norm
      value: 24.83
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: HellaSwag (10-Shot)
      type: hellaswag
      split: validation
      args:
        num_few_shot: 10
    metrics:
    - type: acc_norm
      value: 29.76
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU (5-Shot)
      type: cais/mmlu
      config: all
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 25.85
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: TruthfulQA (0-shot)
      type: truthful_qa
      config: multiple_choice
      split: validation
      args:
        num_few_shot: 0
    metrics:
    - type: mc2
      value: 44.55
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: Winogrande (5-shot)
      type: winogrande
      config: winogrande_xl
      split: validation
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 50.99
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GSM8k (5-shot)
      type: gsm8k
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 0.68
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 23.86
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 3.04
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 0.0
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 0.78
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 9.07
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 1.66
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=BEE-spoke-data/smol_llama-220M-GQA
      name: Open LLM Leaderboard
---


# smol_llama: 220M GQA


A small 220M param (total) decoder model. This is the first version of the model.

- 1024 hidden size, 10 layers
- GQA (32 heads, 8 key-value), context length 2048
- train-from-scratch on one GPU :)

## Links 

[Here](https://huggingface.co/collections/BEE-spoke-data/finetuned-smol-220m-65998b080ae723e79c830f83) are some fine-tunes we did, but there are many more possibilities out there!

- instruct
  - openhermes - [link](https://huggingface.co/BEE-spoke-data/smol_llama-220M-openhermes)
  - open-instruct - [link](https://huggingface.co/BEE-spoke-data/smol_llama-220M-open_instruct)
- code
  - python (pypi) - [link](https://huggingface.co/BEE-spoke-data/beecoder-220M-python)
- zephyr DPO tune
  - SFT - [link](https://huggingface.co/BEE-spoke-data/zephyr-220m-sft-full)
  - full DPO - [link](https://huggingface.co/BEE-spoke-data/zephyr-220m-dpo-full)

---

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_BEE-spoke-data__smol_llama-220M-GQA)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |29.44|
|AI2 Reasoning Challenge (25-Shot)|24.83|
|HellaSwag (10-Shot)              |29.76|
|MMLU (5-Shot)                    |25.85|
|TruthfulQA (0-shot)              |44.55|
|Winogrande (5-shot)              |50.99|
|GSM8k (5-shot)                   | 0.68|


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_BEE-spoke-data__smol_llama-220M-GQA)

|      Metric       |Value|
|-------------------|----:|
|Avg.               | 6.62|
|IFEval (0-Shot)    |23.86|
|BBH (3-Shot)       | 3.04|
|MATH Lvl 5 (4-Shot)| 0.00|
|GPQA (0-shot)      | 0.78|
|MuSR (0-shot)      | 9.07|
|MMLU-PRO (5-shot)  | 1.66|

