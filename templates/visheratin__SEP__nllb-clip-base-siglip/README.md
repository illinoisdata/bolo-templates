---
tags:
- clip
library_name: open_clip
pipeline_tag: zero-shot-image-classification
license: cc-by-nc-4.0
datasets:
- visheratin/laion-coco-nllb
new_version: visheratin/mexma-siglip2
---

## Model Summary

NLLB-CLIP-SigLIP is a model that combines a text encoder from the [NLLB model](https://huggingface.co/facebook/nllb-200-distilled-600M) and an image encoder from the 
[SigLIP](https://huggingface.co/timm/ViT-B-16-SigLIP-384) model. This allows us to extend the model capabilities 
to 201 languages of the Flores-200. NLLB-CLIP sets state-of-the-art on the [Crossmodal-3600](https://google.github.io/crossmodal-3600/) dataset by performing very 
well on low-resource languages. You can find more details about the model in the [paper](https://arxiv.org/abs/2309.01859).

This version performs much better than the [standard](https://huggingface.co/visheratin/nllb-clip-base-oc) version. You can see the results
[here](https://github.com/mlfoundations/open_clip/blob/main/docs/openclip_multilingual_retrieval_results.csv) and 
[here](https://github.com/gregor-ge/Babel-ImageNet/blob/main/evaluation_scripts/results_analysis.ipynb).

<b>NB: There is even better [version](https://huggingface.co/visheratin/nllb-siglip-mrl-base) of this model available!</b>

## How to use

<a target="_blank" href="https://colab.research.google.com/drive/1TE_jln3SwTDzjFsGqbdxIJkwrUlnNs3i">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

This model is integrated into OpenCLIP so that you can use it as any other model:

```
!pip install -U open_clip_torch
```

```
from open_clip import create_model_from_pretrained, get_tokenizer
from PIL import Image
import requests
import torch

model, transform = create_model_from_pretrained("nllb-clip-base-siglip", "v1", device="cuda")

tokenizer = get_tokenizer("nllb-clip-base-siglip")

class_options = ["бабочка", "butterfly", "kat"]
class_langs = ["rus_Cyrl", "eng_Latn", "afr_Latn"]

text_inputs = []
for i in range(len(class_options)):
    tokenizer.set_language(class_langs[i])
    text_inputs.append(tokenizer(class_options[i]))
text_inputs = torch.stack(text_inputs).squeeze(1).to("cuda")

image_path = "https://huggingface.co/spaces/jjourney1125/swin2sr/resolve/main/samples/butterfly.jpg"
image = Image.open(requests.get(image_path, stream=True).raw)

image_inputs = transform(image).unsqueeze(0).to("cuda")

with torch.inference_mode():
    logits_per_image, logits_per_text = model.get_logits(image_inputs, text_inputs)

print(logits_per_image.softmax(dim=-1))
```

## Acknowledgements

I thank [ML Collective](https://mlcollective.org/) for providing Google Cloud compute resources to train the OpenCLIP-compatible version of NLLB-CLIP.