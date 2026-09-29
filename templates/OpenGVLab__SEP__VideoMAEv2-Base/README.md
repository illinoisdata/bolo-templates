---
license: cc-by-nc-4.0
tags:
- vision
- video-classification
pipeline_tag: video-classification
---

# VideoMAE-v2 (base-sized model, Pretrained on UnlabeledHybrid-1M) 

VideoMAEv2-Base model pre-trained for 800 epochs in a self-supervised way on UnlabeldHybrid-1M dataset. It was introduced in the paper [[CVPR23]VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking](https://arxiv.org/abs/2203.12602) by Wang et al. and first released in [GitHub](https://github.com/OpenGVLab/VideoMAEv2). 


## Intended uses & limitations

You can use the raw model for video feature extraction.

### How to use

Here is how to use this model to extract a video feature:

```python
from transformers import VideoMAEImageProcessor, AutoModel, AutoConfig
import numpy as np
import torch


config = AutoConfig.from_pretrained("OpenGVLab/VideoMAEv2-Base", trust_remote_code=True)
processor = VideoMAEImageProcessor.from_pretrained("OpenGVLab/VideoMAEv2-Base")
model = AutoModel.from_pretrained('OpenGVLab/VideoMAEv2-Base', config=config, trust_remote_code=True)


video = list(np.random.rand(16, 3, 224, 224))




# B, T, C, H, W -> B, C, T, H, W
inputs = processor(video, return_tensors="pt")
inputs['pixel_values'] = inputs['pixel_values'].permute(0, 2, 1, 3, 4)

with torch.no_grad():
  outputs = model(**inputs)
```




### BibTeX entry and citation info

```bibtex
@InProceedings{wang2023videomaev2,
    author    = {Wang, Limin and Huang, Bingkun and Zhao, Zhiyu and Tong, Zhan and He, Yinan and Wang, Yi and Wang, Yali and Qiao, Yu},
    title     = {VideoMAE V2: Scaling Video Masked Autoencoders With Dual Masking},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2023},
    pages     = {14549-14560}
}

@misc{videomaev2,
      title={VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking},
      author={Limin Wang and Bingkun Huang and Zhiyu Zhao and Zhan Tong and Yinan He and Yi Wang and Yali Wang and Yu Qiao},
      year={2023},
      eprint={2303.16727},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```