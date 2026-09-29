---
base_model:
- openai/gpt-oss-20b
---
# gpt-oss-20b

Detailed guide for using this model with `llama.cpp`:

https://github.com/ggml-org/llama.cpp/discussions/15396

Quick start:

```sh
llama-server -hf ggml-org/gpt-oss-20b-GGUF -c 0 --jinja

# Then, access http://localhost:8080
```