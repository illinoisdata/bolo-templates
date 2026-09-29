---
library_name: py-feat
pipeline_tag: image-feature-extraction
tags:
- model_hub_mixin
- pytorch_model_hub_mixin
license: cc-by-nc-4.0
---

# img2pose

## Model Description
img2pose uses Faster R-CNN to predict 6 Degree of Freedom Pose (DoF) for all faces in the photo. An interesting property of this model is that it can project the 3D face onto a 2D plane to also identify bounding boxes for each face. It does not require any other face detection model. 

## Model Details
- **Model Type**: Convolutional Neural Network (CNN)
- **Architecture**: Faster R-CNN 
- **Framework**: PyTorch

## Model Sources
- **Repository**: [GitHub Repository](https://github.com/vitoralbiero/img2pose)
- **Paper**: [img2pose: Face Alignment and Detection via 6DoF, Face Pose Estimation](https://arxiv.org/abs/2012.07791)

## Citation
If you use this model in your research or application, please cite the following paper:

Vítor Albiero, Xingyu Chen, Xi Yin, Guan Pang, Tal Hassner, "img2pose: Face Alignment and Detection via 6DoF, Face Pose Estimation," CVPR, 2021, arXiv:2012.07791

```
@inproceedings{albiero2021img2pose,
  title={img2pose: Face Alignment and Detection via 6DoF, Face Pose Estimation},
  author={Albiero, Vítor and Chen, Xingyu and Yin, Xi and Pang, Guan and Hassner, Tal},
  booktitle={CVPR},
  year={2021},
  url={https://arxiv.org/abs/2012.07791},
}
```

## Acknowledgements
We thank Albiero Vítor for sharing their code and training weights with a permissive license. 

## Example Useage

```{python}
import numpy as np
import os
import json
import torch
import torch.nn as nn
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
from feat.facepose_detectors.img2pose.deps.models import FasterDoFRCNN, postprocess_img2pose
from feat.utils.io import get_resource_path
from torchvision.models.detection.backbone_utils import resnet_fpn_backbone


# Load Model Configurations
facepose_config_file = hf_hub_download(repo_id= "py-feat/img2pose", filename="config.json", cache_dir=get_resource_path())
with open(facepose_config_file, "r") as f:
    facepose_config = json.load(f)
           
# Initialize img2pose
device = 'cpu'
backbone = resnet_fpn_backbone(backbone_name="resnet18", weights=None)
backbone.eval()
backbone.to(device)
facepose_detector = FasterDoFRCNN(backbone=backbone,
                            num_classes=2,
                            min_size=facepose_config['min_size'],
                            max_size=facepose_config['max_size'],
                            pose_mean=torch.tensor(facepose_config['pose_mean']),
                            pose_stddev=torch.tensor(facepose_config['pose_stddev']),
                            threed_68_points=torch.tensor(facepose_config['threed_points']),
                            rpn_pre_nms_top_n_test=facepose_config['rpn_pre_nms_top_n_test'],
                            rpn_post_nms_top_n_test=facepose_config['rpn_post_nms_top_n_test'],
                            bbox_x_factor=facepose_config['bbox_x_factor'],
                            bbox_y_factor=facepose_config['bbox_y_factor'],
                            expand_forehead=facepose_config['expand_forehead'])
facepose_model_file = hf_hub_download(repo_id= "py-feat/img2pose", filename="model.safetensors", cache_dir=get_resource_path())
facepose_checkpoint = load_file(facepose_model_file)
facepose_detector.load_state_dict(facepose_checkpoint)
facepose_detector.eval()
facepose_detector.to(device)

# Test model
face_image = "path/to/your/test_image.jpg"  # Replace with your image

img2pose_output = facepose_detector(face_image)

# Postprocess
img2pose_output = postprocess_img2pose(img2pose_output[0])
bbox = img2pose_output['boxes']
poses = img2pose_output['dofs']
facescores = img2pose_output['scores']

```