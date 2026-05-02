---
language: 
- hr
- bs
- sr
- cnr
- hbs

license: apache-2.0
---

# BERTić&ast; [bert-ich] /bɜrtitʃ/ - A transformer language model for Bosnian, Croatian, Montenegrin and Serbian

&ast; The name should resemble the facts (1) that the model was trained in Zagreb, Croatia, where diminutives ending in -ić (as in fotić, smajlić, hengić etc.) are very popular, and (2) that most surnames in the countries where these languages are spoken end in -ić (with diminutive etymology as well).

This Electra model was trained on more than 8 billion tokens of Bosnian, Croatian, Montenegrin and Serbian text.

**&ast;new&ast;** We have published a version of this model fine-tuned on the named entity recognition task ([bcms-bertic-ner](https://huggingface.co/classla/bcms-bertic-ner)) and on the hate speech detection task ([bcms-bertic-frenk-hate](https://huggingface.co/classla/bcms-bertic-frenk-hate)).

If you use the model, please cite the following paper:

```
@inproceedings{ljubesic-lauc-2021-bertic,
    title = "{BERT}i{\'c} - The Transformer Language Model for {B}osnian, {C}roatian, {M}ontenegrin and {S}erbian",
    author = "Ljube{\v{s}}i{\'c}, Nikola  and Lauc, Davor",
    booktitle = "Proceedings of the 8th Workshop on Balto-Slavic Natural Language Processing",
    month = apr,
    year = "2021",
    address = "Kiyv, Ukraine",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.bsnlp-1.5",
    pages = "37--42",
}
```

## Benchmarking

Comparing this model to [multilingual BERT](https://huggingface.co/bert-base-multilingual-cased) and [CroSloEngual BERT](https://huggingface.co/EMBEDDIA/crosloengual-bert) on the tasks of (1) part-of-speech tagging, (2) named entity recognition, (3) geolocation prediction, and (4) commonsense causal reasoning, shows the BERTić model to be superior to the other two.

### Part-of-speech tagging

Evaluation metric is (seqeval) microF1. Reported are means of five runs. Best results are presented in bold. Statistical significance is calculated between two best-performing systems via a two-tailed t-test (&ast; p<=0.05, &ast;&ast; p<=0.01, &ast;&ast;&ast; p<=0.001, &ast;&ast;&ast;&ast;&ast; p<=0.0001).

Dataset  | Language | Variety | CLASSLA | mBERT | cseBERT | BERTić
---|---|---|---|---|---|---
hr500k | Croatian | standard | 93.87 | 94.60 | 95.74 | **95.81&ast;&ast;&ast;**
reldi-hr | Croatian | internet non-standard | - | 88.87 | 91.63 | **92.28&ast;&ast;&ast;**
SETimes.SR | Serbian | standard | 95.00 | 95.50 | **96.41** | 96.31
reldi-sr | Serbian | internet non-standard | - | 91.26 |  93.54 | **93.90&ast;&ast;&ast;**

### Named entity recognition

Evaluation metric is (seqeval) microF1. Reported are means of five runs. Best results are presented in bold. Statistical significance is calculated between two best-performing systems via a two-tailed t-test (&ast; p<=0.05, &ast;&ast; p<=0.01, &ast;&ast;&ast; p<=0.001, &ast;&ast;&ast;&ast;&ast; p<=0.0001).

Dataset  | Language | Variety | CLASSLA | mBERT | cseBERT | BERTić
---|---|---|---|---|---|---
hr500k | Croatian | standard | 80.13 | 85.67 | 88.98 | **89.21&ast;&ast;&ast;&ast;**
reldi-hr | Croatian | internet non-standard | - | 76.06 | 81.38 | **83.05&ast;&ast;&ast;&ast;**
SETimes.SR | Serbian | standard | 84.64 | **92.41** | 92.28 | 92.02
reldi-sr | Serbian | internet non-standard | - | 81.29 | 82.76 | **87.92&ast;&ast;&ast;&ast;**


### Geolocation prediction

The dataset comes from the VarDial 2020 evaluation campaign's shared task on [Social Media variety Geolocation prediction](https://sites.google.com/view/vardial2020/evaluation-campaign). The task is to predict the latitude and longitude of a tweet given its text.

Evaluation metrics are median and mean of distance between gold and predicted geolocations (lower is better). No statistical significance is computed due to large test set (39,723 instances). Centroid baseline predicts each text to be created in the centroid of the training dataset.

System | Median | Mean
---|---|---
centroid | 107.10 | 145.72 
mBERT | 42.25 | 82.05 
cseBERT | 40.76 | 81.88
BERTić | **37.96** | **79.30**

### Choice Of Plausible Alternatives

The dataset is a translation of the [COPA dataset](https://people.ict.usc.edu/~gordon/copa.html) into Croatian ([link to the dataset](http://hdl.handle.net/11356/1404)).

Evaluation metric is accuracy. Reported are means of five runs. Best results are presented in bold. Statistical significance is calculated between two best-performing systems via a two-tailed t-test (&ast; p<=0.05, &ast;&ast; p<=0.01, &ast;&ast;&ast; p<=0.001, &ast;&ast;&ast;&ast;&ast; p<=0.0001).

System | Accuracy
---|---
random | 50.00
mBERT | 54.12
cseBERT | 61.80
BERTić | **65.76&ast;&ast;**