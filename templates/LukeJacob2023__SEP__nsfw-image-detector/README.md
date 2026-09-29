---
license: apache-2.0
base_model: google/vit-base-patch16-224-in21k
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: nsfw-image-detector
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9315615772103526
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# nsfw-image-detector

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8138
- Accuracy: 0.9316
- Accuracy K: 0.9887

You can access 384 version on:

https://huggingface.co/LukeJacob2023/nsfw-image-detector-384

## Model description

Labels: ['drawings', 'hentai', 'neutral', 'porn', 'sexy']

## Intended uses & limitations

## Training and evaluation data

A custom dataset about 28k images, if you need to improve your domain's accurate, you can contribute the dataset to me.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Accuracy K |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:----------:|
| 0.7836        | 1.0   | 720  | 0.3188          | 0.9085   | 0.9891     |
| 0.2441        | 2.0   | 1440 | 0.2382          | 0.9257   | 0.9936     |
| 0.1412        | 3.0   | 2160 | 0.2334          | 0.9335   | 0.9932     |
| 0.0857        | 4.0   | 2880 | 0.2934          | 0.9347   | 0.9934     |
| 0.0569        | 5.0   | 3600 | 0.4500          | 0.9307   | 0.9927     |
| 0.0371        | 6.0   | 4320 | 0.5524          | 0.9357   | 0.9910     |
| 0.0232        | 7.0   | 5040 | 0.6691          | 0.9347   | 0.9913     |
| 0.02          | 8.0   | 5760 | 0.7408          | 0.9335   | 0.9917     |
| 0.0154        | 9.0   | 6480 | 0.8138          | 0.9316   | 0.9887     |


### Framework versions

- Transformers 4.36.2
- Pytorch 2.0.0
- Datasets 2.15.0
- Tokenizers 0.15.0
