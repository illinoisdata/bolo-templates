---
license: apache-2.0
datasets:
- cnmoro/AllTripletsMsMarco-PTBR
- Tevatron/msmarco-passage-corpus
language:
- en
- pt
library_name: model2vec
base_model:
- nomic-ai/nomic-embed-text-v2-moe
pipeline_tag: feature-extraction
---

This [Model2Vec](https://github.com/MinishLab/model2vec) model was created by using [Tokenlearn](https://github.com/MinishLab/tokenlearn), with [nomic-embed-text-v2-moe](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) as a base, trained on around 20M passages (english and portuguese).

The output dimension is 50.

This is supposed to be a more minimalistic version of [cnmoro/static-nomic-eng-ptbr](https://huggingface.co/cnmoro/static-nomic-eng-ptbr)

## Usage

Load this model using the `from_pretrained` method:
```python
from model2vec import StaticModel

# Load a pretrained Model2Vec model
model = StaticModel.from_pretrained("cnmoro/static-nomic-eng-ptbr-tiny")

# Compute text embeddings
embeddings = model.encode(["Example sentence"])
```