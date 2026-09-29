---
license: mit
pipeline_tag: feature-extraction
---

# bge-m3-onnx-o4

This is `bge-m3-onnx-o4` weights of the original [`BAAI/bge-m3`](https://huggingface.co/BAAI/bge-m3). Why is this model cool?

- [x] Multi-Functionality: It can simultaneously perform the three common retrieval functionalities of embedding model: dense retrieval, multi-vector retrieval, and sparse retrieval.
- [x] Multi-Linguality: It can support more than **100** working languages.
- [x] Multi-Granularity: It is able to process inputs of different granularities, spanning from short sentences to long documents of up to **8192** tokens.

## Usage 

### IMPORTANT - DOWNLOAD MODEL WEIGHTS

Please see the instructions below.

1. **Download** the checkpoint: For some reason you cannot directly load from this online version (you will get an exception).
Please download this repo as below:

```python
# pip install huggingface-hub
 
from huggingface_hub import snapshot_download

snapshot_download(repo_id="hooman650/bge-m3-onnx-o4",local_dir="bge-m3-onnx")
```


### Dense Retrieval

```
# for cuda 
pip install --upgrade-strategy eager optimum[onnxruntime]
```

```python

from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import AutoTokenizer
import torch

# Make sure that you download the model weights locally to `bge-m3-onnx`
model = ORTModelForFeatureExtraction.from_pretrained("bge-m3-onnx", provider="CUDAExecutionProvider") # omit provider for CPU usage.
tokenizer = AutoTokenizer.from_pretrained("hooman650/bge-m3-onnx-o4")

sentences = [
    "English: The quick brown fox jumps over the lazy dog.",
    "Spanish: El rápido zorro marrón salta sobre el perro perezoso.",
    "French: Le renard brun rapide saute par-dessus le chien paresseux.",
    "German: Der schnelle braune Fuchs springt über den faulen Hund.",
    "Italian: La volpe marrone veloce salta sopra il cane pigro.",
    "Japanese: 速い茶色の狐が怠惰な犬を飛び越える。",
    "Chinese (Simplified): 快速的棕色狐狸跳过懒狗。",
    "Russian: Быстрая коричневая лиса прыгает через ленивую собаку.",
    "Arabic: الثعلب البني السريع يقفز فوق الكلب الكسول.",
    "Hindi: तेज़ भूरी लोमड़ी आलसी कुत्ते के ऊपर कूद जाती है।"
]

encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt').to("cuda")

# Get the embeddings
out=model(**encoded_input,return_dict=True).last_hidden_state

# normalize the embeddings
dense_vecs = torch.nn.functional.normalize(out[:, 0], dim=-1)
```
### Multi-Vector (ColBERT)

`coming soon...`


