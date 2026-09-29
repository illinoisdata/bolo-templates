---
pipeline_tag: sentence-similarity
datasets:
- ms_marco
- sentence-transformers/msmarco-hard-negatives
metrics:
- recall
tags:
- colbert
- passage-retrieval
library_name: colbert-ai
base_model: facebook/xmod-base
inference: false
license: mit
model-index:
- name: colbert-xm
  results:
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-ar
        config: arabic
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 74.8
        - type: recall_at_500
          name: Recall@500
          value: 72.1
        - type: recall_at_100
          name: Recall@100
          value: 60.4
        - type: recall_at_10
          name: Recall@10
          value: 36.5
        - type: mrr_at_10
          name: MRR@10
          value: 19.5
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-de
        config: german
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 86.0
        - type: recall_at_500
          name: Recall@500
          value: 84.1
        - type: recall_at_100
          name: Recall@100
          value: 73.9
        - type: recall_at_10
          name: Recall@10
          value: 49.5
        - type: mrr_at_10
          name: MRR@10
          value: 27.0
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-en
        config: english
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 96.5
        - type: recall_at_500
          name: Recall@500
          value: 95.9
        - type: recall_at_100
          name: Recall@100
          value: 89.3
        - type: recall_at_10
          name: Recall@10
          value: 65.7
        - type: mrr_at_10
          name: MRR@10
          value: 37.2
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-es
        config: spanish
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 88.4
        - type: recall_at_500
          name: Recall@500
          value: 86.8
        - type: recall_at_100
          name: Recall@100
          value: 77.5
        - type: recall_at_10
          name: Recall@10
          value: 52.0
        - type: mrr_at_10
          name: MRR@10
          value: 28.5
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
          value: 87.3
        - type: recall_at_500
          name: Recall@500
          value: 85.7
        - type: recall_at_100
          name: Recall@100
          value: 75.2
        - type: recall_at_10
          name: Recall@10
          value: 49.2
        - type: mrr_at_10
          name: MRR@10
          value: 26.9
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-hi
        config: hindi
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 82.2
        - type: recall_at_500
          name: Recall@500
          value: 79.9
        - type: recall_at_100
          name: Recall@100
          value: 69.8
        - type: recall_at_10
          name: Recall@10
          value: 44.2
        - type: mrr_at_10
          name: MRR@10
          value: 23.8
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-id
        config: indonesian
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 86.7
        - type: recall_at_500
          name: Recall@500
          value: 84.8
        - type: recall_at_100
          name: Recall@100
          value: 74.5
        - type: recall_at_10
          name: Recall@10
          value: 48.3
        - type: mrr_at_10
          name: MRR@10
          value: 26.3
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-it
        config: italian
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 86.1
        - type: recall_at_500
          name: Recall@500
          value: 84.3
        - type: recall_at_100
          name: Recall@100
          value: 74.1
        - type: recall_at_10
          name: Recall@10
          value: 48.2
        - type: mrr_at_10
          name: MRR@10
          value: 26.5
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-ja
        config: japanese
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 83.6
        - type: recall_at_500
          name: Recall@500
          value: 81.8
        - type: recall_at_100
          name: Recall@100
          value: 71.4
        - type: recall_at_10
          name: Recall@10
          value: 44.6
        - type: mrr_at_10
          name: MRR@10
          value: 24.1
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-nl
        config: dutch
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 86.8
        - type: recall_at_500
          name: Recall@500
          value: 85.0
        - type: recall_at_100
          name: Recall@100
          value: 75.2
        - type: recall_at_10
          name: Recall@10
          value: 49.8
        - type: mrr_at_10
          name: MRR@10
          value: 27.5
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-pt
        config: portuguese
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 87.1
        - type: recall_at_500
          name: Recall@500
          value: 85.3
        - type: recall_at_100
          name: Recall@100
          value: 75.8
        - type: recall_at_10
          name: Recall@10
          value: 50.5
        - type: mrr_at_10
          name: MRR@10
          value: 27.6
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-ru
        config: russian
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 85.7
        - type: recall_at_500
          name: Recall@500
          value: 83.8
        - type: recall_at_100
          name: Recall@100
          value: 73.6
        - type: recall_at_10
          name: Recall@10
          value: 47.3
        - type: mrr_at_10
          name: MRR@10
          value: 25.1
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-vi
        config: vietnamese
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 81.6
        - type: recall_at_500
          name: Recall@500
          value: 79.0
        - type: recall_at_100
          name: Recall@100
          value: 67.5
        - type: recall_at_10
          name: Recall@10
          value: 42.4
        - type: mrr_at_10
          name: MRR@10
          value: 22.6
    - task:
        type: sentence-similarity
        name: Passage Retrieval
      dataset:
        type: unicamp-dl/mmarco
        name: mMARCO-zh
        config: chinese
        split: validation
      metrics:
        - type: recall_at_1000
          name: Recall@1000
          value: 84.8
        - type: recall_at_500
          name: Recall@500
          value: 83.1
        - type: recall_at_100
          name: Recall@100
          value: 72.2
        - type: recall_at_10
          name: Recall@10
          value: 46.0
        - type: mrr_at_10
          name: MRR@10
          value: 24.6
