---
language:
- ko
license: artistic-2.0
tags:
- generated_from_trainer
datasets:
- jsonl_dataset_sum.py
metrics:
- rouge
widget:
- text: 'summarization-num_lines-1: 현대자동차는 18일(현지 시간) 이탈리아 레이크 코모에서 개최된 ''현대 리유니온''
    행사에서 ''포니 쿠페 콘셉트'' 복원 모델을 세계에 첫 공개했습니다. 이 프로젝트는 현대차의 창업자인 정주영 선대 회장의 수출보국(輸出報國)
    정신과 포니 쿠페를 통한 글로벌 브랜드 정립에 대한 끊임없는 열정과 도전 정신을 재조명하기 위한 것입니다. 현대차에 따르면, 이번 현대 리유니온
    행사는 회사의 역사를 다시 돌아보며 변하지 않는 미래 지향적인 비전과 방향성을 공유하는 브랜드 유산 행사입니다.'
  example_title: sample 1
base_model: KETI-AIR/long-ke-t5-base
model-index:
- name: summarization_all
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: jsonl_dataset_sum.py
      type: jsonl_dataset_sum.py
      config: 'null'
      split: None
    metrics:
    - type: rouge
      value: 21.7197
      name: Rouge1
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# summarization_all

This model is a fine-tuned version of [KETI-AIR/long-ke-t5-base](https://huggingface.co/KETI-AIR/long-ke-t5-base) on the jsonl_dataset_sum.py dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0758
- Rouge1: 21.7197
- Rouge2: 10.1392
- Rougel: 21.1499
- Rougelsum: 21.173
- Gen Len: 87.4589

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 8
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:------:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.2171        | 1.0   | 184670 | 1.2070          | 20.611  | 9.2868  | 20.0833 | 20.1095   | 87.4065 |
| 1.0916        | 2.0   | 369340 | 1.1190          | 21.3264 | 9.8656  | 20.7683 | 20.8005   | 88.0284 |
| 0.9823        | 3.0   | 554010 | 1.0758          | 21.7197 | 10.1392 | 21.1499 | 21.173    | 87.4589 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.0
- Datasets 2.8.0
- Tokenizers 0.13.2