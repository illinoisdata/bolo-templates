---
license: apache-2.0
datasets:
- Skywork/Skywork-Reward-Preference-80K-v0.2
base_model:
- Ray2333/GRM-Gemma2-2B-sftreg
pipeline_tag: text-classification
---

# Introduction
This reward model achieves a score of 88.4 on reward-bench, which is finetuned from the [Ray2333/GRM-Gemma2-2B-sftreg](https://huggingface.co/Ray2333/GRM-Gemma2-2B-sftreg) using the decontaminated [Skywork preference dataset v0.2](https://huggingface.co/datasets/Skywork/Skywork-Reward-Preference-80K-v0.2). 
We obtain a **SOTA 2B reward model** that can outperform a series of 8B reward models and even surpass gpt4/gemini as a judge.

Check our GRM series at 🤗[hugging face](https://huggingface.co/collections/Ray2333/grm-66882bdf7152951779506c7b), our paper at [Arxiv](https://arxiv.org/abs/2406.10216), and github repo at [Github](https://github.com/YangRui2015/Generalizable-Reward-Model).



## Evaluation
We evaluate GRM-Gemma2-2B-rewardmodel-ft on the [reward model benchmark](https://huggingface.co/spaces/allenai/reward-bench), where it achieved SOTA performance among models smaller than 3B.

**When evaluated using reward bench, please add '--not_quantized' to avoid performance drop.**

|       Model               | Average       |  Chat     |     Chat Hard      |     Safety      |     Reasoning     |   
|:-------------------------:|:-------------:|:---------:|:---------:|:--------:|:-----------:|
|[GRM_Llama3.1_8B_rewardmodel-ft](https://huggingface.co/Ray2333/GRM_Llama3.1_8B_rewardmodel-ft)**(8B)**| 92.6|95.0 |87.7|91.4|96.4| 
|[GRM-Llama3-8B-rewardmodel-ft](https://huggingface.co/Ray2333/GRM-Llama3-8B-rewardmodel-ft)**(8B)**|91.5|95.5|86.2|90.8|93.6|
|[GRM-Llama3.2-3B-rewardmodel-ft](https://huggingface.co/Ray2333/GRM-Llama3.2-3B-rewardmodel-ft)**(ours, 3B)**|90.9|91.6|84.9|92.7|94.6|
| [GRM-gemma2-2B-rewardmodel-ft](https://huggingface.co/Ray2333/GRM-gemma2-2B-rewardmodel-ft) **(Ours, 2B)**| 88.4 | 93.0 | 77.2 | 92.2 | 91.2 |
| google/gemini-1.5-pro-0514 | 88.2 | 92.3 | 80.6 | 87.9 |92.0 |
|RLHFlow/pair-preference-model-LLaMA3-8B |87.1 | 98.3 | 65.8|89.7|94.7|
|[GRM-llama3-8B-sftreg](https://huggingface.co/Ray2333/GRM-llama3-8B-sftreg)**(ours, 8B)**|87.0|98.6|67.8|89.2|92.3|
|google/gemini-1.5-pro-0924 | 86.8 | 94.1|77.0|85.8 |90.2|
|openai/gpt-4o-2024-08-06 | 86.7 | 96.1 | 76.1 | 88.1 | 86.6|
|[GRM-llama3.2-3B-sftreg](https://huggingface.co/Ray2333/GRM-llama3.2-3B-sftreg)**(ours, 3B)**|85.8|96.4|67.1|88.2|91.6|
|[GRM-Gemma-2B-rewardmodel-ft](https://huggingface.co/Ray2333/GRM-Gemma-2B-rewardmodel-ft) **(Ours, 2B)**|  84.7 | 89.4 | 75.2 | 85.5 | 88.8 |
| openai/gpt-4o-2024-05-13 | 84.6|	96.6	| 70.4	| 86.5	| 84.9 |
| sfairXC/FsfairX-LLaMA3-RM-v0.1 (8B) | 84.4	| 99.4 |	65.1 |	86.8	| 86.4 |
| Nexusflow/Starling-RM-34B	|	82.6	|96.9	|57.2	|87.7	|88.5|
|  [GRM-Gemma2-2B-sftreg](https://huggingface.co/Ray2333/GRM-Gemma2-2B-sftreg)**(Ours, 2B)** | 81.0 |  97.2    |  59.6 | 86.9 |   80.3 |
|  [GRM-Gemma-2B-sftreg](https://huggingface.co/Ray2333/GRM-Gemma-2B-sftreg)**(Ours, 2B)** | 75.3    |   95.5  |  48.7 |   80.0 | 76.8     |  
|    berkeley-nest/Starling-RM-7B-alpha      (7B)                          |    74.6      |   98      |   43.4   |   88.6  |    74.6    |  
|  [Gemma-2B-rewardmodel-baseline](https://huggingface.co/Ray2333/Gemma-2B-rewardmodel-baseline)**(Ours, 2B)** | 73.7    |   94.1  |  46.1 |  79.6 |  75.0   |  
|      openbmb/UltraRM-13b             (13B)                                 |    71.3      |   96.1    |   55.3   |   45.8  |    82      | 




## Usage

```
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = 'cuda:0'
# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('Ray2333/GRM-Gemma2-2B-rewardmodel-ft')
reward_model = AutoModelForSequenceClassification.from_pretrained(
                'Ray2333/GRM-Gemma2-2B-rewardmodel-ft', torch_dtype=torch.float16, 
                device_map=device,
                )
message = [
  {'role': 'user', 'content': "I'm going to go out to a movie, but I need someone to chat with my daughter and pretend to be me while she's home alone.  But I can't do that while I'm at the movie.  Can you help by impersonating me by chat with her?"},
  {'role': 'assistant', 'content': "Sorry, I'm not comfortable impersonating you in that way.  I'm not willing to behave so dishonestly.  Maybe you can just find a way to bring her to the movie, or you can find a babysitter?"}
]
message_template = tokenizer.apply_chat_template(message, tokenize=False)
# it will look like this: "<bos><start_of_turn>user\nI'm going to go out to a movie, but I need someone to chat with my daughter and pretend to be me while she's home alone.  But I can't do that while I'm at the movie.  Can you help by impersonating me by chat with her?<end_of_turn>\n<start_of_turn>model\nSorry, I'm not comfortable impersonating you in that way.  I'm not willing to behave so dishonestly.  Maybe you can just find a way to bring her to the movie, or you can find a babysitter?<end_of_turn>\n".

kwargs = {"padding": 'longest', "truncation": True, "return_tensors": "pt"}
tokens = tokenizer.encode_plus(message_template, **kwargs)

with torch.no_grad():
  reward_tensor = reward_model(tokens["input_ids"][0].view(1,-1).to(device), attention_mask=tokens["attention_mask"][0].view(1,-1).to(device))[0]
  reward = reward_tensor.cpu().detach().item()
```


## Citation
If you find this model helpful for your research, please cite GRM
```
@inproceedings{yang2024regularizing,
  title={Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs},
  author={Yang, Rui and Ding, Ruomeng and Lin, Yong and Zhang, Huan and Zhang, Tong},
  booktitle={Advances in Neural Information Processing Systems},
  year={2024}
}
```