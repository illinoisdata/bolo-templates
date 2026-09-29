---
tags:
- image-classification
- timm
- transformers
library_name: timm
license: mit
datasets:
- imagenet-1k
---
# Model card for edgenext_small.usi_in1k

An EdgeNeXt image classification model. Trained on ImageNet-1k by paper authors using distillation (`USI` as per `Solving ImageNet`).

## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 5.6
  - GMACs: 1.3
  - Activations (M): 9.1
  - Image size: train = 256 x 256, test = 320 x 320
- **Papers:**
  - EdgeNeXt: Efficiently Amalgamated CNN-Transformer Architecture for Mobile Vision Applications: https://arxiv.org/abs/2206.10589
  - Solving ImageNet: a Unified Scheme for Training any Backbone to Top Results: https://arxiv.org/abs/2204.03475
- **Dataset:** ImageNet-1k
- **Original:** https://github.com/mmaaz60/EdgeNeXt

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('edgenext_small.usi_in1k', pretrained=True)
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
    'edgenext_small.usi_in1k',
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
    #  torch.Size([1, 48, 64, 64])
    #  torch.Size([1, 96, 32, 32])
    #  torch.Size([1, 160, 16, 16])
    #  torch.Size([1, 304, 8, 8])

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
    'edgenext_small.usi_in1k',
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
# output is unpooled, a (1, 304, 8, 8) shaped tensor

output = model.forward_head(output, pre_logits=True)
# output is a (1, num_features) shaped tensor
```

## Citation
```bibtex
@inproceedings{Maaz2022EdgeNeXt,
  title={EdgeNeXt: Efficiently Amalgamated CNN-Transformer Architecture for Mobile Vision Applications},
    author={Muhammad Maaz and Abdelrahman Shaker and Hisham Cholakkal and Salman Khan and Syed Waqas Zamir and Rao Muhammad Anwer and Fahad Shahbaz Khan},
  booktitle={International Workshop on Computational Aspects of Deep Learning at 17th European Conference on Computer Vision (CADL2022)},
  year={2022},
  organization={Springer}
}
```
```bibtex
@misc{https://doi.org/10.48550/arxiv.2204.03475,
  doi = {10.48550/ARXIV.2204.03475},  
  url = {https://arxiv.org/abs/2204.03475},  
  author = {Ridnik, Tal and Lawen, Hussam and Ben-Baruch, Emanuel and Noy, Asaf},  
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},  
  title = {Solving ImageNet: a Unified Scheme for Training any Backbone to Top Results},  
  publisher = {arXiv},  
  year = {2022},  
}
```
