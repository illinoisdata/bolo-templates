---
license: apache-2.0
---

Here is a code to create this tiny model:


```python
import os
import torch

torch.set_default_dtype(torch.bfloat16)

from transformers import AutoTokenizer, AutoConfig, Lfm2ForCausalLM

# # === Step 1: Define tiny model config ===
model_id = "LiquidAI/LFM2-350M"
config = AutoConfig.from_pretrained(model_id)

config.num_hidden_layers=4
config.layer_types=[
    "conv",
    "conv",
    "full_attention",
    "conv",
  ]
config.num_attention_heads=4
config.num_key_value_heads=4
config.hidden_size=16
config.block_multiple_of=8

# === Step 2: Create model from config ===
model = Lfm2ForCausalLM(config)

# === Step 3: Load or create tokenizer ===
tokenizer = AutoTokenizer.from_pretrained(model_id)

# === Step 4: Save model and tokenizer ===
output_dir = "./lfm2"
os.makedirs(output_dir, exist_ok=True)
model.save_pretrained(output_dir, safe_serialization=False)
tokenizer.save_pretrained(output_dir)
```