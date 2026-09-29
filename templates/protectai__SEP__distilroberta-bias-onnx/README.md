---
pipeline_tag: text-classification
language: en
datasets:
- valurank/wikirev-bias
inference: false
tags:
- bias
- distilroberta
base_model: valurank/distilroberta-bias
---

> [!WARNING]
> **THIS PROJECT HAS BEEN ARCHIVED.**
> 
> This project and its associated code on [GitHub](https://github.com/protectai/llm-guard) are no longer under active development or maintained.

# ONNX version of valurank/distilroberta-bias

**This model is a conversion of [valurank/distilroberta-bias](https://huggingface.co/valurank/distilroberta-bias) to ONNX** format. It is designed to detect biases in text using the distilled version of the RoBERTa model. The model was converted to ONNX using the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library.

## Model Architecture

**Base Model**: DistilRoBERTa, a distilled version of the RoBERTa model that is optimized for faster performance while maintaining similar accuracy.

**Modifications**: The model is converted to ONNX format with no additional changes.

## Usage

### Optimum

Loading the model requires the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library installed.

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline


tokenizer = AutoTokenizer.from_pretrained("laiyer/distilroberta-bias-onnx")
model = ORTModelForSequenceClassification.from_pretrained("laiyer/distilroberta-bias-onnx")
classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
)

classifier_output = classifier("Your text to analyze for bias.")
score = (classifier_output[0]["score"] if classifier_output[0]["label"] == "BIASED" else 1 - classifier_output[0]["score"])
```

### LLM Guard

[Bias scanner](https://llm-guard.com/output_scanners/bias/)

## Community

Join our Slack to give us feedback, connect with the maintainers and fellow users, ask questions, 
or engage in discussions about LLM security!

<a href="https://join.slack.com/t/laiyerai/shared_invite/zt-28jv3ci39-sVxXrLs3rQdaN3mIl9IT~w"><img src="https://github.com/laiyer-ai/llm-guard/blob/main/docs/assets/join-our-slack-community.png?raw=true" width="200"></a>
