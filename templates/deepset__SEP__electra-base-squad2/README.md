---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: deepset/electra-base-squad2
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_v2
      type: squad_v2
      config: squad_v2
      split: validation
    metrics:
    - type: exact_match
      value: 77.6074
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzE5NTRmMmUwYTk1MTI0NjM0ZmQwNDFmM2Y4Mjk4ZWYxOGVmOWI3ZGFiNWM4OTUxZDQ2ZjdmNmU3OTk5ZjRjYyIsInZlcnNpb24iOjF9.0VZRewdiovE4z3K5box5R0oTT7etpmd0BX44FJBLRFfot-uJ915b-bceSv3luJQ7ENPjaYSa7o7jcHlDzn3oAw
    - type: f1
      value: 81.7181
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2VlMzM0Y2UzYjhhNTJhMTFiYWZmMDNjNjRiZDgwYzc5NWE3N2M4ZGFlYWQ0ZjVkZTE2MDU0YmMzMDc1MTY5MCIsInZlcnNpb24iOjF9.jRV58UxOM7CJJSsmxJuZvlt00jMGA1thp4aqtcFi1C8qViQ1kW7NYz8rg1gNTDZNez2UwPS1NgN_HnnwBHPbCQ
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad
      type: squad
      config: plain_text
      split: validation
    metrics:
    - type: exact_match
      value: 80.407
      name: Exact Match
    - type: f1
      value: 88.942
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: adversarial_qa
      type: adversarial_qa
      config: adversarialQA
      split: validation
    metrics:
    - type: exact_match
      value: 23.533
      name: Exact Match
    - type: f1
      value: 36.521
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_adversarial
      type: squad_adversarial
      config: AddOneSent
      split: validation
    metrics:
    - type: exact_match
      value: 73.867
      name: Exact Match
    - type: f1
      value: 81.381
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts amazon
      type: squadshifts
      config: amazon
      split: test
    metrics:
    - type: exact_match
      value: 64.512
      name: Exact Match
    - type: f1
      value: 80.166
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts new_wiki
      type: squadshifts
      config: new_wiki
      split: test
    metrics:
    - type: exact_match
      value: 76.568
      name: Exact Match
    - type: f1
      value: 87.706
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts nyt
      type: squadshifts
      config: nyt
      split: test
    metrics:
    - type: exact_match
      value: 77.884
      name: Exact Match
    - type: f1
      value: 87.858
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts reddit
      type: squadshifts
      config: reddit
      split: test
    metrics:
    - type: exact_match
      value: 64.399
      name: Exact Match
    - type: f1
      value: 78.096
      name: F1
---

# electra-base for Extractive QA

## Overview
**Language model:** electra-base  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
**Code:**  See [an example extractive QA pipeline built with Haystack](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline)
**Infrastructure**: 1x Tesla v100

## Hyperparameters

```
seed=42
batch_size = 32
n_epochs = 5
base_LM_model = "google/electra-base-discriminator"
max_seq_len = 384
learning_rate = 1e-4
lr_schedule = LinearWarmup
warmup_proportion = 0.1
doc_stride=128
max_query_length=64
```

## Performance
Evaluated on the SQuAD 2.0 dev set with the [official eval script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/).
```
"exact": 77.30144024256717,
 "f1": 81.35438272008543,
 "total": 11873,
 "HasAns_exact": 74.34210526315789,
 "HasAns_f1": 82.45961302894314,
 "HasAns_total": 5928,
 "NoAns_exact": 80.25231286795626,
 "NoAns_f1": 80.25231286795626,
 "NoAns_total": 5945
```


## Usage

### In Haystack
Haystack is an AI orchestration framework to build customizable, production-ready LLM applications. You can use this model in Haystack to do extractive question answering on documents. 
To load and run the model with [Haystack](https://github.com/deepset-ai/haystack/):
```python
# After running pip install haystack-ai "transformers[torch,sentencepiece]"

from haystack import Document
from haystack.components.readers import ExtractiveReader

docs = [
    Document(content="Python is a popular programming language"),
    Document(content="python ist eine beliebte Programmiersprache"),
]

reader = ExtractiveReader(model="deepset/roberta-base-squad2")
reader.warm_up()

question = "What is a popular programming language?"
result = reader.run(query=question, documents=docs)
# {'answers': [ExtractedAnswer(query='What is a popular programming language?', score=0.5740374326705933, data='python', document=Document(id=..., content: '...'), context=None, document_offset=ExtractedAnswer.Span(start=0, end=6),...)]}
```
For a complete example with an extractive question answering pipeline that scales over many documents, check out the [corresponding Haystack tutorial](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline).

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

## Authors
Vaishali Pal `vaishali.pal [at] deepset.ai`  
Branden Chan: `branden.chan [at] deepset.ai`  
Timo Möller: `timo.moeller [at] deepset.ai`  
Malte Pietsch: `malte.pietsch [at] deepset.ai`  
Tanay Soni: `tanay.soni [at] deepset.ai`  

## About us

<div class="grid lg:grid-cols-2 gap-x-4 gap-y-3">
    <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/deepset-logo-colored.png" class="w-40"/>
     </div>
     <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/haystack-logo-colored.png" class="w-40"/>
     </div>
</div>

[deepset](http://deepset.ai/) is the company behind the production-ready open-source AI framework [Haystack](https://haystack.deepset.ai/).

Some of our other work: 
- [Distilled roberta-base-squad2 (aka "tinyroberta-squad2")](https://huggingface.co/deepset/tinyroberta-squad2)
- [German BERT](https://deepset.ai/german-bert), [GermanQuAD and GermanDPR](https://deepset.ai/germanquad), [German embedding model](https://huggingface.co/mixedbread-ai/deepset-mxbai-embed-de-large-v1)
- [deepset Cloud](https://www.deepset.ai/deepset-cloud-product), [deepset Studio](https://www.deepset.ai/deepset-studio)

## Get in touch and join the Haystack community

<p>For more info on Haystack, visit our <strong><a href="https://github.com/deepset-ai/haystack">GitHub</a></strong> repo and <strong><a href="https://docs.haystack.deepset.ai">Documentation</a></strong>. 

We also have a <strong><a class="h-7" href="https://haystack.deepset.ai/community">Discord community open to everyone!</a></strong></p>

[Twitter](https://twitter.com/Haystack_AI) | [LinkedIn](https://www.linkedin.com/company/deepset-ai/) | [Discord](https://haystack.deepset.ai/community) | [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) | [Website](https://haystack.deepset.ai/) | [YouTube](https://www.youtube.com/@deepset_ai)

By the way: [we're hiring!](http://www.deepset.ai/jobs)