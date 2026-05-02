---
language:
- en
- de
thumbnail:
tags:
- wmt19
- testing
license: apache-2.0
datasets:
- wmt19
metrics:
- bleu
---

# Tiny FSMT en-de

This is a tiny model that is used in the `transformers` test suite. It doesn't do anything useful, other than testing that `modeling_fsmt.py` is functional.

Do not try to use it for anything that requires quality.

The model is indeed 1MB in size.

You can see how it was created [here](https://huggingface.co/stas/tiny-wmt19-en-de/blob/main/fsmt-make-tiny-model.py).


If you're looking for the real model, please go to [https://huggingface.co/facebook/wmt19-en-de](https://huggingface.co/facebook/wmt19-en-de).