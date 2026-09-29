---
license: cc-by-4.0
datasets:
- mozilla-foundation/common_voice_17_0
- facebook/multilingual_librispeech
- facebook/voxpopuli
- datasets-CNRS/PFC
- datasets-CNRS/CFPP
- datasets-CNRS/CLAPI
- gigant/african_accented_french
- google/fleurs
- datasets-CNRS/lesvocaux
- datasets-CNRS/ACSYNT
- medkit/simsamu
language:
- fr
metrics:
- wer
base_model:
- nvidia/stt_fr_fastconformer_hybrid_large_pc
pipeline_tag: automatic-speech-recognition
tags:
- automatic-speech-recognition
- speech
- audio
- Transducer
- FastConformer
- CTC
- Transformer
- pytorch
- NeMo
library_name: nemo
model-index:
- name: linto_stt_fr_fastconformer
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: common-voice-18-0
      type: mozilla-foundation/common_voice_18_0
      config: fr
      split: test
      args:
        language: fr
    metrics:
    - name: Test WER
      type: wer
      value: 8.96
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Multilingual LibriSpeech
      type: facebook/multilingual_librispeech
      config: french
      split: test
      args:
        language: fr
    metrics:
    - name: Test WER
      type: wer
      value: 4.7
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Vox Populi
      type: facebook/voxpopuli
      config: french
      split: test
      args:
        language: fr
    metrics:
    - name: Test WER
      type: wer
      value: 10.83
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: SUMM-RE
      type: linagora/SUMM-RE
      config: french
      split: test
      args:
        language: fr
    metrics:
    - name: Test WER
      type: wer
      value: 23.5
---
# LinTO STT French – FastConformer

<style>
img {
 display: inline;
}
</style>

