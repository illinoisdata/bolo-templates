# dia-1.6b-safetensors

This repository contains [Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) converted to SafeTensors format for improved security.

## Original Model

This is a conversion of [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) to SafeTensors format.

## Files

- `dia-v0_1.safetensors` - Original precision model
- `dia-v0_1_bf16.safetensors` - BF16 precision model (approximately half the size)

## Usage

```python
from safetensors.torch import load_file
from dia.model import Dia
from dia.config import DiaConfig

# Load config
config = DiaConfig.load("config.json")

# Create a Dia model instance
dia = Dia(config)

# Load weights from safetensors
state_dict = load_file("dia-v0_1.safetensors")  # or dia-v0_1_bf16.safetensors
dia.model.load_state_dict(state_dict)

# Use the model
output = dia.generate("[S1] Dia is a text to speech model. [S2] You get full control over scripts and voices.")
```

## Conversion

This model was converted from pickle format to SafeTensors format, which provides better security since it doesn't execute arbitrary code during loading.