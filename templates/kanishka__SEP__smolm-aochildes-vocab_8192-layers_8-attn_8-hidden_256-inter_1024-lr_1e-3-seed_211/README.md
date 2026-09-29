---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_211
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_211

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4916
- Accuracy: 0.4976

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
- seed: 211
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 24000
- num_epochs: 20.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.3066        | 1.0   | 2928  | 3.2340          | 0.4211   |
| 2.8679        | 2.0   | 5856  | 2.9006          | 0.4498   |
| 2.6589        | 3.0   | 8784  | 2.7427          | 0.4640   |
| 2.5669        | 4.0   | 11712 | 2.6725          | 0.4723   |
| 2.4972        | 5.0   | 14640 | 2.6331          | 0.4768   |
| 2.4769        | 6.0   | 17568 | 2.6187          | 0.4790   |
| 2.4547        | 7.0   | 20496 | 2.6075          | 0.4802   |
| 2.4472        | 8.0   | 23424 | 2.6004          | 0.4807   |
| 2.4248        | 9.0   | 26352 | 2.5779          | 0.4847   |
| 2.3811        | 10.0  | 29280 | 2.5608          | 0.4858   |
| 2.3435        | 11.0  | 32208 | 2.5386          | 0.4893   |
| 2.3179        | 12.0  | 35136 | 2.5243          | 0.4896   |
| 2.274         | 13.0  | 38064 | 2.5168          | 0.4919   |
| 2.2358        | 14.0  | 40992 | 2.5043          | 0.4936   |
| 2.2084        | 15.0  | 43920 | 2.5034          | 0.4945   |
| 2.158         | 16.0  | 46848 | 2.4918          | 0.4960   |
| 2.1051        | 17.0  | 49776 | 2.4916          | 0.4976   |
| 2.0558        | 18.0  | 52704 | 2.4946          | 0.4990   |
| 1.9885        | 19.0  | 55632 | 2.4998          | 0.4985   |
| 1.9244        | 20.0  | 58560 | 2.5085          | 0.4982   |


### Framework versions

- Transformers 4.38.0
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.15.2