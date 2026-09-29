---
license: apache-2.0
tags:
- object-detection
- ultralytics
- yolov8
- pytorch
- pickle
pipeline_tag: object-detection
library_name: ultralytics
library_version: 8.0.198
model-index:
    - name: arnabdhar/YOLOv8-nano-aadhar-card
      results:
        - task:
            type: object-detection
          metrics:
            - type: precision
              value: 0.963
              name: mAP@50
            - type: precision
              value: 0.748 
              name: mAP@50-95

---
# YOLOv8 model to detect import texts on an Aadhar Card

## Overview

Aadhaar Card text detection is the process of identifying and extracting text from Aadhaar Card images. This can be useful for a variety of applications, such as automatic data entry, fraud detection, and document verification.

One approach to Aadhaar Card text detection is to use YOLOv8, a state-of-the-art object detection model. YOLOv8 can be trained to detect a variety of object classes, including text. Once trained, YOLOv8 can be used to detect text in Aadhaar Card images and extract the text to a text file or other format.

## Inference

### Supported Labels

```python
# label_id: label_name
{0: "AADHAR_NUMBER", 1: "DATE_OF_BIRTH", 2: "GENDER", 3: "NAME", 4: "ADDRESS"}
```

### Install Dependencies

```bash
$ pip install ultralytics huggingface_hub supervision
```

### Load the model

```python
from ultralytics import YOLO
from huggingface_hub import hf_hub_download
from supervision import Detections

# repo details
repo_config = dict(
    repo_id = "arnabdhar/YOLOv8-nano-aadhar-card",
    filename = "model.pt",
    local_dir = "./models"
)

# load model
model = YOLO(hf_hub_download(**repo_config))

# get id to label mapping
id2label = model.names
print(id2label)

# Perform Inference
image_url = "https://i.pinimg.com/originals/08/6d/82/086d820550f34066764f4047ddc263ca.jpg"

detections = Detections.from_ultralytics(model.predict(image_url)[0])

print(detections)

```

## Fine Tuning

 The following hyperparameters were used to finetune the model

```yaml
model: yolov8n.pt
batch: 4
epochs: 100
optimizer: AdamW
warmup_epochs: 15
seed: 42
imgsz: 640
```

The following evaluation metrics were achieved by `best.pt` for bounding box predictions:

```yaml
recall: 0.962
precision: 0.973
mAP50: 0.963
mAP50_95: 0.748 
```


## Dataset

+ __Source__: Roboflow Universe
+ __Dataset URL__: https://universe.roboflow.com/jizo/aadhar-card-entity-detection