---
tags:
- sentence-similarity
inference: false
license: pddl
language: en
library_name: staticvectors
base_model:
- NeuML/glove-6B
---

# GloVe-6B StaticVectors model

This model is an export of these [GloVe-6B English Vectors](https://nlp.stanford.edu/projects/glove/) (_300d_) for [`staticvectors`](https://github.com/neuml/staticvectors). `staticvectors` enables running inference in Python with NumPy. This helps it maintain solid runtime performance.

_This model is a quantized version of the base model. It's using 10x256 Product Quantization._

## Usage with StaticVectors

```python
from staticvectors import StaticVectors

model = StaticVectors("neuml/glove-6B-quantized")
model.embeddings(["word"])
```