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
- keremberke/chest-xray-classification

model-index:
- name: keremberke/yolov8s-chest-xray-classification
  results:
  - task:
      type: image-classification

    dataset:
      type: keremberke/chest-xray-classification
      name: chest-xray-classification
      split: validation

    metrics:
      - type: accuracy
        value: 0.94158  # min: 0.0 - max: 1.0
        name: top1 accuracy
      - type: accuracy
        value: 1  # min: 0.0 - max: 1.0
        name: top5 accuracy
---

<div align="center">
  <img width="640" alt="keremberke/yolov8s-chest-xray-classification" src="https://huggingface.co/keremberke/yolov8s-chest-xray-classification/resolve/main/thumbnail.jpg">
</div>

### Supported Labels

```
['NORMAL', 'PNEUMONIA']
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
model = YOLO('keremberke/yolov8s-chest-xray-classification')

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