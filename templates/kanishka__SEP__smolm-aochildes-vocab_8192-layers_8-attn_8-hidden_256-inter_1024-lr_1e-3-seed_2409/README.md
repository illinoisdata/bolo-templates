---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_2409
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_2409

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4882
- Accuracy: 0.4981

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
- seed: 2409
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 24000
- num_epochs: 20.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.3001        | 1.0   | 2928  | 3.2264          | 0.4217   |
| 2.8648        | 2.0   | 5856  | 2.9074          | 0.4497   |
| 2.6734        | 3.0   | 8784  | 2.7481          | 0.4638   |
| 2.5598        | 4.0   | 11712 | 2.6742          | 0.4715   |
| 2.5101        | 5.0   | 14640 | 2.6399          | 0.4753   |
| 2.4816        | 6.0   | 17568 | 2.6169          | 0.4779   |
| 2.454         | 7.0   | 20496 | 2.6083          | 0.4791   |
| 2.445         | 8.0   | 23424 | 2.6006          | 0.4792   |
| 2.4111        | 9.0   | 26352 | 2.5726          | 0.4846   |
| 2.385         | 10.0  | 29280 | 2.5509          | 0.4866   |
| 2.3402        | 11.0  | 32208 | 2.5366          | 0.4892   |
| 2.306         | 12.0  | 35136 | 2.5242          | 0.4911   |
| 2.2773        | 13.0  | 38064 | 2.5114          | 0.4925   |
| 2.2262        | 14.0  | 40992 | 2.5019          | 0.4939   |
| 2.1914        | 15.0  | 43920 | 2.4951          | 0.4951   |
| 2.1503        | 16.0  | 46848 | 2.4916          | 0.4968   |
| 2.1054        | 17.0  | 49776 | 2.4882          | 0.4981   |
| 2.0424        | 18.0  | 52704 | 2.4923          | 0.4979   |
| 1.9798        | 19.0  | 55632 | 2.5003          | 0.4981   |
| 1.9075        | 20.0  | 58560 | 2.5082          | 0.4985   |


### Framework versions

- Transformers 4.38.0
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.15.2