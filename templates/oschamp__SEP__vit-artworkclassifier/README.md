---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
base_model: google/vit-base-patch16-224-in21k
model-index:
- name: vit-artworkclassifier
  results:
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: artbench10-vit
      split: test
      args: artbench10-vit
    metrics:
    - type: accuracy
      value: 0.5947786606129398
      name: Accuracy
---

# vit-artworkclassifier
This model returns the artwork style of any image input.


This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset. This is a subset of the artbench-10 dataset (https://www.kaggle.com/datasets/alexanderliao/artbench10), with a train set of 1000 artworks per class and a validation set of 100 artworks per class.
It achieves the following results on the evaluation set:
- Loss: 1.1392
- Accuracy: 0.5948

## Model description

You can find a description of the project that this model was trained for here: https://medium.com/@oliverpj.schamp/training-and-evaluating-stable-diffusion-for-artwork-generation-b099d1f5b7a6

## Intended uses & limitations

This model only contains 9 out of the 10 artbench-10 classes - it does not contain ukiyo_e. This was due to availability and formatting issues.

## Training and evaluation data

Train: 1000 randomly selected images from artbench-10 (per class). Val: 100 randomly selected images from artbench-10 (per class).

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.5906        | 0.36  | 100  | 1.4709          | 0.4847   |
| 1.3395        | 0.72  | 200  | 1.3208          | 0.5074   |
| 1.1461        | 1.08  | 300  | 1.3363          | 0.5165   |
| 0.9593        | 1.44  | 400  | 1.1790          | 0.5846   |
| 0.8761        | 1.8   | 500  | 1.1252          | 0.5902   |
| 0.5922        | 2.16  | 600  | 1.1392          | 0.5948   |
| 0.4803        | 2.52  | 700  | 1.1560          | 0.5936   |
| 0.4454        | 2.88  | 800  | 1.1545          | 0.6118   |
| 0.2271        | 3.24  | 900  | 1.2284          | 0.6039   |
| 0.207         | 3.6   | 1000 | 1.2625          | 0.5959   |
| 0.1958        | 3.96  | 1100 | 1.2621          | 0.6005   |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.1+cu117
- Datasets 2.9.0
- Tokenizers 0.13.2

### Code to Run
```
def vit_classify(image):
    vit = ViTForImageClassification.from_pretrained("oschamp/vit-artworkclassifier")
    vit.eval()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    vit.to(device)
    
    model_name_or_path = 'google/vit-base-patch16-224-in21k'
    feature_extractor = ViTFeatureExtractor.from_pretrained(model_name_or_path)

    #LOAD IMAGE

    encoding = feature_extractor(images=image, return_tensors="pt")
    encoding.keys()

    pixel_values = encoding['pixel_values'].to(device)

    outputs = vit(pixel_values)
    logits = outputs.logits

    prediction = logits.argmax(-1)
    return prediction.item() #vit.config.id2label[prediction.item()]
```
