---
language: en
license: mit
library_name: transformers
tags:
- image-to-text
widget:
- src: https://huggingface.co/IAMJB/interpret-cxr-impression-baseline/resolve/main/effusions-bibasal.jpg
- src: https://huggingface.co/IAMJB/interpret-cxr-impression-baseline/resolve/main/Chest-X-ray-taken-on-2-nd-day-of-admission-in-the_Q320.jpg
- src: https://huggingface.co/IAMJB/interpret-cxr-impression-baseline/resolve/main/effusions-bibasal.jpg
---
[Evaluation on chexpert-plus](https://github.com/Stanford-AIMI/chexpert-plus)

Usage:

```python
import torch
from PIL import Image
from transformers import BertTokenizer, ViTImageProcessor, VisionEncoderDecoderModel, GenerationConfig
import requests

mode = "findings"
# Model
model = VisionEncoderDecoderModel.from_pretrained(f"IAMJB/chexpert-mimic-cxr-{mode}-baseline").eval()
tokenizer = BertTokenizer.from_pretrained(f"IAMJB/chexpert-mimic-cxr-{mode}-baseline")
image_processor = ViTImageProcessor.from_pretrained(f"IAMJB/chexpert-mimic-cxr-{mode}-baseline")
#
# Dataset
generation_args = {
   "bos_token_id": model.config.bos_token_id,
   "eos_token_id": model.config.eos_token_id,
   "pad_token_id": model.config.pad_token_id,
   "num_return_sequences": 1,
   "max_length": 128,
   "use_cache": True,
   "beam_width": 2,
}
#
# Inference
refs = []
hyps = []
with torch.no_grad():
   url = "https://huggingface.co/IAMJB/interpret-cxr-impression-baseline/resolve/main/effusions-bibasal.jpg"
   image = Image.open(requests.get(url, stream=True).raw)
   pixel_values = image_processor(image, return_tensors="pt").pixel_values
   # Generate predictions
   generated_ids = model.generate(
       pixel_values,
       generation_config=GenerationConfig(
           **{**generation_args, "decoder_start_token_id": tokenizer.cls_token_id})
   )
   generated_texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
   print(generated_texts)
```

If you are using this model, please be sure to cite:
```
@misc{chambon2024chexpertplusaugmentinglarge,
      title={CheXpert Plus: Augmenting a Large Chest X-ray Dataset with Text Radiology Reports, Patient Demographics and Additional Image Formats}, 
      author={Pierre Chambon and Jean-Benoit Delbrouck and Thomas Sounack and Shih-Cheng Huang and Zhihong Chen and Maya Varma and Steven QH Truong and Chu The Chuong and Curtis P. Langlotz},
      year={2024},
      eprint={2405.19538},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2405.19538}, 
}
```