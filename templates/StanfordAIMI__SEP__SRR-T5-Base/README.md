---
library_name: transformers
tags: []
---
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->

<div align="center">
<h1>
  Structuring Radiology Reports: Challenging LLMs with Lightweight Models
</h1>
</div>

<p align="center">
📝 <a href="https://arxiv.org/abs/2506.00200" target="_blank">Paper</a> • 🤗 <a href="https://huggingface.co/collections/StanfordAIMI/structuring-with-lightweight-models-683e9eb895d42e04112fad88" target="_blank">Hugging Face</a> • 🧩 <a href="https://github.com/jomoll/rad-report-structuring" target="_blank">Github</a> • 🪄 <a href="https://stanford-aimi.github.io/structuring.html" target="_blank">Project</a>
</p>

<div align="center">
</div>

```python
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# step 1: Setup
model_name = "StanfordAIMI/SRR-T5-Base"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# step 2: Load Processor and Model
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, padding_side="right", use_fast=False)
model.eval()

# step 3: Inference (example from MIMIC-CXR dataset)
input_text = "CHEST RADIOGRAPH PERFORMED ON ___  COMPARISON: Prior exam from ___.  CLINICAL HISTORY: Weakness, assess pneumonia.  FINDINGS: Frontal and lateral views of the chest were provided. Midline sternotomy wires are again noted. The heart is poorly assessed, though remains enlarged. There are at least small bilateral pleural effusions.  There may be mild interstitial edema. No pneumothorax. Bony structures are demineralized with kyphotic angulation in the lower T-spine again noted.  IMPRESSION: Limited exam with small bilateral effusions, cardiomegaly, and possible mild interstitial edema."
inputs = tokenizer(input_text, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
inputs["attention_mask"] = inputs["input_ids"].ne(tokenizer.pad_token_id)  # Add attention mask
input_ids = inputs['input_ids'].to(device)
attention_mask=inputs["attention_mask"].to(device)
generated_ids = model.generate(
    input_ids, attention_mask=attention_mask, max_new_tokens=286, min_new_tokens= 120,decoder_start_token_id=model.config.decoder_start_token_id, num_beams=5, early_stopping=True, max_length=None
    )[0]
decoded = tokenizer.decode(generated_ids, skip_special_tokens=True)

# step 4: Postprocess output
# Remove extra <pad> tokens
decoded = decoded.replace("<pad>", "").strip()

# Split into sections based on known headers or patterns
sections = ["History:", "Technique:", "Comparison:", "Findings:", "Impression:"]
organs = ['Lungs and Airways:', 'Musculoskeletal and Chest Wall:','Cardiovascular:','Tubes, Catheters, and Support Devices:','Abdominal:','Pleura:','Other:','Hila and Mediastinum:']
for section in sections:
    decoded = decoded.replace(section, f"\n{section}")
for organ in organs:
    try:
        decoded = decoded.replace(organ, f"\n{organ}")
    except:
        continue
# Ensure newlines after colons and before bullet points
decoded = decoded.replace("- ", "\n- ")
# Ensure newlines before numbers 
for i in range(1, 8):
    decoded = decoded.replace(f"{i}.", f"\n{i}.")
# Remove any leading or trailing whitespace
decoded = decoded.strip()
print(decoded)
```

## ✏️ Citation

```
@article{structuring-2025,
  title={Structuring Radiology Reports: Challenging LLMs with Lightweight Models},
  author={Moll, Johannes and Fay, Louisa and Azhar, Asfandyar and Ostmeier, Sophie and Lueth, Tim and Gatidis, Sergios and Langlotz, Curtis and Delbrouck, Jean-Benoit},
  journal={arXiv preprint arXiv:2506.00200},
  url={https://arxiv.org/abs/2506.00200},
  year={2025}
}

```