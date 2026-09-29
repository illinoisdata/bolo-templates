---
license: apache-2.0
pipeline_tag: image-classification
tags:
- safety-checker
- explicit-filter
metrics:
- accuracy
library_name: timm
---

[Safesearch v3.1 was released](https://huggingface.co/aistrova/safesearch-v3.1)

## Google Safesearch Mini V2 is an ultra-precise multi-class image classifier that accurately detects explicit content

Google Safesearch Mini V2 took a different approach to its training than [V1](https://huggingface.co/FredZhang7/google-safesearch-mini); it used the InceptionResNetV2 architecture and a dataset of roughly **3,400,000 images** randomly sourced from the internet, some of which were generated via data argumentation.
The training and validation data are sourced from Google Images, Reddit, Kaggle, and Imgur, and were classified as safe or nsfw by companies, Google SafeSearch, and moderators.

After training the model for 5 epochs with cross entropy loss and evaluating it on both the training and validation sets to identify images with predicted probabilities below 0.90, some necessary corrections were made to the curated dataset and the model was trained for an additional 8 epochs.
Next, I tested the model on various cases that it may struggle to classify and observed that it was mistaking the fur of a brown cat for human skin.
To improve the accuracy, I fine-tuned the model with [15 additional datasets from Kaggle](./kaggle-datasets.txt) for one epoch, and then trained it for the last epoch with a combination of training and test data.
This resulted in **97% accuracy** on both training and validation data.

A safesearch filter is not only a great tool for moderating social media, but it also can be used to filter datasets. Compared to stable diffusion safety checkers, this model offers a major advantage - users can save 1.0 GB of RAM and disk space.

## PyTorch


```bash
pip install --upgrade torchvision
```
```python
import torch, os
from torchvision import transforms
from PIL import Image
import urllib.request
import timm

image_path = "https://www.allaboutcats.ca/wp-content/uploads/sites/235/2022/03/shutterstock_320462102-2500-e1647917149997.jpg"
device = "cuda"

def preprocess_image(image_path):
  # Define image pre-processing transforms
    transform = transforms.Compose([
      transforms.Resize(299),
      transforms.CenterCrop(299),
      transforms.ToTensor(),
      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    if image_path.startswith('http://') or image_path.startswith('https://'):
        import requests
        from io import BytesIO
        response = requests.get(image_path)
        img = Image.open(BytesIO(response.content)).convert('RGB')
    else:
        img = Image.open(image_path).convert('RGB')
    img = transform(img).unsqueeze(0)
    img = img.cuda() if device.lower() == "cuda" else img.cpu()
    return img

def eval():
    model = timm.create_model("hf_hub:FredZhang7/google-safesearch-mini-v2", pretrained=True)
    model.to(device)
    img = preprocess_image(image_path)

    with torch.no_grad():
        out = model(img)
        _, predicted = torch.max(out.data, 1)
        classes = {
            0: 'nsfw_gore',
            1: 'nsfw_suggestive',
            2: 'safe'
        }
        print('\n\033[1;31m' + classes[predicted.item()] + '\033[0m' if predicted.item() != 2 else '\033[1;32m' + classes[predicted.item()] + '\033[0m\n')

if __name__ == '__main__':
    eval()
```