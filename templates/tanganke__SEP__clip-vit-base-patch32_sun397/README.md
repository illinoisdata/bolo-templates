---
base_model:
- openai/clip-vit-base-patch32
datasets:
- tanganke/sun397
metrics:
- accuracy
---

# Model Card

## Model Details

- Architecture: ViT-Base with patch size 32
- Training Data: Sun397

## Training Details

  Adam Optimizer with a constant learning rate 1e-5 for 4000 steps training (batch_size=32).
  Only the vision encoder is fine-tuned.

## Evaluation Results

- pre-trained: 0.63209068775177
- fine-tuned: 0.7501258850097656

## Usage

load vision model

```python
from transformers import CLIPVisionModel

vision_model = CLIPVisionModel.from_pretrained('tanganke/clip-vit-base-patch32_sun397')
```

substitute the vision encoder of clip

```python
from transformers import CLIPModel

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_model.vision_model.load_state_dict(vision_model.vision_model.state_dict())
```
