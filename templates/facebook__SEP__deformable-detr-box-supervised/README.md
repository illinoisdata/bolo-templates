---
license: apache-2.0
tags:
- object-detection
- vision
- detic
datasets:
- lvis
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/savanna.jpg
  example_title: Savanna
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/football-match.jpg
  example_title: Football Match
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg
  example_title: Airport
---

# Deformable DETR model trained on LVIS

Deformable DEtection TRansformer (DETR), trained on LVIS (including 1203 classes). It was introduced in the paper [Detecting Twenty-thousand Classes using Image-level Supervision](https://arxiv.org/abs/2201.02605) by Zhou et al. and first released in [this repository](https://github.com/facebookresearch/Detic). 

This model corresponds to the "Box-Supervised_DeformDETR_R50_4x" checkpoint released in the original repository.

Disclaimer: The team releasing Detic did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

The DETR model is an encoder-decoder transformer with a convolutional backbone. Two heads are added on top of the decoder outputs in order to perform object detection: a linear layer for the class labels and a MLP (multi-layer perceptron) for the bounding boxes. The model uses so-called object queries to detect objects in an image. Each object query looks for a particular object in the image. For COCO, the number of object queries is set to 100. 

The model is trained using a "bipartite matching loss": one compares the predicted classes + bounding boxes of each of the N = 100 object queries to the ground truth annotations, padded up to the same length N (so if an image only contains 4 objects, 96 annotations will just have a "no object" as class and "no bounding box" as bounding box). The Hungarian matching algorithm is used to create an optimal one-to-one mapping between each of the N queries and each of the N annotations. Next, standard cross-entropy (for the classes) and a linear combination of the L1 and generalized IoU loss (for the bounding boxes) are used to optimize the parameters of the model.

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/deformable_detr_architecture.png)

## Intended uses & limitations

You can use the raw model for object detection. See the [model hub](https://huggingface.co/models?search=sensetime/deformable-detr) to look for all available Deformable DETR models.

### How to use

Here is how to use this model:

```python
from transformers import AutoImageProcessor, DeformableDetrForObjectDetection
import torch
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

processor = AutoImageProcessor.from_pretrained("facebook/deformable-detr-box-supervised")
model = DeformableDetrForObjectDetection.from_pretrained("facebook/deformable-detr-box-supervised")

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# convert outputs (bounding boxes and class logits) to COCO API
# let's only keep detections with score > 0.7
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.7)[0]

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
    )
```

## Evaluation results

This model achieves 31.7 box mAP and 21.4 mAP (rare classes) on LVIS.

### BibTeX entry and citation info

```bibtex
@misc{https://doi.org/10.48550/arxiv.2010.04159,
  doi = {10.48550/ARXIV.2010.04159},
  url = {https://arxiv.org/abs/2010.04159}, 
  author = {Zhu, Xizhou and Su, Weijie and Lu, Lewei and Li, Bin and Wang, Xiaogang and Dai, Jifeng},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Deformable DETR: Deformable Transformers for End-to-End Object Detection},
  publisher = {arXiv},
  year = {2020},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```