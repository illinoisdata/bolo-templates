---
language:
- en
datasets:
- Spotify Podcasts Dataset
tags:
- t5
- summarisation
- pytorch
- lm-head
metrics:
- ROUGE
pipeline:
- summarisation
---

# T5 for Automatic Podcast Summarisation

This model is the result of fine-tuning [t5-base](https://huggingface.co/t5-base) on the [Spotify Podcast Dataset](https://arxiv.org/abs/2004.04270).

It is based on [Google's T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) which was pretrained on the [C4 dataset](https://huggingface.co/datasets/c4).


Paper: [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf)

Authors: Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu

## Intended uses & limitations
This model is intended to be used for automatic podcast summarisation. As creator provided descriptions
were used for training, the model also learned to generate promotional material (links, hashtags, etc) in its summaries, as such
some post processing may be required on the model's outputs.

If using on Colab, the instance will crash if the number of tokens in the transcript exceeds 7000. I discovered that the model
generated reasonable summaries even when the podcast transcript was truncated to reduce the number of tokens.

#### How to use

The model can be used with the summarisation as follows:

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="paulowoicho/t5-podcast-summarisation", tokenizer="paulowoicho/t5-podcast-summarisation")
summary = summarizer(podcast_transcript, min_length=5, max_length=20)

print(summary[0]['summary_text'])
```

## Training data

This model is the result of fine-tuning [t5-base](https://huggingface.co/t5-base) on the [Spotify Podcast Dataset](https://arxiv.org/abs/2004.04270).
[Pre-processing](https://github.com/paulowoicho/msc_project/blob/master/reformat.py) was done on the original data before fine-tuning.

## Training procedure

Training was largely based on [Fine-tune T5 for Summarization](https://github.com/abhimishra91/transformers-tutorials/blob/master/transformers_summarization_wandb.ipynb) by [Abhishek Kumar Mishra](https://github.com/abhimishra91)