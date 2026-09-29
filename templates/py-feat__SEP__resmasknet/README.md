---
library_name: py-feat
pipeline_tag: image-feature-extraction
tags:
- model_hub_mixin
- pytorch_model_hub_mixin
license: mit
---

# ResMaskNet

## Model Description
resmasknet combines residual masking with unet architecture to predict 7 facial emotion categories from images. 

## Model Details
- **Model Type**: Convolutional Neural Network (CNN)
- **Architecture**: Residual masking network with u-network. Output layer classifies 7 emotion categories
- **Input Size**: 224x224 pixels
- **Framework**: PyTorch

## Model Sources
- **Repository**: [GitHub Repository](https://github.com/phamquiluan/ResidualMaskingNetwork)
- **Paper**: [Facial Expression Recognition Using Residual Masking Network](https://ieeexplore.ieee.org/document/9411919)

## Citation
If you use the svm_au model in your research or application, please cite the following paper:

Pham Luan, The Huynh Vu, and Tuan Anh Tran. "Facial Expression Recognition using Residual Masking Network". In: Proc. ICPR. 2020.

```
@inproceedings{pham2021facial,
  title={Facial expression recognition using residual masking network},
  author={Pham, Luan and Vu, The Huynh and Tran, Tuan Anh},
  booktitle={2020 25th International Conference on Pattern Recognition (ICPR)},
  pages={4513--4519},
  year={2021},
  organization={IEEE}
}
```

## Acknowledgements
We thank Luan Pham for generously sharing this model with a permissive license. 

## Example Useage

```python
import numpy as np
import torch
import torch.nn as nn
from feat.emo_detectors.ResMaskNet.resmasknet_test import ResMasking
from huggingface_hub import hf_hub_download

# Load Configs
emotion_config_file = hf_hub_download(repo_id= "py-feat/resmasknet", filename="config.json", cache_dir=get_resource_path())
with open(emotion_config_file, "r") as f:
    emotion_config = json.load(f)

device = 'cpu'
emotion_detector = ResMasking("", in_channels=emotion_config['in_channels'])
emotion_detector.fc = nn.Sequential(nn.Dropout(0.4), nn.Linear(512, emotion_config['num_classes']))
emotion_model_file = hf_hub_download(repo_id='py-feat/resmasknet', filename="ResMaskNet_Z_resmasking_dropout1_rot30.pth")
emotion_checkpoint = torch.load(emotion_model_file, map_location=device)["net"]
emotion_detector.load_state_dict(emotion_checkpoint)
emotion_detector.eval()
emotion_detector.to(device)


# Test model
face_image = "path/to/your/test_image.jpg"  # Replace with your extracted face image that is [224, 224]

# Classification - [angry, disgust, fear, happy, sad, surprise, neutral]
emotions = emotion_detector.forward(face_image)
emotion_probabilities = torch.softmax(emotions, 1)
        
```