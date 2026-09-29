---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_210
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# smolm-aochildes-vocab_8192-layers_8-attn_8-hidden_256-inter_1024-lr_1e-3-seed_210

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4903
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
- seed: 210
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 24000
- num_epochs: 20.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.3163        | 1.0   | 2928  | 3.2312          | 0.4214   |
| 2.8574        | 2.0   | 5856  | 2.9029          | 0.4492   |
| 2.653         | 3.0   | 8784  | 2.7476          | 0.4637   |
| 2.5644        | 4.0   | 11712 | 2.6728          | 0.4723   |
| 2.5093        | 5.0   | 14640 | 2.6416          | 0.4764   |
| 2.4761        | 6.0   | 17568 | 2.6137          | 0.4798   |
| 2.4411        | 7.0   | 20496 | 2.6089          | 0.4805   |
| 2.4423        | 8.0   | 23424 | 2.5978          | 0.4813   |
| 2.4153        | 9.0   | 26352 | 2.5725          | 0.4846   |
| 2.3679        | 10.0  | 29280 | 2.5454          | 0.4865   |
| 2.3469        | 11.0  | 32208 | 2.5452          | 0.4887   |
| 2.2991        | 12.0  | 35136 | 2.5217          | 0.4912   |
| 2.2761        | 13.0  | 38064 | 2.5047          | 0.4930   |
| 2.225         | 14.0  | 40992 | 2.5018          | 0.4943   |
| 2.1946        | 15.0  | 43920 | 2.4924          | 0.4963   |
| 2.1489        | 16.0  | 46848 | 2.4906          | 0.4967   |
| 2.0948        | 17.0  | 49776 | 2.4908          | 0.4981   |
| 2.0438        | 18.0  | 52704 | 2.4903          | 0.4981   |
| 1.9705        | 19.0  | 55632 | 2.4985          | 0.4980   |
| 1.9167        | 20.0  | 58560 | 2.5070          | 0.4985   |


### Framework versions

- Transformers 4.38.0
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.15.2