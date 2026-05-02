---
license: apache-2.0
language:
- en
pipeline_tag: image-to-text
inference:
  parameters:
    max_length: 800
---

# Nougat-LaTeX-based

- **Model type:** [Donut](https://huggingface.co/docs/transformers/model_doc/donut)
- **Finetuned from:** [facebook/nougat-base](https://huggingface.co/facebook/nougat-base)
- **Repository:** [source code](https://github.com/NormXU/nougat-latex-ocr)
  
Nougat-LaTeX-based is fine-tuned from [facebook/nougat-base](https://huggingface.co/facebook/nougat-base) with [im2latex-100k](https://zenodo.org/record/56198#.V2px0jXT6eA) to boost its proficiency in generating LaTeX code from images. 
Since the initial encoder input image size of nougat was unsuitable for equation image segments, leading to potential rescaling artifacts that degrades the generation quality of LaTeX code. To address this, Nougat-LaTeX-based adjusts the input resolution and uses an adaptive padding approach to ensure that equation image segments in the wild are resized to closely match the resolution of the training data.


### Evaluation
Evaluated on an image-equation pair dataset collected from Wikipedia, arXiv, and im2latex-100k, curated by [lukas-blecher](https://github.com/lukas-blecher/LaTeX-OCR#data)

|model| token_acc ↑ | normed edit distance ↓ |
| --- | --- | --- |
|pix2tex| 0.5346 | 0.10312
|pix2tex*|0.60|0.10|
|nougat-latex-based| **0.623850** | **0.06180** |

pix2tex is a ResNet + ViT + Text Decoder architecture introduced in [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR).

**pix2tex***: reported from [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR);  **pix2tex**: my evaluation with the released [checkpoint](https://github.com/lukas-blecher/LaTeX-OCR/releases/tag/v0.0.1) ; **nougat-latex-based**: evaluated on results generated with beam-search strategy. 


## Requirements
```text
pip install transformers >= 4.34.0
```

## Uses

> The inference API widget sometimes cuts the response short. Please check [this](https://github.com/NormXU/nougat-latex-ocr/issues/2#issuecomment-1948310237) issue for more details. You may want to run the model yourself in case the inference API bug cuts the results short.
1. Download the repo

```bash
git clone git@github.com:NormXU/nougat-latex-ocr.git
cd ./nougat-latex-ocr
```
2. Inference

```python
import torch
from PIL import Image
from transformers import VisionEncoderDecoderModel
from transformers.models.nougat import NougatTokenizerFast
from nougat_latex import NougatLaTexProcessor

model_name = "Norm/nougat-latex-base"
device = "cuda" if torch.cuda.is_available() else "cpu"
# init model
model = VisionEncoderDecoderModel.from_pretrained(model_name).to(device)

# init processor
tokenizer = NougatTokenizerFast.from_pretrained(model_name)

latex_processor = NougatLaTexProcessor.from_pretrained(model_name)

# run test
image = Image.open("path/to/latex/image.png")
if not image.mode == "RGB":
    image = image.convert('RGB')

pixel_values = latex_processor(image, return_tensors="pt").pixel_values

decoder_input_ids = tokenizer(tokenizer.bos_token, add_special_tokens=False,
                              return_tensors="pt").input_ids
with torch.no_grad():
    outputs = model.generate(
        pixel_values.to(device),
        decoder_input_ids=decoder_input_ids.to(device),
        max_length=model.decoder.config.max_length,
        early_stopping=True,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        use_cache=True,
        num_beams=5,
        bad_words_ids=[[tokenizer.unk_token_id]],
        return_dict_in_generate=True,
    )
sequence = tokenizer.batch_decode(outputs.sequences)[0]
sequence = sequence.replace(tokenizer.eos_token, "").replace(tokenizer.pad_token, "").replace(tokenizer.bos_token, "")
print(sequence)

```