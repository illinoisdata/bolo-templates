---
license: apache-2.0
library_name: timm
tags:
- image-classification
- timm
- transformers
datasets:
- imagenet-1k
- imagenet-22k
---
# Model card for deit3_base_patch16_224.fb_in22k_ft_in1k

A DeiT-III image classification model. Pretrained on ImageNet-22k and fine-tuned on ImageNet-1k by paper authors.

## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 86.6
  - GMACs: 17.6
  - Activations (M): 23.9
  - Image size: 224 x 224
- **Papers:**
  - DeiT III: Revenge of the ViT: https://arxiv.org/abs/2204.07118
- **Original:** https://github.com/facebookresearch/deit
- **Dataset:** ImageNet-1k
- **Pretrain Dataset:** ImageNet-22k

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('deit3_base_patch16_224.fb_in22k_ft_in1k', pretrained=True)
model = model.eval()

# get model specific transforms (normalization, resize)
data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=False)

output = model(transforms(img).unsqueeze(0))  # unsqueeze single image into batch of 1

top5_probabilities, top5_class_indices = torch.topk(output.softmax(dim=1) * 100, k=5)
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
    'deit3_base_patch16_224.fb_in22k_ft_in1k',
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
# output is unpooled, a (1, 197, 768) shaped tensor

output = model.forward_head(output, pre_logits=True)
# output is a (1, num_features) shaped tensor
```

## Model Comparison
Explore the dataset and runtime metrics of this model in timm [model results](https://github.com/huggingface/pytorch-image-models/tree/main/results).

## Citation
```bibtex
@article{Touvron2022DeiTIR,
  title={DeiT III: Revenge of the ViT},
  author={Hugo Touvron and Matthieu Cord and Herve Jegou},
  journal={arXiv preprint arXiv:2204.07118},
  year={2022},
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
