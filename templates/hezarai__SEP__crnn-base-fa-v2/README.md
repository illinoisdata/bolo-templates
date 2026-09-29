---
license: apache-2.0
language:
- fa
library_name: hezar
tags:
- hezar
- image-to-text
pipeline_tag: image-to-text
---
A CRNN model for Persian OCR. This model is based on a simple CNN + LSTM architecture inspired by [this paper](https://arxiv.org/abs/1507.05717). 

This is a successor model to our previous model [hezarai/crnn-base-fa-v1](https://huggingface.co/hezarai/crnn-base-fa-v1). 
The improvements include:
- 5X larger dataset
- Change input image size from 64x256 to 32x384
- Increase max output length from 64 to 96 (Max length of the samples in the dataset was 48 to handle CTC loss issues)
- Support numbers and special characters (see id2label in `model_config.yaml`)
- Auto-handling of LTR characters like digits in between the text

Note that this model is only optimized for printed/scanned documents and works best on texts with a length of up to 50-ish characters. (For an end-to-end OCR pipeline, use a text detector model first like https://huggingface.co/hezarai/CRAFT to 
extract text boxes preferrably in word-level and then use this model), but it can be used to be fine-tuned on other domains like license plate or handwritten texts.

#### Usage
```
pip install hezar
```

```python
from hezar.models import Model

crnn = Model.load("hezarai/crnn-base-fa-v2")
texts = crnn.predict(["sample_image.jpg"])
print(texts)
```