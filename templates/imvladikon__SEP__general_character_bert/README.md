---
language: 
  - en
tags:
- language model
datasets:
- wikipedia
- openwebtext
---

Pretrained general_character_bert model 
from the ['CharacterBERT: Reconciling ELMo and BERT for Word-Level Open-Vocabulary Representations From Characters' El Boukkouri H., et al., 2020](https://github.com/helboukkouri/character-bert)


```
@inproceedings{el-boukkouri-etal-2020-characterbert,
    title = "{C}haracter{BERT}: Reconciling {ELM}o and {BERT} for Word-Level Open-Vocabulary Representations From Characters",
    author = "El Boukkouri, Hicham  and
      Ferret, Olivier  and
      Lavergne, Thomas  and
      Noji, Hiroshi  and
      Zweigenbaum, Pierre  and
      Tsujii, Jun{'}ichi",
    booktitle = "Proceedings of the 28th International Conference on Computational Linguistics",
    month = dec,
    year={2020},
    eprint={2010.10392},
    archivePrefix={arXiv},
    address = "Barcelona, Spain (Online)",
    publisher = "International Committee on Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.coling-main.609",
    doi = "10.18653/v1/2020.coling-main.609",
    pages = "6903--6915",
    abstract = "Due to the compelling improvements brought by BERT, many recent representation models adopted the Transformer architecture as their main building block, consequently inheriting the wordpiece tokenization system despite it not being intrinsically linked to the notion of Transformers. While this system is thought to achieve a good balance between the flexibility of characters and the efficiency of full words, using predefined wordpiece vocabularies from the general domain is not always suitable, especially when building models for specialized domains (e.g., the medical domain). Moreover, adopting a wordpiece tokenization shifts the focus from the word level to the subword level, making the models conceptually more complex and arguably less convenient in practice. For these reasons, we propose CharacterBERT, a new variant of BERT that drops the wordpiece system altogether and uses a Character-CNN module instead to represent entire words by consulting their characters. We show that this new model improves the performance of BERT on a variety of medical domain tasks while at the same time producing robust, word-level, and open-vocabulary representations.",
}
```