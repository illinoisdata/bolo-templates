---
tags:
- clip
library_name: open_clip
pipeline_tag: zero-shot-image-classification
license: apache-2.0
datasets:
- mlfoundations/datacomp_1b
---
# Model card for ViT-bigG-14-CLIPA-datacomp1B

A CLIPA-v2 model...

## Model Details
- **Model Type:** Contrastive Image-Text, Zero-Shot Image Classification.
- **Original:** https://github.com/UCSC-VLAA/CLIPA
- **Dataset:** mlfoundations/datacomp_1b
- **Papers:**
  - CLIPA-v2: Scaling CLIP Training with 81.1% Zero-shot ImageNet Accuracy within a $10,000 Budget; An Extra $4,000 Unlocks 81.8% Accuracy: https://arxiv.org/abs/2306.15658
  - An Inverse Scaling Law for CLIP Training: https://arxiv.org/abs/2305.07017

## Model Usage
### With OpenCLIP
```
import torch
import torch.nn.functional as F
from urllib.request import urlopen
from PIL import Image
from open_clip import create_model_from_pretrained, get_tokenizer

model, preprocess = create_model_from_pretrained('hf-hub:ViT-bigG-14-CLIPA')
tokenizer = get_tokenizer('hf-hub:ViT-bigG-14-CLIPA')

image = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))
image = preprocess(image).unsqueeze(0)

text = tokenizer(["a diagram", "a dog", "a cat", "a beignet"], context_length=model.context_length)

with torch.no_grad(), torch.cuda.amp.autocast():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    image_features = F.normalize(image_features, dim=-1)
    text_features = F.normalize(text_features, dim=-1)

    text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)

print("Label probs:", text_probs)  # prints: [[0., 0., 0., 1.0]]
```   

## Citation
```bibtex
@article{li2023clipav2,
      title={CLIPA-v2: Scaling CLIP Training with 81.1% Zero-shot ImageNet Accuracy within a $10,000 Budget; An Extra $4,000 Unlocks 81.8% Accuracy}, 
      author={Xianhang Li and Zeyu Wang and Cihang Xie},
      journal={arXiv preprint arXiv:2306.15658},
      year={2023},
}
```
```bibtex
@inproceedings{li2023clipa,
      title={An Inverse Scaling Law for CLIP Training}, 
      author={Xianhang Li and Zeyu Wang and Cihang Xie},
      booktitle={NeurIPS},
      year={2023},
}
```