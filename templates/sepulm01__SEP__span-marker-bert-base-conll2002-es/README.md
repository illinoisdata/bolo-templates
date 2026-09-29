---
language:
- es
license: cc-by-sa-4.0
library_name: span-marker
tags:
- span-marker
- token-classification
- ner
- named-entity-recognition
- generated_from_span_marker_trainer
datasets:
- conll2002
metrics:
- precision
- recall
- f1
widget:
- text: Por otro lado, el primer ministro portugués, Antonio Guterres, presidente
    de turno del Consejo Europeo, recibió hoy al ministro del Interior de Colombia,
    Hugo de la Calle, enviado especial del presidente de su país, Andrés Pastrana.
- text: Los consejeros de la Presidencia, Gaspar Zarrías, de Justicia, Carmen Hermosín,
    y de Asuntos Sociales, Isaías Pérez Saldaña, darán comienzo mañana a los turnos
    de comparecencias de los miembros del Gobierno andaluz en el Parlamento autonómico
    para informar de las líneas de actuación de sus departamentos.
- text: '(SV2147) PP: PROBLEMAS INTERNOS PSOE INTERFIEREN EN POLITICA DE LA JUNTA
    Córdoba (EFE).'
- text: Cuando vino a Soria, en febrero de 1998, para sustituir al entonces destituido
    Antonio Gómez, estaba dirigiendo al Badajoz B en tercera división y consiguió
    con el Numancia la permanencia en la última jornada frente al Hércules.
- text: El ministro ecuatoriano de Defensa, Hugo Unda, aseguró hoy que las Fuerzas
    Armadas respetarán la decisión del Parlamento sobre la amnistía para los involucrados
    en la asonada golpista del pasado 21 de enero, cuando fue derrocado el presidente
    Jamil Mahuad.
pipeline_tag: token-classification
base_model: bert-base-cased
model-index:
- name: SpanMarker with bert-base-cased on conll2002
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    dataset:
      name: Unknown
      type: conll2002
      split: test
    metrics:
    - type: f1
      value: 0.8200812536273941
      name: F1
    - type: precision
      value: 0.8331367924528302
      name: Precision
    - type: recall
      value: 0.8074285714285714
      name: Recall
---

# SpanMarker with bert-base-cased on conll2002

This is a [SpanMarker](https://github.com/tomaarsen/SpanMarkerNER) model trained on the [conll2002](https://huggingface.co/datasets/conll2002) dataset that can be used for Named Entity Recognition. This SpanMarker model uses [bert-base-cased](https://huggingface.co/bert-base-cased) as the underlying encoder.

## Model Details

### Model Description
- **Model Type:** SpanMarker
- **Encoder:** [bert-base-cased](https://huggingface.co/bert-base-cased)
- **Maximum Sequence Length:** 256 tokens
- **Maximum Entity Length:** 8 words
- **Training Dataset:** [conll2002](https://huggingface.co/datasets/conll2002)
- **Language:** es
- **License:** cc-by-sa-4.0

### Model Sources

- **Repository:** [SpanMarker on GitHub](https://github.com/tomaarsen/SpanMarkerNER)
- **Thesis:** [SpanMarker For Named Entity Recognition](https://raw.githubusercontent.com/tomaarsen/SpanMarkerNER/main/thesis.pdf)

### Model Labels
| Label | Examples                                                          |
|:------|:------------------------------------------------------------------|
| LOC   | "Victoria", "Australia", "Melbourne"                              |
| MISC  | "Ley", "Ciudad", "CrimeNet"                                       |
| ORG   | "Tribunal Supremo", "EFE", "Commonwealth"                         |
| PER   | "Abogado General del Estado", "Daryl Williams", "Abogado General" |

## Evaluation

### Metrics
| Label   | Precision | Recall | F1     |
|:--------|:----------|:-------|:-------|
| **all** | 0.8331    | 0.8074 | 0.8201 |
| LOC     | 0.8471    | 0.7759 | 0.8099 |
| MISC    | 0.7092    | 0.4264 | 0.5326 |
| ORG     | 0.7854    | 0.8558 | 0.8191 |
| PER     | 0.9471    | 0.9329 | 0.9400 |

## Uses

### Direct Use for Inference

```python
from span_marker import SpanMarkerModel

# Download from the 🤗 Hub
model = SpanMarkerModel.from_pretrained("span_marker_model_id")
# Run inference
entities = model.predict("(SV2147) PP: PROBLEMAS INTERNOS PSOE INTERFIEREN EN POLITICA DE LA JUNTA Córdoba (EFE).")
```

### Downstream Use
You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

```python
from span_marker import SpanMarkerModel, Trainer

# Download from the 🤗 Hub
model = SpanMarkerModel.from_pretrained("span_marker_model_id")

# Specify a Dataset with "tokens" and "ner_tag" columns
dataset = load_dataset("conll2003") # For example CoNLL2003

# Initialize a Trainer using the pretrained model & dataset
trainer = Trainer(
    model=model,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
)
trainer.train()
trainer.save_model("span_marker_model_id-finetuned")
```
</details>

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Set Metrics
| Training set          | Min | Median  | Max  |
|:----------------------|:----|:--------|:-----|
| Sentence length       | 0   | 31.8014 | 1238 |
| Entities per sentence | 0   | 2.2583  | 160  |

### Training Hyperparameters
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training Results
| Epoch  | Step | Validation Loss | Validation Precision | Validation Recall | Validation F1 | Validation Accuracy |
|:------:|:----:|:---------------:|:--------------------:|:-----------------:|:-------------:|:-------------------:|
| 0.1164 | 200  | 0.0260          | 0.6907               | 0.5358            | 0.6035        | 0.9264              |
| 0.2328 | 400  | 0.0199          | 0.7567               | 0.6384            | 0.6925        | 0.9414              |
| 0.3491 | 600  | 0.0176          | 0.7773               | 0.7273            | 0.7515        | 0.9563              |
| 0.4655 | 800  | 0.0157          | 0.8066               | 0.7598            | 0.7825        | 0.9601              |
| 0.5819 | 1000 | 0.0158          | 0.8031               | 0.7413            | 0.7710        | 0.9605              |
| 0.6983 | 1200 | 0.0156          | 0.7975               | 0.7598            | 0.7782        | 0.9609              |
| 0.8147 | 1400 | 0.0139          | 0.8210               | 0.7615            | 0.7901        | 0.9625              |
| 0.9310 | 1600 | 0.0129          | 0.8426               | 0.7848            | 0.8127        | 0.9651              |

### Framework Versions
- Python: 3.10.12
- SpanMarker: 1.5.0
- Transformers: 4.38.2
- PyTorch: 2.2.1+cu121
- Datasets: 2.18.0
- Tokenizers: 0.15.2

## Citation

### BibTeX
```
@software{Aarsen_SpanMarker,
    author = {Aarsen, Tom},
    license = {Apache-2.0},
    title = {{SpanMarker for Named Entity Recognition}},
    url = {https://github.com/tomaarsen/SpanMarkerNER}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->