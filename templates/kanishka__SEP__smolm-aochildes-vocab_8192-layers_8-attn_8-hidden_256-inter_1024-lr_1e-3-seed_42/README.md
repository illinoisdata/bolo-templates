---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_42

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4920
- Accuracy: 0.4962

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 16
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 24000
- num_epochs: 20.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.3054        | 1.0   | 2928  | 3.2320          | 0.4213   |
| 2.8563        | 2.0   | 5856  | 2.8929          | 0.4503   |
| 2.6596        | 3.0   | 8784  | 2.7392          | 0.4652   |
| 2.5465        | 4.0   | 11712 | 2.6691          | 0.4730   |
| 2.5012        | 5.0   | 14640 | 2.6355          | 0.4764   |
| 2.4757        | 6.0   | 17568 | 2.6153          | 0.4787   |
| 2.4509        | 7.0   | 20496 | 2.6033          | 0.4791   |
| 2.4401        | 8.0   | 23424 | 2.5999          | 0.4799   |
| 2.4264        | 9.0   | 26352 | 2.5776          | 0.4838   |
| 2.3886        | 10.0  | 29280 | 2.5566          | 0.4864   |
| 2.3385        | 11.0  | 32208 | 2.5341          | 0.4889   |
| 2.3074        | 12.0  | 35136 | 2.5232          | 0.4903   |
| 2.2746        | 13.0  | 38064 | 2.5146          | 0.4918   |
| 2.2323        | 14.0  | 40992 | 2.5030          | 0.4934   |
| 2.1894        | 15.0  | 43920 | 2.5011          | 0.4948   |
| 2.1608        | 16.0  | 46848 | 2.4920          | 0.4962   |
| 2.1094        | 17.0  | 49776 | 2.4947          | 0.4968   |
| 2.0509        | 18.0  | 52704 | 2.4931          | 0.4981   |
| 1.9852        | 19.0  | 55632 | 2.5010          | 0.4980   |


### Framework versions

- Transformers 4.38.0
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.15.2