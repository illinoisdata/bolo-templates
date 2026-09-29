---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_1709
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_1709

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4932
- Accuracy: 0.4961

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
- seed: 1709
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 24000
- num_epochs: 20.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.2972        | 1.0   | 2928  | 3.2235          | 0.4226   |
| 2.8563        | 2.0   | 5856  | 2.8899          | 0.4504   |
| 2.6527        | 3.0   | 8784  | 2.7421          | 0.4648   |
| 2.5452        | 4.0   | 11712 | 2.6701          | 0.4721   |
| 2.5034        | 5.0   | 14640 | 2.6426          | 0.4755   |
| 2.471         | 6.0   | 17568 | 2.6162          | 0.4795   |
| 2.4497        | 7.0   | 20496 | 2.6053          | 0.4811   |
| 2.4389        | 8.0   | 23424 | 2.6032          | 0.4814   |
| 2.4232        | 9.0   | 26352 | 2.5767          | 0.4837   |
| 2.3762        | 10.0  | 29280 | 2.5590          | 0.4852   |
| 2.339         | 11.0  | 32208 | 2.5337          | 0.4884   |
| 2.3109        | 12.0  | 35136 | 2.5224          | 0.4911   |
| 2.2803        | 13.0  | 38064 | 2.5112          | 0.4924   |
| 2.2357        | 14.0  | 40992 | 2.5025          | 0.4942   |
| 2.2013        | 15.0  | 43920 | 2.4973          | 0.4957   |
| 2.1591        | 16.0  | 46848 | 2.4932          | 0.4961   |
| 2.1092        | 17.0  | 49776 | 2.4934          | 0.4963   |
| 2.0504        | 18.0  | 52704 | 2.4953          | 0.4980   |
| 1.9935        | 19.0  | 55632 | 2.4979          | 0.4983   |


### Framework versions

- Transformers 4.38.0
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.15.2