---
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: deepset/xlm-roberta-base-squad2
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
      value: 74.0354
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMWMxNWQ2ODJkNWIzZGQwOWI4OTZjYjU3ZDVjZGQzMjI5MzljNjliZTY4Mzk4YTk4OTMzZWYxZjUxYmZhYTBhZSIsInZlcnNpb24iOjF9.eEeFYYJ30BfJDd-JYfI1kjlxJrRF6OFtj2GnkTCOO4kqX31inFy8ptDWusVlLFsUphm4dNWfTKXC5e-gytLBDA
    - type: f1
      value: 77.1833
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjg4MjNkOTA4Y2I5OGFlYTk1NWZjMWFlNjI5M2Y0NGZhMThhN2M4YmY2Y2RhZjcwYzU0MGNjN2RkZDljZmJmNiIsInZlcnNpb24iOjF9.TX42YMXpH4e0qu7cC4ARDlZWSkd55dwwyeyFXmOlXERNnEicDuFBCsy8WHLaqQCLUkzODJ22Hw4zhv81rwnlAQ
---

# Multilingual XLM-RoBERTa base for Extractive QA on various languages 

## Overview
**Language model:** xlm-roberta-base  
**Language:** Multilingual  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0   
**Eval data:** SQuAD 2.0 dev set - German MLQA - German XQuAD   
**Code:**  See [an example extractive QA pipeline built with Haystack](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline)  
**Infrastructure**: 4x Tesla v100

## Hyperparameters

```
batch_size = 22*4
n_epochs = 2
max_seq_len=256,
doc_stride=128,
learning_rate=2e-5,
``` 

Corresponding experiment logs in mlflow: [link](https://public-mlflow.deepset.ai/#/experiments/2/runs/b25ec75e07614accb3f1ce03d43dbe08)


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

reader = ExtractiveReader(model="deepset/xlm-roberta-base-squad2")
reader.warm_up()

question = "What is a popular programming language?"
result = reader.run(query=question, documents=docs)
# {'answers': [ExtractedAnswer(query='What is a popular programming language?', score=0.5740374326705933, data='python', document=Document(id=..., content: '...'), context=None, document_offset=ExtractedAnswer.Span(start=0, end=6),...)]}
```
For a complete example with an extractive question answering pipeline that scales over many documents, check out the [corresponding Haystack tutorial](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline).

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/xlm-roberta-base-squad2"

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

## Performance
Evaluated on the SQuAD 2.0 dev set with the [official eval script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/).
```
"exact": 73.91560683904657
"f1": 77.14103746689592
```

Evaluated on German MLQA: test-context-de-question-de.json
  "exact": 33.67279167589108
  "f1": 44.34437105434842
  "total": 4517

Evaluated on German XQuAD: xquad.de.json
"exact": 48.739495798319325
  "f1": 62.552615701071495
  "total": 1190

## Authors
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