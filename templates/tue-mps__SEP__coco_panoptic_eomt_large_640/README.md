---
library_name: transformers
license: mit
tags:
- vision
- image-segmentation
- pytorch
---
# EoMT

[![PyTorch](https://img.shields.io/badge/PyTorch-DE3412?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org/)

**EoMT (Encoder-only Mask Transformer)** is a Vision Transformer (ViT) architecture designed for high-quality and efficient image segmentation. It was introduced in the CVPR 2025 highlight paper:  
**[Your ViT is Secretly an Image Segmentation Model](https://www.tue-mps.org/eomt)**  
by Tommie Kerssies, Niccolò Cavagnero, Alexander Hermans, Narges Norouzi, Giuseppe Averta, Bastian Leibe, Gijs Dubbelman, and Daan de Geus.

> **Key Insight**: Given sufficient scale and pretraining, a plain ViT along with additional few params can perform segmentation without the need for task-specific decoders or pixel fusion modules. The same model backbone supports semantic, instance, and panoptic segmentation with different post-processing 🤗

The original implementation can be found in this [repository](https://github.com/tue-mps/eomt).

The HuggingFace model page is available at this [link](https://huggingface.co/papers/2503.19108).

---


### How to use

Here is how to use this model for Panotpic Segmentation:

```python
import matplotlib.pyplot as plt
import requests
import torch
from PIL import Image

from transformers import EomtForUniversalSegmentation, AutoImageProcessor


model_id = "tue-mps/coco_panoptic_eomt_large_640"
processor = AutoImageProcessor.from_pretrained(model_id)
model = EomtForUniversalSegmentation.from_pretrained(model_id)

image = Image.open(requests.get("http://images.cocodataset.org/val2017/000000039769.jpg", stream=True).raw)

inputs = processor(
    images=image,
    return_tensors="pt",
)

with torch.inference_mode():
    outputs = model(**inputs)

# Prepare the original image size in the format (height, width)
target_sizes = [(image.height, image.width)]

# Post-process the model outputs to get final segmentation prediction
preds = processor.post_process_panoptic_segmentation(
    outputs,
    target_sizes=target_sizes,
)

# Visualize the panoptic segmentation mask
plt.imshow(preds[0]["segmentation"])
plt.axis("off")
plt.title("Panoptic Segmentation")
plt.show()
```

## Citation
If you find our work useful, please consider citing us as:
```bibtex
@inproceedings{kerssies2025eomt,
  author    = {Kerssies, Tommie and Cavagnero, Niccolò and Hermans, Alexander and Norouzi, Narges and Averta, Giuseppe and Leibe, Bastian and Dubbelman, Gijs and de Geus, Daan},
  title     = {Your ViT is Secretly an Image Segmentation Model},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2025},
}
```
