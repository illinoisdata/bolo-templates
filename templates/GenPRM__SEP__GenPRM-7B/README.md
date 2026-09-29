---
license: mit
datasets:
- GenPRM/GenPRM-MATH-Data
base_model:
- deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
language:
- en
---

# Introduction

We propose **GenPRM**, a strong generative process reward model with the following features:

- performing explicit **CoT reasoning** and **code verfication** before providing the process judgment;
- improving Monte Carlo estimation and hard label with **Relative Progress Estimation (RPE)**;
- supporting GenPRM **test-time scaling** in a parallel manner with majority voting;
- supporting policy model test-time scaling with GenPRM as **verifiers** or **critics**.

GenPRM achieves state-of-the-art performance across multiple benchmarks in two key roles: 

- **As a verifier**: GenPRM-7B outperforms all classification-based PRMs of comparable size and even surpasses **Qwen2.5-Math-PRM-72B** via test-time scaling.
- **As a critic**: GenPRM-7B demonstrates superior critique capabilities, achieving **3.4×** greater performance gains than DeepSeekR1-Distill-Qwen-7B after 3 refinement iterations.

![](images/fig_head.png)

- Project Page: [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://ryanliu112.github.io/GenPRM)
- Paper: [https://arxiv.org/abs/2504.00891](https://arxiv.org/abs/2504.00891)
- Code: [https://github.com/RyanLiu112/GenPRM](https://github.com/RyanLiu112/GenPRM)
- Awesome Process Reward Models: [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)
- HF Paper Link: [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://hf.co/papers/2504.00891)
- HF Collection: [GenPRM](https://hf.co/collections/GenPRM/genprm-67ee4936234ba5dd16bb9943)

# Model details

For full training details, please refer to our [paper](https://arxiv.org/abs/2504.00891).

- Training data: 23K SFT data is released in [GenPRM-MATH-Data](https://huggingface.co/datasets/GenPRM/GenPRM-MATH-Data).
- Base model: we use [DeepSeek-R1-Distill series](https://huggingface.co/deepseek-ai) (1.5B, 7B, and 32B) as our base models.

# How to use

The evaluation code of GenPRM is available in our GitHub repository: [https://github.com/RyanLiu112/GenPRM](https://github.com/RyanLiu112/GenPRM).

Here's a minimal example of using GenPRM for rationale generation and process supervision:

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

# Load model and tokenizer
model = LLM(model="GenPRM/GenPRM-7B")
tokenizer = AutoTokenizer.from_pretrained("GenPRM/GenPRM-7B")

# Configure sampling parameters
sampling_params = SamplingParams(
    temperature=0.6,
    top_p=0.95,
    max_tokens=8192,
	top_k=20,
	repetition_penalty=1.0
)

# Define the messages
messages = [
    {'role': 'system', 'content': 'You are a math teacher. Your task is to review and critique the paragraphs in solution step by step.'},
	{'role': 'user', 'content': 'Question: Let $f(x)=x^2-7x+18$ and let $g(f(x))=2x+3$. What is the sum of all possible values of $g(8)$?\n\nTo solve the problem, we need to first understand the given functions and how they interact with each other. We are given $f(x) = x^2 - 7x + 18$ and $g(f(x)) = 2x + 3$.'}
]

# Generate prompt and get the model's output
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = model.generate(prompt, sampling_params)

# Print result
print(f"Model output for the first solution step: {outputs[0].outputs[0].text}")
```

# Citation
If you find this work helpful, please kindly cite our paper:

```bibtex
@article{zhao2025genprm,
    title   = {GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning},
    author  = {Jian Zhao and Runze Liu and Kaiyan Zhang and Zhimu Zhou and Junqi Gao and Dong Li and Jiafei Lyu and Zhouyi Qian and Biqing Qi and Xiu Li and Bowen Zhou},
    journal = {arXiv preprint arXiv:2504.00891},
    year    = {2025}
}
```

Our collection of PRMs in [Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models):

```bibtex
@misc{Awesome-Process-Reward-Models,
    title        = {Awesome Process Reward Models},
    author       = {Runze Liu and Jian Zhao and Kaiyan Zhang and Zhimu Zhou and Junqi Gao and Dong Li and Jiafei Lyu and Zhouyi Qian and Biqing Qi and Xiu Li and Bowen Zhou},
    howpublished = {\url{https://github.com/RyanLiu112/Awesome-Process-Reward-Models}},
    note         = {GitHub repository},
    year         = {2025}
}
```

Our recent work on LLM test-time scaling with PRMs:

```bibtex
@article{liu2025can,
    title   = {Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling},
    author  = {Runze Liu and Junqi Gao and Jian Zhao and Kaiyan Zhang and Xiu Li and Biqing Qi and Wanli Ouyang and Bowen Zhou},
    journal = {arXiv preprint arXiv:2502.06703},
    year    = {2025}
}
```