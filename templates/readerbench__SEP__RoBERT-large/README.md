Model card for RoBERT-large

---
language: 
- ro
---

# RoBERT-large


## Pretrained BERT model for Romanian 

Pretrained model on Romanian language using a masked language modeling (MLM) and next sentence prediction (NSP) objective. 
It was introduced in this [paper](https://www.aclweb.org/anthology/2020.coling-main.581/). Three BERT models were released: RoBERT-small, RoBERT-base and **RoBERT-large**, all versions uncased.

| Model          | Weights   |   L    |   H    |    A   | MLM accuracy   | NSP accuracy   |
|----------------|:---------:|:------:|:------:|:------:|:--------------:|:--------------:|
| RoBERT-small | 19M     | 12   | 256  | 8    | 0.5363       | 0.9687       |
| RoBERT-base    | 114M      | 12     | 768    | 12     | 0.6511         | 0.9802         |
| *RoBERT-large*   | *341M*      | *24*     | *1024*   | *24*     | *0.6929*         | *0.9843*         |




All models are available:

* [RoBERT-small](https://huggingface.co/readerbench/RoBERT-small)
* [RoBERT-base](https://huggingface.co/readerbench/RoBERT-base)
* [RoBERT-large](https://huggingface.co/readerbench/RoBERT-large)



#### How to use

```python
# tensorflow
from transformers import AutoModel, AutoTokenizer, TFAutoModel
tokenizer = AutoTokenizer.from_pretrained("readerbench/RoBERT-large")
model = TFAutoModel.from_pretrained("readerbench/RoBERT-large")
inputs = tokenizer("exemplu de propoziție", return_tensors="tf")
outputs = model(inputs)

# pytorch
from transformers import AutoModel, AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("readerbench/RoBERT-large")
model = AutoModel.from_pretrained("readerbench/RoBERT-large")
inputs = tokenizer("exemplu de propoziție", return_tensors="pt")
outputs = model(**inputs)
```


## Training data

The model is trained on the following compilation of corpora. Note that we present the statistics after the cleaning process.

| Corpus    | Words     | Sentences | Size (GB)|
|-----------|:---------:|:---------:|:--------:|
| Oscar     | 1.78B     | 87M       | 10.8     |
| RoTex     | 240M      | 14M       | 1.5      |
| RoWiki    | 50M       | 2M        | 0.3      |
| **Total** | **2.07B** | **103M**  | **12.6** |


## Downstream performance

### Sentiment analysis

We report Macro-averaged F1 score (in %)

| Model            | Dev      | Test     |
|------------------|:--------:|:--------:|
| multilingual-BERT| 68.96    | 69.57    |
| XLM-R-base       | 71.26    | 71.71    |
| BERT-base-ro     | 70.49    | 71.02    |
| RoBERT-small     | 66.32    | 66.37    |
| RoBERT-base      | 70.89    | 71.61    |
| *RoBERT-large*   | **72.48**| **72.11**|

### Moldavian vs. Romanian Dialect and Cross-dialect Topic identification

We report results on [VarDial 2019](https://sites.google.com/view/vardial2019/campaign) Moldavian vs. Romanian Cross-dialect Topic identification Challenge, as Macro-averaged F1 score (in %).

| Model             | Dialect Classification | MD to RO | RO to MD |
|-------------------|:----------------------:|:--------:|:--------:|
| 2-CNN + SVM       | 93.40                  | 65.09    | 75.21    |
| Char+Word SVM     | 96.20                  | 69.08    | 81.93    |
| BiGRU             | 93.30                  | **70.10**| 80.30    |
| multilingual-BERT | 95.34                  | 68.76    | 78.24    |
| XLM-R-base        | 96.28                  | 69.93    | 82.28    |
| BERT-base-ro      | 96.20                  | 69.93    | 78.79    |
| RoBERT-small      | 95.67                  | 69.01    | 80.40    |
| RoBERT-base       | 97.39                  | 68.30    | 81.09    |
| *RoBERT-large*    | **97.78**              | *69.91*  | **83.65**|

### Diacritics Restoration

Challenge can be found [here](https://diacritics-challenge.speed.pub.ro/). We report results on the official test set, as accuracies in %.

| Model                       | word level | char level |
|-----------------------------|:----------:|:----------:|
| BiLSTM                      | 99.42      | -          |
| CharCNN                     | 98.40      | 99.65      |
| CharCNN + multilingual-BERT | 99.72      | 99.94      |
| CharCNN + XLM-R-base        | 99.76      | **99.95**  |
| CharCNN + BERT-base-ro      | **99.79**  | **99.95**  |
| CharCNN + RoBERT-small      | 99.73      |  99.94     |
| CharCNN + RoBERT-base       | 99.78      | **99.95**  |
| *CharCNN + RoBERT-large*    | *99.76*    | **99.95**  |


### BibTeX entry and citation info

```bibtex
@inproceedings{masala2020robert,
  title={RoBERT--A Romanian BERT Model},
  author={Masala, Mihai and Ruseti, Stefan and Dascalu, Mihai},
  booktitle={Proceedings of the 28th International Conference on Computational Linguistics},
  pages={6626--6637},
  year={2020}
}
```