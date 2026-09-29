---
language:
- fa
- en
library_name: hezar
pipeline_tag: object-detection
tags:
- hezar
---
## CRAFT: Character-Region Awareness For Text detection

CRAFT is a multilingual text detection model. The original implementation is located at https://github.com/clovaai/CRAFT-pytorch. This repo is only compatible 
with the [Hezar](https://github.com/hezarai/hezar) package (**>=v0.40.0**) to perform text detection for Persian but other languages should work too.


### Usage
```
pip install hezar[vision]
```
```python
from hezar.models import Model
from hezar.utils import load_image, draw_boxes, show_image


model = Model.load("hezarai/CRAFT", device="cuda")
image = load_image("../assets/text_detection_example.jpg")
outputs = model.predict(image)
result_image = draw_boxes(image, outputs[0]["boxes"])
show_image(result_image, "text_detected")
```