---
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://huggingface.co/nvidia/C-RADIO/resolve/main/nvidia-open-model-license-agreement-june-2024.pdf
library_name: transformers
---

# Model Overview

## Description:
This model performs visual feature extraction.
For instance, RADIO generates image embeddings that can be used by a downstream model to classify images.

### License/Terms of Use

[License] This model is governed by the [NVIDIA Open Model License Agreement](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf).

## References:

[**AM-RADIO: Agglomerative Vision Foundation Model - Reduce All Domains Into One**](https://arxiv.org/abs/2312.06709)

[**PHI-S: Distribution Balancing for Label-Free Multi-Teacher Distillation**](https://arxiv.org/abs/2410.01680)

[**RADIO Amplified: Improved Baselines for Agglomerative Vision Foundation Models**](https://arxiv.org/pdf/2412.07679)


## Model Architecture:
**Architecture Type:** Neural Network  <br>
**Network Architecture:** Vision Transformer <br>

## Input:
**Input Type(s):** Image <br>
**Input Format(s):** Red, Green, Blue (RGB) pixel values in [0, 1] range. <br>
**Input Parameters:** Two Dimensional (2D) <br>
**Other Properties Related to Input:** Image resolutions up to 2048x2028 in increments of 16 pixels <br>

## Output:
**Output Type(s):** Embeddings <br>
**Output Format:** Tensor <br>
**Output Parameters:** 2D <br>
**Other Properties Related to Output:** Downstream model required to leverage image features <br>

## Usage:

RADIO will return a tuple with two tensors.
The `summary` is similar to the `cls_token` in ViT and is meant to represent the general concept of the entire image.
It has shape `(B,C)` with `B` being the batch dimension, and `C` being some number of channels.
The `spatial_features` represent more localized content which should be suitable for dense tasks such as semantic segmentation, or for integration into an LLM.

```python
import torch
from PIL import Image
from transformers import AutoModel, CLIPImageProcessor

hf_repo = "nvidia/C-RADIO"

image_processor = CLIPImageProcessor.from_pretrained(hf_repo)
model = AutoModel.from_pretrained(hf_repo, trust_remote_code=True)
model.eval().cuda()

image = Image.open('./assets/radio.png').convert('RGB')
pixel_values = image_processor(images=image, return_tensors='pt', do_resize=True).pixel_values
pixel_values = pixel_values.cuda()

summary, features = model(pixel_values)
```

Spatial features have shape `(B,T,D)` with `T` being the flattened spatial tokens, and `D` being the channels for spatial features. Note that `C!=D` in general.
Converting to a spatial tensor format can be done using the downsampling size of the model, combined with the input tensor shape. For RADIO, the patch size is 16.

```Python
from einops import rearrange
spatial_features = rearrange(spatial_features, 'b (h w) d -> b d h w', h=x.shape[-2] // patch_size, w=x.shape[-1] // patch_size)
```

The resulting tensor will have shape `(B,D,H,W)`, as is typically seen with computer vision models.


## Software Integration:
**Runtime Engine(s):**
* TAO- 24.10 <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Blackwell <br>
* NVIDIA Jetson  <br>
* NVIDIA Hopper <br>
* NVIDIA Lovelace <br>
* NVIDIA Pascal <br>
* NVIDIA Turing <br>
* NVIDIA Volta <br>

**[Preferred/Supported] Operating System(s):** <br>
* Linux
* Linux 4 Tegra
* QNX
* Windows

## Model Version(s):
C-RADIO.

**Link:** https://huggingface.co/nvidia/C-RADIO

# Training, Testing, and Evaluation Datasets:

## Training Dataset:

NV-CC-Img-Text-Dataset  <br>
** Data Collection Method by dataset <br>
* Automated <br>
** Labeling Method by dataset <br>
* Not Applicable (no labels are needed) <br>
**Properties:** 700 Million Images <br>

## Evaluation Dataset:
**Link:** [ImageNet](https://www.image-net.org/)  <br>
** Data Collection Method by dataset <br>
* Automated <br>
** Labeling Method by dataset <br>
* Human <br>

**Properties:** This dataset spans 1000 object classes and contains 1,281,167 training images, 50,000 validation images and 100,000 test images.<br>

## Inference:
**Engine:** PyTorch <br>
**Test Hardware:** A100 <br>

## Ethical Considerations (For NVIDIA Models Only):
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Users should evaluate the model for safety and quality for a specific use case and build additional guardrails as appropriate.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).