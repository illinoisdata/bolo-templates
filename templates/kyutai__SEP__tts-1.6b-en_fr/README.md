---
license: cc-by-4.0
language:
- en
- fr
library_name: moshi
pipeline_tag: text-to-speech
tags:
- audio
---
# Model Card for Kyutai TTS

See also the [pre-print research paper](https://arxiv.org/abs/2509.08753),
the [project page](https://kyutai.org/next/tts), 
the [Colab example](https://colab.research.google.com/github/kyutai-labs/delayed-streams-modeling/blob/main/tts_pytorch.ipynb),
the [GitHub repository](https://github.com/kyutai-labs/delayed-streams-modeling/),
and the [repository of voices](https://huggingface.co/kyutai/tts-voices).

This is a model for streaming text-to-speech (TTS).
Unlike offline text-to-speech, where the model needs the entire text to produce the audio,
our model starts to output audio as soon as the first few words from the text have been given as input.
This model is actually 1.8B parameters, not 1.6B as the name might suggest.

## Model Details

The model architecture is a hierarchical Transformer that consumes tokenized text and generateds audio tokenized by Mimi,
see [the Moshi paper](https://arxiv.org/abs/2410.00037).
The frame rate is 12.5 Hz and each audio frame is represented by 32 audio tokens, although you can use less tokens at inference time for faster generation.
The backbone model is 1B parameters, and the depth transformer is 600M parameters and uses partial weight sharing similar to [Hibiki](https://arxiv.org/abs/2502.03382).
The audio is shifted by 16 steps (1.28 sec.) with respect to the text, and the model uses an acoustic/semantic delay of 2.

## Model Description

Kyutai TTS is a decoder-only model for streaming speech-to-text.
It leverages the multistream architecture of [Moshi](https://moshi.chat/) to model text stream based on the speech stream.
The text stream is shifted w.r.t. the audio stream to allow the model to predict text tokens based on the input audio.

* Developed by: Kyutai
* Model type: Streaming Text-To-Speech.
* Language(s) (NLP): English and French
* License: Model weights are licensed under CC-BY 4.0
* Repository: [GitHub](https://github.com/kyutai-labs/delayed-streams-modeling/)

## Uses

### Direct Use

This model is able to perform streaming text-to-speech generation, including dialogs.
The model supports voice conditioning through cross-attention pre-computed embeddings,
which are provided for a number of voices in our [tts-voices](https://huggingface.co/kyutai/tts-voices) repository. 
This model does not support Classifier Free Guidance (CFG) directly, but was trained with *CFG distillation* for improved speed (no need to double the batch size).
It is easy to batch and can reach a throughput of 75x generated audio per compute unit of time.

This model does not perform watermarking for two reasons:
- watermarking can easily be deactivated for open source models,
- our early experiments show that all watermark systems used by existing TTS are removed by simply encodeding and decoding the audio with Mimi.

Instead, we prefered to restrict the voice cloning ability to the use of pre-computed voice embeddings.

## How to Get Started with the Model

See the [GitHub repository](https://github.com/kyutai-labs/delayed-streams-modeling/).

## Training Details

The model was trained for 750k steps, with a batch size of 64, and a segment duration of 120 seconds. Then, CFG distillation was performed for 24k updates.

### Training Data

Pretraining stage: we use an audio collection of 2.5 million hours of publicly available audio content.
For this dataset, we obtained synthetic transcripts by running [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped)
with `whisper-medium`.


### Compute Infrastructure

Pretraining was done with 32 H100 Nvidia GPUs. CFG distillation was done on 8 such GPUs.

## Model Card Authors

Neil Zeghidour, Eugene Kharitonov, Manu Orsini, Václav Volhejn, Gabriel de Marmiesse, Edouard Grave, Patrick Perez, Laurent Mazaré, Alexandre Défossez