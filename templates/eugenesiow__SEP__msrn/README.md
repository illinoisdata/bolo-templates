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
# Multi-scale Residual Network for Image Super-Resolution (MSRN)
MSRN model pre-trained on DIV2K (800 images training, augmented to 4000 images, 100 images validation) for 2x, 3x and 4x image super resolution. It was introduced in the paper [Multi-scale Residual Network for Image Super-Resolution](https://openaccess.thecvf.com/content_ECCV_2018/html/Juncheng_Li_Multi-scale_Residual_Network_ECCV_2018_paper.html) by Li et al. (2018) and first released in [this repository](https://github.com/MIVRC/MSRN-PyTorch). 

The goal of image super resolution is to restore a high resolution (HR) image from a single low resolution (LR) image. The image below shows the ground truth (HR), the bicubic upscaling x2 and model upscaling x2.

![Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 4](images/msrn_4_4_compare.png "Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 4")
## Model description
The MSRN model proposes a feature extraction structure called the multi-scale residual block. This module can "adaptively detect image features at different scales" and "exploit the potential features of the image".
## Intended uses & limitations
You can use the pre-trained models for upscaling your images 2x, 3x and 4x. You can also use the trainer to train a model on your own dataset.
### How to use
The model can be used with the [super_image](https://github.com/eugenesiow/super-image) library:
```bash
pip install super-image
```
Here is how to use a pre-trained model to upscale your image:
```python
from super_image import MsrnModel, ImageLoader
from PIL import Image
import requests

url = 'https://paperswithcode.com/media/datasets/Set5-0000002728-07a9793f_zA3bDjj.jpg'
image = Image.open(requests.get(url, stream=True).raw)

model = MsrnModel.from_pretrained('eugenesiow/msrn', scale=4)           # scale 2, 3 and 4 models available
inputs = ImageLoader.load_image(image)
preds = model(inputs)

ImageLoader.save_image(preds, './scaled_4x.png')                        # save the output 4x scaled image to `./scaled_4x.png`
ImageLoader.save_compare(inputs, preds, './scaled_4x_compare.png')      # save an output comparing the super-image with a bicubic scaling
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
from super_image import Trainer, TrainingArguments, MsrnModel, MsrnConfig

training_args = TrainingArguments(
    output_dir='./results',                 # output directory
    num_train_epochs=1000,                  # total number of training epochs
)

config = MsrnConfig(
    scale=4,                                # train a model to upscale 4x
)
model = MsrnModel(config)

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

|Dataset  	    |Scale      |Bicubic  	        |msrn  	                        |
|---	        |---	    |---	            |---	                        |
|Set5  	        |2x         |33.64/0.9292       |**38.08/0.9609**               |
|Set5  	        |3x  	    |30.39/0.8678  	    |**35.12/0.9409**  	            |
|Set5  	        |4x  	    |28.42/0.8101  	    |**32.19/0.8951**               |
|Set14  	    |2x         |30.22/0.8683  	    |**33.75/0.9183**  	            |
|Set14  	    |3x         |27.53/0.7737  	    |**31.08/0.8593**  	            |
|Set14  	    |4x         |25.99/0.7023  	    |**28.78/0.7862**  	            |
|BSD100  	    |2x  	    |29.55/0.8425  	    |**33.82/0.9258**  	            |
|BSD100  	    |3x  	    |27.20/0.7382  	    |**29.67/0.8198**  	            |
|BSD100  	    |4x  	    |25.96/0.6672  	    |**28.53/0.7657**  	            |
|Urban100  	    |2x  	    |26.66/0.8408  	    |**32.14/0.9287**  	            |
|Urban100  	    |3x  	    |  	                |**29.31/0.8743** 	            |
|Urban100  	    |4x  	    |23.14/0.6573  	    |**26.12/0.7866**  	            |

![Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 2](images/msrn_2_4_compare.png "Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 2")

You can find a notebook to easily run evaluation on pretrained models below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/super-image-notebooks/blob/master/notebooks/Evaluate_Pretrained_super_image_Models.ipynb "Open in Colab")

## BibTeX entry and citation info
```bibtex
@InProceedings{Agustsson_2017_CVPR_Workshops,
    author = {Agustsson, Eirikur and Timofte, Radu},
    title = {NTIRE 2017 Challenge on Single Image Super-Resolution: Dataset and Study},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    url = "http://www.vision.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf",
    month = {July},
    year = {2017}
} 
```