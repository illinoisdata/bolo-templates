---
{}
---

# Model Card for ProteInferTorch trained on EC task with CLUSTERED data split

Unofficial PyTorch version of ProteInfer (https://github.com/google-research/proteinfer), originally implemented in TensorFlow 1.X. 

ProteInfer is a model for protein function prediction that is trained to predict the functional properties of protein sequences using Deep Learning.
Authors provide pre-trained models for two tasks: Gene Ontology (GO) and Enzyme Commission (EC) number prediction, as well as two data splits two data splits: random and clustered.
Additionally, for every task and data split combination, authors trained multiple models using different random seeds.

This model is trained on the **EC** task with the **CLUSTERED** data split, and corresponds to the model with ID **13704042** in the original ProteInfer repository.

## Model Details

### Model Description

For all the details about the model, please refer to the original ProteInfer paper: https://elifesciences.org/articles/80942.

- **Developed by:** Samir Char, adapted from the original TensorFlow 1.X implementation by Google Research
- **Model type:** Dilated Convolutional Neural Network
- **License:** Apache

### Model Sources

- **Repository:** https://github.com/samirchar/proteinfertorch

## Uses

### Direct Use

This model is intended for research use. It can be used for protein function prediction tasks, such as Gene Ontology (GO) and Enzyme Commission (EC) number prediction, or
as a feature extractor for protein sequences.

### Downstream Use

This model can be fine-tuned for any task that can benefit from function-aware protein embeddings.

## Bias, Risks, and Limitations

- This model is intended for use on protein sequences. It is not meant for other biological sequences, such as DNA sequences.

## How to Get Started with the Model

```
git clone https://github.com/samirchar/proteinfertorch
cd proteinfertorch
conda env create -f environment.yml
conda activate proteinfertorch
pip install -e ./  # make sure ./ is the dir including setup.py
```

For detailed instructions on package usage, please refer to the README in model repo

## Evaluation

### Results

TODO: Add table comparing the performance of this model with the original TensorFlow 1.X implementation.


## Technical Specifications 

### Compute Infrastructure

8xV100 GPU cluster


## Citation

**BibTeX:**
If you use this model in your work, I would greatly appreciate it if you could cite it as follows:

```bibtex
@misc{yourname2024pytorchmodel,
  title={ProteInferTorch: a PyTorch implementation of ProteInfer},
  version={v1.0.0},
  author={Samir Char},
  year={2024},
  month={12},
  day={08},
  doi={10.5281/zenodo.14514368},
  url={https://github.com/samirchar/proteinfertorch}
}
```


## Model Card Authors

Samir Char

## Model Card Contact

Samir Char