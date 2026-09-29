---
language: tr
license: mit
datasets:
- allenai/c4
---

# 🇹🇷 Turkish ConvBERT model

<p align="center">
  <img alt="Logo provided by Merve Noyan" title="Awesome logo from Merve Noyan" src="https://raw.githubusercontent.com/stefan-it/turkish-bert/master/merve_logo.png">
</p>

[![DOI](https://zenodo.org/badge/237817454.svg)](https://zenodo.org/badge/latestdoi/237817454)

We present community-driven BERT, DistilBERT, ELECTRA and ConvBERT models for Turkish 🎉

Some datasets used for pretraining and evaluation are contributed from the
awesome Turkish NLP community, as well as the decision for the BERT model name: BERTurk.

Logo is provided by [Merve Noyan](https://twitter.com/mervenoyann).

# Stats

We've trained an (uncased) ConvBERT model on the recently released Turkish part of the
[multiligual C4 (mC4) corpus](https://github.com/allenai/allennlp/discussions/5265) from the AI2 team.

After filtering documents with a broken encoding, the training corpus has a size of 242GB resulting
in 31,240,963,926 tokens.

We used the original 32k vocab (instead of creating a new one).

# mC4 ConvBERT

In addition to the ELEC**TR**A base model, we also trained an ConvBERT model on the Turkish part of the mC4 corpus. We use a
sequence length of 512 over the full training time and train the model for 1M steps on a v3-32 TPU.

# Model usage

All trained models can be used from the [DBMDZ](https://github.com/dbmdz) Hugging Face [model hub page](https://huggingface.co/dbmdz)
using their model name.

Example usage with 🤗/Transformers:

```python
tokenizer = AutoTokenizer.from_pretrained("dbmdz/convbert-base-turkish-mc4-uncased")

model = AutoModel.from_pretrained("dbmdz/convbert-base-turkish-mc4-uncased")
```

# Citation

You can use the following BibTeX entry for citation:

```bibtex
@software{stefan_schweter_2020_3770924,
  author       = {Stefan Schweter},
  title        = {BERTurk - BERT models for Turkish},
  month        = apr,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.3770924},
  url          = {https://doi.org/10.5281/zenodo.3770924}
}
```

# Acknowledgments

Thanks to [Kemal Oflazer](http://www.andrew.cmu.edu/user/ko/) for providing us
additional large corpora for Turkish. Many thanks to Reyyan Yeniterzi for providing
us the Turkish NER dataset for evaluation.

We would like to thank [Merve Noyan](https://twitter.com/mervenoyann) for the
awesome logo!

Research supported with Cloud TPUs from Google's TensorFlow Research Cloud (TFRC).
Thanks for providing access to the TFRC ❤️