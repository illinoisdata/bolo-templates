---
tags:
- image-classification
- timm
- chart
- charts
- fintwit
- stocks
- crypto
- finance
- financial
- financial charts
- graphs
- financial graphs
- plot
- plots
- financial plots
- cryptocurrency
- image-recognition
- recognition
library_name: timm
license: mit
datasets:
- StephanAkkerman/crypto-charts
- StephanAkkerman/stock-charts
- StephanAkkerman/fintwit-images
language:
- en
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: chart-recognizer
  results:
  - task:
      type: image-classification
    dataset:
      name: Test Set
      type: images
    metrics:
    - type: accuracy
      value: 0.9782
    - type: f1
      value: 0.9685
pipeline_tag: image-classification
base_model: timm/efficientnet_b0.ra_in1k
---
# Chart Recognizer

chart-recognizer is a finetuned model for classifying images. It uses efficientnet as its base model, making it a fast and small model.
This model is trained on my own dataset of financial charts posted on Twitter, which can be found here [StephanAkkerman/fintwit-charts](https://huggingface.co/datasets/StephanAkkerman/fintwit-charts).

## Intended Uses

chart-recognizer is intended for classifying images, mainly images posted on social media.

## Dataset

chart-recognizer has been trained on my own dataset. So far I have not been able to find another image dataset about financial charts.
- [StephanAkkerman/crypto-charts](https://huggingface.co/datasets/StephanAkkerman/crypto-charts): 4,880 images.
- [StephanAkkerman/stock-charts](https://huggingface.co/datasets/StephanAkkerman/stock-charts): 5,203 images.
- [StephanAkkerman/fintwit-images](https://huggingface.co/datasets/StephanAkkerman/fintwit-images): 4,579 images.

### Example Images
The following images are not part of the training set and can be used for testing purposes.

#### Chart
![image/png](https://cdn-uploads.huggingface.co/production/uploads/648728961eee18b6bd1836bb/LWfEx-IhNLIsBPkbsvvnO.png)

#### Non-Chart
This can be any image that does not represent a (financial) chart.
![image/png](https://cdn-uploads.huggingface.co/production/uploads/648728961eee18b6bd1836bb/mKdLqAVXG032eODbt4EXw.png)

## More Information

For a comprehensive overview, including the training setup and analysis of the model, visit the [chart-recognizer GitHub repository](https://github.com/StephanAkkerman/chart-recognizer).

## Usage

Using [HuggingFace's transformers library](https://huggingface.co/docs/transformers/index) the model can be converted into a pipeline for image classification.

```python
import timm
import torch
from PIL import Image
from timm.data import resolve_data_config, create_transform

# Load and set model to eval mode
model = timm.create_model("hf_hub:StephanAkkerman/chart-recognizer", pretrained=True)
model.eval()

# Create transform and get labels
transform = create_transform(**resolve_data_config(model.pretrained_cfg, model=model))
labels = model.pretrained_cfg["label_names"]

# Load and preprocess image
image = Image.open("img/examples/tweet_example.png").convert("RGB")
x = transform(image).unsqueeze(0)

# Get model output and apply softmax
probabilities = torch.nn.functional.softmax(model(x)[0], dim=0)

# Map probabilities to labels
output = {label: prob.item() for label, prob in zip(labels, probabilities)}

# Print the predicted probabilities
print(output)
```

## Citing & Authors

If you use chart-recognizer in your research, please cite me as follows:

```
@misc{chart-recognizer,
  author = {Stephan Akkerman},
  title = {chart-recognizer: A Specialized Image Model for Financial Charts},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/StephanAkkerman/chart-recognizer}}
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.