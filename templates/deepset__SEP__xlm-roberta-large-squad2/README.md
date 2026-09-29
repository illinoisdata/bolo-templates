---
language: multilingual
license: cc-by-4.0
tags:
- question-answering
datasets:
- squad_v2
model-index:
- name: deepset/xlm-roberta-large-squad2
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
      value: 81.8281
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzVhZDE2NTg5NmUwOWRkMmI2MGUxYjFlZjIzNmMyNDQ2MDY2MDNhYzE0ZjY5YTkyY2U4ODc3ODFiZjQxZWQ2YSIsInZlcnNpb24iOjF9.f_rN3WPMAdv-OBPz0T7N7lOxYz9f1nEr_P-vwKhi3jNdRKp_JTy18MYR9eyJM2riKHC6_ge-8XwfyrUf51DSDA
    - type: f1
      value: 84.8886
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGE5MWJmZGUxMGMwNWFhYzVhZjQwZGEwOWQ4N2Q2Yjg5NzdjNDFiNDhiYTQ1Y2E5ZWJkOTFhYmI1Y2Q2ZGYwOCIsInZlcnNpb24iOjF9.TIdH-tOx3kEMDs5wK1r6iwZqqSjNGlBrpawrsE917j1F3UFJVnQ7wJwaj0OIgmC4iw8OQeLZL56ucBcLApa-AQ
---

# Multilingual XLM-RoBERTa large for Extractive QA on various languages 

## Overview
**Language model:** xlm-roberta-large  
**Language:** Multilingual  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD dev set - German MLQA - German XQuAD   
**Training run:** [MLFlow link](https://public-mlflow.deepset.ai/#/experiments/124/runs/3a540e3f3ecf4dd98eae8fc6d457ff20)  
**Code:**  See [an example extractive QA pipeline built with Haystack](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline)  
**Infrastructure**: 4x Tesla v100

## Hyperparameters

```
batch_size = 32
n_epochs = 3
base_LM_model = "xlm-roberta-large"
max_seq_len = 256
learning_rate = 1e-5
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

reader = ExtractiveReader(model="deepset/xlm-roberta-large-squad2")
reader.warm_up()

question = "What is a popular programming language?"
result = reader.run(query=question, documents=docs)
# {'answers': [ExtractedAnswer(query='What is a popular programming language?', score=0.5740374326705933, data='python', document=Document(id=..., content: '...'), context=None, document_offset=ExtractedAnswer.Span(start=0, end=6),...)]}
```
For a complete example with an extractive question answering pipeline that scales over many documents, check out the [corresponding Haystack tutorial](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline).

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/xlm-roberta-large-squad2"

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
Evaluated on the SQuAD 2.0 English dev set with the [official eval script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/).
```
  "exact": 79.45759285774446,
  "f1": 83.79259828925511,
  "total": 11873,
  "HasAns_exact": 71.96356275303644,
  "HasAns_f1": 80.6460053117963,
  "HasAns_total": 5928,
  "NoAns_exact": 86.93019343986543,
  "NoAns_f1": 86.93019343986543,
  "NoAns_total": 5945
```

Evaluated on German [MLQA: test-context-de-question-de.json](https://github.com/facebookresearch/MLQA)
```
"exact": 49.34691166703564,
"f1": 66.15582561674236,
"total": 4517,
```

Evaluated on German [XQuAD: xquad.de.json](https://github.com/deepmind/xquad)
```
"exact": 61.51260504201681,
"f1": 78.80206098332569,
"total": 1190,
```

## Usage

### In Haystack
For doing QA at scale (i.e. many docs instead of single paragraph), you can load the model also in [haystack](https://github.com/deepset-ai/haystack/):
```python
reader = FARMReader(model_name_or_path="deepset/xlm-roberta-large-squad2")
# or 
reader = TransformersReader(model="deepset/xlm-roberta-large-squad2",tokenizer="deepset/xlm-roberta-large-squad2")
```

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/xlm-roberta-large-squad2"

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
**Branden Chan:** branden.chan@deepset.ai    
**Timo Möller:** timo.moeller@deepset.ai      
**Malte Pietsch:** malte.pietsch@deepset.ai      
**Tanay Soni:** tanay.soni@deepset.ai    

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