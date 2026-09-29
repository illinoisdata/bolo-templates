---
license: other
license_name: tencent-hunyuanworld-mirror-community
license_link: https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror/blob/main/License.txt
language:
- en
- zh
tags:
- hunyuan3d
- worldmodel
- 3d-reconstruction
- 3d-generation
- 3d
- scene-generation
- image-to-3D
- video-to-3D
pipeline_tag: image-to-3d
extra_gated_eu_disallowed: true
---

<p align="center">
  <img src="assets/teaser.jpg" width="95%" alt="HunyuanWorld-Mirror Teaser">
</p>

<p align="center">
<a href='https://3d-models.hunyuan.tencent.com/world/'><img src='https://img.shields.io/badge/Project-Page-green'></a>
<a href='https://3d-models.hunyuan.tencent.com/world/worldMirror1_0/HYWorld_Mirror_Tech_Report.pdf'><img src='https://img.shields.io/badge/Technique-Report-red'></a>
<a href='https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror'><img src='https://img.shields.io/badge/Github-Page-Green'></a>
<a href='https://huggingface.co/spaces/tencent/HunyuanWorld-Mirror'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Demo-orange'></a>
<a href=https://discord.gg/dNBrdrGGMa target="_blank"><img src= https://img.shields.io/badge/Discord-white.svg?logo=discord height=22px></a>
  <a href=https://x.com/TencentHunyuan target="_blank"><img src=https://img.shields.io/badge/Hunyuan-black.svg?logo=x height=22px></a>
<p align="center">



HunyuanWorld-Mirror is a versatile feed-forward model for comprehensive 3D geometric prediction. It integrates diverse geometric priors (**camera poses**, **calibrated intrinsics**, **depth maps**) and simultaneously generates various 3D representations (**point clouds**, **multi-view depths**, **camera parameters**, **surface normals**, **3D Gaussians**) in a single forward pass.


## ☯️ **HunyuanWorld-Mirror Introduction**

### Architecture
HunyuanWorld-Mirror consists of two key components:

**(1) Multi-Modal Prior Prompting**: A mechanism that embeds diverse prior modalities,
including calibrated intrinsics, camera pose, and depth, into the feed-forward model. Given any subset of the available priors, we utilize several lightweight encoding layers to convert each modality into structured tokens.

**(2) Universal Geometric Prediction**: A unified architecture capable of handling
the full spectrum of 3D reconstruction tasks from camera and depth estimation to point map regression, surface normal estimation, and novel view synthesis. 

<p align="left">
  <img src="assets/arch.png">
</p>


## 🔗 BibTeX

If you find HunyuanWorld-Mirror useful for your research and applications, please cite using this BibTeX:

```BibTeX
@article{liu2025worldmirror,
  title={WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting},
  author={Liu, Yifan and Min, Zhiyuan and Wang, Zhenwei and Wu, Junta and Wang, Tengfei and Yuan, Yixuan and Luo, Yawei and Guo, Chunchao},
  journal={arXiv preprint arXiv:2510.10726},
  year={2025}
}
```

## Acknowledgements
We would like to thank [HunyuanWorld](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0). We also sincerely thank the authors and contributors of [VGGT](https://github.com/facebookresearch/vggt), [Fast3R](https://github.com/facebookresearch/fast3r), [CUT3R](https://github.com/CUT3R/CUT3R), and [DUSt3R](https://github.com/naver/dust3r) for their outstanding open-source work and pioneering research.