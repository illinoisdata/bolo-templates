---
license: apache-2.0
tags:
- vision
datasets:
- imagenet-21k
---

# ImageGPT (small-sized model) 

ImageGPT (iGPT) model pre-trained on ImageNet ILSVRC 2012 (14 million images, 21,843 classes) at resolution 32x32. It was introduced in the paper [Generative Pretraining from Pixels](https://cdn.openai.com/papers/Generative_Pretraining_from_Pixels_V2.pdf) by Chen et al. and first released in [this repository](https://github.com/openai/image-gpt). See also the official [blog post](https://openai.com/blog/image-gpt/).

Disclaimer: The team releasing ImageGPT did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

The ImageGPT (iGPT) is a transformer decoder model (GPT-like) pretrained on a large collection of images in a self-supervised fashion, namely ImageNet-21k, at a resolution of 32x32 pixels. 

The goal for the model is simply to predict the next pixel value, given the previous ones.

By pre-training the model, it learns an inner representation of images that can then be used to:
- extract features useful for downstream tasks: one can either use ImageGPT to produce fixed image features, in order to train a linear model (like a sklearn logistic regression model or SVM). This is also referred to as "linear probing".
- perform (un)conditional image generation. 

## Intended uses & limitations

You can use the raw model for either feature extractor or (un) conditional image generation. See the [model hub](https://huggingface.co/models?search=openai/imagegpt) to all ImageGPT variants.

### How to use

Here is how to use this model in PyTorch to perform unconditional image generation:

```python
from transformers import ImageGPTImageProcessor, ImageGPTForCausalImageModeling
import torch
import matplotlib.pyplot as plt
import numpy as np

processor = ImageGPTImageProcessor.from_pretrained('openai/imagegpt-small')
model = ImageGPTForCausalImageModeling.from_pretrained('openai/imagegpt-small')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# unconditional generation of 8 images
batch_size = 8
context = torch.full((batch_size, 1), model.config.vocab_size - 1) #initialize with SOS token
context = torch.tensor(context).to(device)
output = model.generate(pixel_values=context, max_length=model.config.n_positions + 1, temperature=1.0, do_sample=True, top_k=40)

clusters = processor.clusters
n_px = processor.size

samples = output[:,1:].cpu().detach().numpy()
samples_img = [np.reshape(np.rint(127.5 * (clusters[s] + 1.0)), [n_px, n_px, 3]).astype(np.uint8) for s in samples] # convert color cluster tokens back to pixels

f, axes = plt.subplots(1, batch_size, dpi=300)
for img, ax in zip(samples_img, axes):
   ax.axis('off')
   ax.imshow(img)
```

## Training data

The ImageGPT model was pretrained on [ImageNet-21k](http://www.image-net.org/), a dataset consisting of 14 million images and 21k classes. 

## Training procedure

### Preprocessing

Images are first resized/rescaled to the same resolution (32x32) and normalized across the RGB channels. Next, color-clustering is performed. This means that every pixel is turned into one of 512 possible cluster values. This way, one ends up with a sequence of 32x32 = 1024 pixel values, rather than 32x32x3 = 3072, which is prohibitively large for Transformer-based models. 

### Pretraining

Training details can be found in section 3.4 of v2 of the paper.

## Evaluation results

For evaluation results on several image classification benchmarks, we refer to the original paper.

### BibTeX entry and citation info

```bibtex
@InProceedings{pmlr-v119-chen20s,
  title = 	 {Generative Pretraining From Pixels},
  author =       {Chen, Mark and Radford, Alec and Child, Rewon and Wu, Jeffrey and Jun, Heewoo and Luan, David and Sutskever, Ilya},
  booktitle = 	 {Proceedings of the 37th International Conference on Machine Learning},
  pages = 	 {1691--1703},
  year = 	 {2020},
  editor = 	 {III, Hal DaumÃ© and Singh, Aarti},
  volume = 	 {119},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {13--18 Jul},
  publisher =    {PMLR},
  pdf = 	 {http://proceedings.mlr.press/v119/chen20s/chen20s.pdf},
  url = 	 {https://proceedings.mlr.press/v119/chen20s.html
}
```

```bibtex
@inproceedings{deng2009imagenet,
  title={Imagenet: A large-scale hierarchical image database},
  author={Deng, Jia and Dong, Wei and Socher, Richard and Li, Li-Jia and Li, Kai and Fei-Fei, Li},
  booktitle={2009 IEEE conference on computer vision and pattern recognition},
  pages={248--255},
  year={2009},
  organization={Ieee}
}
```