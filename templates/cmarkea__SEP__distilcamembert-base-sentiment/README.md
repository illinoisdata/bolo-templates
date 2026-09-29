---
language: fr
license: mit
datasets:
- amazon_reviews_multi
- allocine
widget:
- text: Je pensais lire un livre nul, mais finalement je l'ai trouvé super !
- text: >-
    Cette banque est très bien, mais elle n'offre pas les services de paiements
    sans contact.
- text: >-
    Cette banque est très bien et elle offre en plus les services de paiements
    sans contact.
base_model:
- cmarkea/distilcamembert-base
---

DistilCamemBERT-Sentiment
=========================

We present DistilCamemBERT-Sentiment, which is [DistilCamemBERT](https://huggingface.co/cmarkea/distilcamembert-base) fine-tuned for the sentiment analysis task for the French language. This model is built using two datasets: [Amazon Reviews](https://huggingface.co/datasets/amazon_reviews_multi) and [Allociné.fr](https://huggingface.co/datasets/allocine) to minimize the bias. Indeed, Amazon reviews are similar in messages and relatively shorts, contrary to Allociné critics, who are long and rich texts.

This modelization is close to [tblard/tf-allocine](https://huggingface.co/tblard/tf-allocine) based on [CamemBERT](https://huggingface.co/camembert-base) model. The problem of the modelizations based on CamemBERT is at the scaling moment, for the production phase, for example. Indeed, inference cost can be a technological issue. To counteract this effect, we propose this modelization which **divides the inference time by two** with the same consumption power thanks to [DistilCamemBERT](https://huggingface.co/cmarkea/distilcamembert-base).

Dataset
-------

The dataset comprises 204,993 reviews for training and 4,999 reviews for the test from Amazon, and 235,516 and 4,729 critics from [Allocine website](https://www.allocine.fr/). The dataset is labeled into five categories:

- 1 star: represents a terrible appreciation,
- 2 stars: bad appreciation,
- 3 stars: neutral appreciation,
- 4 stars: good appreciation,
- 5 stars: excellent appreciation. 
 
Evaluation results
------------------

In addition of accuracy (called here *exact accuracy*) in order to be robust to +/-1 star estimation errors, we will take the following definition as a performance measure:

$$\mathrm{top\!-\!2\; acc}=\frac{1}{|\mathcal{O}|}\sum_{i\in\mathcal{O}}\sum_{0\leq l < 2}\mathbb{1}(\hat{f}_{i,l}=y_i)$$

where \\(\hat{f}_l\\) is the l-th largest predicted label, \\(y\\) the true label, \\(\mathcal{O}\\) is the test set of the observations and \\(\mathbb{1}\\) is the indicator function.

| **class**   | **exact accuracy (%)** | **top-2 acc (%)** | **support** |
| :---------: | :--------------------: | :---------------: | :---------: |
| **global**  | 61.01                  | 88.80             | 9,698       | 
| **1 star**  | 87.21                  | 77.17             | 1,905       |
| **2 stars** | 79.19                  | 84.75             | 1,935       |
| **3 stars** | 77.85                  | 78.98             | 1,974       |
| **4 stars** | 78.61                  | 90.22             | 1,952       |
| **5 stars** | 85.96                  | 82.92             | 1,932       |

Benchmark
---------

This model is compared to 3 reference models (see below). As each model doesn't have the exact definition of targets, we detail the performance measure used for each. An **AMD Ryzen 5 4500U @ 2.3GHz with 6 cores** was used for the mean inference time measure.

#### bert-base-multilingual-uncased-sentiment
[nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) is based on BERT model in the multilingual and uncased version. This sentiment analyzer is trained on Amazon reviews, similar to our model. Hence the targets and their definitions are the same.

| **model** | **time (ms)** | **exact accuracy (%)** | **top-2 acc (%)** |
| :-------: | :-----------: | :--------------------: | :---------------: |
| [cmarkea/distilcamembert-base-sentiment](https://huggingface.co/cmarkea/distilcamembert-base-sentiment) | **95.56** | **61.01** | **88.80** |
| [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) | 187.70 | 54.41 | 82.82 |

#### tf-allociné and barthez-sentiment-classification
[tblard/tf-allocine](https://huggingface.co/tblard/tf-allocine) based on [CamemBERT](https://huggingface.co/camembert-base) model and [moussaKam/barthez-sentiment-classification](https://huggingface.co/moussaKam/barthez-sentiment-classification) based on [BARThez](https://huggingface.co/moussaKam/barthez) use the same bi-class definition between them. To bring this back to a two-class problem, we will only consider the *"1 star"* and *"2 stars"* labels for the *negative* sentiments and *"4 stars"* and *"5 stars"* for *positive* sentiments. We exclude the *"3 stars"* which can be interpreted as a *neutral* class. In this context, the problem of +/-1 star estimation errors disappears. Then we use only the classical accuracy definition.

| **model** | **time (ms)** | **exact accuracy (%)** |
| :-------: | :-----------: | :--------------------: |
| [cmarkea/distilcamembert-base-sentiment](https://huggingface.co/cmarkea/distilcamembert-base-sentiment) | **95.56** | **97.52** |
| [tblard/tf-allocine](https://huggingface.co/tblard/tf-allocine) | 329.74 | 95.69 |
| [moussaKam/barthez-sentiment-classification](https://huggingface.co/moussaKam/barthez-sentiment-classification) | 197.95 | 94.29 |

How to use DistilCamemBERT-Sentiment
------------------------------------

```python
from transformers import pipeline

analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer="cmarkea/distilcamembert-base-sentiment"
)
result = analyzer(
    "J'aime me promener en forêt même si ça me donne mal aux pieds.",
    return_all_scores=True
)

result
[{'label': '1 star',
  'score': 0.047529436647892},
 {'label': '2 stars',
  'score': 0.14150355756282806},
 {'label': '3 stars',
  'score': 0.3586442470550537},
 {'label': '4 stars',
  'score': 0.3181498646736145},
 {'label': '5 stars',
  'score': 0.13417290151119232}]
```

### Optimum + ONNX

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline

HUB_MODEL = "cmarkea/distilcamembert-base-sentiment"

tokenizer = AutoTokenizer.from_pretrained(HUB_MODEL)
model = ORTModelForSequenceClassification.from_pretrained(HUB_MODEL)
onnx_qa = pipeline("text-classification", model=model, tokenizer=tokenizer)

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