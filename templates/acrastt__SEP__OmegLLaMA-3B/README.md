---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- not-for-all-audiences
datasets:
- anon8231489123/Omegle_logs_dataset
pipeline_tag: text-generation
model-index:
- name: OmegLLaMA-3B
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
      value: 40.36
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/OmegLLaMA-3B
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
      value: 66.13
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/OmegLLaMA-3B
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
      value: 28.0
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/OmegLLaMA-3B
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
      value: 33.31
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/OmegLLaMA-3B
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
      value: 61.64
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/OmegLLaMA-3B
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
      value: 0.23
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/OmegLLaMA-3B
      name: Open LLM Leaderboard
---

<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [Xander Boyce](https://huggingface.co/takeraparterer)'s [OmegLLaMA LoRA](https://huggingface.co/takeraparterer/Omegllama) merged with [OpenLLama 3B](https://huggingface.co/openlm-research/open_llama_3b).

Prompt format:
```
Interests: {interests}
Conversation:
You: {prompt}
Stranger: 
```
For multiple interests, seperate them with space. Repeat You and Stranger for multi-turn conversations, which means Interests and Conversation are technically part of the system prompt.

GGUF quantizations available [here](https://huggingface.co/maddes8cht/acrastt-OmegLLaMA-3B-gguf).

This model is very good at NSFW ERP and sexting(For a 3B model). I recommend using this with [Faraday.dev](https://faraday.dev/) if you want ERP or sexting.

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__OmegLLaMA-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 38.28   |
| ARC (25-shot)         | 40.36          |
| HellaSwag (10-shot)   | 66.13    |
| MMLU (5-shot)         | 28.0         |
| TruthfulQA (0-shot)   | 33.31   |
| Winogrande (5-shot)   | 61.64   |
| GSM8K (5-shot)        | 0.23        |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__OmegLLaMA-3B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |38.28|
|AI2 Reasoning Challenge (25-Shot)|40.36|
|HellaSwag (10-Shot)              |66.13|
|MMLU (5-Shot)                    |28.00|
|TruthfulQA (0-shot)              |33.31|
|Winogrande (5-shot)              |61.64|
|GSM8k (5-shot)                   | 0.23|

