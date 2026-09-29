---
library_name: dust3r
tags:
- image-to-3d
- model_hub_mixin
- pytorch_model_hub_mixin
license: cc-by-nc-sa-4.0
---

## MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion

<video controls>
  <source src="https://monst3r-project.github.io/files/teaser_vid_v2_lowres.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

```bibtex
@article{zhang2024monst3r,
  author    = {Zhang, Junyi and Herrmann, Charles and Hur, Junhwa and Jampani, Varun and Darrell, Trevor and Cole, Forrester and Sun, Deqing and Yang, Ming-Hsuan},
  title     = {MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion},
  journal   = {arXiv preprint arxiv:2410.03825},
  year      = {2024}
}
```

# Model info

- GitHub page: https://github.com/junyi42/monst3r
- Project page: https://monst3r-project.github.io/
- Paper: https://arxiv.org/abs/2410.03825

# How to use

First, [install monst3r](https://github.com/junyi42/monst3r).
To load the model:

```python
from dust3r.model import AsymmetricCroCo3DStereo
import torch

model = AsymmetricCroCo3DStereo.from_pretrained("Junyi42/MonST3R_PO-TA-S-W_ViTLarge_BaseDecoder_512_dpt")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)