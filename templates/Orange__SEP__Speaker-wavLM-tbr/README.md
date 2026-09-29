---
license: cc-by-sa-3.0
tags:
- Speaker traits
- Voice
- Speaker
language:
- en
base_model:
- microsoft/wavlm-large
datasets:
- VCTK
- VoxCeleb
---

# Timbral Embeddings extractor
This model produces embeddings that globally represent the timbral traits of a speaker's voice. These embeddings can be used the same way as for a classical speaker verification (ASV): 
in order to compare two voice signals, an embeddings vector must be computed for each of them. Then the cosine similarity between the two embeddings can be used for comparison.
The main difference with classical ASV embeddings is that, here, only the timbral traits are compared.

The model has been derived from the self-supervised pretrained model [WavLM-large](https://huggingface.co/microsoft/wavlm-large). 

The next section explains how to compute these timbral embeddings.


# Usage
The following code snippet uses the file [spk_embeddings.py](https://huggingface.co/Orange/Speaker-wavLM-pro/blob/main/spk_embeddings.py) 
to build the architecture of the model. 
Its weights are then downloaded from this repository.
```
from spk_embeddings import EmbeddingsModel, compute_embedding
import torch

model = EmbeddingsModel.from_pretrained("Orange/Speaker-wavLM-tbr")
model.eval()
```

The model produces normalized vectors as embeddings.

The python file also contains the function to compute the timbral embeddings of an audio file.
In this tutorial version, the audio file is expected to be sampled at 16kHz.
Depending on the available memory (cpu or gpu), you may change the value of the *max_size* parameter, 
which is used to truncate the long audio signals.

finally, we can compute two embeddings from two different files and compare them with a cosine similarity:

```
wav1 = "/voxceleb1_2019/test/wav/id10270/x6uYqmx31kE/00001.wav"
wav2 = "/voxceleb1_2019/test/wav/id10270/8jEAjG6SegY/00008.wav"

e1 = compute_embedding(wav1, model)
e2 = compute_embedding(wav2, model)
sim = float(torch.matmul(e1,e2.t()))

print(sim) # 0.7743815779685974
```

# Evaluations
Although it is not directly designed for this use case, evaluation on a standard ASV task can be performed with this model. Applied to 
the [VoxCeleb1-clean test set](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/meta/veri_test2.txt), one can compute an Equal Error Rate 
(EER, lower value denotes a better identification, random prediction leads to a value of 50%) and the associated threshold. 
This value can be interpreted as the ability to identify speakers only with timbral cues. 
Tests between two utterances leading to a cosine similarity above the threshold should be considered as similar in terms of timbral cues.

A discussion about this interpretation can be
found in the paper mentioned hereafter, as well as other experiments showing correlations between these embeddings and timbral voice attributes.

The table below provides the EER and threshold of the different [variants](#variants) of this model.

| Variant name| EER (%) | threshold |
| --- | --- | --- |
| W-TBR   | 1.68 | 0.472 |
| WTA128 | 2.29 | 0.472 |
| WTA64 | 2.88 | 0.446 |

Please note that the EER value can vary a little depending on the max_size defined to reduce long audios (max 30 seconds in our case).

# Limitations
The fine tuning data used to produce this model (VoxCeleb, VCTK) are mostly in english, which may affect the performance on other languages.
The performance may also vary with the audio quality (recording device, background noise, ...), specially for audio qualities not covered by the training set, as no specific algorithm, e.g. data augmentation, was used during training to tackle this problem.

# Publication
Details about the method used to build this model have been published at Interspeech 2024 in the paper entitled 
[Disentangling prosody and timbre embeddings via voice conversion](https://www.isca-archive.org/interspeech_2024/gengembre24_interspeech.pdf).

Please consider citing this paper if you use this model in your own research work.

In this paper the model corresponding to revision 'main' is denoted as W-TBR. The other two models used in this study can also be found on HuggingFace :
- [W-PRO](https://huggingface.co/Orange/Speaker-wavLM-pro) for non-timbral related embeddings
- [W-SPK](https://huggingface.co/Orange/Speaker-wavLM-id) for speaker embeddings (ASV)


### Citation
Gengembre, N., Le Blouch, O., Gendrot, C. (2024) Disentangling prosody and timbre embeddings via voice conversion. Proc. Interspeech 2024, 2765-2769, doi: 10.21437/Interspeech.2024-207

### BibteX citation
```
@inproceedings{gengembre24_interspeech,
  title     = {Disentangling prosody and timbre embeddings via voice conversion},
  author    = {Nicolas Gengembre and Olivier {Le Blouch} and Cédric Gendrot},
  year      = {2024},
  booktitle = {Interspeech 2024},
  pages     = {2765--2769},
  doi       = {10.21437/Interspeech.2024-207},
  issn      = {2958-1796},
}
```

# Variants
By using the `revision` parameter in the `from_pretrained` method (set as one of the branch names of this repository) you will be able to access alternative versions of the model. 

The table below provides a short description of the variants and their performance on the Voxceleb test set.

| Variant name | `revision` | Description | Embeddings size |
| --- | --- | --- | --- | 
| W-TBR | main    | baseline, description in paper | 128 | 
| WTA128 | wta128 | enriched training dataset, more conversions | 128  | 
| WTA64 | wta64 | enriched training dataset, more conversions | 64  | 


# License

CREATIVE COMMONS Attribution-ShareAlike 3.0 Unported