---
language: 
- multilingual
- en 
- de
license: cc-by-nc-4.0
---

# xlm-mlm-ende-1024

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

The XLM model was proposed in [Cross-lingual Language Model Pretraining](https://arxiv.org/abs/1901.07291) by Guillaume Lample, Alexis Conneau. xlm-mlm-ende-1024 is a transformer pretrained using a masked language modeling (MLM) objective for English-German. This model uses language embeddings to specify the language used at inference. See the [Hugging Face Multilingual Models for Inference docs](https://huggingface.co/docs/transformers/v4.20.1/en/multilingual#xlm-with-language-embeddings) for further details.

## Model Description

- **Developed by:** Guillaume Lample, Alexis Conneau, see [associated paper](https://arxiv.org/abs/1901.07291)
- **Model type:** Language model
- **Language(s) (NLP):** English-German
- **License:** CC-BY-NC-4.0
- **Related Models:** [xlm-clm-enfr-1024](https://huggingface.co/xlm-clm-enfr-1024), [xlm-clm-ende-1024](https://huggingface.co/xlm-clm-ende-1024), [xlm-mlm-enfr-1024](https://huggingface.co/xlm-mlm-enfr-1024), [xlm-mlm-enro-1024](https://huggingface.co/xlm-mlm-enro-1024)
- **Resources for more information:** 
  - [Associated paper](https://arxiv.org/abs/1901.07291)
  - [GitHub Repo](https://github.com/facebookresearch/XLM)
  - [Hugging Face Multilingual Models for Inference docs](https://huggingface.co/docs/transformers/v4.20.1/en/multilingual#xlm-with-language-embeddings)

# Uses

## Direct Use

The model is a language model. The model can be used for masked language modeling. 

## Downstream Use

To learn more about this task and potential downstream uses, see the Hugging Face [fill mask docs](https://huggingface.co/tasks/fill-mask) and the [Hugging Face Multilingual Models for Inference](https://huggingface.co/docs/transformers/v4.20.1/en/multilingual#xlm-with-language-embeddings) docs.

## Out-of-Scope Use

The model should not be used to intentionally create hostile or alienating environments for people. 

# Bias, Risks, and Limitations

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).

## Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.

# Training

The model developers write: 

> In all experiments, we use a Transformer architecture with 1024 hidden units, 8 heads, GELU activations (Hendrycks and Gimpel, 2016), a dropout rate of 0.1 and learned positional embeddings. We train our models with the Adam op- timizer (Kingma and Ba, 2014), a linear warm- up (Vaswani et al., 2017) and learning rates varying from 10^−4 to 5.10^−4.

See the [associated paper](https://arxiv.org/pdf/1901.07291.pdf) for links, citations, and further details on the training data and training procedure.

The model developers also write that: 

> If you use these models, you should use the same data preprocessing / BPE codes to preprocess your data.

See the associated [GitHub Repo](https://github.com/facebookresearch/XLM#ii-cross-lingual-language-model-pretraining-xlm) for further details.
 
# Evaluation

## Testing Data, Factors & Metrics

The model developers evaluated the model on the [WMT'16 English-German](https://huggingface.co/datasets/wmt16) dataset using the [BLEU metric](https://huggingface.co/spaces/evaluate-metric/bleu). See the [associated paper](https://arxiv.org/pdf/1901.07291.pdf) for further details on the testing data, factors and metrics.

## Results 

For xlm-mlm-ende-1024 results, see Table 1 and Table 2 of the [associated paper](https://arxiv.org/pdf/1901.07291.pdf).

# Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** More information needed
- **Hours used:** More information needed
- **Cloud Provider:** More information needed
- **Compute Region:** More information needed
- **Carbon Emitted:** More information needed

# Technical Specifications

The model developers write: 

> We implement all our models in PyTorch (Paszke et al., 2017), and train them on 64 Volta GPUs for the language modeling tasks, and 8 GPUs for the MT tasks. We use float16 operations to speed up training and to reduce the memory usage of our models.

See the [associated paper](https://arxiv.org/pdf/1901.07291.pdf) for further details.

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

More information needed. This model uses language embeddings to specify the language used at inference. See the [Hugging Face Multilingual Models for Inference docs](https://huggingface.co/docs/transformers/v4.20.1/en/multilingual#xlm-with-language-embeddings) for further details.