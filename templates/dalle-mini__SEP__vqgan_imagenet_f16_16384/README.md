## VQGAN-f16-16384

### Model Description

This is a Flax/JAX implementation of VQGAN, which learns a codebook of context-rich visual parts by leveraging both the use of convolutional methods and transformers. It was introduced in [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/) ([CVPR paper](https://openaccess.thecvf.com/content/CVPR2021/html/Esser_Taming_Transformers_for_High-Resolution_Image_Synthesis_CVPR_2021_paper.html)).

The model allows the encoding of images as a fixed-length sequence of tokens taken from the codebook.

This version of the model uses a reduction factor `f=16` and a vocabulary of `16,384` tokens.

As an example of how the reduction factor works, images of size `256x256` are encoded to sequences of `256` tokens: `256/16 * 256/16`. Images of `512x512` would result in sequences of `1024` tokens.

This model was ported to JAX using [a checkpoint trained on ImageNet](https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/).

### How to Use

The checkpoint can be loaded using [Suraj Patil's implementation](https://github.com/patil-suraj/vqgan-jax) of `VQModel`.

### Other

This model can be used as part of the implementation of [DALL·E mini](https://github.com/borisdayma/dalle-mini). Our [report](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-mini--Vmlldzo4NjIxODA) contains more details on how to leverage it in an image encoding / generation pipeline.