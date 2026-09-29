# Model Card for ResNet-152 Text Detector
This model was trained with the intent to quickly classify whether or not an image contains legible text or not. It was trained as a binary classification problem on the COCO-Text dataset together with some images from LLaVAR. This came out to a total of ~140k images, where 50% of them had text and 50% of them had no legible text.

# Model Details
## How to Get Started with the Model
```python
from PIL import Image
import requests
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification

model = AutoModelForImageClassification.from_pretrained(
    "miguelcarv/resnet-152-text-detector",
)

processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50", do_resize=False)

url = "http://images.cocodataset.org/train2017/000000044520.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert('RGB').resize((300,300))

inputs = processor(image, return_tensors="pt").pixel_values

with torch.no_grad():
    outputs = model(inputs)
    
logits_per_image = outputs.logits 
probs = logits_per_image.softmax(dim=1) 
print(probs)
# tensor([[0.1085, 0.8915]])
```
# Training Details
- Trained for three epochs
- Resolution: 300x300
- Learning rate: 5e-5
- Optimizer: AdamW
- Batch size: 64
- Trained with FP32