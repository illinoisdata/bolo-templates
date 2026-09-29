---
language:
- en
license: mit
base_model: roberta-large
tags:
- generated_from_trainer
datasets:
- schone-power
model-index:
- name: final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# final

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the GLUE SCHONE_POW dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1556
- Roc Auc: 0.9742

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 128
- eval_batch_size: 256
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Roc Auc |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.2924        | 0.9985 | 332  | 0.2605          | 0.9248  |
| 0.2553        | 2.0    | 665  | 0.2234          | 0.9468  |
| 0.2317        | 2.9985 | 997  | 0.1899          | 0.9620  |
| 0.2063        | 4.0    | 1330 | 0.1645          | 0.9715  |
| 0.1897        | 4.9925 | 1660 | 0.1556          | 0.9742  |


### Framework versions

- Transformers 4.44.0.dev0
- Pytorch 2.0.1+cu118
- Datasets 2.20.0
- Tokenizers 0.19.1