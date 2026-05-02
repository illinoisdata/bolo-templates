---
language: en
widget:
- text: What is Night of the Living Dead? \n Night of the Living Dead is a 1968 American independent horror film , directed by George A. Romero , starring Duane Jones and Judith O'Dea . George A. Romero George A. Romero Duane Jones Duane Jones Judith O'Dea Judith O'Dea independent Independent film horror film horror film.
---

# Domain-adapted QA Model From ZeroFEC 

ZeroFEC is a faithful and interpetable factual error correction framework introduced in the paper [Zero-shot Faithful Factual Error Correction](https://aclanthology.org/2023.acl-long.311/). It involves a QA component, which is a UnifiedQA model continue fine-tuned on two additional biomedical QA datasets. The associated code is released in [this](https://github.com/khuangaf/ZeroFEC) repository.

### How to use
Using Huggingface pipeline abstraction:
```python
from transformers import pipeline

nlp = pipeline("text2text-generation", model='khhuang/zerofec-daqa-t5-base', tokenizer='khhuang/zerofec-daqa-t5-base')
    
QUESTION = "What is Night of the Living Dead?"
CONTEXT = "Night of the Living Dead is a 1968 American independent horror film , directed by George A."

def format_inputs(context: str, question: str):
    return f"{question} \n {context}"

text = format_inputs(CONTEXT, QUESTION)

nlp(text)
# should output [{'generated_text': 'a 1968 american independent horror film'}]
```

Using the pre-trained model directly:
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained('khhuang/zerofec-daqa-t5-base')
model = AutoModelForSeq2SeqLM.from_pretrained('khhuang/zerofec-daqa-t5-base')

QUESTION = "What is Night of the Living Dead?"
CONTEXT = "Night of the Living Dead is a 1968 American independent horror film , directed by George A."

def format_inputs(context: str, question: str):
    return f"{question} \n {context}"

text = format_inputs(CONTEXT, QUESTION)


input_ids = tokenizer(text, return_tensors="pt").input_ids
generated_ids = model.generate(input_ids, max_length=32, num_beams=4)
output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
print(output)
# should output "a 1968 american independent horror film"
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