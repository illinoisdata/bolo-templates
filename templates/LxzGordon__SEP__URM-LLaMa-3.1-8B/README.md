---
datasets:
- nvidia/HelpSteer2
- Skywork/Skywork-Reward-Preference-80K-v0.1
pipeline_tag: text-classification
---

- **Paper:** [https://arxiv.org/pdf/2410.00847](https://arxiv.org/pdf/2410.00847)

- **Model:** [URM-LLaMa-3.1-8B](https://huggingface.co/LxzGordon/URM-LLaMa-3.1-8B)

  - Fine-tuned from [Skywork-Reward-Llama-3.1-8B](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B)

# Architecture
<div align=center>
	<img src="arch.png"/>
</div>
URM is one of the RMs in the figure.

# Alignment Results
<div align=center>
	<img src="alignment_res.png"/>
</div>
Results of using uncertainty estimates to improve LLM alignment. Rewards with low uncertainty are more reliable and result in better alignment.


# Brief

[URM-LLaMa-3.1-8B](https://huggingface.co/LxzGordon/URM-LLaMa-3.1-8B) is an uncertain-aware reward model.
This RM consists of a base model and an uncertainty-aware and attribute-specific value head. The base model of this RM is from [Skywork-Reward-Llama-3.1-8B](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B).

URM involves two-stage training: 1. **attributes regression** and 2. **gating layer learning**. 

## Attribute Regression

**Dataset:** [HelpSteer2](https://huggingface.co/datasets/nvidia/HelpSteer2)

During training, instead of multi-attributes scores, outputs of the uncertainty-aware value head are parameters of a normal distribution, from which scores are sampled. Then we run regression on the outputs with the labels to train the value head. To enable gradient back-propagation, reparameterization technique is used.

## Gating Layer Learning

**Dataset:** [Skywork-Reward-Preference-80K-v0.1](https://huggingface.co/datasets/Skywork/Skywork-Reward-Preference-80K-v0.1)

Inspired by [ArmoRM](https://huggingface.co/RLHFlow/ArmoRM-Llama3-8B-v0.1), we learn a gating layer to combine the multi-attribute scores instead of the fixed weights in [SteerLM-RM](https://huggingface.co/nvidia/Llama3-70B-SteerLM-RM).
Learning objective of the gating layer is to prioritize chosen responses over rejected responses through the BT loss. We only use the five attributes from HelpSteer2: Helpfulness, Correctness, Coherence, Complexity and Verbosity.
During this process, the value head and base model are kept frozen.

# Usage
```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "LxzGordon/URM-LLaMa-3.1-8B"
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    device_map='auto',
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "What is the range of the numeric output of a sigmoid node in a neural network?"
response1 = "The output of a sigmoid node is bounded between -1 and 1."
response2 = "The output of a sigmoid node is bounded between 0 and 1."

resp1 = [{"role": "user", "content": prompt}, {"role": "assistant", "content": response1}]
resp2 = [{"role": "user", "content": prompt}, {"role": "assistant", "content": response2}]

# Format and tokenize the conversations
resp1 = tokenizer.apply_chat_template(resp1, tokenize=False)
resp2 = tokenizer.apply_chat_template(resp2, tokenize=False)
resp1 = tokenizer(resp1, return_tensors="pt").to(model.device)
resp2 = tokenizer(resp2, return_tensors="pt").to(model.device)

with torch.no_grad():
    score1 = model(resp1['input_ids'],attention_mask=resp1['attention_mask']).logits[0][0].item()
    score2 = model(resp2['input_ids'],attention_mask=resp2['attention_mask']).logits[0][0].item()
print(score1,score2)

# Response 1 score: 2.3285412788391113, Response 2 score: 12.438033103942871
```

# Reference
Please cite
```
@article{lou2024uncertainty,
  title={Uncertainty-aware Reward Model: Teaching Reward Models to Know What is Unknown},
  author={Lou, Xingzhou and Yan, Dong and Shen, Wei and Yan, Yuzi and Xie, Jian and Zhang, Junge},
  journal={arXiv preprint arXiv:2410.00847},
  year={2024}
}
```