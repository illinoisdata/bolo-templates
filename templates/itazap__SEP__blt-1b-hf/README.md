---
license: apache-2.0
---

# Byte Latent Transformer (BLT)

![BLT Architecture](./figures/blt_architecture.png)

## Model Description

**BLT (Byte Latent Transformer)** is a tokenizer-free transformer architecture that operates directly on raw byte sequences. Instead of processing text token by token, BLT dynamically groups bytes into **entropy-based patches**, enabling more efficient and scalable processing for byte-level tasks.  

Key components:  
- **Local Encoder → Latent Transformer → Local Decoder** architecture.  
- **Entropy-based patcher (BltPatcher)**: scans byte streams and creates patches when entropy thresholds are met.  
- **Hash n-gram embeddings**: maintain contextual information over neighboring bytes.  

BLT achieves competitive performance compared to traditional token-based transformers, supporting multilingual, noisy, or mixed-script input.

Paper: [Byte Latent Transformer: Patches Scale Better Than Tokens](https://arxiv.org/abs/2412.09871) (FAIR @ Meta)

Original FAIR checkpoint: https://huggingface.co/facebook/blt-1b

---

## How to Use

```python
from transformers import BltForCausalLM, AutoTokenizer

model = BltForCausalLM.from_pretrained("itazap/blt-1b-hf", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("itazap/blt-1b-hf")

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
generated_ids = model.generate(**inputs, max_new_tokens=200, do_sample=False, use_cache=False)
output_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)