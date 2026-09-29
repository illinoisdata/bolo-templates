---
license: apache-2.0
datasets:
- ystemsrx/Bad_Data_Alpaca
- ystemsrx/Toxic-All
- ystemsrx/Erotic_Literature_Collection
language:
- zh
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
pipeline_tag: text2text-generation
library_name: adapter-transformers
tags:
- not-for-all-audiences
---

[English](README.en.md)

# Qwen2.5-Sex

## 简介

Qwen2.5-Sex 是基于 Qwen2.5-1.5B-Instruct 微调的模型，主要训练于大量色情文学作品及敏感数据集。由于数据集主要为中文，模型在处理中文文本时效果更佳。

> **警告**：本模型仅供研究和测试使用，用户需遵循当地法律法规，承担自身行为的责任。

## 模型使用

要实现**连续对话**，请使用以下代码：

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# 可调参数，建议在文本生成时设置为较高值（温度不要太高）
TOP_P = 0.9        # Top-p (nucleus sampling)，范围0到1
TOP_K = 80         # Top-k 采样的K值
TEMPERATURE = 0.3  # 温度参数，控制生成文本的随机性

device = "cuda" if torch.cuda.is_available() else "cpu"

# 获取当前脚本目录，亦可改为绝对路径
current_directory = os.path.dirname(os.path.abspath(__file__))

# 加载模型和分词器
model = AutoModelForCausalLM.from_pretrained(
    current_directory,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(current_directory)

# 系统指令（建议为空）
messages = [
    {"role": "system", "content": ""}
]

while True:
    # 获取用户输入
    user_input = input("User: ").strip()

    # 添加用户输入到对话
    messages.append({"role": "user", "content": user_input})

    # 准备输入文本
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    # 生成响应
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512,
        top_p=TOP_P,
        top_k=TOP_K,
        temperature=TEMPERATURE,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id  # 避免警告
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    # 解码并打印响应
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(f"Assistant: {response}")

    # 将生成的响应添加到对话中
    messages.append({"role": "assistant", "content": response})

```

## 数据集

Qwen2-Sex 模型使用了大量色情文学和敏感数据集进行微调，这些数据集涵盖道德、法律、色情及暴力等主题。由于微调数据集为中文，模型在处理中文时表现更佳。如欲进一步了解，可通过以下链接获取：

- [Bad Data](https://huggingface.co/datasets/ystemsrx/bad_data.json)
- [Toxic-All](https://huggingface.co/datasets/ystemsrx/Toxic-All)
- [Erotic Literature Collection](https://huggingface.co/datasets/ystemsrx/Erotic_Literature_Collection)

有关更多数据集的信息，请访问我们的[GitHub](https://github.com/ystemsrx)以查看它们的获取方式。

## GitHub 仓库

如需了解该系列模型的详细信息及持续更新，请访问我们的 GitHub 仓库：

- [GitHub: ystemsrx/Qwen2.5-Sex](https://github.com/ystemsrx/Qwen2.5-Sex)

## 声明

本模型提供的所有内容仅供研究和测试，模型开发者不对任何滥用行为负责。使用者需遵循相关法律法规，并承担因使用本模型产生的所有责任。