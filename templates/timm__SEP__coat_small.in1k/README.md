---
tags:
- image-classification
- timm
- transformers
library_name: timm
license: apache-2.0
datasets:
- imagenet-1k
---
# Model card for coat_small.in1k

A CoaT (Co-Scale Conv-Attentional Transformer) image classification model. Trained on ImageNet-1k by paper authors.

## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 21.7
  - GMACs: 12.6
  - Activations (M): 44.3
  - Image size: 224 x 224
- **Papers:**
  - Co-Scale Conv-Attentional Image Transformers: https://arxiv.org/abs/2104.06399
- **Dataset:** ImageNet-1k
- **Original:** https://github.com/mlpc-ucsd/CoaT

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('coat_small.in1k', pretrained=True)
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
    'coat_small.in1k',
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
# output is unpooled, a (torch.Size([1, 785, 320]), torch.Size([1, 197, 320]), torch.Size([1, 50, 320])) shaped tensor

output = model.forward_head(output, pre_logits=True)
# output is a (1, num_features) shaped tensor
```

## Model Comparison
Explore the dataset and runtime metrics of this model in timm [model results](https://github.com/huggingface/pytorch-image-models/tree/main/results).

## Citation
```bibtex
@InProceedings{Xu_2021_ICCV,
  author    = {Xu, Weijian and Xu, Yifan and Chang, Tyler and Tu, Zhuowen},
  title     = {Co-Scale Conv-Attentional Image Transformers},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  month     = {October},
  year      = {2021},
  pages     = {9981-9990}
}
```
