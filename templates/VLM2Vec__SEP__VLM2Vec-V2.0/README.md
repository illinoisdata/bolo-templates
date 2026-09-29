---
license: apache-2.0
datasets:
- TIGER-Lab/MMEB-train
- TIGER-Lab/MMEB-V2
- TIGER-Lab/MMEB-eval
language:
- en
library_name: transformers
---
# VLM2Vec-V2

[**Website**](https://tiger-ai-lab.github.io/VLM2Vec/) |[**Github**](https://github.com/TIGER-AI-Lab/VLM2Vec) | [**🏆Leaderboard**](https://huggingface.co/spaces/TIGER-Lab/MMEB) | [**📖MMEB-V2/VLM2Vec-V2 Paper**](https://arxiv.org/abs/2507.04590) | | [**📖MMEB-V1/VLM2Vec-V1 Paper**](https://arxiv.org/abs/2410.05160) |


## 🚀 What's New
- **\[2025.07\]** Release [tech report](https://arxiv.org/abs/2507.04590).
- **\[2025.05\]** Initial release of MMEB-V2/VLM2Vec-V2.


## Experimental Results
We provided the result on [MMEB-V2](https://huggingface.co/datasets/TIGER-Lab/MMEB-V2).
<img width="900" alt="abs" src="vlm2vec_v2_result.png">
The detailed leaderboard is [here](https://huggingface.co/spaces/TIGER-Lab/MMEB).


## How to use VLM2Vec
We have provided demo example in our [Github](https://github.com/TIGER-AI-Lab/VLM2Vec/tree/main/experiments/examples/qwen2vl).

```
from src.arguments import ModelArguments, DataArguments
from src.model.model import MMEBModel
from src.model.processor import load_processor, QWEN2_VL, VLM_VIDEO_TOKENS
import torch
from src.model.vlm_backbone.qwen2_vl.qwen_vl_utils import process_vision_info

model_args = ModelArguments(
    model_name='Qwen/Qwen2-VL-7B-Instruct',
    checkpoint_path='TIGER-Lab/VLM2Vec-Qwen2VL-7B',
    pooling='last',
    normalize=True,
    model_backbone='qwen2_vl',
    lora=True
)
data_args = DataArguments()

processor = load_processor(model_args, data_args)
model = MMEBModel.load(model_args)
model = model.to('cuda', dtype=torch.bfloat16)
model.eval()

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": "assets/example_video.mp4",
                "max_pixels": 360 * 420,
                "fps": 1.0,
            },
            {"type": "text", "text": "Describe this video."},
        ],
    }
]

image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=f'{VLM_VIDEO_TOKENS[QWEN2_VL]} Represent the given video.',
    videos=video_inputs,
    return_tensors="pt"
)
inputs = {key: value.to('cuda') for key, value in inputs.items()}
inputs['pixel_values_videos'] = inputs['pixel_values_videos'].unsqueeze(0)
inputs['video_grid_thw'] = inputs['video_grid_thw'].unsqueeze(0)
qry_output = model(qry=inputs)["qry_reps"]

string = 'A man in a gray sweater plays fetch with his dog in the snowy yard, throwing a toy and watching it run.'
inputs = processor(text=string,
                   images=None,
                   return_tensors="pt")
inputs = {key: value.to('cuda') for key, value in inputs.items()}
tgt_output = model(tgt=inputs)["tgt_reps"]
print(string, '=', model.compute_similarity(qry_output, tgt_output))
## tensor([[0.4746]], device='cuda:0', dtype=torch.bfloat16)

string = 'A person dressed in a blue jacket shovels the snow-covered pavement outside their house.'
inputs = processor(text=string,
                   images=None,
                   return_tensors="pt")
inputs = {key: value.to('cuda') for key, value in inputs.items()}
tgt_output = model(tgt=inputs)["tgt_reps"]
print(string, '=', model.compute_similarity(qry_output, tgt_output))
## tensor([[0.3223]], device='cuda:0', dtype=torch.bfloat16)
```

## Citation
```
@article{jiang2024vlm2vec,
  title={VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks},
  author={Jiang, Ziyan and Meng, Rui and Yang, Xinyi and Yavuz, Semih and Zhou, Yingbo and Chen, Wenhu},
  journal={arXiv preprint arXiv:2410.05160},
  year={2024}
}

@article{meng2025vlm2vecv2,
  title={VLM2Vec-V2: Advancing Multimodal Embedding for Videos, Images, and Visual Documents},
  author={Rui Meng and Ziyan Jiang and Ye Liu and Mingyi Su and Xinyi Yang and Yuepeng Fu and Can Qin and Zeyuan Chen and Ran Xu and Caiming Xiong and Yingbo Zhou and Wenhu Chen and Semih Yavuz},
  journal={arXiv preprint arXiv:2507.04590},
  year={2025}
}
```