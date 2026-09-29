---
license: mit
language:
- pt
base_model:
- distil-whisper/distil-large-v3
pipeline_tag: automatic-speech-recognition
tags:
- asr
- pt
- ptbr
- stt
- speech-to-text
- automatic-speech-recognition
---
# Distil-Whisper-Large-v3 for Brazilian Portuguese

<!-- Provide a quick summary of what the model is/does. -->

This model is a fine-tuned version of distil-whisper-large-v3 for automatic speech recognition (ASR) in Brazilian Portuguese. It was trained using the Common Voice 16 dataset in conjunction with a private dataset transcribed using Whisper Large v3.

### Model Description

<!-- Provide a longer summary of what this model is. -->

The model aims to perform automatic speech transcription in Brazilian Portuguese with high accuracy. By combining data from Common Voice 16 with an automatically transcribed private dataset, the model achieved a Word Error Rate (WER) of 8.221% on the validation set of Common Voice 16.

- **Model type:** Speech recognition model based on distil-whisper-large-v3
- **Language(s) (NLP):** Brazilian Portuguese (pt-BR)
- **License:** MIT
- **Finetuned from model [optional]:** distil-whisper/distil-large-v3

## How to Get Started with the Model

You can use the model with the Transformers library:
from transformers import WhisperForConditionalGeneration, WhisperProcessor

```python   
from datasets import load_dataset
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Load the validation split of the Common Voice dataset for Portuguese
common_voice = load_dataset("mozilla-foundation/common_voice_11_0", "pt", split="validation")

# Load the pretrained model and processor
processor = WhisperProcessor.from_pretrained("freds0/distil-whisper-large-v3-ptbr")
model = WhisperForConditionalGeneration.from_pretrained("freds0/distil-whisper-large-v3-ptbr")

# Select a sample from the dataset
sample = common_voice[0]  # You can change the index to select a different sample

# Get the audio array and sampling rate
audio_input = sample["audio"]["array"]
sampling_rate = sample["audio"]["sampling_rate"]

# Preprocess the audio
input_features = processor(audio_input, sampling_rate=sampling_rate, return_tensors="pt").input_features

# Generate transcription
predicted_ids = model.generate(input_features)
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
print("Transcription:", transcription[0])
```