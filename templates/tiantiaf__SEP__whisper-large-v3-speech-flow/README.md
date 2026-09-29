---
tags:
- model_hub_mixin
- pytorch_model_hub_mixin
license: openrail
language:
- en
metrics:
- accuracy
base_model:
- openai/whisper-large-v3
pipeline_tag: audio-classification
---
# Whisper Large v3 for Speech Flow (Fluency) Classification

# Model Description
This model includes the implementation of speech fluency classification described in Vox-Profile: A Speech Foundation Model Benchmark for Characterizing Diverse Speaker and Speech Traits (https://arxiv.org/pdf/2505.14648)

The model first predicts the speech with 3-second window size and 1-second step size in 
```
["fluent", "disfluent"]
```
If the disfluent speech is detected, we predict the disfluent types in: 
```
[
  "Block", 
  "Prolongation", 
  "Sound Repetition", 
  "Word Repetition", 
  "Interjection"
]
```

# How to use this model

## Download repo
```
git clone git@github.com:tiantiaf0627/vox-profile-release.git
```
## Install the package
```
conda create -n vox_profile python=3.8
cd vox-profile-release
pip install -e .
```

## Load the model
```python
# Load libraries
import torch
import torch.nn.functional as F
from src.model.fluency.whisper_fluency import WhisperWrapper

# Find device
device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

# Load model from Huggingface
model = WhisperWrapper.from_pretrained("tiantiaf/whisper-large-v3-speech-flow").to(device)
model.eval()
```

## Prediction
```python
audio_data = torch.zeros([1, 16000*10]).float().to(device)
audio_segment = (audio_data.shape[1] - 3*16000) // 16000 + 1
if audio_segment < 1: audio_segment = 1
input_audio = list()
input_audio_length = list()
for idx in range(audio_segment): 
    input_audio.append(audio_data[0, 16000*idx:16000*idx+3*16000])
    input_audio_length.append(torch.tensor(len(audio_data[0, 16000*idx:16000*idx+3*16000])))
input_audio = torch.stack(input_audio, dim=0)
input_audio_length = torch.stack(input_audio_length, dim=0)
```
## Prediction
```python
fluency_outputs, disfluency_type_outputs = model(input_audio, length=input_audio_length)
fluency_prob   = F.softmax(fluency_outputs, dim=1).detach().cpu().numpy().astype(float).tolist()

disfluency_type_prob = nn.Sigmoid()(disfluency_type_outputs)
# we can set a higher threshold in practice
disfluency_type_predictions = (disfluency_type_prob > 0.7).int().detach().cpu().numpy().tolist()
disfluency_type_prob = disfluency_type_prob.cpu().numpy().astype(float).tolist()
```

## Now let's gather the predictions for the utterance
```python
utterance_fluency_list = list()
utterance_disfluency_list = list()
for audio_idx in range(audio_segment):
  disfluency_type = list()
  if fluency_prob[audio_idx][0] > 0.5: 
      utterance_fluency_list.append("fluent")
  else: 
      # If the prediction is disfluent, then which disfluency type
      utterance_fluency_list.append("disfluent")
      predictions = disfluency_type_predictions[audio_idx]
      for label_idx in range(len(predictions)):
          if predictions[label_idx] == 1:
            disfluency_type.append(disfluency_type_labels[label_idx])
  utterance_disfluency_list.append(disfluency_type)

# Now print how fluent is the utterance
print(utterance_fluency_list)
print(utterance_disfluency_list)
```

## If you have any questions, please contact: Tiantian Feng (tiantiaf@usc.edu)

## Kindly cite our paper if you are using our model or find it useful in your work
```
@article{feng2025vox,
  title={Vox-Profile: A Speech Foundation Model Benchmark for Characterizing Diverse Speaker and Speech Traits},
  author={Feng, Tiantian and Lee, Jihwan and Xu, Anfeng and Lee, Yoonjeong and Lertpetchpun, Thanathai and Shi, Xuan and Wang, Helin and Thebaud, Thomas and Moro-Velazquez, Laureano and Byrd, Dani and others},
  journal={arXiv preprint arXiv:2505.14648},
  year={2025}
}
```

Responsible use of the Model: the Model is released under Open RAIL license, and users should respect the privacy and consent of the data subjects, and adhere to the relevant laws and regulations in their jurisdictions in using our model.

❌ **Out-of-Scope Use**
- Clinical or diagnostic applications
- Surveillance
- Privacy-invasive applications
- No commercial use