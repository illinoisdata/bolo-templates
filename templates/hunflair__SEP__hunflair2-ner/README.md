---
tags:
- flair
- token-classification
- sequence-tagger-model
---

### Demo: How to use in Flair

Requires:
- **[Flair](https://github.com/flairNLP/flair/)>=0.14.0** (`pip install flair` or `pip install git+https://github.com/flairNLP/flair.git`)

```python
from flair.data import Sentence
from flair.models.prefixed_tagger import PrefixedSequenceTagger
from flair.tokenization import SciSpacyTokenizer

# load tagger
tagger = PrefixedSequenceTagger.load("hunflair/hunflair2-ner")

# make example sentence
sentence = Sentence("The mutation in the ABCD1 gene causes X-linked adrenoleukodystrophy, "
    "a neurodegenerative disease, which is exacerbated by exposure to high "
    "levels of mercury in dolphin populations.",
    use_tokenizer=SciSpacyTokenizer())

# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following NER tags are found:')

# iterate over entities and print
for entity in sentence.get_spans('ner'):
    print(entity)
```