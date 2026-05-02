---
tags:
- translation

language:
- en
- ro

license: mit
---
### mbart-large-en-ro
This is mbart-large-cc25, finetuned on wmt_en_ro.

It scores BLEU 28.1 without post processing and BLEU 38 with postprocessing. Instructions in `romanian_postprocessing.md`

Original Code: https://github.com/pytorch/fairseq/tree/master/examples/mbart

Docs:  https://huggingface.co/transformers/master/model_doc/mbart.html

Finetuning Code: examples/seq2seq/finetune.py (as of Aug 20, 2020)