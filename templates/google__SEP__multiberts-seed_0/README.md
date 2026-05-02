---
language: en
tags:
-   multiberts
-   multiberts-seed_0
license: apache-2.0
---

# MultiBERTs - Seed 0

MultiBERTs is a collection of checkpoints and a statistical library to support
robust research on BERT. We provide 25 BERT-base models trained with
similar hyper-parameters as
[the original BERT model](https://github.com/google-research/bert) but
with different random seeds, which causes variations in the initial weights and order of
training instances. The aim is to distinguish findings that apply to a specific
artifact (i.e., a particular instance of the model) from those that apply to the
more general procedure.

We also provide 140 intermediate checkpoints captured
during the course of pre-training (we saved 28 checkpoints for the first 5 runs).

The models were originally released through
[http://goo.gle/multiberts](http://goo.gle/multiberts). We describe them in our
paper
[The MultiBERTs: BERT Reproductions for Robustness Analysis](https://arxiv.org/abs/2106.16163).

This is model #0.

## Model Description

This model is a reproduction of
[BERT-base uncased](https://github.com/google-research/bert), for English: it
is a Transformers model pretrained on a large corpus of English data, using the
Masked Language Modelling (MLM) and the Next Sentence Prediction (NSP)
objectives.

The intended uses, limitations, training data and training procedure are similar
to [BERT-base uncased](https://github.com/google-research/bert). Two major
differences with the original model:

*   We pre-trained the MultiBERTs models for 2 million steps using sequence
    length 512 (instead of 1 million steps using sequence length 128 then 512).
*   We used an alternative version of Wikipedia and Books Corpus, initially
    collected for [Turc et al., 2019](https://arxiv.org/abs/1908.08962).

This is a best-effort reproduction, and so it is probable that differences with
the original model have gone unnoticed. The performance of MultiBERTs on GLUE is oftentimes comparable to that of original
BERT, but we found significant differences on the dev set of SQuAD (MultiBERTs outperforms original BERT).
See our [technical report](https://arxiv.org/abs/2106.16163) for more details.

### How to use

Using code from
[BERT-base uncased](https://huggingface.co/bert-base-uncased), here is an example based on
Tensorflow:

```
from transformers import BertTokenizer, TFBertModel
tokenizer = BertTokenizer.from_pretrained('google/multiberts-seed_0')
model = TFBertModel.from_pretrained("google/multiberts-seed_0")
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
```

PyTorch version:

```
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('google/multiberts-seed_0')
model = BertModel.from_pretrained("google/multiberts-seed_0")
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

## Citation info

```bibtex
@article{sellam2021multiberts,
  title={The MultiBERTs: BERT Reproductions for Robustness Analysis},
  author={Thibault Sellam and Steve Yadlowsky and Jason Wei and Naomi Saphra and Alexander D'Amour and Tal Linzen and Jasmijn Bastings and Iulia Turc and Jacob Eisenstein and Dipanjan Das and Ian Tenney and Ellie Pavlick},
  journal={arXiv preprint arXiv:2106.16163},
  year={2021}
}
```