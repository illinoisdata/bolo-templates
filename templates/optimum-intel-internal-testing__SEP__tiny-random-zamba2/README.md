---
license: apache-2.0
---

Here is a code to create this tiny model:

```python
import os

from transformers import AutoTokenizer
from transformers import Zamba2Config, Zamba2ForCausalLM

# === Step 1: Define tiny model config ===
config = Zamba2Config(
    num_hidden_layers=4,
    layers_block_type=[
        "mamba",
        "mamba",
        "hybrid",
        "mamba",
    ],
    d_model=16,
    d_state=32,
    expand=2,
    conv_kernel=3,
    vocab_size=50280,
    hidden_size=16
)

# === Step 2: Create model from config ===
model = Zamba2ForCausalLM(config)

# === Step 3: Load or create tokenizer ===
# If tokenizer is not specific to Zamba2, reuse any tokenizer (e.g., from Mamba)
tokenizer = AutoTokenizer.from_pretrained("Zyphra/Zamba2-2.7B")

# === Step 4: Save model and tokenizer ===
output_dir = "./tiny-zamba2"
os.makedirs(output_dir, exist_ok=True)
model.save_pretrained(output_dir, safe_serialization=False)
tokenizer.save_pretrained(output_dir)
```