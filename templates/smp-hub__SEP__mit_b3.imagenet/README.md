---
library_name: segmentation-models-pytorch
license: other
pipeline_tag: image-classification
tags:
- segmentation-models-pytorch
- image-classification
- pytorch
- mit
languages:
- python
---

# Model card for mit_b3.

This repository contains the `imagenet` pre-trained weights for the `mit_b3` model used as 
encoder in the [segmentation-models-pytorch](https://github.com/qubvel-org/segmentation_models.pytorch) library.

### Example usage:

1. Install the library:

```bash
pip install segmentation-models-pytorch
```

2. Use the encoder in your code:

```python
import segmentation_models_pytorch as smp

model = smp.Unet("mit_b3", encoder_weights="imagenet")
```

### References

- Github: https://github.com/qubvel/segmentation_models.pytorch
- Docs: https://smp.readthedocs.io/en/latest/
- Original weights URL: https://github.com/qubvel/segmentation_models.pytorch/releases/download/v0.0.2/mit_b3.pth