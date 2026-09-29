---
tags:
- generated_from_trainer
model-index:
- name: security-bert256-50k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CTI-BERT

CTI-BERT is a pre-trained language model for the cybersecurity domain. 
The model was trained on a large corpus of security-related text data, comprising approximately 1.2 billion tokens sourced from
a diverse range of sources, including security news articles, vulnerability descriptions, books, academic publications, and security-related Wikipedia pages.

For additional technical details and the model's performance metrics, please refer to [this paper](https://aclanthology.org/2023.emnlp-industry.12.pdf).


## Model description

This model has a vocabulary of 50,000 tokens and the sequence length of 256.
Both the tokenizer and the BERT model were trained from scratch using the [run_mlm script](https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_mlm.py)
with the Masked language modeling (MLM) objective.


## Intended uses & limitations

You can use the model for masked language modeling or token embedding generation, but the model is aimed at being fine-tuned on a downstream task, such as 
sequence classification, text classification or question answering. 

The model has shown improved performance for various cybersecurity text classification. However, it is not designed to be used as the main model for general-domain text.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 2048
- optimizer: Adam with betas=(0.9,0.98) and epsilon=1e-06
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10000
- training_steps: 200000


### Framework versions

- Transformers 4.18.0
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1