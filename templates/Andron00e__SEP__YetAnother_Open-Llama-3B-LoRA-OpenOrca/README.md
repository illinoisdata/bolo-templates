---
license: apache-2.0
datasets:
- Open-Orca/OpenOrca
language:
- en
library_name: transformers
pipeline_tag: question-answering
metrics:
- accuracy
---
## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->



- **Developed by:** Andron00e
- **Language(s) (NLP):** Python (PyTorch, transformers, peft)
- **License:** apache-2.0
- **Finetuned from model:** openlm-research/open_llama_3b

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/Andron00e/Fine-Tuning-project

### Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->
https://huggingface.co/datasets/Open-Orca/OpenOrca

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->
Evaluation of the model was carried out using EulerAI library, more [precisely](https://github.com/EleutherAI/lm-evaluation-harness/tree/e47e01beea79cfe87421e2dac49e64d499c240b4#task-versioning)

#### Testing Data

<!-- This should link to a Data Card if possible. -->
hellaswag testing dataset

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

Accuracy

### Results and Model Examination

|  Task   |Version| Metric |Value |   |Stderr|
|---------|------:|--------|-----:|---|-----:|
|hellaswag|      0|acc     |0.4899|±  |0.0050|
|         |       |acc_norm|0.6506|±  |0.0048|





## Citations

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->
```
@software{openlm2023openllama,
  author = {Geng, Xinyang and Liu, Hao},
  title = {OpenLLaMA: An Open Reproduction of LLaMA},
  month = May,
  year = 2023,
  url = {https://github.com/openlm-research/open_llama}
}
```
```
@software{eval-harness,
  author       = {Gao, Leo and
                  Tow, Jonathan and
                  Biderman, Stella and
                  Black, Sid and
                  DiPofi, Anthony and
                  Foster, Charles and
                  Golding, Laurence and
                  Hsu, Jeffrey and
                  McDonell, Kyle and
                  Muennighoff, Niklas and
                  Phang, Jason and
                  Reynolds, Laria and
                  Tang, Eric and
                  Thite, Anish and
                  Wang, Ben and
                  Wang, Kevin and
                  Zou, Andy},
  title        = {A framework for few-shot language model evaluation},
  month        = sep,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v0.0.1},
  doi          = {10.5281/zenodo.5371628},
  url          = {https://doi.org/10.5281/zenodo.5371628}
}
```

## Model Card Authors and Contact

[Andron00e](https://github.com/Andron00e)