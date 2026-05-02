---
language:
- he
- en

tags:
- translation

license: apache-2.0
---

### he-en

* source group: Hebrew 
* target group: English 
*  OPUS readme: [heb-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-eng/README.md)

*  model: transformer
* source language(s): heb
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-10-04.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-eng/opus-2020-10-04.zip)
* test set translations: [opus-2020-10-04.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-eng/opus-2020-10-04.test.txt)
* test set scores: [opus-2020-10-04.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-eng/opus-2020-10-04.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.heb.eng 	| 52.0 	| 0.670 |


### System Info: 
- hf_name: he-en

- source_languages: heb

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['he', 'en']

- src_constituents: ('Hebrew', {'heb'})

- tgt_constituents: ('English', {'eng'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: heb-eng

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-eng/opus-2020-10-04.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-eng/opus-2020-10-04.test.txt

- src_alpha3: heb

- tgt_alpha3: eng

- chrF2_score: 0.67

- bleu: 52.0

- brevity_penalty: 0.9690000000000001

- ref_len: 73560.0

- src_name: Hebrew

- tgt_name: English

- train_date: 2020-10-04 00:00:00

- src_alpha2: he

- tgt_alpha2: en

- prefer_old: False

- short_pair: he-en

- helsinki_git_sha: 61fd6908b37d9a7b21cc3e27c1ae1fccedc97561

- transformers_git_sha: d99ed7ad618037ae878f0758157ed0764bd7f935

- port_machine: LM0-400-22516.local

- port_time: 2020-10-15-16:31