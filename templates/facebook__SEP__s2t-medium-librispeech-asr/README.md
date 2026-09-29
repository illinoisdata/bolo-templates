---
language: en
datasets:
- librispeech_asr
tags:
- audio
- automatic-speech-recognition
pipeline_tag: automatic-speech-recognition
widget:
- example_title: Librispeech sample 1
  src: https://cdn-media.huggingface.co/speech_samples/sample1.flac
- example_title: Librispeech sample 2
  src: https://cdn-media.huggingface.co/speech_samples/sample2.flac
license: mit
---


# S2T-MEDIUM-LIBRISPEECH-ASR

`s2t-medium-librispeech-asr` is a Speech to Text Transformer (S2T) model trained for automatic speech recognition (ASR).
The S2T model was proposed in [this paper](https://arxiv.org/abs/2010.05171) and released in
[this repository](https://github.com/pytorch/fairseq/tree/master/examples/speech_to_text)


## Model description

S2T is an end-to-end sequence-to-sequence transformer model. It is trained with standard
autoregressive cross-entropy loss and generates the transcripts autoregressively.

## Intended uses & limitations

This model can be used for end-to-end speech recognition (ASR).
See the [model hub](https://huggingface.co/models?filter=speech_to_text) to look for other S2T checkpoints.


### How to use

As this a standard sequence to sequence transformer model, you can use the `generate` method to generate the
transcripts by passing the speech features to the model.

*Note: The `Speech2TextProcessor` object uses [torchaudio](https://github.com/pytorch/audio)  to extract the
filter bank features. Make sure to install the `torchaudio` package before running this example.*

You could either install those as extra speech dependancies with
`pip install transformers"[speech, sentencepiece]"` or install the packages seperatly 
with `pip install torchaudio sentencepiece`.


```python
import torch
from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
from datasets import load_dataset
import soundfile as sf

model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-medium-librispeech-asr")
processor = Speech2Textprocessor.from_pretrained("facebook/s2t-medium-librispeech-asr")

def map_to_array(batch):
    speech, _ = sf.read(batch["file"])
    batch["speech"] = speech
    return batch

ds = load_dataset(
    "patrickvonplaten/librispeech_asr_dummy",
    "clean",
    split="validation"
)
ds = ds.map(map_to_array)

input_features = processor(
    ds["speech"][0],
    sampling_rate=16_000,
    return_tensors="pt"
).input_features  # Batch size 1
generated_ids = model.generate(input_features=input_features)

transcription = processor.batch_decode(generated_ids)
```

#### Evaluation on LibriSpeech Test

The following script shows how to evaluate this model on the [LibriSpeech](https://huggingface.co/datasets/librispeech_asr)
*"clean"* and *"other"* test dataset.

```python
from datasets import load_dataset
from evaluate import load
from transformers import Speech2TextForConditionalGeneration, Speech2TextProcessor

librispeech_eval = load_dataset("librispeech_asr", "clean", split="test")  # change to "other" for other test dataset
wer = load("wer")

model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-medium-librispeech-asr").to("cuda")
processor = Speech2TextProcessor.from_pretrained("facebook/s2t-medium-librispeech-asr", do_upper_case=True)


def map_to_pred(batch):
    features = processor(batch["audio"]["array"], sampling_rate=16000, padding=True, return_tensors="pt")
    input_features = features.input_features.to("cuda")
    attention_mask = features.attention_mask.to("cuda")

    gen_tokens = model.generate(input_features=input_features, attention_mask=attention_mask)
    batch["transcription"] = processor.batch_decode(gen_tokens, skip_special_tokens=True)[0]
    return batch

result = librispeech_eval.map(map_to_pred, remove_columns=["audio"])

print("WER:", wer.compute(predictions=result["transcription"], references=result["text"]))
```

*Result (WER)*:

| "clean" | "other" |
|:-------:|:-------:|
| 3.5     | 7.8     |



## Training data

The S2T-MEDIUM-LIBRISPEECH-ASR is trained on [LibriSpeech ASR Corpus](https://www.openslr.org/12), a dataset consisting of
approximately 1000 hours of 16kHz read English speech.


## Training procedure

### Preprocessing

The speech data is pre-processed by extracting Kaldi-compliant 80-channel log mel-filter bank features automatically from
WAV/FLAC audio files via PyKaldi or torchaudio. Further utterance-level CMVN (cepstral mean and variance normalization)
is applied to each example.

The texts are lowercased and tokenized using SentencePiece and a vocabulary size of 10,000.


### Training

The model is trained with standard autoregressive cross-entropy loss and using [SpecAugment](https://arxiv.org/abs/1904.08779).
The encoder receives speech features, and the decoder generates the transcripts autoregressively.


### BibTeX entry and citation info

```bibtex
@inproceedings{wang2020fairseqs2t,
  title = {fairseq S2T: Fast Speech-to-Text Modeling with fairseq},
  author = {Changhan Wang and Yun Tang and Xutai Ma and Anne Wu and Dmytro Okhonko and Juan Pino},
  booktitle = {Proceedings of the 2020 Conference of the Asian Chapter of the Association for Computational Linguistics (AACL): System Demonstrations},
  year = {2020},
}

```