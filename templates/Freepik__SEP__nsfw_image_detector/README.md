---
license: mit
base_model:
- timm/eva02_base_patch14_448.mim_in22k_ft_in22k_in1k
pipeline_tag: image-classification
tags:
- pytorch
- transformers
---

# EVA-based Fast NSFW Image Classifier

## Table of Contents
- [Model Description](#model-description)
- [Try it Online!](#try-it-online-)
- [Model Performance Comparison](#model-performance-comparison)
  - [Global Performance](#global-performance)
  - [Accuracy by AI Content](#accuracy-by-ai-content)
    - [AI-Generated Content](#ai-generated-content)
    - [Non-AI-Generated Content](#non-ai-generated-content)
- [Usage](#usage)
  - [Quick Start via pip](#quick-start-via-pip)
  - [Quick Start with Pipeline](#quick-start-with-pipeline)
  - [Avoid installation of pip dependency](#avoid-installation-of-pip-dependency)
- [Training](#training)
- [Speed and Memory Metrics](#speed-and-memory-metrics)

## Model Description

This model is a vision transformer based on the **EVA architecture**, fine-tuned for **NSFW content classification**. It has been trained
to detect **four categories** (neutral, low, medium, high) of visual content using **100,000 synthetically labeled images**.

The model can be used as a **binary (true/false) classifier if desired, or you can obtain the full output probabilities.**. It **outperforms other excellent publicly available models** such as [Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection) or [AdamCodd/vit-base-nsfw-detector](https://huggingface.co/AdamCodd/vit-base-nsfw-detector) in our internal benchmarks adding the enrichment of being able to select the NSFW level that suits your use case.

## Try it Online! 🚀

You can try this model directly in your browser through our [Hugging Face Space](https://huggingface.co/spaces/ccabrerafreepik/nsfw_image_detector). Upload any image and get instant NSFW classification results without any installation required. 

## Model Performance Comparison

### Global Performance

| Category | Freepik | Falconsai | Adamcodd |
|----------|-------------|------------------|----------------|
| High     | 99.54%     | 97.92%          | 98.62%         |
| Medium   | 97.02%     | 78.54%          | 91.65%         |
| Low      | 98.31%     | 31.25%          | 89.66%         |
| Neutral  | 99.87%     | 99.27%          | 98.37%         |


In the table below, the results are obtained as follows:
 
* For the **Falconsai and AdamCodd** models:
    * A prediction is considered correct if the image is labeled "low", "medium", or "high" and the model returns true.
    * If the label is "neutral", the correct output should be false.

* For the **Freepik model**:
    * If the image label is "low", "medium", or "high", the model should return at least "low".
    * If the label is "neutral", the correct output should be "neutral".


**Conclusions:**

* Our model **outperforms AdamCodd and Falconsai in accuracy**. It is entirely fair to compare them on the "high" and "neutral" labels.
* Our model **offers greater granularity**. It is not only suitable for detecting "high" and "neutral" content, but also performs excellently at identifying "low" and "medium" NSFW content.
    * Falconsai may classify some "medium" and "low" images as not NSFW but mark others as safe for work(SFW), which could lead to unexpected results.
    * AdamCodd classifies both "low" and "medium" categories as NSFW, which may not be desirable depending on your use case. Furthermore, a 10% of images in low and medium are considered SFW.

### Accuracy by AI Content

We have created a **manually labeled dataset** with careful attention to **avoiding biases** (gender, ethnicity, etc.). While the sample size is relatively small, it provides meaningful insights into model performance across different scenarios, which was very useful in the training process to avoid biases.

The following tables show detection accuracy percentages across different NSFW categories and content types:

#### AI-Generated Content

| Category | Freepik Model | Falconsai Model | Adamcodd Model |
|----------|-------------|------------------|----------------|
| High     | 100.00%     | 84.00%          | 92.00%         |
| Medium   | 96.15%      | 69.23%          | 96.00%         |
| Low      | 100.00%     | 35.71%          | 92.86%         |
| Neutral  | 100.00%     | 100.00%         | 66.67%         |


**Conclusions:**
* **Avoid using Falconsai for AI-generated content** to prevent prediction errors.
* **Our model is the best option to detect NSFW content in AI-generated content**.  


## Usage

### Quick Start via pip

```sh 
pip install nsfw-image-detector
```

```python
from PIL import Image
from nsfw_image_detector import NSFWDetector
import torch

# Initialize the detector
detector = NSFWDetector(dtype=torch.bfloat16, device="cuda")

# Load and classify an image
image = Image.open("your_image")

# Check if the image contains NSFW content sentivity level medium or higher
is_nsfw = detector.is_nsfw(image, "medium")

# Get probability scores for all categories
probabilities = detector.predict_proba(image)
print(f"Is NSFW: {is_nsfw}")
print(f"Probabilities: {probabilities}")
```

Example output:
```python
Is NSFW: False
Probabilities: 
    [
        {<NSFWLevel.HIGH: 'high'>: 0.00372314453125, 
        <NSFWLevel.MEDIUM: 'medium'>: 0.1884765625, 
        <NSFWLevel.LOW: 'low'>: 0.234375, 
        <NSFWLevel.NEUTRAL: 'neutral'>: 0.765625}
    ]
```

### Quick Start with Pipeline

```python
from transformers import pipeline
from PIL import Image

# Create classifier pipeline
classifier = pipeline(
    "image-classification",
    model="Freepik/nsfw_image_detector",
    device=0  # Use GPU (0) or CPU (-1)
)

# Load and classify an image
image = Image.open("path/to/your/image.jpg")
predictions = classifier(image)
print(predictions)
```

Example output:
```python
[
    {'label': 'neutral', 'score': 0.92},
    {'label': 'low', 'score': 0.05},
    {'label': 'medium', 'score': 0.02},
    {'label': 'high', 'score': 0.01}
]
```

The model supports efficient batch processing for multiple images:

```python
images = [Image.open(path) for path in ["image1.jpg", "image2.jpg", "image3.jpg"]]
predictions = classifier(images)
```

**Note**: If the intention is to use the model in production review [Speed and Memory Metrics](#speed-and-memory-metrics) section before using this approach.

### Avoid installation of pip dependency

The following example demonstrates how to **customize the NSFW detection label**, it is very similar to the code in [PyPy](https://pypi.org/project/nsfw-image-detector/0.1.0/). This code returns True if the NSFW level is 'medium' or higher:

```python
from transformers import AutoModelForImageClassification
import torch
from PIL import Image
from typing import List, Dict
import torch.nn.functional as F
from timm.data.transforms_factory import create_transform
from torchvision.transforms import Compose
from timm.data import resolve_data_config
from timm.models import get_pretrained_cfg


device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model and processor
model = AutoModelForImageClassification.from_pretrained("Freepik/nsfw_image_detector", torch_dtype = torch.bfloat16).to(device) 

# Load original processor (faster for tensors)
cfg = get_pretrained_cfg("eva02_base_patch14_448.mim_in22k_ft_in22k_in1k")
processor: Compose = create_transform(**resolve_data_config(cfg.__dict__))

def predict_batch_values(model, processor: Compose, img_batch: List[Image.Image] | torch.Tensor) -> List[Dict[str, float]]:
    """
    Process a batch of images and return prediction scores for each NSFW category
    """
    idx_to_label = {0: 'neutral', 1: 'low', 2: 'medium', 3: 'high'}
    
    # Prepare batch
    inputs = torch.stack([processor(img) for img in img_batch])
    output = []
    with torch.inference_mode():
        logits = model(inputs).logits
        batch_probs = F.log_softmax(logits, dim=-1)
        batch_probs = torch.exp(batch_probs).cpu()
        
        for i in range(len(batch_probs)):
            element_probs = batch_probs[i]
            output_img = {}
            danger_cum_sum = 0
            
            for j in range(len(element_probs) - 1, -1, -1):
                danger_cum_sum += element_probs[j]
                if j == 0:
                    danger_cum_sum = element_probs[j]
                output_img[idx_to_label[j]] = danger_cum_sum.item()
            output.append(output_img)

    return output

def prediction(model, processor, img_batch: List[Image.Image], class_to_predict: str, threshold: float=0.5) -> List[bool]:
    """
    Predict if images meet or exceed a specific NSFW threshold
    """
    if class_to_predict not in ["low", "medium", "high"]:
        raise ValueError("class_to_predict must be one of: low, medium, high")
    
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    output = predict_batch_values(model, processor, img_batch)
    return [output[i][class_to_predict] >= threshold for i in range(len(output))]

# Example usage
image = Image.open("path/to/your/image.jpg")
print(predict_batch_values(model, processor, [image]))
print(prediction(model, processor, [image], "medium")) # Options: low, medium, high
```

Example output:

```python
[
    {'label': 'neutral', 'score': 0.92},
    {'label': 'low', 'score': 0.08},
    {'label': 'medium', 'score': 0.03},
    {'label': 'high', 'score': 0.01}
]

[False]
```
**Note**: The sum is higher than one because the prediction is the cumulative sum of all labels equal to or higher than your selected label, except neutral. For instance, if you select 'medium', it is the sum of 'medium' and 'high'. In our opinion, this approach is more effective than selecting only the highest probability label.

## Training

* **100,000 images** were used during training. 
* The model were trained for **3 epochs on 3 NVIDIA GeForce RTX 3090**
* The model were trained using two sets, training and validation.
* There are **no images with a cosine similarity higher than 0.92** to avoid duplicates and biases between training and validation. The model used for deduplication is "openai/clip-vit-base-patch32"
* A **custom loss** was created to minimize predictions that are lower than the true class. For instance, it is very rare for an image labeled as 'high' to be predicted as 'neutral' (this only happens 0.46% of the time).

## Speed and Memory Metrics

| Batch Size | Avg by batch (ms) | VRAM (MB) | Optimizations |
|------------|------------------|------------|---------------|
| 1          | 28               | 540        | BF16 using PIL images |
| 4          | 110              | 640        | BF16 using PIL images |
| 16         | 412              | 1144       | BF16 using PIL images |
| 1          | 10               | 540        | BF16 using torch tensor |
| 4          | 33               | 640        | BF16 using torch tensor |
| 16         | 102              | 1144       | BF16 using torch tensor |

**Notes:**
* The model has been trained in bf16 so it is **recommended to use it in bf16**.
* **Using torch tensor**: The speed using torch tensor is not achieved using pipeline. Avoid pipeline use in production.
* Measurements taken on **NVIDIA RTX 3090**, expect better metrics in more powerful servers.
* Throughput increases with larger batch sizes due to better GPU utilization. Consider your use case when selecting batch size.
* Optimizations listed are suggestions that could further improve performance.
* **Using torch tensors is specially indicated** in cases such as use the model for **text to image models or similar** because the output is already in tensor format.



## License

This project is licensed under the MIT License - Copyright 2025 Freepik Company S.L.


## Citation

If you use this model in your research or project, please cite it as:

```bibtex
@software{freepik2025nsfw,
    title={EVA-based Fast NSFW Image Classifier},
    author={Freepik Company S.L.},
    year={2025},
    publisher={Hugging Face},
    url = {https://huggingface.co/Freepik/nsfw_image_detector},
    organization = {Freepik Company S.L.}
}
```

## Acknowledgements

This model is based on the EVA architecture ([timm/eva02_base_patch14_448.mim_in22k_ft_in22k_in1k](https://huggingface.co/timm/eva02_base_patch14_448.mim_in22k_ft_in22k_in1k)), as described in the following paper:

EVA-02: A Visual Representation for Neon Genesis - https://arxiv.org/abs/2303.11331

```bibtex
@article{EVA02,
  title={EVA-02: A Visual Representation for Neon Genesis},
  author={Fang, Yuxin and Sun, Quan and Wang, Xinggang and Huang, Tiejun and Wang, Xinlong and Cao, Yue},
  journal={arXiv preprint arXiv:2303.11331},
  year={2023}
}
```