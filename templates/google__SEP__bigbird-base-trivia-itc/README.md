---
language: en
license: apache-2.0
datasets:
- trivia_qa
---

# BigBird base trivia-itc

This model is a fine-tune checkpoint of `bigbird-roberta-base`, fine-tuned on `trivia_qa` with `BigBirdForQuestionAnsweringHead` on its top.

Check out [this](https://colab.research.google.com/drive/1DVOm1VHjW0eKCayFq1N2GpY6GR9M4tJP?usp=sharing) to see how well `google/bigbird-base-trivia-itc` performs on question answering.

## How to use

Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import BigBirdForQuestionAnswering

# by default its in `block_sparse` mode with num_random_blocks=3, block_size=64
model = BigBirdForQuestionAnswering.from_pretrained("google/bigbird-base-trivia-itc")

# you can change `attention_type` to full attention like this:
model = BigBirdForQuestionAnswering.from_pretrained("google/bigbird-base-trivia-itc", attention_type="original_full")

# you can change `block_size` & `num_random_blocks` like this:
model = BigBirdForQuestionAnswering.from_pretrained("google/bigbird-base-trivia-itc", block_size=16, num_random_blocks=2)

question = "Replace me by any text you'd like."
context = "Put some context for answering"
encoded_input = tokenizer(question, context, return_tensors='pt')
output = model(**encoded_input)
```

# Fine-tuning config & hyper-parameters

- No. of global token = 128
- Window length = 192
- No. of random token = 192
- Max. sequence length = 4096
- No. of heads = 12
- No. of hidden layers = 12
- Hidden layer size = 768
- Batch size = 32
- Loss = cross-entropy noisy spans

## BibTeX entry and citation info

```tex
@misc{zaheer2021big,
      title={Big Bird: Transformers for Longer Sequences}, 
      author={Manzil Zaheer and Guru Guruganesh and Avinava Dubey and Joshua Ainslie and Chris Alberti and Santiago Ontanon and Philip Pham and Anirudh Ravula and Qifan Wang and Li Yang and Amr Ahmed},
      year={2021},
      eprint={2007.14062},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```