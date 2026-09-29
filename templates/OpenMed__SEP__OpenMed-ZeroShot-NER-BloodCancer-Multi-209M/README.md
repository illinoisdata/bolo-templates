---
widget:
- text: "The patient presented with chronic lymphocytic leukemia symptoms."
- text: "B-cell proliferation was observed in bone marrow samples."
- text: "Treatment with ibrutinib showed promising results."
- text: "Flow cytometry confirmed the diagnosis of chronic lymphocytic leukemia."
- text: "The patient had del(17p), a high-risk feature in CLL."
tags:
- token-classification
- entity recognition
- named-entity-recognition
- zero-shot
- zero-shot-ner
- zero shot
- biomedical-nlp
- gliner
- leukemia
- hematology
- cancer
- clinical-medicine
- disease
- gene
- protein
- treatment
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-ZeroShot-NER-BloodCancer-Multi-209M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-BloodCancer-Multi-209M)

**Specialized model for Clinical Entity Recognition - Clinical entities related to Chronic Lymphocytic Leukemia**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)]()
[![GliNER](https://img.shields.io/badge/🤗-GliNER-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

Domain-tuned for **Chronic Lymphocytic Leukemia (CLL)** terminology, capturing disease descriptors, biomarkers, and therapies.Supports **hematology research**, **treatment response analysis**, and **clinical evidence tracking**.

OpenMed ZeroShot NER is an advanced, domain-adapted Named Entity Recognition (NER) model designed specifically for medical, biomedical, and clinical text mining. Leveraging state-of-the-art zero-shot learning, this model empowers researchers, clinicians, and data scientists to extract expert-level biomedical entities—such as diseases, chemicals, genes, species, and clinical findings—directly from unstructured text, without the need for task-specific retraining.

Built on the robust GLiNER architecture and fine-tuned on curated biomedical corpora, OpenMed ZeroShot NER delivers high-precision entity recognition for critical healthcare and life sciences applications. Its zero-shot capability means you can flexibly define and extract any entity type relevant to your workflow, from standard biomedical categories to custom clinical concepts, supporting rapid adaptation to new research domains and regulatory requirements.

Whether you are working on clinical NLP, biomedical research, electronic health record (EHR) de-identification, or large-scale literature mining, OpenMed ZeroShot NER provides a production-ready, open-source solution that combines expert-level accuracy with unmatched flexibility. Join the OpenMed community to accelerate your medical text analytics with cutting-edge, zero-shot NER technology.

### 🎯 Key Features
- **Zero-Shot Capability**: Can recognize any entity type without specific training
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Fine-tuned on curated CLL dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem
- **Flexible Entity Recognition**: Add custom entity types without retraining

### 🏷️ Supported Entity Types

This zero-shot model can identify and classify biomedical entities, including but not limited to these entity types. **You can also add custom entity types without retraining the model**:

- `CL`

**💡 Zero-Shot Flexibility**: As a GliNER-based model, you can specify any entity types you want to detect, even if they weren't part of the original training. Simply provide the entity labels when using the model, and it will adapt to recognize them.

## 📊 Dataset

CLL corpus is specialized for chronic lymphocytic leukemia entity recognition in hematology and cancer research.

The CLL (Chronic Lymphocytic Leukemia) corpus is a domain-specific biomedical NER dataset focused on entities related to chronic lymphocytic leukemia, a type of blood cancer. This specialized corpus contains annotations for CLL-specific terminology, biomarkers, treatment entities, and clinical concepts relevant to hematology and oncology research. The dataset is designed to support the development of clinical NLP systems for leukemia research, hematological disorder analysis, and cancer informatics applications. It is particularly valuable for identifying disease-specific entities, therapeutic interventions, and prognostic factors mentioned in CLL research literature. The corpus serves as a benchmark for evaluating NER models in specialized medical domains and clinical research.


## 📊 Performance Metrics

### Current Model Performance

- **Finetuned F1 vs. Base Model (on test dataset excluded from training)**: `0.60`
- **F1 Improvement vs Base Model**: `31.0%`

### 🏆 Top F1 Improvements on CLL Dataset

| Rank | Model | Base F1 | Finetuned F1 | ΔF1 | ΔF1 % |
|------|-------|--------:|------------:|----:|------:|
| 🥇 1 | [OpenMed-ZeroShot-NER-BloodCancer-Medium-209M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-BloodCancer-Medium-209M) | 0.5068 | 0.9130 | 0.4062 | 80.2% |
| 🥈 2 | [OpenMed-ZeroShot-NER-BloodCancer-XLarge-770M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-BloodCancer-XLarge-770M) | 0.7291 | 0.8750 | 0.1459 | 20.0% |
| 🥉 3 | [OpenMed-ZeroShot-NER-BloodCancer-Large-459M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-BloodCancer-Large-459M) | 0.6009 | 0.7755 | 0.1746 | 29.0% |
|  4 | [OpenMed-ZeroShot-NER-BloodCancer-Small-166M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-BloodCancer-Small-166M) | 0.5505 | 0.6818 | 0.1314 | 23.9% |
|  5 | [OpenMed-ZeroShot-NER-BloodCancer-Tiny-60M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-BloodCancer-Tiny-60M) | 0.5361 | 0.6780 | 0.1419 | 26.5% |


*Rankings are sorted by finetuned F1 and show ΔF1% over base model. Test dataset is excluded from training.*

![OpenMed ZeroShot Clinical & Biomedical NER vs. Original GLiNER models](https://huggingface.co/spaces/OpenMed/README/resolve/main/openmed-zero-shot-clinical-ner-finetuned.png)

*Figure: OpenMed ZeroShot Clinical & Biomedical NER vs. Original GLiNER models.*

## 🚀 Quick Start

### Installation

```bash
pip install -q "gliner[tokenizers]"
```

### Usage

```python
from transformers import pipeline

# Load the model and tokenizer
# Model: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-BloodCancer-Multi-209M
model_name = "OpenMed/OpenMed-ZeroShot-NER-BloodCancer-Multi-209M"

from gliner import GLiNER
model = GLiNER.from_pretrained(model_name)

# Example usage with default entity types
text = "The patient presented with chronic lymphocytic leukemia symptoms."

labels = ['CL']
entities = model.predict_entities(text, labels, flat_ner=True, threshold=0.5)
for entity in entities:
    print(entity)
```

### Zero-Shot Usage with Custom Entity Types
💡 **Tip:** If you want to extract entities that are not present in the original training set (i.e., use custom or rare entity types), you may get better results by lowering the `threshold` parameter in `model.predict_entities`. For example, try `threshold=0.3` or even lower, depending on your use case:

```python
# You can specify custom entity types for zero-shot recognition - for instance:
custom_entities = ["MISC", "CL", "PERSON", "LOCATION", "MEDICATION", "PROCEDURE"]

entities = model.predict_entities(text, custom_entities, flat_ner=True, threshold=0.1)
for entity in entities:
    print(entity)
```

> Lowering the threshold makes the model more permissive and can help it recognize new or less common entity types, but may also increase false positives. Adjust as needed for your application.

## 📚 Dataset Information

- **Dataset**: CLL
- **Description**: Clinical Entity Recognition - Clinical entities related to Chronic Lymphocytic Leukemia

### Training Details
- **Base Model**: gliner_multi-v2.1
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 💡 Use Cases

This model is particularly useful for:
- **Clinical Text Mining**: Extracting entities from medical records
- **Biomedical Research**: Processing scientific literature
- **Drug Discovery**: Identifying chemical compounds and drugs
- **Healthcare Analytics**: Analyzing patient data and outcomes
- **Academic Research**: Supporting biomedical NLP research
- **Custom Entity Recognition**: Zero-shot detection of domain-specific entities

## 🔬 Model Architecture

- **Task**: Zero-Shot Classification (Named Entity Recognition)
- **Labels**: Dataset-specific entity types
- **Input**: Biomedical text
- **Output**: Named entity predictions

## 📜 License

Licensed under the Apache License 2.0. See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) for details.

## 🤝 Contributing

I welcome contributions of all kinds! Whether you have ideas, feature requests, or want to join my mission to advance open-source Healthcare AI, I'd love to hear from you.

Follow [OpenMed Org](https://huggingface.co/OpenMed) on Hugging Face 🤗 and click "Watch" to stay updated on my latest releases and developments.

## Citation

If you use this model in your research or applications, please cite the following paper:

```latex
@misc{panahi2025openmedneropensourcedomainadapted,
      title={OpenMed NER: Open-Source, Domain-Adapted State-of-the-Art Transformers for Biomedical NER Across 12 Public Datasets},
      author={Maziyar Panahi},
      year={2025},
      eprint={2508.01630},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.01630},
}
```

Proper citation helps support and acknowledge my work. Thank you!