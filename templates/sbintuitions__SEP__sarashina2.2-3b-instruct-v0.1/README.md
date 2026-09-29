---
license: mit
language:
- ja
pipeline_tag: text-generation
base_model:
  - sbintuitions/sarashina2.2-3b
---

# sbintuitions/sarashina2.2-3b-instruct-v0.1

## Model Summary

This repository provides Japanese language models trained by [SB Intuitions](https://www.sbintuitions.co.jp/).

## Model Details

- Model type: Autoregressive Language Model
- Language(s): Japanese

## Evaluation in Japanese and English Tasks

| Model                                                                                             | Elyza-tasks-100 | Japanese MT Bench | English MT Bench |
| ------------------------------------------------------------------------------------------------- | --------------- | ----------------- | ---------------- |
| [Qwen/Qwen2.5-0.5B-instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)                   | 1.53            | 2.95              | 4.98             |
| **sarashina2.2-0.5B-instruct-v0.1**                                                               | **2.38**        | **4.55**          | **5.09**         |
|                                                                                                   |                 |                   |                  |
| [Rakuten/RakutenAI-2.0-mini-instruct](https://huggingface.co/Rakuten/RakutenAI-2.0-mini-instruct) | 2.41            | 4.49              | 5.13             |
| [SakanaAI/TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct)   | 2.81            | **5.24**          | 6.31             |
| [Qwen/Qwen2.5-1.5B-instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)                   | 2.28            | 4.06              | **6.99**         |
| [llm-jp/llm-jp-3-1.8b-instruct3](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct3)           | 2.53            | 4.62              | 4.83             |
| **sarashina2.2-1B-instruct-v0.1**                                                                 | **2.88**        | 5.09              | 6.46             |
|                                                                                                   |                 |                   |                  |
| [google/gemma-2-2b-jpn-it](https://huggingface.co/google/gemma-2-2b-jpn-it)                       | 3.02            | 5.19              | 7.56             |
| [Qwen/Qwen2.5-3B-instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)                       | 2.99            | 5.68              | **7.88**         |
| [llm-jp/llm-jp-3-3.7b-instruct3](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct3)           | 2.79            | 4.98              | 5.44             |
| **sarashina2.2-3B-instruct-v0.1**                                                                 | **3.75**        | **6.51**          | 7.71             |

## How to Use

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, set_seed

# モデルのロード
model_name = "sbintuitions/sarashina2.2-3b-instruct-v0.1"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)
chat_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
set_seed(123)

# ユーザーの入力
user_input = [{"role": "user", "content": "こんにちは。あなたの名前を教えて"}]

# モデルによる応答生成
responses = chat_pipeline(
    user_input,
    max_length=50,
    do_sample=True,
    num_return_sequences=3,
)

# 応答を表示
for i, response in enumerate(responses, 1):
    print(f"Response {i}: {response['generated_text']}")

# Response 1: [{'role': 'user', 'content': 'こんにちは。あなたの名前を教えて'}, {'role': 'assistant', 'content': 'Sarashina2と言います。本日のご要件を教えて下さい。'}]
# Response 2: [{'role': 'user', 'content': 'こんにちは。あなたの名前を教えて'}, {'role': 'assistant', 'content': 'こんにちは！私の名前はSarashina2です。今日はどうしましたか？'}]
# Response 3: [{'role': 'user', 'content': 'こんにちは。あなたの名前を教えて'}, {'role': 'assistant', 'content': 'Sarashina2と言います。本日のご要件を教えて下さい。'}]
```

## Limitations

This model has limited safety training.
Therefore, it might generate some meaningless sequences, some inaccurate instances, or biased/objectionable outputs.
Before using it, we would like developers to tune models based on human preferences and safety considerations.

## License

MIT License