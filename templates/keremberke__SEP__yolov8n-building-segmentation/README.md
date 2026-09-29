---
tags:
- ultralyticsplus
- yolov8
- ultralytics
- yolo
- vision
- image-segmentation
- pytorch
- awesome-yolov8-models
library_name: ultralytics
library_version: 8.0.21
inference: false

datasets:
- keremberke/satellite-building-segmentation

model-index:
- name: keremberke/yolov8n-building-segmentation
  results:
  - task:
      type: image-segmentation

    dataset:
      type: keremberke/satellite-building-segmentation
      name: satellite-building-segmentation
      split: validation

    metrics:
      - type: precision  # since mAP@0.5 is not available on hf.co/metrics
        value: 0.63834  # min: 0.0 - max: 1.0
        name: mAP@0.5(box)
      - type: precision  # since mAP@0.5 is not available on hf.co/metrics
        value: 0.62845  # min: 0.0 - max: 1.0
        name: mAP@0.5(mask)
---

<div align="center">
  <img width="640" alt="keremberke/yolov8n-building-segmentation" src="https://huggingface.co/keremberke/yolov8n-building-segmentation/resolve/main/thumbnail.jpg">
</div>

### Supported Labels

```
['Building']
```

### How to use

- Install [ultralyticsplus](https://github.com/fcakyon/ultralyticsplus):

```bash
pip install ultralyticsplus==0.0.23 ultralytics==8.0.21
```

- Load model and perform prediction:

```python
from ultralyticsplus import YOLO, render_result

# load model
model = YOLO('keremberke/yolov8n-building-segmentation')

# set model parameters
model.overrides['conf'] = 0.25  # NMS confidence threshold
model.overrides['iou'] = 0.45  # NMS IoU threshold
model.overrides['agnostic_nms'] = False  # NMS class-agnostic
model.overrides['max_det'] = 1000  # maximum number of detections per image

# set image
image = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
results = model.predict(image)

# observe results
print(results[0].boxes)
print(results[0].masks)
render = render_result(model=model, image=image, result=results[0])
render.show()
```

**More models available at: [awesome-yolov8-models](https://yolov8.xyz)**