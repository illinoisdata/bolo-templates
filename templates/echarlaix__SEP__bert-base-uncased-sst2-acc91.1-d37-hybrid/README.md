---
language: en
license: apache-2.0
tags:
- text-classification
datasets:
- sst2
metrics:
- accuracy
---

## bert-base-uncased model fine-tuned on SST-2

This model was created using the [nn_pruning](https://github.com/huggingface/nn_pruning) python library: the linear layers contains **37%** of the original  weights.

The model contains **51%** of the original weights **overall** (the embeddings account for a significant part of the model, and they are not pruned by this method).

<div class="graph"><script src="/echarlaix/bert-base-uncased-sst2-acc91.1-d37-hybrid/raw/main/model_card/density_info.js" id="2d0fc334-fe98-4315-8890-d6eaca1fa9be"></script></div>

In terms of perfomance, its **accuracy** is **91.17**.

## Fine-Pruning details
This model was fine-tuned from the HuggingFace [model](https://huggingface.co/bert-base-uncased) checkpoint on task, and distilled from the model [textattack/bert-base-uncased-SST-2](https://huggingface.co/textattack/bert-base-uncased-SST-2).
This model is case-insensitive: it does not make a difference between english and English.

A side-effect of the block pruning method is that some of the attention heads are completely removed: 88 heads were removed on a total of 144 (61.1%).
Here is a detailed view on how the remaining heads are distributed in the network after pruning.
<div class="graph"><script src="/echarlaix/bert-base-uncased-sst2-acc91.1-d37-hybrid/raw/main/model_card/pruning_info.js" id="93b19d7f-c11b-4edf-9670-091e40d9be25"></script></div>

## Details of the SST-2 dataset

| Dataset  | Split | # samples |
| -------- | ----- | --------- |
|  SST-2   | train |    67K    |
|  SST-2   | eval  |    872    |

### Results

**Pytorch model file size**: `351MB` (original BERT: `420MB`)

| Metric | # Value   | # Original ([Table 2](https://www.aclweb.org/anthology/N19-1423.pdf))| Variation |
| ------ | --------- | --------- | --------- |
| **accuracy** | **91.17** | **92.7** | **-1.53**|


## Example Usage
Install nn_pruning: it contains the optimization script, which just pack the linear layers into smaller ones by removing empty rows/columns.

`pip install nn_pruning`

Then you can use the `transformers library` almost as usual: you just have to call `optimize_model` when the pipeline has loaded.

```python
from transformers import pipeline
from nn_pruning.inference_model_patcher import optimize_model

cls_pipeline = pipeline(
    "text-classification",
    model="echarlaix/bert-base-uncased-sst2-acc91.1-d37-hybrid",
    tokenizer="echarlaix/bert-base-uncased-sst2-acc91.1-d37-hybrid",
)

print(f"Parameters count (includes only head pruning, no feed forward pruning)={int(cls_pipeline.model.num_parameters() / 1E6)}M")
cls_pipeline.model = optimize_model(cls_pipeline.model, "dense")
print(f"Parameters count after optimization={int(cls_pipeline.model.num_parameters() / 1E6)}M")
predictions = cls_pipeline("This restaurant is awesome")
print(predictions)
```
