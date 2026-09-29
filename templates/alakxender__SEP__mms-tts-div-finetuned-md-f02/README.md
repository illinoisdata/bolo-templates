---
library_name: transformers
datasets:
- alakxender/dv_syn_speech_md
language:
- dv
license: mit
base_model:
- facebook/mms-tts-div
tags:
- dhivehi-tts
---

# Divehi TTS – Female Voice (VITS-based)

This is a fine-tuned VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech) model for Divehi speech synthesis. The model produces female voice audio from Thaana-scripted Divehi text. Fine-tuned from Meta’s MMS-TTS architecture using a curated dataset of synthetic Divehi speech.

## Model Details

| Field                 | Value                                           |
|----------------------|-------------------------------------------------|
| **Model ID**         | `alakxender/mms-tts-div-finetuned-md-f02`       |
| **Base Architecture**| MMS-TTS (VITS)                                  |
| **Language**         | Divehi (dv)                                     |
| **Voice**            | Female                                          |
| **Sampling Rate**    | 16 kHz                                          |
| **Tokenizer**        | VITSTokenizer                                   |
| **Inference Engine** | Transformers (🤗 Hugging Face)                  |


## Usage

```python
from transformers import VitsModel, VitsTokenizer
import torchaudio

tokenizer = VitsTokenizer.from_pretrained("alakxender/mms-tts-div-finetuned-md-f02")
model = VitsModel.from_pretrained("alakxender/mms-tts-div-finetuned-md-f02")

text = "މޫސުން ވަރަށް ގޯސްވެ، ފުވައްމުލަކުން ފެށިގެން އައްޑުއަށް އޮރެންޖް އެލާޓް ނެރެފި"
inputs = tokenizer(text, return_tensors="pt")
waveform = model.generate(**inputs).waveform[0]

torchaudio.save("output.wav", waveform.unsqueeze(0), 16000)
```

## Evaluation Summary

- **Model**: `alakxender/mms-tts-div-finetuned-md-f02`
- **Evaluated Samples**: 3
- **Avg Estimated MOS (UTMOS)**: `2.147`
  ```json
  {
    "5": "Excellent (very natural)",
    "4": "Good (mostly natural)",
    "3": "Fair (some robotic quality)",
    "2": "Poor (noticeably unnatural)",
    "1": "Bad (unintelligible or very synthetic)"
  }
  ```
- **Artifacts**:
  - 🎵 Audio: `outputs/audio/`
  - 📊 Spectrograms: `outputs/spectrograms/`
  - 📄 Report: `outputs/report.txt`
  - 📈 MOS Scores: `outputs/mos_scores.txt`

## Acknowledgements

- [Meta MMS-TTS](https://github.com/facebookresearch/fairseq/tree/main/examples/mms)
- [Tarepan's SpeechMOS](https://github.com/Tarepan/SpeechMOS)
- [Hugging Face 🤗 Transformers](https://huggingface.co/transformers/)