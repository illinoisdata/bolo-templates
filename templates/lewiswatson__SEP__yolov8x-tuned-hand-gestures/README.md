---
license: cc-by-4.0
library_name: ultralytics
pipeline_tag: object-detection
inference: false
tags:
- roboflow
- hand_gesture
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- Ultralytics/YOLOv8
---

# Yolov8x Tuned to Hand Gestures

Yolo v8x Finetuned on the [hand gestures roboflow dataset.](https://universe.roboflow.com/hand-gestures-recognition/hand-gestures-dataset)


## Inference
```py
from ultralyticsplus import YOLO, render_result

# load model
model = YOLO('lewiswatson/yolov8x-tuned-hand-gestures')

# set image
image = 'https://thumbs.dreamstime.com/b/young-man-showing-peace-sign-isolated-over-yellow-background-133210696.jpg'

# perform inference
results = model.predict(image)

# observe results
print(results[0].boxes)
render = render_result(model=model, image=image, result=results[0])
render.show()
```

## Training Parameters

Trained using [Ultralytics](https://ultralytics.com/) and [Ultralyticsplus](https://pypi.org/project/ultralyticsplus/).

- Epochs: 10
- Optimiser: SGD
- Patience 50
- Imgsz: 640
- Batch: -1