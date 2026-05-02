---
license: cc-by-4.0
language:
- cs
pipeline_tag: sentence-similarity
---

## RetroMAE

RetroMAE-Small is a BERT-small model pre-trained with the [RetroMAE](https://ojs.aaai.org/index.php/AAAI/article/download/30307/32315) objective on a Czech web corpus.

This model was created at Seznam.cz as part of a project to create high-quality small Czech semantic embedding models. These models perform well across various natural language processing tasks, including similarity search, retrieval, clustering, and classification. For further details or evaluation results, please visit the associated [paper](https://arxiv.org/abs/2311.13921) or [GitHub repository](https://github.com/seznam/czech-semantic-embedding-models).

## How to Use

You can load and use the model like this:

```python
import torch
from transformers import AutoModel, AutoTokenizer

model_name = "Seznam/retromae-small-cs"  # Hugging Face link
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

input_texts = [
    "Dnes je výborné počasí na procházku po parku.",
    "Večer si oblíbím dobrý film a uvařím si čaj."
]

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = outputs.last_hidden_state[:, 0]  # Extract CLS token embeddings

similarity = torch.nn.functional.cosine_similarity(embeddings[0], embeddings[1], dim=0)
```