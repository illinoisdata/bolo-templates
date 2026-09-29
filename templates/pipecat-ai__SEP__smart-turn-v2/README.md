---
pipeline_tag: voice-activity-detection
license: bsd-2-clause
tags:
  - speech-processing
  - semantic-vad
  - multilingual
datasets:
  - pipecat-ai/chirp3_1
  - pipecat-ai/orpheus_midfiller_1
  - pipecat-ai/orpheus_grammar_1
  - pipecat-ai/orpheus_endfiller_1
  - pipecat-ai/human_convcollector_1
  - pipecat-ai/rime_2
  - pipecat-ai/human_5_all
languages: 
  - en
  - fr
  - de
  - es
  - pt
  - zh
  - ja
  - hi
  - it
  - ko
  - nl
  - pl
  - ru
  - tr
---

# Smart Turn v2

**Smart Turn v2** is an open‑source semantic Voice Activity Detection (VAD) model that tells you **_whether a speaker has finished their turn_** by analysing the raw waveform, not the transcript.  
Compared with v1 it is:

* **Multilingual** – 14 languages (EN, FR, DE, ES, PT, ZH, JA, HI, IT, KO, NL, PL, RU, TR).
* **6 × smaller** – ≈ 360 MB vs. 2.3 GB.
* **3 × faster** – ≈ 12 ms to analyse 8 s of audio on an NVIDIA L40S.

## Links

* [Blog post: Smart Turn v2](https://www.daily.co/blog/smart-turn-v2-faster-inference-and-13-new-languages-for-voice-ai/)
* [GitHub repo](https://github.com/pipecat-ai/smart-turn) with training and inference code


## Intended use & task

| Use‑case                                    | Why this model helps                                                    |
|---------------------------------------------|-------------------------------------------------------------------------|
| Voice agents / chatbots                     | Wait to reply until the user has **actually** finished speaking.        |
| Real‑time transcription + TTS               | Avoid “double‑talk” by triggering TTS only when the user turn ends.     |
| Call‑centre assist & analytics              | Accurate segmentation for diarisation and sentiment pipelines.          |
| Any project needing semantic VAD            | Detects incomplete thoughts, filler words (“um …”, “えーと …”) and intonation cues ignored by classic energy‑based VAD. |

The model outputs a single probability; values ≥ 0.5 indicate the speaker has completed their utterance.

## Model architecture

* Backbone : `wav2vec2` encoder  
* Head     : shallow linear classifier  
* Params   : 94.8 M (float32)  
* Checkpoint: 360 MB Safetensors (compressed)  
The `wav2vec2 + linear` configuration out‑performed LSTM and deeper transformer variants during ablation studies.  

## Training data

| Source                  | Type                          | Languages |
|-------------------------|-------------------------------|-----------|
| `human_5_all`           | Human‑recorded                | EN        |
| `human_convcollector_1` | Human‑recorded                | EN        |
| `rime_2`                | Synthetic (Rime)              | EN        |
| `orpheus_midfiller_1`   | Synthetic (Orpheus)           | EN        |
| `orpheus_grammar_1`     | Synthetic (Orpheus)           | EN        |
| `orpheus_endfiller_1`   | Synthetic (Orpheus)           | EN        |
| `chirp3_1`              | Synthetic (Google Chirp3 TTS) | 14 langs  |

* Sentences were cleaned with Gemini 2.5 Flash to remove ungrammatical, controversial or written‑only text.
* Filler‑word lists per language (e.g., “um”, “えーと”) built with Claude & GPT‑o3 and injected near sentence ends to teach the model about interrupted speech.

All audio/text pairs are released on the [pipecat‑ai/datasets](https://huggingface.co/pipecat-ai/datasets) hub.

## Evaluation & performance

### Accuracy on unseen synthetic test set (50 % complete / 50 % incomplete)  
| Lang | Acc % | Lang | Acc % |
|------|-------|------|-------|
| EN   | 94.3  | IT   | 94.4  |
| FR   | 95.5  | KO   | 95.5  |
| ES   | 92.1  | PT   | 95.5  |
| DE   | 95.8  | TR   | 96.8  |
| NL   | 96.7  | PL   | 94.6  |
| RU   | 93.0  | HI   | 91.2  |
| ZH   | 87.2  | –    |   –   |

*Human English benchmark (`human_5_all`) : **99 %** accuracy.*

### Inference latency for 8 s audio

| Device                        | Time |
|-------------------------------|------|
| NVIDIA L40S                   | 12 ms |
| NVIDIA A100                   | 19 ms |
| NVIDIA T4 (AWS g4dn.xlarge)   | 75 ms |
| 16‑core x86\_64 CPU (Modal)   | 410 ms |

 [oai_citation:7‡Daily](https://www.daily.co/blog/smart-turn-v2-faster-inference-and-13-new-languages-for-voice-ai/)


## How to use

Please see the blog post and GitHub repo for more information on using the model, either standalone or with Pipecat.