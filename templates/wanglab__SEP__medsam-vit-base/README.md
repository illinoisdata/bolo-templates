---
license: apache-2.0
---

# Model Card for Segment Anything Model (SAM) - ViT Base (ViT-B) version, fine-tuned for medical image segmentation

<p>
	<img src="https://s3.amazonaws.com/moonup/production/uploads/62441d1d9fdefb55a0b7d12c/F1LWM9MXjHJsiAtgBFpDP.png" alt="Model architecture">
	<em> Detailed architecture of Segment Anything Model (SAM).</em>
</p>


#  Table of Contents

0. [TL;DR](#TL;DR)
1. [Model Details](#model-details)
2. [Usage](#usage)
3. [Citation](#citation)

# TL;DR


[Link to original SAM repository](https://github.com/facebookresearch/segment-anything)
[Link to original MedSAM repository](https://github.com/bowang-lab/medsam)

| <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/sam-beancans.png" alt="Snow" width="600" height="600"> | <img src="https://s3.amazonaws.com/moonup/production/uploads/62441d1d9fdefb55a0b7d12c/wHXbJx1oXqHCYNeUNKHs8.png" alt="Forest" width="600" height="600"> | <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/sam-car-seg.png" alt="Mountains" width="600" height="600"> |
|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|


The **Segment Anything Model (SAM)** produces high-quality object masks from input prompts such as points or boxes, and it can be used to generate masks for all objects in an image. It has been trained on a [dataset](https://segment-anything.com/dataset/index.html) of 11 million images and 1.1 billion masks, and has strong zero-shot performance on a variety of segmentation tasks.
The abstract of the paper states:

>  We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. Using our efficient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on 11M licensed and privacy respecting images. The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks. We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive -- often competitive with or even superior to prior fully supervised results. We are releasing the Segment Anything Model (SAM) and corresponding dataset (SA-1B) of 1B masks and 11M images at [https://segment-anything.com](https://segment-anything.com) to foster research into foundation models for computer vision.

**Disclaimer**: Content from **this** model card has been written by the Hugging Face team, and parts of it were copy pasted from the original [SAM model card](https://github.com/facebookresearch/segment-anything).

# Model Details

The SAM model is made up of 3 modules:
  - The `VisionEncoder`: a VIT based image encoder. It computes the image embeddings using attention on patches of the image. Relative Positional Embedding is used.
  - The `PromptEncoder`: generates embeddings for points and bounding boxes
  - The `MaskDecoder`: a two-ways transformer which performs cross attention between the image embedding and the point embeddings (->) and between the point embeddings and the image embeddings. The outputs are fed
  - The `Neck`: predicts the output masks based on the contextualized masks produced by the `MaskDecoder`.

# Usage

Refer to the demo notebooks:

- [this one](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/SAM/Run_inference_with_MedSAM_using_HuggingFace_Transformers.ipynb) showcasing inference with MedSAM
- [this one](https://github.com/huggingface/notebooks/blob/main/examples/segment_anything.ipynb) showcasing general usage of SAM,

as well as the [docs](https://huggingface.co/docs/transformers/main/en/model_doc/sam).


# Citation

If you use this model, please use the following BibTeX entry.

```
@article{kirillov2023segany,
  title={Segment Anything},
  author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
  journal={arXiv:2304.02643},
  year={2023}
}
```