---
license: apache-2.0
language:
- ru
pipeline_tag: automatic-speech-recognition
tags:
- conformer
- streaming
- asr
- stt
- telephony
- russian
- speech
- t-tech
- t-one
---

# T-one: Streaming ASR for Russian Telephony

**🚀 T-one is a high-performance streaming ASR pipeline for Russian, specialized for the telephony domain.**

T-one provides a complete low-latency solution for real-time transcription. It features a pretrained streaming Conformer-based acoustic model, a custom phrase boundary detector and a decoder, making it a ready-to-use solution for production environments. It provides not only the pretrained model but also a full suite of tools for inference, fine-tuning, and deployment.

Developed by *T-Software DC*, this project is a practical low-latency, high-throughput ASR solution with modular components.

For more details, see the [**GitHub Repository**](https://github.com/voicekit-team/T-one).

## Table of Contents
1. [Project Summary](#-project-summary)
2. [Quality benchmarks](#-quality-benchmarks)
3. [Inference examples](#-inference-examples)
4. [Fine-tuning](#-fine-tuning)
5. [Acoustic model](#-acoustic-model)
6. [Training details](#-training-details)
7. [License](#-license)

## 📝 Project Summary

**Key Features:**
- **Streaming-first Architecture:** Built for low-latency, real-time applications.
- **Ready-to-Use Pipeline:** Includes a pretrained acoustic model, phrase splitter, and a KenLM-based [**CTC**](https://huggingface.co/learn/audio-course/chapter3/ctc) beam search decoder with examples for offline and streaming speech recognition inference.
- **Demo** — launch a local speech recognition service instantly via Docker and transcribe audio files or real-time microphone input.
- **Fine-tuning** T-one on a custom dataset is straightforward using the 🤗 ecosystem.
- **Easy Deployment:** Includes examples for deploying with Triton Inference Server for high-throughput scenarios.
- **Fully Open Source architecture:** All model and pipeline code is available.

## 📊 Quality benchmarks

**Word Error Rate ([WER](https://huggingface.co/spaces/evaluate-metric/wer))** is used to evaluate the quality of automatic speech recognition systems, which can be interpreted as the percentage of incorrectly recognized words compared to a reference transcript. A lower value indicates higher accuracy. T-one demonstrates state-of-the-art performance, especially on its target domain of telephony, while remaining competitive on general-purpose benchmarks.

| Category | T-one (71M) | GigaAM-RNNT v2 (243M) | GigaAM-CTC v2 (242M) | Vosk-model-ru 0.54 (65M) | Vosk-model-small-streaming-ru 0.54 (20M) | Whisper large-v3 (1540M) |
|:--|:--|:--|:--|--:|:--|:--|
| Call-center | **8.63** | 10.22 | 10.57 | 11.28 | 15.53 | 19.39 |
| Other telephony | **6.20** | 7.88 | 8.15 | 8.69 | 13.49 | 17.29 |
| Named entities | **5.83** | 9.55 | 9.81 | 12.12 | 17.65 | 17.87 |
| CommonVoice 19 (test split) | 5.32 | **2.68** | 3.14 | 6.22 | 11.3 | 5.78 |
| OpenSTT asr_calls_2_val original | 20.27 | **20.07** | 21.24 | 22.64 | 29.45 | 29.02 |
| OpenSTT asr_calls_2_val re-labeled | **7.94** | 11.14 | 12.43 | 13.22 | 21.03 | 20.82 |

## 👨‍💻 Inference examples

### Offline Inference (for entire audio files)
```python
from tone import StreamingCTCPipeline, read_audio, read_example_audio


audio = read_example_audio() # or read_audio("your_audio.flac")

pipeline = StreamingCTCPipeline.from_hugging_face()
print(pipeline.forward_offline(audio))  # run offline recognition
```
Output:
```
[TextPhrase(text='привет', start_time=1.79, end_time=2.04), TextPhrase(text='это я', start_time=3.72, end_time=4.26), TextPhrase(text='я подумала не хочешь ли ты встретиться спустя все эти годы', start_time=5.88, end_time=10.59)]
```

### Streaming Inference (for real-time audio)

```python
from tone import StreamingCTCPipeline, read_stream_example_audio


pipeline = StreamingCTCPipeline.from_hugging_face()

state = None  # Current state of the ASR pipeline (None - initial)
for audio_chunk in read_stream_example_audio():  # Use any source of audio chunks
    new_phrases, state = pipeline.forward(audio_chunk, state)
    print(new_phrases)

# Finalize the pipeline and get the remaining phrases
new_phrases, _ = pipeline.finalize(state)
print(new_phrases)
```
Output:
```
TextPhrase(text='привет', start_time=1.79, end_time=2.04)
TextPhrase(text='это я', start_time=3.72, end_time=4.26)
TextPhrase(text='я подумала не хочешь ли ты встретиться спустя все эти годы', start_time=5.88, end_time=10.59)
```

## 🔧 Fine-tuning
In order to fine-tune T-one from a pre-trained checkpoint you need to prepare the training dataset, load the tokenizer and feature extractor from `t-tech/T-one` 🤗 repo.

```python
import torch

from tone.training.model_wrapper import ToneForCTC


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = ToneForCTC.from_pretrained("t-tech/T-one").to(device)
```

Setup the data collator, evaluation metric, training arguments and 🤗 Trainer.

For a complete guide please refer to the [**fine-tuning example notebook**](https://github.com/voicekit-team/T-one/blob/main/examples/finetune_example.ipynb).

## 🎙 Acoustic model

### Architecture
T-one is a 71M parameter acoustic model based on the **Conformer** architecture, with several key innovations to improve performance and efficiency:
- **SwiGLU Activation:** The feed-forward module is replaced with a SwiGLU module for better performance.
- **Modern Normalization:** SiLU (Swish) activations and RMSNorm are used in place of ReLU and LayerNorm.
- **RoPE Embeddings:** Relative positional embeddings from Transformer-XL are replaced with faster Rotary Position Embeddings (RoPE).
- **U-Net Structure:** The temporal dimension is downsampled and then upsampled within the Conformer blocks, improving the model's receptive field.
- **Attention Score Reuse:** Multi-Head Self-Attention layers are grouped, and attention scores are computed only once per group to reduce computation.
- **Efficient State Management:** Streaming states are used only in the final two layers of the model.

It processes audio in 300 ms chunks and generates transcriptions using either greedy decoding or a KenLM-based CTC beam search decoder.

The model was trained using CTC-Loss.
T-one is primarily intended for use with telephone-channel audio. However, since it was trained on heterogeneous data, it is robust across different domains and can be used not only for telephony.
The model supports streaming inference, which means it can process long audio files out-of-the-box in a real-time manner.
The primary use case for this model is streaming speech recognition of calls. The user sends small audio chunks to the model, and it processes each segment incrementally, returning the finalized text and word-level timestamps in real time.
T-one can be easily fine-tuned for specific domains.

For a detailed exploration of our architecture, design choices, and implementation, check out our accompanying [**article**](https://habr.com/ru/companies/tbank/articles/929850). Also refer to our **technical deep dive** on how to improve quality and training speed of a streaming ASR model on [**YouTube**](https://www.youtube.com/watch?v=OQD9o1MdFRE).

## 📉 Training details

### Training Data
The acoustic model was trained on over 80,000 hours of Russian speech. A significant portion (up to 64%) was pseudo-labeled using a robust ROVER model ensemble.

| Domain      | Hours   | Source      |
|:------------|:--------|:------------|
| Telephony   | 57.9k   | internal    |
| Far-field   | 2.2K    | internal    |
| Mix         | 18.4K   | internal    |
| Mix         | 2.3K    | open-source |

### Training Procedure
The model was trained from scratch (random initialization) for 7 days on 8 A100 GPUs using the **NVIDIA NeMo** framework. Key training parameters include:
- **Optimizer:** AdamW
- **Scheduler:** Cosine annealing with warmup
- **Precision:** 16-bit mixed precision
- **Batching:** Semi-sorted batching for efficiency

## 📜 License

This project, including the code and pretrained models, is released under the **Apache 2.0 License**.