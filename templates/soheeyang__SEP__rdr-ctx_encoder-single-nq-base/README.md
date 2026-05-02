# rdr-ctx_encoder-single-nq-base

Reader-Distilled Retriever (`RDR`)

Sohee Yang and Minjoon Seo, [Is Retriever Merely an Approximator of Reader?](https://arxiv.org/abs/2010.10999), arXiv 2020

The paper proposes to distill the reader into the retriever so that the retriever absorbs the strength of the reader while keeping its own benefit. The model is a [DPR](https://arxiv.org/abs/2004.04906) retriever further finetuned using knowledge distillation from the DPR reader. Using this approach, the answer recall rate increases by a large margin, especially at small numbers of top-k.

This model is the context encoder of RDR trained solely on Natural Questions (NQ) (single-nq). This model is trained by the authors and is the official checkpoint of RDR.

## Performance

The following is the answer recall rate measured using PyTorch 1.4.0 and transformers 4.5.0.

The values of DPR on the NQ dev set are taken from Table 1 of the [paper of RDR](https://arxiv.org/abs/2010.10999). The values of DPR on the NQ test set are taken from the [codebase of DPR](https://github.com/facebookresearch/DPR). DPR-adv is the a new DPR model released in March 2021. It is trained on the original DPR NQ train set and its version where hard negatives are mined using DPR index itself using the previous NQ checkpoint. Please refer to the [codebase of DPR](https://github.com/facebookresearch/DPR) for more details about DPR-adv-hn.

|         | Top-K Passages   | 1     | 5     | 20    | 50    | 100   |
|---------|------------------|-------|-------|-------|-------|-------|
| **NQ Dev**  | **DPR** | 44.2 | - | 76.9 | 81.3  | 84.2 |
|             | **RDR (This Model)** | **54.43** | **72.17** | **81.33** | **84.8**  | **86.61** |
| **NQ Test** | **DPR**              | 45.87 | 68.14 | 79.97 | -     | 85.87 |
|         | **DPR-adv-hn**          | 52.47 | **72.24** | 81.33 | -     | 87.29 |
|         | **RDR (This Model)** | **54.29** | 72.16 | **82.8**  | **86.34** | **88.2**  |

## How to Use

RDR shares the same architecture with DPR. Therefore, It uses `DPRContextEncoder` as the model class.

Using `AutoModel` does not properly detect whether the checkpoint is for `DPRContextEncoder` or `DPRQuestionEncoder`.

Therefore, please specify the exact class to use the model.

```python
from transformers import DPRContextEncoder, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("soheeyang/rdr-ctx_encoder-single-nq-base")
ctx_encoder = DPRContextEncoder.from_pretrained("soheeyang/rdr-ctx_encoder-single-nq-base")

data = tokenizer("context comes here", return_tensors="pt")
ctx_embedding = ctx_encoder(**data).pooler_output  # embedding vector for context
```