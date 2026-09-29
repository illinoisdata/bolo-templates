---
license: mit
base_model:
- 5CD-AI/Vintern-1B-v3_5
---

Original model: https://huggingface.co/5CD-AI/Vintern-1B-v3_5

### How to use this

Install llama.cpp

Then:

```
llama-server -hf ngxson/Vintern-1B-v3_5-GGUF --chat-template vicuna
```