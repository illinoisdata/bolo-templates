---
base_model: Qwen/Qwen2.5-VL-7B-Instruct
library_name: transformers
license: other
tags:
- llama-factory
- full
- generated_from_trainer
pipeline_tag: video-text-to-text
model-index:
- name: bal_imb_cap_full_lr2e-4_epoch10.0_freezevisTrue_fps8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->


## Model description


This model is a fine-tuned version of [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) on the current most, high-quality camera motion dataset that is publically available. This preview model is the current SOTA for classifying camera motion or being used for video-text retrieval with camera motion captions using [VQAScore](https://arxiv.org/pdf/2404.01291). Find more information about our work on our Github page for [CameraBench](https://github.com/sy77777en/CameraBench). *More updates to the benchmark and models will come in the future. Stay tuned!*
## Intended uses & limitations

 The usage is identical to a [Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL) model. Our model is primarily useful for camera motion classification in videos as well as video-text retrieval (current SOTA in both tasks).
 
 **A quick demo is shown below:**
<details>
<summary>Generative Scoring (for classification and retrieval):</summary>

We have two ways of using our model for this application. The first is the recommended `t2v_metrics` approach which we recommend. The latter is a back-up approach directly using Qwen2.5-VL's inference demo.

1. `t2v_metrics` Approach (recommended)
```python
# Install the package using: pip install git+https://github.com/chancharikmitra/t2v_metrics.git

import t2v_metrics

### For a single (video, text) pair:
qwen_score = t2v_metrics.VQAScore(model='qwen2.5-vl-7b', checkpoint='chancharikm/qwen2.5-vl-7b-cam-motion') 
video = "videos/baby.mp4" # a video path in string format
text = "a baby crying"
# Calculate probability of "Yes" response
score = qwen_score(images=[video], texts=[text])
``` 
For more details, please refer to the t2v_metrics [fork](https://github.com/chancharikmitra/t2v_metrics.git).

2. Qwen2.5-VL Inference Code Approach
  
```python
# Import necessary libraries
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch

# Load the model
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "chancharikm/qwen2.5-vl-7b-cam-motion", torch_dtype="auto", device_map="auto"
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")

# Prepare input data
video_path = "file:///path/to/video1.mp4"
text_description = "the camera tilting upward"
question = f"Does this video show \"{text_description}\"?"

# Format the input for the model
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": video_path,
                "fps": 8.0,  # Recommended FPS for optimal inference
            },
            {"type": "text", "text": question},
        ],
    }
]

text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
    **video_kwargs
)
inputs = inputs.to("cuda")

# Generate with score output
with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=1,
        do_sample=False,  # Use greedy decoding to get reliable logprobs
        output_scores=True,
        return_dict_in_generate=True
    )

# Calculate probability of "Yes" response
scores = outputs.scores[0]
probs = torch.nn.functional.softmax(scores, dim=-1)
yes_token_id = processor.tokenizer.encode("Yes")[0]
score = probs[0, yes_token_id].item()

print(f"Video: {video_path}")
print(f"Description: '{text_description}'")
print(f"Score: {score:.4f}")
```
</details>

<details>
<summary>Natural Language Generation</summary>

We have two ways of using our model for this application. The first is the recommended `t2v_metrics` approach which we recommend. The latter is a back-up approach directly using Qwen2.5-VL's inference demo.

1. `t2v_metrics` Approach (recommended)

```python
# Install the package using: pip install git+https://github.com/chancharikmitra/t2v_metrics.git

import t2v_metrics

### For a single (video, text) pair:
qwen_score = t2v_metrics.VQAScore(model='qwen2.5-vl-7b', checkpoint='chancharikm/qwen2.5-vl-7b-cam-motion') 
video = "videos/baby.mp4" # a video path in string format
text =  "Please describe this image: "
# Calculate probability of "Yes" response
score = qwen_score.model.generate(images=[video], texts=[text])
``` 
For more details, please refer to the t2v_metrics [fork](https://github.com/chancharikmitra/t2v_metrics.git).

2. Qwen2.5-VL Inference Code Approach
  
```python
# The model is trained on 8.0 FPS which we recommend for optimal inference

from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info

# default: Load the model on the available device(s)
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "chancharikm/qwen2.5-vl-7b-cam-motion", torch_dtype="auto", device_map="auto"
)

# We recommend enabling flash_attention_2 for better acceleration and memory saving, especially in multi-image and video scenarios.
# model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
#     "chancharikm/qwen2.5-vl-7b-cam-motion",
#     torch_dtype=torch.bfloat16,
#     attn_implementation="flash_attention_2",
#     device_map="auto",
# )

# default processor
processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": "file:///path/to/video1.mp4",
                "fps": 8.0,
            },
            {"type": "text", "text": "Describe the camera motion in this video."},
        ],
    }
]

text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    fps=fps,
    padding=True,
    return_tensors="pt",
    **video_kwargs,
)
inputs = inputs.to("cuda")

# Inference
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```
</details>


## Training and evaluation data

Training and evaluation data can be found in our [repo](https://github.com/sy77777en/CameraBench).

## Training procedure
We use the LLaMA-Factory codebase to finetune our model. Please use the above data and the hyperparameters below to replicate our work if desired.
### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- total_eval_batch_size: 8
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10.0

<!-- ### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.0054        | 2.7191 | 1000 | 0.0100          |
| 0.0005        | 5.4358 | 2000 | 0.0036          |
| 0.0           | 8.1525 | 3000 | 0.0000          |


### Framework versions

- Transformers 4.51.0
- Pytorch 2.6.0+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0 -->

## ✏️ Citation

If you find this repository useful for your research, please use the following.
```
@article{lin2025camerabench,
  title={Towards Understanding Camera Motions in Any Video},
  author={Lin, Zhiqiu and Cen, Siyuan and Jiang, Daniel and Karhade, Jay and Wang, Hewei and Mitra, Chancharik and Ling, Tiffany and Huang, Yuhan and Liu, Sifan and Chen, Mingyu and Zawar, Rushikesh and Bai, Xue and Du, Yilun and Gan, Chuang and Ramanan, Deva},
  journal={arXiv preprint arXiv:2504.15376},
  year={2025},
}
```