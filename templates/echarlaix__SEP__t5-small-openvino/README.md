---
language:
- en
- fr
- ro
- de
datasets:
- c4
tags:
- summarization
- translation
- openvino

license: apache-2.0
---

## [t5-small](https://huggingface.co/t5-small) exported to the OpenVINO IR.

## Model description

[T5](https://huggingface.co/docs/transformers/model_doc/t5#t5) is an encoder-decoder model pre-trained on a multi-task mixture of unsupervised and supervised tasks and for which each task is converted into a text-to-text format.

For more information, please take a look at the original paper.

Paper: [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf)

Authors: *Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu*


## Usage example

You can use this model with Transformers *pipeline*.

```python
from transformers import AutoTokenizer, pipeline
from optimum.intel.openvino import OVModelForSeq2SeqLM

model_id = "echarlaix/t5-small-openvino"
model = OVModelForSeq2SeqLM.from_pretrained(model_id, use_cache=False)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Create a pipeline
translation_pipe = pipeline("translation_en_to_fr", model=model, tokenizer=tokenizer)

text = "He never went out without a book under his arm, and he often came back with two."
result = translation_pipe(text)
```