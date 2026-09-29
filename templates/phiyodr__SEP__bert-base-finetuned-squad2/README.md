---
language: en
tags:
- pytorch
- question-answering
datasets:
- squad2
metrics:
- exact
- f1
widget:
- text: "What discipline did Winkelmann create?"
  context: "Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. The prophet and founding hero of modern archaeology, Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art."
---

# bert-base-finetuned-squad2

## Model description

This model is based on **[bert-base-uncased](https://huggingface.co/bert-base-uncased)** and was finetuned on **[SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer/)**. The corresponding papers you can found [here (model)](https://arxiv.org/abs/1810.04805) and [here (data)](https://arxiv.org/abs/1806.03822).


## How to use

```python
from transformers.pipelines import pipeline

model_name = "phiyodr/bert-base-finetuned-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
inputs = {
    'question': 'What discipline did Winkelmann create?',
    'context': 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '
}
nlp(inputs)
```



## Training procedure

```
{
	"base_model": "bert-base-uncased",
	"do_lower_case": True,
	"learning_rate": 3e-5,
	"num_train_epochs": 4,
	"max_seq_length": 384,
	"doc_stride": 128,
	"max_query_length": 64,
	"batch_size": 96 
}
```

## Eval results

- Data: [dev-v2.0.json](https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json)
- Script: [evaluate-v2.0.py](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/) (original script from [here](https://github.com/huggingface/transformers/blob/master/examples/question-answering/README.md))

```
{
  "exact": 70.3950138970774,
  "f1": 73.90527661873521,
  "total": 11873,
  "HasAns_exact": 71.4574898785425,
  "HasAns_f1": 78.48808186475087,
  "HasAns_total": 5928,
  "NoAns_exact": 69.33557611438184,
  "NoAns_f1": 69.33557611438184,
  "NoAns_total": 5945
}
```