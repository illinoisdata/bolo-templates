---
language:
- en
license: apache-2.0
library_name: transformers
datasets:
- totally-not-an-llm/EverythingLM-data-V2-sharegpt
model-index:
- name: Marx-3B-V2
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
      value: 44.03
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Marx-3B-V2
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
      value: 72.92
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Marx-3B-V2
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
      value: 27.84
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Marx-3B-V2
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
      value: 39.92
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Marx-3B-V2
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
      value: 66.54
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Marx-3B-V2
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
      value: 1.21
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=acrastt/Marx-3B-V2
      name: Open LLM Leaderboard
---
<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [OpenLLaMA 3B V2](https://huggingface.co/openlm-research/open_llama_3b_v2) finetuned on [EverythingLM Data V2(ShareGPT format)](https://huggingface.co/datasets/totally-not-an-llm/EverythingLM-data-V2-sharegpt) for 2 epochs.

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
q4_1 GGML quant available [here](https://huggingface.co/NikolayKozloff/Marx-3B-V2/).</br>
q4_1 GGUF quant available [here]( https://huggingface.co/NikolayKozloff/Marx-3B-V2-GGUF/).

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Marx-3B-V2)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |42.08|
|AI2 Reasoning Challenge (25-Shot)|44.03|
|HellaSwag (10-Shot)              |72.92|
|MMLU (5-Shot)                    |27.84|
|TruthfulQA (0-shot)              |39.92|
|Winogrande (5-shot)              |66.54|
|GSM8k (5-shot)                   | 1.21|

