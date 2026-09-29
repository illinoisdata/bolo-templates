---
license: apache-2.0
language:
- en
pipeline_tag: text-to-speech
tags:
- model_hub_mixin
- pytorch_model_hub_mixin
- text-to-speech
base_model:
- sesame/csm-1b
---
<div>
  <p style="margin-bottom: 0; margin-top: 0;">
    <strong>See <a href="https://huggingface.co/collections/unsloth/text-to-speech-tts-models-68007ab12522e96be1e02155">our collection</a> for all our TTS model uploads.</strong>
  </p>
  <p style="margin-bottom: 0;">
    <em>Learn to fine-tune TTS models - <a href="https://docs.unsloth.ai/basics/text-to-speech-tts-fine-tuning">Read our Guide</a>.</em>
  </p>
<p style="margin-top: 0;margin-bottom: 0;">
    <em><a href="https://docs.unsloth.ai/basics/unsloth-dynamic-v2.0-gguf">Unsloth Dynamic 2.0</a> achieves superior accuracy & outperforms other leading quants.</em>
  </p>
  <div style="display: flex; gap: 5px; align-items: center; ">
    <a href="https://github.com/unslothai/unsloth/">
      <img src="https://github.com/unslothai/unsloth/raw/main/images/unsloth%20new%20logo.png" width="133">
    </a>
    <a href="https://discord.gg/unsloth">
      <img src="https://github.com/unslothai/unsloth/raw/main/images/Discord%20button.png" width="173">
    </a>
    <a href="https://docs.unsloth.ai/basics/text-to-speech-tts-fine-tuning">
      <img src="https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/images/documentation%20green%20button.png" width="143">
    </a>
  </div>
<h1 style="margin-top: 0rem;">✨ Run & Fine-tune TTS models with Unsloth!</h1>
</div>

- Fine-tune TTS models for free using our Google [Colab notebooks here](https://docs.unsloth.ai/get-started/unsloth-notebooks#text-to-speech-tts-notebooks)!
- Read our Blog about TTS support: [unsloth.ai/blog/tts](https://docs.unsloth.ai/basics/text-to-speech-tts-fine-tuning)

| Unsloth supports          |    Free Notebooks                                                                                           | Performance | Memory use |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|-------------|----------|
| **Sesame-CSM-1B**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Sesame_CSM_(1B)-TTS.ipynb)               | 1.5x faster | 58% less |
| **Whisper Large V3**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Whisper.ipynb)               | 1.5x faster | 50% less |
| **Qwen3 (14B)**      | [▶️ Start on Colab](https://docs.unsloth.ai/get-started/unsloth-notebooks)               | 2x faster | 70% less |
| **Llama 3.2 Vision (11B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(11B)-Vision.ipynb)               | 1.8x faster | 50% less |

## CSM 1B

**2025/03/13** - We are releasing the 1B CSM variant. Code is available on GitHub: [SesameAILabs/csm](https://github.com/SesameAILabs/csm).

---

CSM (Conversational Speech Model) is a speech generation model from [Sesame](sesame.com) that generates RVQ audio codes from text and audio inputs. The model architecture employs a [Llama](https://www.llama.com/) backbone and a smaller audio decoder that produces [Mimi](https://huggingface.co/kyutai/mimi) audio codes.

A fine-tuned variant of CSM powers the [interactive voice demo](https://www.sesame.com/voicedemo) shown in our [blog post](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice).

A hosted [HuggingFace space](https://huggingface.co/spaces/sesame/csm-1b) is also available for testing audio generation.

## Usage

Setup the repo

```bash
git clone git@github.com:SesameAILabs/csm.git
cd csm
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# You will need access to sesame/csm-1b and meta-llama/Llama-3.2-1B
huggingface-cli login
```

Generate a sentence

```python
from generator import load_csm_1b
import torchaudio

generator = load_csm_1b(device="cuda")

audio = generator.generate(
    text="Hello from Sesame.",
    speaker=0,
    context=[],
    max_audio_length_ms=10_000,
)

torchaudio.save("audio.wav", audio.unsqueeze(0).cpu(), generator.sample_rate)
```

CSM sounds best when provided with context. You can prompt or provide context to the model using a `Segment` for each speaker utterance.

```python
speakers = [0, 1, 0, 0]
transcripts = [
    "Hey how are you doing.",
    "Pretty good, pretty good.",
    "I'm great.",
    "So happy to be speaking to you.",
]
audio_paths = [
    "utterance_0.wav",
    "utterance_1.wav",
    "utterance_2.wav",
    "utterance_3.wav",
]

def load_audio(audio_path):
    audio_tensor, sample_rate = torchaudio.load(audio_path)
    audio_tensor = torchaudio.functional.resample(
        audio_tensor.squeeze(0), orig_freq=sample_rate, new_freq=generator.sample_rate
    )
    return audio_tensor

segments = [
    Segment(text=transcript, speaker=speaker, audio=load_audio(audio_path))
    for transcript, speaker, audio_path in zip(transcripts, speakers, audio_paths)
]
audio = generator.generate(
    text="Me too, this is some cool stuff huh?",
    speaker=1,
    context=segments,
    max_audio_length_ms=10_000,
)

torchaudio.save("audio.wav", audio.unsqueeze(0).cpu(), generator.sample_rate)
```

## FAQ

**Does this model come with any voices?**

The model open sourced here is a base generation model. It is capable of producing a variety of voices, but it has not been fine-tuned on any specific voice.

**Can I converse with the model?**

CSM is trained to be an audio generation model and not a general purpose multimodal LLM. It cannot generate text. We suggest using a separate LLM for text generation.

**Does it support other languages?**

The model has some capacity for non-English languages due to data contamination in the training data, but it likely won't do well.

## Misuse and abuse ⚠️

This project provides a high-quality speech generation model for research and educational purposes. While we encourage responsible and ethical use, we **explicitly prohibit** the following:

- **Impersonation or Fraud**: Do not use this model to generate speech that mimics real individuals without their explicit consent.
- **Misinformation or Deception**: Do not use this model to create deceptive or misleading content, such as fake news or fraudulent calls.
- **Illegal or Harmful Activities**: Do not use this model for any illegal, harmful, or malicious purposes.

By using this model, you agree to comply with all applicable laws and ethical guidelines. We are **not responsible** for any misuse, and we strongly condemn unethical applications of this technology.

**Authors**
Johan Schalkwyk, Ankit Kumar, Dan Lyth, Sefik Emre Eskimez, Zack Hodari, Cinjon Resnick, Ramon Sanabria, Raven Jiang, and the Sesame team.