---
license: mit
language:
- en
metrics:
- f1
base_model:
- microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
pipeline_tag: token-classification
tags:
- clinical
- MIMIC-III
- Segmentation
---

# Model Details

## Model Description

<!-- Provide a longer summary of what this model is/does. -->
This model is used for sentence segmentation of MIMIC-III notes. It takes the clinical text as input and predict BIO tagging, where B indicates the Beginning of a sentence, I represents Inside of a sentence, and O denotes Outside of a sentence. More details of this model is in the paper [Automatic sentence segmentation of clinical record narratives in real-world data](https://aclanthology.org/2024.emnlp-main.1156/). The smaple code of using this model is at [github](https://github.com/dongfang91/sentence_segmenter/tree/main/baseline) 

Out segmentation model is based on [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext), and we trained on MIMIC-III notes for a sequence labeling (token classification) task.


- **Model type:** token classification model
- **Language(s) (NLP):** en
- **Parent Model:** [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext)
- **Resources for more information:** More information needed
[GitHub Repo](https://github.com/dongfang91/sentence_segmenter/tree/main/baseline)


# Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->
Dongfang Xu, Davy Weissenbacher, Karen O’Connor, Siddharth Rawal, and Graciela Gonzalez Hernandez. 2024. [Automatic sentence segmentation of clinical record narratives in real-world data](https://aclanthology.org/2024.emnlp-main.1156/). In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 20780–20793, Miami, Florida, USA. Association for Computational Linguistics.