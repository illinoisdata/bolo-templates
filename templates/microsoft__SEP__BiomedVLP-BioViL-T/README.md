---
language: en
tags:
- exbert
license: mit
widget:
- text: "Left pleural effusion with adjacent [MASK]."
  example_title: "Radiology 1"
- text: "Heart size normal and lungs are [MASK]."
  example_title: "Radiology 2"
- text: "[MASK] is a tumor suppressor gene."
  example_title: "Biomedical"
- text: "The patient was on [MASK] for chronic atrial fibrillation"
  example_title: "Medication"
---

# BioViL-T

 [BioViL-T](https://arxiv.org/abs/2301.04558) is a domain-specific vision-language model designed to analyze chest X-rays (CXRs) and radiology reports. It was trained using a temporal multi-modal pre-training procedure, which distinguishes it from its predecessor model ([BioViL](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960001.pdf)). In detail, BioViL-T takes advantage of the temporal structure between data points, resulting in improved downstream performance on multiple benchmarks, while using the same training dataset as its predecessor. In particular, the resultant model displays significant improvement in embedding temporal information present in the image and text modalities (see [results](#performance)), as well as in the joint space. The canonical model can be adapted to both single- and multi-image downstream applications including: natural language inference, phrase-grounding, image/text classification, and language decoding. 

The corresponding BERT language model is trained in two stages: First, we pretrain [CXR-BERT-general](https://huggingface.co/microsoft/BiomedVLP-CXR-BERT-general) from a randomly initialized BERT model via Masked Language Modeling (MLM) on [PubMed](https://pubmed.ncbi.nlm.nih.gov/) abstracts and clinical notes from the publicly-available [MIMIC-III](https://physionet.org/content/mimiciii/1.4/) and [MIMIC-CXR](https://physionet.org/content/mimic-cxr/). The general model can be fine-tuned for research in other clinical domains by adjusting the parameters specific to the target domain. In the second stage, BioViL-T is continually pretrained from CXR-BERT-general using a multi-modal pre-training procedure by utilising radiology reports and sequences of chest X-rays. We utilise the latent representation of [CLS] token to align text and image embeddings.


## Language model variations

| Model                                             | Model identifier on HuggingFace                                                                             | Vocabulary     | Note                                                      |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------- |
| CXR-BERT-general                                  | [microsoft/BiomedVLP-CXR-BERT-general](https://huggingface.co/microsoft/BiomedVLP-CXR-BERT-general)       | PubMed & MIMIC | Pretrained for biomedical literature and clinical domains |
| CXR-BERT-specialized        | [microsoft/BiomedVLP-CXR-BERT-specialized](https://huggingface.co/microsoft/BiomedVLP-CXR-BERT-specialized) | PubMed & MIMIC | Static pretraining for the CXR domain                         |
| BioViL-T | [microsoft/BiomedVLP-BioViL-T](https://huggingface.co/microsoft/BiomedVLP-BioViL-T) | PubMed & MIMIC |  Static & temporal pretraining for the CXR domain

## Image model
The image model is jointly trained with the text model in a multi-modal contrastive learning framework. It's a hybrid image encoder composed of a Vision Transformer and ResNet-50, where the latter is used as backbone network to extract features from images at each time point. The transformer is included in the design to aggregate and compare image features extracted across the temporal dimension. The corresponding model definition and its loading functions can be accessed through our [HI-ML-Multimodal](https://github.com/microsoft/hi-ml/blob/main/hi-ml-multimodal/src/health_multimodal/image/model/model.py) GitHub repository. The joint image and text model, namely [BioViL-T](https://arxiv.org/abs/2204.09817), can be used in phrase grounding applications as shown in this python notebook [example](https://mybinder.org/v2/gh/microsoft/hi-ml/HEAD?labpath=hi-ml-multimodal%2Fnotebooks%2Fphrase_grounding.ipynb). Additionally, please check the [MS-CXR benchmark](https://physionet.org/content/ms-cxr/0.1/) for a more systematic evaluation of joint image and text models in phrase grounding tasks.

## Citation

The corresponding manuscript is accepted to be presented at the [**Conference on Computer Vision and Pattern Recognition (CVPR) 2023**](https://cvpr2023.thecvf.com/)

```bibtex
@misc{https://doi.org/10.48550/arXiv.2301.04558,
  doi = {10.48550/ARXIV.2301.04558},
  url = {https://arxiv.org/abs/2301.04558},
  author = {Bannur, Shruthi and Hyland, Stephanie and Liu, Qianchu and Perez-Garcia, Fernando and Ilse, Maximilian and Castro, Daniel C and Boecking, Benedikt and Sharma, Harshita and Bouzid, Kenza and Thieme, Anja and Schwaighofer, Anton and Wetscherek, Maria and Lungren, Matthew P and Nori, Aditya and Alvarez-Valle, Javier and Oktay, Ozan}
  title = {Learning to Exploit Temporal Structure for Biomedical Vision–Language Processing},
  publisher = {arXiv},
  year = {2023},
}
```

## Model Use

### Intended Use

This model is intended to be used solely for (I) future research on visual-language processing and (II) reproducibility of the experimental results reported in the reference paper.

#### Primary Intended Use

The primary intended use is to support AI researchers building on top of this work. CXR-BERT and its associated models should be helpful for exploring various clinical NLP & VLP research questions, especially in the radiology domain.

#### Out-of-Scope Use

**Any** deployed use case of the model --- commercial or otherwise --- is currently out of scope. Although we evaluated the models using a broad set of publicly-available research benchmarks, the models and evaluations are not intended for deployed use cases. Under unprecedented conditions, the models may make inaccurate predictions and display limitations, which may require additional mitigation strategies. Therefore, we discourage use of the model for automated diagnosis or in a medical device. Please refer to [the associated paper](https://arxiv.org/abs/2301.04558) for more details.

### How to use

Here is how to use this model to extract radiological sentence embeddings and obtain their cosine similarity in the joint space (image and text):

```python
import torch
from transformers import AutoModel, AutoTokenizer

# Load the model and tokenizer
url = "microsoft/BiomedVLP-BioViL-T"
tokenizer = AutoTokenizer.from_pretrained(url, trust_remote_code=True)
model = AutoModel.from_pretrained(url, trust_remote_code=True)

# Input text prompts describing findings.
# The order of prompts is adjusted to capture the spectrum from absence of a finding to its temporal progression.
text_prompts = ["No pleural effusion or pneumothorax is seen.",
                "There is no pneumothorax or pleural effusion.",
                "The extent of the pleural effusion is reduced.",
                "The extent of the pleural effusion remains constant.",
                "Interval enlargement of pleural effusion."]

# Tokenize and compute the sentence embeddings
with torch.no_grad():
    tokenizer_output = tokenizer.batch_encode_plus(batch_text_or_text_pairs=text_prompts,
                                                   add_special_tokens=True,
                                                   padding='longest',
                                                   return_tensors='pt')
    embeddings = model.get_projected_text_embeddings(input_ids=tokenizer_output.input_ids,
                                                 attention_mask=tokenizer_output.attention_mask)

    # Compute the cosine similarity of sentence embeddings obtained from input text prompts.
    sim = torch.mm(embeddings, embeddings.t())
```

## Data

This model builds upon existing publicly-available datasets:

- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- [MIMIC-III](https://physionet.org/content/mimiciii/)
- [MIMIC-CXR](https://physionet.org/content/mimic-cxr/)

These datasets reflect a broad variety of sources ranging from biomedical abstracts to intensive care unit notes to chest X-ray radiology notes. The radiology notes are accompanied with their associated chest x-ray DICOM images in MIMIC-CXR dataset.  

## Performance

The presented model achieves state-of-the-art results in radiology natural language inference by leveraging semantics and discourse characteristics at training time more efficiently.
The experiments were performed on the RadNLI and MS-CXR-T benchmarks, which measure the quality of text embeddings in terms of static and temporal semantics respectively.
BioViL-T is benchmarked against other commonly used SOTA domain specific BERT models, including [PubMedBERT](https://aka.ms/pubmedbert) and [CXR-BERT](https://aka.ms/biovil).
The results below show that BioViL-T has increased sensitivity of sentence embeddings to temporal content (MS-CXR-T) whilst better capturing the static content (RadNLI).

|                                                                                           | MS-CXR-T                          | MS-CXR-T                 | RadNLI (2 classes)   |  RadNLI (2 classes) |
| -----------------------------------------------                                           | :-------------------------------: | :----------------------: | :-------------------------: | :-------------:  |
|                                                                                           | Accuracy                          | ROC-AUC                  | Accuracy             |  ROC-AUC  |
| [PubMedBERT]((https://aka.ms/pubmedbert))                                                 |             60.39                 |        .542              |        81.38                |     .727        |
| [CXR-BERT-General](https://huggingface.co/microsoft/BiomedVLP-CXR-BERT-general)           |             62.60                 |        .601              |        87.59                |     .902        |
| [CXR-BERT-Specialized]((https://huggingface.co/microsoft/BiomedVLP-CXR-BERT-specialized)) |             78.12                 |        .837              |        89.66                |     .932        |
| **BioViL-T**                                                                              |             **87.77**             |        **.933**          |        **90.52**                |     **.947**        |

The novel pretraining framework yields also better vision-language representations. Below is the zero-shot phrase grounding performance obtained on the [MS-CXR](https://physionet.org/content/ms-cxr/0.1/) benchmark dataset, which evaluates the quality of image-text latent representations.

| Vision–Language Pretraining Method | MS-CXR Phrase Grounding (Avg. CNR Score) | MS-CXR Phrase Grounding (mIoU) |
| ---------------------------------- | :--------------------------------------: | :----------------------------: | 
| BioViL                             |                  1.07 +- 0.04            |            0.229 +- 0.005      |
| BioViL-L                           |                  1.21 +- 0.05            |            0.202 +- 0.010      |
| **BioViL-T**                       |                **1.33 +- 0.04**          |          **0.240 +- 0.005**    |

Additional experimental results and discussion can be found in the corresponding paper, ["Learning to Exploit Temporal Structure for Biomedical Vision–Language Processing", CVPR'23](https://arxiv.org/abs/2301.04558).


## Limitations

This model was developed using English corpora, and thus can be considered English-only.

The training dataset contains only medical images and reports acquired from an intensive-care-unit (ICU), where longitudinal images are often collected within range of hours or at most few days. As a result, the models may show reduced performance in analyzing consecutive images acquired over longer periods of time (e.g. years) where significant anatomical variations are observed between the scans.

## Further information

Please refer to the corresponding paper, ["Learning to Exploit Temporal Structure for Biomedical Vision–Language Processing", CVPR'23](https://arxiv.org/abs/2301.04558.pdf) for additional details on the model training and evaluation.

For additional inference pipelines with BioViL-T, please refer to the [HI-ML GitHub](https://aka.ms/biovil-t-code) repository. The associated source files will soon be accessible through this link.


