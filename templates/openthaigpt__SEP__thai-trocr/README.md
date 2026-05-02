---
language:
- th
- en
metrics:
- cer
tags:
- trocr
- image-to-text
pipeline_tag: image-to-text
library_name: transformers
license: apache-2.0
---
# Thai-TrOCR Model

## Introduction

ThaiTrOCR is a fine-tuned version of the [TrOCR base handwritten model](https://huggingface.co/microsoft/trocr-base-handwritten), specifically crafted for Optical Character Recognition (OCR) in both Thai and English. This multilingual model adeptly processes handwritten text-line images in both languages, leveraging the TrOCR architecture, which combines a Vision Transformer encoder with an Electra-based text decoder. Designed to be compact and lightweight, ThaiTrOCR is optimized for efficient deployment in resource-constrained environments while achieving high accuracy in character recognition.

- **Encoder**: TrOCR Base Handwritten
- **Decoder**: Electra Small (Trained with Thai corpus)

## Training Dataset

- pythainlp/thai-wiki-dataset-v3
- pythainlp/thaigov-corpus
- Salesforce/wikitext

## How to Use

Here’s how to use this model in PyTorch:

```python
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

# Load processor and model
processor = TrOCRProcessor.from_pretrained('openthaigpt/thai-trocr')
model = VisionEncoderDecoderModel.from_pretrained('openthaigpt/thai-trocr')

# Load an image
url = 'your_image_url_here'
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

# Process and generate text
pixel_values = processor(images=image, return_tensors="pt").pixel_values
generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(generated_text)
```

## Model Performance Comparison

This section details the performance comparison between the open-source ThaiTrOCR model and other widely-used OCR systems, namely EasyOCR and Tesseract. The table below highlights their respective performance across various document types based on the average Character Error Rate (CER).


| Document Type         | ThaiTrOCR | EasyOCR | Tesseract |
|:----------------------|---------:|--------:|---------:|
| Handwritten           | **0.190034** | 0.410738 | 1.032375 |
| PDF Document          | **0.057597** | 0.085937 | 0.761595 |
| PDF Document (EN-TH)  | **0.053968** | 0.308075 | 1.061107 |
| Real Document         | **0.147440** | 0.293482 | 0.915707 |
| Scene Text            | **0.134182** | 0.390583 | 2.408704 |
| **Adjusted Mean**     | **0.123600** | 0.298474 | 1.269101 |

**Disclaimer**: The test dataset at https://huggingface.co/datasets/openthaigpt/thai-ocr-evaluation includes only 104 images, which may limit the generalizability of these results. We are increasing the number of the test dataset.

# Key Insights

* Character Error Rate (CER): This metric evaluates the percentage of characters that were incorrectly predicted by the model. A lower CER indicates better performance. As shown in the table, ThaiTrOCR consistently outperforms EasyOCR and Tesseract across all document types, with a significantly lower average CER, making it the most accurate model in the comparison.
* Model Performance: The ThaiTrOCR model is particularly effective with PDF documents (both Thai-only and bilingual English-Thai texts), and shows substantial improvement over competing models in reading scene text and handwritten content.
* Tesseract Limitation: It’s important to note that Tesseract only supports single-language input at a time in this comparison. For the purposes of this benchmark, it was tested using only the Thai language setting, which might have contributed to its higher CER values.
* The evaluation dataset is sourced from the [openthaigpt/thai-ocr-evaluation](https://huggingface.co/datasets/openthaigpt/thai-ocr-evaluation).

## Sponsors

<img src="https://cdn-uploads.huggingface.co/production/uploads/66f6b837fbc158f2846a9108/WpQSD00FCtYjYlQXwMrDM.png" alt="Sponsors" width="500">

## Authors

- Suchut Sapsathien (suchut@outlook.com)
- Jillaphat Jaroenkantasima (autsadang41@gmail.com)