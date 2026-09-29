---
license: mit
datasets:
- Superar/Puntuguese
language:
- pt
base_model:
- neuralmind/bert-base-portuguese-cased
pipeline_tag: text-classification
tags:
- humor
- pun
- pun-recognition
---

# Pun Recognition in Portuguese

This is a Pun Recognition model for texts in Portuguese, as reported in two of our publications:

- **Exploring Multimodal Models for Humor Recognition in Portuguese** ([PROPOR 2024 Paper](https://aclanthology.org/2024.propor-1.62/))
- **Puntuguese: A Corpus of Puns in Portuguese with Micro-Edits** ([LREC-COLING 2024 Paper](https://aclanthology.org/2024.lrec-main.1167/))

The model has been fine-tuned on the [Puntuguese](https://huggingface.co/datasets/Superar/Puntuguese) dataset, a collection of puns and corresponding non-pun texts in Portuguese.

With this model, we achieved a maximum of **69% F1-Score** in the task of Pun Recognition with Puntuguese.

## Installation and Setup

To use this model, ensure you have the following dependencies installed:
```bash
pip install accelerate datasets scikit-learn torch transformers
```

## How to Use
To load the Puntuguese corpus and use the model for pun classification, run the following script:

```python
from datasets import load_dataset
from transformers import pipeline
import pandas as pd
from sklearn.metrics import classification_report

dataset = load_dataset('Superar/Puntuguese')
classifier = pipeline('text-classification', model='Superar/pun-recognition-pt', device=0)

prediction = classifier(dataset['test']['text'])
pred_df = pd.DataFrame(prediction)
pred_df['label'] = pred_df['label'].str[-1].astype(int)

y_true = dataset['test']['label']
y_pred = pred_df['label']
print(classification_report(y_true, y_pred))
```

## Hyperparameters

We used [Weights and Biases](https://wandb.ai/) to do a random search to optimize for the lowest evaluation loss using the following configuration:

```python
{
  'method': 'random',
  'metric': {'name': 'loss', 'goal': 'minimize'},
  'parameters': {
  'optim': {'values': ['adamw_torch', 'sgd']},
  'learning_rate': {'distribution': 'uniform', 'min': 1e-6, 'max': 1e-4},
  'per_device_train_batch_size': {'values': [16, 32, 64, 128]},
  'num_train_epochs': {'distribution': 'uniform', 'min': 1, 'max': 5}
  }
}
```

The best hyperparameters found were:

- **Learning Rate**: 8.47e-5
- **Optimizer**: AdamW
- **Training Batch Size**: 128
- **Epochs**: 2

## Citation

```bibtex
@inproceedings{InacioEtAl2024,
  title = {Puntuguese: A Corpus of Puns in {{Portuguese}} with Micro-Edits},
  booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation ({{LREC-COLING}} 2024)},
  author = {In{\'a}cio, Marcio Lima and {Wick-Pedro}, Gabriela and Ramisch, Renata and Esp{\'{\i}}rito Santo, Lu{\'{\i}}s and Chacon, Xiomara S. Q. and Santos, Roney and Sousa, Rog{\'e}rio and Anchi{\^e}ta, Rafael and Goncalo Oliveira, Hugo},
  editor = {Calzolari, Nicoletta and Kan, Min-Yen and Hoste, Veronique and Lenci, Alessandro and Sakti, Sakriani and Xue, Nianwen},
  year = {2024},
  month = may,
  pages = {13332--13343},
  publisher = {{ELRA and ICCL}},
  address = {Torino, Italia},
  url = {https://aclanthology.org/2024.lrec-main.1167}
}
```