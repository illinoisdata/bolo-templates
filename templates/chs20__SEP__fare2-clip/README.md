---
license: mit
library_name: open_clip
pipeline_tag: zero-shot-image-classification
---
[[Paper]](https://arxiv.org/abs/2402.12336) [[GitHub]](https://github.com/chs20/RobustVLM)

FARE CLIP ViT-L/14 model.

Unsupervised adversarial fine-tuning from Openai CLIP initialization on ImageNet with infinity-norm and radius 2/255.

## Usage


```python
model, _, image_processor = open_clip.create_model_and_transforms('hf-hub:chs20/fare2-clip')
```


## Citation
If you find this model useful, please consider citing our paper:
```bibtex
@article{schlarmann2024robustclip,
    title={Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models}, 
    author={Christian Schlarmann and Naman Deep Singh and Francesco Croce and Matthias Hein},
    year={2024},
    journal={ICML}
}
```