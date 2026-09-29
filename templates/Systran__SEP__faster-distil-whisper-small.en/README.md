---
language:
  - en
tags:
  - audio
  - automatic-speech-recognition
license: mit
library_name: ctranslate2
---

# Whisper small.en model for CTranslate2

This repository contains the conversion of [distil-whisper/distil-small.en](https://huggingface.co/distil-whisper/distil-small.en) to the [CTranslate2](https://github.com/OpenNMT/CTranslate2) model format.

This model can be used in CTranslate2 or projects based on CTranslate2 such as [faster-whisper](https://github.com/systran/faster-whisper).

## Example

```python
from faster_whisper import WhisperModel

model = WhisperModel("distil-small.en")

segments, info = model.transcribe("audio.mp3")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
```

## Conversion details

The original model was converted with the following command:

```
ct2-transformers-converter --model distil-whisper/distil-small.en --output_dir faster-distil-whisper-small.en \
    --copy_files tokenizer.json preprocessor_config.json --quantization float16
```

Note that the model weights are saved in FP16. This type can be changed when the model is loaded using the [`compute_type` option in CTranslate2](https://opennmt.net/CTranslate2/quantization.html).

## More information

**For more information about the original model, see its [model card](https://huggingface.co/distil-whisper/distil-small.en).**