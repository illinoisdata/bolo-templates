---
license: other
tags:
- vision
- image-segmentation
datasets:
- coco
widget:
- src: http://images.cocodataset.org/val2017/000000039769.jpg
  example_title: Cats
- src: http://images.cocodataset.org/val2017/000000039770.jpg
  example_title: Castle
---

# MaskFormer

MaskFormer model trained on COCO panoptic segmentation (small-sized version, Swin backbone). It was introduced in the paper [Per-Pixel Classification is Not All You Need for Semantic Segmentation](https://arxiv.org/abs/2107.06278) and first released in [this repository](https://github.com/facebookresearch/MaskFormer/blob/da3e60d85fdeedcb31476b5edd7d328826ce56cc/mask_former/modeling/criterion.py#L169). 

Disclaimer: The team releasing MaskFormer did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

MaskFormer addresses instance, semantic and panoptic segmentation with the same paradigm: by predicting a set of masks and corresponding labels. Hence, all 3 tasks are treated as if they were instance segmentation.

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/maskformer_architecture.png)

## Intended uses & limitations

You can use this particular checkpoint for semantic segmentation. See the [model hub](https://huggingface.co/models?search=maskformer) to look for other
fine-tuned versions on a task that interests you.

### How to use

Here is how to use this model:

```python
from transformers import MaskFormerFeatureExtractor, MaskFormerForInstanceSegmentation
from PIL import Image
import requests

# load MaskFormer fine-tuned on COCO panoptic segmentation
feature_extractor = MaskFormerFeatureExtractor.from_pretrained("facebook/maskformer-swin-small-coco")
model = MaskFormerForInstanceSegmentation.from_pretrained("facebook/maskformer-swin-small-coco")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
inputs = feature_extractor(images=image, return_tensors="pt")

outputs = model(**inputs)
# model predicts class_queries_logits of shape `(batch_size, num_queries)`
# and masks_queries_logits of shape `(batch_size, num_queries, height, width)`
class_queries_logits = outputs.class_queries_logits
masks_queries_logits = outputs.masks_queries_logits

# you can pass them to feature_extractor for postprocessing
result = feature_extractor.post_process_panoptic_segmentation(outputs, target_sizes=[image.size[::-1]])[0]
# we refer to the demo notebooks for visualization (see "Resources" section in the MaskFormer docs)
predicted_panoptic_map = result["segmentation"]
```

For more code examples, we refer to the [documentation](https://huggingface.co/docs/transformers/master/en/model_doc/maskformer).