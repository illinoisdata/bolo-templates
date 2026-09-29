---
language:
- en
license: apache-2.0
model-index:
- name: Tiny-Vicuna-1B
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
      value: 33.45
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Jiayi-Pan/Tiny-Vicuna-1B
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
      value: 55.92
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Jiayi-Pan/Tiny-Vicuna-1B
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
      value: 25.45
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Jiayi-Pan/Tiny-Vicuna-1B
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
      value: 33.82
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Jiayi-Pan/Tiny-Vicuna-1B
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
      value: 58.41
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Jiayi-Pan/Tiny-Vicuna-1B
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
      value: 1.52
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Jiayi-Pan/Tiny-Vicuna-1B
      name: Open LLM Leaderboard
---
# Tiny Vicuna 1B
This model is a fine-tuned version of [TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-intermediate-step-955k-token-2T) on [WizardVicuna Dataset](https://github.com/melodysdreamj/WizardVicunaLM).
It should be fully compatible with Vicuna-v1.5 series.


This model is easy to iterate on for early experiments!
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Jiayi-Pan__Tiny-Vicuna-1B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |34.76|
|AI2 Reasoning Challenge (25-Shot)|33.45|
|HellaSwag (10-Shot)              |55.92|
|MMLU (5-Shot)                    |25.45|
|TruthfulQA (0-shot)              |33.82|
|Winogrande (5-shot)              |58.41|
|GSM8k (5-shot)                   | 1.52|

