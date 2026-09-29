---
datasets:
- PKU-Alignment/BeaverTails
language:
- en
tags:
- beaver
- safety
- llama
- ai-safety
- deepspeed
- rlhf
- alpaca
library_name: safe-rlhf
---

# 🦫 BeaverDam Model Card

## Beaver-Dam-7B

Boasting 7 billion parameters, Beaver-Dam-7B is a powerful QA-Moderation model derived from the Llama-7B base model and trained on the [PKU-Alignment/BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) Classification Dataset.
Beaver-Dam's key feature is its ability to analyze responses to prompts for toxicity across 14 different categories.

- **Developed by:** [PKU-Alignment Team](https://github.com/PKU-Alignment)
- **Model type:** QA moderation
- **License:** Non-commercial license
- **Finetuned from model:** [LLaMA](https://arxiv.org/abs/2302.13971)

## Model Sources

- **Repository:** https://github.com/PKU-Alignment/beavertails
- **Web:** https://sites.google.com/view/pku-beavertails
- **Paper:** Coming soon

## Why Choose Beaver-Dam-7B?

Traditional approaches to content moderation in Question-Answering (QA) tasks often gauge the toxicity of a QA pair by examining each utterance individually. This method, while effective to a degree, can inadvertently result in a significant number of user prompts being discarded. If the moderation system perceives them as too harmful, it may prevent the language model from generating appropriate responses, consequently interrupting the user experience and potentially hindering the evolution of a beneficial AI with human-like understanding.

BeaverDam is a shift in the approach to content moderation for QA tasks - a concept we term "QA moderation":

![qa-moderation-teaser.png](qa-moderation-teaser.png)

In this paradigm, a QA pair is classified as harmful or benign based on its degree of risk neutrality. Specifically, it assesses the extent to which potential risks in a potentially harmful question can be counteracted by a non-threatening response.