---
tags:
- generated_from_trainer
- summarization
- finance
model-index:
- name: T5-Base-10K-Summarization
  results: []
---

# T5-Base-10K-Summarization

This model is a fine-tuned version of Google's T5-Base model tailored for summarizing financial 10K report sections.

## Model description

T5-Base-10K-Summarization is optimized to condense lengthy 10K reports into manageable summaries, enabling quick insights into financial data and trends.

## Intended uses & limitations

Ideal for use by financial analysts and regulatory agencies needing rapid insights from 10K reports. It may not be suited for summarizing non-financial documents or informal texts.

## Training and evaluation data

Trained on a diverse collection of 10K reports from various industries, annotated for summarization to ensure broad applicability and accuracy.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Tokenizers 0.19.1