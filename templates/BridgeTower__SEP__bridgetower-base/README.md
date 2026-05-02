---
language: en
tags:
- bridgetower
license: mit
datasets:
- conceptual_captions
- sbu_captions
- visual_genome
- mscoco_captions
---

# BridgeTower base model

The BridgeTower model was proposed in "BridgeTower: Building Bridges Between Encoders in Vision-Language Representative Learning" by Xiao Xu, Chenfei Wu, Shachar Rosenman, Vasudev Lal, Wanxiang Che, Nan Duan. 
The model was pretrained on English language using masked language modeling (MLM) and image text matching (ITM)objectives. It was introduced in
[this paper](https://arxiv.org/pdf/2206.08657.pdf) and first released in
[this repository](https://github.com/microsoft/BridgeTower). 

BridgeTower got accepted to [AAAI'23](https://aaai.org/Conferences/AAAI-23/).

## Model description

The abstract from the paper is the following:
Vision-Language (VL) models with the Two-Tower architecture have dominated visual-language representation learning in recent years. Current VL models either use lightweight uni-modal encoders and learn to extract, align and fuse both modalities simultaneously in a deep cross-modal encoder, or feed the last-layer uni-modal representations from the deep pre-trained uni-modal encoders into the top cross-modal encoder. Both approaches potentially restrict vision-language representation learning and limit model performance. In this paper, we propose BridgeTower, which introduces multiple bridge layers that build a connection between the top layers of uni-modal encoders and each layer of the cross-modal encoder. This enables effective bottom-up cross-modal alignment and fusion between visual and textual representations of different semantic levels of pre-trained uni-modal encoders in the cross-modal encoder. Pre-trained with only 4M images, BridgeTower achieves state-of-the-art performance on various downstream vision-language tasks. In particular, on the VQAv2 test-std set, BridgeTower achieves an accuracy of 78.73%, outperforming the previous state-of-the-art model METER by 1.09% with the same pre-training data and almost negligible additional parameters and computational costs. Notably, when further scaling the model, BridgeTower achieves an accuracy of 81.15%, surpassing models that are pre-trained on orders-of-magnitude larger datasets.

## Intended uses & limitations(TODO)

You can use the raw model for masked language modeling, but it's mostly intended to be fine-tuned on a downstream task.
See the [model hub](https://huggingface.co/models?filter=BridgeTower) to look for fine-tuned versions on a task that
interests you.

### How to use

Here is how to use this model to get the features of a given text in PyTorch:
```python
from transformers import BridgeTowerProcessor, BridgeTowerModel
import requests
from PIL import Image

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
text = "hello world"

processor = BridgeTowerProcessor.from_pretrained("BridgeTower/bridgetower-base")
model = BridgeTowerModel.from_pretrained("BridgeTower/bridgetower-base")
# Prepare inputs
encoding = processor(image, text, return_tensors="pt")
# Forward pass
outputs = model(**encoding)
outputs.keys()
odict_keys(['text_feats', 'image_feats', 'pooler_output'])
```
### Limitations and bias

TODO

## Training data

The BridgeTower model was pretrained on four public image-caption datasets:
- [Conceptual Captions(CC)](https://ai.google.com/research/ConceptualCaptions/), 
- [SBU Captions](https://www.cs.rice.edu/~vo9/sbucaptions/),
- [MSCOCO Captions](https://arxiv.org/pdf/1504.00325.pdf),
- [Visual Genome](https://visualgenome.org/)
  
The total number of unique images in the combined data is 4M. 

## Training procedure

### Preprocessing

TODO

### Pretraining

The model was pre-trained for 100k steps on 8 NVIDIA A100 GPUs with a batch size of 4096. 
The optimizer used was AdamW with a learning rate of 1e-5. No data augmentation was used except for center-crop. The image resolution in pre-training is set to 288 x 288. 

## Evaluation results

Please refer to [Table 5](https://arxiv.org/pdf/2206.08657.pdf) for BridgeTower's performance on Image Retrieval and other downstream tasks. 


### BibTeX entry and citation info
```bibtex
@article{xu2022bridge,
  title={BridgeTower: Building Bridges Between Encoders in Vision-Language Representation Learning},
  author={Xu, Xiao and Wu, Chenfei and Rosenman, Shachar and Lal, Vasudev and Che, Wanxiang and Duan, Nan},
  journal={arXiv preprint arXiv:2206.08657},
  year={2022}
}
```