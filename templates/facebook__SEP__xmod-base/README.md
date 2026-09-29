---
language: 
  - multilingual
  - af
  - am
  - ar
  - az
  - be
  - bg
  - bn
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - ga
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - no
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - uk
  - ur
  - uz
  - vi
  - zh
license: mit
---

# xmod-base

X-MOD is a multilingual masked language model trained on filtered CommonCrawl data containing 81 languages. It was introduced in the paper [Lifting the Curse of Multilinguality by Pre-training Modular Transformers](http://dx.doi.org/10.18653/v1/2022.naacl-main.255) (Pfeiffer et al., NAACL 2022) and first released in [this repository](https://github.com/facebookresearch/fairseq/tree/main/examples/xmod).

Because it has been pre-trained with language-specific modular components (_language adapters_), X-MOD differs from previous multilingual models like [XLM-R](https://huggingface.co/xlm-roberta-base). For fine-tuning, the language adapters in each transformer layer are frozen.

# Usage

## Tokenizer
This model reuses the tokenizer of [XLM-R](https://huggingface.co/xlm-roberta-base).

## Input Language
Because this model uses language adapters, you need to specify the language of your input so that the correct adapter can be activated:

```python
from transformers import XmodModel

model = XmodModel.from_pretrained("facebook/xmod-base")
model.set_default_language("en_XX")
```

A directory of the language adapters in this model is found at the bottom of this model card.

## Fine-tuning
In the experiments in the original paper, the embedding layer and the language adapters are frozen during fine-tuning. A method for doing this is provided in the code:

```python
model.freeze_embeddings_and_language_adapters()
# Fine-tune the model ...
```

## Cross-lingual Transfer
After fine-tuning, zero-shot cross-lingual transfer can be tested by activating the language adapter of the target language:
```python
model.set_default_language("de_DE")
# Evaluate the model on German examples ...
```

# Bias, Risks, and Limitations

Please refer to the model card of [XLM-R](https://huggingface.co/xlm-roberta-base), because X-MOD has a similar architecture and has been trained on similar training data.


# Citation

**BibTeX:**

```bibtex
@inproceedings{pfeiffer-etal-2022-lifting,
    title = "Lifting the Curse of Multilinguality by Pre-training Modular Transformers",
    author = "Pfeiffer, Jonas  and
      Goyal, Naman  and
      Lin, Xi  and
      Li, Xian  and
      Cross, James  and
      Riedel, Sebastian  and
      Artetxe, Mikel",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.naacl-main.255",
    doi = "10.18653/v1/2022.naacl-main.255",
    pages = "3479--3495"
}
```

# Languages

This model contains the following language adapters:

| lang_id (Adapter index) | Language code | Language              |
|-------------------------|---------------|-----------------------|
| 0                       | en_XX         | English               |
| 1                       | id_ID         | Indonesian            |
| 2                       | vi_VN         | Vietnamese            |
| 3                       | ru_RU         | Russian               |
| 4                       | fa_IR         | Persian               |
| 5                       | sv_SE         | Swedish               |
| 6                       | ja_XX         | Japanese              |
| 7                       | fr_XX         | French                |
| 8                       | de_DE         | German                |
| 9                       | ro_RO         | Romanian              |
| 10                      | ko_KR         | Korean                |
| 11                      | hu_HU         | Hungarian             |
| 12                      | es_XX         | Spanish               |
| 13                      | fi_FI         | Finnish               |
| 14                      | uk_UA         | Ukrainian             |
| 15                      | da_DK         | Danish                |
| 16                      | pt_XX         | Portuguese            |
| 17                      | no_XX         | Norwegian             |
| 18                      | th_TH         | Thai                  |
| 19                      | pl_PL         | Polish                |
| 20                      | bg_BG         | Bulgarian             |
| 21                      | nl_XX         | Dutch                 |
| 22                      | zh_CN         | Chinese (simplified)  |
| 23                      | he_IL         | Hebrew                |
| 24                      | el_GR         | Greek                 |
| 25                      | it_IT         | Italian               |
| 26                      | sk_SK         | Slovak                |
| 27                      | hr_HR         | Croatian              |
| 28                      | tr_TR         | Turkish               |
| 29                      | ar_AR         | Arabic                |
| 30                      | cs_CZ         | Czech                 |
| 31                      | lt_LT         | Lithuanian            |
| 32                      | hi_IN         | Hindi                 |
| 33                      | zh_TW         | Chinese (traditional) |
| 34                      | ca_ES         | Catalan               |
| 35                      | ms_MY         | Malay                 |
| 36                      | sl_SI         | Slovenian             |
| 37                      | lv_LV         | Latvian               |
| 38                      | ta_IN         | Tamil                 |
| 39                      | bn_IN         | Bengali               |
| 40                      | et_EE         | Estonian              |
| 41                      | az_AZ         | Azerbaijani           |
| 42                      | sq_AL         | Albanian              |
| 43                      | sr_RS         | Serbian               |
| 44                      | kk_KZ         | Kazakh                |
| 45                      | ka_GE         | Georgian              |
| 46                      | tl_XX         | Tagalog               |
| 47                      | ur_PK         | Urdu                  |
| 48                      | is_IS         | Icelandic             |
| 49                      | hy_AM         | Armenian              |
| 50                      | ml_IN         | Malayalam             |
| 51                      | mk_MK         | Macedonian            |
| 52                      | be_BY         | Belarusian            |
| 53                      | la_VA         | Latin                 |
| 54                      | te_IN         | Telugu                |
| 55                      | eu_ES         | Basque                |
| 56                      | gl_ES         | Galician              |
| 57                      | mn_MN         | Mongolian             |
| 58                      | kn_IN         | Kannada               |
| 59                      | ne_NP         | Nepali                |
| 60                      | sw_KE         | Swahili               |
| 61                      | si_LK         | Sinhala               |
| 62                      | mr_IN         | Marathi               |
| 63                      | af_ZA         | Afrikaans             |
| 64                      | gu_IN         | Gujarati              |
| 65                      | cy_GB         | Welsh                 |
| 66                      | eo_EO         | Esperanto             |
| 67                      | km_KH         | Central Khmer         |
| 68                      | ky_KG         | Kirghiz               |
| 69                      | uz_UZ         | Uzbek                 |
| 70                      | ps_AF         | Pashto                |
| 71                      | pa_IN         | Punjabi               |
| 72                      | ga_IE         | Irish                 |
| 73                      | ha_NG         | Hausa                 |
| 74                      | am_ET         | Amharic               |
| 75                      | lo_LA         | Lao                   |
| 76                      | ku_TR         | Kurdish               |
| 77                      | so_SO         | Somali                |
| 78                      | my_MM         | Burmese               |
| 79                      | or_IN         | Oriya                 |
| 80                      | sa_IN         | Sanskrit              |
