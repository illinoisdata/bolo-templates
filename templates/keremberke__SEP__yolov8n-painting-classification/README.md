---
tags:
- ultralyticsplus
- yolov8
- ultralytics
- yolo
- vision
- image-classification
- pytorch
- awesome-yolov8-models
library_name: ultralytics
library_version: 8.0.21
inference: false

datasets:
- keremberke/painting-style-classification

model-index:
- name: keremberke/yolov8n-painting-classification
  results:
  - task:
      type: image-classification

    dataset:
      type: keremberke/painting-style-classification
      name: painting-style-classification
      split: validation

    metrics:
      - type: accuracy
        value: 0.04928  # min: 0.0 - max: 1.0
        name: top1 accuracy
      - type: accuracy
        value: 0.23688  # min: 0.0 - max: 1.0
        name: top5 accuracy
---

<div align="center">
  <img width="640" alt="keremberke/yolov8n-painting-classification" src="https://huggingface.co/keremberke/yolov8n-painting-classification/resolve/main/thumbnail.jpg">
</div>

### Supported Labels

```
['Abstract_Expressionism', 'Action_painting', 'Analytical_Cubism', 'Art_Nouveau_Modern', 'Baroque', 'Color_Field_Painting', 'Contemporary_Realism', 'Cubism', 'Early_Renaissance', 'Expressionism', 'Fauvism', 'High_Renaissance', 'Impressionism', 'Mannerism_Late_Renaissance', 'Minimalism', 'Naive_Art_Primitivism', 'New_Realism', 'Northern_Renaissance', 'Pointillism', 'Pop_Art', 'Post_Impressionism', 'Realism', 'Rococo', 'Romanticism', 'Symbolism', 'Synthetic_Cubism', 'Ukiyo_e']
```

### How to use

- Install [ultralyticsplus](https://github.com/fcakyon/ultralyticsplus):

```bash
pip install ultralyticsplus==0.0.23 ultralytics==8.0.21
```

- Load model and perform prediction:

```python
from ultralyticsplus import YOLO, postprocess_classify_output

# load model
model = YOLO('keremberke/yolov8n-painting-classification')

# set model parameters
model.overrides['conf'] = 0.25  # model confidence threshold

# set image
image = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
results = model.predict(image)

# observe results
print(results[0].probs) # [0.1, 0.2, 0.3, 0.4]
processed_result = postprocess_classify_output(model, result=results[0])
print(processed_result) # {"cat": 0.4, "dog": 0.6}
```

**More models available at: [awesome-yolov8-models](https://yolov8.xyz)**