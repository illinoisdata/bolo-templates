---
license: apache-2.0
base_model: facebook/bart-large
tags:
- generated_from_trainer
model-index:
- name: tech-keyword-extractor
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tech-keyword-extractor

This model is a fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) on a private dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8795

## Model description

This model extracts tech terms, tools, company names from texts so they can easily be aggregated. It is trained to extract tech terms, tools, languages, platforms but may be used on other texts.

## Intended uses & limitations

Use to extract keywords from texts.

Example text: "If a task raises an exception, or a worker process dies, Celery will by default lose the job. So if you happen to reboot or redeploy, any running jobs with be lost to the sands of time."

Output: "Celery, Exception Handling, Worker Process"

Example text: "Spin 2.0 – open-source tool for building and running WebAssembly applications -"

Output: "Spin 2.0, WebAssembly, Open Source"

Example text: "Do you think that low-code and no-code is a threat for developers in the long term?"

Output: "Low Code, No Code, Developers"

Example text: "I'm reaching out for some guidance on choosing the right no-code or low-code platform for my web app development projects. As a proficient back-end developer with a strong grasp of AWS, I have always struggled with front-end development"

Output: "No Code, Low Code, Web App Development, AWS"

## Training and evaluation data

More information needed

## Training procedure


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.5095        | 0.44  | 50   | 1.1766          |
| 1.1875        | 0.89  | 100  | 0.9652          |
| 1.0428        | 1.33  | 150  | 1.0587          |
| 0.9392        | 1.78  | 200  | 0.8968          |
| 0.786         | 2.22  | 250  | 1.0131          |
| 0.8503        | 2.67  | 300  | 0.8795          |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0