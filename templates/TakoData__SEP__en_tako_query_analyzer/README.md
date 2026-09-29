---
tags:
- spacy
- token-classification
- text-classification
language:
- en
model-index:
- name: en_tako_query_analyzer
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.0
    - name: NER Recall
      type: recall
      value: 0.0
    - name: NER F Score
      type: f_score
      value: 0.0
---
| Feature | Description |
| --- | --- |
| **Name** | `en_tako_query_analyzer` |
| **Version** | `0.0.5` |
| **spaCy** | `>=3.8.11,<3.9.0` |
| **Default Pipeline** | `tok2vec_small`, `tagger`, `parser`, `attribute_ruler`, `senter`, `tok2vec`, `ner`, `textcat_multilabel`, `textcat_classify` |
| **Components** | `tok2vec_small`, `tagger`, `parser`, `attribute_ruler`, `senter`, `tok2vec`, `ner`, `textcat_multilabel`, `textcat_classify` |
| **Vectors** | 684830 keys, 342918 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (124 labels for 5 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `$`, `''`, `,`, `-LRB-`, `-RRB-`, `.`, `:`, `ADD`, `AFX`, `CC`, `CD`, `DT`, `EX`, `FW`, `HYPH`, `IN`, `JJ`, `JJR`, `JJS`, `LS`, `MD`, `NFP`, `NN`, `NNP`, `NNPS`, `NNS`, `PDT`, `POS`, `PRP`, `PRP$`, `RB`, `RBR`, `RBS`, `RP`, `SYM`, `TO`, `UH`, `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `WDT`, `WP`, `WP$`, `WRB`, `XX`, `_SP`, ```` |
| **`parser`** | `ROOT`, `acl`, `acomp`, `advcl`, `advmod`, `agent`, `amod`, `appos`, `attr`, `aux`, `auxpass`, `case`, `cc`, `ccomp`, `compound`, `conj`, `csubj`, `csubjpass`, `dative`, `dep`, `det`, `dobj`, `expl`, `intj`, `mark`, `meta`, `neg`, `nmod`, `npadvmod`, `nsubj`, `nsubjpass`, `nummod`, `oprd`, `parataxis`, `pcomp`, `pobj`, `poss`, `preconj`, `predet`, `prep`, `prt`, `punct`, `quantmod`, `relcl`, `xcomp` |
| **`ner`** | `CARDINAL`, `DATE`, `EVENT`, `FAC`, `GPE`, `LANGUAGE`, `LAW`, `LOC`, `MONEY`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PRODUCT`, `QUANTITY`, `STOCK_TICKER`, `TIME`, `WORK_OF_ART` |
| **`textcat_multilabel`** | `Finance`, `Economics`, `Demographics`, `Health`, `Politics`, `Sports`, `Climate`, `Other` |
| **`textcat_classify`** | `ACCEPT`, `REJECT` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 0.00 |
| `ENTS_P` | 0.00 |
| `ENTS_R` | 0.00 |
| `ENTS_PER_TYPE` | 0.00 |
| `CATS_SCORE` | 84.62 |
| `CATS_MICRO_P` | 83.50 |
| `CATS_MICRO_R` | 83.50 |
| `CATS_MICRO_F` | 83.50 |
| `CATS_MACRO_P` | 84.23 |
| `CATS_MACRO_R` | 83.50 |
| `CATS_MACRO_F` | 83.41 |
| `CATS_MACRO_AUC` | 83.96 |
| `TEXTCAT_CLASSIFY_LOSS` | 1108.70 |