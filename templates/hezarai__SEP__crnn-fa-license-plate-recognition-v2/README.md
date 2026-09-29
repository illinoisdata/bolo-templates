---
language:
- fa
library_name: hezar
tags:
- image-to-text
- hezar
datasets:
- hezarai/persian-license-plate-v1
pipeline_tag: image-to-text
base_model:
- hezarai/crnn-fa-printed-96-long
---
A robust CRNN-based OCR model for license plate recognition (Persian only)(V2). This model is a finetuned version of [hezarai/crnn-fa-printed-96-long](https://huggingface.co/hezarai/crnn-fa-printed-96-long)
on the [Persian license plate dataset (v1)](https://huggingface.co/datasets/hezarai/persian-license-plate-v1).

Note that this model only works on a cropped image of a plate, so you have to run an object(license plate) detection model and pass its output to this model to work.

## Usage
```
pip install hezar
```
```python
from hezar.models import Model

model = Model.load("hezarai/crnn-fa-license-plate-recognition-v2")
plate_text = model.predict("assets/license_plate_ocr_example.jpg")
print(plate_text)  # Persian text of mixed numbers and characters might not show correctly in the console
```
```
['۵۷س۷۷۹۷۷']
```