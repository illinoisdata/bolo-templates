---
language:
- en
license: other
tags:
- chat
- mlx
license_name: tongyi-qianwen-research
license_link: https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat/blob/main/LICENSE
pipeline_tag: text-generation
---

# mlx-community/Qwen1.5-0.5B-Chat-4bit
This model was converted to MLX format from [`qwen/Qwen1.5-0.5B-Chat`]() using mlx-lm version **0.10.0**.
Refer to the [original model card](https://huggingface.co/qwen/Qwen1.5-0.5B-Chat) for more details on the model.
## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Qwen1.5-0.5B-Chat-4bit")
response = generate(model, tokenizer, prompt="hello", verbose=True)
```