---
license: mit
datasets:
- mahwizzzz/UAT
language:
- ur
base_model:
- canopylabs/orpheus-3b-0.1-pretrained
pipeline_tag: text-to-speech
---
# Orpheus Urdu (16 bit)
Samle generated audio
<audio controls src="https://cdn-uploads.huggingface.co/production/uploads/62c5a943b4d97e47fd7cfaf7/mP5dWqQfIYdcYOkhARij7.wav"></audio>

## Model Description

The Orpheus Urdu TTS model is a fine-tuned version of the Orpheus 3B text-to-speech model specifically adapted for Urdu language. This experimental model **not recommended for production use** this was trained on the `mahwizzzz/UAT` dataset, which contains 20.4k audio samples split from train. This fine-tuning was performed for 10 epochs on a single RTX 4090.


## Intended Use

This model can be used for generating Urdu speech from text. It is ideal for experimenting with TTS systems for Urdu, particularly for audiobooks, conversational AI, or speech synthesis tasks.

## Model Training

- **Dataset**: `mahwizzzz/UAT` (20.4k audiobook audio samples)
- **Training Epochs**: 10 epochs
- **Hardware**: RTX 4090

  
## Model Usage
```
```