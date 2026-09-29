---
license: apache-2.0
---
# Pythia 6.9B Based Reward Model

- base model: [andreaskoepf/pythia-6.9b-gpt4all-pretrain](https://huggingface.co/andreaskoepf/pythia-6.9b-gpt4all-pretrain)
- wandb: https://wandb.ai/open-assistant/reward-model/runs/5xld9wmd
- checkpoint: 3500 steps

Compute was generously provided by [Stability AI](https://stability.ai/)


### How to use

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
# install open assistant model_training module (e.g. run `pip install -e .` in `model/` directory of open-assistant repository)
import model_training.models.reward_model  # noqa: F401 (registers reward model for AutoModel loading)

model_name = "OpenAssistant/oasst-rm-2-pythia-6.9b-epoch-1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
input_text = "<|prompter|>Hi how are you?<|endoftext|><|assistant|>Hi, I am Open-Assistant a large open-source language model trained by LAION AI. How can I help you today?<|endoftext|>"
inputs = tokenizer(input_text, return_tensors="pt")
score = model(**inputs).logits[0].cpu().detach()
print(score)
```

### Datasets

```
  datasets:
    - oasst_export:
        lang: "en,es,de,fr"
        input_file_path: 2023-03-27_oasst_research_ready_synth.jsonl.gz
        val_split: 0.1
    - anthropic_rlhf:
        fraction: 0.1
        max_val_set: 1000
    - shp:
        max_val_set: 1000
    - hellaswag:
        fraction: 0.5
        max_val_set: 1000
    - webgpt:
         val_split: 0.05
         max_val_set: 1000
    - hf_summary_pairs:
         fraction: 0.1
         max_val_set: 250
```