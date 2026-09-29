---
language:
- en
- ru
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

# Tiny FSMT en-ru

This is a tiny model that is used in the `transformers` test suite. It doesn't do anything useful, other than testing that `modeling_fsmt.py` is functional.

Do not try to use it for anything that requires quality.

The model is indeed 30KB in size.

You can see how it was created [here](https://huggingface.co/stas/tiny-wmt19-en-ru/blob/main/fsmt-make-super-tiny-model.py).

If you're looking for the real model, please go to [https://huggingface.co/facebook/wmt19-en-ru](https://huggingface.co/facebook/wmt19-en-ru).