---
pipeline_tag: text-ranking
language: fr
datasets:
- stsb_multi_mt
tags:
- Text
- Sentence Similarity
- Sentence-Embedding
- camembert-base
license: apache-2.0
model-index:
- name: sentence-camembert-base by Van Tuan DANG
  results:
  - task:
      type: Text Similarity
      name: Sentence-Embedding
    dataset:
      name: Text Similarity fr
      type: stsb_multi_mt
      args: fr
    metrics:
    - type: Pearson_correlation_coefficient
      value: xx.xx
      name: Test Pearson correlation coefficient
---

## Model

Cross-Encoder for sentence-similarity

This model was trained using [sentence-transformers](https://www.SBERT.net) Cross-Encoder class.

## Training Data
This model was trained on the [STS benchmark dataset](https://huggingface.co/datasets/stsb_multi_mt/viewer/fr/train). The model will predict a score between 0 and 1 how for the semantic similarity of two sentences.


## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import CrossEncoder
model = CrossEncoder('dangvantuan/CrossEncoder-camembert-large', max_length=128)
scores = model.predict([('Un avion est en train de décoller.', "Un homme joue d'une grande flûte."), ("Un homme étale du fromage râpé sur une pizza.", "Une personne jette un chat au plafond") ])

```
## Evaluation
The model can be evaluated as follows on the French test data of stsb.
```python
from sentence_transformers.readers import InputExample
from sentence_transformers.cross_encoder.evaluation import CECorrelationEvaluator
from datasets import load_dataset
def convert_dataset(dataset):
    dataset_samples=[]
    for df in dataset:
        score = float(df['similarity_score'])/5.0  # Normalize score to range 0 ... 1
        inp_example = InputExample(texts=[df['sentence1'], 
                                    df['sentence2']], label=score)
        dataset_samples.append(inp_example)
    return dataset_samples

# Loading the dataset for evaluation
df_dev = load_dataset("stsb_multi_mt", name="fr", split="dev")
df_test = load_dataset("stsb_multi_mt", name="fr", split="test")

# Convert the dataset for evaluation

# For Dev set:
dev_samples = convert_dataset(df_dev)
val_evaluator = CECorrelationEvaluator.from_input_examples(dev_samples, name='sts-dev')
val_evaluator(model, output_path="./")

# For Test set

test_samples = convert_dataset(df_test)
test_evaluator = CECorrelationEvaluator.from_input_examples(test_samples, name='sts-test')
test_evaluator(models, output_path="./")
```
**Test Result**: 
The performance is measured using Pearson and Spearman correlation:
- On dev
| Model  | Pearson correlation | Spearman correlation  |  #params  |
| ------------- | ------------- | ------------- |------------- |
| [dangvantuan/CrossEncoder-camembert-large](https://huggingface.co/dangvantuan/CrossEncoder-camembert-large)| 90.11 |90.01 | 336M |

- On test
| Model  | Pearson correlation | Spearman correlation  |
| ------------- | ------------- | ------------- |
| [dangvantuan/CrossEncoder-camembert-large](https://huggingface.co/dangvantuan/CrossEncoder-camembert-large)| 88.16 | 87.57|