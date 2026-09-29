---
language:
- en
license: apache-2.0
library_name: transformers
datasets:
- LDJnr/Puffin
pipeline_tag: text-generation
model-index:
- name: Griffin-3B
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
      value: 41.81
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Griffin-3B
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
      value: 72.3
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Griffin-3B
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
      value: 26.36
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Griffin-3B
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
      value: 38.33
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Griffin-3B
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
      value: 67.01
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Griffin-3B
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
      value: 0.99
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Griffin-3B
      name: Open LLM Leaderboard
---

<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [OpenLLaMA 3B V2](https://huggingface.co/openlm-research/open_llama_3b_v2) finetuned on [Puffin](https://huggingface.co/datasets/LDJnr/Puffin) for 1 epochs.

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
GGML quants available [here](https://huggingface.co/TheBloke/Griffin-3B-GGML).</br>
GPTQ quants available [here](https://huggingface.co/TheBloke/Griffin-3B-GPTQ).

Note: Don't expect this model to be good, I was just starting out to finetune. So don't roast me please!

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Griffin-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 41.13   |
| ARC (25-shot)         | 41.81          |
| HellaSwag (10-shot)   | 72.3    |
| MMLU (5-shot)         | 26.36         |
| TruthfulQA (0-shot)   | 38.33   |
| Winogrande (5-shot)   | 67.01   |
| GSM8K (5-shot)        | 0.99        |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Griffin-3B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |41.13|
|AI2 Reasoning Challenge (25-Shot)|41.81|
|HellaSwag (10-Shot)              |72.30|
|MMLU (5-Shot)                    |26.36|
|TruthfulQA (0-shot)              |38.33|
|Winogrande (5-shot)              |67.01|
|GSM8k (5-shot)                   | 0.99|

