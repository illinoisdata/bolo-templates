---
library_name: transformers
license: apache-2.0
base_model: Salesforce/codet5-base
tags:
- generated_from_trainer
model-index:
- name: py38-pylingual-v1-statement
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# py38-pylingual-v1-statement

This model is a fine-tuned version of [Salesforce/codet5-base](https://huggingface.co/Salesforce/codet5-base) on the syssec-utd/statement-py38-pylingual-v1-tokenized dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- total_train_batch_size: 48
- total_eval_batch_size: 48
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.1
- Tokenizers 0.21.0