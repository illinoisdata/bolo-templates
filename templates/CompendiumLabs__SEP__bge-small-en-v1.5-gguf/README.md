---
license: mit
---

<img src="https://raw.githubusercontent.com/CompendiumLabs/compendiumlabs.ai/main/images/logo_text_crop.png" alt="Compendium Labs" style="width: 500px;">

# bge-small-en-v1.5-gguf
Source model: https://huggingface.co/BAAI/bge-small-en-v1.5

Quantized and unquantized embedding models in GGUF format for use with `llama.cpp`. A large benefit over `transformers` is almost guaranteed and the benefit over ONNX will vary based on the application, but this seems to provide a large speedup on CPU and a modest speedup on GPU for larger models. Due to the relatively small size of these models, quantization will not provide huge benefits, but it does generate up to a 30% speedup on CPU with minimal loss in accuracy.

<br/>

# Files Available

<div style="width: 500px; margin: 0;">

| Filename | Quantization | Size |
|:-------- | ------------ | ---- |
| [bge-small-en-v1.5-f32.gguf](https://huggingface.co/CompendiumLabs/bge-small-en-v1.5-gguf/blob/main/bge-small-en-v1.5-f32.gguf) | F32 | 128 MB |
| [bge-small-en-v1.5-f16.gguf](https://huggingface.co/CompendiumLabs/bge-small-en-v1.5-gguf/blob/main/bge-small-en-v1.5-f16.gguf) | F16 | 65 MB |
| [bge-small-en-v1.5-q8_0.gguf](https://huggingface.co/CompendiumLabs/bge-small-en-v1.5-gguf/blob/main/bge-small-en-v1.5-q8_0.gguf) | Q8_0 | 36 MB |
| [bge-small-en-v1.5-q4_k_m.gguf](https://huggingface.co/CompendiumLabs/bge-small-en-v1.5-gguf/blob/main/bge-small-en-v1.5-q4_k_m.gguf) | Q4_K_M | 24 MB |

</div>

<br/>

# Usage

These model files can be used with pure `llama.cpp` or with the `llama-cpp-python` Python bindings
```python
from llama_cpp import Llama
model = Llama(gguf_path, embedding=True)
embed = model.embed(texts)
```
Here `texts` can either be a string or a list of strings, and the return value is a list of embedding vectors. The inputs are grouped into batches automatically for efficient execution. There is also LangChain integration through `langchain_community.embeddings.LlamaCppEmbeddings`.