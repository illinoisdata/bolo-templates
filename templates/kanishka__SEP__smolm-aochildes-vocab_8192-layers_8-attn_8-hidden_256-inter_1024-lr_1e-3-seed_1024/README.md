---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_1024
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_1024

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4920
- Accuracy: 0.4972

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
- seed: 1024
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 24000
- num_epochs: 20.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.3019        | 1.0   | 2928  | 3.2185          | 0.4233   |
| 2.8528        | 2.0   | 5856  | 2.8859          | 0.4519   |
| 2.6521        | 3.0   | 8784  | 2.7378          | 0.4656   |
| 2.5541        | 4.0   | 11712 | 2.6664          | 0.4718   |
| 2.4913        | 5.0   | 14640 | 2.6308          | 0.4768   |
| 2.4743        | 6.0   | 17568 | 2.6151          | 0.4801   |
| 2.457         | 7.0   | 20496 | 2.6045          | 0.4803   |
| 2.4417        | 8.0   | 23424 | 2.6016          | 0.4804   |
| 2.4233        | 9.0   | 26352 | 2.5709          | 0.4852   |
| 2.371         | 10.0  | 29280 | 2.5555          | 0.4866   |
| 2.3386        | 11.0  | 32208 | 2.5369          | 0.4894   |
| 2.3118        | 12.0  | 35136 | 2.5268          | 0.4901   |
| 2.2846        | 13.0  | 38064 | 2.5160          | 0.4927   |
| 2.2349        | 14.0  | 40992 | 2.5059          | 0.4943   |
| 2.2032        | 15.0  | 43920 | 2.4964          | 0.4950   |
| 2.1625        | 16.0  | 46848 | 2.4924          | 0.4958   |
| 2.105         | 17.0  | 49776 | 2.4920          | 0.4972   |
| 2.0585        | 18.0  | 52704 | 2.4922          | 0.4974   |
| 1.9865        | 19.0  | 55632 | 2.4997          | 0.4981   |
| 1.9236        | 20.0  | 58560 | 2.5079          | 0.4981   |


### Framework versions

- Transformers 4.38.0
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.15.2