---
pipeline_tag: sentence-similarity
tags:
  - sentence-similarity
language: en
license: mit
---

# ONNX Conversion of [BAAI/bge-reranker-base](https://huggingface.co/BAAI/bge-reranker-base)

- ONNX model for CPU with O3 optimisation

## Usage

```python
from itertools import product

import torch.nn.functional as F
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer

sentences = [
    "The llama (/ˈlɑːmə/) (Lama glama) is a domesticated South American camelid.",
    "The alpaca (Lama pacos) is a species of South American camelid mammal.",
    "The vicuña (Lama vicugna) (/vɪˈkuːnjə/) is one of the two wild South American camelids.",
]
queries = ["What is a llama?", "What is a harimau?", "How to fly a kite?"]
pairs = list(product(queries, sentences))

model_name = "EmbeddedLLM/bge-reranker-base-onnx-o3-cpu"
device = "cpu"
provider = "CPUExecutionProvider"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = ORTModelForSequenceClassification.from_pretrained(
    model_name, use_io_binding=True, provider=provider, device_map=device
)
inputs = tokenizer(
    pairs,
    padding=True,
    truncation=True,
    return_tensors="pt",
    max_length=model.config.max_position_embeddings,
)
inputs = inputs.to(device)
scores = model(**inputs).logits.view(-1).cpu().numpy()
# Sort most similar to least
pairs = sorted(zip(pairs, scores), key=lambda x: x[1], reverse=True)
for ps in pairs:
    print(ps)
```