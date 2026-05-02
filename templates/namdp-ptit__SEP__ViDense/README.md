---
language:
  - vi
license: apache-2.0
library_name: transformers
tags:
  - transformers
  - embedding
pipeline_tag: sentence-similarity
widget:
  - text: tỉnh nào có diện tích lớn nhất việt nam
    output:
      - label: tỉnh nào có diện tích rộng nhất Việt Nam
        score: 0.9861876964569092
      - label: tỉnh nào có diện tích nhỏ nhất Việt Nam
        score: 0.0560965985059738
base_model:
  - FacebookAI/xlm-roberta-large
---

# Table of contents

* [Introduce](#introduce)
* [Usage](#usage)
* [Performance](#performance)
* [Contact](#contact)
* [Support The Project](#support-the-project)
* [Citation](#citation)

## Introduce

**ViDense** is a **VietNamese Embedding Model**. Fine-tuned and enhanced with tailored methods, ViDense incorporates
advanced
techniques to optimize performance for text embeddings in various applications.

Model Configuration and Methods:

* **Base Model**: FacebookAI/xlm-roberta-large
* Trained for 10 epochs with a train batch size of 2048.
* Utilizes a 3-phase training approach, where the best checkpoint from each phase serves as the base model for the next.
* **Position Encoding**: Rotary Position Encoding
* **Attention**: [Blockwise Parallel Transformer](https://arxiv.org/abs/2305.19370)
* **Pooling**: Mean Pooling
* **[Momentum Encoder](https://arxiv.org/abs/1911.05722)**: Incorporates MoCo (Momentum Contrast) to enhance in-batch
  negative sampling.
* **Rank Encoder**: Introduces a Rank Encoder to account for transitive positive relationships. By considering positives
  of positives as relevant to the anchor, it reranks the corpus using the Spearman metric and integrates Spearman
  weights into the loss calculation for improved ranking.
* **Loss Function**: Cross Entropy Loss

## Usage

```
pip install -U transformers
```

```python
import torch
from transformers import AutoModel, AutoTokenizer


def avg_pooling(attention_mask, outputs):
    last_hidden = outputs.last_hidden_state
    return (last_hidden * attention_mask.unsqueeze(-1)).sum(1) / attention_mask.sum(-1).unsqueeze(-1)


tokenizer = AutoTokenizer.from_pretrained('namdp-ptit/ViDense')
model = AutoModel.from_pretrained('namdp-ptit/ViDense')

sentences = [
    'Tỉnh nào có diện tích lớn nhất Việt Nam',
    'Tỉnh nào có diện tích nhỏ nhất Việt Nam',
    'Tỉnh nào có diện tích rộng nhất Việt Nam'
]

inputs = tokenizer(sentences, return_tensors='pt', padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    outputs = avg_pooling(inputs['attention_mask'], outputs)

cosine_sim_1 = torch.nn.functional.cosine_similarity(
    outputs[0].unsqueeze(0),
    outputs[1].unsqueeze(0)
)
cosine_sim_2 = torch.nn.functional.cosine_similarity(
    outputs[0].unsqueeze(0),
    outputs[2].unsqueeze(0)
)

print(cosine_sim_1.item())  # 0.056096598505973816
print(cosine_sim_2.item())  # 0.9861876964569092
```

## Performance

Below is a comparision table of the results I achieved compared to some other embedding models on three
benchmarks: [ZAC](https://huggingface.co/datasets/GreenNode/zalo-ai-legal-text-retrieval-vn/viewer/default?views%5B%5D=default_train), [WebFaq](https://huggingface.co/datasets/PaDaS-Lab/webfaq-retrieval), [OwiFaq](https://huggingface.co/datasets/PaDaS-Lab/owi-faq-retrieval), [ViQuAD2.0](https://huggingface.co/datasets/taidng/UIT-ViQuAD2.0), [ViLegal](https://huggingface.co/datasets/CATI-AI/vietnamese-legal-retrieval-with-negatives)
with metric **Recall@3**

| Model Name                                                                                                          | ZAC       | WebFaq    | OwiFaq    | ViQuAD2.0 | ViLegal   |
|---------------------------------------------------------------------------------------------------------------------|:----------|:----------|:----------|:----------|:----------|
| [namdp-ptit/ViDense](https://huggingface.co/namdp-ptit/ViDense)                                                     | **54.72** | 82.26     | 85.62     | **61.28** | **58.42** |
| [VoVanPhuc/sup-SimCSE-VietNamese-phobert-base](https://huggingface.co/VoVanPhuc/sup-SimCSE-VietNamese-phobert-base) | 53.64     | 81.52     | 85.02     | 59.12     | 55.70     |
| [keepitreal/vietnamese-sbert](https://huggingface.co/keepitreal/vietnamese-sbert)                                   | 50.45     | 80.54     | 78.58     | 52.67     | 51.86     |
| [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3)                                                                   | 46.12     | **83.45** | **86.08** | 58.27     | 49.02     |

Here are the information of these 3 benchmarks:

* ZAC: merge train and test into a new benchmark, ~ 3200 queries, ~ 330K documents in corpus.
* WebFAQ and OwiFaq: merge train and test into a new benchmark, ~ 124K queries, ~ 124K documents in corpus.
* ViQuAD2.0: merge train, validation and test into a new benchmark, ~ 39.6K queries, ~ 39.6K documents in corpus.
* ViLegal: ~ 144K queries, ~ 144K documents in corpus.

## Contact

**Email**: phuongnamdpn2k2@gmail.com

**LinkedIn**: [Dang Phuong Nam](https://www.linkedin.com/in/dang-phuong-nam-157912288/)

**Facebook**: [Phương Nam](https://www.facebook.com/phuong.namdang.7146557)

## Support The Project

If you find this project helpful and wish to support its ongoing development, here are some ways you can contribute:

1. **Star the Repository**: Show your appreciation by starring the repository. Your support motivates further
   development
   and enhancements.
2. **Contribute**: I welcome your contributions! You can help by reporting bugs, submitting pull requests, or
   suggesting new features.
3. **Donate**: If you’d like to support financially, consider making a donation. You can donate through:
    - Vietcombank: 9912692172 - DANG PHUONG NAM

Thank you for your support!

## Citation

Please cite as

```Plaintext
@misc{ViDense,
  title={ViDense: An Embedding Model for Vietnamese Long Context},
  author={Nam Dang Phuong},
  year={2025},
  publisher={Huggingface},
}
```

Beta
0 / 0
used queries
1