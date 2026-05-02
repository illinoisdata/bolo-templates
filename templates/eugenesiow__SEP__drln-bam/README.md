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
# Densely Residual Laplacian Super-Resolution (DRLN)
DRLN model pre-trained on DIV2K (800 images training, augmented to 4000 images, 100 images validation) for 2x, 3x and 4x image super resolution. It was introduced in the paper [Densely Residual Laplacian Super-resolution](https://arxiv.org/abs/1906.12021) by Anwar et al. (2020) and first released in [this repository](https://github.com/saeed-anwar/DRLN). 

The goal of image super resolution is to restore a high resolution (HR) image from a single low resolution (LR) image. The image below shows the ground truth (HR), the bicubic upscaling and model upscaling.

![Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 4](images/drln_4_4_compare.png "Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 4")
## Model description
Super-Resolution convolutional neural networks have recently demonstrated high-quality restoration for single images. However, existing algorithms often require very deep architectures and long training times. Furthermore, current convolutional neural networks for super-resolution are unable to exploit features at multiple scales and weigh them equally, limiting their learning capability. In this exposition, we present a compact and accurate super-resolution algorithm namely, Densely Residual Laplacian Network (DRLN). The proposed network employs cascading residual on the residual structure to allow the flow of low-frequency information to focus on learning high and mid-level features. In addition, deep supervision is achieved via the densely concatenated residual blocks settings, which also helps in learning from high-level complex features. Moreover, we propose Laplacian attention to model the crucial features to learn the inter and intra-level dependencies between the feature maps. Furthermore, comprehensive quantitative and qualitative evaluations on low-resolution, noisy low-resolution, and real historical image benchmark datasets illustrate that our DRLN algorithm performs favorably against the state-of-the-art methods visually and accurately.

This model also applies the balanced attention (BAM) method invented by [Wang et al. (2021)](https://arxiv.org/abs/2104.07566) to further improve the results.
## Intended uses & limitations
You can use the pre-trained models for upscaling your images 2x, 3x and 4x. You can also use the trainer to train a model on your own dataset.
### How to use
The model can be used with the [super_image](https://github.com/eugenesiow/super-image) library:
```bash
pip install super-image
```
Here is how to use a pre-trained model to upscale your image:
```python
from super_image import DrlnModel, ImageLoader
from PIL import Image
import requests

url = 'https://paperswithcode.com/media/datasets/Set5-0000002728-07a9793f_zA3bDjj.jpg'
image = Image.open(requests.get(url, stream=True).raw)

model = DrlnModel.from_pretrained('eugenesiow/drln-bam', scale=2)      # scale 2, 3 and 4 models available
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
from super_image import Trainer, TrainingArguments, DrlnModel, DrlnConfig

training_args = TrainingArguments(
    output_dir='./results',                 # output directory
    num_train_epochs=1000,                  # total number of training epochs
)

config = DrlnConfig(
    scale=4,                                # train a model to upscale 4x
    bam=True,                               # apply balanced attention to the network
)
model = DrlnModel(config)

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

|Dataset  	    |Scale      |Bicubic  	        |drln-bam  	                    |
|---	        |---	    |---	            |---	                        |
|Set5  	        |2x         |33.64/0.9292       |**38.23/0.9614**       |
|Set5  	        |3x  	    |30.39/0.8678  	    |**35.3/0.9422**  	    |
|Set5  	        |4x  	    |28.42/0.8101  	    |**32.49/0.8986**       |
|Set14  	    |2x         |30.22/0.8683  	    |**33.95/0.9206**  	    |
|Set14  	    |3x         |27.53/0.7737  	    |**31.27/0.8624**  	    |
|Set14  	    |4x         |25.99/0.7023  	    |**28.94/0.7899**  	    |
|BSD100  	    |2x  	    |29.55/0.8425  	    |**33.95/0.9269**  	    |
|BSD100  	    |3x  	    |27.20/0.7382  	    |**29.78/0.8224**  	    |
|BSD100  	    |4x  	    |25.96/0.6672  	    |**28.63/0.7686**  	    |
|Urban100  	    |2x  	    |26.66/0.8408  	    |**32.81/0.9339**  	    |
|Urban100  	    |3x  	    |  	                |**29.82/0.8828**  	    |
|Urban100  	    |4x  	    |23.14/0.6573  	    |**26.53/0.7991**  	    |

![Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 2](images/drln_2_4_compare.png "Comparing Bicubic upscaling against the models x4 upscaling on Set5 Image 2")

You can find a notebook to easily run evaluation on pretrained models below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eugenesiow/super-image-notebooks/blob/master/notebooks/Evaluate_Pretrained_super_image_Models.ipynb "Open in Colab")

## BibTeX entry and citation info
```bibtex
@misc{wang2021bam,
    title={BAM: A Lightweight and Efficient Balanced Attention Mechanism for Single Image Super Resolution}, 
    author={Fanyi Wang and Haotian Hu and Cheng Shen},
    year={2021},
    eprint={2104.07566},
    archivePrefix={arXiv},
    primaryClass={eess.IV}
}
```

```bibtex
@misc{anwar2019densely,
      title={Densely Residual Laplacian Super-Resolution}, 
      author={Saeed Anwar and Nick Barnes},
      year={2019},
      eprint={1906.12021},
      archivePrefix={arXiv},
      primaryClass={eess.IV}
}
```