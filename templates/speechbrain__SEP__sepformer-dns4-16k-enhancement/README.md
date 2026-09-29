---
language:
  - "en"
  - "de"
  - "ru"
  - "fr"
  - "it"
  - "es"
thumbnail:
tags:
- audio-to-audio 
- Speech Enhancement
- DNS-4
- SepFormer
- Transformer 
- pytorch
- speechbrain
- Microsoft DNS Challenge
- Deep Noise Suppression Challenge – ICASSP 2022
license: "apache-2.0"
datasets:
- DNS-4
metrics:
- SI-SNR
- PESQ
- SIG
- BAK
- OVRL
model-index:
- name: sepformer-dns4-16k-enhancement
  results:
  - task:
      name: Speech Enhancement
      type: speech-enhancement
    dataset:
      name: DNS-4
      type: deep-noise-suppression-challenge-icassp-2022
      split: baseline-dev-set
      args:
        language: de
    metrics:
    - name: DNSMOS SIG
      type: sig
      value: '2.999'
    - name: DNSMOS BAK
      type: bak
      value: '3.076'
    - name: DNSMOS OVRL
      type: ovrl
      value: '2.437'
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# SepFormer trained on Microsoft DNS-4 (Deep Noise Suppression Challenge 4 – ICASSP 2022) for speech enhancement (16k sampling frequency)
This repository provides all the necessary tools to perform speech enhancement (denoising) with a [SepFormer](https://arxiv.org/abs/2010.13154v2) model, implemented with SpeechBrain. The model is trained on 1300HRS of Microsoft-DNS 4 dataset with 16k sampling frequency. For a better experience we encourage you to learn more about [SpeechBrain](https://speechbrain.github.io). Evaluation on DNS4 2022 baseline dev set using DNSMOS are-


| Release | SIG | BAK | OVRL |
|:-------------:|:--------------:|:--------------:|:--------------:|
| 08-01-23 | 2.999 | 3.076 | 2.437 |

DNSMOS - deep noise suppression (DNS)- mean opinion score (MOS) is a non-intrusive evaluation metric. It computes 3 scores– SIG (speech quality), BAK (background noise quality), and OVRL (overall quality) each on a scale of 1 to 5, with 5 being the best quality.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about [SpeechBrain](https://speechbrain.github.io).

### Perform speech enhancement on your own audio file

```python
from speechbrain.inference.separation import SepformerSeparation as separator
import torchaudio

model = separator.from_hparams(source="speechbrain/sepformer-dns4-16k-enhancement", savedir='pretrained_models/sepformer-dns4-16k-enhancement')

# for custom file, change path
est_sources = model.separate_file(path='speechbrain/sepformer-dns4-16k-enhancement/example_dns4-16k.wav') 

torchaudio.save("enhanced_dns4-16k.wav", est_sources[:, :, 0].detach().cpu(), 16000)

```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

You can find our training results (models, logs, etc) [here](https://www.dropbox.com/sh/02c3wesc65402f6/AAApoxBApft-JwqHK-bddedBa?dl=0).

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

### Referencing SpeechBrain
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

### Referencing SepFormer
```bibtex
@inproceedings{subakan2021attention,
      title={Attention is All You Need in Speech Separation}, 
      author={Cem Subakan and Mirco Ravanelli and Samuele Cornell and Mirko Bronzi and Jianyuan Zhong},
      year={2021},
      booktitle={ICASSP 2021}
}
```

### Referencing ICASSP 2022 Deep Noise Suppression Challenge
```bibtex
@inproceedings{dubey2022icassp,
  title={ICASSP 2022 Deep Noise Suppression Challenge},
  author={Dubey, Harishchandra and Gopal, Vishak and Cutler, Ross and Matusevych, Sergiy and Braun, Sebastian and Eskimez, Emre Sefik and Thakker, Manthan and Yoshioka, Takuya and Gamper, Hannes and Aichner, Robert},
  booktitle={ICASSP},
  year={2022}
}
```


# **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/