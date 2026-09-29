---
license: other
license_name: deepseek-license
license_link: LICENSE
tags:
- mlx
---

# mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx

The Model [mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx](https://huggingface.co/mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx) was converted to MLX format from [deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct) using mlx-lm version **0.16.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx")
response = generate(model, tokenizer, prompt="hello", verbose=True)
```