---
license: cc-by-nc-sa-4.0
---

# Inclusively Rewriting model

This model is an Italian sequence-to-sequence model fine-tuned from the [IT5-large](https://huggingface.co/gsarti/it5-large) for the task of inclusive language rewriting.

It has been trained to analyze and rewrite sentences in Italian to make them more inclusive (if needed).

For example, the sentence `I professori devono essere preparati` (The professors must be prepared) is rewritten as `Il personale docente deve essere preparato` (The teaching staff must be prepared).

## Training data

The model has been trained on a dataset containing a total of 4705 pairs of sentences, each pair containing an inclusive and a non-inclusive sentence. The dataset has been split as follows:
- Training set: 3764 pairs
- Validation set: 470 pairs
- Test set: 471 pairs

We also leverage a small set of synthetic data (generated using a set of rules) to improve the model's performance on the test set.
The training is so performed on a total of 3764 + 75 = **3839** pairs.

The data collection has been manually annotated by experts in the field of inclusive language (dataset is not publicly available yet).

## Training procedure

The model has been fine-tuned from the [Italian BERT model](https://huggingface.co/dbmdz/bert-base-italian-xxl-cased) using the following hyperparameters:
- `max_length`: 128
- `batch_size`: 8
- `learning_rate`: 5e-5
- `warmup_steps`: 500
- `epochs`: 25 (best model is selected based on validation `BLEU` score)
- `optimizer`: AdamW

## Evaluation results

The model has been evaluated on the test set and obtained the following results:

| Model | BLEU | ROUGE-2 F1 | Human Correct | Human Partial (L) | Human Incorrect (L) |
|-------|------|------------|---------------|---------------|-----------------|
| IT5 (no synth. data) | 80.32 | 87.17 | 64.76 | 15.71 | 19.52 |
| **This**             | 80.79 | 87.47 | 69.52 | 17.14 | 13.22 |

(L) in the metric indicates "Lower is better".
The comparison with the same version of the model without synthetic data shows that the synthetic data is useful to improve the model's performance on the test set.
Other comparisons can be found in the [paper](#citation).

## Citation

If you use this model, please make sure to cite the following papers:

**Main paper**:

```bibtex
@article{10.1145/3729237,
author = {Greco, Salvatore and La Quatra, Moreno and Cagliero, Luca and Cerquitelli, Tania},
title = {Towards AI-Assisted Inclusive Language Writing in Italian Formal Communications},
year = {2025},
issue_date = {August 2025},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {16},
number = {4},
issn = {2157-6904},
url = {https://doi.org/10.1145/3729237},
doi = {10.1145/3729237},
journal = {ACM Trans. Intell. Syst. Technol.},
month = jun,
articleno = {79},
numpages = {24},
keywords = {inclusive language, natural language processing, text classification, text generation}
}
```

**Demo paper**:

```bibtex
@InProceedings{PKDD23_inclusively,
author="La Quatra, Moreno
and Greco, Salvatore
and Cagliero, Luca
and Cerquitelli, Tania",
title="Inclusively: An AI-Based Assistant for Inclusive Writing",
booktitle="Machine Learning and Knowledge Discovery in Databases: Applied Data Science and Demo Track",
year="2023",
publisher="Springer Nature Switzerland",
address="Cham",
pages="361--365",
isbn="978-3-031-43430-3",
doi="10.1007/978-3-031-43430-3_31"
}
```