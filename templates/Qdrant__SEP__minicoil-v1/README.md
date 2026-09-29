---
license: apache-2.0
language:
- en
pipeline_tag: sentence-similarity
base_model:
- jinaai/jina-embeddings-v2-small-en
---


# MiniCOIL v1

MiniCOIL is a sparse neural embedding model for textual retrieval. 

It creates 4-dimensional embeddings for each word stem, capturing the word's meaning.  
These meaning embeddings are combined into a bag-of-words (BoW) representation of the input text.  
The final sparse representation is calculated by weighting each word using the BM25 scoring formula.

<img src="https://storage.googleapis.com/qdrant-examples/miniCOIL_inference.png" alt="miniCOIL inference" width="600"/>

In the case of a word's absence in the miniCOIL vocabulary, word weight in sparse representation is purely based on the BM25 score.

Read more about miniCOIL in [the article](https://qdrant.tech/articles/minicoil).


## Usage

This model is designed to be used with the [FastEmbed](https://github.com/qdrant/fastembed) library.

> Note:
This model was designed with Qdrant's specifics in mind; miniCOIL sparse vectors in Qdrant have to be configured with [Modifier.IDF](https://qdrant.tech/documentation/concepts/indexing/?q=modifier#idf-modifier). Otherwise, you'll have to personally calculate & scale the produced sparse representations by the IDF part of the BM25 formula.

```py
from fastembed import SparseTextEmbedding

model = SparseTextEmbedding(model_name="Qdrant/minicoil-v1")

documents = [
    "fruit bat",
    "baseball bat",
]

embeddings = list(model.embed(documents))
query_embedding = list(model.query_embed("bat in a cave"))

# embeddings[0] - "fruit bat"
# SparseEmbedding(values=array([-1.2509683 , -0.9510568 , -0.55398935,  0.188206  ,  1.0497165 ,
#       0.31841373, -0.82047373, -0.9671025 ], dtype=float32), indices=array([ 8992,  8993,  8994,  8995, 18832, 18833, 18834, 18835],
#      dtype=int32)) # 8992,  8993,  8994,  8995 - 4D "fruit" representation, 18832, 18833, 18834, 18835 - 4D "bat" representation

# embeddings[1] - "baseball bat"
#SparseEmbedding(values=array([ 1.1004512 , -0.5959816 ,  0.23380531, -1.0912857 ,  1.6768292 ],
#      dtype=float32), indices=array([     18832,      18833,      18834,      18835, 2068153269],
#      dtype=int32)) # 18832, 18833, 18834, 18835 - 4D "bat" representation, 2068153269 - 1D "baseball" representation, as "baseball" is not in miniCOIL_v1 vocabulary, so we fall back to Qdrant/bm25 1D score
 
# query_embedding - "bat in a cave"
#[SparseEmbedding(values=array([ 0.5656684 ,  0.395691  , -0.48945513, -0.5328054 , -0.5889519 ,
#         0.55871224,  0.27323055,  0.5160634 ], dtype=float32), indices=array([18832, 18833, 18834, 18835, 18920, 18921, 18922, 18923],
#       dtype=int32))] # 18832, 18833, 18834, 18835 - 4D "bat" representation, 18920, 18921, 18922, 18923 - 4D "cave" representation, "in"/"a" - removed stop words

bat_1 = embeddings[0].values[4:8]
bat_2 = embeddings[1].values[:4]
bat_query = query_embedding[0].values[:4]

dot_product_1 = (bat_1 * bat_query).sum() #np.float32(1.6366475) measuring dot product between matching indices of sparse vectors
dot_product_2 = (bat_2 * bat_query).sum() #np.float32(0.8536716) measuring dot product between matching indices of sparse vectors

#1.6366475 > 0.8536716, as "bat" in "fruit bat" is more semantically similar to "bat" in "bat in a cave", as "bat" in "baseball bat"
```