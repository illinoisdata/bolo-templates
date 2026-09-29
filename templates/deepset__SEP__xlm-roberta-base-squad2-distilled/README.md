---
language: multilingual
datasets:
- squad_v2
license: mit
thumbnail: https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg
tags:
- exbert
---

# Multilingual XLM-RoBERTa base distilled for Extractive QA on various languages
- Haystack's distillation feature was used for training. deepset/xlm-roberta-large-squad2 was used as the teacher model.

## Overview
**Language model:** deepset/xlm-roberta-base-squad2-distilled   
**Language:** Multilingual  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
**Code:**  See [an example extractive QA pipeline built with Haystack](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline)  
**Infrastructure**: 1x Tesla v100

## Hyperparameters

```
batch_size = 56
n_epochs = 4
max_seq_len = 384
learning_rate = 3e-5
lr_schedule = LinearWarmup
embeds_dropout_prob = 0.1
temperature = 3
distillation_loss_weight = 0.75
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

reader = ExtractiveReader(model="deepset/xlm-roberta-base-squad2-distilled")
reader.warm_up()

question = "What is a popular programming language?"
result = reader.run(query=question, documents=docs)
# {'answers': [ExtractedAnswer(query='What is a popular programming language?', score=0.5740374326705933, data='python', document=Document(id=..., content: '...'), context=None, document_offset=ExtractedAnswer.Span(start=0, end=6),...)]}
```
For a complete example with an extractive question answering pipeline that scales over many documents, check out the [corresponding Haystack tutorial](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline).

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/xlm-roberta-base-squad2-distilled"

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
Evaluated on the SQuAD 2.0 dev set
```
"exact": 74.06721131980123%
"f1": 76.39919553344667%
```

## Authors
**Timo Möller:** timo.moeller@deepset.ai    
**Julian Risch:** julian.risch@deepset.ai    
**Malte Pietsch:** malte.pietsch@deepset.ai    
**Michel Bartels:** michel.bartels@deepset.ai    

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