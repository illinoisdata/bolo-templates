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
datasets:
- mozilla-foundation/common_voice_11_0
---
# Whisper-Large for Broad Accent Classification

# Model Description
This model includes the implementation of broader accent classification described in Vox-Profile: A Speech Foundation Model Benchmark for Characterizing Diverse Speaker and Speech Traits (https://arxiv.org/pdf/2505.14648)

The included English accents are: 
<pre>
['British Isles', 'North America', 'Other']
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
from src.model.accent.whisper_accent import WhisperWrapper

# Find device
device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

# Load model from Huggingface
model = WhisperWrapper.from_pretrained("tiantiaf/whisper-large-v3-broad-accent").to(device)
model.eval()
```

## Prediction
```python
# Label List
english_accent_list = [
    'British Isles', 'North America', 'Other'
]
    
# Load data, here just zeros as the example
# Our training data filters output audio shorter than 3 seconds (unreliable predictions) and longer than 15 seconds (computation limitation)
# So you need to prepare your audio to a maximum of 15 seconds, 16kHz and mono channel
max_audio_length = 15 * 16000
data = torch.zeros([1, 16000]).float().to(device)[:, :max_audio_length]
logits, embeddings = model(data, return_feature=True)
    
# Probability and output
accent_prob = F.softmax(logits, dim=1)
print(english_accent_list[torch.argmax(accent_prob).detach().cpu().item()])
```

## If you have any questions, please contact: Tiantian Feng (tiantiaf@usc.edu)

Responsible use of the Model: the Model is released under Open RAIL license, and users should respect the privacy and consent of the data subjects, and adhere to the relevant laws and regulations in their jurisdictions in using our model.

❌ **Out-of-Scope Use**
- Clinical or diagnostic applications
- Surveillance
- Privacy-invasive applications
- No commercial use