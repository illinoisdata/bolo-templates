---
pipeline_tag: text-generation
---
# Factual Consistency Evaluator/Metric in ACL 2023 paper

*[WeCheck: Strong Factual Consistency Checker via Weakly Supervised Learning
](https://arxiv.org/abs/2212.10057)*

Open-sourced code: https://github.com/nightdessert/WeCheck
## Model description
WeCheck is a factual consistency metric trained from weakly annotated samples.

This WeCheck checkpoint can be used to check the following three generation tasks:

**Text Summarization/Knowlege grounded dialogue Generation/Paraphrase**

This WeCheck checkpoint is trained based on the following three weak labler:

*[QAFactEval
](https://github.com/salesforce/QAFactEval)* / *[Summarc](https://github.com/tingofurro/summac)* / *[NLI warmup](https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli)* 
---

# How to use the model
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model_name = "nightdessert/WeCheck"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
premise = "I first thought that I liked the movie, but upon second thought it was actually disappointing." # Input for Summarization/ Dialogue / Paraphrase
hypothesis = "The movie was not good." # Output for Summarization/ Dialogue / Paraphrase
input = tokenizer(premise, hypothesis, truncation=True, return_tensors="pt", truncation_strategy="only_first", max_length=512)
output = model(input["input_ids"].to(device))['logits'][:,0]  # device = "cuda:0" or "cpu"
prediction = torch.sigmoid(output).tolist()
print(prediction) #0.884
```
or apply for a batch of samples
```python
premise = ["I first thought that I liked the movie, but upon second thought it was actually disappointing."]*3 # Input list for Summarization/ Dialogue / Paraphrase
hypothesis = ["The movie was not good."]*3 # Output list for Summarization/ Dialogue / Paraphrase
batch_tokens = tokenizer.batch_encode_plus(list(zip(premise, hypothesis)), padding=True, 
            truncation=True, max_length=512, return_tensors="pt", truncation_strategy="only_first")
output = model(batch_tokens["input_ids"].to(device))['logits'][:,0]  # device = "cuda:0" or "cpu"
prediction = torch.sigmoid(output).tolist()
print(prediction) #[0.884,0.884,0.884]
```


license: openrail
pipeline_tag: text-classification
tags:
- Factual Consistency
- Natrual Language Inference
---
language:
- en
tags:
- Factual Consistency Evaluation