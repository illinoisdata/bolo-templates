---
license: apache-2.0
tags:
- qa
datasets:
- squad_v2
- natural_questions
model-index:
- name: nlpconnect/roberta-base-squad2-nq
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
      value: 80.3185
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTlmNTE0N2U3MTA1MDY1ZGZjYTYxZGIwMWUwN2EzYWM1MzhhZDI2Y2FiZDcxYTk1YTkyYzcxNGViYTM4MTUxNCIsInZlcnNpb24iOjF9.QOTfyyo4ttC1iCceQM7fYeJG9u976t1rG8RM-UxTIORP_rJHgdoYymjpTd4aghwkxg6hn3jeSKqpR5qV__0MAg
    - type: f1
      value: 83.4669
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjg5NjgwZjVmNDZlYjYyOTlhZjgxNGJjYmMyMDUzZjQ1YTdhOWExZjVjMmE2YmJlMGUyZTQ5MzE3ZTUxMjY0ZCIsInZlcnNpb24iOjF9.qQ4U9ZwpqJeeU2lEWQ2bN_Ktq0kJbGEKjOq9liFy0_7EpTtYSc9Qzr64sJOO40fJ08Twe2At3weuz6aPgBQIDA
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
      value: 85.5666
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmQzMzQzOTUwNjcwN2NjOGMwNDRiZmEwZTA4OGNhZGIzZjUzNmM5MzEzYWRmOTQwMzlhNDY3ZDllYWQ3Y2ZlYSIsInZlcnNpb24iOjF9.3t6pbSduzMYHZisQWgacYssbu3ver3Xmn9hIaRO-SlRw8qsBlE5z4xM8yo5fLluZy-o_mZ6Z5l31XWpGxcNvBw
    - type: f1
      value: 92.1939
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjEzZGYxODU4YWNlZmM5ZDE5ODBhZWUyMmZlN2I3MDNlMTlkYTU1M2ZiNjMwY2QyYzM4YWZiOGIzZGMzODcwZSIsInZlcnNpb24iOjF9.5wQliHDlVaZK_dIOcJYGKCo-DPtPcmpSlaf2E4EuQJcW23rNN2gci8_h_RS0ay-6m1MF-7BgsIeivlMDZgSKBQ
---

# Roberta-base-Squad2-NQ

## What is SQuAD?
Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

SQuAD2.0 combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers to look similar to answerable ones. To do well on SQuAD2.0, systems must not only answer questions when possible, but also determine when no answer is supported by the paragraph and abstain from answering.

## The Natural Questions Dataset
To help spur development in open-domain question answering, we have created the Natural Questions (NQ) corpus, along with a challenge website based on this data. The NQ corpus contains questions from real users, and it requires QA systems to read and comprehend an entire Wikipedia article that may or may not contain the answer to the question. The inclusion of real user questions, and the requirement that solutions should read an entire page to find the answer, cause NQ to be a more realistic and challenging task than prior QA datasets.

## Training

Firstly, we took base roberta model and trained on SQuQD 2.0 dataset for 2 epoch and then after we took NQ Small answer and trained for 1 epoch.

Total Dataset Size: 204416 Examples from squadv2 and NQ Small answer dataset

## Evaluation

Eval Dataset: Squadv2 dev

```
  {'exact': 80.2998399730481,
   'f1': 83.4402145786235,
   'total': 11873,
   'HasAns_exact': 79.08232118758434,
   'HasAns_f1': 85.37207619635592,
   'HasAns_total': 5928,
   'NoAns_exact': 81.5138772077376,
   'NoAns_f1': 81.5138772077376,
   'NoAns_total': 5945,
   'best_exact': 80.2998399730481,
   'best_exact_thresh': 0.0,
   'best_f1': 83.44021457862335,
   'best_f1_thresh': 0.0}
 ```