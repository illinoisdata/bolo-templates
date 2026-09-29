---
language:
- es
library_name: pysentimiento
tags:
- twitter
- named-entity-recognition
- ner
datasets:
- lince
---

# Named Entity Recognition model for Spanish/English
## robertuito-ner

Repository: [https://github.com/pysentimiento/pysentimiento/](https://github.com/finiteautomata/pysentimiento/)


Model trained with the Spanish/English split of the [LinCE NER corpus](https://ritual.uh.edu/lince/), a code-switched benchmark . Base model is [RoBERTuito](https://github.com/pysentimiento/robertuito), a RoBERTa model trained in Spanish tweets.


## Usage

If you want to use this model, we suggest you use it directly from the `pysentimiento` library as it is not working properly with the pipeline due to tokenization issues

```python
from pysentimiento import create_analyzer

ner_analyzer = create_analyzer("ner", lang="es")

ner_analyzer.predict(
  "rindanse ante el mejor, leonel andres messi cuccitini. serresiete no existis, segui en al-nassr"
)
 

# [{'type': 'PER',
#   'text': 'leonel andres messi cuccitini',
#   'start': 24,
#   'end': 53},
#  {'type': 'PER', 'text': 'serresiete', 'start': 55, 'end': 65},
#  {'type': 'LOC', 'text': 'al-nassr', 'start': 108, 'end': 116}]
```

## Results

Results are taken from the LinCE leaderboard

| Model                  | Sentiment       | NER                | POS     |
|:-----------------------|:----------------|:-------------------|:--------|
| RoBERTuito             | **60.6**        | 68.5               | 97.2    |
| XLM Large              | --              | **69.5**           | **97.2**   |
| XLM Base               | --              | 64.9               | 97.0    |
| C2S mBERT              | 59.1            | 64.6               | 96.9    |
| mBERT                  | 56.4            | 64.0               | 97.1    |
| BERT                   | 58.4            | 61.1               | 96.9    |
| BETO                   | 56.5            | --                 | --      |



## Citation

If you use this model in your research, please cite pysentimiento, RoBERTuito and LinCE papers:

```
@misc{perez2021pysentimiento,
      title={pysentimiento: A Python Toolkit for Sentiment Analysis and SocialNLP tasks},
      author={Juan Manuel Pérez and Juan Carlos Giudici and Franco Luque},
      year={2021},
      eprint={2106.09462},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@inproceedings{perez2022robertuito,
  title={RoBERTuito: a pre-trained language model for social media text in Spanish},
  author={P{\'e}rez, Juan Manuel and Furman, Dami{\'a}n Ariel and Alemany, Laura Alonso and Luque, Franco M},
  booktitle={Proceedings of the Thirteenth Language Resources and Evaluation Conference},
  pages={7235--7243},
  year={2022}
}

@inproceedings{aguilar2020lince,
  title={LinCE: A Centralized Benchmark for Linguistic Code-switching Evaluation},
  author={Aguilar, Gustavo and Kar, Sudipta and Solorio, Thamar},
  booktitle={Proceedings of the 12th Language Resources and Evaluation Conference},
  pages={1803--1813},
  year={2020}
}
```