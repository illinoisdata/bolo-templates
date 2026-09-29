---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: smolm-autoreg-bpe-seed_496
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# smolm-autoreg-bpe-seed_496

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4752
- Accuracy: 0.4995

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
- seed: 496
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 24000
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.0603        | 1.0   | 2928  | 3.0255          | 0.4367   |
| 2.7088        | 2.0   | 5856  | 2.7873          | 0.4580   |
| 2.586         | 3.0   | 8784  | 2.6956          | 0.4688   |
| 2.5037        | 4.0   | 11712 | 2.6362          | 0.4772   |
| 2.466         | 5.0   | 14640 | 2.6123          | 0.4787   |
| 2.4203        | 6.0   | 17568 | 2.5878          | 0.4828   |
| 2.3871        | 7.0   | 20496 | 2.5691          | 0.4855   |
| 2.367         | 8.0   | 23424 | 2.5567          | 0.4880   |
| 2.2871        | 9.0   | 26352 | 2.5026          | 0.4941   |
| 2.1368        | 10.0  | 29280 | 2.4752          | 0.4995   |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
