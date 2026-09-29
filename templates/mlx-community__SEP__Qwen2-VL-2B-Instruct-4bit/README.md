---
language:
- en
library_name: transformers
license: apache-2.0
pipeline_tag: image-text-to-text
tags:
- multimodal
- mlx
---

# mlx-community/Qwen2-VL-2B-Instruct-4bit
This model was converted to MLX format from [`Qwen/Qwen2-VL-2B-Instruct`]() using mlx-vlm version **0.0.13**.
Refer to the [original model card](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) for more details on the model.
## Use with mlx

```bash
pip install -U mlx-vlm
```

```bash
python -m mlx_vlm.generate --model mlx-community/Qwen2-VL-2B-Instruct-4bit --max-tokens 100 --temp 0.0
```
