---
datasets:
- davidrrobinson/AnimalSpeak
---

# Model card for BioLingual

Model card for BioLingual: Transferable Models for bioacoustics with Human Language Supervision

An audio-text model for bioacoustics based on contrastive language-audio pretraining.

# Usage

You can use this model for bioacoustic zero shot audio classification, or for fine-tuning on bioacoustic tasks.

# Uses

## Perform zero-shot audio classification

### Using `pipeline`

```python
from datasets import load_dataset
from transformers import pipeline

dataset = load_dataset("ashraq/esc50")
audio = dataset["train"]["audio"][-1]["array"]

audio_classifier = pipeline(task="zero-shot-audio-classification", model="davidrrobinson/BioLingual")
output = audio_classifier(audio, candidate_labels=["Sound of a sperm whale", "Sound of a sea lion"])
print(output)
>>> [{"score": 0.999, "label": "Sound of a dog"}, {"score": 0.001, "label": "Sound of vaccum cleaner"}]
```

## Run the model:

You can also get the audio and text embeddings using `ClapModel`

### Run the model on CPU:

```python
from datasets import load_dataset
from transformers import ClapModel, ClapProcessor

librispeech_dummy = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio_sample = librispeech_dummy[0]

model = ClapModel.from_pretrained("laion/clap-htsat-unfused")
processor = ClapProcessor.from_pretrained("laion/clap-htsat-unfused")

inputs = processor(audios=audio_sample["audio"]["array"], return_tensors="pt")
audio_embed = model.get_audio_features(**inputs)
```

### Run the model on GPU:

```python
from datasets import load_dataset
from transformers import ClapModel, ClapProcessor

librispeech_dummy = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio_sample = librispeech_dummy[0]

model = ClapModel.from_pretrained("laion/clap-htsat-unfused").to(0)
processor = ClapProcessor.from_pretrained("laion/clap-htsat-unfused")

inputs = processor(audios=audio_sample["audio"]["array"], return_tensors="pt").to(0)
audio_embed = model.get_audio_features(**inputs)