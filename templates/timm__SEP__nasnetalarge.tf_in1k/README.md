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
# Model card for nasnetalarge.tf_in1k

A NasNet image classification model. Trained on ImageNet-1k by paper authors. Ported from Tensorflow via Cadene's pretrained-models.pytorch.

## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 88.8
  - GMACs: 23.9
  - Activations (M): 90.6
  - Image size: 331 x 331
- **Papers:**
  - Learning Transferable Architectures for Scalable Image Recognition: https://arxiv.org/abs/1707.07012
- **Original:**
  - https://github.com/tensorflow/models
  - https://github.com/Cadene/pretrained-models.pytorch
- **Dataset:** ImageNet-1k

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('nasnetalarge.tf_in1k', pretrained=True)
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
    'nasnetalarge.tf_in1k',
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
    #  torch.Size([1, 96, 165, 165])
    #  torch.Size([1, 168, 83, 83])
    #  torch.Size([1, 1008, 42, 42])
    #  torch.Size([1, 2016, 21, 21])
    #  torch.Size([1, 4032, 11, 11])

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
    'nasnetalarge.tf_in1k',
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
# output is unpooled, a (1, 4032, 11, 11) shaped tensor

output = model.forward_head(output, pre_logits=True)
# output is a (1, num_features) shaped tensor
```

## Model Comparison
Explore the dataset and runtime metrics of this model in timm [model results](https://github.com/huggingface/pytorch-image-models/tree/main/results).

## Citation
```bibtex
@misc{zoph2018learning,
  title={Learning Transferable Architectures for Scalable Image Recognition}, 
  author={Barret Zoph and Vijay Vasudevan and Jonathon Shlens and Quoc V. Le},
  year={2018},
  eprint={1707.07012},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```
