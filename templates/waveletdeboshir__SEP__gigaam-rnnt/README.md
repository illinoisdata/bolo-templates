---
license: mit
language:
- ru
pipeline_tag: automatic-speech-recognition
library_name: transformers
tags:
- asr
- gigaam
- stt
- audio
- speech
- rnnt
- transducer
---
[![Finetune In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/waveletdeboshir/351c1915c1a0369e1d45299f6bec4478/gigaam-rnnt-finetune.ipynb)

# GigaAM-v2-RNNT 🤗 Hugging Face transformers

This is an **unofficial Transformers wrapper** for the original GigaAM-v2-RNNT model released by SberDevices.

* original git https://github.com/salute-developers/GigaAM

Russian ASR model GigaAM-v2-RNNT.

## Model info
This is an original GigaAM-v2-RNNT with `transformers` library interface.

File [`gigaam_transformers.py`](https://huggingface.co/waveletdeboshir/gigaam-rnnt/blob/main/gigaam_transformers.py) contains model, feature extractor and tokenizer classes with usual transformers methods. Model can be initialized with transformers auto classes (see an example below).

## Installation

my lib versions:
* `torch` 2.7.1
* `torchaudio` 2.7.1
* `transformers` **4.49.0**

## Usage
Usage is same as other `transformers` ASR models.

```python
from transformers import AutoModel, AutoProcessor
import torch
import torchaudio

# load audio
wav, sr = torchaudio.load("audio.wav")
# resample if necessary
wav = torchaudio.functional.resample(wav, sr, 16000)

# load model and processor
processor = AutoProcessor.from_pretrained("waveletdeboshir/gigaam-rnnt", trust_remote_code=True)
model = AutoModel.from_pretrained("waveletdeboshir/gigaam-rnnt", trust_remote_code=True)
model.eval()

input_features = processor(wav[0], sampling_rate=16000, return_tensors="pt")

# greedy prediction
with torch.no_grad():
    pred_ids = model.generate(**input_features)

# decode token ids to text
transcription = processor.batch_decode(pred_ids, group_tokens=False)[0]

```

## Fine-tune
[![Finetune In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/waveletdeboshir/351c1915c1a0369e1d45299f6bec4478/gigaam-rnnt-finetune.ipynb)