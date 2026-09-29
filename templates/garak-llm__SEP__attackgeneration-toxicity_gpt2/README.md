---
language:
- en
base_model: openai-community/gpt2
license: apache-2.0
datasets:
- Anthropic/hh-rlhf
- google/jigsaw_unintended_bias
tags:
- not-for-all-audiences
---

**This adversarial model has a propensity to produce highly unsavoury content from the outset.
It is not intended or suitable for general use or human consumption.**

This special-use model aims to provide prompts that goad LLMs into producting "toxicity".
Toxicity here is defined by the content of the [Civil Comments](https://medium.com/@aja_15265/saying-goodbye-to-civil-comments-41859d3a2b1d) dataset, containing
categories such as `obscene`, `threat`, `insult`, `identity_attack`, `sexual_explicit` and 
`severe_toxicity`. For details, see the description of the [Jigsaw 2019 data](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data).

The base model is the [community version of gpt2](https://huggingface.co/openai-community/gpt2) with ~125M parameters. 
This model is not aligned and is "noisy" relative to more advanced models. 
Both the lack of alignment and the existence of noise are favourable to the task of 
trying to goad other models into producing unsafe output: unsafe prompts have a 
propensity to yield unsafe outputs, and noisy behaviour can lead to a broader
exploration of input space.

The model is fine-tuned to emulate the responses of humans in conversation 
exchanges that led to LLMs producing toxicity. 
These prompt-response pairs are taken from the Anthropic HHRLHF corpus ([paper](https://arxiv.org/abs/2204.05862), [data](https://github.com/anthropics/hh-rlhf)), 
filtered to those exchanges in which the model produced "toxicity" as defined above,
using the [martin-ha/toxic-comment-model](https://huggingface.co/martin-ha/toxic-comment-model) DistilBERT classifier based on that data.

See https://interhumanagreement.substack.com/p/faketoxicityprompts-automatic-red for details on the training process.