---
license: mit
pipeline_tag: sentence-similarity
---

ONNX port of [sentence-transformers/clip-ViT-B-32](https://huggingface.co/sentence-transformers/clip-ViT-B-32) for text classification and similarity searches.

### Usage

Here's an example of performing inference using the model with [FastEmbed](https://github.com/qdrant/fastembed).

```py
from fastembed import TextEmbedding

documents = [
    "You should stay, study and sprint.",
    "History can only prepare us to be surprised yet again.",
]

model = TextEmbedding(model_name="Qdrant/clip-ViT-B-32-text")
embeddings = list(model.embed(documents))

# [
#     array([1.57889184e-02, -2.21896712e-02, -1.40235685e-02, -2.36918423e-02, ...],
#           dtype=float32)
# ]
```