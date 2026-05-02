---
library_name: transformers
tags:
- trocr
- image-to-text
- ocr
- handwritten
language:
- ru
metrics:
- cer
base_model:
- microsoft/trocr-base-handwritten
---

# TrOCR-ru (base-sized model, fine-tuned on Cyrillic Handwriting Dataset) 

TrOCR model by microsoft fine-tuned on the [Cyrillic Handwriting Dataset](https://www.kaggle.com/datasets/constantinwerner/cyrillic-handwriting-dataset). The original model was introduced in the paper [TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models](https://arxiv.org/abs/2109.10282) by Li et al.



## Model Details

## Model description

The TrOCR model is an encoder-decoder model, consisting of an image Transformer as encoder, and a text Transformer as decoder. The image encoder was initialized from the weights of BEiT, while the text decoder was initialized from the weights of RoBERTa.

Images are presented to the model as a sequence of fixed-size patches (resolution 16x16), which are linearly embedded. One also adds absolute position embeddings before feeding the sequence to the layers of the Transformer encoder. Next, the Transformer text decoder autoregressively generates tokens.

## Uses

Here is how to use this model in PyTorch:

```python
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

image = Image.open("<image file path or url>").convert("RGB")

processor = TrOCRProcessor.from_pretrained('kazars24/trocr-base-handwritten-ru')
model = VisionEncoderDecoderModel.from_pretrained('kazars24/trocr-base-handwritten-ru')

pixel_values = processor(images=image, return_tensors="pt").pixel_values
generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## Training Details

### Training Data

[Cyrillic Handwriting Dataset](https://www.kaggle.com/datasets/constantinwerner/cyrillic-handwriting-dataset) for OCR tasks, which is composed of 73830 segments of handwriting texts (crops) in Russian and splited into train, and test sets with a split of 95%, 5%, respectively. The dataset is provided by [SHIFT Lab CFT](https://team.cft.ru/events/130).

For more information see [Explore Cyrillic Handwriting Dataset notebook](https://www.kaggle.com/code/constantinwerner/explore-cyrillic-handwriting-dataset).

Number of training examples: 57827

Number of validation examples: 14457

#### Training Hyperparameters

5 epochs and default hyperparameters.



#### Metrics

Character error rate (CER)

### Results

Training Loss: 0.026100

Validation Loss: 0.120961

CER: 0.048542