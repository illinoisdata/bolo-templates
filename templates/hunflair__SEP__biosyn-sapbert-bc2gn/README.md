---
tags:
  - flair
  - entity-mention-linker
---

## bioasyn-sapbert-bc2gn-gene

Biomedical Entity Mention Linking for gene:

- Model: [dmis-lab/biosyn-sapbert-bc2gn](https://huggingface.co/dmis-lab/biosyn-sapbert-bc2gn)
- Dictionary: [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene) ([Homo_sapiens.gene_info.gz](https://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/))

### Demo: How to use in Flair

Requires:

- **[Flair](https://github.com/flairNLP/flair/)>=0.14.0** (`pip install flair` or `pip install git+https://github.com/flairNLP/flair.git`)

```python
from flair.data import Sentence
from flair.models import Classifier, EntityMentionLinker
from flair.tokenization import SciSpacyTokenizer

sentence = Sentence(
    "The mutation in the ABCD1 gene causes X-linked adrenoleukodystrophy, "
    "a neurodegenerative disease, which is exacerbated by exposure to high "
    "levels of mercury in dolphin populations.",
    use_tokenizer=SciSpacyTokenizer()
)

# load hunflair to detect the entity mentions we want to link.
tagger = Classifier.load("hunflair-gene")
tagger.predict(sentence)

# load the linker and dictionary
linker = EntityMentionLinker.load("gene-linker")
linker.predict(sentence)

# print the results for each entity mention:
for span in sentence.get_spans(tagger.label_type):
    for link in span.get_labels(linker.label_type):
      print(f"{span.text} -> {link.value}")
```

As an alternative to downloading the already precomputed model (much storage). You can also build the model
and compute the embeddings for the dataset using:

```python
linker = EntityMentionLinker.build("dmis-lab/biosyn-sapbert-bc2gn", dictionary_name_or_path="ncbi-gene", hybrid_search=False)
```

This will reduce the download requirements, at the cost of computation.