---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: smolm-autoreg-bpe-seed_2309
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# smolm-autoreg-bpe-seed_2309

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4752
- Accuracy: 0.4999

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.003
- train_batch_size: 16
- eval_batch_size: 128
- seed: 2309
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 24000
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.0551        | 1.0   | 2928  | 3.0203          | 0.4362   |
| 2.7076        | 2.0   | 5856  | 2.7878          | 0.4595   |
| 2.5796        | 3.0   | 8784  | 2.6938          | 0.4705   |
| 2.4976        | 4.0   | 11712 | 2.6370          | 0.4768   |
| 2.4691        | 5.0   | 14640 | 2.6149          | 0.4800   |
| 2.421         | 6.0   | 17568 | 2.5835          | 0.4827   |
| 2.3918        | 7.0   | 20496 | 2.5660          | 0.4860   |
| 2.3654        | 8.0   | 23424 | 2.5586          | 0.4854   |
| 2.2908        | 9.0   | 26352 | 2.5052          | 0.4948   |
| 2.1465        | 10.0  | 29280 | 2.4752          | 0.4999   |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
