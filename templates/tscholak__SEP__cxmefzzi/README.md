---
language: 
  - en
thumbnail: "https://repository-images.githubusercontent.com/401779782/c2f46be5-b74b-4620-ad64-57487be3b1ab"
tags:
- text2sql
widget:
- "How many singers do we have? | concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id"
license: "apache-2.0"
datasets:
- spider
metrics:
- spider
---

## tscholak/cxmefzzi

Fine-tuned weights for [PICARD - Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models](https://arxiv.org/abs/2109.05093) based on [T5-3B](https://huggingface.co/t5-3b).


### Training Data

The model has been fine-tuned on the 7000 training examples in the [Spider text-to-SQL dataset](https://yale-lily.github.io/spider). The model solves Spider's zero-shot text-to-SQL translation task, and that means that it can generalize to unseen SQL databases.


### Training Objective

This model was initialized with [T5-3B](https://huggingface.co/t5-3b) and fine-tuned with the text-to-text generation objective.

Questions are always grounded in a database schema, and the model is trained to predict the SQL query that would be used to answer the question. The input to the model is composed of the user's natural language question, the database identifier, and a list of tables and their columns:

```
[question] | [db_id] | [table] : [column] ( [content] , [content] ) , [column] ( ... ) , [...] | [table] : ... | ...
```

The model outputs the database identifier and the SQL query that will be executed on the database to answer the user's question:

```
[db_id] | [sql]
```


### Performance

Out of the box, this model achieves 71.5 % exact-set match accuracy and 74.4 % execution accuracy on the Spider development set. On the test set, the model achieves 68.0 % exact-set match accuracy and 70.1 % execution accuracy.

Using the PICARD constrained decoding method (see [the official PICARD implementation](https://github.com/ElementAI/picard)), the model's performance can be improved to **75.5 %** exact-set match accuracy and **79.3 %** execution accuracy on the Spider development set. On the test set and with PICARD, the model achieves **71.9 %** exact-set match accuracy and **75.1 %** execution accuracy.


### Usage

Please see [the official repository](https://github.com/ElementAI/picard) for scripts and docker images that support evaluation and serving of this model.


### References

1. [PICARD - Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models](https://arxiv.org/abs/2109.05093)

2. [Official PICARD code](https://github.com/ElementAI/picard)


### Citation

```bibtex
@inproceedings{Scholak2021:PICARD,
  author = {Torsten Scholak and Nathan Schucher and Dzmitry Bahdanau},
  title = "{PICARD}: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models",
  booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
  month = nov,
  year = "2021",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2021.emnlp-main.779",
  pages = "9895--9901",
}
```