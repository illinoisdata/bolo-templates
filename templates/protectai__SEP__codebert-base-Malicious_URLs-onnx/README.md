---
language:
- en
pipeline_tag: text-classification
base_model: DunnBC22/codebert-base-Malicious_URLs
inference: false
datasets:
- sid321axn/malicious-urls-dataset
tags:
- malicious-urls
- url
---

> [!WARNING]
> **THIS PROJECT HAS BEEN ARCHIVED.**
> 
> This project and its associated code on [GitHub](https://github.com/protectai/llm-guard) are no longer under active development or maintained.

# ONNX version of DunnBC22/codebert-base-Malicious_URLs

**This model is a conversion of [DunnBC22/codebert-base-Malicious_URLs](https://huggingface.co/DunnBC22/codebert-base-Malicious_URLs) to ONNX** format. It's based on the CodeBERT architecture, tailored for the specific task of identifying URLs that may pose security threats. The model was converted to ONNX using the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library.

## Model Architecture

**Base Model**: CodeBERT-base, a robust model for programming and natural languages.

**Dataset**: [https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset).

**Modifications**: Details of any modifications or fine-tuning done to tailor the model for malicious URL detection.

## Usage

Loading the model requires the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library installed.

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline


tokenizer = AutoTokenizer.from_pretrained("laiyer/codebert-base-Malicious_URLs-onnx")
model = ORTModelForSequenceClassification.from_pretrained("laiyer/codebert-base-Malicious_URLs-onnx")
classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=None,
)

classifier_output = classifier("https://google.com")
print(classifier_output)
```

### LLM Guard

[Malicious URLs scanner](https://llm-guard.com/output_scanners/malicious_urls/)

## Community

Join our Slack to give us feedback, connect with the maintainers and fellow users, ask questions, 
or engage in discussions about LLM security!

<a href="https://join.slack.com/t/laiyerai/shared_invite/zt-28jv3ci39-sVxXrLs3rQdaN3mIl9IT~w"><img src="https://github.com/laiyer-ai/llm-guard/blob/main/docs/assets/join-our-slack-community.png?raw=true" width="200"></a>
