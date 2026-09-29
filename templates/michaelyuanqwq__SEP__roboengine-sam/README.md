---
datasets:
- michaelyuanqwq/roboseg
license: mit
pipeline_tag: image-segmentation
tags:
- segmentation
- robotics
- computer-vision
---

# RoboEngine: Plug-and-Play Robot Data Augmentation with Semantic Robot Segmentation and Background Generation

**[Chengbo Yuan*](https://michaelyuancb.github.io/), [Suraj Joshi*](https://x.com/nonlinearjunkie), [Shaoting Zhu*](https://zst1406217.github.io/), [Hang Su](https://scholar.google.com/citations?user=dxN1_X0AAAAJ&hl=en), [Hang Zhao](https://hangzhaomit.github.io/), [Yang Gao](https://yang-gao.weebly.com/).**

**[[Project Website](https://roboengine.github.io/)] [[Hugging Face Paper](https://huggingface.co/papers/2503.18738)] [[arXiv](https://arxiv.org/abs/2503.18738)] [[GitHub Code](https://github.com/michaelyuancb/roboengine)] [[BibTex](#jump)]**

This repository contains the Robo-SAM checkpoints from the paper "RoboEngine: Plug-and-Play Robot Data Augmentation with Semantic Robot Segmentation and Background Generation". RoboEngine introduces the first plug-and-play visual robot data augmentation toolkit, enabling users to effortlessly generate physics- and task-aware robot scenes with just a few lines of code. It significantly enhances the visual robustness of imitation learning by addressing limitations of existing methods.

## Abstract
Visual augmentation has become a crucial technique for enhancing the visual robustness of imitation learning. However, existing methods are often limited by prerequisites such as camera calibration or the need for controlled environments (e.g., green screen setups). In this work, we introduce RoboEngine, the first plug-and-play visual robot data augmentation toolkit. For the first time, users can effortlessly generate physics- and task-aware robot scenes with just a few lines of code. To achieve this, we present a novel robot scene segmentation dataset, a generalizable high-quality robot segmentation model, and a fine-tuned background generation model, which together form the core components of the out-of-the-box toolkit. Using RoboEngine, we demonstrate the ability to generalize robot manipulation tasks across six entirely new scenes, based solely on demonstrations collected from a single scene, achieving a more than 200% performance improvement compared to the no-augmentation baseline. All datasets, model weights, and the toolkit are released this https URL.

## Usage

Refer to the [official GitHub repository](https://github.com/michaelyuancb/roboengine).

## Citation

```bibtex
@article{yuan2025roboengine,
  title={RoboEngine: Plug-and-Play Robot Data Augmentation with Semantic Robot Segmentation and Background Generation},
  author={Yuan, Chengbo and Joshi, Suraj and Zhu, Shaoting and Su, Hang and Zhao, Hang and Gao, Yang},
  journal={arXiv preprint arXiv:2503.18738},
  year={2025}
}
```