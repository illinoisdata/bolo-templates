---
library_name: medvae
license: mit
pipeline_tag: image-to-image
---

# MedVAE: Efficient Automated Interpretation of Medical Images with Large-Scale Generalizable Autoencoders

The model was presented in the paper [MedVAE: Efficient Automated Interpretation of Medical Images with Large-Scale Generalizable Autoencoders](https://huggingface.co/papers/2502.14753).

**Abstract:** Medical images are acquired at high resolutions with large fields of view in order to capture fine-grained features necessary for clinical decision-making. Consequently, training deep learning models on medical images can incur large computational costs. In this work, we address the challenge of downsizing medical images in order to improve downstream computational efficiency while preserving clinically-relevant features. We introduce MedVAE, a family of six large-scale 2D and 3D autoencoders capable of encoding medical images as downsized latent representations and decoding latent representations back to high-resolution images. We train MedVAE autoencoders using a novel two-stage training approach with 1,052,730 medical images. Across diverse tasks obtained from 20 medical image datasets, we demonstrate that (1) utilizing MedVAE latent representations in place of high-resolution images when training downstream models can lead to efficiency benefits (up to 70x improvement in throughput) while simultaneously preserving clinically-relevant features and (2) MedVAE can decode latent representations back to high-resolution images with high fidelity. Our work demonstrates that large-scale, generalizable autoencoders can help address critical efficiency challenges in the medical domain.


## Model Description
MedVAE is a family of six large-scale, generalizable 2D and 3D variational autoencoders (VAEs) designed for medical imaging. It is trained on over one million medical images across multiple anatomical regions and modalities. MedVAE autoencoders encode medical images as downsized latent representations and decode latent representations back to high-resolution images. Across diverse tasks obtained from 20 medical image datasets, we demonstrate that utilizing MedVAE latent representations in place of high-resolution images when training downstream models can lead to efficiency benefits (up to 70x improvement in throughput) while simultaneously preserving clinically-relevant features.

| Total Compression Factor | Channels | Dimensions | Modalities | Anatomies | Config File | Model File |
|---|---|---|---|---|---|---|
| 16 | 1 | 2D | X-ray | Chest, Breast (FFDM) | [medvae_4x1.yaml](model_weights/medvae_4x1.yaml) | [vae_4x_1c_2D.ckpt](model_weights/vae_4x_1c_2D.ckpt) |
| 16 | 3 | 2D | X-ray | Chest, Breast (FFDM) | [medvae_4x3.yaml](model_weights/medvae_4x3.yaml) | [vae_4x_3c_2D.ckpt](model_weights/vae_4x_3c_2D.ckpt) |
| 64 | 1 | 2D | X-ray | Chest, Breast (FFDM) | [medvae_8x1.yaml](model_weights/medvae_8x1.yaml) | [vae_8x_1c_2D.ckpt](model_weights/vae_8x_1c_2D.ckpt) |
| 64 | 3 | 2D | X-ray | Chest, Breast (FFDM) | [medvae_8x4.yaml](model_weights/medvae_8x4.yaml) | [vae_8x_4c_2D.ckpt](model_weights/vae_8x_4c_2D.ckpt) |
| 64 | 1 | 3D | MRI, CT | Whole-Body | [medvae_4x1.yaml](model_weights/medvae_4x1.yaml) | [vae_4x_1c_3D.ckpt](model_weights/vae_4x_1c_3D.ckpt) |
| 512 | 1 | 3D | MRI, CT | Whole-Body | [medvae_8x1.yaml](model_weights/vae_8x1.yaml) | [vae_8x_1c_3D.ckpt](model_weights/vae_8x_1c_3D.ckpt) |

Note: Model weights and checkpoints are located in the `model_weights` folder.

## Installation
To install MedVAE, you can simply run:

```python
pip install medvae
```

For an editable installation, use the following commands to clone and install this repository:

```bash
git clone https://github.com/StanfordMIMI/MedVAE.git
cd MedVAE
pip install -e .[dev]
```

## Usage
A simple example using the `medvae` library for inference:

```python
import torch
from medvae import MVAE

fpath = "documentation/data/mmg_data/isJV8hQ2hhJsvEP5rdQNiy.png"  # Replace with your image path
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = MVAE(model_name="medvae_4_3_2d", modality="xray").to(device)
img = model.apply_transform(fpath).to(device)

model.requires_grad_(False)
model.eval()

with torch.no_grad():
    latent = model(img)
```

We also provide an easy-to-use CLI inference tool:

```bash
medvae_inference -i INPUT_FOLDER -o OUTPUT_FOLDER -model_name MED_VAE_MODEL -modality MODALITY
```

For more detailed instructions, refer to the [Github repository](https://github.com/StanfordMIMI/MedVAE).


## Citation
If you use MedVAE, please cite the original paper:

```bibtex
@misc{varma2025medvaeefficientautomatedinterpretation,
      title={MedVAE: Efficient Automated Interpretation of Medical Images with Large-Scale Generalizable Autoencoders}, 
      author={Maya Varma and Ashwin Kumar and Rogier van der Sluijs and Sophie Ostmeier and Louis Blankemeier and Pierre Chambon and Christian Bluethgen and Jip Prince and Curtis Langlotz and Akshay Chaudhari},
      year={2025},
      eprint={2502.14753},
      archivePrefix={arXiv},
      primaryClass={eess.IV},
      url={https://arxiv.org/abs/2502.14753}, 
}
```

For questions, please open an issue on the [Github repository](https://github.com/StanfordMIMI/MedVAE).