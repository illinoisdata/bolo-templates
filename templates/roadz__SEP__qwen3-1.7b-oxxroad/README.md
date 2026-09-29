# Qwen3 1.7B

This repository follows the structure of a Qwen3-style causal language model on Hugging Face. It includes model configuration, tokenizer assets, generation configuration, and weight artifacts.

Contents:
- `config.json` — model configuration (Qwen3 fields)
- `generation_config.json` — text generation defaults
- `tokenizer.json` — tokenizer (fast) with special tokens
- `tokenizer_config.json` — tokenizer settings
- `special_tokens_map.json` — mapping for special tokens
- `vocab.json`, `merges.txt` — BPE assets
- `model.safetensors` — weights (safetensors, single file)

Notes:
- The tokenizer uses a compact vocabulary and special tokens typical for causal LMs.

Example usage:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tok = AutoTokenizer.from_pretrained("<your-namespace>/<your-model-id>")
model = AutoModelForCausalLM.from_pretrained("<your-namespace>/<your-model-id>")
```

How to publish to the Hub:
1. Create a new repo on the Hugging Face Hub (private or public).
2. Run `huggingface-cli login`.
3. From this folder, run `git init`, `git remote add origin <your-hf-repo-url>`, `git add -A`, `git commit -m "init"`, `git push -u origin main`.