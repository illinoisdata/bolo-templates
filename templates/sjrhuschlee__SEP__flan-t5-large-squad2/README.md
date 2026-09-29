---
language:
- en
license: mit
library_name: transformers
tags:
- question-answering
- squad
- squad_v2
- t5
- lora
- peft
datasets:
- squad_v2
- squad
base_model: google/flan-t5-large
model-index:
- name: sjrhuschlee/flan-t5-large-squad2
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
      value: 86.819
      name: Exact Match
    - type: f1
      value: 89.569
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
      value: 89.357
      name: Exact Match
    - type: f1
      value: 95.060
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
      value: 48.833
      name: Exact Match
    - type: f1
      value: 62.555
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
      value: 84.835
      name: Exact Match
    - type: f1
      value: 90.245
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
      value: 76.722
      name: Exact Match
    - type: f1
      value: 89.680
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
      value: 84.316
      name: Exact Match
    - type: f1
      value: 92.967
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
      value: 86.925
      name: Exact Match
    - type: f1
      value: 94.064
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
      value: 78.241
      name: Exact Match
    - type: f1
      value: 89.243
      name: F1
---

# flan-t5-large for Extractive QA

This is the [flan-t5-large](https://huggingface.co/google/flan-t5-large) model, fine-tuned using the [SQuAD2.0](https://huggingface.co/datasets/squad_v2) dataset. It's been trained on question-answer pairs, including unanswerable questions, for the task of Extractive Question Answering.

**UPDATE:** With transformers version 4.31.0 the `use_remote_code=True` is no longer necessary.

This model was trained using LoRA available through the [PEFT library](https://github.com/huggingface/peft).

**NOTE:** The `<cls>` token must be manually added to the beginning of the question for this model to work properly. It uses the `<cls>` token to be able to make "no answer" predictions. The t5 tokenizer does not automatically add this special token which is why it is added manually.

## Overview
**Language model:** flan-t5-large  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
**Infrastructure**: 1x NVIDIA 3070  

## Model Usage

### Using Transformers
This uses the merged weights (base model weights + LoRA weights) to allow for simple use in Transformers pipelines. It has the same performance as using the weights separately when using the PEFT library.
```python
import torch
from transformers import(
  AutoModelForQuestionAnswering,
  AutoTokenizer,
  pipeline
)
model_name = "sjrhuschlee/flan-t5-large-squad2"

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
# {'score': 0.984, 'start': 30, 'end': 37, 'answer': ' London'}

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
    "eval_HasAns_exact": 85.08771929824562,
    "eval_HasAns_f1": 90.598422845031,
    "eval_HasAns_total": 5928,
    "eval_NoAns_exact": 88.47771236333053,
    "eval_NoAns_f1": 88.47771236333053,
    "eval_NoAns_total": 5945,
    "eval_best_exact": 86.78514276088605,
    "eval_best_exact_thresh": 0.0,
    "eval_best_f1": 89.53654936623764,
    "eval_best_f1_thresh": 0.0,
    "eval_exact": 86.78514276088605,
    "eval_f1": 89.53654936623776,
    "eval_runtime": 1908.3189,
    "eval_samples": 12001,
    "eval_samples_per_second": 6.289,
    "eval_steps_per_second": 0.787,
    "eval_total": 11873
}

# Squad
{
    "eval_HasAns_exact": 85.99810785241249,
    "eval_HasAns_f1": 91.296119057944,
    "eval_HasAns_total": 10570,
    "eval_best_exact": 85.99810785241249,
    "eval_best_exact_thresh": 0.0,
    "eval_best_f1": 91.296119057944,
    "eval_best_f1_thresh": 0.0,
    "eval_exact": 85.99810785241249,
    "eval_f1": 91.296119057944,
    "eval_runtime": 1508.9596,
    "eval_samples": 10657,
    "eval_samples_per_second": 7.062,
    "eval_steps_per_second": 0.883,
    "eval_total": 10570
}
```

### Using with Peft
**NOTE**: This requires code in the PR https://github.com/huggingface/peft/pull/473 for the PEFT library.
```python
#!pip install peft

from peft import LoraConfig, PeftModelForQuestionAnswering
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
model_name = "sjrhuschlee/flan-t5-large-squad2"
```