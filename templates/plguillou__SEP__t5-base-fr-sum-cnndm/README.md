---
language: fr
tags:
- pytorch
- t5
- seq2seq
- summarization
datasets: cnn_dailymail
widget:
- text: "Apollo 11 est une mission du programme spatial américain Apollo au cours de laquelle, pour la première fois, des hommes se sont posés sur la Lune, le lundi 21 juillet 1969. L'agence spatiale américaine, la NASA, remplit ainsi l'objectif fixé par le président John F. Kennedy en 1961 de poser un équipage sur la Lune avant la fin de la décennie 1960. Il s'agissait de démontrer la supériorité des États-Unis sur l'Union soviétique qui avait été mise à mal par les succès soviétiques au début de l'ère spatiale dans le contexte de la guerre froide qui oppose alors ces deux pays. Ce défi est lancé alors que la NASA n'a pas encore placé en orbite un seul astronaute. Grâce à une mobilisation de moyens humains et financiers considérables, l'agence spatiale rattrape puis dépasse le programme spatial soviétique."
  example_title: "Apollo 11"
---

# French T5 Abstractive Text Summarization

~~Version 1.0 (I will keep improving the model's performances.)~~

Version 2.0 is here! (with improved performances of course)

I trained the model on 13x more data than v1.

ROUGE-1: 44.5252

ROUGE-2: 22.652

ROUGE-L: 29.8866

## Model description

This model is a T5 Transformers model (JDBN/t5-base-fr-qg-fquad) that was fine-tuned in french for abstractive text summarization.

## How to use

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("plguillou/t5-base-fr-sum-cnndm")
model = T5ForConditionalGeneration.from_pretrained("plguillou/t5-base-fr-sum-cnndm")
```

To summarize an ARTICLE, just modify the string like this : "summarize: ARTICLE".

## Training data

The base model I used is JDBN/t5-base-fr-qg-fquad (it can perform question generation, question answering and answer extraction).

I used the "t5-base" model from the transformers library to translate in french the CNN / Daily Mail summarization dataset.