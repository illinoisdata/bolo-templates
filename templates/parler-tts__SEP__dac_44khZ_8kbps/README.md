---
library_name: transformers
tags:
- DAC
- audio
license: mit
---

# Descript Audio Codec (.dac): High-Fidelity Audio Compression with Improved RVQGAN

This repository is a wrapper around the original **Descript Audio Codec** model, a high fidelity general neural audio codec, introduced in the paper titled **High-Fidelity Audio Compression with Improved RVQGAN**.

It is designed to be used as a drop-in replacement of the [transformers implementation](https://huggingface.co/docs/transformers/v4.39.3/en/model_doc/encodec#overview) of [Encodec](https://github.com/facebookresearch/encodec), so that architectures that use Encodec can also be trained with DAC instead.
The [Parler-TTS library](https://github.com/huggingface/parler-tts) is an example of how to use DAC to train high-quality TTS models. We released [Parler-TTS Mini v0.1]("https://huggingface.co/parler-tts/parler_tts_mini_v0.1"), a first iteration model trained using 10k hours of narrated audiobooks. It generates high-quality speech with features that can be controlled using a simple text prompt (e.g. gender, background noise, speaking rate, pitch and reverberation)

To use this checkpoint, you first need to install the [Parler-TTS library](https://github.com/huggingface/parler-tts) with (to do once):
```sh
pip install git+https://github.com/huggingface/parler-tts.git
```

And then use:
```python
from parler_tts import DACModel
dac_model = DACModel.from_pretrained("parler-tts/dac_44khZ_8kbps")
```


🚨 If you want to use the original DAC codebase, refers to the [original repository](https://github.com/descriptinc/descript-audio-codec/tree/main) or to the [Original Usage](#original-usage) section.


## Original Usage

[arXiv Paper: High-Fidelity Audio Compression with Improved RVQGAN
](http://arxiv.org/abs/2306.06546) <br>
[Demo Site](https://descript.notion.site/Descript-Audio-Codec-11389fce0ce2419891d6591a68f814d5)<br>
[Github repo](https://github.com/descriptinc/descript-audio-codec/tree/main)<br>

👉 With Descript Audio Codec, you can compress **44.1 KHz audio** into discrete codes at a **low 8 kbps bitrate**.  <br>
🤌 That's approximately **90x compression** while maintaining exceptional fidelity and minimizing artifacts.  <br>
💪 Descript universal model works on all domains (speech, environment, music, etc.), making it widely applicable to generative modeling of all audio.  <br>
👌 It can be used as a drop-in replacement for EnCodec for all audio language modeling applications (such as AudioLMs, MusicLMs, MusicGen, etc.) <br>


### Installation
```
pip install descript-audio-codec
```
OR

```
pip install git+https://github.com/descriptinc/descript-audio-codec
```

### Weights
Weights are released as part of this repo under MIT license.
We release weights for models that can natively support 16 kHz, 24kHz, and 44.1kHz sampling rates.
Weights are automatically downloaded when you first run `encode` or `decode` command. You can cache them using one of the following commands
```bash
python3 -m dac download # downloads the default 44kHz variant
python3 -m dac download --model_type 44khz # downloads the 44kHz variant
python3 -m dac download --model_type 24khz # downloads the 24kHz variant
python3 -m dac download --model_type 16khz # downloads the 16kHz variant
```
We provide a Dockerfile that installs all required dependencies for encoding and decoding. The build process caches the default model weights inside the image. This allows the image to be used without an internet connection. [Please refer to instructions below.](#docker-image)


### Compress audio
```
python3 -m dac encode /path/to/input --output /path/to/output/codes
```

This command will create `.dac` files with the same name as the input files.
It will also preserve the directory structure relative to input root and
re-create it in the output directory. Please use `python -m dac encode --help`
for more options.

### Reconstruct audio from compressed codes
```
python3 -m dac decode /path/to/output/codes --output /path/to/reconstructed_input
```

This command will create `.wav` files with the same name as the input files.
It will also preserve the directory structure relative to input root and
re-create it in the output directory. Please use `python -m dac decode --help`
for more options.

### Programmatic Usage
```py
import dac
from audiotools import AudioSignal

# Download a model
model_path = dac.utils.download(model_type="44khz")
model = dac.DAC.load(model_path)

model.to('cuda')

# Load audio signal file
signal = AudioSignal('input.wav')

# Encode audio signal as one long file
# (may run out of GPU memory on long files)
signal.to(model.device)

x = model.preprocess(signal.audio_data, signal.sample_rate)
z, codes, latents, _, _ = model.encode(x)

# Decode audio signal
y = model.decode(z)

# Alternatively, use the `compress` and `decompress` functions
# to compress long files.

signal = signal.cpu()
x = model.compress(signal)

# Save and load to and from disk
x.save("compressed.dac")
x = dac.DACFile.load("compressed.dac")

# Decompress it back to an AudioSignal
y = model.decompress(x)

# Write to file
y.write('output.wav')
```