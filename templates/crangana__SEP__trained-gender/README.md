---
license: apache-2.0
base_model: microsoft/resnet-50
tags:
- generated_from_trainer
datasets:
- fair_face
metrics:
- accuracy
model-index:
- name: trained-gender
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: fair_face
      type: fair_face
      config: '0.25'
      split: validation
      args: '0.25'
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8985758626985576
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trained-gender

This model is a fine-tuned version of [microsoft/resnet-50](https://huggingface.co/microsoft/resnet-50) on the fair_face dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2437
- Accuracy: 0.8986

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.4277        | 0.18  | 1000  | 0.4054          | 0.8089   |
| 0.315         | 0.37  | 2000  | 0.3487          | 0.8318   |
| 0.3082        | 0.55  | 3000  | 0.3052          | 0.8633   |
| 0.3235        | 0.74  | 4000  | 0.2899          | 0.8684   |
| 0.2505        | 0.92  | 5000  | 0.2693          | 0.8785   |
| 0.2484        | 1.11  | 6000  | 0.2547          | 0.8889   |
| 0.1933        | 1.29  | 7000  | 0.2521          | 0.8901   |
| 0.1497        | 1.48  | 8000  | 0.2443          | 0.8929   |
| 0.326         | 1.66  | 9000  | 0.2406          | 0.8958   |
| 0.215         | 1.84  | 10000 | 0.2381          | 0.9007   |
| 0.2035        | 2.03  | 11000 | 0.2437          | 0.8986   |


### Framework versions

- Transformers 4.34.0
- Pytorch 2.0.1+cu118
- Datasets 2.14.5
- Tokenizers 0.14.0