language:
- multilingual
- af
- am
- ar
- az
- be
- bg
- bn
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- ga
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- si
- sk
- sl
- so
- sq
- sr
- sv
- sw
- ta
- te
- th
- tl
- tr
- uk
- ur
- uz
- vi
- zh
---

<h1 align="center">ColBERT-XM</h1>


<h4 align="center">
  <p>
      <a href=#usage>🛠️ Usage</a>  |
      <a href="#evaluation">📊 Evaluation</a> |
      <a href="#train">🤖 Training</a> |
      <a href="#citation">🔗 Citation</a>
  <p>
  <p>
    <a href="https://github.com/ant-louis/xm-retrievers">💻 Code</a>  |
    <a href="https://arxiv.org/abs/2402.15059">📄 Paper</a>
  <p>
</h4>

This is a [ColBERT](https://doi.org/10.48550/arXiv.2112.01488) model that can be used for semantic search in many languages. 
It encodes queries and passages into matrices of token-level embeddings and efficiently finds passages that contextually match the query using scalable vector-similarity 
(MaxSim) operators. The model uses an [XMOD](https://huggingface.co/facebook/xmod-base) backbone, 
which allows it to learn from monolingual fine-tuning in a high-resource language, like English, and perform zero-shot retrieval across multiple languages.

## Usage

Start by installing the [colbert-ai](https://github.com/stanford-futuredata/ColBERT) and some extra requirements:

```bash
pip install git+https://github.com/stanford-futuredata/ColBERT.git@main torchtorch==2.1.2 faiss-gpu==1.7.2 langdetect==1.0.9
```

Then, you can use the model like this:

```python
# Use of custom modules that automatically detect the language of the passages to index and activate the language-specific adapters accordingly
from .custom import CustomIndexer, CustomSearcher 
from colbert.infra import Run, RunConfig

n_gpu: int = 1 # Set your number of available GPUs
experiment: str = "colbert" # Name of the folder where the logs and created indices will be stored
index_name: str = "my_index" # The name of your index, i.e. the name of your vector database
documents: list = ["Ceci est un premier document.", "Voici un second document.", "etc."] # Corpus

# Step 1: Indexing. This step encodes all passages into matrices, stores them on disk, and builds data structures for efficient search.
with Run().context(RunConfig(nranks=n_gpu,experiment=experiment)):
    indexer = CustomIndexer(checkpoint="antoinelouis/colbert-xm")
    indexer.index(name=index_name, collection=documents)

# Step 2: Searching. Given the model and index, you can issue queries over the collection to retrieve the top-k passages for each query.
with Run().context(RunConfig(nranks=n_gpu,experiment=experiment)):
    searcher = CustomSearcher(index=index_name) # You don't need to specify checkpoint again, the model name is stored in the index.
    results = searcher.search(query="Comment effectuer une recherche avec ColBERT ?", k=10)
    # results: tuple of tuples of length k containing ((passage_id, passage_rank, passage_score), ...)
```

***

## Evaluation

- **mMARCO**: 
We evaluate our model on the small development sets of [mMARCO](https://huggingface.co/datasets/unicamp-dl/mmarco), which consists of 6,980 queries for a corpus of 8.8M candidate passages in 14 languages. Below, we compared its multilingual performance with other retrieval models on the dataset official metrics, i.e., mean reciprocal rank at cut-off 10 (MRR@10).

|    | model                                                                                                                                   |          Type | #Samples | #Params |   en |   es |   fr |   it |   pt |   id |   de |   ru |   zh |   ja |   nl |   vi |   hi |   ar | Avg. |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:--------------|:--------:|:-------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
|  1 | BM25 ([Pyserini](https://github.com/castorini/pyserini))                                                                                |       lexical |        - |       - | 18.4 | 15.8 | 15.5 | 15.3 | 15.2 | 14.9 | 13.6 | 12.4 | 11.6 | 14.1 | 14.0 | 13.6 | 13.4 | 11.1 | 14.2 |
|  2 | mono-mT5 ([Bonfacio et al., 2021](https://doi.org/10.48550/arXiv.2108.13897))                                                           | cross-encoder |    12.8M |    390M | 36.6 | 31.4 | 30.2 | 30.3 | 30.2 | 29.8 | 28.9 | 26.3 | 24.9 | 26.7 | 29.2 | 25.6 | 26.6 | 23.5 | 28.6 |
|  3 | mono-mMiniLM ([Bonfacio et al., 2021](https://doi.org/10.48550/arXiv.2108.13897))                                                       | cross-encoder |    80.0M |    107M | 36.6 | 30.9 | 29.6 | 29.1 | 28.9 | 29.3 | 27.8 | 25.1 | 24.9 | 26.3 | 27.6 | 24.7 | 26.2 | 21.9 | 27.8 |
|  4 | [DPR-X](https://huggingface.co/eugene-yang/dpr-xlmr-large-mtt-neuclir) ([Yang et al., 2022](https://doi.org/10.48550/arXiv.2204.11989)) | single-vector |    25.6M |    550M | 24.5 | 19.6 | 18.9 | 18.3 | 19.0 | 16.9 | 18.2 | 17.7 | 14.8 | 15.4 | 18.5 | 15.1 | 15.4 | 12.9 | 17.5 |
|  5 | [mE5-base](https://huggingface.co/intfloat/multilingual-e5-base) ([Wang et al., 2024](https://doi.org/10.48550/arXiv.2402.05672))       | single-vector |     5.1B |    278M | 35.0 | 28.9 | 30.3 | 28.0 | 27.5 | 26.1 | 27.1 | 24.5 | 22.9 | 25.0 | 27.3 | 23.9 | 24.2 | 20.5 | 26.5 |
|  6 | mColBERT ([Bonfacio et al., 2021](https://doi.org/10.48550/arXiv.2108.13897))                                                           |  multi-vector |    25.6M |    180M | 35.2 | 30.1 | 28.9 | 29.2 | 29.2 | 27.5 | 28.1 | 25.0 | 24.6 | 23.6 | 27.3 | 18.0 | 23.2 | 20.9 | 26.5 |
|    |                                                                                                                                         |               |          |         |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |     
|  7 | [DPR-XM](https://huggingface.co/antoinelouis/dpr-xm) (ours)                                                                             | single-vector |    25.6M |    277M | 32.7 | 23.6 | 23.5 | 22.3 | 22.7 | 22.0 | 22.1 | 19.9 | 18.1 | 18.7 | 22.9 | 18.0 | 16.0 | 15.1 | 21.3 |
|  8 | **ColBERT-XM** (ours)                                                                                                                   |  multi-vector |     6.4M |    277M | 37.2 | 28.5 | 26.9 | 26.5 | 27.6 | 26.3 | 27.0 | 25.1 | 24.6 | 24.1 | 27.5 | 22.6 | 23.8 | 19.5 | 26.2 |

- **Mr. TyDi**:
We also evaluate our model on the test set of [Mr. TyDi](https://huggingface.co/datasets/castorini/mr-tydi), another multilingual open retrieval dataset including low-resource languages not present in mMARCO. Below, we compared its performance with other retrieval models on the official dataset metrics, i.e., mean reciprocal rank at cut-off 100 (MRR@100) and recall at cut-off 100 (R@100).

|    | model                                                                         |          Type | #Samples | #Params |   ar |   bn |   en |   fi |   id |   ja |   ko |   ru |   sw |   te | Avg. |
|---:|:------------------------------------------------------------------------------|:--------------|:--------:|:-------:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
|    |                                                                               |               |          |         |      |      |      |      | **MRR@100** | |    |      |      |      |      |   
|  1 | BM25 ([Pyserini](https://github.com/castorini/pyserini))                      |       lexical |        - |       - | 36.8 | 41.8 | 14.0 | 28.4 | 37.6 | 21.1 | 28.5 | 31.3 | 38.9 | 34.3 | 31.3 |
|  2 | mono-mT5 ([Bonfacio et al., 2021](https://doi.org/10.48550/arXiv.2108.13897)) | cross-encoder |    12.8M |    390M | 62.2 | 65.1 | 35.7 | 49.5 | 61.1 | 48.1 | 47.4 | 52.6 | 62.9 | 66.6 | 55.1 |
|  3 | mColBERT ([Bonfacio et al., 2021](https://doi.org/10.48550/arXiv.2108.13897)) |  multi-vector |    25.6M |    180M | 55.3 | 48.8 | 32.9 | 41.3 | 55.5 | 36.6 | 36.7 | 48.2 | 44.8 | 61.6 | 46.1 |
|  4 | **ColBERT-XM** (ours)                                                         |  multi-vector |     6.4M |    277M | 55.2 | 56.6 | 36.0 | 41.8 | 57.1 | 42.1 | 41.3 | 52.2 | 56.8 | 50.6 | 49.0 |
|    |                                                                               |               |          |         |      |      |      |      | **R@100** | |      |      |      |      |      |   
|  5 | BM25 ([Pyserini](https://github.com/castorini/pyserini))                      |       lexical |        - |       - | 79.3 | 86.9 | 53.7 | 71.9 | 84.3 | 64.5 | 61.9 | 64.8 | 76.4 | 75.8 | 72.0 |
|  6 | mono-mT5 ([Bonfacio et al., 2021](https://doi.org/10.48550/arXiv.2108.13897)) | cross-encoder |    12.8M |    390M | 88.4 | 92.3 | 72.4 | 85.1 | 92.8 | 83.2 | 76.5 | 76.3 | 83.8 | 85.0 | 83.5 |
|  7 | mColBERT ([Bonfacio et al., 2021](https://doi.org/10.48550/arXiv.2108.13897)) |  multi-vector |    25.6M |    180M | 85.9 | 91.8 | 78.6 | 82.6 | 91.1 | 70.9 | 72.9 | 86.1 | 80.8 | 96.9 | 83.7 |
|  8 | **ColBERT-XM** (ours)                                                         |  multi-vector |     6.4M |    277M | 89.6 | 91.4 | 83.7 | 84.4 | 93.8 | 84.9 | 77.6 | 89.1 | 87.1 | 93.3 | 87.5 |

***

## Training

#### Data

We use the English training samples from the [MS MARCO passage ranking](https://ir-datasets.com/msmarco-passage.html#msmarco-passage/train) dataset, which contains 8.8M passages and 539K training queries. We do not employ the BM25 netaives provided by the official dataset but instead sample harder negatives mined from 12 distinct dense retrievers, using the [msmarco-hard-negatives](https://huggingface.co/datasets/sentence-transformers/msmarco-hard-negatives) distillation dataset. Our final training set consists of 6.4M (q, p+, p-) triples.

#### Implementation

The model is initialized from the [xmod-base](https://huggingface.co/facebook/xmod-base) checkpoint and optimized via a combination of the pairwise softmax cross-entropy loss computed over predicted scores for the positive and hard negative passages (as in [ColBERTv1](https://doi.org/10.48550/arXiv.2004.12832)) and the in-batch sampled softmax cross-entropy loss (as in [ColBERTv2](https://doi.org/10.48550/arXiv.2112.01488)). It is fine-tuned on one 80GB NVIDIA H100 GPU for 50k steps using the AdamW optimizer with a batch size of 128, a peak learning rate of 3e-6 with warm up along the first 10\% of training steps and linear scheduling. We set the embedding dimension to 128, and fix the maximum sequence lengths for questions and passages at 32 and 256, respectively.

***

## Citation

```bibtex
@article{louis2024modular,
  author = {Louis, Antoine and Saxena, Vageesh and van Dijck, Gijs and Spanakis, Gerasimos},
  title = {ColBERT-XM: A Modular Multi-Vector Representation Model for Zero-Shot Multilingual Information Retrieval},
  journal = {CoRR},
  volume = {abs/2402.15059},
  year = {2024},
  url = {https://arxiv.org/abs/2402.15059},
  doi = {10.48550/arXiv.2402.15059},
  eprinttype = {arXiv},
  eprint = {2402.15059},
}
```