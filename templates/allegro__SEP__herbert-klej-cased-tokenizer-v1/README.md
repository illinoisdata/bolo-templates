---
language: pl
---

# HerBERT tokenizer

**[HerBERT](https://en.wikipedia.org/wiki/Zbigniew_Herbert)** tokenizer is a character level byte-pair encoding with
vocabulary size of 50k tokens. The tokenizer was trained on [Wolne Lektury](https://wolnelektury.pl/) and a publicly available subset of
[National Corpus of Polish](http://nkjp.pl/index.php?page=14&lang=0) with [fastBPE](https://github.com/glample/fastBPE) library.
Tokenizer utilize `XLMTokenizer` implementation from [transformers](https://github.com/huggingface/transformers).

## Tokenizer usage
Herbert tokenizer should be used together with [HerBERT model](https://huggingface.co/allegro/herbert-klej-cased-v1):
```python
from transformers import XLMTokenizer, RobertaModel

tokenizer = XLMTokenizer.from_pretrained("allegro/herbert-klej-cased-tokenizer-v1")
model = RobertaModel.from_pretrained("allegro/herbert-klej-cased-v1")

encoded_input = tokenizer.encode("Kto ma lepszą sztukę, ma lepszy rząd – to jasne.", return_tensors='pt')
outputs = model(encoded_input)
```

## License
CC BY-SA 4.0

## Citation
If you use this tokenizer, please cite the following paper:
```
@inproceedings{rybak-etal-2020-klej,
    title = "{KLEJ}: Comprehensive Benchmark for {P}olish Language Understanding",
    author = "Rybak, Piotr  and
      Mroczkowski, Robert  and
      Tracz, Janusz  and
      Gawlik, Ireneusz",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.111",
    doi = "10.18653/v1/2020.acl-main.111",
    pages = "1191--1201",
}
```

## Authors
Tokenizer was created by **Allegro Machine Learning Research** team.

You can contact us at: <a href="mailto:klejbenchmark@allegro.pl">klejbenchmark@allegro.pl</a>