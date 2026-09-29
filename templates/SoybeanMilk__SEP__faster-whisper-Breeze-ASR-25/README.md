---
language:
- en
- zh
- de
- es
- ru
- ko
- fr
- ja
- pt
- tr
- pl
- ca
- nl
- ar
- sv
- it
- id
- hi
- fi
- vi
- he
- uk
- el
- ms
- cs
- ro
- da
- hu
- ta
- 'no'
- th
- ur
- hr
- bg
- lt
- la
- mi
- ml
- cy
- sk
- te
- fa
- lv
- bn
- sr
- az
- sl
- kn
- et
- mk
- br
- eu
- is
- hy
- ne
- mn
- bs
- kk
- sq
- sw
- gl
- mr
- pa
- si
- km
- sn
- yo
- so
- af
- oc
- ka
- be
- tg
- sd
- gu
- am
- yi
- lo
- uz
- fo
- ht
- ps
- tk
- nn
- mt
- sa
- lb
- my
- bo
- tl
- mg
- as
- tt
- haw
- ln
- ha
- ba
- jw
- su
tags:
- audio
- automatic-speech-recognition
license: apache-2.0
library_name: ctranslate2
base_model:
- MediaTek-Research/Breeze-ASR-25
---

# Breeze-ASR-25 Model for CTranslate2

This repository contains the [MediaTek-Research/Breeze-ASR-25](https://huggingface.co/MediaTek-Research/Breeze-ASR-25) model converted to the [CTranslate2](https://github.com/OpenNMT/CTranslate2) format.

The model can be used with CTranslate2 or CTranslate2-based projects such as [faster-whisper](https://github.com/systran/faster-whisper).

## Example

```python
from faster_whisper import WhisperModel

model = WhisperModel("SoybeanMilk/faster-whisper-Breeze-ASR-25")

segments, info = model.transcribe("audio.wav")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
```

## Conversion Details

The original model was converted with the following command:

```
ct2-transformers-converter \
  --model MediaTek-Research/Breeze-ASR-25 \
  --output_dir faster-whisper-Breeze-ASR-25 \
  --copy_files tokenizer.json preprocessor_config.json \
  --quantization float16
```

Note: The model weights are saved in FP16 format. You can change the type when loading the model using the [`compute_type` option in CTranslate2](https://opennmt.net/CTranslate2/quantization.html).

## More Information

**For more information about the original model, please refer to its [model card](https://huggingface.co/MediaTek-Research/Breeze-ASR-25)**