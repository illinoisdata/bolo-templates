---
language: uk
tags:
 - gec
 - mbart-50
widget:
 - text: "я й не думав що комп'ютерна лінгвістика це легкоо."
---
This model was finetuned on errorful sentences from the `train` subset of [UA-GEC](https://github.com/grammarly/ua-gec) corpus, introduced in [UA-GEC: Grammatical Error Correction and Fluency Corpus for the Ukrainian Language](https://arxiv.org/abs/2103.16997) paper.

Only sentences containing errors were used; 8,874 sentences for training and 987 sentences for validation. The training arguments were defined as follows:
```
batch_size = 4
num_train_epochs = 3
learning_rate=5e-5
weight_decay=0.01
optim = "adamw_hf"
```