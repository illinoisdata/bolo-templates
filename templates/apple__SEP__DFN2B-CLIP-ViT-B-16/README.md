---
license: apple-amlr
license_name: apple-sample-code-license
license_link: LICENSE
---



A CLIP (Contrastive Language-Image Pre-training) model trained on DFN-2B. 
Data Filtering Networks (DFNs) are small networks used to automatically filter large pools of uncurated data. 
This model was trained on 2B images that were filtered from a pool of 12.8B uncurated image-text pairs 
(12.8B image-text pairs from CommonPool-12.8B).

These weights are directly usable in OpenCLIP (image + text).


## Model Details

- **Model Type:**  Contrastive Image-Text, Zero-Shot Image Classification.
- **Dataset:** DFN-2b
- **Papers:**
  - Data Filtering Networks: https://arxiv.org/abs/2309.17425
- **Examples Seen:** 12.8B


## Model Metrics 
| Dataset                |   Metric |
|:-----------------------|---------:|
| ImageNet 1k            | 0.76236  |
| Caltech-101            | 0.942894 |
| CIFAR-10               | 0.9672   |
| CIFAR-100              | 0.8347   |
| CLEVR Counts           | 0.232333 |
| CLEVR Distance         | 0.245267 |
| Country211             | 0.19545  |
| Describable Textures   | 0.575532 |
| EuroSAT                | 0.54     |
| FGVC Aircraft          | 0.248503 |
| Food-101               | 0.91303  |
| GTSRB                  | 0.469913 |
| ImageNet Sketch        | 0.620684 |
| ImageNet v2            | 0.682    |
| ImageNet-A             | 0.482133 |
| ImageNet-O             | 0.493    |
| ImageNet-R             | 0.830967 |
| KITTI Vehicle Distance | 0.192686 |
| MNIST                  | 0.782    |
| ObjectNet              | 0.631851 |
| Oxford Flowers-102     | 0.819895 |
| Oxford-IIIT Pet        | 0.936907 |
| Pascal VOC 2007        | 0.788528 |
| PatchCamelyon          | 0.521545 |
| Rendered SST2          | 0.486546 |
| RESISC45               | 0.61381  |
| Stanford Cars          | 0.90735  |
| STL-10                 | 0.97525  |
| SUN397                 | 0.714162 |
| SVHN                   | 0.598955 |
| Flickr                 | 0.7728   |
| MSCOCO                 | 0.518773 |
| WinoGAViL              | 0.541748 |
| iWildCam               | 0.155574 |
| Camelyon17             | 0.499283 |
| FMoW                   | 0.141149 |
| Dollar Street          | 0.625    |
| GeoDE                  | 0.891023 |
| **Average**                | **0.609232** |

## Model Usage
### With OpenCLIP
```
import torch
import torch.nn.functional as F
from urllib.request import urlopen
from PIL import Image
from open_clip import create_model_from_pretrained, get_tokenizer 

model, preprocess = create_model_from_pretrained('hf-hub:apple/DFN2B-CLIP-ViT-B-16')
tokenizer = get_tokenizer('ViT-B-16')

image = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))
image = preprocess(image).unsqueeze(0)

labels_list = ["a dog", "a cat", "a donut", "a beignet"]
text = tokenizer(labels_list, context_length=model.context_length)

with torch.no_grad(), torch.cuda.amp.autocast():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    image_features = F.normalize(image_features, dim=-1)
    text_features = F.normalize(text_features, dim=-1)

    text_probs = torch.sigmoid(image_features @ text_features.T * model.logit_scale.exp() + model.logit_bias)

zipped_list = list(zip(labels_list, [round(p.item(), 3) for p in text_probs[0]]))
print("Label probabilities: ", zipped_list)
```

## Citation
```bibtex
@article{fang2023data,
  title={Data Filtering Networks},
  author={Fang, Alex and Jose, Albin Madappally and Jain, Amit and Schmidt, Ludwig and Toshev, Alexander and Shankar, Vaishaal},
  journal={arXiv preprint arXiv:2309.17425},
  year={2023}
}

```