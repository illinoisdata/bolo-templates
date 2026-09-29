---
tags:
- pytorch_model_hub_mixin
- model_hub_mixin
license: apache-2.0
---
# NemoCurator Quality Classifier DeBERTa

# Model Overview
This is a text classification model that can enable qualitative data annotation, creation of quality-specific blends and addition of metadata tags. The model classifies documents into one of three classes based on the quality of the document: "High", "Medium", "Low"

The model was trained using data annotated by human annotators, who considered quality factors such as content accuracy, clarity, coherence, grammar, depth of information, and overall usefulness of the document.

This model is used in the [NVIDIA NeMo Curator](https://github.com/NVIDIA-NeMo/Curator) as part of the qualitative filtering module.
# Model Architecture
The model architecture is Deberta V3 Base
Context length is 1024 tokens
# Training (details)
## Training data:
The training set is 22828 Common Crawl text samples, labeled as "High", "Medium", "Low". Here are some examples:
1. Input: 
    ```
    Volunteering

    It's all about the warm, fuzzy feeling when you serve the community, without expectation of gain. Volunteering offers you the necessary experience and development skills to take forward with you, as you venture out to work with other people and apply what you learn, to achieve your career goals.

    HOW IT WORKS

    SEARCH

    BOOK NOW

    ENJOY THE SHOW

    GET A FREE QUOTE

    Planning your event ahead of time is the right move. Contact our experts and let us surprise you.
    ```
    Output: `Low`
1. Input:
    ```
    Sharapova has been in New Zealand since well before the New Year, preparing for her 2011 start and requested the opening day match to test her form. "My last tournament was over two months ago and it will be really good to get back playing again."

    "My priority since I have been here has been to adjust to time and conditions. I have had a couple of practices a day and think that has been really important."

    The three-time Grand Slam champion who once stood number one next plays Voracova after winning their only previous match in 2003.
    ```
    Output: `High`


# How To Use This Model
## Input
The model takes one or several paragraphs of text as input.

Example input:
```
Reasons to visit Thatta

Thatta is one of the most important cities of the province of Sindh, Pakistan. Historically it is the richest city. The sands of Thatta have seen many great men. It provided Alexander the Great and his troops a comfortable resting place before they moved further. It welcomed the Mughal Emperor Shah Jehan.
```
## Output
The model outputs one of the 3 classes as the predicted quality for each input sample.

Example output:
```
Medium
```

# How to use in NeMo Curator

The inference code is available on [NeMo Curator's GitHub repository](https://github.com/NVIDIA-NeMo/Curator). Check out this [example notebook](https://github.com/NVIDIA-NeMo/Curator/blob/main/tutorials/text/distributed-data-classification/quality-classification.ipynb) to get started.

# How to use in transformers
To use the quality classifier, use the following code:

```python
import torch
from torch import nn
from transformers import AutoModel, AutoTokenizer, AutoConfig
from huggingface_hub import PyTorchModelHubMixin


class QualityModel(nn.Module, PyTorchModelHubMixin):
    def __init__(self, config):
        super(QualityModel, self).__init__()
        self.model = AutoModel.from_pretrained(config["base_model"])
        self.dropout = nn.Dropout(config["fc_dropout"])
        self.fc = nn.Linear(self.model.config.hidden_size, len(config["id2label"]))

    def forward(self, input_ids, attention_mask):
        features = self.model(
            input_ids=input_ids, attention_mask=attention_mask
        ).last_hidden_state
        dropped = self.dropout(features)
        outputs = self.fc(dropped)
        return torch.softmax(outputs[:, 0, :], dim=1)


device = "cuda" if torch.cuda.is_available() else "cpu"

# Setup configuration and model
config = AutoConfig.from_pretrained("nvidia/quality-classifier-deberta")
tokenizer = AutoTokenizer.from_pretrained("nvidia/quality-classifier-deberta")
model = QualityModel.from_pretrained("nvidia/quality-classifier-deberta").to(device)
model.eval()

# Prepare and process inputs
text_samples = [".?@fdsa Low quality text.", "This sentence is ok."]
inputs = tokenizer(
    text_samples, return_tensors="pt", padding="longest", truncation=True
).to(device)
outputs = model(inputs["input_ids"], inputs["attention_mask"])

# Predict and display results
predicted_classes = torch.argmax(outputs, dim=1)
predicted_domains = [
    config.id2label[class_idx.item()] for class_idx in predicted_classes.cpu().numpy()
]
print(predicted_domains)
# ['Low', 'Medium']
```

# Evaluation Benchmarks
## Evaluation data

The evaluation data is a subset of training data where all three annotators agree on the label. It has 7128 samples.

## Results
Accuracy score on evaluation set with 7128 samples - `0.8252`


|        | Precision | Recall | F1-Score |
|--------|-----------|--------|----------|
| High   | 0.5043    | 0.1776 | 0.2626   |
| Medium | 0.8325    | 0.9396 | 0.8825   |
| Low    | 0.8510    | 0.7279 | 0.7842   |


Confusion Matrix: 

We verify that the predicted scores are indeed close to their ground truth, and are due to the noisy nature of the annotation.

|         | High | Medium | Low |
|---------|------|--------|-----|
| High    | 117  | 541    | 1   |
| Medium  | 115  | 4688   | 187 |
| Low     | 0    | 402    | 1077|

# Limitations
- Subjectivity in Quality: Quality assessment is inherently subjective and may vary among different annotators.

# References
- https://arxiv.org/abs/2111.09543
- https://github.com/microsoft/DeBERTa
# License
License to use this model is covered by the Apache 2.0. By downloading the public and release version of the model, you accept the terms and conditions of the Apache License 2.0.
This repository contains the code for the domain classifier model.