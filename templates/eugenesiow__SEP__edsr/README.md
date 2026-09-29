---
license: apache-2.0
tags:
- super-image
- image-super-resolution
datasets:
- eugenesiow/Div2k
- eugenesiow/Set5
- eugenesiow/Set14
- eugenesiow/BSD100
- eugenesiow/Urban100
metrics:
- pnsr
- ssim
---
# Enhanced Deep Residual Networks for Single Image Super-Resolution (EDSR)
EDSR model pre-trained on DIV2K (800 images training, augmented to 4000 images, 100 images validation) for 2x, 3x and 4x image super resolution. It was introduced in the paper [Enhanced Deep Residual Networks for Single Image Super-Resolution](https://arxiv.org/abs/1707.02921) by Lim et al. (2017) and first released in [this repository](https://github.com/sanghyun-son/EDSR-PyTorch). 

The goal of image super resolution is to restore a high resolution (HR) image from a single low resolution (LR) image. The image below shows the ground truth (HR), the bicubic upscaling x2 and EDSR upscaling x2.

![Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 4](images/edsr_4_4_compare.png "Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 4")
## Model description
EDSR is a model that uses both deeper and wider architecture (32 ResBlocks and 256 channels) to improve performance. It uses both global and local skip connections, and up-scaling is done at the end of the network. It doesn't use batch normalization layers (input and output have similar distributions, normalizing intermediate features may not be desirable) instead it uses constant scaling layers to ensure stable training. An L1 loss function (absolute error) is used instead of L2 (MSE), the authors showed better performance empirically and it requires less computation.

This is a base model (~5mb vs ~100mb) that includes just 16 ResBlocks and 64 channels.
## Intended uses & limitations
You can use the pre-trained models for upscaling your images 2x, 3x and 4x. You can also use the trainer to train a model on your own dataset.
### How to use
The model can be used with the [super_image](https://github.com/eugenesiow/super-image) library:
```bash
pip install super-image
```
Here is how to use a pre-trained model to upscale your image:
```python
from super_image import EdsrModel, ImageLoader
from PIL import Image
import requests

url = 'https://paperswithcode.com/media/datasets/Set5-0000002728-07a9793f_zA3bDjj.jpg'
image = Image.open(requests.get(url, stream=True).raw)

model = EdsrModel.from_pretrained('eugenesiow/edsr', scale=2)      # scale 2, 3 and 4 models available
inputs = ImageLoader.load_image(image)
preds = model(inputs)

ImageLoader.save_image(preds, './scaled_2x.png')                        # save the output 2x scaled image to `./scaled_2x.png`
ImageLoader.save_compare(inputs, preds, './scaled_2x_compare.png')      # save an output comparing the super-image with a bicubic scaling
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/super-image-notebooks/blob/master/notebooks/Upscale_Images_with_Pretrained_super_image_Models.ipynb "Open in Colab")
## Training data
The models for 2x, 3x and 4x image super resolution were pretrained on [DIV2K](https://huggingface.co/datasets/eugenesiow/Div2k), a dataset of 800 high-quality (2K resolution) images for training, augmented to 4000 images and uses a dev set of  100 validation images (images numbered 801 to 900). 
## Training procedure
### Preprocessing
We follow the pre-processing and training method of [Wang et al.](https://arxiv.org/abs/2104.07566).
Low Resolution (LR) images are created by using bicubic interpolation as the resizing method to reduce the size of the High Resolution (HR) images by x2, x3 and x4 times.
During training, RGB patches with size of 64×64 from the LR input are used together with their corresponding HR patches. 
Data augmentation is applied to the training set in the pre-processing stage where five images are created from the four corners and center of the original image. 

We need the huggingface [datasets](https://huggingface.co/datasets?filter=task_ids:other-other-image-super-resolution) library to download the data:
```bash
pip install datasets
```
The following code gets the data and preprocesses/augments the data.

```python
from datasets import load_dataset
from super_image.data import EvalDataset, TrainDataset, augment_five_crop

augmented_dataset = load_dataset('eugenesiow/Div2k', 'bicubic_x4', split='train')\
    .map(augment_five_crop, batched=True, desc="Augmenting Dataset")                                # download and augment the data with the five_crop method
train_dataset = TrainDataset(augmented_dataset)                                                     # prepare the train dataset for loading PyTorch DataLoader
eval_dataset = EvalDataset(load_dataset('eugenesiow/Div2k', 'bicubic_x4', split='validation'))      # prepare the eval dataset for the PyTorch DataLoader
```
### Pretraining
The model was trained on GPU. The training code is provided below:
```python
from super_image import Trainer, TrainingArguments, EdsrModel, EdsrConfig

training_args = TrainingArguments(
    output_dir='./results',                 # output directory
    num_train_epochs=1000,                  # total number of training epochs
)

config = EdsrConfig(
    scale=4,                                # train a model to upscale 4x
)
model = EdsrModel(config)

trainer = Trainer(
    model=model,                         # the instantiated model to be trained
    args=training_args,                  # training arguments, defined above
    train_dataset=train_dataset,         # training dataset
    eval_dataset=eval_dataset            # evaluation dataset
)

trainer.train()
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/super-image-notebooks/blob/master/notebooks/Train_super_image_Models.ipynb "Open in Colab")
## Evaluation results
The evaluation metrics include [PSNR](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio#Quality_estimation_with_PSNR) and [SSIM](https://en.wikipedia.org/wiki/Structural_similarity#Algorithm). 

Evaluation datasets include:
- Set5 - [Bevilacqua et al. (2012)](https://huggingface.co/datasets/eugenesiow/Set5)
- Set14 - [Zeyde et al. (2010)](https://huggingface.co/datasets/eugenesiow/Set14)
- BSD100 - [Martin et al. (2001)](https://huggingface.co/datasets/eugenesiow/BSD100)
- Urban100 - [Huang et al. (2015)](https://huggingface.co/datasets/eugenesiow/Urban100)

The results columns below are represented below as `PSNR/SSIM`. They are compared against a Bicubic baseline.

|Dataset  	    |Scale      |Bicubic  	        |edsr  	                |
|---	        |---	    |---	            |---	                |
|Set5  	        |2x         |33.64/0.9292       |**38.19/0.9612**       |
|Set5  	        |3x  	    |30.39/0.8678  	    |**35.31/0.9421**  	    |
|Set5  	        |4x  	    |28.42/0.8101  	    |**32.5/0.8986**        |
|Set14  	    |2x         |30.22/0.8683  	    |**33.99/0.9215**  	    |
|Set14  	    |3x         |27.53/0.7737  	    |**31.18/0.862**  	    |
|Set14  	    |4x         |25.99/0.7023  	    |**28.92/0.7899**  	    |
|BSD100  	    |2x  	    |29.55/0.8425  	    |**33.89/0.9266**  	    |
|BSD100  	    |3x  	    |27.20/0.7382  	    |**29.77/0.8224**  	    |
|BSD100  	    |4x  	    |25.96/0.6672  	    |**28.62/0.7689**  	    |
|Urban100  	    |2x  	    |26.66/0.8408  	    |**32.68/0.9331**  	    |
|Urban100  	    |3x  	    |  	                |**29.75/0.8825**  	    |
|Urban100  	    |4x  	    |23.14/0.6573  	    |**26.53/0.7995**  	    |

![Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 2](images/edsr_2_4_compare.png "Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 2")

You can find a notebook to easily run evaluation on pretrained models below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/super-image-notebooks/blob/master/notebooks/Evaluate_Pretrained_super_image_Models.ipynb "Open in Colab")

## BibTeX entry and citation info
```bibtex
@InProceedings{Lim_2017_CVPR_Workshops,
  author = {Lim, Bee and Son, Sanghyun and Kim, Heewon and Nah, Seungjun and Lee, Kyoung Mu},
  title = {Enhanced Deep Residual Networks for Single Image Super-Resolution},
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
  month = {July},
  year = {2017}
}
```