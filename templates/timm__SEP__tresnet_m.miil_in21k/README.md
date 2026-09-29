---
tags:
- image-classification
- timm
- transformers
library_name: timm
license: apache-2.0
---
# Model card for tresnet_m.miil_in21k

A TResNet image classification model. Trained on ImageNet-21K-P ("ImageNet-21K Pretraining for the Masses", a 11k subset of ImageNet-22k) by paper authors.

The weights for this model have been remapped and modified from the originals to work with standard BatchNorm instead of InplaceABN. `inplace_abn` can be problematic to build recently and ends up slower with `memory_format=channels_last`, torch.compile(), etc.

## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 52.3
  - GMACs: 5.8
  - Activations (M): 7.3
  - Image size: 224 x 224
- **Papers:**
  - TResNet: High Performance GPU-Dedicated Architecture: https://arxiv.org/abs/2003.13630
  - ImageNet-21K Pretraining for the Masses: https://arxiv.org/abs/2104.10972
- **Pretrain Dataset:** ImageNet-21K-P
- **Original:**
  - https://github.com/Alibaba-MIIL/TResNet
  - https://github.com/Alibaba-MIIL/ImageNet21K

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('tresnet_m.miil_in21k', pretrained=True)
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
    'tresnet_m.miil_in21k',
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
    #  torch.Size([1, 64, 56, 56])
    #  torch.Size([1, 128, 28, 28])
    #  torch.Size([1, 1024, 14, 14])
    #  torch.Size([1, 2048, 7, 7])

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
    'tresnet_m.miil_in21k',
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
# output is unpooled, a (1, 2048, 7, 7) shaped tensor

output = model.forward_head(output, pre_logits=True)
# output is a (1, num_features) shaped tensor
```

## Citation
```bibtex
@misc{ridnik2020tresnet,
    title={TResNet: High Performance GPU-Dedicated Architecture},
    author={Tal Ridnik and Hussam Lawen and Asaf Noy and Itamar Friedman},
    year={2020},
    eprint={2003.13630},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```
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
