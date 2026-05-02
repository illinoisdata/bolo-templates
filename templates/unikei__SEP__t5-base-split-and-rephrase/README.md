---
license: bigscience-openrail-m
tags:
- split and rephrase
widget:
- text: >-
    Cystic Fibrosis (CF) is an autosomal recessive disorder that affects
    multiple organs, which is common in the Caucasian population,
    symptomatically affecting 1 in 2500 newborns in the UK, and more than 80,000
    individuals globally.
datasets:
- wiki_split
- web_split
language:
- en
---


# T5 model for splitting complex sentences to simple sentences in English
Split-and-rephrase is the task of splitting a complex input sentence into shorter sentences while preserving meaning. (Narayan et al., 2017) 

E.g.:
```
Cystic Fibrosis (CF) is an autosomal recessive disorder that affects multiple organs,
which is common in the Caucasian population, symptomatically affecting 1 in 2500 newborns in the UK,
and more than 80,000 individuals globally.
```
could be split into
```
Cystic Fibrosis is an autosomal recessive disorder that affects multiple organs. 
```
```
Cystic Fibrosis is common in the Caucasian population.
```
```
Cystic Fibrosis affects 1 in 2500 newborns in the UK. 
```
```
Cystic Fibrosis affects more than 80,000 individuals globally.
```

## How to use it in your code:
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
checkpoint="unikei/t5-base-split-and-rephrase"
tokenizer = T5Tokenizer.from_pretrained(checkpoint)
model = T5ForConditionalGeneration.from_pretrained(checkpoint)

complex_sentence = "Cystic Fibrosis (CF) is an autosomal recessive disorder that \
affects multiple organs, which is common in the Caucasian \
population, symptomatically affecting 1 in 2500 newborns in \
the UK, and more than 80,000 individuals globally."
complex_tokenized = tokenizer(complex_sentence, 
                                 padding="max_length", 
                                 truncation=True,
                                 max_length=256, 
                                 return_tensors='pt')

simple_tokenized = model.generate(complex_tokenized['input_ids'], attention_mask = complex_tokenized['attention_mask'], max_length=256, num_beams=5)
simple_sentences = tokenizer.batch_decode(simple_tokenized, skip_special_tokens=True)
print(simple_sentences)

"""
Output:
Cystic Fibrosis is an autosomal recessive disorder that affects multiple organs. Cystic Fibrosis is common in the Caucasian population. Cystic Fibrosis affects 1 in 2500 newborns in the UK. Cystic Fibrosis affects more than 80,000 individuals globally.
"""
```