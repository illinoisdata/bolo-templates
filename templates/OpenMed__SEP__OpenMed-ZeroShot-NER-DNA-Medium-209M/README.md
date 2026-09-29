---
widget:
- text: "The p53 protein plays a crucial role in tumor suppression."
- text: "Expression of BRCA1 gene was significantly upregulated in breast tissue."
- text: "The NF-kB pathway regulates inflammatory responses."
- text: "Activation of the STAT3 signaling pathway is observed in many cancers."
- text: "The experiment involved transfecting HeLa cells with a plasmid containing the target gene."
tags:
- token-classification
- entity recognition
- named-entity-recognition
- zero-shot
- zero-shot-ner
- zero shot
- biomedical-nlp
- gliner
- protein-recognition
- gene-recognition
- molecular-biology
- genomics
- protein
- dna
- rna
- cell_line
- cell_type
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-ZeroShot-NER-DNA-Medium-209M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-DNA-Medium-209M)

**Specialized model for Biomedical Entity Recognition - Proteins, DNA, RNA, cell lines, and cell types**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)]()
[![GliNER](https://img.shields.io/badge/🤗-GliNER-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

Targets **molecular biology entities**: proteins, DNA/RNA, cell lines, and cell types in biomedical research content.Great for **pathway curation**, **molecular interaction mining**, and **omics-aware information extraction**.

OpenMed ZeroShot NER is an advanced, domain-adapted Named Entity Recognition (NER) model designed specifically for medical, biomedical, and clinical text mining. Leveraging state-of-the-art zero-shot learning, this model empowers researchers, clinicians, and data scientists to extract expert-level biomedical entities—such as diseases, chemicals, genes, species, and clinical findings—directly from unstructured text, without the need for task-specific retraining.

Built on the robust GLiNER architecture and fine-tuned on curated biomedical corpora, OpenMed ZeroShot NER delivers high-precision entity recognition for critical healthcare and life sciences applications. Its zero-shot capability means you can flexibly define and extract any entity type relevant to your workflow, from standard biomedical categories to custom clinical concepts, supporting rapid adaptation to new research domains and regulatory requirements.

Whether you are working on clinical NLP, biomedical research, electronic health record (EHR) de-identification, or large-scale literature mining, OpenMed ZeroShot NER provides a production-ready, open-source solution that combines expert-level accuracy with unmatched flexibility. Join the OpenMed community to accelerate your medical text analytics with cutting-edge, zero-shot NER technology.

### 🎯 Key Features
- **Zero-Shot Capability**: Can recognize any entity type without specific training
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Fine-tuned on curated JNLPBA dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem
- **Flexible Entity Recognition**: Add custom entity types without retraining

### 🏷️ Supported Entity Types

This zero-shot model can identify and classify biomedical entities, including but not limited to these entity types. **You can also add custom entity types without retraining the model**:

- `DNA`
- `RNA`
- `cell_line`
- `cell_tyle`
- `protein`

**💡 Zero-Shot Flexibility**: As a GliNER-based model, you can specify any entity types you want to detect, even if they weren't part of the original training. Simply provide the entity labels when using the model, and it will adapt to recognize them.

## 📊 Dataset

JNLPBA corpus focuses on biomedical named entity recognition for protein, DNA, RNA, cell line, and cell type entities.

The JNLPBA (Joint Workshop on Natural Language Processing in Biomedicine and its Applications) corpus is a widely-used biomedical NER dataset derived from the GENIA corpus for the 2004 bio-entity recognition task. It contains annotations for five entity types: protein, DNA, RNA, cell line, and cell type, making it essential for molecular biology and genomics research applications. The corpus consists of MEDLINE abstracts annotated with biomedical entities relevant to gene and protein recognition tasks. It has been extensively used as a benchmark for evaluating biomedical NER systems and continues to be a standard evaluation dataset for developing machine learning models in computational biology and bioinformatics.


## 📊 Performance Metrics

### Current Model Performance

- **Finetuned F1 vs. Base Model (on test dataset excluded from training)**: `0.82`
- **F1 Improvement vs Base Model**: `18.5%`

### 🏆 Top F1 Improvements on JNLPBA Dataset

| Rank | Model | Base F1 | Finetuned F1 | ΔF1 | ΔF1 % |
|------|-------|--------:|------------:|----:|------:|
| 🥇 1 | [OpenMed-ZeroShot-NER-DNA-Large-459M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-DNA-Large-459M) | 0.7006 | 0.8220 | 0.1214 | 17.3% |
| 🥈 2 | [OpenMed-ZeroShot-NER-DNA-Medium-209M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-DNA-Medium-209M) | 0.6928 | 0.8208 | 0.1280 | 18.5% |
| 🥉 3 | [OpenMed-ZeroShot-NER-DNA-XLarge-770M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-DNA-XLarge-770M) | 0.5271 | 0.8106 | 0.2835 | 53.8% |
|  4 | [OpenMed-ZeroShot-NER-DNA-Base-220M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-DNA-Base-220M) | 0.4896 | 0.7907 | 0.3011 | 61.5% |
|  5 | [OpenMed-ZeroShot-NER-DNA-Multi-209M](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-DNA-Multi-209M) | 0.6660 | 0.7750 | 0.1090 | 16.4% |


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
# Model: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-DNA-Medium-209M
model_name = "OpenMed/OpenMed-ZeroShot-NER-DNA-Medium-209M"

from gliner import GLiNER
model = GLiNER.from_pretrained(model_name)

# Example usage with default entity types
text = "The p53 protein plays a crucial role in tumor suppression."

labels = ['DNA', 'RNA', 'cell_line', 'cell_tyle', 'protein']
entities = model.predict_entities(text, labels, flat_ner=True, threshold=0.5)
for entity in entities:
    print(entity)
```

### Zero-Shot Usage with Custom Entity Types
💡 **Tip:** If you want to extract entities that are not present in the original training set (i.e., use custom or rare entity types), you may get better results by lowering the `threshold` parameter in `model.predict_entities`. For example, try `threshold=0.3` or even lower, depending on your use case:

```python
# You can specify custom entity types for zero-shot recognition - for instance:
custom_entities = ["MISC", "DNA", "PERSON", "LOCATION", "MEDICATION", "PROCEDURE"]

entities = model.predict_entities(text, custom_entities, flat_ner=True, threshold=0.1)
for entity in entities:
    print(entity)
```

> Lowering the threshold makes the model more permissive and can help it recognize new or less common entity types, but may also increase false positives. Adjust as needed for your application.

## 📚 Dataset Information

- **Dataset**: JNLPBA
- **Description**: Biomedical Entity Recognition - Proteins, DNA, RNA, cell lines, and cell types

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