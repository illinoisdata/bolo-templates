---
license: apache-2.0
---

A 123M SmolLm model Pre-trained on 10M words for babyLM challenge.
You can test the model:

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

def generate_text(prompt, tokenizer, model, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        output = model.generate(**inputs, max_length=max_length, num_return_sequences=1)
    
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

model_name = "universitytehran/SmolLM-135M-10M-word"

tokenizer, model = load_model(model_name)

prompt = "Once upon a time"
completed_text = generate_text(prompt, tokenizer, model)

print(f"Prompt: {prompt}")
print(f"Completed text: {completed_text}")
```