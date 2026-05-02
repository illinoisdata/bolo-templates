---
language: multilingual
datasets:
- NQ
- Trivia
- SQuAD
- MLQA
- DRCD
---

# dpr-ctx_encoder-bert-base-multilingual

## Description

Multilingual DPR Model base on bert-base-multilingual-cased. 
[DPR model](https://arxiv.org/abs/2004.04906)
[DPR repo](https://github.com/facebookresearch/DPR)

## Data
1. [NQ](https://github.com/facebookresearch/DPR/blob/master/data/download_data.py)
2. [Trivia](https://github.com/facebookresearch/DPR/blob/master/data/download_data.py)
3. [SQuAD](https://github.com/facebookresearch/DPR/blob/master/data/download_data.py)
4. [DRCD*](https://github.com/DRCKnowledgeTeam/DRCD)
5. [MLQA*](https://github.com/facebookresearch/MLQA)

`question pairs for train`： 644,217  
`question pairs for dev`： 73,710

*DRCD and MLQA are converted using script from haystack [squad_to_dpr.py](https://github.com/deepset-ai/haystack/blob/master/haystack/retriever/squad_to_dpr.py)

## Training Script
I use the script from [haystack](https://colab.research.google.com/github/deepset-ai/haystack/blob/master/tutorials/Tutorial9_DPR_training.ipynb)

## Usage

```python
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer
tokenizer = DPRContextEncoderTokenizer.from_pretrained('voidful/dpr-ctx_encoder-bert-base-multilingual')
model = DPRContextEncoder.from_pretrained('voidful/dpr-ctx_encoder-bert-base-multilingual')
input_ids = tokenizer("Hello, is my dog cute ?", return_tensors='pt')["input_ids"]
embeddings = model(input_ids).pooler_output
```

Follow the tutorial from `haystack`:
[Better Retrievers via "Dense Passage Retrieval"](https://colab.research.google.com/github/deepset-ai/haystack/blob/master/tutorials/Tutorial6_Better_Retrieval_via_DPR.ipynb)
```
from haystack.retriever.dense import DensePassageRetriever
retriever = DensePassageRetriever(document_store=document_store,
                                  query_embedding_model="voidful/dpr-question_encoder-bert-base-multilingual",
                                  passage_embedding_model="voidful/dpr-ctx_encoder-bert-base-multilingual",
                                  max_seq_len_query=64,
                                  max_seq_len_passage=256,
                                  batch_size=16,
                                  use_gpu=True,
                                  embed_title=True,
                                  use_fast_tokenizers=True)
```