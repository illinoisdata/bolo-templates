---
datasets:
- squad_v2
model_index:
- name: sapbert-from-pubmedbert-squad2
  results:
  - task:
      name: Question Answering
      type: question-answering
    dataset:
      name: squad_v2
      type: squad_v2
      args: squad_v2
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sapbert-from-pubmedbert-squad2

This model is a fine-tuned version of [cambridgeltl/SapBERT-from-PubMedBERT-fulltext](https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext) on the squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2582

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.035         | 1.0   | 8298  | 0.9545          |
| 0.8053        | 2.0   | 16596 | 0.9988          |
| 0.5949        | 3.0   | 24894 | 0.9909          |
| 0.4878        | 4.0   | 33192 | 1.1428          |
| 0.3932        | 5.0   | 41490 | 1.2582          |


### Framework versions

- Transformers 4.7.0
- Pytorch 1.8.0
- Datasets 1.4.1
- Tokenizers 0.10.2