---
language:
- en
license: apache-2.0
library_name: transformers
datasets:
- 64bits/lima_vicuna_format
pipeline_tag: text-generation
model-index:
- name: Bean-3B
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
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Bean-3B
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
      value: 72.0
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Bean-3B
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
      value: 26.43
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Bean-3B
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
      value: 36.11
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Bean-3B
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
      value: 65.67
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Bean-3B
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
      value: 0.53
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Bean-3B
      name: Open LLM Leaderboard
---

<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [OpenLLaMA 3B V2](https://huggingface.co/openlm-research/open_llama_3b_v2) finetuned on [LIMA(ShareGPT format)](https://huggingface.co/datasets/64bits/lima_vicuna_format) for 2 epochs.

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
GGUF quantizations available [here](https://huggingface.co/maddes8cht/acrastt-Bean-3B-gguf).

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Bean-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 40.18   |
| ARC (25-shot)         | 40.36          |
| HellaSwag (10-shot)   | 72.0    |
| MMLU (5-shot)         | 26.43         |
| TruthfulQA (0-shot)   | 36.11   |
| Winogrande (5-shot)   | 65.67   |
| GSM8K (5-shot)        | 0.53        |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Bean-3B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |40.18|
|AI2 Reasoning Challenge (25-Shot)|40.36|
|HellaSwag (10-Shot)              |72.00|
|MMLU (5-Shot)                    |26.43|
|TruthfulQA (0-shot)              |36.11|
|Winogrande (5-shot)              |65.67|
|GSM8k (5-shot)                   | 0.53|

