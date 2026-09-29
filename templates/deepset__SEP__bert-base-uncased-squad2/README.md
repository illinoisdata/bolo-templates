---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: deepset/bert-base-uncased-squad2
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
      value: 75.6529
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTY2YmQ0ZDFjMjRlZWRiZWQ2YWQ4MTM0ODkyYTQ0NmYwMzBlNWViZWQ0ODFhMGJmMmY4ZGYwOTQyMDAyZGNjYyIsInZlcnNpb24iOjF9.UyqonQTsCB0BW86LfPy17kLt3a4r3wMeh04MDam5t_UhElp6N02YpiKOqcb1ethNHjAR0WGyxrcV3TI4d-wFAQ
    - type: f1
      value: 78.6191
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWRkZWVjMDU2YTcxYWVkZTU1YmUzY2FkNWI5NDJkM2YwMjFmMmE0Njc3MjI5N2Q0NDdhZDNkZWNjMWE5YTRmZiIsInZlcnNpb24iOjF9.ol0Zacd9ZryXazXjgVssGFYG4s5FzbhGGaj1ZEDLVN2ziyzx23bo4GH9PSuGTFxRK2BO5_dxvDupLRqJOF59Bg
---

# bert-base-uncased for Extractive QA 

## Overview
**Language model:** bert-base-uncased  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
**Code:**  See [an example extractive QA pipeline built with Haystack](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline)  
**Infrastructure**: 1x Tesla v100

## Hyperparameters

```
batch_size = 32
n_epochs = 3
base_LM_model = "bert-base-uncased"
max_seq_len = 384
learning_rate = 3e-5
lr_schedule = LinearWarmup
warmup_proportion = 0.2
doc_stride=128
max_query_length=64
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

reader = ExtractiveReader(model="deepset/bert-base-uncased-squad2")
reader.warm_up()

question = "What is a popular programming language?"
result = reader.run(query=question, documents=docs)
# {'answers': [ExtractedAnswer(query='What is a popular programming language?', score=0.5740374326705933, data='python', document=Document(id=..., content: '...'), context=None, document_offset=ExtractedAnswer.Span(start=0, end=6),...)]}
```
For a complete example with an extractive question answering pipeline that scales over many documents, check out the [corresponding Haystack tutorial](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline).

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/bert-base-uncased-squad2"

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
```
"exact": 73.67977764676156
"f1": 77.87647139308865
```

## Authors
- Timo Möller: `timo.moeller [at] deepset.ai`
- Julian Risch: `julian.risch [at] deepset.ai`
- Malte Pietsch: `malte.pietsch [at] deepset.ai`
- Michel Bartels: `michel.bartels [at] deepset.ai`

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
- [deepset Cloud](https://www.deepset.ai/deepset-cloud-product)
- [deepset Studio](https://www.deepset.ai/deepset-studio)

## Get in touch and join the Haystack community

<p>For more info on Haystack, visit our <strong><a href="https://github.com/deepset-ai/haystack">GitHub</a></strong> repo and <strong><a href="https://docs.haystack.deepset.ai">Documentation</a></strong>. 

We also have a <strong><a class="h-7" href="https://haystack.deepset.ai/community">Discord community open to everyone!</a></strong></p>

[Twitter](https://twitter.com/Haystack_AI) | [LinkedIn](https://www.linkedin.com/company/deepset-ai/) | [Discord](https://haystack.deepset.ai/community) | [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) | [Website](https://haystack.deepset.ai/) | [YouTube](https://www.youtube.com/@deepset_ai)

By the way: [we're hiring!](http://www.deepset.ai/jobs)