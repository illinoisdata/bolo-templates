---
tags:
- generated_from_trainer
model-index:
- name: event-extraction-tagger
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# event-extraction-tagger

This model was finetuned on Wikipedia's current events portal

## Model description

Extracts events mentioned in text by framing it as a token classification task with labels B-event, I-event and O

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

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

- Transformers 4.44.0
- Pytorch 2.4.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1