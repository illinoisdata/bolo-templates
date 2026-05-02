---
library_name: transformers
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bm
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - ff
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gn
  - gu
  - ha
  - he
  - hi
  - hr
  - ht
  - hu
  - hy
  - id
  - ig
  - is
  - it
  - ja
  - jv
  - ka
  - kg
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lg
  - ln
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - no
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - qu
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - ss
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - ti
  - tl
  - tn
  - tr
  - uk
  - ur
  - uz
  - vi
  - wo
  - xh
  - yo
  - zh

license: agpl-3.0
tags:
  - v1.0.0
  - entity-disambiguation
  - named-entity-linking
  - entity-linking
  - text2text-generation
---

# Model Card for `impresso-project/nel-mgenre-multilingual`

The **Impresso multilingual named entity linking (NEL)** model is based on **mGENRE** (multilingual Generative ENtity
REtrieval) proposed by [De Cao et al](https://arxiv.org/abs/2103.12528), a sequence-to-sequence architecture for entity
disambiguation based on [mBART](https://arxiv.org/abs/2001.08210). It uses **constrained generation** to output entity
names mapped to Wikidata/QIDs.

This model was adapted for historical texts and fine-tuned on
the [HIPE-2022 dataset](https://github.com/hipe-eval/HIPE-2022-data), which includes a variety of historical document
types and languages.

## Model Details

### Model Description

- **Developed by:** EPFL from the [Impresso team](https://impresso-project.ch). The project is an interdisciplinary
  project focused on historical media analysis across languages, time, and modalities. Funded by the Swiss National
  Science
  Foundation ([CRSII5_173719](http://p3.snf.ch/project-173719), [CRSII5_213585](https://data.snf.ch/grants/grant/213585))
  and the Luxembourg National Research Fund (grant No. 17498891).
- **Model type:** mBART-based sequence-to-sequence model with constrained beam search for named entity linking
- **Languages:** Multilingual (100+ languages, optimized for French, German, and English)
- **License:** [AGPL v3+](https://github.com/impresso/impresso-pyindexation/blob/master/LICENSE)
- **Finetuned from:** [`facebook/mgenre-wiki`](https://huggingface.co/facebook/mgenre-wiki)

### Model Architecture

- **Architecture:** mBART-based seq2seq with constrained beam search

## Training Details

### Training Data

The model was trained on the following datasets:

| Dataset alias | README                                     | Document type          | Languages      | Suitable for               | Project                                                     | License                                                                                                                                                 |
|---------------|--------------------------------------------|------------------------|----------------|----------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ajmc          | [link](documentation/README-ajmc.md)       | classical commentaries | de, fr, en     | NERC-Coarse, NERC-Fine, EL | [AjMC](https://mromanello.github.io/ajax-multi-commentary/) | [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)                     |
| hipe2020      | [link](documentation/README-hipe2020.md)   | historical newspapers  | de, fr, en     | NERC-Coarse, NERC-Fine, EL | [CLEF-HIPE-2020](https://impresso.github.io/CLEF-HIPE-2020) | [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| topres19th    | [link](documentation/README-topres19th.md) | historical newspapers  | en             | NERC-Coarse, EL            | [Living with Machines](https://livingwithmachines.ac.uk/)   | [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| newseye       | [link](documentation/README-newseye.md)    | historical newspapers  | de, fi, fr, sv | NERC-Coarse, NERC-Fine, EL | [NewsEye](https://www.newseye.eu/)                          | [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)                     |
| sonar         | [link](documentation/README-sonar.md)      | historical newspapers  | de             | NERC-Coarse, EL            | [SoNAR](https://sonar.fh-potsdam.de/)                       | [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)                     |

## How to Use

```python
from transformers import AutoTokenizer, pipeline

NEL_MODEL_NAME = "impresso-project/nel-mgenre-multilingual"
nel_tokenizer = AutoTokenizer.from_pretrained(NEL_MODEL_NAME)

nel_pipeline = pipeline("generic-nel", model=NEL_MODEL_NAME,
                        tokenizer=nel_tokenizer,
                        trust_remote_code=True,
                        device='cpu')

sentence = "Le 0ctobre 1894, [START] Dreyfvs [END] est arrêté à Paris, accusé d'espionnage pour l'Allemagne — un événement qui déch1ra la société fr4nçaise pendant des années."
print(nel_pipeline(sentence))
```

### Output Format

```python
[
    {
        'surface': 'Dreyfvs',
        'wkd_id': 'Q171826',
        'wkpedia_pagename': 'Alfred Dreyfus',
        'wkpedia_url': 'https://fr.wikipedia.org/wiki/Alfred_Dreyfus',
        'type': 'UNK',
        'confidence_nel': 99.98,
        'lOffset': 24,
        'rOffset': 33}]
```

----

### Batched predictions

```python
from transformers import AutoTokenizer, pipeline

NEL_MODEL_NAME = "impresso-project/nel-mgenre-multilingual"

nel_tokenizer = AutoTokenizer.from_pretrained(NEL_MODEL_NAME)

nel_pipeline = pipeline(
    "generic-nel",
    model=NEL_MODEL_NAME,
    tokenizer=nel_tokenizer,
    trust_remote_code=True,
    device="cpu",
)

sentences = [
    "Le 0ctobre 1894, [START] Dreyfvs [END] est arrêté à Paris.",
    "En 1912, [START] Giollitti [END] était encore au pouvoir en Italie.",
    "La ville de [START] Lpzbourg [END] est importante dans la région."
]

results = nel_pipeline(sentences)

from pprint import pprint
pprint(results)
```

The type of the entity is `UNK` because the model was not trained on the entity type. The `confidence_nel` score
indicates the model's confidence in the prediction.

## Use Cases

- Entity disambiguation in noisy OCR settings
- Linking historical names to modern Wikidata entities
- Assisting downstream event extraction and biography generation from historical archives

> 🐱**Easter Egg**:  
> While the pipeline’s main goal is to link surface forms to QIDs and Wikipedia pages,  
> it sometimes slips in an extra surprise: a coarse Wikidata type label (`pers`, `org`, or `loc`).  
> Not strictly required — but a handy little bonus when it shows up!

## Limitations

- Sensitive to tokenisation and malformed spans
- Accuracy degrades on non-Wikidata entities or in highly ambiguous contexts
- Focused on historical entity mentions — performance may vary on modern texts

## Environmental Impact

- **Hardware:** 1x A100 (80GB) for finetuning
- **Training time:** ~12 hours
- **Estimated CO₂ Emissions:** ~2.3 kg CO₂eq

## Contact

- Website: [https://impresso-project.ch](https://impresso-project.ch)

<p align="center">
  <img src="https://github.com/impresso/impresso.github.io/blob/master/assets/images/3x1--Yellow-Impresso-Black-on-White--transparent.png?raw=true" width="300" alt="Impresso Logo"/>
</p>