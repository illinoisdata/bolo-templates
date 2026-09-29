---
language:
- en
license: apache-2.0
library_name: transformers
datasets:
- totally-not-an-llm/sharegpt-hyperfiltered-3k
pipeline_tag: text-generation
model-index:
- name: Puma-3B
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
      value: 41.3
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Puma-3B
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
      value: 71.85
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Puma-3B
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
      value: 27.51
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Puma-3B
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
      value: 38.34
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Puma-3B
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
      value: 66.38
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Puma-3B
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
      value: 0.76
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Puma-3B
      name: Open LLM Leaderboard
---

<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [OpenLLaMA 3B V2](https://huggingface.co/openlm-research/open_llama_3b_v2) finetuned on [ShareGPT Hyperfiltered](https://huggingface.co/datasets/totally-not-an-llm/sharegpt-hyperfiltered-3k) for 1 epochs.

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
GGML quants available [here](https://huggingface.co/TheBloke/Puma-3b-GGML).</br>
GPTQ quants available [here](https://huggingface.co/TheBloke/Puma-3b-GPTQ).

Note: Don't expect this model to be good, I was just starting out to finetune. So don't roast me please!

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Puma-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 41.02   |
| ARC (25-shot)         | 41.3          |
| HellaSwag (10-shot)   | 71.85    |
| MMLU (5-shot)         | 27.51         |
| TruthfulQA (0-shot)   | 38.34   |
| Winogrande (5-shot)   | 66.38   |
| GSM8K (5-shot)        | 0.76        |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Puma-3B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |41.02|
|AI2 Reasoning Challenge (25-Shot)|41.30|
|HellaSwag (10-Shot)              |71.85|
|MMLU (5-Shot)                    |27.51|
|TruthfulQA (0-shot)              |38.34|
|Winogrande (5-shot)              |66.38|
|GSM8k (5-shot)                   | 0.76|

