---
language:
- en
library_name: transformers
pipeline_tag: summarization
datasets:
- ChristophSchuhmann/gutenberg-wiki-arxiv-pubmed-soda-summaries
---


# Usage

```python
from transformers import pipeline

max_length = 50
min_length = 10
model_id = "marianna13/flan-t5-base-summarization"

summarizer = pipeline("summarization", model=model_id, max_length=max_length, min_length=min_length)

text = ''' For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.'''
print(text)
print('##### Summary:')
print(summarizer(text)[0]['summary_text'])

#  For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.
# ##### Summary:
# "I am convinced that neither death, life, angels, demons, present, future, powers, height, depth, or anything else in all creation can separate us from the love of God that is in Christ Jesus our Lord."
```