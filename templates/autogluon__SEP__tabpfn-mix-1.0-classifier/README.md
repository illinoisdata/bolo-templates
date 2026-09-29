---
license: apache-2.0
pipeline_tag: tabular-classification
---

# TabPFNMix Classifier

TabPFNMix classifier is a tabular foundation model that is pre-trained on purely synthetic datasets sampled from a mix of random classifiers. 

## Architecture

TabPFNMix is based on a 12-layer encoder-decoder Transformer of 37 M parameters. We use a pre-training strategy incorporating in-context learning, similar to that used by TabPFN and TabForestPFN.

## Usage

To use TabPFNMix classifier, install AutoGluon by running:

```sh
pip install autogluon
```

A minimal example showing how to perform fine-tuning and inference using the TabPFNMix classifier:

```python
import pandas as pd

from autogluon.tabular import TabularPredictor


if __name__ == '__main__':
    train_data = pd.read_csv('https://autogluon.s3.amazonaws.com/datasets/Inc/train.csv')
    subsample_size = 5000  
    if subsample_size is not None and subsample_size < len(train_data):
        train_data = train_data.sample(n=subsample_size, random_state=0)
    test_data = pd.read_csv('https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv')

    tabpfnmix_default = {
        "model_path_classifier": "autogluon/tabpfn-mix-1.0-classifier",
        "model_path_regressor": "autogluon/tabpfn-mix-1.0-regressor",
        "n_ensembles": 1,
        "max_epochs": 30,
    }

    hyperparameters = {
        "TABPFNMIX": [
            tabpfnmix_default,
        ],
    }

    label = "class"

    predictor = TabularPredictor(label=label)
    predictor = predictor.fit(
        train_data=train_data,
        hyperparameters=hyperparameters,
        verbosity=3,
    )

    predictor.leaderboard(test_data, display=True)
```

## Citation

If you find TabPFNMix useful for your research, please consider citing the associated papers:

```
@article{erickson2020autogluon,
  title={Autogluon-tabular: Robust and accurate automl for structured data},
  author={Erickson, Nick and Mueller, Jonas and Shirkov, Alexander and Zhang, Hang and Larroy, Pedro and Li, Mu and Smola, Alexander},
  journal={arXiv preprint arXiv:2003.06505},
  year={2020}
}

@article{hollmann2022tabpfn,
  title={Tabpfn: A transformer that solves small tabular classification problems in a second},
  author={Hollmann, Noah and M{\"u}ller, Samuel and Eggensperger, Katharina and Hutter, Frank},
  journal={arXiv preprint arXiv:2207.01848},
  year={2022}
}

@article{breejen2024context,
  title={Why In-Context Learning Transformers are Tabular Data Classifiers},
  author={Breejen, Felix den and Bae, Sangmin and Cha, Stephen and Yun, Se-Young},
  journal={arXiv preprint arXiv:2405.13396},
  year={2024}
}
```

## License

This project is licensed under the Apache-2.0 License.