---
base_model: MiMe-MeMo/MeMo-BERT-03
tags:
- generated_from_trainer
model-index:
- name: MeMo-BERT-WSD
  results: []
  language: da        # <-- my language
widget:
 - text: "Men havde Gud vendt sig fra ham , saa kunde han ogsaa vende sig fra Gud . Havde Gud ingen Øren , saa havde han heller ingen Læber , havde Gud ingen Naade , saa havde han heller ingen Tilbedelse , og han trodsede og viste Gud ud af sit Hjærte ."


---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MeMo-BERT-WSD

This model is a fine-tuned version of [MiMe-MeMo/MeMo-BERT-03](https://huggingface.co/MiMe-MeMo/MeMo-BERT-03) on https://huggingface.co/MiMe-MeMo/MeMo-Dataset-WSD dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1503
- F1-score: 0.5541

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1-score |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 61   | 1.3445          | 0.2569   |
| No log        | 2.0   | 122  | 1.0424          | 0.5124   |
| No log        | 3.0   | 183  | 1.1609          | 0.5304   |
| No log        | 4.0   | 244  | 1.3851          | 0.5389   |
| No log        | 5.0   | 305  | 1.9822          | 0.4456   |
| No log        | 6.0   | 366  | 2.0347          | 0.4914   |
| No log        | 7.0   | 427  | 2.9891          | 0.4419   |
| No log        | 8.0   | 488  | 2.5316          | 0.5183   |
| 0.4858        | 9.0   | 549  | 2.5900          | 0.5419   |
| 0.4858        | 10.0  | 610  | 2.9300          | 0.5051   |
| 0.4858        | 11.0  | 671  | 3.0018          | 0.5211   |
| 0.4858        | 12.0  | 732  | 3.0486          | 0.5109   |
| 0.4858        | 13.0  | 793  | 3.0887          | 0.5337   |
| 0.4858        | 14.0  | 854  | 3.1180          | 0.5441   |
| 0.4858        | 15.0  | 915  | 3.1503          | 0.5541   |
| 0.4858        | 16.0  | 976  | 3.1649          | 0.5436   |
| 0.0041        | 17.0  | 1037 | 3.1925          | 0.5436   |
| 0.0041        | 18.0  | 1098 | 3.2019          | 0.5436   |
| 0.0041        | 19.0  | 1159 | 3.2089          | 0.5436   |
| 0.0041        | 20.0  | 1220 | 3.2116          | 0.5436   |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
