---
language: 
- multilingual
- en
- fr 
- es 
- de 
- el 
- bg 
- ru 
- tr 
- ar 
- vi 
- th 
- zh 
- hi 
- sw 
- ur
license: cc-by-nc-4.0
---

# xlm-mlm-xnli15-1024

#  Table of Contents

1. [Model Details](#model-details)
2. [Uses](#uses)
3. [Bias, Risks, and Limitations](#bias-risks-and-limitations)
4. [Training Details](#training-details)
5. [Evaluation](#evaluation)
6. [Environmental Impact](#environmental-impact)
7. [Technical Specifications](#technical-specifications)
8. [Citation](#citation)
9. [Model Card Authors](#model-card-authors)
10. [How To Get Started With the Model](#how-to-get-started-with-the-model)


# Model Details

The XLM model was proposed in [Cross-lingual Language Model Pretraining](https://arxiv.org/abs/1901.07291) by Guillaume Lample, Alexis Conneau. xlm-mlm-xnli15-1024 is a transformer pretrained using a masked language modeling (MLM) objective fine-tuned on the English NLI dataset. The model developers evaluated the capacity of the model to make correct predictions in all 15 XNLI languages (see the [XNLI data card](https://huggingface.co/datasets/xnli) for further information on XNLI).

## Model Description

- **Developed by:** Guillaume Lample, Alexis Conneau, see [associated paper](https://arxiv.org/abs/1901.07291)
- **Model type:** Language model
- **Language(s) (NLP):** English; evaluated in 15 languages (see [XNLI data card](https://huggingface.co/datasets/xnli))
- **License:** CC-BY-NC-4.0
- **Related Models:** [XLM models](https://huggingface.co/models?sort=downloads&search=xlm)
- **Resources for more information:** 
  - [Associated paper](https://arxiv.org/abs/1901.07291)
  - [GitHub Repo for XLM](https://github.com/facebookresearch/XLM)
  - [GitHub Repo for XNLI](https://github.com/facebookresearch/XNLI)
  - [XNLI data card](https://huggingface.co/datasets/xnli)
  - [Hugging Face Multilingual Models for Inference docs](https://huggingface.co/docs/transformers/v4.20.1/en/multilingual#xlm-with-language-embeddings)

# Uses

## Direct Use

The model is a language model. The model can be used for cross-lingual text classification. Though the model is fine-tuned based on English text data, the model's ability to classify sentences in 14 other languages has been evaluated (see [Evaluation](#evaluation)).

## Downstream Use

This model can be used for downstream tasks related to natural language inference in different languages. For more information, see the [associated paper](https://arxiv.org/abs/1901.07291).

## Out-of-Scope Use

The model should not be used to intentionally create hostile or alienating environments for people. 

# Bias, Risks, and Limitations

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).

## Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.

# Training Details

Training details are culled from the [associated paper](https://arxiv.org/pdf/1901.07291.pdf). See the paper for links, citations, and further details. Also see the associated [GitHub Repo](https://github.com/facebookresearch/XLM#ii-cross-lingual-language-model-pretraining-xlm) for further details.

## Training Data

The model developers write: 

> We use WikiExtractor2 to extract raw sentences from Wikipedia dumps and use them as mono-lingual data for the CLM and MLM objectives. For the TLM objective, we only use parallel data that involves English, similar to Conneau et al. (2018b). 
> - Precisely, we use MultiUN (Ziemski et al., 2016) for French, Spanish, Russian, Arabic and Chinese, and the IIT Bombay corpus (Anoop et al., 2018) for Hindi. 
> - We extract the following corpora from the OPUS 3 website Tiedemann (2012): the EUbookshop corpus for German, Greek and Bulgarian, OpenSubtitles 2018 for Turkish, Vietnamese and Thai, Tanzil for both Urdu and Swahili and GlobalVoices for Swahili. 
> - For Chinese, Japanese and Thai we use the tokenizer of Chang et al. (2008), the Kytea4 tokenizer, and the PyThaiNLP5 tokenizer respectively. 
> - For all other languages, we use the tokenizer provided by Moses (Koehn et al., 2007), falling back on the default English tokenizer when necessary.

For fine-tuning, the developers used the English NLI dataset (see the [XNLI data card](https://huggingface.co/datasets/xnli)).

## Training Procedure

### Preprocessing

The model developers write:

> We use fastBPE to learn BPE codes and split words into subword units. The BPE codes are learned on the concatenation of sentences sampled from all languages, following the method presented in Section 3.1.

### Speeds, Sizes, Times

The model developers write: 

> We use a Transformer architecture with 1024 hidden units, 8 heads, GELU activations (Hendrycks and Gimpel, 2016), a dropout rate of 0.1 and learned positional embeddings. We train our models with the Adam optimizer (Kingma and Ba, 2014), a linear warm-up (Vaswani et al., 2017) and learning rates varying from 10^−4 to 5.10^−4.
> 
> For the CLM and MLM objectives, we use streams of 256 tokens and a mini-batches of size 64. Unlike Devlin et al. (2018), a sequence in a mini-batch can contain more than two consecutive sentences, as explained in Section 3.2. For the TLM objective, we sample mini-batches of 4000 tokens composed of sentences with similar lengths. We use the averaged perplexity over languages as a stopping criterion for training. For machine translation, we only use 6 layers, and we create mini-batches of 2000 tokens.
> 
> When fine-tuning on XNLI, we use mini-batches of size 8 or 16, and we clip the sentence length to 256 words. We use 80k BPE splits and a vocabulary of 95k and train a 12-layer model on the Wikipedias of the XNLI languages. We sample the learning rate of the Adam optimizer with values from 5.10−4 to 2.10−4, and use small evaluation epochs of 20000 random samples. We use the first hidden state of the last layer of the transformer as input to the randomly initialized final linear classifier, and fine-tune all parameters. In our experiments, using either max-pooling or mean-pooling over the last layer did not work bet- ter than using the first hidden state.
>
> We implement all our models in Py-Torch (Paszke et al., 2017), and train them on 64 Volta GPUs for the language modeling tasks, and 8 GPUs for the MT tasks. We use float16 operations to speed up training and to reduce the memory usage of our models.
 
# Evaluation

## Testing Data, Factors & Metrics

After fine-tuning the model on the English NLI dataset, the model developers evaluated the capacity of the model to make correct predictions in the 15 XNLI languages using the XNLI data and the metric of test accuracy.See the [associated paper](https://arxiv.org/pdf/1901.07291.pdf) for further details.

## Results 

|Language| en | fr  | es | de | el | bg | ru  | tr | ar | vi | th | zh  | hi | sw | ur |
|:------:|:--:|:---:|:--:|:--:|:--:|:--:|:---:|:--:|:--:|:--:|:--:|:---:|:--:|:--:|:--:|
|Accuracy|83.2|76.5 |76.3|74.2|73.1|74.0|73.1 |67.8|68.5|71.2|69.2|71.9 |65.7|64.6|63.4|

# Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** 64 Volta GPUs
- **Hours used:** More information needed
- **Cloud Provider:** More information needed
- **Compute Region:** More information needed
- **Carbon Emitted:** More information needed

# Technical Specifications

Details are culled from the [associated paper](https://arxiv.org/pdf/1901.07291.pdf). See the paper for links, citations, and further details. Also see the associated [GitHub Repo](https://github.com/facebookresearch/XLM#ii-cross-lingual-language-model-pretraining-xlm) for further details.

## Model Architecture and Objective

xlm-mlm-xnli15-1024 is a transformer pretrained using a masked language modeling (MLM) objective fine-tuned on the English NLI dataset. About the MLM objective, the developers write: 

> We also consider the masked language model- ing (MLM) objective of Devlin et al. (2018), also known as the Cloze task (Taylor, 1953). Follow- ing Devlin et al. (2018), we sample randomly 15% of the BPE tokens from the text streams, replace them by a [MASK] token 80% of the time, by a random token 10% of the time, and we keep them unchanged 10% of the time. Differences be- tween our approach and the MLM of Devlin et al. (2018) include the use of text streams of an ar- bitrary number of sentences (truncated at 256 to- kens) instead of pairs of sentences. To counter the imbalance between rare and frequent tokens (e.g. punctuations or stop words), we also subsample the frequent outputs using an approach similar to Mikolov et al. (2013b): tokens in a text stream are sampled according to a multinomial distribution, whose weights are proportional to the square root of their invert frequencies. Our MLM objective is illustrated in Figure 1.

## Compute Infrastructure

### Hardware and Software

The developers write: 

> We implement all our models in PyTorch (Paszke et al., 2017), and train them on 64 Volta GPUs for the language modeling tasks, and 8 GPUs for the MT tasks. We use float16 operations to speed up training and to reduce the memory usage of our models.

# Citation

**BibTeX:**

```bibtex
@article{lample2019cross,
  title={Cross-lingual language model pretraining},
  author={Lample, Guillaume and Conneau, Alexis},
  journal={arXiv preprint arXiv:1901.07291},
  year={2019}
}
```

**APA:**
- Lample, G., & Conneau, A. (2019). Cross-lingual language model pretraining. arXiv preprint arXiv:1901.07291.

# Model Card Authors 

This model card was written by the team at Hugging Face.

# How to Get Started with the Model

This model uses language embeddings to specify the language used at inference. See the [Hugging Face Multilingual Models for Inference docs](https://huggingface.co/docs/transformers/v4.20.1/en/multilingual#xlm-with-language-embeddings) for further details.