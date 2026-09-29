---
language:
- en
- da
- fr
- it
- es
- de
- pt
- cs
- pl
- nl
- 'no'
- fi
license: apache-2.0
---

<p align="center">
<img src="https://github.com/felixdittrich92/OnnxTR/raw/main/docs/images/logo.jpg" width="40%">
</p>

**Optical Character Recognition made seamless & accessible to anyone, powered by Onnxruntime**

## Task: recognition

https://github.com/felixdittrich92/OnnxTR

### Example usage:

```python
>>> from onnxtr.io import DocumentFile
>>> from onnxtr.models import ocr_predictor, from_hub

>>> img = DocumentFile.from_images(['<image_path>'])
>>> # Load your model from the hub
>>> model = from_hub('onnxtr/my-model')

>>> # Pass it to the predictor
>>> # If your model is a recognition model:
>>> predictor = ocr_predictor(det_arch='db_mobilenet_v3_large',
>>>                           reco_arch=model)

>>> # If your model is a detection model:
>>> predictor = ocr_predictor(det_arch=model,
>>>                           reco_arch='crnn_mobilenet_v3_small')

>>> # Get your predictions
>>> res = predictor(img)
```