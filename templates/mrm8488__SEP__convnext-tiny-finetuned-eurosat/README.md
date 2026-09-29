---
license: apache-2.0
tags:
- generated_from_trainer
- CV
- ConvNeXT
- satellite
- EuroSAT
datasets:
- nielsr/eurosat-demo
metrics:
- accuracy
model-index:
- name: convnext-tiny-finetuned-eurosat
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: image_folder
      type: image_folder
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9804938271604938
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ConvNeXT (tiny) fine-tuned on EuroSAT

This model is a fine-tuned version of [facebook/convnext-tiny-224](https://huggingface.co/facebook/convnext-tiny-224) on the [EuroSAT](https://github.com/phelber/eurosat) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0549
- Accuracy: 0.9805

#### Drag and drop the following pics in the right widget to test the model

![image1](https://huggingface.co/mrm8488/convnext-tiny-finetuned-eurosat/resolve/main/test1.jpg)
![image2](https://huggingface.co/mrm8488/convnext-tiny-finetuned-eurosat/resolve/main/test2.jpg)


## Model description

ConvNeXT is a pure convolutional model (ConvNet), inspired by the design of Vision Transformers, that claims to outperform them. The authors started from a ResNet and "modernized" its design by taking the Swin Transformer as inspiration.

## Dataset information

**EuroSAT : Land Use and Land Cover Classification with Sentinel-2**

In this study, we address the challenge of land use and land cover classification using Sentinel-2 satellite images. The Sentinel-2 satellite images are openly and freely accessible provided in the Earth observation program Copernicus. We present a novel dataset based on Sentinel-2 satellite images covering 13 spectral bands and consisting out of 10 classes with in total 27,000 labeled and geo-referenced images. We provide benchmarks for this novel dataset with its spectral bands using state-of-the-art deep Convolutional Neural Network (CNNs). With the proposed novel dataset, we achieved an overall classification accuracy of 98.57%. The resulting classification system opens a gate towards a number of Earth observation applications. We demonstrate how this classification system can be used for detecting land use and land cover changes and how it can assist in improving geographical maps.

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 7171
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2082        | 1.0   | 718  | 0.1057          | 0.9654   |
| 0.1598        | 2.0   | 1436 | 0.0712          | 0.9775   |
| 0.1435        | 3.0   | 2154 | 0.0549          | 0.9805   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1