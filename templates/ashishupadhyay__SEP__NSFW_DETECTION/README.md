---
license: mit
language:
- en
pipeline_tag: image-classification
---
# NSFW Image Detection Model

A fine-tuned Vision Transformer (ViT) model for NSFW image classification based on the "google/vit-base-patch16-224-in21k" architecture.

## Model Description

This model is a variant of the transformer encoder architecture adapted for image classification tasks. It has been fine-tuned specifically for detecting Not Safe For Work (NSFW) content in images with high accuracy.

### Training Details

- **Base Model**: google/vit-base-patch16-224-in21k
- **Image Resolution**: 224x224 pixels
- **Batch Size**: 16
- **Learning Rate**: 5e-5
- **Training Dataset**: 80,000 images (proprietary dataset)
- **Classes**: 2 (normal, nsfw)

### Training Stats

- Evaluation Loss: 0.07463
- Accuracy: 98.04%
- Evaluation Runtime: 304.98s
- Samples per Second: 52.46
- Steps per Second: 3.28

## How to Use

### Using Pipeline (Simple Method)

```python
from PIL import Image
from transformers import pipeline

img = Image.open("<path_to_image_file>")
classifier = pipeline("image-classification", model="ashishupadhyay/NSFW_DETECTION")
classifier(img)
```

### Using Model Directly

```python
import torch
from PIL import Image
from transformers import AutoModelForImageClassification, ViTImageProcessor

img = Image.open("<path_to_image_file>")
model = AutoModelForImageClassification.from_pretrained("ashishupadhyay/NSFW_DETECTION")
processor = ViTImageProcessor.from_pretrained('ashishupadhyay/NSFW_DETECTION')

with torch.no_grad():
    inputs = processor(images=img, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

predicted_label = logits.argmax(-1).item()
model.config.id2label[predicted_label]
```

## Intended Uses & Limitations

### Intended Uses
- NSFW Image Classification
- Content Moderation
- Safe Content Filtering

### Limitations
- Specialized for NSFW detection only
- Performance may vary for other tasks
- Should be used in conjunction with content guidelines and regulations

## Important Notes

- The model is fine-tuned specifically for NSFW content detection
- Use responsibly and ethically
- Adhere to applicable content guidelines and regulations
- Performance may vary based on input image quality and characteristics

## References

- [Hugging Face Model Hub](https://huggingface.co/ashishupadhyay/NSFW_DETECTION)
- [Vision Transformer (ViT) Paper](https://arxiv.org/abs/2010.11929)
- [ImageNet-21k Dataset](https://www.image-net.org/)

## Disclaimer

The model's performance may be influenced by the quality and representativeness of the training data. Users should assess the model's suitability for their specific applications and datasets before implementation.