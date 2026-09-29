---
tags:
- timm
- transformers
- image-feature-extraction
- siglip
- siglip2
library_name: timm
license: apache-2.0
datasets:
- webli
---
# Model card for vit_base_patch16_siglip_224.v2_webli

A SigLIP 2 ViT (image encoder only) for `timm`. Equivalent to image tower from https://huggingface.co/timm/ViT-B-16-SigLIP2.


## Model Details
- **Dataset:** webli
- **Papers:**
  - SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features: https://arxiv.org/abs/2502.14786
  - Sigmoid Loss for Language Image Pre-Training: https://arxiv.org/abs/2303.15343

## Citation
```bibtex
@article{tschannen2025siglip,
          title={SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features},
          author={Tschannen, Michael and Gritsenko, Alexey and Wang, Xiao and Naeem, Muhammad Ferjad and Alabdulmohsin, Ibrahim and Parthasarathy, Nikhil and Evans, Talfan and Beyer, Lucas and Xia, Ye and Mustafa, Basil and H'enaff, Olivier and Harmsen, Jeremiah and Steiner, Andreas and Zhai, Xiaohua},
          year={2025},
          journal={arXiv preprint arXiv:2502.14786}
        }
        
```
```bibtex
@inproceedings{zhai2023sigmoid,
          title={Sigmoid loss for language image pre-training},
          author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
          booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
          pages={11975--11986},
          year={2023}
        }
        
```
