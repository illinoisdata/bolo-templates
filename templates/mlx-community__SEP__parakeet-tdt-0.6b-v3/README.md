---
library_name: mlx
language:
- en
- es
- fr
- de
- bg
- hr
- cs
- da
- nl
- et
- fi
- el
- hu
- it
- lv
- lt
- mt
- pl
- pt
- ro
- sk
- sl
- sv
- ru
- uk
tags:
- mlx
- automatic-speech-recognition
- speech
- audio
- FastConformer
- Conformer
- Parakeet
license: cc-by-4.0
pipeline_tag: automatic-speech-recognition
base_model: nvidia/parakeet-tdt-0.6b-v3
---

# mlx-community/parakeet-tdt-0.6b-v3

This model was converted to MLX format from [nvidia/parakeet-tdt-0.6b-v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) using [the conversion script](https://gist.github.com/senstella/77178bb5d6ec67bf8c54705a5f490bed). Please refer to [original model card](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) for more details on the model.

## Use with mlx

### parakeet-mlx

```bash
pip install -U parakeet-mlx
```

```bash
parakeet-mlx audio.wav --model mlx-community/parakeet-tdt-0.6b-v3
```

### mlx-audio

```bash
pip install -U mlx-audio
```

```bash
python -m mlx_audio.stt.generate --model mlx-community/parakeet-tdt-0.6b-v3 --audio audio.wav --output somewhere
```