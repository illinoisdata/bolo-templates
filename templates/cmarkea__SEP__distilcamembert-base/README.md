---
language: fr
license: mit
datasets:
- oscar
widget:
- text: "J'aime lire les <mask> de SF."
---

DistilCamemBERT
===============

We present a distillation version of the well named [CamemBERT](https://huggingface.co/camembert-base), a RoBERTa French model version, alias DistilCamemBERT. The aim of distillation is to drastically reduce the complexity of the model while preserving the performances. The proof of concept is shown in the [DistilBERT paper](https://arxiv.org/abs/1910.01108) and the code used for the training is inspired by the code of [DistilBERT](https://github.com/huggingface/transformers/tree/master/examples/research_projects/distillation).

Loss function
-------------

The training for the distilled model (student model) is designed to be the closest as possible to the original model (teacher model). To perform this the loss function is composed of 3 parts:
* DistilLoss: a distillation loss which measures the silimarity between the probabilities at the outputs of the student and teacher models with a cross-entropy loss on the MLM task ;
* CosineLoss: a cosine embedding loss. This loss function is applied on the last hidden layers of student and teacher models to guarantee a collinearity between them ;
* MLMLoss: and finaly a Masked Language Modeling (MLM) task loss to perform the student model with the original task of the teacher model.

The final loss function is a combination of these three losses functions. We use the following ponderation:

$$Loss = 0.5 \times DistilLoss + 0.3 \times CosineLoss + 0.2 \times MLMLoss$$

Dataset
-------

To limit the bias between the student and teacher models, the dataset used for the DstilCamemBERT training is the same as the camembert-base training one: OSCAR. The French part of this dataset approximately represents 140 GB on a hard drive disk.

Training
--------

We pre-trained the model on a nVidia Titan RTX during 18 days.

Evaluation results
------------------

| Dataset name | f1-score |
| :----------: | :------: |
| [FLUE](https://huggingface.co/datasets/flue) CLS     | 83%      |
| [FLUE](https://huggingface.co/datasets/flue) PAWS-X  | 77%      |
| [FLUE](https://huggingface.co/datasets/flue) XNLI    | 77%      |
| [wikiner_fr](https://huggingface.co/datasets/Jean-Baptiste/wikiner_fr) NER | 98%    |

How to use DistilCamemBERT
--------------------------

Load DistilCamemBERT and its sub-word tokenizer :

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("cmarkea/distilcamembert-base")
model = AutoModel.from_pretrained("cmarkea/distilcamembert-base")
model.eval()
...
```

Filling masks using pipeline :

```python
from transformers import pipeline

model_fill_mask = pipeline("fill-mask", model="cmarkea/distilcamembert-base", tokenizer="cmarkea/distilcamembert-base")
results = model_fill_mask("Le camembert est <mask> :)")

results
[{'sequence': '<s> Le camembert est délicieux :)</s>', 'score': 0.3878222405910492, 'token': 7200},
 {'sequence': '<s> Le camembert est excellent :)</s>', 'score': 0.06469205021858215, 'token': 2183}, 
 {'sequence': '<s> Le camembert est parfait :)</s>', 'score': 0.04534877464175224, 'token': 1654}, 
 {'sequence': '<s> Le camembert est succulent :)</s>', 'score': 0.04128391295671463, 'token': 26202}, 
 {'sequence': '<s> Le camembert est magnifique :)</s>', 'score': 0.02425697259604931, 'token': 1509}]
 ```

Citation
--------

```bibtex
@inproceedings{delestre:hal-03674695,
  TITLE = {{DistilCamemBERT : une distillation du mod{\`e}le fran{\c c}ais CamemBERT}},
  AUTHOR = {Delestre, Cyrile and Amar, Abibatou},
  URL = {https://hal.archives-ouvertes.fr/hal-03674695},
  BOOKTITLE = {{CAp (Conf{\'e}rence sur l'Apprentissage automatique)}},
  ADDRESS = {Vannes, France},
  YEAR = {2022},
  MONTH = Jul,
  KEYWORDS = {NLP ; Transformers ; CamemBERT ; Distillation},
  PDF = {https://hal.archives-ouvertes.fr/hal-03674695/file/cap2022.pdf},
  HAL_ID = {hal-03674695},
  HAL_VERSION = {v1},
}
```