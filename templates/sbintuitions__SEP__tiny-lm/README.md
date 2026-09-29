---
license: mit
datasets:
- wikipedia
language:
- ja
- en
---

# tiny-lm

This repository provides a tiny 16M parameters language model for debugging and testing purposes.

Trained on English and Japanese Wikipedia data.

## How to use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
 
model = AutoModelForCausalLM.from_pretrained("sbintuitions/tiny-lm", torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained("sbintuitions/tiny-lm", use_fast=False)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
print(generator("Hello", max_length=30, do_sample=True, top_k=100))
```

## Model architecture
A 4-layer, 512-hidden-size transformer-based language model.

## Training
The model was trained on English Wikipedia and Japanese Wikipedia to optimize a traditional language modelling objective for 25B tokens.

## License
[MIT License](https://huggingface.co/sbintuitions/tiny-lm/resolve/main/LICENSE)

