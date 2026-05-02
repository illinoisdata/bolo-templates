---
language: en
license: cc-by-4.0
pipeline_tag: summarization
widget:
- text: "Example question body."
---

# Titlewave: t5-base

## Model description

Titlewave is a Chrome extension that helps you choose better titles for your Stack Overflow questions. See https://github.com/tennessejoyce/TitleWave for more information.
This is one of two NLP models used in the Titlewave project, and its purpose is to suggests a new title based on on the body of the question. The companion model (https://huggingface.co/tennessejoyce/titlewave-bert-base-uncased) classifies whether question will be answered or not just based on the title

## Intended use

Try out different titles for your Stack Overflow post, and see which one gives you the best chance of recieving an answer.
This model can be used in your browser as a Chrome extension by following the installation instructions at https://github.com/tennessejoyce/TitleWave.
Or load it in Python like this (which will automatically download the model to your machine):

```python
>>> from transformers import pipeline
>>> classifier = pipeline('summarization', model='tennessejoyce/titlewave-t5-base')
>>> body = """"Example question body."""
>>> classifier(body)

[{'summary_text': 'Example title suggestion?'}]
```


## Training data

The weights were initialized from the BERT base model (https://huggingface.co/bert-base-uncased), which was trained on BookCorpus and English Wikipedia.
Then the model was fine-tuned on the dataset of previous Stack Overflow post titles (https://archive.org/details/stackexchange).
Specifically I used three years of posts from 2017-2019, filtered out posts which were closed, and selected 25% of the remaining posts at random to use in
the training set. In order to improve the quality of the titles generated, the model was trained only on questions with an accepted answer.

## Evaluation

See https://github.com/tennessejoyce/TitleWave/blob/master/model_training/test_summarizer.ipynb for the performance of the title generation model on the test set.