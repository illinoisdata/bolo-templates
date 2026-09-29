---
license: apache-2.0 # Assuming a common open-source license, adjust if known
language:
- en
library_name: pytorch
tags:
- chess
- embeddings
- transformer
- vision-transformer
- self-supervised-learning
- pytorch
datasets:
- lichess
- computerchess # Hypothetical dataset tag based on paper reference [15]
model-index:
- name: ChessLM-Encoder
  results: [] # Qualitative results described in Evaluation section
---

# ChessLM: Contextual Chess Position Embeddings

## Model Description

**ChessLM** is a Transformer-based model designed to learn rich, contextual vector representations (embeddings) for chess positions. Inspired by self-supervised learning in NLP (like BERT) and adapting the Vision Transformer (ViT) architecture, ChessLM focuses on capturing the strategic and thematic similarities between board states, rather than primarily predicting the best move or evaluating the position's score like traditional chess engines.

The core of the model is a Transformer encoder that processes the 8x8 board, considering piece types, locations (via positional embeddings), and whose turn it is (via a turn embedding). It outputs a **256-dimensional embedding vector** for a given position (represented by a FEN string).

## Model Architecture and Training

The model adopts an encoder Transformer architecture with 6 layers each with 8 heads. The model has approximatly 4.5 million total parameters, all of which are trainable. 

To encourage the model to learn comprehensive representations of chess positions, we employ a multi-task learning strategy combining two self-supervised objectives, mirroring techniques used in large language model pre-training:

- Masked Piece Prediction (MPP): Analogous to BERT’s Masked Language Model task, a random subset of pieces on the input board are masked (replaced with a mask token). The model’s objective is to predict the original identity of these masked pieces based on the surrounding context (the remaining pieces and whose turn it is). This task allows the model to understand typical piece configurations, legal placements, and the relationships between pieces. For MPP 10% of the pieces were masked.
- Moves Difference Prediction: This task involves presenting the model with two distinct board states (a start and an end position) from actual game sequences. The model must predict the number of moves (plies) separating these two positions. This objective encourages the model to learn about piece mobility, game dynamics, and the plausible evolution of a position over time.

Training used two distinct datasets, pre-processed into structured formats to facilitate the self-supervised tasks. These datasets are derived from a large corpus of chess games and positions, available from the Lichess database (https://database.lichess.org/) and the computerchess (https://www.computerchess.org.uk/ccrl/) database.

The full training details and modle architecture can be found in the technical writeup here: https://bluehood.github.io/research/benh_Beyond_Evaluation__Learning_Contextual_Chess_Position_Representations_2025.pdf.

## Intended Uses & Limitations

### Intended Use

The primary intended use of this model is to generate embeddings that capture the "feel" or thematic essence of a chess position. These embeddings can be used for:

* **Position Similarity Search:** Finding positions in a database that are structurally or strategically similar to a query position. This is useful for finding similar games or puzzles.
* **Retrieval-Augmented Generation (RAG):** Enhancing chess analysis tools by retrieving similar historical positions and their outcomes or analyses to provide additional context to another model.
* **Downstream Task Input:** Serving as input features for tasks like:
    * Classifying tactical motifs. positional themes or more generally chess positions.
    * Suggesting relevant chess puzzles based on similarity.


### Limitations

* **Not an Evaluation Engine:** ChessLM was **not** trained to predict the evaluation (e.g., centipawn score) of a position. Qualitative analysis shows that while it captures structural similarities, the embeddings are **not highly sensitive** to subtle tactical nuances or precise piece activity that heavily influence a position's true strength. Positions deemed similar by the embeddings can have vastly different engine evaluations.
* **Focus on Structure:** The model may overemphasize structural similarities (like pawn formations) while potentially under-weighting critical dynamic factors or specific tactical threats.

## How to Use
For detailed usage for this model please see https://github.com/bluehood/Encoder-ChessLM and https://github.com/bluehood/Encoder-ChessLM/blob/main/examples/generate_embedding.py.

If you use this model, its embeddings, or the concepts presented in the associated paper, please cite:

```
@misc{hull2025beyond,
      title={Beyond Evaluation: Learning Contextual Chess Position Representations},
      author={Ben Hull},
      year={2025},
      howpublished={Accessed via \url{[https://bluehood.github.io/](https://bluehood.github.io/)}},
      note={Technical report}
}
```