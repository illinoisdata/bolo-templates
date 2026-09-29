---
library_name: vllm
inference: false
base_model:
- mistralai/Mistral-Small-3.1-24B-Base-2503
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
tags:
- mistral-common
- mlx
license: apache-2.0
---

# mlx-community/Devstral-Small-2-24B-Instruct-2512-4bit
This model was converted to MLX format from [`mistralai/Devstral-Small-2-24B-Instruct-2512`]() using mlx-vlm version **0.3.9**.
Refer to the [original model card](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) for more details on the model.
## Use with mlx

```bash
pip install -U mlx-vlm
```

```bash
python -m mlx_vlm.generate --model mlx-community/Devstral-Small-2-24B-Instruct-2512-4bit --max-tokens 100 --temperature 0.0 --prompt "Describe this image." --image <path_to_image>
```