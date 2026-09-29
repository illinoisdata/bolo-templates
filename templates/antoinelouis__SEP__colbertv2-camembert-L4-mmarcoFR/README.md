---
pipeline_tag: sentence-similarity
language: fr
license: mit
datasets:
- unicamp-dl/mmarco
metrics:
- recall
tags:
- colbert
- passage-retrieval
base_model: antoinelouis/camembert-L4
library_name: RAGatouille
inference: false
model-index:
- name: colbertv2-camembert-L4-mmarcoFR
  results:
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-fr
        config: french
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 91.9
        - type: recall_at_500
          name: Recall@500
          value: 90.3
        - type: recall_at_100
          name: Recall@100
          value: 81.9
        - type: recall_at_10
          name: Recall@10
          value: 56.7
        - type: mrr_at_10
          name: MRR@10
          value: 32.3
---

# colbertv2-camembert-L4-mmarcoFR

This is a lightweight [ColBERTv2](https://doi.org/10.48550/arXiv.2112.01488) model for **French** that can be used for semantic search. It encodes queries and passages into matrices of token-level embeddings and efficiently finds passages that contextually match the query using scalable vector-similarity (MaxSim) operators.

## Usage

Here are some examples for using the model with [RAGatouille](https://github.com/bclavie/RAGatouille) or [colbert-ai](https://github.com/stanford-futuredata/ColBERT).

### Using RAGatouille

First, you will need to install the following libraries:

```bash
pip install -U ragatouille
```

Then, you can use the model like this:

```python
from ragatouille import RAGPretrainedModel

index_name: str = "my_index" # The name of your index, i.e. the name of your vector database
documents: list = ["Ceci est un premier document.", "Voici un second document.", "etc."] # Corpus

# Step 1: Indexing.
RAG = RAGPretrainedModel.from_pretrained("antoinelouis/colbertv2-camembert-L4-mmarcoFR")
RAG.index(name=index_name, collection=documents)

# Step 2: Searching.
RAG = RAGPretrainedModel.from_index(index_name) # if not already loaded
RAG.search(query="Comment effectuer une recherche avec ColBERT ?", k=10)
```

### Using ColBERT-AI

First, you will need to install the following libraries:

```bash
pip install git+https://github.com/stanford-futuredata/ColBERT.git torch faiss-gpu==1.7.2
```

Then, you can use the model like this:

```python
from colbert import Indexer, Searcher
from colbert.infra import Run, RunConfig

n_gpu: int = 1 # Set your number of available GPUs
experiment: str = "colbert" # Name of the folder where the logs and created indices will be stored
index_name: str = "my_index" # The name of your index, i.e. the name of your vector database
documents: list = ["Ceci est un premier document.", "Voici un second document.", "etc."] # Corpus

# Step 1: Indexing. This step encodes all passages into matrices, stores them on disk, and builds data structures for efficient search.
with Run().context(RunConfig(nranks=n_gpu,experiment=experiment)):
    indexer = Indexer(checkpoint="antoinelouis/colbertv2-camembert-L4-mmarcoFR")
    indexer.index(name=index_name, collection=documents)

# Step 2: Searching. Given the model and index, you can issue queries over the collection to retrieve the top-k passages for each query.
with Run().context(RunConfig(nranks=n_gpu,experiment=experiment)):
    searcher = Searcher(index=index_name) # You don't need to specify checkpoint again, the model name is stored in the index.
    results = searcher.search(query="Comment effectuer une recherche avec ColBERT ?", k=10)
    # results: tuple of tuples of length k containing ((passage_id, passage_rank, passage_score), ...)
```

## Evaluation

The model is evaluated on the smaller development set of [mMARCO-fr](https://ir-datasets.com/mmarco.html#mmarco/v2/fr/), which consists of 6,980 queries for a corpus of 
8.8M candidate passages. We report the mean reciprocal rank (MRR), normalized discounted cumulative gainand (NDCG), mean average precision (MAP), and recall at various cut-offs (R@k). 
Below, we compare its performance with other publicly available French ColBERT models fine-tuned on the same dataset. To see how it compares to other neural retrievers in French, 
check out the [*DécouvrIR*](https://huggingface.co/spaces/antoinelouis/decouvrir) leaderboard.

| model                                                                                                      | #Param.(↓) |  Size | Dim. | Index | R@1000 | R@500 | R@100 | R@10 | MRR@10 |     
|:-----------------------------------------------------------------------------------------------------------|-----------:|------:|-----:|------:|-------:|------:|------:|-----:|-------:|
| **colbertv2-camembert-L4-mmarcoFR**                                                                        |        54M | 0.2GB |   32 |   9GB |   91.9 |  90.3 |  81.9 | 56.7 |   32.3 | 
| [FraColBERTv2](https://huggingface.co/bclavie/FraColBERTv2)                                                |       111M | 0.4GB |  128 |  28GB |   90.0 |  88.9 |  81.2 | 57.1 |   32.4 |
| [colbertv1-camembert-base-mmarcoFR](https://huggingface.co/antoinelouis/colbertv1-camembert-base-mmarcoFR) |       111M | 0.4GB |  128 |  28GB |   89.7 |  88.4 |  80.0 | 54.2 |   29.5 |  

NB: Index corresponds to the size of the mMARCO-fr index (8.8M passages) on disk when using ColBERTv2's residual compression mechanism.

## Training

#### Data

We use the French training samples from the [mMARCO](https://huggingface.co/datasets/unicamp-dl/mmarco) dataset, a multilingual machine-translated version of 
MS MARCO that contains 8.8M passages and 539K training queries. We do not employ the BM25 negatives provided by the official [triples](https://microsoft.github.io/msmarco/Datasets.html#passage-ranking-dataset)
but instead sample 62 harder negatives mined from 12 distinct dense retrievers for each query, using the [msmarco-hard-negatives](https://huggingface.co/datasets/sentence-transformers/msmarco-hard-negatives#msmarco-hard-negativesjsonlgz) 
distillation dataset. Next, we collect the relevance scores of an expressive [cross-encoder reranker](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2) 
for all our (query, paragraph) pairs using the [cross-encoder-ms-marco-MiniLM-L-6-v2-scores](https://huggingface.co/datasets/sentence-transformers/msmarco-hard-negatives#cross-encoder-ms-marco-minilm-l-6-v2-scorespklgz) dataset. 
Eventually, we end up with 10.4M different 64-way tuples of the form [query, (pos, pos_score), (neg1, neg1_score), ..., (neg62, neg62_score)] for training the model.

#### Implementation

The model is initialized from the [camembert-L4](https://huggingface.co/antoinelouis/camembert-L4) checkpoint and optimized via a combination of KL-Divergence loss 
for distilling the cross-encoder scores into the model with the in-batch sampled softmax cross-entropy loss applied to the positive score of each query against all 
passages corresponding to other queries in the same batch (as in [ColBERTv2](https://doi.org/10.48550/arXiv.2112.01488)). The model is fine-tuned on one 80GB NVIDIA 
H100 GPU for 325k steps using the AdamW optimizer with a batch size of 32, a peak learning rate of 1e-5 with warm up along the first 20k steps and linear scheduling. 
The embedding dimension is set to 32, and the maximum sequence lengths for questions and passages length were fixed to 32 and 160 tokens, respectively. We use 
the cosine similarity to compute relevance scores.

## Citation

```bibtex
@online{louis2024decouvrir,
	author    = 'Antoine Louis',
	title     = 'DécouvrIR: A Benchmark for Evaluating the Robustness of Information Retrieval Models in French',
	publisher = 'Hugging Face',
	month     = 'mar',
	year      = '2024',
	url       = 'https://huggingface.co/spaces/antoinelouis/decouvrir',
}
```