---
license: cc-by-4.0
datasets:
- Ken-Z/Latin-Audio
language:
- la
base_model:
- microsoft/speecht5_tts
pipeline_tag: automatic-speech-recognition
metrics:
- cer
---
# Whisper Small Latin - Ken
This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Latin language. It achieves a 20 CER (with punctuations) with the 67 hours of audio from [Vox Classica](https://huggingface.co/datasets/Ken-Z/Latin-Audio)

Try this model directly in your browser: [ASR Demo](https://huggingface.co/spaces/ken-z/latin_whisper-small-demo)