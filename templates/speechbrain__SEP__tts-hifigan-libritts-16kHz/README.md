---
language: "en"
inference: false
tags:
- Vocoder
- HiFIGAN
- text-to-speech
- TTS
- speech-synthesis
- speechbrain
license: "apache-2.0"
datasets:
- LibriTTS
---

# Vocoder with HiFIGAN trained on LibriTTS

This repository provides all the necessary tools for using a [HiFIGAN](https://arxiv.org/abs/2010.05646) vocoder trained with [LibriTTS](https://www.openslr.org/60/) (with multiple speakers). The sample rate used for the vocoder is 16000 Hz.

The pre-trained model takes in input a spectrogram and produces a waveform in output. Typically, a vocoder is used after a TTS model that converts an input text into a spectrogram.

Alternatives to this models are the following:
- [tts-hifigan-libritts-22050Hz](https://huggingface.co/speechbrain/tts-hifigan-libritts-22050Hz) (same model trained on the same dataset, but for a sample rate of 22050 Hz)
- [tts-hifigan-ljspeech](https://huggingface.co/speechbrain/tts-hifigan-ljspeech)  (same model trained on LJSpeech for a sample rate of 22050 Hz).


## Install SpeechBrain

```bash
pip install speechbrain
```


Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Using the Vocoder

- *Basic Usage:*
```python
import torch
from speechbrain.inference.vocoders import HIFIGAN
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-libritts-16kHz", savedir="pretrained_models/tts-hifigan-libritts-16kHz")
mel_specs = torch.rand(2, 80,298)

# Running Vocoder (spectrogram-to-waveform)
waveforms = hifi_gan.decode_batch(mel_specs)
```

- *Spectrogram to Waveform Conversion:*
```python
import torchaudio
from speechbrain.inference.vocoders import HIFIGAN
from speechbrain.lobes.models.FastSpeech2 import mel_spectogram

# Load a pretrained HIFIGAN Vocoder
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-libritts-16kHz", savedir="pretrained_models/tts-hifigan-libritts-16kHz")

# Load an audio file (an example file can be found in this repository)
# Ensure that the audio signal is sampled at 16000 Hz; refer to the provided link for a 22050 Hz Vocoder.
signal, rate = torchaudio.load('tests/samples/ASR/spk1_snt1.wav')

# Ensure the audio is sigle channel
signal = signal[0].squeeze()

torchaudio.save('waveform.wav', signal.unsqueeze(0), 16000)

# Compute the mel spectrogram.
# IMPORTANT: Use these specific parameters to match the Vocoder's training settings for optimal results.
spectrogram, _ = mel_spectogram(
    audio=signal.squeeze(),
    sample_rate=16000,
    hop_length=256,
    win_length=1024,
    n_mels=80,
    n_fft=1024,
    f_min=0.0,
    f_max=8000.0,
    power=1,
    normalized=False,
    min_max_energy_norm=True,
    norm="slaney",
    mel_scale="slaney",
    compression=True
)

# Convert the spectrogram to waveform
waveforms = hifi_gan.decode_batch(spectrogram)

# Save the reconstructed audio as a waveform
torchaudio.save('waveform_reconstructed.wav', waveforms.squeeze(1), 16000)

# If everything is set up correctly, the original and reconstructed audio should be nearly indistinguishable

```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain.
To train it from scratch follow these steps:
1. Clone SpeechBrain:
```bash
git clone https://github.com/speechbrain/speechbrain/
```
2. Install it:
```bash
cd speechbrain
pip install -r requirements.txt
pip install -e .
```
3. Run Training:
```bash
cd recipes/LibriTTS/vocoder/hifigan/
python train.py hparams/train.yaml --data_folder=/path/to/LibriTTS_data_destination --sample_rate=16000
```

To change the sample rate for model training go to the `"recipes/LibriTTS/vocoder/hifigan/hparams/train.yaml"` file and change the value for `sample_rate` as required.
The training logs and checkpoints are available [here](https://drive.google.com/drive/folders/1cImFzEonNYhetS9tmH9R_d0EFXXN0zpn?usp=sharing).