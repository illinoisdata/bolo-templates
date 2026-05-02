---
language: ja
tags:
- t5
- text2text-generation
- seq2seq
license: apache-2.0
datasets:
- mc4
- wiki40b
---

# t5-base-japanese-web (with Byte-fallback, 32K)

## Description

[megagonlabs/t5-base-japanese-web](https://huggingface.co/megagonlabs/t5-base-japanese-web) is a T5 (Text-to-Text Transfer Transformer) model pre-trained on Japanese web texts.  
Training codes are [available on GitHub](https://github.com/megagonlabs/t5-japanese).

The vocabulary size of this model is 32K.
[8K version is also available](https://huggingface.co/megagonlabs/t5-base-japanese-web-8k).

### Corpora

We used following corpora for pre-training.

- Japanese in [mC4/3.0.1](https://huggingface.co/datasets/mc4) (We used [Tensorflow native format](https://github.com/allenai/allennlp/discussions/5056))
    - 87,425,304 pages
    - 782 GB in TFRecord format
- [Japanese](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bja) in [wiki40b/1.3.0](https://www.tensorflow.org/datasets/catalog/wiki40b)
    - 828,236 articles (2,073,584 examples)
    - 2 GB in TFRecord format

### Tokenizer

We used Japanese Wikipedia to train [SentencePiece](https://github.com/google/sentencepiece).

- Vocabulary size: 32,000
- [Byte-fallback](https://github.com/google/sentencepiece/releases/tag/v0.1.9): Enabled

### Parameters

- T5 model: [models/t5.1.1.base.gin](https://github.com/google-research/text-to-text-transfer-transformer/blob/main/t5/models/gin/models/t5.1.1.base.gin)
- Training steps: 1,000,000

It took about 126 hours with TPU v3-8

## Related models

- [日本語T5事前学習済みモデル (sonoisa/t5-base-japanese)](https://huggingface.co/sonoisa/t5-base-japanese)
- [日本語T5事前学習済みモデル (sonoisa/t5-base-japanese-mC4-Wikipedia)](https://huggingface.co/sonoisa/t5-base-japanese-mC4-Wikipedia)

## License

Apache License 2.0

## Citations

- mC4

Contains information from `mC4` which is made available under the [ODC Attribution License](https://opendatacommons.org/licenses/by/1-0/).

```bibtex
@article{2019t5,
    author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
    title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
    journal = {arXiv e-prints},
    year = {2019},
    archivePrefix = {arXiv},
    eprint = {1910.10683},
}
```

- wiki40b

```bibtex
@inproceedings{49029,
title = {Wiki-40B: Multilingual Language Model Dataset},
author = {Mandy Guo and Zihang Dai and Denny Vrandecic and Rami Al-Rfou},
year = {2020},
booktitle   = {LREC 2020}
}
```