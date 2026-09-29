---
library_name: transformers
metrics:
- accuracy
tags:
- realism
- bad anatomy
- image classifier
- Finetuned VIT
---

# Model Card for Bad-Anatomy-Realism-Classifier

A finetuned Vision Transformer model for classifying AI-generated pictures for bad anatomy and realism.

This model is currently a support model for my Youtube series. Feel free to build on top of this.

## Model Detail

<!-- Provide a quick summary of what the model is/does. -->
**Detecting Bad Anatomy in Realistic AI-Generated Images** - Not all Image Generation models generate images with good anatomy. Some might generate the typical "bad hands" where the hand might have more than 5 fingers. This model's goaal is to detect such anatomy issues in AI-generated images.

**Determining True Realism Versus AI Realism** - AI-generated images tend to have an issue when attempting to achieve realism, which is the skin and generation style. Compared to a normal post on social media, a High-Definition upscaled AI-generated image can be easily identified by, characteristic such as shiny skin or very bright lighting. Below are some examples of such:

<img src="https://huggingface.co/angusleung100/bad-anatomy-realism-classifier/resolve/main/Unrealistic_Good_Anatomy_29.png" alt="Unrealistic Good Anatomy AI-generated image number 29" width="512" height="512"/>
<img src="https://huggingface.co/angusleung100/bad-anatomy-realism-classifier/resolve/main/Unrealistic_Good_Anatomy_31.png" alt="Unrealistic Good Anatomy AI-generated image number 31" width="512" height="512"/>

### Model Description

<!-- Provide a longer summary of what this model is. -->

This was fine-tuned on the [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) Vision Transformer (ViT).

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
- Detecting whether an image is actually real or is a very well AI-generated image
- Detecting bad anatomy in AI-generated images to trigger a regeneration

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
- Racism
- Illegal activities where doing illegal things is a crime

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
This initial model was trained on images generated on Stable Diffusion v1.5 on the [Beautiful Realistic Asians v6](https://civitai.com/models/25494?modelVersionId=113479) checkpoint by pleasebankai. 

The dataset for this model was only 134 images, with only 6 being Unrealistic Bad Anatomy. (Additions of dataset details will be placed in the model card in later updates to documentation)

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Recommendation is to build on the dataset and continue training with more variety of characters to raise performance for images that do not conform to the characteristics of images used in training.

## How to Get Started with the Model

### Finetuning
Please refer to the initial finetune script for this model in the supporting Github Repository here: [https://github.com/angusleung100/barc-finetuning-gh](https://github.com/angusleung100/barc-finetuning-gh)

### Using The Model For Classification
Please refer to the Hugging Face documentation example here for Image Classification: [https://huggingface.co/docs/transformers/en/tasks/image_classification#inference](https://huggingface.co/docs/transformers/en/tasks/image_classification#inference)

## Training Details

### Training and Testing Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

## Dataset Image Label Criteria

### Bad / Good Anatomy
- Any deformed body parts or extra limbs for the character
- Background does not overly matte (As it can always be removed or changed in post-processing with professional editing software)

### Realistic vs. Unrealistic
The criteria is more interesting for determining realism. Since a lot of people like to use filters now, it's actually quite hard to determine what is a good standard for realism. Here is what I narrowed it down to for this model:
- **First glance reaction** - Do I take a closer look and feel skeptical? Or do I know instantly it isn't real.
- **Lighting** - It is easier to sort amateur style images since I can move onto the next criteria first. Some professional images do look AI-generated but are actually heavily edited. But we can definitely base it also off of unnatural lighting
- **Skin and hair** - If the skin and hair are too shiny (Like the images at the start of the Model Card) or there is not enough detail on an upscaled image. Or there is TOO much detail on an upscaled image.
- **Photography style** - This could lead to false positives or false negatives, but if the shot looks like the focal point is weird or just very airbrushed, it could be unrealistic

Overall it is based on "gut feeling" for the sorting. The model also has a goal to be able to replicate "gut feeling" and just your underlying feel for the image.

### Compatible Images For Dataset
Since the default data collator is used and images are primarily from SD 1.5, I am not entirely certain whether images and sizes from different models will break the training, even if the testing pipeline didn't have any problems for the 3 images we used later on.

Here are a list of models where default image sizes should work:
- Stable Diffusion 1.5
- OpenDalle v1.1
- Flux 1
- Dall-E 3 on Copilot

## Dataset Stats
```
Number Images Per Label
=======================
Realistic Bad Anatomy: 6 (4.48%)
Realistic Good Anatomy: 15 (11.19%)
Unrealistic Bad Anatomy: 81 (60.45%)
Unrealistic Good Anatomy: 32 (23.88%)

Total Number of Images:  134
```

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Results

```
***** train metrics *****
  epoch                    =        3.0
  total_flos               = 20135801GF
  train_loss               =     0.8453
  train_runtime            = 0:00:42.83
  train_samples_per_second =      6.514
  train_steps_per_second   =      0.841
```

```
***** eval metrics *****
  epoch                   =        3.0
  eval_accuracy           =     0.6341
  eval_f1                 =      0.513
  eval_loss               =     0.8219
  eval_precision          =      0.464
  eval_recall             =     0.6341
  eval_runtime            = 0:00:06.95
  eval_samples_per_second =      5.893
  eval_steps_per_second   =      0.862
```

#### Summary
The initial dataset and finetune resulted in a 64.41% accuracy and 51.3% F1 score, which is low but expected for a small amateur dataset. 

Hopefully I will have time to further build on the dataset and improve the model's performance in the future.

**The next steps would be:**
- Have more variety of characters and poses
- More variety of clothing styles and lighting
- Different camera styles
- Different model generations from different models -> Currently dominated by the SD1.5 BRAV6 and BRAV7 checkpoints 


## Model Examination

<!-- Relevant interpretability work for the model goes here -->

You can view example pipeline inferences and their results on the [Initial Finetune notebook](https://nbviewer.org/github/angusleung100/barc-finetuning-gh/blob/main/Bad_Anatomy_and_Realism_Classification_Model_Initial_Fine_Tune.ipynb)

The examples are at the bottom of the notebook. You can do ```ctr+f``` and search for ```Test Model With Custom Inputs``` to reach it faster.

## Model Card Contact

Feel free to contact me if you have any questions or find me on Github

- [Twitter](https://twitter.com/angusleung100)
- [Github](https://github.com/angusleung100)