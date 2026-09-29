---
license: apache-2.0
datasets:
- gair-prox/RedPajama-pro
language:
- en
base_model:
- gair-prox/RedPJ-ProX-0.3B
pipeline_tag: text-generation
library_name: transformers
tags:
- llama
- code
---

# Web-doc-refining-lm

<p align="center">
  <img src="prox-teaser.png">
</p>

[ArXiv](http://arxiv.org/abs/2409.17115) | [Code](https://github.com/GAIR-NLP/program-every-example)

**Web-doc-refining-lm** is an adapted [0.3B-ProX](https://huggingface.co/gair-prox/RedPJ-ProX-0.3B) model, fine-tuned for document level refining via program generation.

<p align="center">
  <img src="func_design.png">
</p>

### Citation
```
@article{zhou2024programming,
  title={Programming Every Example: Lifting Pre-training Data Quality like Experts at Scale},
  author={Zhou, Fan and Wang, Zengzhi and Liu, Qian and Li, Junlong and Liu, Pengfei},
  journal={arXiv preprint arXiv:2409.17115},
  year={2024}
}
```