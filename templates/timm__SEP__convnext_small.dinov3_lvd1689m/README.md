---
tags:
- timm
- transformers
pipeline_tag: image-feature-extraction
library_name: timm
license: other
license_name: dinov3-license
license_link: https://ai.meta.com/resources/models-and-libraries/dinov3-license
---
# Model card for convnext_small.dinov3_lvd1689m

A DINOv3 ConvNeXt image feature model. Pretrained on LVD-1689M with self-supervised DINOv3 method, distilled from DINOv3 ViT-7B.


## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 49.5
  - GMACs: 8.7
  - Activations (M): 21.6
  - Image size: 224 x 224
- **Papers:**
  - DINOv3: https://arxiv.org/abs/2508.10104
  - A ConvNet for the 2020s: https://arxiv.org/abs/2201.03545
  - PyTorch Image Models: https://github.com/huggingface/pytorch-image-models
- **Original:** https://github.com/facebookresearch/dinov3
- **Pretrain Dataset:** LVD-1689M
- **License:** [DINOv3](https://ai.meta.com/resources/models-and-libraries/dinov3-license)

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('convnext_small.dinov3_lvd1689m', pretrained=True)
model = model.eval()

# get model specific transforms (normalization, resize)
data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=False)

output = model(transforms(img).unsqueeze(0))  # unsqueeze single image into batch of 1

top5_probabilities, top5_class_indices = torch.topk(output.softmax(dim=1) * 100, k=5)
```

### Feature Map Extraction
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model(
    'convnext_small.dinov3_lvd1689m',
    pretrained=True,
    features_only=True,
)
model = model.eval()

# get model specific transforms (normalization, resize)
data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=False)

output = model(transforms(img).unsqueeze(0))  # unsqueeze single image into batch of 1

for o in output:
    # print shape of each feature map in output
    # e.g.:
    #  torch.Size([1, 96, 56, 56])
    #  torch.Size([1, 192, 28, 28])
    #  torch.Size([1, 384, 14, 14])
    #  torch.Size([1, 768, 7, 7])

    print(o.shape)
```

### Image Embeddings
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model(
    'convnext_small.dinov3_lvd1689m',
    pretrained=True,
    num_classes=0,  # remove classifier nn.Linear
)
model = model.eval()

# get model specific transforms (normalization, resize)
data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=False)

output = model(transforms(img).unsqueeze(0))  # output is (batch_size, num_features) shaped tensor

# or equivalently (without needing to set num_classes=0)

output = model.forward_features(transforms(img).unsqueeze(0))
# output is unpooled, a (1, 768, 7, 7) shaped tensor

output = model.forward_head(output, pre_logits=True)
# output is a (1, num_features) shaped tensor
```

## Citation
```bibtex
@article{simeoni2025dinov3,
  title={DINOv3},
  author={Sim{'e}oni, Oriane and Vo, Huy V and Seitzer, Maximilian and Baldassarre, Federico and Oquab, Maxime and Jose, Cijo and Khalidov, Vasil and Szafraniec, Marc and Yi, Seungeun and Ramamonjisoa, Micha{"e}l and others},
  journal={arXiv preprint arXiv:2508.10104},
  year={2025}
}
}
```
```bibtex
@article{liu2022convnet,
  author  = {Zhuang Liu and Hanzi Mao and Chao-Yuan Wu and Christoph Feichtenhofer and Trevor Darrell and Saining Xie},
  title   = {A ConvNet for the 2020s},
  journal = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year    = {2022},
}
```
```bibtex
@misc{rw2019timm,
  author = {Ross Wightman},
  title = {PyTorch Image Models},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  doi = {10.5281/zenodo.4414861},
  howpublished = {\url{https://github.com/huggingface/pytorch-image-models}}
}
```