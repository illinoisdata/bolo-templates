---
language:
- en
thumbnail: null
tags:
- audio-classification
- speechbrain
- embeddings
- Accent Identification
- pytorch
- wav2vec2
- XLSR
- CommonAccent
- English
license: mit
datasets:
- CommonVoice
metrics:
- Accuracy
widget:
- example_title: USA
  src: >-
    https://huggingface.co/Jzuluaga/accent-id-commonaccent_xlsr-en-english/resolve/main/data/us_1.wav
- example_title: Scotland
  src: >-
    https://huggingface.co/Jzuluaga/accent-id-commonaccent_xlsr-en-english/resolve/main/data/scotland_1.wav
- example_title: Malaysia
  src: >-
    https://huggingface.co/Jzuluaga/accent-id-commonaccent_xlsr-en-english/resolve/main/data/malaysia_1.wav
- example_title: Philippines
  src: >-
    https://huggingface.co/Jzuluaga/accent-id-commonaccent_xlsr-en-english/resolve/main/data/philippines_1.wav
---


<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>


# CommonAccent: Exploring Large Acoustic Pretrained Models for Accent Classification Based on CommonVoice

**English Accent Classifier with XLSR model**


**Abstract**: 
Despite the recent advancements in Automatic Speech Recognition (ASR), the recognition of accented speech still remains a dominant problem. In order to create more inclusive ASR systems, research has shown that the integration of accent information, as part of a larger ASR framework, can lead to the mitigation of accented speech errors. We address multilingual accent classification through the ECAPA-TDNN and Wav2Vec 2.0/XLSR architectures which have been proven to perform well on a variety of speech-related downstream tasks. We introduce a simple-to-follow recipe aligned to the SpeechBrain toolkit for accent classification based on Common Voice 7.0 (English) and Common Voice 11.0 (Italian, German, and Spanish). Furthermore, we establish new state-of-the-art for English accent classification with as high as 95% accuracy. We also study the internal categorization of the Wav2Vev 2.0 embeddings through t-SNE, noting that there is a level of clustering based on phonological similarity. 


This repository provides all the necessary tools to perform accent identification from speech recordings with [SpeechBrain](https://github.com/speechbrain/speechbrain).
The system uses a model pretrained on the CommonAccent dataset in English (16 accents). This system is based on the CommonLanguage Recipe located here: https://github.com/speechbrain/speechbrain/tree/develop/recipes/CommonLanguage


The provided system can recognize the following 16 accents from short speech recordings in English (EN):

```
- us
- england
- australia
- indian
- canada
- bermuda
- scotland
- african
- ireland
- newzealand
- wales
- malaysia
- philippines
- singapore
- hongkong
- southatlandtic
```

<a href="https://github.com/JuanPZuluaga/accent-recog-slt2022"> <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Open%20source-green"> </a> Github repository link: https://github.com/JuanPZuluaga/accent-recog-slt2022


**NOTE**: due to incompatibility with the model and the current SpeechBrain interfaces, we cannot offer the Inference API. Please, follow the steps in **"Perform Accent Identification from Speech Recordings"** to use this Italian Accent ID model.

For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). 


## Pipeline description
This system is composed of a fine-tuned XLSR model coupled with statistical pooling. A classifier, trained with NLL Loss, is applied on top of that.

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *classify_file* if needed. Make sure your input tensor is compliant with the expected sampling rate if you use *encode_batch* and *classify_batch*.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Perform Accent Identification from Speech Recordings

```python
import torchaudio
from speechbrain.pretrained.interfaces import foreign_class

classifier = foreign_class(source="Jzuluaga/accent-id-commonaccent_xlsr-en-english", pymodule_file="custom_interface.py", classname="CustomEncoderWav2vec2Classifier")

# US Accent Example
out_prob, score, index, text_lab = classifier.classify_file('Jzuluaga/accent-id-commonaccent_xlsr-en-english/data/us.wav')
print(text_lab)

# Philippines Example
out_prob, score, index, text_lab = classifier.classify_file('Jzuluaga/accent-id-commonaccent_xlsr-en-english/data/philippines.wav')
print(text_lab)
```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training

The model was trained with SpeechBrain.

To train it from scratch follow these steps:

1. Clone SpeechBrain:
```bash
git clone https://github.com/speechbrain/speechbrain/
```

2. Install it:
```bash
cd speechbrain
pip install -r requirements.txt
pip install -e .
```

3. Clone our repository in https://github.com/JuanPZuluaga/accent-recog-slt2022:

```bash
git clone https://github.com/JuanPZuluaga/accent-recog-slt2022
cd CommonAccent/accent_id
python train_w2v2.py hparams/train_w2v2.yaml
```

You can find our training results (models, logs, etc) in this repository's `Files and versions` page.

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.



#### Cite our work: CommonAccent

If you find useful this work, please cite our work as: 

```
@article{zuluaga2023commonaccent,
  title={CommonAccent: Exploring Large Acoustic Pretrained Models for Accent Classification Based on Common Voice},
  author={Zuluaga-Gomez, Juan and Ahmed, Sara and Visockas, Danielius and Subakan, Cem},
  journal={Interspeech 2023},
  url={https://arxiv.org/abs/2305.18283},
  year={2023}
}
```

#### Cite XLSR model

```@article{conneau2020unsupervised,
  title={Unsupervised cross-lingual representation learning for speech recognition},
  author={Conneau, Alexis and Baevski, Alexei and Collobert, Ronan and Mohamed, Abdelrahman and Auli, Michael},
  journal={arXiv preprint arXiv:2006.13979},
  year={2020}
}
```


# **Cite SpeechBrain**
Please, cite SpeechBrain if you use it for your research or business.


```bibtex
@misc{speechbrain,
  title={{SpeechBrain}: A General-Purpose Speech Toolkit},
  author={Mirco Ravanelli and Titouan Parcollet and Peter Plantinga and Aku Rouhe and Samuele Cornell and Loren Lugosch and Cem Subakan and Nauman Dawalatabad and Abdelwahab Heba and Jianyuan Zhong and Ju-Chieh Chou and Sung-Lin Yeh and Szu-Wei Fu and Chien-Feng Liao and Elena Rastorgueva and François Grondin and William Aris and Hwidong Na and Yan Gao and Renato De Mori and Yoshua Bengio},
  year={2021},
  eprint={2106.04624},
  archivePrefix={arXiv},
  primaryClass={eess.AS},
  note={arXiv:2106.04624}
}
```