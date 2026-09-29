---
license: apache-2.0
---

# Eurus-2-7B-SFT

## Links

- 📜 [Paper](https://arxiv.org/abs/2502.01456)
- 📜 [Blog](https://curvy-check-498.notion.site/Process-Reinforcement-through-Implicit-Rewards-15f4fcb9c42180f1b498cc9b2eaf896f)
- 🤗 [PRIME Collection](https://huggingface.co/PRIME-RL)
- 🤗 [SFT Data](https://huggingface.co/datasets/PRIME-RL/Eurus-2-SFT-Data) 

## Introduction

Eurus-2-7B-SFT is fine-tuned from [Qwen2.5-Math-7B-Base](https://huggingface.co/Qwen/Qwen2.5-Math-7B) for its great mathematical capabilities. It trains on [Eurus-2-SFT-Data](https://huggingface.co/datasets/PRIME-RL/Eurus-2-SFT-Data), which is an action-centric chain-of-thought reasoning dataset.

We apply imitation learning (supervised finetuning) as a warmup stage to teach models to learn reasoning patterns, , serving as a starter model for [Eurus-2-7B-PRIME](https://huggingface.co/PRIME-RL/Eurus-2-7B-PRIME). 

## Usage

We apply tailored prompts for coding and math task:

**Coding**

```
{question} + "\n\nWrite Python code to solve the problem. Present the code in \n```python\nYour code\n```\nat the end."
```

**Math**

```
{question} + "\n\nPresent the answer in LaTex format: \\boxed{Your answer}"
```

```python
import os
from tqdm import tqdm
import torch
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams
os.environ["NCCL_IGNORE_DISABLED_P2P"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "true"
def generate(question_list,model_path):
    llm = LLM(
        model=model_path,
        trust_remote_code=True,
        tensor_parallel_size=torch.cuda.device_count(),
        gpu_memory_utilization=0.90,
    )
    sampling_params = SamplingParams(max_tokens=8192,
                                    temperature=0.0,
                                    n=1)
    outputs = llm.generate(question_list, sampling_params, use_tqdm=True)
    completions = [[output.text for output in output_item.outputs] for output_item in outputs]
    return completions
def make_conv_hf(question, tokenizer):
    # for math problem
    content = question + "\n\nPresent the answer in LaTex format: \\boxed{Your answer}"
    # for code problem
    # content = question + "\n\nWrite Python code to solve the problem. Present the code in \n```python\nYour code\n```\nat the end." 
    msg = [
        {"role": "user", "content": content}
    ]
    chat = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=True)
    return chat
    
def run():
    model_path = "PRIME-RL/Eurus-2-7B-SFT"
    all_problems = [
        "which number is larger? 9.11 or 9.9?"
    ]
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    completions = generate([make_conv_hf(problem_data, tokenizer) for problem_data in all_problems],model_path)
    print(completions)
    # [['[ASSESS]\n\n# The task is to compare two decimal numbers, 9.11 and 9.9, to determine which one is larger.\n# The numbers are in a standard decimal format, making direct comparison possible.\n# No additional information or context is provided that could affect the comparison.\n\nNext action: [ADVANCE]\n\n[ADVANCE]\n\n# To compare the two numbers, I will examine their whole and decimal parts separately.\n# The whole part of both numbers is 9, so I will focus on the decimal parts.\n# The decimal part of 9.11 is 0.11, and the decimal part of 9.9 is 0.9.\n# Since 0.9 is greater than 0.11, I can conclude that 9.9 is larger than 9.11.\n\nNext action: [VERIFY]\n\n[VERIFY]\n\n# I will review my comparison of the decimal parts to ensure accuracy.\n# Upon re-examination, I confirm that 0.9 is indeed greater than 0.11.\n# I also consider the possibility of a mistake in my initial assessment, but the comparison seems straightforward.\n# I evaluate my process and conclude that it is sound, as I correctly identified the whole and decimal parts of the numbers and compared them accurately.\n# No potential errors or inconsistencies are found in my reasoning.\n\nNext action: [OUTPUT]\n\n[OUTPUT]\n\nTo determine which number is larger, 9.11 or 9.9, I compared their whole and decimal parts. Since the whole parts are equal, I focused on the decimal parts, finding that 0.9 is greater than 0.11. After verifying my comparison, I concluded that 9.9 is indeed larger than 9.11.\n\n\\boxed{9.9}\n\n']]
if __name__ == "__main__":
    run()
```


## Evaluation

After finetuning, the performance of our Eurus-2-7B-SFT is shown in the following figure.

![image-20241230162026156](./figures/performance.jpg)

## Citation

```latex
@article{cui2025process,
  title={Process reinforcement through implicit rewards},
  author={Cui, Ganqu and Yuan, Lifan and Wang, Zefan and Wang, Hanbin and Li, Wendi and He, Bingxiang and Fan, Yuchen and Yu, Tianyu and Xu, Qixin and Chen, Weize and others},
  journal={arXiv preprint arXiv:2502.01456},
  year={2025}
}
```



```latex
@article{yuan2024implicitprm,
  title={Free Process Rewards without Process Labels},
  author={Lifan Yuan and Wendi Li and Huayu Chen and Ganqu Cui and Ning Ding and Kaiyan Zhang and Bowen Zhou and Zhiyuan Liu and Hao Peng},
  journal={arXiv preprint arXiv:2412.01981},
  year={2024}
}
```