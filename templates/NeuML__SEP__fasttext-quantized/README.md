---
tags:
- sentence-similarity
inference: false
license: cc-by-sa-3.0
language: en
library_name: staticvectors
base_model:
- NeuML/fasttext
---

# FastText StaticVectors model

This model is an export of these [FastText English Vectors](https://fasttext.cc/docs/en/english-vectors.html) (_wiki-news-300d-1M-subword.vec.zip_) for [`staticvectors`](https://github.com/neuml/staticvectors). `staticvectors` enables running inference in Python with NumPy. This helps it maintain solid runtime performance.

_This model is a quantized version of the base model. It's using 10x256 Product Quantization._

## Usage with StaticVectors

```python
from staticvectors import StaticVectors

model = StaticVectors("neuml/fasttext-quantized")
model.embeddings(["word"])
```