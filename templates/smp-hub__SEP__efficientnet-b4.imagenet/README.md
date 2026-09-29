---
library_name: segmentation-models-pytorch
license: other
pipeline_tag: image-classification
tags:
- segmentation-models-pytorch
- image-classification
- pytorch
- efficientnet
languages:
- python
---

# Model card for efficientnet-b4.

This repository contains the `imagenet` pre-trained weights for the `efficientnet-b4` model used as 
encoder in the [segmentation-models-pytorch](https://github.com/qubvel-org/segmentation_models.pytorch) library.

### Example usage:

1. Install the library:

```bash
pip install segmentation-models-pytorch
```

2. Use the encoder in your code:

```python
import segmentation_models_pytorch as smp

model = smp.Unet("efficientnet-b4", encoder_weights="imagenet")
```

### References

- Github: https://github.com/qubvel/segmentation_models.pytorch
- Docs: https://smp.readthedocs.io/en/latest/
- Original weights URL: https://github.com/lukemelas/EfficientNet-PyTorch/releases/download/1.0/efficientnet-b4-6ed6700e.pth