---
language:
- zh
- en
- fr
- de
- ja
- ko
- it
- fi
license: apache-2.0
tags:
- llamaify
- qwen2.5
pipeline_tag: text-generation
model-index:
- name: openbuddy-qwen2.5llamaify-7b-v23.1-200k
  results:
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
      value: 56.73
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k
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
      value: 36.4
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k
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
      value: 11.4
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k
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
      value: 8.61
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k
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
      value: 13.81
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k
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
      value: 32.75
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k
      name: Open LLM Leaderboard
base_model: Qwen/Qwen2.5-7B-Instruct
---


# OpenBuddy - Open Multilingual Chatbot


GitHub and Usage Guide: [https://github.com/OpenBuddy/OpenBuddy](https://github.com/OpenBuddy/OpenBuddy)

Website and Demo: [https://openbuddy.ai](https://openbuddy.ai)

Evaluation result of this model: [Evaluation.txt](Evaluation.txt)

![Demo](https://raw.githubusercontent.com/OpenBuddy/OpenBuddy/main/media/demo.png)



# Copyright Notice

Base Model: Qwen2.5-7B-Chat

License: Apache 2.0

# Prompt Format

We recommend using the fast tokenizer from `transformers`, which should be enabled by default in the `transformers` and `vllm` libraries. Other implementations including `sentencepiece` may not work as expected, especially for special tokens like `<|role|>`, `<|says|>` and `<|end|>`.

```
<|role|>system<|says|>You(assistant) are a helpful, respectful and honest INTP-T AI Assistant named Buddy. You are talking to a human(user).
Always answer as helpfully and logically as possible, while being safe. Your answers should not include any harmful, political, religious, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
You cannot access the internet, but you have vast knowledge, cutoff: 2023-04.
You are trained by OpenBuddy team, (https://openbuddy.ai, https://github.com/OpenBuddy/OpenBuddy), not related to GPT or OpenAI.<|end|>
<|role|>user<|says|>History input 1<|end|>
<|role|>assistant<|says|>History output 1<|end|>
<|role|>user<|says|>History input 2<|end|>
<|role|>assistant<|says|>History output 2<|end|>
<|role|>user<|says|>Current input<|end|>
<|role|>assistant<|says|>
```


This format is also defined in `tokenizer_config.json`, which means you can directly use `vllm` to deploy an OpenAI-like API service. For more information, please refer to the [vllm documentation](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html).

## Disclaimer

All OpenBuddy models have inherent limitations and may potentially produce outputs that are erroneous, harmful, offensive, or otherwise undesirable. Users should not use these models in critical or high-stakes situations that may lead to personal injury, property damage, or significant losses. Examples of such scenarios include, but are not limited to, the medical field, controlling software and hardware systems that may cause harm, and making important financial or legal decisions.

OpenBuddy is provided "as-is" without any warranty of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors, contributors, or copyright holders be liable for any claim, damages, or other liabilities, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

By using OpenBuddy, you agree to these terms and conditions, and acknowledge that you understand the potential risks associated with its use. You also agree to indemnify and hold harmless the authors, contributors, and copyright holders from any claims, damages, or liabilities arising from your use of OpenBuddy.


## 免责声明

所有OpenBuddy模型均存在固有的局限性，可能产生错误的、有害的、冒犯性的或其他不良的输出。用户在关键或高风险场景中应谨慎行事，不要使用这些模型，以免导致人身伤害、财产损失或重大损失。此类场景的例子包括但不限于医疗领域、可能导致伤害的软硬件系统的控制以及进行重要的财务或法律决策。

OpenBuddy按“原样”提供，不附带任何种类的明示或暗示的保证，包括但不限于适销性、特定目的的适用性和非侵权的暗示保证。在任何情况下，作者、贡献者或版权所有者均不对因软件或使用或其他软件交易而产生的任何索赔、损害赔偿或其他责任（无论是合同、侵权还是其他原因）承担责任。

使用OpenBuddy即表示您同意这些条款和条件，并承认您了解其使用可能带来的潜在风险。您还同意赔偿并使作者、贡献者和版权所有者免受因您使用OpenBuddy而产生的任何索赔、损害赔偿或责任的影响。
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_OpenBuddy__openbuddy-qwen2.5llamaify-7b-v23.1-200k)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |26.62|
|IFEval (0-Shot)    |56.73|
|BBH (3-Shot)       |36.40|
|MATH Lvl 5 (4-Shot)|11.40|
|GPQA (0-shot)      | 8.61|
|MuSR (0-shot)      |13.81|
|MMLU-PRO (5-shot)  |32.75|