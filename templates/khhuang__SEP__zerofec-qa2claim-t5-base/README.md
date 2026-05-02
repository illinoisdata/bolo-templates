---
language: en
widget:
- text: a 1968 american independent horror film \\n What is Night of the Living Dead?
---

# QA2Claim Model From ZeroFEC 

ZeroFEC is a faithful and interpetable factual error correction framework introduced in the paper [Zero-shot Faithful Factual Error Correction](https://aclanthology.org/2023.acl-long.311/). It involves a component that converts qa-pairs to declarative statements, which is hosted in this repo. The associated code is released in [this](https://github.com/khuangaf/ZeroFEC) repository.

### How to use
Using Huggingface pipeline abstraction:
```python
from transformers import pipeline

nlp = pipeline("text2text-generation", model='khhuang/zerofec-qa2claim-t5-base', tokenizer='khhuang/zerofec-qa2claim-t5-base')
    
QUESTION = "What is Night of the Living Dead?"
ANSWER = "a 1968 american independent horror film"

def format_inputs(question: str, answer: str):
    return f"{answer} \\n {question}"

text = format_inputs(QUESTION, ANSWER)

nlp(text)
# should output [{'generated_text': 'Night of the Living Dead is a 1968 american independent horror film.'}]
```

Using the pre-trained model directly:
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained('khhuang/zerofec-qa2claim-t5-base')
model = AutoModelForSeq2SeqLM.from_pretrained('khhuang/zerofec-qa2claim-t5-base')

QUESTION = "What is Night of the Living Dead?"
ANSWER = "a 1968 american independent horror film"

def format_inputs(question: str, answer: str):
    return f"{answer} \\n {question}"

text = format_inputs(QUESTION, ANSWER)

input_ids = tokenizer(text, return_tensors="pt").input_ids
generated_ids = model.generate(input_ids, max_length=32, num_beams=4)
output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
print(output)
# should output "Night of the Living Dead is a 1968 american independent horror film."
```

### Citation
```
@inproceedings{huang-etal-2023-zero,
    title = "Zero-shot Faithful Factual Error Correction",
    author = "Huang, Kung-Hsiang  and
      Chan, Hou Pong  and
      Ji, Heng",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.311",
    doi = "10.18653/v1/2023.acl-long.311",
    pages = "5660--5676",
}
```