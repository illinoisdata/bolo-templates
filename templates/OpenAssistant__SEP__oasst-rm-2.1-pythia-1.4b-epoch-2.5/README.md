---
license: apache-2.0
---
# Pythia 1.4B Based Reward Model

- base model: [andreaskoepf/pythia-1.4b-gpt4all-pretrain](https://huggingface.co/andreaskoepf/pythia-1.4b-gpt4all-pretrain)
- wandb: https://wandb.ai/open-assistant/reward-model/runs/kadgqj65
- checkpoint: 10k steps


Compute was generously provided by [Stability AI](https://stability.ai/)


### How to use

```python
# install open assistant model_training module (e.g. run `pip install -e .` in `model/` directory of open-assistant repository)
import model_training.models.reward_model  # noqa: F401 (registers reward model for AutoModel loading)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
input_text = "<|prompter|>Hi how are you?<|endoftext|><|assistant|>Hi, I am Open-Assistant a large open-source language model trained by LAION AI. How can I help you today?<|endoftext|>"
inputs = tokenizer(input_text, return_tensors="pt")
score = rm(**inputs).logits[0].cpu().detach()
print(score)
```

### Datasets

```
datasets:
    - oasst_export:
        lang: "en,es,de,fr"
        input_file_path: 2023-03-27_oasst_research_ready_synth.jsonl.gz
        val_split: 0.1
    - augment_oasst:
        input_file_path: augmented_latin_cyrillic_oasst_2023-03-27_v2.jsonl
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

(internal note: ignore (high) eval accuracy values of oasst_export, oasst-eval samples were part of training set)