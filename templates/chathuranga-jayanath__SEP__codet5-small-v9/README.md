---
license: apache-2.0
base_model: Salesforce/codet5-small
tags:
- generated_from_trainer
model-index:
- name: codet5-small-v9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codet5-small-v9

This model is a fine-tuned version of [Salesforce/codet5-small](https://huggingface.co/Salesforce/codet5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0927
- Bleu Score: 0.0023
- Gen Len: 15.5678

## Model description

Trained prompt: [BUG]...[CONTEXT]...

## Intended uses & limitations


## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 30
- eval_batch_size: 30
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu Score | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:----------:|:-------:|
| 0.4292        | 1.0   | 656  | 0.1354          | 0.0023     | 15.4664 |
| 0.1655        | 2.0   | 1312 | 0.1019          | 0.0023     | 15.5576 |
| 0.1233        | 3.0   | 1968 | 0.0927          | 0.0023     | 15.5678 |


### Framework versions

- Transformers 4.38.0.dev0
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1