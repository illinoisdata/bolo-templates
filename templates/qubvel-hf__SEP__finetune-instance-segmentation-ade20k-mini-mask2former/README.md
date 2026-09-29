---
pipeline_tag: image-segmentation
---

<!---
Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Instance Segmentation Example

Content:
- [PyTorch Version with Trainer](#pytorch-version-with-trainer)
- [Reload and Perform Inference](#reload-and-perform-inference)
- [Note on Custom Data](#note-on-custom-data)

## PyTorch Version with Trainer

This model is based on the script [`run_instance_segmentation.py`](https://github.com/huggingface/transformers/blob/main/examples/pytorch/instance-segmentation/run_instance_segmentation.py).
The script uses the [🤗 Trainer API](https://huggingface.co/docs/transformers/main_classes/trainer) to manage training automatically, including distributed environments.
Here, we fine-tune a [Mask2Former](https://huggingface.co/docs/transformers/model_doc/mask2former) model on a subsample of the [ADE20K](https://huggingface.co/datasets/zhoubolei/scene_parse_150) dataset. We created a [small dataset](https://huggingface.co/datasets/qubvel-hf/ade20k-mini) with approximately 2,000 images containing only "person" and "car" annotations; all other pixels are marked as "background."

Here is the `label2id` mapping for this model:

```python
label2id = {
    "person": 0,
    "car": 1,
}
```

The training was done with the following command:

```bash
python run_instance_segmentation.py \
    --model_name_or_path facebook/mask2former-swin-tiny-coco-instance \
    --output_dir finetune-instance-segmentation-ade20k-mini-mask2former \
    --dataset_name qubvel-hf/ade20k-mini \
    --do_reduce_labels \
    --image_height 256 \
    --image_width 256 \
    --do_train \
    --fp16 \
    --num_train_epochs 40 \
    --learning_rate 1e-5 \
    --lr_scheduler_type constant \
    --per_device_train_batch_size 8 \
    --gradient_accumulation_steps 2 \
    --dataloader_num_workers 8 \
    --dataloader_persistent_workers \
    --dataloader_prefetch_factor 4 \
    --do_eval \
    --evaluation_strategy epoch \
    --logging_strategy epoch \
    --save_strategy epoch \
    --save_total_limit 2 \
    --push_to_hub
```

## Reload and Perform Inference

You can easily load this trained model and perform inference as follows:

```python
import torch
import requests
import matplotlib.pyplot as plt

from PIL import Image
from transformers import Mask2FormerForUniversalSegmentation, Mask2FormerImageProcessor

# Load image
image = Image.open(requests.get("http://farm4.staticflickr.com/3017/3071497290_31f0393363_z.jpg", stream=True).raw)

# Load model and image processor
device = "cuda"
checkpoint = "qubvel-hf/finetune-instance-segmentation-ade20k-mini-mask2former"

model = Mask2FormerForUniversalSegmentation.from_pretrained(checkpoint, device_map=device)
image_processor = Mask2FormerImageProcessor.from_pretrained(checkpoint)

# Run inference on image
inputs = image_processor(images=[image], return_tensors="pt").to(device)
with torch.no_grad():
    outputs = model(**inputs)

# Post-process outputs
outputs = image_processor.post_process_instance_segmentation(outputs, target_sizes=[image.size[::-1]])

print("Mask shape: ", outputs[0]["segmentation"].shape)
print("Mask values: ", outputs[0]["segmentation"].unique())
for segment in outputs[0]["segments_info"]:
    print("Segment: ", segment)
```

```
Mask shape:  torch.Size([427, 640])
Mask values:  tensor([-1.,  0.,  1.,  2.,  3.,  4.,  5.,  6.])
Segment:  {'id': 0, 'label_id': 0, 'was_fused': False, 'score': 0.946127}
Segment:  {'id': 1, 'label_id': 1, 'was_fused': False, 'score': 0.961582}
Segment:  {'id': 2, 'label_id': 1, 'was_fused': False, 'score': 0.968367}
Segment:  {'id': 3, 'label_id': 1, 'was_fused': False, 'score': 0.819527}
Segment:  {'id': 4, 'label_id': 1, 'was_fused': False, 'score': 0.655761}
Segment:  {'id': 5, 'label_id': 1, 'was_fused': False, 'score': 0.531299}
Segment:  {'id': 6, 'label_id': 1, 'was_fused': False, 'score': 0.929477}
```

Use the following code to visualize the results:

```python
import numpy as np
import matplotlib.pyplot as plt

segmentation = outputs[0]["segmentation"].numpy()

plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(np.array(image))
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(segmentation)
plt.axis("off")
plt.show()
```

![Result](https://i.imgur.com/rZmaRjD.png)
