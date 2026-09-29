---
license: other
license_name: apple-sample-code-license
license_link: LICENSE
---

A CLIP (Contrastive Language-Image Pre-training) ViT-B/32 model trained on Conceptual Captions 12M, Conceptual Captions 3M, and Shutterstock 15M. 
Data Filtering Networks (DFNs) are small networks used to automatically filter large pools of uncurated data. 
This model is a DFN trained on publicly available data.

This model has been converted to PyTorch from the original JAX checkpoints from Axlearn (https://github.com/apple/axlearn). 


## Model Details

- **Model Type:**  Contrastive Image-Text, Zero-Shot Image Classification.
- **Dataset:** CC12M + CC3M + SS15M
- **Papers:**
  - Data Filtering Networks: https://arxiv.org/abs/2309.17425
- **Examples Seen:** 1.28B

## Citation
```bibtex
@article{fang2023data,
  title={Data Filtering Networks},
  author={Fang, Alex and Jose, Albin Madappally and Jain, Amit and Schmidt, Ludwig and Toshev, Alexander and Shankar, Vaishaal},
  journal={arXiv preprint arXiv:2309.17425},
  year={2023}
}

```