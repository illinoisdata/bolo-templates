---
tags:
- clip
library_name: open_clip
pipeline_tag: zero-shot-image-classification
license: cc-by-4.0
datasets:
- UCSC-VLAA/Recap-DataComp-1B
---
# Model card for Recap-CLIP-ViT-L-16-Txt-Huge-2.56B

A CLIPA model trained on Recap-DataComp-1B...

## Model Details
- **Model Type:** Contrastive Image-Text, Zero-Shot Image Classification.
- **Original:** https://github.com/UCSC-VLAA/Recap-DataComp-1B
- **Dataset:** https://huggingface.co/datasets/UCSC-VLAA/Recap-DataComp-1B
- **Papers:**
  - What If We Recaption Billions of Web Images with LLaMA-3?: https://arxiv.org/abs/2406.08478

## Model Usage
### With OpenCLIP
```
import torch
import torch.nn.functional as F
from urllib.request import urlopen
from PIL import Image
from open_clip import create_model_from_pretrained, get_tokenizer

model, preprocess = create_model_from_pretrained('hf-hub:UCSC-VLAA/ViT-L-16-HTxt-Recap-CLIP')
tokenizer = get_tokenizer('hf-hub:UCSC-VLAA/ViT-L-16-HTxt-Recap-CLIP')

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

## Bias, Risks, and Limitations
This model is trained on image-text dataset with LLaVA-1.5-LLaMA3-8B generated captions, which may still contain biases and inaccuracies inherent in the original web-crawled data. 
Users should be aware of the bias, risks, or limitations when using this model. check the [dataset card](https://huggingface.co/datasets/UCSC-VLAA/Recap-DataComp-1B) page for more details.

## Citation
```bibtex
@article{li2024recaption,
      title={What If We Recaption Billions of Web Images with LLaMA-3?}, 
      author={Xianhang Li and Haoqin Tu and Mude Hui and Zeyu Wang and Bingchen Zhao and Junfei Xiao and Sucheng Ren and Jieru Mei and Qing Liu and Huangjie Zheng and Yuyin Zhou and Cihang Xie},
      journal={arXiv preprint arXiv:2406.08478},
      year={2024}
}

```

## Model Contact
zwang615@ucsc.edu