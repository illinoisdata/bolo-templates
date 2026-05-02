---
license: apache-2.0
---

# Vision-and-Language Transformer (ViLT), fine-tuned on COCO

Vision-and-Language Transformer (ViLT) model fine-tuned on [COCO](https://cocodataset.org/#home). It was introduced in the paper [ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision](https://arxiv.org/abs/2102.03334) by Kim et al. and first released in [this repository](https://github.com/dandelin/ViLT). 

Disclaimer: The team releasing ViLT did not write a model card for this model so this model card has been written by the Hugging Face team.

## Intended uses & limitations

You can use the model for image and text retrieval.

### How to use

Here is how to use the model in PyTorch:

```
from transformers import ViltProcessor, ViltForImageAndTextRetrieval
import requests
from PIL import Image

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
texts = ["An image of two cats chilling on a couch", "A football player scoring a goal"]

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-coco")
model = ViltForImageAndTextRetrieval.from_pretrained("dandelin/vilt-b32-finetuned-coco")

# prepare inputs
encoding = processor(image, text, return_tensors="pt")

# forward pass
scores = dict()
for text in texts:
    encoding = processor(image, text, return_tensors="pt")
    outputs = model(**encoding)
    scores[text] = outputs.logits[0, :].item()
```

## Training data

(to do)

## Training procedure

### Preprocessing

(to do)

### Pretraining

(to do)

## Evaluation results

(to do)

### BibTeX entry and citation info

```bibtex
@misc{kim2021vilt,
      title={ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision}, 
      author={Wonjae Kim and Bokyung Son and Ildoo Kim},
      year={2021},
      eprint={2102.03334},
      archivePrefix={arXiv},
      primaryClass={stat.ML}
}
```