---
language: 
  - ja
thumbnail: "https://raw.githubusercontent.com/megagonlabs/ginza/static/docs/images/GiNZA_logo_4c_s.png"
tags:
- PyTorch
- Transformers
- spaCy
- ELECTRA
- GiNZA
- mC4
- UD_Japanese-BCCWJ
- GSK2014-A
- ja
- MIT
license: "mit"
datasets:
- mC4
- UD_Japanese_BCCWJ r2.8
- GSK2014-A(2019)
metrics:
- UAS
- LAS
- UPOS
---

# transformers-ud-japanese-electra-ginza-510 (sudachitra-wordpiece, mC4 Japanese)

This is an [ELECTRA](https://github.com/google-research/electra) model pretrained on approximately 200M Japanese sentences extracted from the [mC4](https://huggingface.co/datasets/mc4) and finetuned by [spaCy v3](https://spacy.io/usage/v3) on [UD\_Japanese\_BCCWJ r2.8](https://universaldependencies.org/treebanks/ja_bccwj/index.html).

The base pretrain model is [megagonlabs/transformers-ud-japanese-electra-base-discrimininator](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-discriminator).

The entire spaCy v3 model is distributed as a python package named [`ja_ginza_electra`](https://pypi.org/project/ja-ginza-electra/) from PyPI along with [`GiNZA v5`](https://github.com/megagonlabs/ginza) which provides some custom pipeline components to recognize the Japanese bunsetu-phrase structures.
Try running it as below:
```console
$ pip install ginza ja_ginza_electra
$ ginza
```

## Licenses

The models are distributed under the terms of the [MIT License](https://opensource.org/licenses/mit-license.php).

## Acknowledgments

This model is permitted to be published under the `MIT License` under a joint research agreement between NINJAL (National Institute for Japanese Language and Linguistics) and Megagon Labs Tokyo.

## Citations
- [mC4](https://huggingface.co/datasets/mc4)

Contains information from `mC4` which is made available under the [ODC Attribution License](https://opendatacommons.org/licenses/by/1-0/).
```
@article{2019t5,
    author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
    title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
    journal = {arXiv e-prints},
    year = {2019},
    archivePrefix = {arXiv},
    eprint = {1910.10683},
}
```

- [UD\_Japanese\_BCCWJ r2.8](https://universaldependencies.org/treebanks/ja_bccwj/index.html)

```
Asahara, M., Kanayama, H., Tanaka, T., Miyao, Y., Uematsu, S., Mori, S.,
Matsumoto, Y., Omura, M., & Murawaki, Y. (2018).
Universal Dependencies Version 2 for Japanese.
In LREC-2018.
```

- [GSK2014-A(2019)](https://www.gsk.or.jp/catalog/gsk2014-a/)
