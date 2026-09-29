---
license: apache-2.0
tags:
- medical
- vision
---
# Model Card for MedSAM

MedSAM is a fine-tuned version of [SAM](https://huggingface.co/docs/transformers/main/model_doc/sam) for the medical domain.

This repository is based on the paper, code and pre-trained model released by the authors in July 2023.

## Model Description

MedSAM was trained on a large-scale medical image segmentation dataset of 1,090,486 image-mask pairs collected from different publicly available sources. 
The image-mask pairs cover 15 imaging modalities and over 30 cancer types.

MedSAM was initialized using the pre-trained SAM model with the ViT-Base backbone. The prompt encoder weights were frozen, while the image encoder and mask decoder weights were updated during training. 
The training was performed for 100 epochs with a batch size of 160 using the AdamW optimizer with a learning rate of 10−4 and a weight decay of 0.01. 

- **Repository:** [MedSAM Official GitHub Repository](https://github.com/bowang-lab/medsam)
- **Paper:** [Segment Anything in Medical Images](https://arxiv.org/abs/2304.12306v1)

## Usage

```python
import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformers import SamModel, SamProcessor
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = SamModel.from_pretrained("flaviagiammarino/medsam-vit-base").to(device)
processor = SamProcessor.from_pretrained("flaviagiammarino/medsam-vit-base")

img_url = "https://huggingface.co/flaviagiammarino/medsam-vit-base/resolve/main/scripts/input.png"
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")
input_boxes = [95., 255., 190., 350.]

inputs = processor(raw_image, input_boxes=[[input_boxes]], return_tensors="pt").to(device)
outputs = model(**inputs, multimask_output=False)
probs = processor.image_processor.post_process_masks(outputs.pred_masks.sigmoid().cpu(), inputs["original_sizes"].cpu(), inputs["reshaped_input_sizes"].cpu(), binarize=False)

def show_mask(mask, ax, random_color):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([251/255, 252/255, 30/255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)

def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor="blue", facecolor=(0, 0, 0, 0), lw=2))

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(np.array(raw_image))
show_box(input_boxes, ax[0])
ax[0].set_title("Input Image and Bounding Box")
ax[0].axis("off")
ax[1].imshow(np.array(raw_image))
show_mask(mask=probs[0] > 0.5, ax=ax[1], random_color=False)
show_box(input_boxes, ax[1])
ax[1].set_title("MedSAM Segmentation")
ax[1].axis("off")
plt.show()
```
![results](scripts/output.png)

## Additional Information

### Licensing Information
The authors have released the model code and pre-trained checkpoint under the [Apache License 2.0](https://github.com/bowang-lab/MedSAM/blob/main/LICENSE).

### Citation Information
```
@article{ma2023segment,
  title={Segment anything in medical images},
  author={Ma, Jun and Wang, Bo},
  journal={arXiv preprint arXiv:2304.12306},
  year={2023}
}
```