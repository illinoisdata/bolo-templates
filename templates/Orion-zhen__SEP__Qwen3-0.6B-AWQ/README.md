---
license: gpl-3.0
base_model:
- Qwen/Qwen3-0.6B
---

# Qwen3-0.6B-AWQ

```yaml
zero_piont: true
bits: 4
version: GEMM
dataset: wikitext + Orion-zhen/gsm8k-r1-qwen-32b
num_examples: 256
```

The very **first** Qwen3-0.6B-AWQ on HuggingFace. I'm not sure if you really need a quantization of such a small model.