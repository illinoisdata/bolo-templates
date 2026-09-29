---
license: apache-2.0
library_name: timm
tags:
- image-classification
- timm
- transformers
datasets:
- imagenet-1k
---
# Model card for efficientformerv2_s0.snap_dist_in1k

A EfficientFormer-V2 image classification model. Pretrained with distillation on ImageNet-1k.

## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 3.6
  - GMACs: 0.4
  - Activations (M): 5.3
  - Image size: 224 x 224
- **Original:** https://github.com/snap-research/EfficientFormer
- **Papers:**
  - Rethinking Vision Transformers for MobileNet Size and Speed: https://arxiv.org/abs/2212.08059
- **Dataset:** ImageNet-1k

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(
    urlopen('https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'))

model = timm.create_model('efficientformerv2_s0.snap_dist_in1k', pretrained=True)
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

img = Image.open(
    urlopen('https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'))

model = timm.create_model(
    'efficientformerv2_s0.snap_dist_in1k',
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
# output is unpooled (ie.e a (batch_size, num_features, H, W) tensor

output = model.forward_head(output, pre_logits=True)
# output is (batch_size, num_features) tensor
```

### Feature Map Extraction
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(
    urlopen('https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'))

model = timm.create_model(
    'efficientformerv2_s0.snap_dist_in1k',
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
    # e.g. for efficientformerv2_l: 
    # torch.Size([2, 40, 56, 56])
    # torch.Size([2, 80, 28, 28])
    # torch.Size([2, 192, 14, 14])
    # torch.Size([2, 384, 7, 7])
    print(o.shape)
```

## Model Comparison
|model                              |top1  |top5  |param_count|img_size|
|-----------------------------------|------|------|-----------|--------|
|efficientformerv2_l.snap_dist_in1k |83.628|96.54 |26.32      |224     |
|efficientformer_l7.snap_dist_in1k  |83.368|96.534|82.23      |224     |
|efficientformer_l3.snap_dist_in1k  |82.572|96.24 |31.41      |224     |
|efficientformerv2_s2.snap_dist_in1k|82.128|95.902|12.71      |224     |
|efficientformer_l1.snap_dist_in1k  |80.496|94.984|12.29      |224     |
|efficientformerv2_s1.snap_dist_in1k|79.698|94.698|6.19       |224     |
|efficientformerv2_s0.snap_dist_in1k|76.026|92.77 |3.6        |224     |

## Citation
```bibtex
@article{li2022rethinking,
  title={Rethinking Vision Transformers for MobileNet Size and Speed},
  author={Li, Yanyu and Hu, Ju and Wen, Yang and Evangelidis, Georgios and Salahi, Kamyar and Wang, Yanzhi and Tulyakov, Sergey and Ren, Jian},
  journal={arXiv preprint arXiv:2212.08059},
  year={2022}
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
  howpublished = {\url{https://github.com/rwightman/pytorch-image-models}}
}
```
