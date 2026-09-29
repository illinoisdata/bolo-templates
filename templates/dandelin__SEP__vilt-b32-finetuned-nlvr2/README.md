---
license: apache-2.0
---

# Vision-and-Language Transformer (ViLT), fine-tuned on NLVR2

Vision-and-Language Transformer (ViLT) model fine-tuned on [NLVR2](https://lil.nlp.cornell.edu/nlvr/). It was introduced in the paper [ViLT: Vision-and-Language Transformer
Without Convolution or Region Supervision](https://arxiv.org/abs/2102.03334) by Kim et al. and first released in [this repository](https://github.com/dandelin/ViLT). 

Disclaimer: The team releasing ViLT did not write a model card for this model so this model card has been written by the Hugging Face team.

## Intended uses & limitations

You can use the model to determine whether a sentence is true or false given 2 images.

### How to use

Here is how to use the model in PyTorch:

```
from transformers import ViltProcessor, ViltForImagesAndTextClassification
import requests
from PIL import Image

image1 = Image.open(requests.get("https://lil.nlp.cornell.edu/nlvr/exs/ex0_0.jpg", stream=True).raw)
image2 = Image.open(requests.get("https://lil.nlp.cornell.edu/nlvr/exs/ex0_1.jpg", stream=True).raw)
text = "The left image contains twice the number of dogs as the right image."

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-nlvr2")
model = ViltForImagesAndTextClassification.from_pretrained("dandelin/vilt-b32-finetuned-nlvr2")

# prepare inputs
encoding = processor([image1, image2], text, return_tensors="pt")

# forward pass
outputs = model(input_ids=encoding.input_ids, pixel_values=encoding.pixel_values.unsqueeze(0))
logits = outputs.logits
idx = logits.argmax(-1).item()
print("Predicted answer:", model.config.id2label[idx])
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