---
language: "en"
thumbnail:
tags:
- speechbrain
- embeddings
- Speaker
- Verification
- Identification
- pytorch
- ResNet
- TDNN
license: "apache-2.0"
datasets:
- voxceleb
metrics:
- EER
widget:
- example_title: VoxCeleb Speaker id10003
  src: https://cdn-media.huggingface.co/speech_samples/VoxCeleb1_00003.wav
- example_title: VoxCeleb Speaker id10004
  src: https://cdn-media.huggingface.co/speech_samples/VoxCeleb_00004.wav
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Speaker Verification with ResNet embeddings on Voxceleb

This repository provides all the necessary tools to perform speaker verification with a pretrained ResNet TDNN model using SpeechBrain. 
The system can be used to extract speaker embeddings as well. 
It is trained on Voxceleb 1 + Voxceleb2 training data. 

For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The model performance on Voxceleb1-test set(Cleaned) is:

| Release | EER(%) | minDCF | 
|:-------------:|:--------------:|:--------------:|
| 29-07-23 | 1.05 | 0.1082 | 


## Pipeline description

This system is composed of an ResNet TDNN model. The system is trained with Additive Margin Softmax Loss.  Speaker Verification is performed using cosine distance between speaker embeddings.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Compute your speaker embeddings

```python
import torchaudio
from speechbrain.inference.speaker import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-resnet-voxceleb")
signal, fs =torchaudio.load('example.wav')
embeddings = classifier.encode_batch(signal)
```

### Perform Speaker Verification

```python
from speechbrain.inference.speaker import SpeakerRecognition
verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-resnet-voxceleb", savedir="pretrained_models/spkrec-resnet-voxceleb")
score, prediction = verification.verify_files("speechbrain/spkrec-resnet-voxceleb/example1.wav", "speechbrain/spkrec-resnet-voxceleb/example2.flac")
```
 The prediction is 1 if the two signals in input are from the same speaker and 0 otherwise.

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain (aa018540).
To train it from scratch follows these steps:
1. Clone SpeechBrain:
```bash
git clone https://github.com/speechbrain/speechbrain/
```
2. Install it:
```
cd speechbrain
pip install -r requirements.txt
pip install -e .
```

3. Run Training:
```
cd  recipes/VoxCeleb/SpeakerRec
python train_speaker_embeddings.py hparams/train_resnet.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1-ahC1xeyPinAHp2oAohL-02smNWO41Cc?usp=sharing).

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

#### Referencing ResNet TDNN
```
@article{VILLALBA2020101026,
title = {State-of-the-art speaker recognition with neural network embeddings in NIST SRE18 and Speakers in the Wild evaluations},
journal = {Computer Speech & Language},
volume = {60},
pages = {101026},
year = {2020},
doi = {https://doi.org/10.1016/j.csl.2019.101026},
author = {Jesús Villalba and Nanxin Chen and David Snyder and Daniel Garcia-Romero and Alan McCree and Gregory Sell and Jonas Borgstrom and Leibny Paola García-Perera and Fred Richardson and Réda Dehak and Pedro A. Torres-Carrasquillo and Najim Dehak},
}
```

# **Citing SpeechBrain**
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

# **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/