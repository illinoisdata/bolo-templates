---
language: de
datasets:
- deepset/germanquad
license: mit
thumbnail: https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg
tags:
- exbert
---

# gelectra-base distilled for Extractive QA 

## Overview
**Language model:** gelectra-base-germanquad-distilled   
**Language:** German  
**Training data:** GermanQuAD train set (~ 12MB)  
**Eval data:** GermanQuAD test set (~ 5MB)   
**Code:**  See [an example extractive QA pipeline built with Haystack](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline)  
**Infrastructure**: 1x V100 GPU  
**Published**: Apr 21st, 2021

## Details
- We trained a German question answering model with a gelectra-base model as its basis.
- The dataset is GermanQuAD, a new, German language dataset, which we hand-annotated and published [online](https://deepset.ai/germanquad).
- The training dataset is one-way annotated and contains 11518 questions and 11518 answers, while the test dataset is three-way annotated so that there are 2204 questions and with 2204·3−76 = 6536answers, because we removed 76 wrong answers.
- In addition to the annotations in GermanQuAD, haystack's distillation feature was used for training. deepset/gelectra-large-germanquad was used as the teacher model.

See https://deepset.ai/germanquad for more details and dataset download in SQuAD format.

## Hyperparameters
```
batch_size = 24
n_epochs = 6
max_seq_len = 384
learning_rate = 3e-5
lr_schedule = LinearWarmup
embeds_dropout_prob = 0.1
temperature = 2
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

reader = ExtractiveReader(model="deepset/gelectra-base-germanquad-distilled")
reader.warm_up()

question = "What is a popular programming language?"
result = reader.run(query=question, documents=docs)
# {'answers': [ExtractedAnswer(query='What is a popular programming language?', score=0.5740374326705933, data='python', document=Document(id=..., content: '...'), context=None, document_offset=ExtractedAnswer.Span(start=0, end=6),...)]}
```
For a complete example with an extractive question answering pipeline that scales over many documents, check out the [corresponding Haystack tutorial](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline).

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/gelectra-base-germanquad-distilled"

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
We evaluated the extractive question answering performance on our GermanQuAD test set.
Model types and training data are included in the model name. 
For finetuning XLM-Roberta, we use the English SQuAD v2.0 dataset.
The GELECTRA models are warm started on the German translation of SQuAD v1.1 and finetuned on \\\\germanquad. 
The human baseline was computed for the 3-way test set by taking one answer as prediction and the other two as ground truth.
```
"exact": 62.4773139745916
"f1": 80.9488017070188
```
![performancetable](https://lh3.google.com/u/0/d/1IFqkq8OZ7TFnGzxmW6eoxXSYa12f2M7O=w1970-h1546-iv1) 

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
- [deepset Cloud](https://www.deepset.ai/deepset-cloud-product), [deepset Studio](https://www.deepset.ai/deepset-studio)

## Get in touch and join the Haystack community

<p>For more info on Haystack, visit our <strong><a href="https://github.com/deepset-ai/haystack">GitHub</a></strong> repo and <strong><a href="https://docs.haystack.deepset.ai">Documentation</a></strong>. 

We also have a <strong><a class="h-7" href="https://haystack.deepset.ai/community">Discord community open to everyone!</a></strong></p>

[Twitter](https://twitter.com/Haystack_AI) | [LinkedIn](https://www.linkedin.com/company/deepset-ai/) | [Discord](https://haystack.deepset.ai/community) | [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) | [Website](https://haystack.deepset.ai/) | [YouTube](https://www.youtube.com/@deepset_ai)

By the way: [we're hiring!](http://www.deepset.ai/jobs)