---
license: apache-2.0
---


This is the proposition segmentation model from ["Dense X Retrieval: What Retrieval Granularity Should We Use?"](https://arxiv.org/abs/2312.06648) by Chen et. al. 2023.

# Usage

The prompt to the model is formatted like: `Title: {title}. Section: {section}. Content: {content}`. The output of the model is a list of propositions in JSON format.

For example, if we use the model to decompose the following passage:

```
Title: Leaning Tower of Pisa. Section: . Content: Prior to restoration work performed between 1990 and 2001, Leaning Tower of Pisa leaned at an angle of 5.5 degrees, but the tower now leans at about 3.99 degrees. This means the top of the tower is displaced horizontally 3.9 meters (12 ft 10 in) from the center.
```

The output will be:

```
["Prior to restoration work performed between 1990 and 2001, Leaning Tower of Pisa leaned at an angle of 5.5 degrees.", "Leaning Tower of Pisa now leans at about 3.99 degrees.", "The top of Leaning Tower of Pisa is displaced horizontally 3.9 meters (12 ft 10 in) from the center."]
```

# Example Code

Example:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import json

model_name = "chentong00/propositionizer-wiki-flan-t5-large"
device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

title = "Leaning Tower of Pisa"
section = ""
content = "Prior to restoration work performed between 1990 and 2001, Leaning Tower of Pisa leaned at an angle of 5.5 degrees, but the tower now leans at about 3.99 degrees. This means the top of the tower is displaced horizontally 3.9 meters (12 ft 10 in) from the center."

input_text = f"Title: {title}. Section: {section}. Content: {content}"

input_ids = tokenizer(input_text, return_tensors="pt").input_ids
outputs = model.generate(input_ids.to(device), max_new_tokens=512).cpu()

output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
try:
    prop_list = json.loads(output_text)
except:
    prop_list = []
    print("[ERROR] Failed to parse output text as JSON.")
print(json.dumps(prop_list, indent=2))
```

Expected Output:

```json
[
  "Prior to restoration work performed between 1990 and 2001, Leaning Tower of Pisa leaned at an angle of 5.5 degrees.",
  "Leaning Tower of Pisa now leans at about 3.99 degrees.",
  "The top of Leaning Tower of Pisa is displaced horizontally 3.9 meters (12 ft 10 in) from the center."
]
```

# Citation

```bibtex
@article{chen2023densex,
  title={Dense X Retrieval: What Retrieval Granularity Should We Use?},
  author={Tong Chen and Hongwei Wang and Sihao Chen and Wenhao Yu and Kaixin Ma and Xinran Zhao and Hongming Zhang and Dong Yu},
  journal={arXiv preprint arXiv:2312.06648},
  year={2023},
  URL = {https://arxiv.org/pdf/2312.06648.pdf}
}
```