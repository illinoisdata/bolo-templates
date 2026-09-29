---
widget:
- text: "The patient complained of pain in the left ventricle region."
- text: "Examination revealed inflammation of the hippocampus."
- text: "The liver showed signs of fatty infiltration."
- text: "An MRI of the cerebrum showed no signs of abnormalities."
- text: "The procedure involved an incision near the femoral artery."
tags:
- token-classification
- entity recognition
- named-entity-recognition
- zero-shot
- zero-shot-ner
- zero shot
- biomedical-nlp
- gliner
- anatomical-entity-recognition
- medical-terminology
- anatomy
- healthcare
- anatomy
- body_part
- organ
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-ZeroShot-NER-Anatomy-Medium-209M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Anatomy-Medium-209M)

**Specialized model for Anatomical Entity Recognition - Anatomical structures and body parts**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)]()
[![GliNER](https://img.shields.io/badge/🤗-GliNER-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

Tailored to **anatomical structure recognition**, including organs, tissues, and substructures in clinical narratives.Supports **radiology and surgical note parsing**, **site-of-disease extraction**, and **anatomy-aware analytics**.

OpenMed ZeroShot NER is an advanced, domain-adapted Named Entity Recognition (NER) model designed specifically for medical, biomedical, and clinical text mining. Leveraging state-of-the-art zero-shot learning, this model empowers researchers, clinicians, and data scientists to extract expert-level biomedical entities—such as diseases, chemicals, genes, species, and clinical findings—directly from unstructured text, without the need for task-specific retraining.

Built on the robust GLiNER architecture and fine-tuned on curated biomedical corpora, OpenMed ZeroShot NER delivers high-precision entity recognition for critical healthcare and life sciences applications. Its zero-shot capability means you can flexibly define and extract any entity type relevant to your workflow, from standard biomedical categories to custom clinical concepts, supporting rapid adaptation to new research domains and regulatory requirements.

Whether you are working on clinical NLP, biomedical research, electronic health record (EHR) de-identification, or large-scale literature mining, OpenMed ZeroShot NER provides a production-ready, open-source solution that combines expert-level accuracy with unmatched flexibility. Join the OpenMed community to accelerate your medical text analytics with cutting-edge, zero-shot NER technology.

### 🎯 Key Features
- **Zero-Shot Capability**: Can recognize any entity type without specific training
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Fine-tuned on curated ANATOMY dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem
- **Flexible Entity Recognition**: Add custom entity types without retraining

### 🏷️ Supported Entity Types

This zero-shot model can identify and classify biomedical entities, including but not limited to these entity types. **You can also add custom entity types without retraining the model**:

- `Anatomy`

**💡 Zero-Shot Flexibility**: As a GliNER-based model, you can specify any entity types you want to detect, even if they weren't part of the original training. Simply provide the entity labels when using the model, and it will adapt to recognize them.

## 📊 Dataset

Anatomy corpus focuses on anatomical entity recognition for medical terminology and healthcare applications.

The Anatomy corpus is a specialized biomedical NER dataset designed for recognizing anatomical entities and medical terminology in clinical and biomedical texts. This corpus contains annotations for anatomical structures, body parts, organs, and physiological systems mentioned in medical literature. It is essential for developing clinical NLP systems, medical education tools, and healthcare informatics applications where accurate anatomical entity identification is crucial. The dataset supports the development of automated systems for medical coding, clinical decision support, and anatomical knowledge extraction from medical records and literature. It serves as a valuable resource for training NER models used in medical imaging, surgical planning, and clinical documentation.


## 📊 Performance Metrics

### Current Model Performance

- **Finetuned F1 vs. Base Model (on test dataset excluded from training)**: `0.91`
- **F1 Improvement vs Base Model**: `187.3%`

### 🏆 Top F1 Improvements on ANATOMY Dataset

| Rank | Model | Base F1 | Finetuned F1 | ΔF1 | ΔF1 % |
|------|-------|--------:|------------:|----:|------:|
| 🥇 1 | [OpenMed-ZeroShot-NER-Anatomy-Large-459M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Anatomy-Large-459M) | 0.2978 | 0.9271 | 0.6293 | 211.3% |
| 🥈 2 | [OpenMed-ZeroShot-NER-Anatomy-Medium-209M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Anatomy-Medium-209M) | 0.3172 | 0.9114 | 0.5942 | 187.3% |
| 🥉 3 | [OpenMed-ZeroShot-NER-Anatomy-XLarge-770M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Anatomy-XLarge-770M) | 0.3780 | 0.9021 | 0.5241 | 138.7% |
|  4 | [OpenMed-ZeroShot-NER-Anatomy-Base-220M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Anatomy-Base-220M) | 0.2804 | 0.8627 | 0.5823 | 207.7% |
|  5 | [OpenMed-ZeroShot-NER-Anatomy-Multi-209M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Anatomy-Multi-209M) | 0.3121 | 0.8091 | 0.4969 | 159.2% |


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
# Model: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Anatomy-Medium-209M
model_name = "OpenMed/OpenMed-ZeroShot-NER-Anatomy-Medium-209M"

from gliner import GLiNER
model = GLiNER.from_pretrained(model_name)

# Example usage with default entity types
text = "The patient complained of pain in the left ventricle region."

labels = ['Anatomy']
entities = model.predict_entities(text, labels, flat_ner=True, threshold=0.5)
for entity in entities:
    print(entity)
```

### Zero-Shot Usage with Custom Entity Types
💡 **Tip:** If you want to extract entities that are not present in the original training set (i.e., use custom or rare entity types), you may get better results by lowering the `threshold` parameter in `model.predict_entities`. For example, try `threshold=0.3` or even lower, depending on your use case:

```python
# You can specify custom entity types for zero-shot recognition - for instance:
custom_entities = ["MISC", "Anatomy", "PERSON", "LOCATION", "MEDICATION", "PROCEDURE"]

entities = model.predict_entities(text, custom_entities, flat_ner=True, threshold=0.1)
for entity in entities:
    print(entity)
```

> Lowering the threshold makes the model more permissive and can help it recognize new or less common entity types, but may also increase false positives. Adjust as needed for your application.

## 📚 Dataset Information

- **Dataset**: ANATOMY
- **Description**: Anatomical Entity Recognition - Anatomical structures and body parts

### Training Details
- **Base Model**: gliner_medium-v2.1
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