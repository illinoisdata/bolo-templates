---
license: bsd-3-clause
tags:
- image-captioning
datasets:
- unography/laion-14k-GPT4V-LIVIS-Captions
pipeline_tag: image-to-text
languages:
- en
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/savanna.jpg
  example_title: Savanna
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/football-match.jpg
  example_title: Football Match
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg
  example_title: Airport
inference:
  parameters:
    max_length: 250
    num_beams: 3
    repetition_penalty: 2.5
---

# LongCap: Finetuned [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) for generating long captions of images, suitable for prompts for text-to-image generation and captioning text-to-image datasets


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

processor = BlipProcessor.from_pretrained("unography/blip-long-cap")
model = BlipForConditionalGeneration.from_pretrained("unography/blip-long-cap")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

inputs = processor(raw_image, return_tensors="pt")
pixel_values = inputs.pixel_values
out = model.generate(pixel_values=pixel_values, max_length=250, num_beams=3, repetition_penalty=2.5)
print(processor.decode(out[0], skip_special_tokens=True))
>>> a woman sitting on the sand, interacting with a dog wearing a blue and white checkered collar. the dog is positioned to the left of the woman, who is holding something in their hand. the background features a serene beach setting with waves crashing onto the shore. there are no other animals or people visible in the image. the time of day appears to be either early morning or late afternoon, based on the lighting and shadows.

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

processor = BlipProcessor.from_pretrained("unography/blip-long-cap")
model = BlipForConditionalGeneration.from_pretrained("unography/blip-long-cap").to("cuda")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

inputs = processor(raw_image, return_tensors="pt").to("cuda")
pixel_values = inputs.pixel_values
out = model.generate(pixel_values=pixel_values, max_length=250, num_beams=3, repetition_penalty=2.5)
print(processor.decode(out[0], skip_special_tokens=True))
>>> a woman sitting on the sand, interacting with a dog wearing a blue and white checkered collar. the dog is positioned to the left of the woman, who is holding something in their hand. the background features a serene beach setting with waves crashing onto the shore. there are no other animals or people visible in the image. the time of day appears to be either early morning or late afternoon, based on the lighting and shadows.
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

processor = BlipProcessor.from_pretrained("unography/blip-long-cap")
model = BlipForConditionalGeneration.from_pretrained("unography/blip-long-cap", torch_dtype=torch.float16).to("cuda")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

inputs = processor(raw_image, return_tensors="pt").to("cuda", torch.float16)
pixel_values = inputs.pixel_values
out = model.generate(pixel_values=pixel_values, max_length=250, num_beams=3, repetition_penalty=2.5)
print(processor.decode(out[0], skip_special_tokens=True))
>>> a woman sitting on the sand, interacting with a dog wearing a blue and white checkered collar. the dog is positioned to the left of the woman, who is holding something in their hand. the background features a serene beach setting with waves crashing onto the shore. there are no other animals or people visible in the image. the time of day appears to be either early morning or late afternoon, based on the lighting and shadows.
```
</details>