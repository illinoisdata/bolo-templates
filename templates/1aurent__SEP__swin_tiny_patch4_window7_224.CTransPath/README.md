---
tags:
- feature-extraction
- image-classification
- timm
- biology
- cancer
- histology
library_name: timm
model-index:
- name: ctranspath
  results:
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: Camelyon16[Meta]
      type: image-classification
    metrics:
    - type: accuracy
      value: 96.3 ± 2.6
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-BRCA[Hist]
      type: image-classification
    metrics:
    - type: accuracy
      value: 95.8 ± 0.5
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-BRCA[HRD]
      type: image-classification
    metrics:
    - type: accuracy
      value: 77.1 ± 2.5
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-BRCA[Mol]
      type: image-classification
    metrics:
    - type: accuracy
      value: 80.8 ± 1.7
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-BRCA[OS]
      type: image-classification
    metrics:
    - type: accuracy
      value: 65.0 ± 6.0
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-CRC[MSI]
      type: image-classification
    metrics:
    - type: accuracy
      value: 88.5 ± 2.3
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-COAD[OS]
      type: image-classification
    metrics:
    - type: accuracy
      value: 64.3 ± 5.4
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-NSCLC[CType]
      type: image-classification
    metrics:
    - type: accuracy
      value: 97.3 ± 0.4
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-LUAD[OS]
      type: image-classification
    metrics:
    - type: accuracy
      value: 59.1 ± 4.5
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-LUSC[OS]
      type: image-classification
    metrics:
    - type: accuracy
      value: 61.5 ± 2.9
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-OV[HRD]
      type: image-classification
    metrics:
    - type: accuracy
      value: 69.5 ± 7.0
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-RCC[CType]
      type: image-classification
    metrics:
    - type: accuracy
      value: 98.9 ± 0.2
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-STAD[MSI]
      type: image-classification
    metrics:
    - type: accuracy
      value: 83.2 ± 8.1 
      name: ROC AUC
      verified: false
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: TCGA-PAAD[OS]
      type: image-classification
    metrics:
    - type: accuracy
      value: 59.0 ± 4.2
      name: ROC AUC
      verified: false
license: gpl-3.0
pipeline_tag: feature-extraction
inference: false
metrics:
- accuracy
---

# Model card for swin_tiny_patch4_window7_224.CTransPath

A Swin Transformer image classification model. \
Trained on 15M histology patches from PAIP and TCGA.

