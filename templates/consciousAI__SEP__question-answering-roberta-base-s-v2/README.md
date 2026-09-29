---
license: apache-2.0
tags:
- Question Answering
metrics:
- squad
model-index:
- name: consciousAI/question-answering-roberta-base-s-v2
  results: []
---

# Question Answering 
The model is intended to be used for Q&A task, given the question & context, the model would attempt to infer the answer text, answer span & confidence score.<br>
Model is encoder-only (deepset/roberta-base-squad2) with QuestionAnswering LM Head, fine-tuned on SQUADx dataset with **exact_match:** 84.83 & **f1:** 91.80 performance scores.

[Live Demo: Question Answering Encoders vs Generative](https://huggingface.co/spaces/consciousAI/question_answering)

Please follow this link for [Encoder based Question Answering V1](https://huggingface.co/consciousAI/question-answering-roberta-base-s/)
<br>Please follow this link for [Generative Question Answering](https://huggingface.co/consciousAI/question-answering-generative-t5-v1-base-s-q-c/)

Example code:
```
from transformers import pipeline

model_checkpoint = "consciousAI/question-answering-roberta-base-s-v2"

context = """
🤗 Transformers is backed by the three most popular deep learning libraries — Jax, PyTorch and TensorFlow — with a seamless integration
between them. It's straightforward to train your models with one before loading them for inference with the other.
"""
question = "Which deep learning libraries back 🤗 Transformers?"

question_answerer = pipeline("question-answering", model=model_checkpoint)
question_answerer(question=question, context=context)

```

## Training and evaluation data

SQUAD Split

## Training procedure

Preprocessing:
1. SQUAD Data longer chunks were sub-chunked with input context max-length 384 tokens and stride as 128 tokens.
2. Target answers readjusted for sub-chunks, sub-chunks with no-answers or partial answers were set to target answer span as (0,0)

Metrics:
1. Adjusted accordingly to handle sub-chunking.
2. n best = 20
3. skip answers with length zero or higher than max answer length (30)

### Training hyperparameters
Custom Training Loop:
The following hyperparameters were used during training:
- learning_rate: 2e-5
- train_batch_size: 32
- eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results
{'exact_match': 84.83443708609272, 'f1': 91.79987545811638}

### Framework versions

- Transformers 4.23.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.13.0