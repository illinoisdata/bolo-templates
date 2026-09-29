---
datasets:
- agentica-org/DeepScaleR-Preview-Dataset
language:
- en
metrics:
- accuracy
base_model:
- deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
---
# Model Overview
<div align="center">
<span style="font-family: default; font-size: 1.5em;">DLER-R1-1.5B</span>
<div>
🚀 The leading efficient reasoning model for cutting-edge research and development 🌟
</div>
</div>

[![Paper](https://img.shields.io/badge/ArXiv-Paper-brown)](https://www.arxiv.org/abs/2510.15110)
[![Code](https://img.shields.io/badge/GitHub-Link-blue)](https://github.com/NVlabs/DLER)
[![Model](https://img.shields.io/badge/HuggingFace-Model-yellow)](https://huggingface.co/collections/nvidia/reasoning-efficiency-research)
[![Website](https://img.shields.io/badge/Web-Page-orange)](https://nvlabs.github.io/DLER/)
![Comparison between DeepSeek-R1-1.5B and DLER-R1-1.5B](./asset/latency_1.5b.png)


### Description:
DLER-Qwen-R1-1.5B is an ultra-efficient 1.5B open-weight reasoning model designed for challenging tasks such as mathematics, programming, and scientific problem-solving. It is trained with the DLER algorithm on agentica-org/DeepScaleR-Preview-Dataset. Compared to DeepSeek’s 1.5B model, DLER-Qwen-R1-1.5B achieves substantial efficiency gains, reducing the average response length by nearly 80% across diverse mathematical benchmarks with better accuracy.


This model is for research and development only.


### Evaluation Results:

|Model            | MATH | Length | AIME               | Length        | AMC                | Length        | Minerva            |Length         | Olympiad           |Length         | Total Avg Length    |
|--------------------|----------|------------|--------|----------|-------|----------|---------|----------|----------|----------|--------------|
| Deepseek-R1-1.5B   | 84.31    | 5500       | 29.79  | 16916    | 61.97 | 10967    | 38.41   | 7494     | 44.07    | 11620    | 10499        |
| **DLER-R1-1.5B**   | **86.95 (+2.64%)** | **1652 (-70%)** | **34.375 (+4.59%)** | **3551 (-80%)** | **70.48 (+8.51%)** | **2537 (-77%)** | **43.58 (+5.18%)** | **2029 (-73%)** | **48.314 (+4.24%)** | **2563 (-78%)** | **2466 (-77%)** |


### Environment Setup
```
pip install transformers==4.51.3
```

# Inference:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


model = AutoModelForCausalLM.from_pretrained('nvidia/DLER-R1-1.5B-Research').to(device)
tokenizer = AutoTokenizer.from_pretrained('nvidia/DLER-R1-1.5B-Research')


messages = [
   {"role": "user", "content": "Convert the point $(0,3)$ in rectangular coordinates to polar coordinates.  Enter your answer in the form $(r,\\theta),$ where $r > 0$ and $0 \\le \\theta < 2 \\pi.$"+" Let's think step by step and output the final answer within \\boxed{}."},
]


tokenized_chat = tokenizer.apply_chat_template(
   messages,
   tokenize=True,
   add_generation_prompt=True,
   return_tensors="pt"
).to(model.device)


outputs = model.generate(
   tokenized_chat,
   max_new_tokens=10000,
   eos_token_id=tokenizer.eos_token_id
)


print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```


### License/Terms of Use
NSCLv1


## Citation
If you find our model helpful, please cite the following [paper]():

```
@article{liu2025dler,
  title={DLER: Doing Length pEnalty Right-Incentivizing More Intelligence per Token via Reinforcement Learning},
  author={Liu, Shih-Yang and Dong, Xin and Lu, Ximing and Diao, Shizhe and Liu, Mingjie and Chen, Min-Hung and Yin, Hongxu and Wang, Yu-Chiang Frank and Cheng, Kwang-Ting and Choi, Yejin and others},
  journal={arXiv preprint arXiv:2510.15110},
  year={2025}
}
```