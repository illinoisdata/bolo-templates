---
language:
- cs
- sl
- sk
- pt
- pl
- 'no'
- it
- hr
- fr
- en
- da
- de
- sv
license: cc-by-4.0
tags:
- pretraining
---

# mELECTRA (Multilingual ELECTRA)

mELECTRA is an [Electra](https://arxiv.org/abs/2003.10555)-based model pretrained on a diverse multilingual corpus. It supports multiple languages, including **Swedish (SE), Slovenian (SL), Slovak (SK), Portuguese (PT), Polish (PL), Norwegian (NO), Italian (IT), Croatian (HR), French (FR), English (EN), Danish (DK), German (DE), and Czech (CZ)**. The model can be fine-tuned for various NLP tasks such as text classification, named entity recognition, and masked token prediction. 

This model is released under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/), allowing commercial use. 

---

## Model Details

- **Architecture:** ELECTRA-Small
- **Languages Supported:** Swedish, Slovenian, Slovak, Portuguese, Spanish, Polish, Norwegian, Italian, Croatian, French, English, Danish, German, Czech
- **Pretraining Data:** Multilingual corpus (news articles, Wikipedia, and web texts)
- **Vocabulary:** SentencePiece-based tokenizer (`m.model`)

---

## Tokenization with SentencePiece

mELECTRA uses a **SentencePiece tokenizer** and requires a SentencePiece model file (`m.model`) for correct tokenization. Ensure that you properly load and use this tokenizer to maintain compatibility with the model.

### Example: Tokenization

#### Using HuggingFace AutoTokenizer (Recommended)

```python
from transformers import AutoTokenizer

# Load the tokenizer directly from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained("AILabTUL/mELECTRA")

# Or load from local directory
# tokenizer = AutoTokenizer.from_pretrained("./mELECTRA")

# Tokenize input text
sentence = "This is a multilingual model supporting multiple languages."
tokens = tokenizer.tokenize(sentence)
ids = tokenizer.encode(sentence)

print(f"Tokens: {tokens}")
print(f"IDs: {ids}")

# Decode back to text
decoded = tokenizer.decode(ids)
print(f"Decoded: {decoded}")
```

#### Using SentencePiece directly

```python
import sentencepiece as spm

# Load the SentencePiece model
sp = spm.SentencePieceProcessor()
sp.load("m.model")

# Tokenize input text (note: input should be lowercase)
sentence = "this is a multilingual model supporting multiple languages."
tokens = sp.encode(sentence, out_type=str)
print(tokens)
```

---

## Citation

This model was published as part of the research paper:

**"Study on Automatic Punctuation Restoration in Bilingual Broadcast Stream"**  

```
@inproceedings{polacek-2025-study,
    title = "Study on Automatic Punctuation Restoration in Bilingual Broadcast Stream",
    author = "Polacek, Martin",
    editor = "Velichkov, Boris  and
      Nikolova-Koleva, Ivelina  and
      Slavcheva, Milena",
    booktitle = "Proceedings of the 9th Student Research Workshop associated with the International Conference Recent Advances in Natural Language Processing",
    month = sep,
    year = "2025",
    address = "Varna, Bulgaria",
    publisher = "INCOMA Ltd., Shoumen, Bulgaria",
    url = "https://aclanthology.org/2025.ranlp-stud.5/",
    pages = "37--43",
    doi = "10.26615/issn.2603-2821.2025_005"
}

```
---

## Related Models

- **Czech-Slovak**: [AILabTUL/BiELECTRA-czech-slovak](https://huggingface.co/AILabTUL/BiELECTRA-czech-slovak)
- **Norwegian-Swedish**: [AILabTUL/BiELECTRA-norwegian-swedish](https://huggingface.co/AILabTUL/BiELECTRA-norwegian-swedish)