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
datasets:
- ajd12342/paraspeechcaps
pipeline_tag: audio-classification
---
# Whisper Large v3 for Voice (Sounding) Quality Classification

# Model Description
This model includes the implementation of voice quality classification described in Vox-Profile: A Speech Foundation Model Benchmark for Characterizing Diverse Speaker and Speech Traits (https://arxiv.org/pdf/2505.14648)

### Metric: 
Specifically, we report speaker-level Macro-F1 scores. Specifically, we randomly sampled five utterances for each speaker and repeated this stratification process 20 times. The speaker-level score is computed as the average Macro-F1 across speakers. **We then report the unweighted average of speaker-level Macro-F1 scores between VoxCeleb and Expresso.**
### Special Note: 
We exclude EARS from ParaSpeechCaps due to its limited number of samples in the holdout set.


The included labels are: 
<pre>
[
    'shrill', 'nasal', 'deep',  # Pitch
    'silky', 'husky', 'raspy', 'guttural', 'vocal-fry', # Texture
    'booming', 'authoritative', 'loud', 'hushed', 'soft', # Volume
    'crisp', 'slurred', 'lisp', 'stammering', # Clarity
    'singsong', 'pitchy', 'flowing', 'monotone', 'staccato', 'punctuated', 'enunciated',  'hesitant', # Rhythm
]
</pre>

- Library: https://github.com/tiantiaf0627/vox-profile-release

# How to use this model

## Download repo
```bash
git clone git@github.com:tiantiaf0627/vox-profile-release.git
```
## Install the package
```bash
conda create -n vox_profile python=3.8
cd vox-profile-release
pip install -e .
```

## Load the model
```python
# Load libraries
import torch
import torch.nn.functional as F
from src.model.voice_quality.whisper_voice_quality import WhisperWrapper
# Find device
device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
# Load model from Huggingface
model = WhisperWrapper.from_pretrained("tiantiaf/whisper-large-v3-voice-quality").to(device)
model.eval()
```

## Prediction
```python
# Label List
voice_quality_label_list = [
    'shrill', 'nasal', 'deep',  # Pitch
    'silky', 'husky', 'raspy', 'guttural', 'vocal-fry', # Texture
    'booming', 'authoritative', 'loud', 'hushed', 'soft', # Volume
    'crisp', 'slurred', 'lisp', 'stammering', # Clarity
    'singsong', 'pitchy', 'flowing', 'monotone', 'staccato', 'punctuated', 'enunciated',  'hesitant', # Rhythm
]
    
# Load data, here just zeros as the example
# Our training data filters output audio shorter than 3 seconds (unreliable predictions) and longer than 15 seconds (computation limitation)
# So you need to prepare your audio to a maximum of 15 seconds, 16kHz and mono channel
max_audio_length = 15 * 16000
data = torch.zeros([1, 16000]).float().to(device)[:, :max_audio_length]
logits = model(
    data, return_feature=False
)
    
# Probability and output
voice_quality_prob = nn.Sigmoid()(torch.tensor(logits))
    
# In practice, a larger threshold would remove some noise, but it is best to aggregate predictions per speaker
voice_label = list()
threshold = 0.7
predictions = (voice_quality_prob > threshold).int().detach().cpu().numpy()[0].tolist()
for label_idx in range(len(predictions)):
    if predictions[label_idx] == 1: voice_label.append(voice_quality_label_list[label_idx])

# print the voice quality labels
print(voice_label)
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

❌ **Out-of-Scope Use**
- Clinical or diagnostic applications
- Surveillance
- Privacy-invasive applications
- No commercial use