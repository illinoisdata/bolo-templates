---
language:
- multilingual
- en
- fr
- es
- de
- it
- pt
- nl
- sv
- pl
- ru
- ar
- tr
- zh
- ja
- ko
- hi
- vi
license: cc-by-nc-4.0
---

# xlm-mlm-17-1280

#  Table of Contents

1. [Model Details](#model-details)
2. [Uses](#uses)
3. [Bias, Risks, and Limitations](#bias-risks-and-limitations)
4. [Training](#training)
5. [Evaluation](#evaluation)
6. [Environmental Impact](#environmental-impact)
7. [Technical Specifications](#technical-specifications)
8. [Citation](#citation)
9. [Model Card Authors](#model-card-authors)
10. [How To Get Started With the Model](#how-to-get-started-with-the-model)


# Model Details

xlm-mlm-17-1280 is the XLM model, which was proposed in [Cross-lingual Language Model Pretraining](https://arxiv.org/abs/1901.07291) by Guillaume Lample and Alexis Conneau, trained on text in 17 languages. The model is a transformer pretrained using a masked language modeling (MLM) objective. 

## Model Description

- **Developed by:** See [associated paper](https://arxiv.org/abs/1901.07291) and [GitHub Repo](https://github.com/facebookresearch/XLM)
- **Model type:** Language model
- **Language(s) (NLP):** 17 languages, see [GitHub Repo](https://github.com/facebookresearch/XLM#the-17-and-100-languages) for full list.
- **License:** CC-BY-NC-4.0
- **Related Models:** [xlm-mlm-17-1280](https://huggingface.co/xlm-mlm-17-1280)
- **Resources for more information:** 
  - [Associated paper](https://arxiv.org/abs/1901.07291)
  - [GitHub Repo](https://github.com/facebookresearch/XLM#the-17-and-100-languages)
  - [Hugging Face Multilingual Models for Inference docs](https://huggingface.co/docs/transformers/v4.20.1/en/multilingual#xlm-with-language-embeddings)

# Uses

## Direct Use

The model is a language model. The model can be used for masked language modeling. 

## Downstream Use

To learn more about this task and potential downstream uses, see the Hugging Face [fill mask docs](https://huggingface.co/tasks/fill-mask) and the [Hugging Face Multilingual Models for Inference](https://huggingface.co/docs/transformers/v4.20.1/en/multilingual#xlm-with-language-embeddings) docs. Also see the [associated paper](https://arxiv.org/abs/1901.07291).

## Out-of-Scope Use

The model should not be used to intentionally create hostile or alienating environments for people. 

# Bias, Risks, and Limitations

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).

## Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.

# Training

This model is the XLM model trained on text in 17 languages. The preprocessing included tokenization and byte-pair-encoding. See the [GitHub repo](https://github.com/facebookresearch/XLM#the-17-and-100-languages) and the [associated paper](https://arxiv.org/pdf/1911.02116.pdf) for further details on the training data and training procedure.

[Conneau et al. (2020)](https://arxiv.org/pdf/1911.02116.pdf) report that this model has 16 layers, 1280 hidden states, 16 attention heads, and the dimension of the feed-forward layer is 1520. The vocabulary size is 200k and the total number of parameters is 570M (see Table 7).
 
# Evaluation

## Testing Data, Factors & Metrics

The model developers evaluated the model on the XNLI cross-lingual classification task (see the [XNLI data card](https://huggingface.co/datasets/xnli) for more details on XNLI) using the metric of test accuracy. See the [GitHub Repo](https://arxiv.org/pdf/1911.02116.pdf) for further details on the testing data, factors and metrics.

## Results

For xlm-mlm-17-1280, the test accuracy on the XNLI cross-lingual classification task in English (en), Spanish (es), German (de), Arabic (ar), and Chinese (zh):

|Language| en | es  | de | ar | zh |
|:------:|:--:|:---:|:--:|:--:|:--:|
|        |84.8|79.4 |76.2|71.5|75  |

See the [GitHub repo](https://github.com/facebookresearch/XLM#ii-cross-lingual-language-model-pretraining-xlm) for further details.

# Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** More information needed
- **Hours used:** More information needed
- **Cloud Provider:** More information needed
- **Compute Region:** More information needed
- **Carbon Emitted:** More information needed

# Technical Specifications

[Conneau et al. (2020)](https://arxiv.org/pdf/1911.02116.pdf) report that this model has 16 layers, 1280 hidden states, 16 attention heads, and the dimension of the feed-forward layer is 1520. The vocabulary size is 200k and the total number of parameters is 570M (see Table 7).

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

More information needed. See the [ipython notebook](https://github.com/facebookresearch/XLM/blob/main/generate-embeddings.ipynb) in the associated [GitHub repo](https://github.com/facebookresearch/XLM#the-17-and-100-languages) for examples.