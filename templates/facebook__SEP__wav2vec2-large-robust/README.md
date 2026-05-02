---
language: en
datasets:
- libri_light
- common_voice
- switchboard
- fisher
tags:
- speech
license: apache-2.0
---

# Wav2Vec2-Large-Robust

[Facebook's Wav2Vec2](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/)

The large model pretrained on 16kHz sampled speech audio. 
Speech datasets from multiple domains were used to pretrain the model:
- [Libri-Light](https://github.com/facebookresearch/libri-light): open-source audio books from the LibriVox project; clean, read-out audio data
- [CommonVoice](https://huggingface.co/datasets/common_voice): crowd-source collected audio data; read-out text snippets
- [Switchboard](https://catalog.ldc.upenn.edu/LDC97S62): telephone speech corpus; noisy telephone data
- [Fisher](https://catalog.ldc.upenn.edu/LDC2004T19): conversational telephone speech; noisy telephone data

When using the model make sure that your speech input is also sampled at 16Khz.

**Note**: This model does not have a tokenizer as it was pretrained on audio alone. In order to use this model **speech recognition**, a tokenizer should be created and the model should be fine-tuned on labeled text data. Check out [this blog](https://huggingface.co/blog/fine-tune-wav2vec2-english) for more in-detail explanation of how to fine-tune the model.

[Paper Robust Wav2Vec2](https://arxiv.org/abs/2104.01027)

Authors: Wei-Ning Hsu, Anuroop Sriram, Alexei Baevski, Tatiana Likhomanenko, Qiantong Xu, Vineel Pratap, Jacob Kahn, Ann Lee, Ronan Collobert, Gabriel Synnaeve, Michael Auli

**Abstract**
Self-supervised learning of speech representations has been a very active research area but most work is focused on a single domain such as read audio books for which there exist large quantities of labeled and unlabeled data. In this paper, we explore more general setups where the domain of the unlabeled data for pre-training data differs from the domain of the labeled data for fine-tuning, which in turn may differ from the test data domain. Our experiments show that using target domain data during pre-training leads to large performance improvements across a variety of setups. On a large-scale competitive setup, we show that pre-training on unlabeled in-domain data reduces the gap between models trained on in-domain and out-of-domain labeled data by 66%-73%. This has obvious practical implications since it is much easier to obtain unlabeled target domain data than labeled data. Moreover, we find that pre-training on multiple domains improves generalization performance on domains not seen during training. Code and models will be made available at this https URL.
The original model can be found under https://github.com/pytorch/fairseq/tree/master/examples/wav2vec#wav2vec-20.

# Usage

See [this notebook](https://colab.research.google.com/drive/1FjTsqbYKphl9kL-eILgUc-bl4zVThL8F?usp=sharing) for more information on how to fine-tune the model.