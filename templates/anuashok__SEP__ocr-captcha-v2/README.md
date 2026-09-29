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
model_name: anuashok/ocr-captcha-v2
base_model:
- microsoft/trocr-base-printed
---

# anuashok/ocr-captcha-v2

This model is a fine-tuned version of [microsoft/trocr-base-printed](https://huggingface.co/microsoft/trocr-base-printed) on your custom dataset.
captchas like


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6569b4be1bac1166939f86b2/urZTYpc7f5ZkC5qhUf_5l.png)

## Training Summary

- **CER (Character Error Rate)**: 0.02025931928687196
- **Hyperparameters**:
  - **Learning Rate**: 1.1081459294764632e-05
  - **Batch Size**: 4
  - **Num Epochs**: 3
  - **Warmup Ratio**: 0.07863134774153628
  - **Weight Decay**: 0.06248152825021373
  - **Num Beams**: 6
  - **Length Penalty**: 0.5095100725173662

## Usage

```python
from transformers import VisionEncoderDecoderModel, TrOCRProcessor
import torch
from PIL import Image

# Load model and processor
processor = TrOCRProcessor.from_pretrained("anuashok/ocr-captcha-v2")
model = VisionEncoderDecoderModel.from_pretrained("anuashok/ocr-captcha-v2")

# Load image
image = Image.open('path_to_your_image.jpg').convert("RGB")

# Prepare image
pixel_values = processor(image, return_tensors="pt").pixel_values

# Generate text
generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(generated_text)