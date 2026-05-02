---
tags:
- summarization
- mT5
language:
- am
- ar
- az
- bn
- my
- zh
- en
- fr
- gu
- ha
- hi
- ig
- id
- ja
- rn
- ko
- ky
- mr
- ne
- om
- ps
- fa
- pcm
- pt
- pa
- ru
- gd
- sr
- si
- so
- es
- sw
- ta
- te
- th
- ti
- tr
- uk
- ur
- uz
- vi
- cy
- yo
licenses:
- cc-by-nc-sa-4.0
widget:
- text: >-
    Videos that say approved vaccines are dangerous and cause autism, cancer or
    infertility are among those that will be taken down, the company said.  The
    policy includes the termination of accounts of anti-vaccine influencers. 
    Tech giants have been criticised for not doing more to counter false health
    information on their sites.  In July, US President Joe Biden said social
    media platforms were largely responsible for people's scepticism in getting
    vaccinated by spreading misinformation, and appealed for them to address the
    issue.  YouTube, which is owned by Google, said 130,000 videos were removed
    from its platform since last year, when it implemented a ban on content
    spreading misinformation about Covid vaccines.  In a blog post, the company
    said it had seen false claims about Covid jabs "spill over into
    misinformation about vaccines in general". The new policy covers
    long-approved vaccines, such as those against measles or hepatitis B. 
    "We're expanding our medical misinformation policies on YouTube with new
    guidelines on currently administered vaccines that are approved and
    confirmed to be safe and effective by local health authorities and the WHO,"
    the post said, referring to the World Health Organization.
datasets:
- csebuetnlp/CrossSum
---

# mT5-m2m-CrossSum-enhanced

This repository contains an enhanced many-to-many (m2m) mT5 checkpoint finetuned on all cross-lingual pairs of the [CrossSum](https://huggingface.co/datasets/csebuetnlp/CrossSum) dataset. This model tries to **summarize text written in any language in the provided target language.** For finetuning details and scripts, see the [paper](https://arxiv.org/abs/2112.08804) and the [official repository](https://github.com/csebuetnlp/CrossSum). 


## Using this model in `transformers` (tested on 4.11.0.dev0)

```python
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

article_text = """Videos that say approved vaccines are dangerous and cause autism, cancer or infertility are among those that will be taken down, the company said.  The policy includes the termination of accounts of anti-vaccine influencers.  Tech giants have been criticised for not doing more to counter false health information on their sites.  In July, US President Joe Biden said social media platforms were largely responsible for people's scepticism in getting vaccinated by spreading misinformation, and appealed for them to address the issue.  YouTube, which is owned by Google, said 130,000 videos were removed from its platform since last year, when it implemented a ban on content spreading misinformation about Covid vaccines.  In a blog post, the company said it had seen false claims about Covid jabs "spill over into misinformation about vaccines in general". The new policy covers long-approved vaccines, such as those against measles or hepatitis B.  "We're expanding our medical misinformation policies on YouTube with new guidelines on currently administered vaccines that are approved and confirmed to be safe and effective by local health authorities and the WHO," the post said, referring to the World Health Organization."""

model_name = "csebuetnlp/mT5_m2m_crossSum_enhanced"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

get_lang_id = lambda lang: tokenizer._convert_token_to_id(
    model.config.task_specific_params["langid_map"][lang][1]
) 

target_lang = "english" # for a list of available language names see below

input_ids = tokenizer(
    [WHITESPACE_HANDLER(article_text)],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=512
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    decoder_start_token_id=get_lang_id(target_lang),
    max_length=84,
    no_repeat_ngram_size=2,
    num_beams=4,
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(summary)
```

### Available target language names
-  `amharic`
-  `arabic`
-  `azerbaijani`
-  `bengali`
-  `burmese`
-  `chinese_simplified`
-  `chinese_traditional`
-  `english`
-  `french`
-  `gujarati`
-  `hausa`
-  `hindi`
-  `igbo`
-  `indonesian`
-  `japanese`
-  `kirundi`
-  `korean`
-  `kyrgyz`
-  `marathi`
-  `nepali`
-  `oromo`
-  `pashto`
-  `persian`
-  `pidgin`
-  `portuguese`
-  `punjabi`
-  `russian`
-  `scottish_gaelic`
-  `serbian_cyrillic`
-  `serbian_latin`
-  `sinhala`
-  `somali`
-  `spanish`
-  `swahili`
-  `tamil`
-  `telugu`
-  `thai`
-  `tigrinya`
-  `turkish`
-  `ukrainian`
-  `urdu`
-  `uzbek`
-  `vietnamese`
-  `welsh`
-  `yoruba`



## Citation

If you use this model, please cite the following paper:
```
@article{hasan2021crosssum,
  author    = {Tahmid Hasan and Abhik Bhattacharjee and Wasi Uddin Ahmad and Yuan-Fang Li and Yong-bin Kang and Rifat Shahriyar},
  title     = {CrossSum: Beyond English-Centric Cross-Lingual Abstractive Text Summarization for 1500+ Language Pairs},
  journal   = {CoRR},
  volume    = {abs/2112.08804},
  year      = {2021},
  url       = {https://arxiv.org/abs/2112.08804},
  eprinttype = {arXiv},
  eprint    = {2112.08804}
}
```