---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- cord-layoutlmv3
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-cord_500
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: cord-layoutlmv3
      type: cord-layoutlmv3
      config: cord
      split: train
      args: cord
    metrics:
    - name: Precision
      type: precision
      value: 0.9509293680297398
    - name: Recall
      type: recall
      value: 0.9573353293413174
    - name: F1
      type: f1
      value: 0.9541215964192465
    - name: Accuracy
      type: accuracy
      value: 0.9609507640067911
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_500

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2339
- Precision: 0.9509
- Recall: 0.9573
- F1: 0.9541
- Accuracy: 0.9610

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
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 4000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 2.5   | 250  | 0.9950          | 0.7114    | 0.7784 | 0.7434 | 0.7903   |
| 1.3831        | 5.0   | 500  | 0.5152          | 0.8483    | 0.8787 | 0.8632 | 0.8816   |
| 1.3831        | 7.5   | 750  | 0.3683          | 0.9013    | 0.9154 | 0.9083 | 0.9240   |
| 0.3551        | 10.0  | 1000 | 0.3051          | 0.9201    | 0.9304 | 0.9252 | 0.9363   |
| 0.3551        | 12.5  | 1250 | 0.2636          | 0.9375    | 0.9424 | 0.9399 | 0.9457   |
| 0.1562        | 15.0  | 1500 | 0.2498          | 0.9385    | 0.9476 | 0.9430 | 0.9508   |
| 0.1562        | 17.5  | 1750 | 0.2380          | 0.9414    | 0.9499 | 0.9456 | 0.9559   |
| 0.0863        | 20.0  | 2000 | 0.2355          | 0.9400    | 0.9491 | 0.9445 | 0.9542   |
| 0.0863        | 22.5  | 2250 | 0.2268          | 0.9451    | 0.9536 | 0.9493 | 0.9601   |
| 0.0512        | 25.0  | 2500 | 0.2277          | 0.9429    | 0.9513 | 0.9471 | 0.9588   |
| 0.0512        | 27.5  | 2750 | 0.2315          | 0.9473    | 0.9551 | 0.9512 | 0.9593   |
| 0.0358        | 30.0  | 3000 | 0.2294          | 0.9509    | 0.9573 | 0.9541 | 0.9605   |
| 0.0358        | 32.5  | 3250 | 0.2330          | 0.9458    | 0.9543 | 0.9501 | 0.9593   |
| 0.028         | 35.0  | 3500 | 0.2374          | 0.9487    | 0.9558 | 0.9523 | 0.9597   |
| 0.028         | 37.5  | 3750 | 0.2374          | 0.9501    | 0.9558 | 0.9530 | 0.9593   |
| 0.0244        | 40.0  | 4000 | 0.2339          | 0.9509    | 0.9573 | 0.9541 | 0.9610   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
