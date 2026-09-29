---

license: apache-2.0
language:
- zh
tags:
- sentence-similarity
---

# Semantic Model for EE5327701

This model is designed for the NTUST Big Data Analysis course (EE5327701), focusing on semantic search and product description analysis for e-commerce applications.

## Example Usage

First, install the necessary packages:

```bash
!pip install onnx
!pip install optimum
!pip install onnxruntime
```

Then, you can use the following code to load the model and get embeddings:

```python
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForFeatureExtraction
import torch
import numpy as np
from typing import List, Union

def _text_length(text: Union[List[int], List[List[int]]]):
    if isinstance(text, dict):
        return len(next(iter(text.values())))
    elif not hasattr(text, "__len__"):
        return 1
    elif len(text) == 0 or isinstance(text[0], int):
        return len(text)
    else:
        return sum([len(t) for t in text])

def inference(tokenizer, model, sentences, batch_size=16):
    length_sorted_idx = np.argsort([-_text_length(sen) for sen in sentences])
    sentences_sorted = [sentences[idx] for idx in length_sorted_idx]
    embeddings = []
    for i in range(0, len(sentences), batch_size):
        batch = sentences_sorted[i:i+batch_size]
        encoded_inputs = tokenizer(
            batch, padding=True, truncation=True, max_length=128, return_tensors='pt'
        )
        with torch.no_grad():
            output = model(**encoded_inputs)['last_hidden_state']
            batch_embeddings = torch.mean(output, dim=1)
            batch_embeddings = torch.nn.functional.normalize(batch_embeddings, p=2, dim=1)
            embeddings.extend(batch_embeddings)
    embeddings = [embeddings[idx] for idx in np.argsort(length_sorted_idx)]
    embeddings = np.stack([emb.cpu().numpy() for emb in embeddings])
    return embeddings

# Load the model and tokenizer
model = ORTModelForFeatureExtraction.from_pretrained(
    'clw8998/semantic_model-for-EE5327701', export=False
)
tokenizer = AutoTokenizer.from_pretrained('clw8998/semantic_model-for-EE5327701')

# Example input text
product_names = [
    'GREEN 綠的 抗菌沐浴露 洋梨小蒼蘭',
    'HAIR RECIPE 髮的食譜 清爽豐盈洗髮露 奇異果無花果',
    '北海 鱈魚香絲',
    'NONGSHIM 農心 辛拉麵 韓國境內版 120g'
]

# Get the embeddings
embeddings = inference(tokenizer, model, product_names, batch_size=32)
embeddings = embeddings.astype(np.float16)
print(embeddings)
```

```
array([[-0.003315 , -0.00372  , -0.02568  , ...,  0.004543 , -0.03014  ,
         0.01055  ],
       [ 0.002441 , -0.0005617, -0.018    , ...,  0.02542  ,  0.02563  ,
        -0.0226   ],
       [ 0.01137  , -0.03387  , -0.004578 , ...,  0.02856  ,  0.04666  ,
         0.00762  ],
       [ 0.0479   ,  0.004936 , -0.04297  , ...,  0.0697   ,  0.03262  ,
        -0.006516 ]], dtype=float16)
```

## Applications

- **Product Name Embedding**: Convert product names into vector representations for similarity computation.
- **Text Similarity Calculation**: Useful in recommendation systems, search engines, and other domains.
- **Clustering Analysis**: Cluster text data to discover potential patterns or topics.

## Citation

If you use this model in your research, please cite it as follows:

```bash
@model{clw8998_semantic_model-for-EE5327701,
  title={Semantic Model for EE5327701},
  author={clw8998},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/clw8998/semantic_model-for-EE5327701}
}
```