[![Model architecture](https://img.shields.io/badge/Model_Arch-FastConformer--Transducer_CTC-lightgrey#model-badge)](#model-architecture)  
[![Model size](https://img.shields.io/badge/Params-115M-lightgrey#model-badge)](#model-architecture)  
[![Language](https://img.shields.io/badge/Language-fr-lightgrey#model-badge)](#datasets)

---

A new version with punctuation is available: [linagora/linto_stt_fr_fastconformer_pc](https://huggingface.co/linagora/linto_stt_fr_fastconformer_pc)!

## Overview

This model is a fine-tuned version of the [NVIDIA French FastConformer Hybrid Large model](https://huggingface.co/nvidia/stt_fr_fastconformer_hybrid_large_pc). 
It is a large (115M parameters) hybrid ASR model trained with both **Transducer (default)** and **CTC** losses.

Compared to the base model, this version:
- Does **not** include punctuation or uppercase letters. See [linagora/linto_stt_fr_fastconformer_pc](https://huggingface.co/linagora/linto_stt_fr_fastconformer_pc) for punctuation and casing.
- Was trained on **9,500+ hours** of diverse, manually transcribed French speech.

---

## Performance

The evaluation code is available in the [ASR Benchmark repository](https://github.com/linagora-labs/asr_benchmark).

### Word Error Rate (WER)

WER was computed **without punctuation or uppercase letters** and datasets were cleaned. 
The [SUMM-RE dataset](https://huggingface.co/datasets/linagora/SUMM-RE) is the only one used **exclusively for evaluation**, meaning neither model saw it during training.

Evaluations can be very long (especially for whisper) so we selected only segments with a duration over 1 second and used a subset of the test split for most datasets:
- 15% of CommonVoice: 2424 rows (3.9h)
- 33% of MultiLingual LibriSpeech: 800 rows (3.3h)
- 33% of SUMM-RE: 1004 rows (2h). We selected only segments above 4 seconds to ensure quality.
- 33% of VoxPopuli: 678 rows (1.6h)
- Multilingual TEDx: 972 rows (1.5h)
- 50% of our internal Youtube corpus: 956 rows (1h)

![WER table](https://huggingface.co/linagora/linto_stt_fr_fastconformer/resolve/main/assets/wer_table.png)

As shown in the table above (lower is better), the model demonstrates robust performance across all datasets, consistently achieving results close to the best.

### Real-Time Factor (RTF)

RTFX (the inverse of RTF) measures how many seconds of audio can be transcribed per second of processing time.

Evaluation:
- Hardware: Laptop with NVIDIA RTX 4090
- Input: 5 audio files (~2 minutes each) from the ACSYNT corpus
- Higher is better

![RTF table](https://huggingface.co/linagora/linto_stt_fr_fastconformer/resolve/main/assets/rtf_table.png)

---

## Usage

This model can be used with the [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo) for both inference and fine-tuning.

```python
# Install nemo
# !pip install nemo_toolkit['all']

import nemo.collections.asr as nemo_asr

model_name = "linagora/linto_stt_fr_fastconformer"
asr_model = nemo_asr.models.ASRModel.from_pretrained(model_name=model_name)

# Path to your 16kHz mono-channel audio file
audio_path = "/path/to/your/audio/file"

# Transcribe with defaut transducer decoder
asr_model.transcribe([audio_path])

# (Optional) Switch to CTC decoder
asr_model.change_decoding_strategy(decoder_type="ctc")

# (Optional) Transcribe with CTC decoder
asr_model.transcribe([audio_path])
```

It can also be used with the [LinTO STT API](https://github.com/linto-ai/linto-stt/tree/master/nemo), 
an Automatic Speech Recognition (ASR) API that can function either as a standalone transcription service 
or be deployed within a microservices infrastructure using a message broker connector. It supports both offline and real-time transcription.

## Training Details

The training code is available in the [nemo_asr_training repository](https://github.com/linagora-labs/nemo_asr_training).  
The full configuration used for fine-tuning is available [here](https://github.com/linagora-labs/nemo_asr_training/blob/main/fastconformer/yamls/finetuning_linto_stt_fr_fastconformer.yaml).

### Hardware
- 1× NVIDIA H100 GPU (80 GB)

### Training Configuration
- Precision: BF16 mixed precision  
- Max training steps: 100,000  
- Gradient accumulation: 4 batches  

### Tokenizer
- Type: SentencePiece  
- Vocabulary size: 1,024 tokens

### Optimization
- Optimizer: `AdamW`
  - Learning rate: `1e-5`
  - Betas: `[0.9, 0.98]`
  - Weight decay: `1e-3`
- Scheduler: `CosineAnnealing`
  - Warmup steps: 10,000
  - Minimum learning rate: `1e-6`

### Data Setup
- 6 duration buckets (ranging from 0.1s to 30s)  
- Batch sizes per bucket:
  - Bucket 1 (shortest segments): batch size 80  
  - Bucket 2: batch size 76  
  - Bucket 3: batch size 72  
  - Bucket 4: batch size 68  
  - Bucket 5: batch size 64  
  - Bucket 6 (longest segments): batch size 60

### Training datasets

The data were transformed, processed and converted using [NeMo tools from the SSAK repository](https://github.com/linagora-labs/ssak/tree/main/tools/nemo)

The model was trained on over 9,500 hours of French speech, covering:
- Read and spontaneous speech
- Conversations and meetings
- Varied accents and audio conditions

![Datasets](https://huggingface.co/linagora/linto_stt_fr_fastconformer/resolve/main/assets/datasets_hours.png)

Datasets Used (by size):
- YouTubeFr: an internally curated corpus of CC0-licensed French-language videos sourced from YouTube. Will soon be available on LeVoiceLab platform
- [YODAS](https://huggingface.co/datasets/espnet/yodas): fr000 subset
- [Multilingual LibriSpeech](https://www.openslr.org/94/): french subset
- [CommonVoice](https://commonvoice.mozilla.org/fr/datasets): french subset
- [ESLO](http://eslo.huma-num.fr/index.php)
- [VoxPopuli](https://huggingface.co/datasets/facebook/voxpopuli): french subset
- [Multilingual TEDx](https://www.openslr.org/100/): french subset
- [TCOF](https://www.cnrtl.fr/corpus/tcof/)
- CTF-AR (Corpus de Conversations Téléphoniques en Français avec Accents Régionaux): will soon be available on LeVoiceLab platform
- [PFC](https://www.ortolang.fr/market/corpora/pfc)
- [OFROM](https://ofrom.unine.ch/index.php?page=citations)
- CTFNN1 (Corpus de Conversations Téléphoniques en Français impliquant des accents Non-Natifs): will soon be available on LeVoiceLab platform
- [CFPP2000](https://www.ortolang.fr/market/corpora/cfpp2000)
- [VOXFORGE](https://www.voxforge.org/)
- [CLAPI](http://clapi.ish-lyon.cnrs.fr/)
- [AfricanAccentedFrench](https://www.openslr.org/57/)
- [FLEURS](https://huggingface.co/datasets/google/fleurs): french subset
- [LesVocaux](https://www.ortolang.fr/market/corpora/lesvocaux/v0.0.1)
- LINAGORA_Meetings
- [CFPB](https://orfeo.ortolang.fr/annis-sample/cfpb/CFPB-1000-5.html)
- [ACSYNT](https://www.ortolang.fr/market/corpora/sldr000832)
- [PxSLU](https://arxiv.org/abs/2207.08292)
- [SimSamu](https://huggingface.co/datasets/medkit/simsamu)

## Limitations

- May struggle with rare vocabulary, heavy accents, or overlapping/multi-speaker audio.
- Outputs are lowercase only, with no punctuation, due to limitations in some training datasets. See [linagora/linto_stt_fr_fastconformer_pc](https://huggingface.co/linagora/linto_stt_fr_fastconformer_pc) for punctuation and casing.

## References

[1] [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084)

[2] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)

[3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

## Acknowledgements

Thanks to NVIDIA for providing the base model architecture and the NeMo framework.

## Licence

The model is released under a [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license, in line with the licensing of the original model it was fine-tuned from.