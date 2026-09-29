---
language: fr
license: mit
tags:
- zero-shot-classification
- sentence-similarity
- nli
pipeline_tag: zero-shot-classification
widget:
- text: >-
    Selon certains physiciens, un univers parallèle, miroir du nôtre ou relevant
    de ce que l'on appelle la théorie des branes, autoriserait des neutrons à
    sortir de notre Univers pour y entrer à nouveau. L'idée a été testée une
    nouvelle fois avec le réacteur nucléaire de l'Institut Laue-Langevin à
    Grenoble, plus précisément en utilisant le détecteur de l'expérience Stereo
    initialement conçu pour chasser des particules de matière noire
    potentielles, les neutrinos stériles.
  candidate_labels: politique, science, sport, santé
  hypothesis_template: Ce texte parle de {}.
datasets:
- flue
base_model:
- cmarkea/distilcamembert-base
---

DistilCamemBERT-NLI
===================

We present DistilCamemBERT-NLI, which is [DistilCamemBERT](https://huggingface.co/cmarkea/distilcamembert-base) fine-tuned for the Natural Language Inference (NLI) task for the french language, also known as recognizing textual entailment (RTE). This model is constructed on the XNLI dataset, which determines whether a premise entails, contradicts or neither entails or contradicts a hypothesis.

This modelization is close to [BaptisteDoyen/camembert-base-xnli](https://huggingface.co/BaptisteDoyen/camembert-base-xnli) based on [CamemBERT](https://huggingface.co/camembert-base) model. The problem of the modelizations based on CamemBERT is at the scaling moment, for the production phase, for example. Indeed, inference cost can be a technological issue especially in the context of cross-encoding like this task. To counteract this effect, we propose this modelization which divides the inference time by 2 with the same consumption power, thanks to DistilCamemBERT.

Dataset
-------

The dataset XNLI from [FLUE](https://huggingface.co/datasets/flue) comprises 392,702 premises with their hypothesis for the train and 5,010 couples for the test. The goal is to predict textual entailment (does sentence A imply/contradict/neither sentence B?) and is a classification task (given two sentences, predict one of three labels). Sentence A is called *premise*, and sentence B is called *hypothesis*, then the goal of modelization is determined as follows:
$$P(premise=c\in\{contradiction, entailment, neutral\}\vert hypothesis)$$

Evaluation results
------------------

| **class**          | **precision (%)** | **f1-score (%)** | **support** |
| :----------------: | :---------------: | :--------------: | :---------: |
| **global**         | 77.70             | 77.45            | 5,010       |
| **contradiction**  | 78.00             | 79.54            | 1,670       | 
| **entailment**     | 82.90             | 78.87            | 1,670       |
| **neutral**        | 72.18             | 74.04            | 1,670       |

Benchmark
---------

We compare the [DistilCamemBERT](https://huggingface.co/cmarkea/distilcamembert-base) model to 2 other modelizations working on the french language. The first one [BaptisteDoyen/camembert-base-xnli](https://huggingface.co/BaptisteDoyen/camembert-base-xnli) is based on well named [CamemBERT](https://huggingface.co/camembert-base), the french RoBERTa model and the second one [MoritzLaurer/mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) based on [mDeBERTav3](https://huggingface.co/microsoft/mdeberta-v3-base) a multilingual model. To compare the performances, the metrics of accuracy and [MCC (Matthews Correlation Coefficient)](https://en.wikipedia.org/wiki/Phi_coefficient) were used. We used an **AMD Ryzen 5 4500U @ 2.3GHz with 6 cores** for mean inference time measure.

| **model**          | **time (ms)** | **accuracy (%)** | **MCC (x100)** |
| :--------------: | :-----------: | :--------------: | :------------: |
| [cmarkea/distilcamembert-base-nli](https://huggingface.co/cmarkea/distilcamembert-base-nli) | **51.35**            | 77.45     | 66.24         |
| [BaptisteDoyen/camembert-base-xnli](https://huggingface.co/BaptisteDoyen/camembert-base-xnli) | 105.0              | 81.72     | 72.67         |
| [MoritzLaurer/mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 299.18 | **83.43** | **75.15**     |

Zero-shot classification
------------------------

The main advantage of such modelization is to create a zero-shot classifier allowing text classification without training. This task can be summarized by:
$$P(hypothesis=i\in\mathcal{C}|premise)=\frac{e^{P(premise=entailment\vert hypothesis=i)}}{\sum_{j\in\mathcal{C}}e^{P(premise=entailment\vert hypothesis=j)}}$$

For this part, we use two datasets, the first one: [allocine](https://huggingface.co/datasets/allocine) used to train the sentiment analysis models. The dataset comprises two classes: "positif" and "négatif" appreciation of movie reviews. Here we use "Ce commentaire est {}." as the hypothesis template and "positif" and "négatif" as candidate labels.

| **model**     | **time (ms)** | **accuracy (%)** | **MCC (x100)** |
| :--------------: | :-----------: | :--------------: | :------------: |
| [cmarkea/distilcamembert-base-nli](https://huggingface.co/cmarkea/distilcamembert-base-nli) | **195.54**           | 80.59         | 63.71         |
| [BaptisteDoyen/camembert-base-xnli](https://huggingface.co/BaptisteDoyen/camembert-base-xnli) | 378.39             | **86.37**     | **73.74**     |
| [MoritzLaurer/mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 520.58 | 84.97         | 70.05         |

The second one: [mlsum](https://huggingface.co/datasets/mlsum) used to train the summarization models. In this aim, we aggregate sub-topics and select a few of them. We use the articles summary part to predict their topics. In this case, the hypothesis template used is "C'est un article traitant de {}." and the candidate labels are: "économie", "politique", "sport" and "science".

| **model**        | **time (ms)** |  **accuracy (%)** | **MCC (x100)** |
| :--------------: | :-----------: | :--------------: | :------------: |
| [cmarkea/distilcamembert-base-nli](https://huggingface.co/cmarkea/distilcamembert-base-nli) | **217.77**           | **79.30**     | **70.55**     |
| [BaptisteDoyen/camembert-base-xnli](https://huggingface.co/BaptisteDoyen/camembert-base-xnli) | 448.27             | 70.7          | 64.10         |
| [MoritzLaurer/mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 591.34 | 64.45         | 58.67         |

How to use DistilCamemBERT-NLI
------------------------------
```python
from transformers import pipeline

classifier = pipeline(
    task='zero-shot-classification',
    model="cmarkea/distilcamembert-base-nli",
    tokenizer="cmarkea/distilcamembert-base-nli"
)
result = classifier (
    sequences="Le style très cinéphile de Quentin Tarantino "
    "se reconnaît entre autres par sa narration postmoderne "
    "et non linéaire, ses dialogues travaillés souvent "
    "émaillés de références à la culture populaire, et ses "
    "scènes hautement esthétiques mais d'une violence "
    "extrême, inspirées de films d'exploitation, d'arts "
    "martiaux ou de western spaghetti.",
    candidate_labels="cinéma, technologie, littérature, politique",
    hypothesis_template="Ce texte parle de {}."
)

result
{"labels": ["cinéma",
            "littérature",
            "technologie",
            "politique"],
 "scores": [0.7164115309715271,
            0.12878799438476562,
            0.1092301607131958,
            0.0455702543258667]}
```

### Optimum + ONNX

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline

HUB_MODEL = "cmarkea/distilcamembert-base-nli"

tokenizer = AutoTokenizer.from_pretrained(HUB_MODEL)
model = ORTModelForSequenceClassification.from_pretrained(HUB_MODEL)
onnx_qa = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

# Quantized onnx model
quantized_model = ORTModelForSequenceClassification.from_pretrained(
    HUB_MODEL, file_name="model_quantized.onnx"
)
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