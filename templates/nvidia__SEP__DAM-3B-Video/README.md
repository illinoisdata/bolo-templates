---
datasets:
- nvidia/describe-anything-dataset
language:
- en
base_model:
- Efficient-Large-Model/VILA1.5-3b
pipeline_tag: image-text-to-text
license: other
license_name: nvidia-non-commercial-license
license_link: https://huggingface.co/nvidia/DAM-3B-Video/blob/main/LICENSE
library_name: describe-anything
---

# Describe Anything: Detailed Localized Image and Video Captioning

**NVIDIA, UC Berkeley, UCSF**

[Long Lian](https://tonylian.com), [Yifan Ding](https://research.nvidia.com/person/yifan-ding), [Yunhao Ge](https://gyhandy.github.io/), [Sifei Liu](https://sifeiliu.net/), [Hanzi Mao](https://hanzimao.me/), [Boyi Li](https://sites.google.com/site/boyilics/home), [Marco Pavone](https://research.nvidia.com/person/marco-pavone), [Ming-Yu Liu](https://mingyuliu.net/), [Trevor Darrell](https://people.eecs.berkeley.edu/~trevor/), [Adam Yala](https://www.adamyala.org/), [Yin Cui](https://ycui.me/)

[[Paper](https://arxiv.org/abs/2504.16072)] | [[Code](https://github.com/NVlabs/describe-anything)] | [[Project Page](https://describe-anything.github.io/)] | [[Video](https://describe-anything.github.io/#video)] | [[HuggingFace Demo](https://huggingface.co/spaces/nvidia/describe-anything-model-demo)] | [[Model/Benchmark/Datasets](https://huggingface.co/collections/nvidia/describe-anything-680825bb8f5e41ff0785834c)] | [[Citation](#citation)]

# Model Card for DAM-3B

## Description
Describe Anything Model 3B Video (DAM-3B-Video) takes inputs of user-specified regions in the form of points/boxes/scribbles/masks within images/videos, and generates detailed localized descriptions of images/videos. DAM integrates full-image/video context with fine-grained local details using a novel focal prompt and a localized vision backbone enhanced with gated cross-attention. The model is for research and development only. This model is ready for non-commercial use.

## License
[NVIDIA Noncommercial License](https://huggingface.co/nvidia/DAM-3B-Video/blob/main/LICENSE)

## Intended Usage
This model is intended to demonstrate and facilitate the understanding and usage of the describe anything models. It should primarily be used for research and non-commercial purposes.

## Model Architecture
**Architecture Type:** Transformer <br>
**Network Architecture:** ViT and Llama <br>

This model was developed based on [VILA-1.5](https://github.com/NVlabs/VILA). <br> 
This model has 3B of model parameters. <br> 

## Input
**Input Type(s):** Image, Video, Text, Binary Mask <br>
**Input Format(s):** RGB Image, RGB Video, Binary Mask <br>
**Input Parameters:** 2D Image, 2D Video, 2D Binary Mask <br>
**Other Properties Related to Input:** 3 channels for RGB image, 3 channels for RGB video, 1 channel for binary mask. Resolution is 384x384. <br>

## Output
**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** 1D Text <br>
**Other Properties Related to Output:** Detailed descriptions for the visual region. <br> 

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere
* NVIDIA Hopper
* NVIDIA Lovelace

**Preferred/Supported Operating System(s):** <br>
* Linux

## Training Dataset
[Describe Anything Training Datasets](https://huggingface.co/datasets/nvidia/describe-anything-dataset)

## Evaluation Dataset
We evaluate our models our detailed localized captioning benchmark: [DLC-Bench](https://huggingface.co/datasets/nvidia/DLC-Bench)

## Inference
PyTorch

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

# Citation
If you use our work or our implementation in this repo, or find them helpful, please consider giving a citation.

```
@article{lian2025describe,
  title={Describe Anything: Detailed Localized Image and Video Captioning}, 
  author={Long Lian and Yifan Ding and Yunhao Ge and Sifei Liu and Hanzi Mao and Boyi Li and Marco Pavone and Ming-Yu Liu and Trevor Darrell and Adam Yala and Yin Cui},
  journal={arXiv preprint arXiv:2504.16072},
  year={2025}
}
```