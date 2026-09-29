---
license: apache-2.0
datasets:
- ARTPARK-IISc/Vaani
language:
- hi
base_model:
- openai/whisper-small
pipeline_tag: automatic-speech-recognition
---


# Whisper-large-v3-vaani-hindi

This is a fine-tuned version of [OpenAI's Whisper-Large-V3](https://huggingface.co/openai/whisper-large-v3), trained on approximately 718 hours of transcribed Hindi speech from multiple datasets.

# Usage
This can be used with the pipeline function from the Transformers module.
```python

import torch
from transformers import pipeline

audio = "path to the audio file to be transcribed"
device = "cuda:0" if torch.cuda.is_available() else "cpu"
modelTags="ARTPARK-IISc/whisper-large-v3-vaani-hindi"
transcribe = pipeline(task="automatic-speech-recognition", model=modelTags, chunk_length_s=30, device=device)
transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="hi", task="transcribe")

print('Transcription: ', transcribe(audio)["text"])

```
# Training and Evaluation

The models has finetuned using folllowing dataset [Vaani](https://huggingface.co/datasets/ARTPARK-IISc/Vaani) ,[Gramvaani](https://sites.google.com/view/gramvaaniasrchallenge/dataset)
[IndicVoices](https://huggingface.co/datasets/ai4bharat/IndicVoices), [Fleurs](https://huggingface.co/datasets/google/fleurs),[IndicTTS](https://huggingface.co/datasets/SPRINGLab/IndicTTS-Hindi)
and [Commonvoice](https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0)


The performance of the model was evaluated using multiple datasets, and the evaluation results are provided below.

| Dataset | WER | 
| :---:   | :---: | 
| Gramvaani | 25.11   | 
| Fleurs | 11.20  | 
| IndicTTS | 02.86  | 
| MUCS | 14.60   | 
|Commonvoice | 13.84  | 
| Kathbath | 08.85  | 
| Kathbath Noisy| 11.80   | 
| Vaani  | 24.66  | 
| RESPIN  | 07.36 |