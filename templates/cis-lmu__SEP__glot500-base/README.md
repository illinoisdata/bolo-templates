---
license: apache-2.0
language:
- multilingual
datasets:
- cis-lmu/Glot500
metrics:
- accuracy
- f1
- perplexity
library_name: transformers
pipeline_tag: fill-mask
---

# Glot500 (base-sized model) 

Glot500 model (Glot500-m) pre-trained on 500+ languages using a masked language modeling (MLM) objective. It was introduced in
[this paper](https://arxiv.org/pdf/2305.12182.pdf) (ACL 2023) and first released in [this repository](https://github.com/cisnlp/Glot500).


## Usage

You can use this model directly with a pipeline for masked language modeling:

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='cis-lmu/glot500-base')
>>> unmasker("Hello I'm a <mask> model.")
```


Here is how to use this model to get the features of a given text in PyTorch:

```python
>>> from transformers import AutoTokenizer, AutoModelForMaskedLM

>>> tokenizer = AutoTokenizer.from_pretrained('cis-lmu/glot500-base')
>>> model = AutoModelForMaskedLM.from_pretrained("cis-lmu/glot500-base")

>>> # prepare input
>>> text = "Replace me by any text you'd like."
>>> encoded_input = tokenizer(text, return_tensors='pt')

>>> # forward pass
>>> output = model(**encoded_input)
```

### BibTeX entry and citation info

```bibtex
@article{imanigooghari-etal-2023-glot500,
  title={Glot500: Scaling Multilingual Corpora and Language Models to 500 Languages},
  author={ImaniGooghari, Ayyoob  and Lin, Peiqin  and Kargaran, Amir Hossein  and Severini, Silvia  and Jalili Sabet, Masoud  and Kassner, Nora  and Ma, Chunlan  and Schmid, Helmut  and Martins, Andr{\'e}  and Yvon, Fran{\c{c}}ois  and Sch{\"u}tze, Hinrich},
  journal={arXiv preprint arXiv:2305.12182},
  year={2023}
}
```

<!---

```bibtex
@inproceedings{imanigooghari-etal-2023-glot500,
	title        = {Glot500: Scaling Multilingual Corpora and Language Models to 500 Languages},
	author       = {ImaniGooghari, Ayyoob  and Lin, Peiqin  and Kargaran, Amir Hossein  and Severini, Silvia  and Jalili Sabet, Masoud  and Kassner, Nora  and Ma, Chunlan  and Schmid, Helmut  and Martins, Andr{\'e}  and Yvon, Fran{\c{c}}ois  and Sch{\"u}tze, Hinrich},
	year         = 2023,
	month        = jul,
	booktitle    = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
	publisher    = {Association for Computational Linguistics},
	address      = {Toronto, Canada},
	pages        = {1082--1117},
	url          = {https://aclanthology.org/2023.acl-long.61}
}
```
-->