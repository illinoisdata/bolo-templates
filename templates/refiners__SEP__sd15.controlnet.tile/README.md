---
license: openrail
language:
- en
library_name: refiners
pipeline_tag: image-to-image
base_model: lllyasviel/control_v11f1e_sd15_tile
base_model_relation: adapter
tags:
- image-to-image
- stable-diffusion
- sd1.5
- art
- controlnet
- controlnet-v1-1
---

# Controlnet Tile (control_v11f1e_sd15_tile)

![controlnet architecture](https://github.com/lllyasviel/ControlNet/blob/e38d22aa1ce2c2c72d2536c8f337b47249033c98/github_page/sd.png?raw=true)

## Citation

```bibtex
@misc{zhang2023adding,
  title         = {Adding Conditional Control to Text-to-Image Diffusion Models},
  author        = {Lvmin Zhang and Maneesh Agrawala},
  year          = 2023,
  url           = {https://arxiv.org/abs/2302.05543},
  eprint        = {2302.05543},
  archiveprefix = {arXiv},
  primaryclass  = {cs.CV}
}
```