![](https://ars.els-cdn.com/content/image/1-s2.0-S1361841522002043-ga1_lrg.jpg)

## Model Details

- **Model Type:** Feature backbone
- **Model Stats:**
  - Params (M): 27.5
  - Image size: 224 x 224 x 3
- **Papers:**
  - Transformer-based unsupervised contrastive learning for histopathological image classification: https://www.sciencedirect.com/science/article/abs/pii/S1361841522002043
- **Dataset:** TCGA: https://portal.gdc.cancer.gov/
- **Original:** https://github.com/Xiyue-Wang/TransPath
- **License:** [GPLv3](https://github.com/Xiyue-Wang/TransPath/blob/main/LICENSE.md)

## Model Usage

### Custom Patch Embed Layer Definition

```python
from timm.layers.helpers import to_2tuple
import timm
import torch.nn as nn

class ConvStem(nn.Module):
  """Custom Patch Embed Layer.

  Adapted from https://github.com/Xiyue-Wang/TransPath/blob/main/ctran.py#L6-L44
  """

  def __init__(self, img_size=224, patch_size=4, in_chans=3, embed_dim=768, norm_layer=None, **kwargs):
    super().__init__()

    # Check input constraints
    assert patch_size == 4, "Patch size must be 4"
    assert embed_dim % 8 == 0, "Embedding dimension must be a multiple of 8"

    img_size = to_2tuple(img_size)
    patch_size = to_2tuple(patch_size)

    self.img_size = img_size
    self.patch_size = patch_size
    self.grid_size = (img_size[0] // patch_size[0], img_size[1] // patch_size[1])
    self.num_patches = self.grid_size[0] * self.grid_size[1]

    # Create stem network
    stem = []
    input_dim, output_dim = 3, embed_dim // 8
    for l in range(2):
      stem.append(nn.Conv2d(input_dim, output_dim, kernel_size=3, stride=2, padding=1, bias=False))
      stem.append(nn.BatchNorm2d(output_dim))
      stem.append(nn.ReLU(inplace=True))
      input_dim = output_dim
      output_dim *= 2
    stem.append(nn.Conv2d(input_dim, embed_dim, kernel_size=1))
    self.proj = nn.Sequential(*stem)

    # Apply normalization layer (if provided)
    self.norm = norm_layer(embed_dim) if norm_layer else nn.Identity()

  def forward(self, x):
    B, C, H, W = x.shape

    # Check input image size
    assert H == self.img_size[0] and W == self.img_size[1], \
        f"Input image size ({H}*{W}) doesn't match model ({self.img_size[0]}*{self.img_size[1]})."

    x = self.proj(x)
    x = x.permute(0, 2, 3, 1)  # BCHW -> BHWC
    x = self.norm(x)
    return x
```

### Image Embeddings
```python
from urllib.request import urlopen
from PIL import Image
import timm

# get example histology image
img = Image.open(
  urlopen(
    "https://github.com/owkin/HistoSSLscaling/raw/main/assets/example.tif"
  )
)

# load model from the hub
model = timm.create_model(
  model_name="hf-hub:1aurent/swin_tiny_patch4_window7_224.CTransPath",
  embed_layer=ConvStem, #  defined above
  pretrained=True,
).eval()

# get model specific transforms (normalization, resize)
data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=False)

data = transforms(img).unsqueeze(0)  # input is (batch_size, num_channels, img_size, img_size) shaped tensor
output = model(data)  # output is (batch_size, num_features) shaped tensor
```

## Citation
```bibtex
@article{WANG2022102559,
  title    = {Transformer-based unsupervised contrastive learning for histopathological image classification},
  journal  = {Medical Image Analysis},
  volume   = {81},
  pages    = {102559},
  year     = {2022},
  issn     = {1361-8415},
  doi      = {https://doi.org/10.1016/j.media.2022.102559},
  url      = {https://www.sciencedirect.com/science/article/pii/S1361841522002043},
  author   = {Xiyue Wang and Sen Yang and Jun Zhang and Minghui Wang and Jing Zhang and Wei Yang and Junzhou Huang and Xiao Han},
  keywords = {Histopathology, Transformer, Self-supervised learning, Feature extraction},
  abstract = {A large-scale and well-annotated dataset is a key factor for the success of deep learning in medical image analysis. However, assembling such large annotations is very challenging, especially for histopathological images with unique characteristics (e.g., gigapixel image size, multiple cancer types, and wide staining variations). To alleviate this issue, self-supervised learning (SSL) could be a promising solution that relies only on unlabeled data to generate informative representations and generalizes well to various downstream tasks even with limited annotations. In this work, we propose a novel SSL strategy called semantically-relevant contrastive learning (SRCL), which compares relevance between instances to mine more positive pairs. Compared to the two views from an instance in traditional contrastive learning, our SRCL aligns multiple positive instances with similar visual concepts, which increases the diversity of positives and then results in more informative representations. We employ a hybrid model (CTransPath) as the backbone, which is designed by integrating a convolutional neural network (CNN) and a multi-scale Swin Transformer architecture. The CTransPath is pretrained on massively unlabeled histopathological images that could serve as a collaborative local–global feature extractor to learn universal feature representations more suitable for tasks in the histopathology image domain. The effectiveness of our SRCL-pretrained CTransPath is investigated on five types of downstream tasks (patch retrieval, patch classification, weakly-supervised whole-slide image classification, mitosis detection, and colorectal adenocarcinoma gland segmentation), covering nine public datasets. The results show that our SRCL-based visual representations not only achieve state-of-the-art performance in each dataset, but are also more robust and transferable than other SSL methods and ImageNet pretraining (both supervised and self-supervised methods). Our code and pretrained model are available at https://github.com/Xiyue-Wang/TransPath.}
}
```