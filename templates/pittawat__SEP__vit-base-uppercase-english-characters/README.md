---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: vit-base-uppercase-english-characters
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-uppercase-english-characters

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the pittawat/uppercase-english-characters dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3160
- Accuracy: 0.9573

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.5944        | 1.35  | 100  | 0.5538          | 0.9487   |
| 0.2241        | 2.7   | 200  | 0.3160          | 0.9573   |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.0
- Datasets 2.1.0
- Tokenizers 0.13.2
