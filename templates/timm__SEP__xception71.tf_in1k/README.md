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
# Model card for xception71.tf_in1k

An Aligned Xception image classification model. Trained on ImageNet-1k in Tensorflow and ported to PyTorch by Ross Wightman.

## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 42.3
  - GMACs: 18.1
  - Activations (M): 69.9
  - Image size: 299 x 299
- **Papers:**
  - Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation: https://arxiv.org/abs/1802.02611
  - Xception: Deep Learning with Depthwise Separable Convolutions: https://arxiv.org/abs/1610.02357
- **Dataset:** ImageNet-1k
- **Original:** https://github.com/tensorflow/models/blob/master/research/deeplab/

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('xception71.tf_in1k', pretrained=True)
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
    'xception71.tf_in1k',
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
    #  torch.Size([1, 128, 150, 150])
    #  torch.Size([1, 256, 75, 75])
    #  torch.Size([1, 728, 38, 38])
    #  torch.Size([1, 1024, 19, 19])
    #  torch.Size([1, 2048, 10, 10])

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
    'xception71.tf_in1k',
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
# output is unpooled, a (1, 2048, 10, 10) shaped tensor

output = model.forward_head(output, pre_logits=True)
# output is a (1, num_features) shaped tensor
```

## Citation
```bibtex
@inproceedings{deeplabv3plus2018,
  title={Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation},
  author={Liang-Chieh Chen and Yukun Zhu and George Papandreou and Florian Schroff and Hartwig Adam},
  booktitle={ECCV},
  year={2018}
}
```
```bibtex
@misc{chollet2017xception,
  title={Xception: Deep Learning with Depthwise Separable Convolutions}, 
  author={François Chollet},
  year={2017},
  eprint={1610.02357},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```
