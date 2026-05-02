# InRanker-base (220M parameters)

InRanker is a version of monoT5 distilled from [monoT5-3B](https://huggingface.co/castorini/monot5-3b-msmarco-10k) with increased effectiveness on out-of-domain scenarios.
Our key insight were to use language models and rerankers to generate as much as possible
synthetic "in-domain" training data, i.e., data that closely resembles
the data that will be seen at retrieval time. The pipeline used for training consists of
two distillation phases that do not require additional user queries
or manual annotations: (1) training on existing supervised soft
teacher labels, and (2) training on teacher soft labels for synthetic
queries generated using a large language model.

The paper with further details can be found [here](https://arxiv.org/abs/2401.06910). The code and library are available at
https://github.com/unicamp-dl/InRanker

## Usage
The library was tested using python 3.10 and is installed with:
```bash
pip install inranker
```

The code for inference is:
```python
from inranker import T5Ranker

model = T5Ranker(model_name_or_path="unicamp-dl/InRanker-base")

docs = [
    "The capital of France is Paris",
    "Learn deep learning with InRanker and transformers"
]
scores = model.get_scores(
    query="What is the best way to learn deep learning?",
    docs=docs
)
# Scores are sorted in descending order (most relevant to least)
# scores -> [0, 1]
sorted_scores = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
```

## How to Cite
```
@misc{laitz2024inranker,
      title={InRanker: Distilled Rankers for Zero-shot Information Retrieval}, 
      author={Thiago Laitz and Konstantinos Papakostas and Roberto Lotufo and Rodrigo Nogueira},
      year={2024},
      eprint={2401.06910},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}
```