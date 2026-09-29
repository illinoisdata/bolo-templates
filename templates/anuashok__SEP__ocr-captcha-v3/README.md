---
tags:
- vision
- ocr
- trocr
- pytorch
license: apache-2.0
datasets:
- custom-captcha-dataset
metrics:
- cer
model_name: anuashok/ocr-captcha-v3
base_model:
- microsoft/trocr-base-printed
---

# anuashok/ocr-captcha-v3

This model is a fine-tuned version of [microsoft/trocr-base-printed](https://huggingface.co/microsoft/trocr-base-printed) on Captchas of the type shown below


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6569b4be1bac1166939f86b2/ncjFKGf86bk18ON9B9mYZ.png)



![image/png](https://cdn-uploads.huggingface.co/production/uploads/6569b4be1bac1166939f86b2/bKLXrLjpjpIwPHaURhjN2.png)


## Training Summary

- **CER (Character Error Rate)**: 0.01394585726004922
- **Hyperparameters**:
  - **Learning Rate**: 1.5078922700531405e-05
  - **Batch Size**: 16
  - **Num Epochs**: 7
  - **Warmup Ratio**: 0.14813004670666596
  - **Weight Decay**: 0.017176551931326833
  - **Num Beams**: 2
  - **Length Penalty**: 1.3612823161368288

## Usage

```python
from transformers import VisionEncoderDecoderModel, TrOCRProcessor
import torch
from PIL import Image

# Load model and processor
processor = TrOCRProcessor.from_pretrained("anuashok/ocr-captcha-v3")
model = VisionEncoderDecoderModel.from_pretrained("anuashok/ocr-captcha-v3")

# Load image
image = Image.open('path_to_your_image.jpg').convert("RGB")
# Load and preprocess image for display
image = Image.open(image_path).convert("RGBA")
# Create white background
background = Image.new("RGBA", image.size, (255, 255, 255))
combined = Image.alpha_composite(background, image).convert("RGB")

# Prepare image
pixel_values = processor(combined, return_tensors="pt").pixel_values

# Generate text
generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(generated_text)