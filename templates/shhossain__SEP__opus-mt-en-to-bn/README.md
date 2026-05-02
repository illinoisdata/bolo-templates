---
license: apache-2.0
datasets:
- opus100
language:
- bn
- en
metrics:
- sacrebleu
pipeline_tag: translation
widget:
- text: "Will you come home tonight?"
  example_title: "Example 1"
- text: "I am so sorry this is a day late, guys. Unfortunately, my internet was down so it was out of my control."
  example_title: "Example 2"
model-index:
- name: shhossain/opus-mt-en-to-bn
  results:
  - task:
      type: translation
      name: Translation
    dataset:
      type: opus100
      name: opus100
      split: validation       
    metrics:
      - type: Bleu
        value: 12.537400
      - type: Validation Loss
        value: 2.120669
      - type: Training Loss
        value: 1.771200
---

# English-Bengali Translation Model
This model is finetuned on `Helsinki-NLP/opus-mt-en-inc` for English to Bangla Translation.

- **Developed by:** [shhossain](https://github.com/shhossain)
- **Model type:** [transformer-align]
- **Language(s) (NLP):** [English, Bengali]
- **License:** [apache-2.0]
- **Finetuned from model [Helsinki-NLP/opus-mt-en-inc]:** [Helsinki-NLP/opus-mt-en-inc](Helsinki-NLP/opus-mt-en-inc)

## Use with transformers
```python
from transformers import pipeline

pipe = pipeline("translation", model="shhossain/opus-mt-en-to-bn")
```