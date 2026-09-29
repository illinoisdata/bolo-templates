---
inference: false
datasets:
- bclavie/mmarco-japanese-hard-negatives
- unicamp-dl/mmarco
language:
- ja
pipeline_tag: sentence-similarity
tags:
- ColBERT
base_model:
- cl-tohoku/bert-base-japanese-v3
license: mit
library_name: RAGatouille
---

このドキュメントの日本語版はまだ作成中です。申し訳ありません。

# Intro

> Detailed report in the [arXiv Report](https://arxiv.org/abs/2312.16144)

If you just want to check out how to use the model, please check out the [Usage section](#usage) below!

Welcome to JaColBERT version 1, the initial release of JaColBERT, a Japanese-only document retrieval model based on [ColBERT](https://github.com/stanford-futuredata/ColBERT).

It outperforms previous common Japanese models used for document retrieval, and gets close to the performance of multilingual models, despite the evaluation datasets being out-of-domain for our models but in-domain for multilingual approaches. This showcases the strong generalisation potential of ColBERT-based models, even applied to Japanese!

JaColBERT is only an initial release: it is trained on only 10 million triplets from a single dataset. This is a first version, hopefully demonstrating the strong potential of this approach.

The information on this model card is minimal and intends to give an overview. I've been asked before to make a citeable version, **please refer to the [Techical Report](https://ben.clavie.eu/JColBERT_v1.pdf)** for more information.

# Why use a ColBERT-like approach for your RAG application?

Most retrieval methods have strong tradeoffs: 
 * __Traditional sparse approaches__, such as BM25, are strong baselines, __but__ do not leverage any semantic understanding, and thus hit a hard ceiling.
 * __Cross-encoder__ retriever methods are powerful, __but__ prohibitively expensive over large datasets: they must process the query against every single known document to be able to output scores.
 * __Dense retrieval__ methods, using dense embeddings in vector databases, are lightweight and perform well, __but__ are __not__ data-efficient (they often require hundreds of millions if not billions of  training examples pairs to reach state-of-the-art performance) and generalise poorly in a lot of cases. This makes sense: representing every single aspect of a document, to be able to match it to any potential query, into a single vector is an extremely hard problem.

ColBERT and its variants, including JaColBERT, aim to combine the best of all worlds: by representing the documents as essentially *bags-of-embeddings*, we obtain superior performance and strong out-of-domain generalisation at much lower compute cost than cross-encoders.

The strong out-of-domain performance can be seen in our results: JaColBERT, despite not having been trained on Mr.TyDi and MIRACL, nearly matches e5 dense retrievers, who have been trained on these datasets.

On JSQuAD, which is partially out-of-domain for e5 (it has only been exposed to the English version) and entirely out-of-domain for JaColBERT, it outperforms all e5 models.

Moreover, this approach requires **considerably less data than dense embeddings**: To reach its current performance, JaColBERT v1 is only trained on 10M training triplets, compared to billion of examples for the multilingual e5 models.


# Training

### Training Data

The model is trained on the japanese split of MMARCO, augmented with hard negatives. [The data, including the hard negatives, is available on huggingface datasets](https://huggingface.co/datasets/bclavie/mmarco-japanese-hard-negatives).

We do not train nor perform data augmentation on any other dataset at this stage. We hope to do so in future work, or support practitioners intending to do so (feel free to [reach out](mailto:ben@clavie.eu)).

### Training Method

JColBERT is trained for a single epoch (1-pass over every triplet) on 8 NVidia L4 GPUs. Total training time was around 10 hours.

JColBERT is initiated from Tohoku University's excellent [bert-base-japanese-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-v3) and benefitted strongly from Nagoya University's work on building [strong Japanese SimCSE models](https://arxiv.org/abs/2310.19349), among other work.

We attempted to train JaColBERT with a variety of settings, including different batch sizes (8, 16, 32 per GPU) and learning rates (3e-6, 5e-6, 1e-5, 2e-5). The best results were obtained with 5e-6, though were very close when using 3e-6. Any higher learning rate consistently resulted in lower performance in early evaluations and was discarded. In all cases, we applied warmup steps equal to 10% of the total steps.

In-batch negative loss was applied, and we did not use any distillation methods (using the scores from an existing model).

# Results

See the table below for an overview of results, vs previous Japanese-only models and the current multilingual state-of-the-art (multilingual-e5).

Worth noting: JaColBERT is evaluated out-of-domain on all three datasets, whereas JSQuAD is partially (English version) and MIRACL & Mr.TyDi are fully in-domain for e5, likely contributing to their strong performance. In a real-world setting, I'm hopeful this could be bridged with moderate, quick (>2hrs) fine-tuning. 

(refer to the technical report for exact evaluation method + code. * indicates the best monolingual/out-of-domain result. **bold** is best overall result. _italic_ indicates the task is in-domain for the model.)

|                                                                           | JSQuAD                  |                      |        |                         | MIRACL                  |                      |        |                         | MrTyDi                  |                      |        |                         | Average                 |                      |        |
| ------------------------------------------------------------------------ | ----------------------- | -------------------- | ------ | ----------------------- | ----------------------- | -------------------- | ------ | ----------------------- | ----------------------- | -------------------- | ------ | ----------------------- | ----------------------- | -------------------- | ------ |
|                                                                           | R@1                     | R@5                  | R@10   |                         | R@3                     | R@5                  | R@10   |                         | R@3                     | R@5                  | R@10   |                         | R@\{1\|3\}              | R@5                  | R@10   |
| JaColBERT                                                                | **0.906***               | **0.968***            | **0.978***  |                         | 0.464*                   | 0.546*                | 0.645*  |                         | 0.744*                   | 0.781*                | 0.821*  |                         | 0.705*               | 0.765*                | 0.813*  |
| m-e5-large (in-domain)                                                   | 0.865                 | 0.966                | 0.977  |                         | **0.522**                   | **0.600**               |   **0.697**  |                         | **0.813**                  |  **0.856**                | **0.893**  |                         |  **0.730**                      |  **0.807**                    |  **0.856**      |
| m-e5-base (in-domain)                                                    | *0.838*                 | *0.955*              | 0.973  |                         | 0.482               | 0.553            | 0.632  |                         | 0.777               | 0.815            | 0.857  |                         | 0.699                   | 0.775            | 0.820  |
| m-e5-small (in-domain)                                                   | *0.840*                 | *0.954*              | 0.973  |                         | 0.464                   | 0.540                | 0.640  |                         | 0.767                   | 0.794                | 0.844  |                         | 0.690                   | 0.763                | 0.819  |
| GLuCoSE                                                                 | 0.645                   | 0.846                | 0.897  |                         | 0.369                   | 0.432                | 0.515  |                         | *0.617*                 | *0.670*              | 0.735  |                         | 0.544                   | 0.649                | 0.716  |
| sentence-bert-base-ja-v2                                                | 0.654                   | 0.863                | 0.914  |                         | 0.172                   | 0.224                | 0.338  |                         | 0.488                   | 0.549                | 0.611  |                         | 0.435                   | 0.545                | 0.621  |
| sup-simcse-ja-base                                                      | 0.632                   | 0.849                | 0.897  |                         | 0.133                   | 0.177                | 0.264  |                         | 0.454                   | 0.514                | 0.580  |                         | 0.406                   | 0.513                | 0.580  |
| sup-simcse-ja-large                                                     | 0.603                   | 0.833                | 0.889  |                         | 0.159                   | 0.212                | 0.295  |                         | 0.457                   | 0.517                | 0.581  |                         | 0.406                   | 0.521                | 0.588  |
| fio-base-v0.1                                                           | 0.700                   | 0.879                | 0.924  |                         | *0.279*                 | *0.358*              | 0.462  |                         | *0.582*                 | *0.649*              | 0.712  |                         | *0.520*                 | *0.629*              | 0.699  |


# Usage

## Installation

JaColBERT works using ColBERT+RAGatouille. You can install it and all its necessary dependencies by running:
```sh
pip install -U ragatouille
```

For further examples on how to use RAGatouille with ColBERT models, you can check out the [`examples` section it the github repository](https://github.com/bclavie/RAGatouille/tree/main/examples).

Specifically, example 01 shows how to build/query an index, 04 shows how you can use JaColBERT as a re-ranker, and 06 shows how to use JaColBERT for in-memory searching rather than using an index.

Notably, RAGatouille has metadata support, so check the examples out if it's something you need!

## Encoding and querying documents without an index

If you want to use JaColBERT without building an index, it's very simple, you just need to load the model, `encode()` some documents, and then `search_encoded_documents()`:

```python
from ragatouille import RAGPretrainedModel
RAG = RAGPretrainedModel.from_pretrained("bclavie/JaColBERT")

RAG.encode(['document_1', 'document_2', ...])
RAG.search_encoded_documents(query="your search query")
```

Subsequent calls to `encode()` will add to the existing in-memory collection. If you want to empty it, simply run `RAG.clear_encoded_docs()`.


## Indexing

In order for the late-interaction retrieval approach used by ColBERT to work, you must first build your index.
Think of it like using an embedding model, like e5, to embed all your documents and storing them in a vector database.
Indexing is the slowest step  retrieval is extremely quick. There are some tricks to speed it up, but the default settings work fairly well:

```python
from ragatouille import RAGPretrainedModel

RAG = RAGPretrainedModel.from_pretrained("bclavie/JaColBERT")
documents = [ "マクドナルドのフライドポテトの少量のカロリーはいくつですか？マクドナルドの小さなフライドポテトのカロリーマクドナルドのウェブサイトには、次のように記載されています。フライドポテトの小さな注文で230カロリーケチャップで25カロリー、ケチャップパケットで15カロリー。",]
RAG.index(name="My_first_index", collection=documents)
```

The index files are stored, by default, at `.ragatouille/colbert/indexes/{index_name}`.

And that's it! Let it run, and your index and all its representations (compressed to 2bits by default) will have been generated.


## Searching

Once you have created an index, searching through it is just as simple! If you're in the same session and `RAG` is still loaded, you can directly search the newly created index.
Otherwise, you'll want to load it from disk:

```python
RAG = RAGPretrainedModel.from_index(".ragatouille/colbert/indexes/My_first_index")
```

And then query it:

```python
RAG.search(query="What animation studio did Miyazaki found?")
> [{'content': 'In April 1984, Miyazaki opened his own office in Suginami Ward, naming it Nibariki.\n\n\n=== Studio Ghibli ===\n\n\n==== Early films (1985–1996) ====\nIn June 1985, Miyazaki, Takahata, Tokuma and Suzuki founded the animation production company Studio Ghibli, with funding from Tokuma Shoten. Studio Ghibli\'s first film, Laputa: Castle in the Sky (1986), employed the same production crew of Nausicaä. Miyazaki\'s designs for the film\'s setting were inspired by Greek architecture and "European urbanistic templates".',
   'score': 25.90448570251465,
   'rank': 1,
   'document_id': 'miyazaki',
   'document_metadata': {'entity': 'person', 'source': 'wikipedia'}},
  {'content': 'Hayao Miyazaki (宮崎 駿 or 宮﨑 駿, Miyazaki Hayao, Japanese: [mijaꜜzaki hajao]; born January 5, 1941) is a Japanese animator, filmmaker, and manga artist. A co-founder of Studio Ghibli, he has attained international acclaim as a masterful storyteller and creator of Japanese animated feature films, and is widely regarded as one of the most accomplished filmmakers in the history of animation.\nBorn in Tokyo City in the Empire of Japan, Miyazaki expressed interest in manga and animation from an early age, and he joined Toei Animation in 1963. During his early years at Toei Animation he worked as an in-between artist and later collaborated with director Isao Takahata.',
   'score': 25.572620391845703,
   'rank': 2,
   'document_id': 'miyazaki',
   'document_metadata': {'entity': 'person', 'source': 'wikipedia'}},
  [...]
]
```


# Citation

If you'd like to cite this work, please cite the technical report:

```
@misc{clavié2023jacolbert,
      title={JaColBERT and Hard Negatives, Towards Better Japanese-First Embeddings for Retrieval: Early Technical Report}, 
      author={Benjamin Clavié},
      year={2023},
      eprint={2312.16144},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```