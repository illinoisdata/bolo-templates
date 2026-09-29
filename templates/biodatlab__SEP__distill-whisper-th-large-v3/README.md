---
license: mit
---

## Distilled Large-V3 Whisper ASR Model for Thai

### Model Description
This is a fine-tuned distilled Automatic Speech Recognition (ASR) model, based on the Whisper Large Turbo V3 architecture. It has been specifically tailored for Thai language speech recognition and substantially improve the performance on Thai speech.

#### Fine-tuning Details
- **Original Model**: Whisper Large V3 Turbo
- **Datasets Used for Fine-tuning**:
  - Common Voice v13
  - Gowajee
  - Thai Elderly Speech Corpus
  - Custom Scraped Data
  - Thai-Central Dialect from [SLSCU Thai Dialect Corpus](https://github.com/SLSCU/thai-dialect-corpus)

### Model Performance
- **DeepCut Tokenized WER on Common Voice 13 Test Set**:
  - Original Model: **41.53%**
  - This Model: **6.82%**
- **DeepCut Tokenized WER on FLEURS Test Set**:
  - Original Model: **25.56%**
  - This Model: **10.65%**

### Intended Use
This model is intended for use in applications requiring Thai language speech recognition.

### Limitations
- The model is specifically trained for the Thai language and may not perform well with other languages.
- Performance might vary across different Thai dialects and accents.
- As with any ASR system, background noise and speech clarity can impact recognition accuracy.

### Acknowledgments
This model was developed using resources and datasets provided by the speech and language technology community. Special thanks to the teams behind Common Voice, Gowajee, SLSCU, and the Thai Elderly Speech Corpus for their valuable datasets.

### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.2
- Datasets 2.16.1
- Tokenizers 0.15.0

### Citation

Cite using Bibtex:

```
@inproceedings{aung-etal-2024-thonburian,
    title = "Thonburian Whisper: Robust Fine-tuned and Distilled Whisper for {T}hai",
    author = "Aung, Zaw Htet  and
      Thavornmongkol, Thanachot  and
      Boribalburephan, Atirut  and
      Tangsriworakan, Vittavas  and
      Pipatsrisawat, Knot  and
      Achakulvisut, Titipat",
    editor = "Abbas, Mourad  and
      Freihat, Abed Alhakim",
    booktitle = "Proceedings of the 7th International Conference on Natural Language and Speech Processing (ICNLSP 2024)",
    month = oct,
    year = "2024",
    address = "Trento",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.icnlsp-1.17",
    pages = "149--156",
}
```
---