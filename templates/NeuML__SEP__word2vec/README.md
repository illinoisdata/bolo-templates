---
tags:
- sentence-similarity
inference: false
license: apache-2.0
language: en
library_name: staticvectors
---

# Word2Vec StaticVectors model

This model is an export of these [Word2Vec Vectors](https://code.google.com/archive/p/word2vec/) for [`staticvectors`](https://github.com/neuml/staticvectors). `staticvectors` enables running inference in Python with NumPy. This helps it maintain solid runtime performance.

## Usage with StaticVectors

```python
from staticvectors import StaticVectors

model = StaticVectors("neuml/word2vec")
model.embeddings(["word"])
```

Given that pre-trained embeddings models can get quite large, there is also a SQLite version that lazily loads vectors.

```python
from staticvectors import StaticVectors

model = StaticVectors("neuml/word2vec/model.sqlite")
model.embeddings(["word"])
```