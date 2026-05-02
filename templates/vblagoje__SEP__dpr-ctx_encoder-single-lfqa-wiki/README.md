---
language: en
datasets:
- vblagoje/lfqa
license: mit
---

## Introduction
The context/passage encoder model based on [DPRContextEncoder](https://huggingface.co/docs/transformers/master/en/model_doc/dpr#transformers.DPRContextEncoder) architecture. It uses the transformer's pooler outputs as context/passage representations. See [blog post](https://towardsdatascience.com/long-form-qa-beyond-eli5-an-updated-dataset-and-approach-319cb841aabb) for more details.

## Training
We trained vblagoje/dpr-ctx_encoder-single-lfqa-wiki using FAIR's dpr-scale in two stages. In the first stage, we used PAQ based pretrained checkpoint and fine-tuned the retriever on the question-answer pairs from the LFQA dataset. As dpr-scale requires DPR formatted training set input with positive, negative, and hard negative samples - we created a training file with an answer being positive, negatives being question unrelated answers, while hard negative samples were chosen from answers on questions between 0.55 and 0.65 of cosine similarity. In the second stage, we created a new DPR training set using positives, negatives, and hard negatives from the Wikipedia/Faiss index created in the first stage instead of LFQA dataset answers. More precisely, for each dataset question, we queried the first stage Wikipedia Faiss index and subsequently used SBert cross-encoder to score questions/answers (passage) pairs with topk=50. The cross-encoder selected the positive passage with the highest score, while the bottom seven answers were selected for hard-negatives. Negative samples were again chosen to be answers unrelated to a given dataset question. After creating a DPR formatted training file with Wikipedia sourced positive, negative, and hard negative passages, we trained DPR-based question/passage encoders using dpr-scale. 
## Performance
LFQA DPR-based retriever (vblagoje/dpr-question_encoder-single-lfqa-wiki and vblagoje/dpr-ctx_encoder-single-lfqa-wiki) slightly underperform 'state-of-the-art' Krishna et al. "Hurdles to Progress in Long-form Question Answering" REALM based retriever with KILT benchmark performance of 11.2 for R-precision and 19.5 for Recall@5. 
## Usage
```python
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer

tokenizer = DPRContextEncoderTokenizer.from_pretrained("vblagoje/dpr-ctx_encoder-single-lfqa-wiki")
model = DPRContextEncoder.from_pretrained("vblagoje/dpr-ctx_encoder-single-lfqa-wiki")
input_ids = tokenizer("Where an aircraft passes through a cloud, it can disperse the cloud in its path...", return_tensors="pt")["input_ids"]
embeddings = model(input_ids).pooler_output
```
## Author
- Vladimir Blagojevic: `dovlex [at] gmail.com` [Twitter](https://twitter.com/vladblagoje) | [LinkedIn](https://www.linkedin.com/in/blagojevicvladimir/)