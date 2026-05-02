---
language: en
thumbnail: https://raw.githubusercontent.com/digitalepidemiologylab/covid-twitter-bert/master/images/COVID-Twitter-BERT_small.png
tags:
- Twitter
- COVID-19
license: mit
---

# COVID-Twitter-BERT v2

## Model description

BERT-large-uncased model, pretrained on a corpus of messages from Twitter about COVID-19. This model is identical to [covid-twitter-bert](https://huggingface.co/digitalepidemiologylab/covid-twitter-bert) - but trained on more data, resulting in higher downstream performance.

Find more info on our [GitHub page](https://github.com/digitalepidemiologylab/covid-twitter-bert).


## Intended uses & limitations

The model can e.g. be used in the `fill-mask` task (see below). You can also use the model without the MLM/NSP heads and train a classifier with it.

#### How to use

```python
from transformers import pipeline
import json

pipe = pipeline(task='fill-mask', model='digitalepidemiologylab/covid-twitter-bert-v2')
out = pipe(f"In places with a lot of people, it's a good idea to wear a {pipe.tokenizer.mask_token}")
print(json.dumps(out, indent=4))
[
    {
        "sequence": "[CLS] in places with a lot of people, it's a good idea to wear a mask [SEP]",
        "score": 0.9998226761817932,
        "token": 7308,
        "token_str": "mask"
    },
    ...
]
```

## Training procedure
This model was trained on 97M unique tweets (1.2B training examples) collected between January 12 and July 5, 2020 containing at least one of the keywords "wuhan", "ncov", "coronavirus", "covid", or "sars-cov-2". These tweets were filtered and preprocessed to reach a final sample of 22.5M tweets (containing 40.7M sentences and 633M tokens) which were used for training.

## Eval results
The model was evaluated based on downstream Twitter text classification tasks from previous SemEval challenges.

### BibTeX entry and citation info

```bibtex
@article{muller2020covid,
  title={COVID-Twitter-BERT: A Natural Language Processing Model to Analyse COVID-19 Content on Twitter},
  author={M{\"u}ller, Martin and Salath{\'e}, Marcel and Kummervold, Per E},
  journal={arXiv preprint arXiv:2005.07503},
  year={2020}
}
```

or

```Martin Müller, Marcel Salathé, and Per E. Kummervold.
COVID-Twitter-BERT: A Natural Language Processing Model to Analyse COVID-19 Content on Twitter.
arXiv preprint arXiv:2005.07503 (2020).
```