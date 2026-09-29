---
language:
- en
license: apache-2.0
tags:
- relik
---

<div align="center">
  <img src="https://github.com/SapienzaNLP/relik/blob/main/relik.png?raw=true" height="150">
  <img src="https://github.com/SapienzaNLP/relik/blob/main/Sapienza_Babelscape.png?raw=true" height="50">
</div>

<div align="center">
  <h1>Retrieve, Read and LinK: Fast and Accurate Entity Linking and Relation Extraction on an Academic Budget</h1>
</div>

<div style="display:flex; justify-content: center; align-items: center; flex-direction: row;">
    <a href="https://2024.aclweb.org/"><img src="http://img.shields.io/badge/ACL-2024-4b44ce.svg"></a> &nbsp; &nbsp; 
    <a href="https://aclanthology.org/"><img src="http://img.shields.io/badge/paper-ACL--anthology-B31B1B.svg"></a> &nbsp; &nbsp; 
    <a href="https://arxiv.org/abs/2408.00103"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg"></a>
</div>
<div style="display:flex; justify-content: center; align-items: center; flex-direction: row;">
    <a href="https://huggingface.co/collections/sapienzanlp/relik-retrieve-read-and-link-665d9e4a5c3ecba98c1bef19"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Collection-FCD21D"></a> &nbsp; &nbsp;
    <a href="https://github.com/SapienzaNLP/relik"><img src="https://img.shields.io/badge/GitHub-Repo-121013?logo=github&logoColor=white"></a> &nbsp; &nbsp;
    <a href="https://github.com/SapienzaNLP/relik/releases"><img src="https://img.shields.io/github/v/release/SapienzaNLP/relik"></a>
</div>

This card is for a **Relation Extraction** model. The relation predictions are Wikidata properties.

A blazing fast and lightweight Information Extraction model for **Entity Linking** and **Relation Extraction**.

## 🛠️ Installation

Installation from PyPI

```bash
pip install relik
```

<details>
  <summary>Other installation options</summary>

#### Install with optional dependencies

Install with all the optional dependencies.

```bash
pip install relik[all]
```

Install with optional dependencies for training and evaluation.

```bash
pip install relik[train]
```

Install with optional dependencies for [FAISS](https://github.com/facebookresearch/faiss)

FAISS PyPI package is only available for CPU. For GPU, install it from source or use the conda package.

For CPU:

```bash
pip install relik[faiss]
```

For GPU:

```bash
conda create -n relik python=3.10
conda activate relik

# install pytorch
conda install -y pytorch=2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia

# GPU
conda install -y -c pytorch -c nvidia faiss-gpu=1.8.0
# or GPU with NVIDIA RAFT
conda install -y -c pytorch -c nvidia -c rapidsai -c conda-forge faiss-gpu-raft=1.8.0

pip install relik
```

Install with optional dependencies for serving the models with
[FastAPI](https://fastapi.tiangolo.com/) and [Ray](https://docs.ray.io/en/latest/serve/quickstart.html).

```bash
pip install relik[serve]
```

#### Installation from source

```bash
git clone https://github.com/SapienzaNLP/relik.git
cd relik
pip install -e .[all]
```

</details>

## 🚀 Quick Start

[//]: # (Write a short description of the model and how to use it with the `from_pretrained` method.)

ReLiK is a lightweight and fast model for **Entity Linking** and **Relation Extraction**.
It is composed of two main components: a retriever and a reader.
The retriever is responsible for retrieving relevant documents from a large collection,
while the reader is responsible for extracting entities and relations from the retrieved documents.
ReLiK can be used with the `from_pretrained` method to load a pre-trained pipeline.

Here is an example of how to use ReLiK for **Entity Linking**:

```python
from relik import Relik
from relik.inference.data.objects import RelikOutput

relik = Relik.from_pretrained("sapienzanlp/relik-entity-linking-large")
relik_out: RelikOutput = relik("Michael Jordan was one of the best players in the NBA.")
```

    RelikOutput(
      text="Michael Jordan was one of the best players in the NBA.",
      tokens=['Michael', 'Jordan', 'was', 'one', 'of', 'the', 'best', 'players', 'in', 'the', 'NBA', '.'],
      id=0,
      spans=[
          Span(start=0, end=14, label="Michael Jordan", text="Michael Jordan"),
          Span(start=50, end=53, label="National Basketball Association", text="NBA"),
      ],
      triples=[],
      candidates=Candidates(
          span=[
              [
                  [
                      {"text": "Michael Jordan", "id": 4484083},
                      {"text": "National Basketball Association", "id": 5209815},
                      {"text": "Walter Jordan", "id": 2340190},
                      {"text": "Jordan", "id": 3486773},
                      {"text": "50 Greatest Players in NBA History", "id": 1742909},
                      ...
                  ]
              ]
          ]
      ),
    )

## 📊 Performance

We evaluate the performance of ReLiK on Entity Linking using [GERBIL](http://gerbil-qa.aksw.org/gerbil/). The following table shows the results (InKB Micro F1) of ReLiK Large and Base:

| Model                                    | AIDA | MSNBC | Der  | K50  | R128 | R500 | O15  | O16  | Tot  | OOD  | AIT (m:s) |
|------------------------------------------|------|-------|------|------|------|------|------|------|------|------|------------|
| GENRE                                    | 83.7 | 73.7  | 54.1 | 60.7 | 46.7 | 40.3 | 56.1 | 50.0 | 58.2 | 54.5 | 38:00      |
| EntQA                                    | 85.8 | 72.1  | 52.9 | 64.5 | **54.1** | 41.9 | 61.1 | 51.3 | 60.5 | 56.4 | 20:00      |
| [ReLiK<sub>Base<sub>](https://huggingface.co/sapienzanlp/relik-entity-linking-base)                      | 85.3 | 72.3  | 55.6 | 68.0 | 48.1 | 41.6 | 62.5 | 52.3 | 60.7 | 57.2 | 00:29      |
| ➡️ [ReLiK<sub>Large<sub>](https://huggingface.co/sapienzanlp/relik-entity-linking-large)                     | **86.4** | **75.0**  | **56.3** | **72.8** | 51.7 | **43.0** | **65.1** | **57.2** | **63.4** | **60.2** | 01:46      |

Comparison systems' evaluation (InKB Micro F1) on the *in-domain* AIDA test set and *out-of-domain* MSNBC (MSN), Derczynski (Der), KORE50 (K50), N3-Reuters-128 (R128), 
N3-RSS-500 (R500), OKE-15 (O15), and OKE-16 (O16) test sets. **Bold** indicates the best model. 
GENRE uses mention dictionaries. 
The AIT column shows the time in minutes and seconds (m:s) that the systems need to process the whole AIDA test set using an NVIDIA RTX 4090, 
except for EntQA which does not fit in 24GB of RAM and for which an A100 is used.

## 🤖 Models

Models can be found on [🤗 Hugging Face](https://huggingface.co/collections/sapienzanlp/relik-retrieve-read-and-link-665d9e4a5c3ecba98c1bef19).

## 💽 Cite this work

If you use any part of this work, please consider citing the paper as follows:

```bibtex
@inproceedings{orlando-etal-2024-relik,
    title     = "Retrieve, Read and LinK: Fast and Accurate Entity Linking and Relation Extraction on an Academic Budget",
    author    = "Orlando, Riccardo and Huguet Cabot, Pere-Llu{\'\i}s and Barba, Edoardo and Navigli, Roberto",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2024",
    month     = aug,
    year      = "2024",
    address   = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
}
```