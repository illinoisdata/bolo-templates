---
license: mit
datasets:
- unicamp-dl/mmarco
language:
- es
tags:
- colbert
- ColBERT
---

## Training

#### Details

The model is initialized from the [ColBERTv1.0-bert-based-spanish-mmarcoES](https://huggingface.co/AdrienB134/ColBERTv1.0-bert-based-spanish-mmarcoES) checkpoint and trained using the ColBERTv2 style of training.  
It was trained on 2 Tesla T4 GPU with 16GBs of memory each with 20k warmup steps warmup using a batch size of 64 and the AdamW optimizer with a constant learning rate of 1e-05. 
Total training time was around 60 hours.

#### Data

The model is fine-tuned on the Spanish version of the [mMARCO](https://huggingface.co/datasets/unicamp-dl/mmarco) dataset, a multi-lingual machine-translated version of the MS MARCO dataset.


## Evaluation

The model is evaluated on the smaller development set of mMARCO-es, which consists of 6,980 queries for a corpus of 8.8M candidate passages. We report the mean reciprocal rank (MRR) and recall at various cut-offs (R@k).

| model                                                                                                                   |  Vocab. | #Param. |  Size |   MRR@10 |   R@50 |  R@1000 |
|:------------------------------------------------------------------------------------------------------------------------|:--------|--------:|------:|---------:|-------:|--------:|
| **ColBERTv2.0-spanish-mmarcoES**                                                                                        | spanish |    110M | 440MB |    **32.86** |  **76.46** |   **81.06** |
| **ColBERTv1.0-bert-based-spanish-mmarcoES**                                                                             | spanish |    110M | 440MB |    24.70 |  59,23 |   63.86 |