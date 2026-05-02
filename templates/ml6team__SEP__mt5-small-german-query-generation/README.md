---
language: 
- de
tags:
- pytorch
- query-generation
widget:
- text: "Das Lama (Lama glama) ist eine Art der Kamele. Es ist in den südamerikanischen Anden verbreitet und eine vom Guanako abstammende Haustierform."
  example_title: "Article 1"
license: apache-2.0
metrics:
- Rouge-Score
---
# mt5-small-german-query-generation 

## Model description:
This model was created with the purpose to generate possible queries for a german input article.

For this model, we finetuned a multilingual T5 model [mt5-small](https://huggingface.co/google/mt5-small) on the [MMARCO dataset](https://huggingface.co/datasets/unicamp-dl/mmarco) the machine translated version of the MS MARCO dataset. 


The model was trained for 1 epoch, on 200,000 unique queries of the dataset. We trained the model on one K80 GPU for 25,000 iterations with following parameters:
  - learning rate: 1e-3
  - train batch size: 8
  - max input sequence length: 512
  - max target sequence length: 64


## Model Performance:

Model evaluation was done on 2000 evaluation paragraphs of the dataset. Mean [f1 ROUGE scores](https://github.com/pltrdy/rouge) were calculated for the model. 

| Rouge-1 | Rouge-2 | Rouge-L |
|---|---|---|
|0.162 | 0.052 | 0.161 |