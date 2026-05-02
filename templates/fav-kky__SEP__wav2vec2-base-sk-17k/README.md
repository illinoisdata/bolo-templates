---
language: "sk"
tags:
- Slovak
- KKY
- FAV
license: "cc-by-nc-sa-4.0"
---

# wav2vec2-base-sk-17k
This is a monolingual Slovak Wav2Vec 2.0 base model pre-trained from 17 thousand hours of Slovak speech.
It was introduced in the paper **Transfer Learning of Transformer-Based Speech Recognition Models from Czech to Slovak** accepted for the TSD2023 conference.

This model does not have a tokenizer as it was pretrained on audio alone. In order to use this model for speech recognition, a tokenizer should be created, and the model should be fine-tuned on labeled data. 

The model was initialized from the Czech pre-trained model [fav-kky/wav2vec2-base-cs-80k-ClTRUS](https://huggingface.co/fav-kky/wav2vec2-base-cs-80k-ClTRUS). We found this cross-language transfer learning approach better than pre-training from scratch. See our paper for details.

## Pretraining data 
Almost 18 thousand hours of unlabeled Slovak speech:
- unlabeled data from VoxPopuli dataset (12.2k hours),
- recordings from TV shows (4.5k hours),
- oral history archives (800 hours),
- CommonVoice 13.0 (24 hours)

## Usage
Inputs must be 16kHz mono audio files.

This model can be used e.g. to extract per-frame contextual embeddings from audio:
```python
from transformers import Wav2Vec2Model, Wav2Vec2FeatureExtractor
import torchaudio

feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("fav-kky/wav2vec2-base-sk-17k")
model = Wav2Vec2Model.from_pretrained("fav-kky/wav2vec2-base-sk-17k")

speech_array, sampling_rate = torchaudio.load("/path/to/audio/file.wav")
inputs = feature_extractor(
    speech_array, 
    sampling_rate=16_000, 
    return_tensors="pt"
)["input_values"][0]

output = model(inputs)
embeddings = output.last_hidden_state.detach().numpy()[0]
```

## Speech recognition results
After fine-tuning, the model scored the following results on public datasets:
- Slovak portion of CommonVoice v13.0: **WER = 8.82%**
- Slovak portion of VoxPopuli: **WER = 8.88%**

See our paper for details.

## Paper 
The paper is available at https://link.springer.com/chapter/10.1007/978-3-031-40498-6_29.

The pre-print of our paper is available at https://arxiv.org/abs/2306.04399.

## Citation
If you find this model useful, please cite our paper:
```
@inproceedings{wav2vec2-base-sk-17k,
  author = {
    Lehe\v{c}ka, Jan and
    Psutka, Josef V. and
    Psutka, Josef
  },
  title = {{Transfer Learning of Transformer-Based Speech Recognition Models from Czech to Slovak}},
  year = {2023},
  isbn = {978-3-031-40497-9},
  publisher = {Springer Nature Switzerland},
  address = {Cham},
  url = {https://doi.org/10.1007/978-3-031-40498-6_29},
  doi = {10.1007/978-3-031-40498-6_29},
  booktitle = {Text, Speech, and Dialogue: 26th International Conference, TSD 2023, Pilsen, Czech Republic, September 4–6, 2023, Proceedings},
  pages = {328–338},
  numpages = {11},
}
```

## Related papers
- [INTERSPEECH 2022 - Exploring Capabilities of Monolingual Audio Transformers using Large Datasets in Automatic Speech Recognition of Czech](https://www.isca-speech.org/archive/pdfs/interspeech_2022/lehecka22_interspeech.pdf)
- [INTERSPEECH 2023 - Transformer-based Speech Recognition Models for Oral History Archives in English, German, and Czech](https://www.isca-archive.org/interspeech_2023/lehecka23_interspeech.pdf)

## Related models
- [fav-kky/wav2vec2-base-cs-80k-ClTRUS](https://huggingface.co/fav-kky/wav2vec2-base-cs-80k-ClTRUS)