---
license: other
---
## AIDO.RNA-650M

[![License](https://img.shields.io/badge/license-GenBio_AI_Community_License-orange)](https://github.com/genbio-ai/ModelGenerator/blob/main/LICENSE)

AIDO.RNA-650M is an RNA foundation model trained on 42 million non-coding RNA sequences at single-nucleotide resolution. 
For a more detailed description, refer to the SOTA model in this collection https://huggingface.co/genbio-ai/AIDO.RNA-1.6B


## How to Use
### Build any downstream models from this backbone with ModelGenerator
For more information, visit: [Model Generator](https://github.com/genbio-ai/modelgenerator)
```bash
mgen fit --model SequenceClassification --model.backbone aido_rna_650m --data SequenceClassificationDataModule --data.path <hf_or_local_path_to_your_dataset>
mgen test --model SequenceClassification --model.backbone aido_rna_650m --data SequenceClassificationDataModule --data.path <hf_or_local_path_to_your_dataset>
```

### Or use directly in Python
#### Embedding
```python
from modelgenerator.tasks import Embed
model = Embed.from_config({"model.backbone": "aido_rna_650m"}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "AGCT"]})
embedding = model(transformed_batch)
print(embedding.shape)
print(embedding)
```
#### Sequence-level Classification
```python
import torch
from modelgenerator.tasks import SequenceClassification
model = SequenceClassification.from_config({"model.backbone": "aido_rna_650m", "model.n_classes": 2}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "AGCT"]})
logits = model(transformed_batch)
print(logits)
print(torch.argmax(logits, dim=-1))
```
#### Token-level Classification
```python
import torch
from modelgenerator.tasks import TokenClassification
model = TokenClassification.from_config({"model.backbone": "aido_rna_650m", "model.n_classes": 3}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "AGCT"]})
logits = model(transformed_batch)
print(logits)
print(torch.argmax(logits, dim=-1))
```
#### Sequence-level Regression
```python
from modelgenerator.tasks import SequenceRegression
model = SequenceRegression.from_config({"model.backbone": "aido_rna_650m"}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "AGCT"]})
logits = model(transformed_batch)
print(logits)
```

### Get RNA sequence embedding
```python
from genbio_finetune.tasks import Embed
model = Embed.from_config({"model.backbone": "aido_rna_650m"}).eval()
transformed_batch = model.transform({"sequences": ["ACGT", "ACGT"]})
embedding = model(transformed_batch)
print(embedding.shape)
print(embedding)
```