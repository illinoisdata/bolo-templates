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
# Model card for davit_small.msft_in1k

A DaViT image classification model. Trained on ImageNet-1k by paper authors.

Thanks to [Fredo Guan](https://github.com/fffffgggg54) for bringing the classification backbone to `timm`.


## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 49.7
  - GMACs: 8.8
  - Activations (M): 30.5
  - Image size: 224 x 224
- **Papers:**
  - DaViT: Dual Attention Vision Transformers: https://arxiv.org/abs/2204.03645
- **Original:** https://github.com/dingmyu/davit
- **Dataset:** ImageNet-1k

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(
    urlopen('https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'))

model = timm.create_model('davit_small.msft_in1k', pretrained=True)
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

img = Image.open(
    urlopen('https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'))

model = timm.create_model(
    'davit_small.msft_in1k',
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
    #  torch.Size([1, 768, 7, 7]
    print(o.shape)
```

### Image Embeddings
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(
    urlopen('https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'))

model = timm.create_model(
    'davit_small.msft_in1k',
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

## Model Comparison
### By Top-1

|model                |top1  |top1_err|top5  |top5_err|param_count|img_size|crop_pct|interpolation|
|---------------------|------|--------|------|--------|-----------|--------|--------|-------------|
|davit_base.msft_in1k |84.634|15.366  |97.014|2.986   |87.95      |224     |0.95    |bicubic      |
|davit_small.msft_in1k|84.25 |15.75   |96.94 |3.06    |49.75      |224     |0.95    |bicubic      |
|davit_tiny.msft_in1k |82.676|17.324  |96.276|3.724   |28.36      |224     |0.95    |bicubic      |

## Citation
```bibtex
@inproceedings{ding2022davit,
    title={DaViT: Dual Attention Vision Transformer}, 
    author={Ding, Mingyu and Xiao, Bin and Codella, Noel and Luo, Ping and Wang, Jingdong and Yuan, Lu},
    booktitle={ECCV},
    year={2022},
}
```
