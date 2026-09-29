---
license: mit
datasets:
- squad_v2
- squad
language:
- en
library_name: transformers
pipeline_tag: question-answering
tags:
- question-answering
- squad
- squad_v2
- t5
model-index:
- name: sjrhuschlee/flan-t5-base-squad2
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_v2
      type: squad_v2
      config: squad_v2
      split: validation
    metrics:
    - type: exact_match
      value: 82.203
      name: Exact Match
    - type: f1
      value: 85.283
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad
      type: squad
      config: plain_text
      split: validation
    metrics:
    - type: exact_match
      value: 86.367
      name: Exact Match
    - type: f1
      value: 92.965
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: adversarial_qa
      type: adversarial_qa
      config: adversarialQA
      split: validation
    metrics:
    - type: exact_match
      value: 34.167
      name: Exact Match
    - type: f1
      value: 46.911
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_adversarial
      type: squad_adversarial
      config: AddOneSent
      split: validation
    metrics:
    - type: exact_match
      value: 80.862
      name: Exact Match
    - type: f1
      value: 86.07
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts amazon
      type: squadshifts
      config: amazon
      split: test
    metrics:
    - type: exact_match
      value: 71.624
      name: Exact Match
    - type: f1
      value: 85.113
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts new_wiki
      type: squadshifts
      config: new_wiki
      split: test
    metrics:
    - type: exact_match
      value: 82.389
      name: Exact Match
    - type: f1
      value: 91.259
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts nyt
      type: squadshifts
      config: nyt
      split: test
    metrics:
    - type: exact_match
      value: 83.736
      name: Exact Match
    - type: f1
      value: 91.675
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts reddit
      type: squadshifts
      config: reddit
      split: test
    metrics:
    - type: exact_match
      value: 72.743
      name: Exact Match
    - type: f1
      value: 84.273
      name: F1
base_model:
- google/flan-t5-base
---

# flan-t5-base for Extractive QA

This is the [flan-t5-base](https://huggingface.co/google/flan-t5-base) model, fine-tuned using the [SQuAD2.0](https://huggingface.co/datasets/squad_v2) dataset. It's been trained on question-answer pairs, including unanswerable questions, for the task of Extractive Question Answering.

**UPDATE:** With transformers version 4.31.0 the `use_remote_code=True` is no longer necessary.

**NOTE:** The `<cls>` token must be manually added to the beginning of the question for this model to work properly.
It uses the `<cls>` token to be able to make "no answer" predictions.
The t5 tokenizer does not automatically add this special token which is why it is added manually.

## Overview
**Language model:** flan-t5-base  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
**Infrastructure**: 1x NVIDIA 3070  

## Model Usage
```python
import torch
from transformers import(
  AutoModelForQuestionAnswering,
  AutoTokenizer,
  pipeline
)
model_name = "sjrhuschlee/flan-t5-base-squad2"

# a) Using pipelines
nlp = pipeline(
  'question-answering',
  model=model_name,
  tokenizer=model_name,
  # trust_remote_code=True, # Do not use if version transformers>=4.31.0
)
qa_input = {
'question': f'{nlp.tokenizer.cls_token}Where do I live?',  # '<cls>Where do I live?'
'context': 'My name is Sarah and I live in London'
}
res = nlp(qa_input)
# {'score': 0.980, 'start': 30, 'end': 37, 'answer': ' London'}

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(
  model_name,
  # trust_remote_code=True # Do not use if version transformers>=4.31.0
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

question = f'{tokenizer.cls_token}Where do I live?'  # '<cls>Where do I live?'
context = 'My name is Sarah and I live in London'
encoding = tokenizer(question, context, return_tensors="pt")
output = model(
  encoding["input_ids"],
  attention_mask=encoding["attention_mask"]
)

all_tokens = tokenizer.convert_ids_to_tokens(encoding["input_ids"][0].tolist())
answer_tokens = all_tokens[torch.argmax(output["start_logits"]):torch.argmax(output["end_logits"]) + 1]
answer = tokenizer.decode(tokenizer.convert_tokens_to_ids(answer_tokens))
# 'London'
```

## Metrics

```bash
# Squad v2
{
    "eval_HasAns_exact": 79.97638326585695,
    "eval_HasAns_f1": 86.1444296592862,
    "eval_HasAns_total": 5928,
    "eval_NoAns_exact": 84.42388561816652,
    "eval_NoAns_f1": 84.42388561816652,
    "eval_NoAns_total": 5945,
    "eval_best_exact": 82.2033184536343,
    "eval_best_exact_thresh": 0.0,
    "eval_best_f1": 85.28292588395921,
    "eval_best_f1_thresh": 0.0,
    "eval_exact": 82.2033184536343,
    "eval_f1": 85.28292588395928,
    "eval_runtime": 522.0299,
    "eval_samples": 12001,
    "eval_samples_per_second": 22.989,
    "eval_steps_per_second": 0.96,
    "eval_total": 11873
}

# Squad
{
    "eval_exact_match": 86.3197729422895,
    "eval_f1": 92.94686836210295,
    "eval_runtime": 442.1088,
    "eval_samples": 10657,
    "eval_samples_per_second": 24.105,
    "eval_steps_per_second": 1.007
}
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 6
- total_train_batch_size: 96
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4.0

### Training results



### Framework versions

- Transformers 4.30.0.dev0
- Pytorch 2.0.1+cu117
- Datasets 2.12.0
- Tokenizers 0.13.3