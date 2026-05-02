---
pipeline_tag: image-to-text
tags:
- image-captioning
languages:
- en
license: bsd-3-clause
widget:
- src: >-
    https://huggingface.co/datasets/mishig/sample_images/resolve/main/savanna.jpg
  example_title: Savanna
- src: >-
    https://huggingface.co/datasets/mishig/sample_images/resolve/main/football-match.jpg
  example_title: Football Match
- src: >-
    https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg
  example_title: Airport
datasets:
- unography/laion-14k-GPT4V-LIVIS-Captions
inference:
  parameters:
    max_length: 300
---

# LongCap: Finetuned [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-large) for generating long captions of images, suitable for prompts for text-to-image generation and captioning text-to-image datasets


## Usage

You can use this model for conditional and un-conditional image captioning

### Using the Pytorch model

#### Running the model on CPU

<details>
<summary> Click to expand </summary>

```python
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("unography/blip-large-long-cap")
model = BlipForConditionalGeneration.from_pretrained("unography/blip-large-long-cap")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

inputs = processor(raw_image, return_tensors="pt")
pixel_values = inputs.pixel_values
out = model.generate(pixel_values=pixel_values, max_length=250)
print(processor.decode(out[0], skip_special_tokens=True))
>>> a woman sitting on the beach, wearing a checkered shirt and a dog collar. the woman is interacting with the dog, which is positioned towards the left side of the image. the setting is a beachfront with a calm sea and a golden hue.

```
</details>

#### Running the model on GPU

##### In full precision 

<details>
<summary> Click to expand </summary>

```python
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("unography/blip-large-long-cap")
model = BlipForConditionalGeneration.from_pretrained("unography/blip-large-long-cap").to("cuda")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

inputs = processor(raw_image, return_tensors="pt").to("cuda")
pixel_values = inputs.pixel_values
out = model.generate(pixel_values=pixel_values, max_length=250)
print(processor.decode(out[0], skip_special_tokens=True))
>>> a woman sitting on the beach, wearing a checkered shirt and a dog collar. the woman is interacting with the dog, which is positioned towards the left side of the image. the setting is a beachfront with a calm sea and a golden hue.
```
</details>

##### In half precision (`float16`)

<details>
<summary> Click to expand </summary>

```python
import torch
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("unography/blip-large-long-cap")
model = BlipForConditionalGeneration.from_pretrained("unography/blip-large-long-cap", torch_dtype=torch.float16).to("cuda")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

inputs = processor(raw_image, return_tensors="pt").to("cuda", torch.float16)
pixel_values = inputs.pixel_values
out = model.generate(pixel_values=pixel_values, max_length=250)
print(processor.decode(out[0], skip_special_tokens=True))
>>> a woman sitting on the beach, wearing a checkered shirt and a dog collar. the woman is interacting with the dog, which is positioned towards the left side of the image. the setting is a beachfront with a calm sea and a golden hue.
```
</details>