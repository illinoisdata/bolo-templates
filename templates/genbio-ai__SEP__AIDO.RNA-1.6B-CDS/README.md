---
base_model:
- genbio-ai/AIDO.RNA-1.6B
license: other
---
# AIDO.RNA-1.6B-CDS

[![License](https://img.shields.io/badge/license-GenBio_AI_Community_License-orange)](https://github.com/genbio-ai/ModelGenerator/blob/main/LICENSE)

AIDO.RNA-1.6B-CDS is a domain adaptation model on the coding sequences. It was pre-trained on 9 million coding sequences released by Carlos et al. (2024) [1] based on our [AIDO.RNA-1.6B](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B) model.

## How to Use
### Build any downstream models from this backbone with ModelGenerator
For more information, visit: [Model Generator](https://github.com/genbio-ai/modelgenerator)
```bash
mgen fit --model SequenceClassification --model.backbone aido_rna_1b600m_cds --data SequenceClassificationDataModule --data.path <hf_or_local_path_to_your_dataset>
mgen test --model SequenceClassification --model.backbone aido_rna_1b600m_cds --data SequenceClassificationDataModule --data.path <hf_or_local_path_to_your_dataset>
```

### Or use directly in Python
#### Embedding
```python
from modelgenerator.tasks import Embed
model = Embed.from_config({"model.backbone": "aido_rna_1b600m_cds"}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "AGCT"]})
embedding = model(transformed_batch)
print(embedding.shape)
print(embedding)
```
#### Sequence-level Classification
```python
import torch
from modelgenerator.tasks import SequenceClassification
model = SequenceClassification.from_config({"model.backbone": "aido_rna_1b600m_cds", "model.n_classes": 2}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "AGCT"]})
logits = model(transformed_batch)
print(logits)
print(torch.argmax(logits, dim=-1))
```
#### Token-level Classification
```python
import torch
from modelgenerator.tasks import TokenClassification
model = TokenClassification.from_config({"model.backbone": "aido_rna_1b600m_cds", "model.n_classes": 3}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "AGCT"]})
logits = model(transformed_batch)
print(logits)
print(torch.argmax(logits, dim=-1))
```
#### Sequence-level Regression
```python
from modelgenerator.tasks import SequenceRegression
model = SequenceRegression.from_config({"model.backbone": "aido_rna_1b600m_cds"}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "AGCT"]})
logits = model(transformed_batch)
print(logits)
```

### Get RNA sequence embedding
```python
from genbio_finetune.tasks import Embed
model = Embed.from_config({"model.backbone": "aido_rna_1b600m_cds"}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "ACGT"]})
embedding = model(transformed_batch)
print(embedding.shape)
print(embedding)
```

## Citation
Please cite AIDO.RNA using the following BibTeX code:
```
@inproceedings{zou_large-scale_2024,
    title = {A Large-Scale Foundation Model for RNA Function and Structure Prediction},
    url = {https://www.biorxiv.org/content/10.1101/2024.11.28.625345v1},
    doi = {10.1101/2024.11.28.625345},
    publisher = {bioRxiv},
    author = {Zou, Shuxian and Tao, Tianhua and Mahbub, Sazan and Ellington, Caleb N. and Algayres, Robin and Li, Dian and Zhuang, Yonghao and Wang, Hongyi and Song, Le and Xing, Eric P.},
    year = {2024},
    booktitle = {NeurIPS 2024 Workshop on AI for New Drug Modalities},
}
```

## Reference
1. Carlos Outeiral and Charlotte M Deane. Codon language embeddings provide strong signals for use in protein engineering. Nature Machine Intelligence, 6(2):170–179, 2024.