---
license: apache-2.0
---

Here is a code to create this tiny model:

```python
import os

from transformers import MambaConfig, MambaForCausalLM, AutoTokenizer

model_dir = "state-spaces/mamba-130m-hf"
tokenizer = AutoTokenizer.from_pretrained(model_dir)

# === Step 1: Define tiny model config ===
config = MambaConfig(
    d_model=16,            # Dimensionality of the input embeddings (model hidden size)
    n_layer=2,             # Number of Mamba layers (or blocks) in the model
    d_state=32,            # Dimensionality of the internal state used in the Mamba block (e.g., for state-space modeling)
    expand=2,              # Expansion factor used in the Mamba block, typically to widen the intermediate dimensions
    conv_kernel=3,         # Size of the convolution kernel used in the Mamba block (affects temporal mixing)
    vocab_size=50280,      # Size of the vocabulary (number of unique tokens)
    num_hidden_layers=32,  # Total number of hidden layers in the model (could override `n_layer`)
    hidden_size=64,        # Size of hidden states used in the model layers (could override `d_model`)
)

# === Step 2: Create model from config ===
model = MambaForCausalLM(config)

# === Step 4: Save model and tokenizer to disk ===
output_dir = "./tiny-mamba2"
os.makedirs(output_dir, exist_ok=True)
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
print(f"Tiny Mamba model and tokenizer saved to: {output_dir}")
```