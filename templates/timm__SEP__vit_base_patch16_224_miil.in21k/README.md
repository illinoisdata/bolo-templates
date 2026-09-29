---
tags:
- image-classification
- timm
- transformers
library_name: timm
license: apache-2.0
datasets:
- imagenet-21k-p
---
# Model card for vit_base_patch16_224_miil.in21k

A Vision Transformer (ViT) image classification model. Trained on ImageNet-21k-P by Alibaba MIIL.


## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 94.4
  - GMACs: 16.9
  - Activations (M): 16.5
  - Image size: 224 x 224
- **Papers:**
  - ImageNet-21K Pretraining for the Masses: https://arxiv.org/abs/2104.10972
  - An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale: https://arxiv.org/abs/2010.11929v2
- **Dataset:** ImageNet-21k-P
- **Original:** https://github.com/Alibaba-MIIL/ImageNet21K

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('vit_base_patch16_224_miil.in21k', pretrained=True)
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
    'vit_base_patch16_224_miil.in21k',
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
@misc{ridnik2021imagenet21k,
  title={ImageNet-21K Pretraining for the Masses}, 
  author={Tal Ridnik and Emanuel Ben-Baruch and Asaf Noy and Lihi Zelnik-Manor},
  year={2021},
  eprint={2104.10972},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```
```bibtex
@article{dosovitskiy2020vit,
  title={An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},
  author={Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and  Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},
  journal={ICLR},
  year={2021}
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
