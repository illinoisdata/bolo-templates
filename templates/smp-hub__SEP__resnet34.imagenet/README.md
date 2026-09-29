---
library_name: segmentation-models-pytorch
license: other
pipeline_tag: image-classification
tags:
- segmentation-models-pytorch
- image-classification
- pytorch
- resnet
languages:
- python
---

# Model card for resnet34.

This repository contains the `imagenet` pre-trained weights for the `resnet34` model used as 
encoder in the [segmentation-models-pytorch](https://github.com/qubvel-org/segmentation_models.pytorch) library.

### Example usage:

1. Install the library:

```bash
pip install segmentation-models-pytorch
```

2. Use the encoder in your code:

```python
import segmentation_models_pytorch as smp

model = smp.Unet("resnet34", encoder_weights="imagenet")
```

### References

- Github: https://github.com/qubvel/segmentation_models.pytorch
- Docs: https://smp.readthedocs.io/en/latest/
- Original weights URL: https://download.pytorch.org/models/resnet34-333f7ec4.pth