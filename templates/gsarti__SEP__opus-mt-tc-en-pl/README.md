---
language:
- en
- pl
- multilingual
license: apache-2.0
tags:
- translation
---

### OPUS Tatoeba English-Polish

**Update: The model is currently not functional. Please refer to the original checkpoint in the Tatoeba repository for a working version**

*This model was obtained by running the script [convert_marian_to_pytorch.py](https://github.com/huggingface/transformers/blob/master/src/transformers/models/marian/convert_marian_to_pytorch.py) with the flag `-m eng-pol`. The original models were trained by [J�rg Tiedemann](https://blogs.helsinki.fi/tiedeman/) using the [MarianNMT](https://marian-nmt.github.io/) library. See all available `MarianMTModel` models on the profile of the [Helsinki NLP](https://huggingface.co/Helsinki-NLP) group.*

* source language name: English
* target language name: Polish
* OPUS readme: [README.md](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pol/README.md)

* model: transformer
* source language code: en
* target language code: pl
* dataset: opus 
* release date: 2021-02-19
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2021-02-19.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pol/opus-2021-02-19.zip/eng-pol/opus-2021-02-19.zip)
* Training data: 
  * eng-pol: Tatoeba-train (59742979)
* Validation data: 
  * eng-pol: Tatoeba-dev, 44146
  * total-size-shuffled: 44145
  * devset-selected: top 5000  lines of Tatoeba-dev.src.shuffled!
* Test data: 
  * Tatoeba-test.eng-pol: 10000/64925
* test set translations file: [test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pol/opus-2021-02-19.zip/eng-pol/opus-2021-02-19.test.txt)
* test set scores file: [eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pol/opus-2021-02-19.zip/eng-pol/opus-2021-02-19.eval.txt)
* BLEU-scores
|Test set|score|
|---|---|
|Tatoeba-test.eng-pol|47.5|
* chr-F-scores
|Test set|score|
|---|---|
|Tatoeba-test.eng-pol|0.673|

### System Info: 
* hf_name: eng-pol
* source_languages: en
* target_languages: pl
* opus_readme_url: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pol/opus-2021-02-19.zip/README.md
* original_repo: Tatoeba-Challenge
* tags: ['translation']
* languages: ['en', 'pl']
* src_constituents: ['eng']
* tgt_constituents: ['pol']
* src_multilingual: False
* tgt_multilingual: False
* helsinki_git_sha: 70b0a9621f054ef1d8ea81f7d55595d7f64d19ff
* transformers_git_sha: 7c6cd0ac28f1b760ccb4d6e4761f13185d05d90b
* port_machine: databox
* port_time: 2021-10-18-15:11