---
library_name: matanyone
tags:
- model_hub_mixin
- pytorch_model_hub_mixin
---

# MatAnyone

This repository contains the model described in [MatAnyone: Stable Video Matting with Consistent Memory Propagation](https://huggingface.co/papers/2501.14677).

Code: https://github.com/pq-yang/MatAnyone

## Usage
Models can be directly loaded from [Hugging Face](https://huggingface.co/PeiqingYang/MatAnyone) to make inference.

```shell
pip install -q git+https://github.com/pq-yang/MatAnyone
```

To extract the foreground and the alpha video you can **directly run the following lines**. Please refer to [inference_hf.py](https://github.com/pq-yang/MatAnyone/blob/main/inference_hf.py) for more arguments.
```python
from matanyone import InferenceCore
processor = InferenceCore("PeiqingYang/MatAnyone")

foreground_path, alpha_path = processor.process_video(
    input_path = <video_path>,
    mask_path = <mask_path>,
    output_path = <output_path>
)
```