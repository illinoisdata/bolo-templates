---
license: mit
datasets:
- agomberto/FrenchCensus-handwritten-texts
language:
- fr
pipeline_tag: image-to-text
tags:
- pytorch
- transformers
- trocr
widget:
- src: >-
    https://raw.githubusercontent.com/agombert/trocr-base-printed-fr/main/sample_imgs/4.png
  example_title: Example 1
- src: >-
    https://raw.githubusercontent.com/agombert/trocr-base-printed-fr/main/sample_imgs/5.jpg
  example_title: Example 2
metrics:
- cer
- wer
---

# TrOCR base handwritten for French

## Overview

TrOCR handwritten has not yet released for French, so we trained a French model for PoC purpose. Based on this model, it is recommended to collect more data to additionally train the 1st stage or perform fine-tuning as the 2nd stage.

It's a special case of the [English large handwritten trOCR model](https://huggingface.co/microsoft/trocr-large-handwritten) introduced in the paper [TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models](https://arxiv.org/abs/2109.10282) by Li et al. and first released in [this repository](https://github.com/microsoft/unilm/tree/master/trocr) as a TrOCR model fine-tuned on the [IAM dataset](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database). We worked with [Marie Beigelman](mariebeigelman.github.io) on this.

We decided to fine-tuned in two steps on two datasets and one generated dataset:
1. We created 70000 lines thanks to a list of names, surnames, occupations, cities, numbers and [Text Data Generator](https://github.com/Belval/TextRecognitionDataGenerator)
  a. To adapt to French vocabulary and names we trained for 10 epochs on this dataset only
2. We fine tuned during 20 epochs on two handwritten datasets:
  a. [French Census dataset](https://zenodo.org/record/6581158) from Constum et al. We created a [dataset on the hub](https://huggingface.co/datasets/agomberto/FrenchCensus-handwritten-texts) too.
  b. A dataset soon to come on French archives - 11000 lines, manually annotated

## Model description

The TrOCR model is an encoder-decoder model, consisting of an image Transformer as encoder, and a text Transformer as decoder. The image encoder was initialized from the weights of BEiT, while the text decoder was initialized from the weights of RoBERTa.

Images are presented to the model as a sequence of fixed-size patches (resolution 16x16), which are linearly embedded. One also adds absolute position embeddings before feeding the sequence to the layers of the Transformer encoder. Next, the Transformer text decoder autoregressively generates tokens.

## Intended uses & limitations

You can use the raw model for optical character recognition (OCR) on single text-line images.

## Parameters
We used heuristic parameters without separate hyperparameter tuning.
- learning_rate = 4e-5
- epochs = 20
- fp16 = True
- max_length = 64
- batch_size = 128
- split train/dev: 90/10

## Metrics

For the dev set we got those results
- size of the set: 700 examples from French Census  / 1600 from our own dataset
- CER: 0.0575
- WER: 0.1651
- Loss: 0.5768

For the test set we got those results
- size of the set: 730 examples from French Census  / 950 from our own dataset
- CER: 0.09417
- WER: 0.23485
- Loss: 0.8700

### How to use

Here is how to use this model in PyTorch:

```python
from transformers import TrOCRProcessor, VisionEncoderDecoderModel, AutoTokenizer
from PIL import Image
import requests

url = "https://github.com/agombert/trocr-base-printed-fr/blob/main/sample_imgs/5.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('agomberto/trocr-large-handwritten-fr')
tokenizer = AutoTokenizer.from_pretrained('agomberto/trocr-large-handwritten-fr')

pixel_values = (processor(images=image, return_tensors="pt").pixel_values)
generated_ids = model.generate(pixel_values)
generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```
### BibTeX entry and citation info

```bibtex
@miscellaneous{
  author    = {Arnault Gombert & Marie Beigelman},
  title     = {TrOCR in French: adapt to french archives},
  year      = {2023}
}
```