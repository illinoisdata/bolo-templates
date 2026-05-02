---
language: 
  - ar
tags:
  - Arabic T5
  - MSA
  - Twitter
  - Arabic Dialect
  - Arabic Machine Translation
  - Arabic Text Summarization
  - Arabic News Title and Question Generation
  - Arabic Paraphrasing and Transliteration
  - Arabic Code-Switched Translation
---
# AraT5v2-base-1024



## What's new?
- **More Data.** `AraT5v2-base-1024` is trained on large and more diverse Arabic data.
- **Larger Sequence Length.** We increase the sequence length from 512 to 1024 in this version.
- **Faster Convergence.** On finetuning process, AraT5v2-base-1024 converges ~10x faster than the previous version (AraT5-base).
- **Extra IDs.**  AraT5v2-base-1024 supports 100 sentinel tokens (a.k.a unique mask tokens).

<span style="color:red"><b>We recommend using AraT5v2-base-1024 instead of the previous version (AraT5-base).</b></span>


## An example of predicted masked token
```python
from transformers import T5Tokenizer, AutoModelForSeq2SeqLM

tokenizer = T5Tokenizer.from_pretrained("UBC-NLP/AraT5v2-base-1024")  
model = AutoModelForSeq2SeqLM.from_pretrained("UBC-NLP/AraT5v2-base-1024")

ar_prompt="عاصمة ألمانيا هي <extra_id_0> "
input_ids = tokenizer(ar_prompt, return_tensors="pt").input_ids
outputs = model.generate(input_ids)
print("Tokenized input:", tokenizer.tokenize(ar_prompt))
print("Decoded output:", tokenizer.decode(outputs[0], skip_special_tokens=True))

```
Output:
```bash
Tokenized input: ['▁عاصمة', '▁ألمانيا', '▁هي', '<extra_id_0>']
Decoded output: برلين
```



# Citation

If you use our models for your scientific publication, or if you find the resources in this repository useful, please cite our papers as follows:

**(AraT5-base, AraT5-msa-base, AraT5-tweet-base, AraT5-msa-small, or AraT5-tweet-small)**
```bibtex
@inproceedings{nagoudi2022_arat5,
@inproceedings{nagoudi-etal-2022-arat5,
    title = "{A}ra{T}5: Text-to-Text Transformers for {A}rabic Language Generation",
    author = "Nagoudi, El Moatez Billah  and
      Elmadany, AbdelRahim  and
      Abdul-Mageed, Muhammad",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.47",
    pages = "628--647",
    abstract = "Transfer learning with a unified Transformer framework (T5) that converts all language problems into a text-to-text format was recently proposed as a simple and effective transfer learning approach. Although a multilingual version of the T5 model (mT5) was also introduced, it is not clear how well it can fare on non-English tasks involving diverse data. To investigate this question, we apply mT5 on a language with a wide variety of dialects{--}Arabic. For evaluation, we introduce a novel benchmark for ARabic language GENeration (ARGEN), covering seven important tasks. For model comparison, we pre-train three powerful Arabic T5-style models and evaluate them on ARGEN. Although pre-trained with {\textasciitilde}49 less data, our new models perform significantly better than mT5 on all ARGEN tasks (in 52 out of 59 test sets) and set several new SOTAs. Our models also establish new SOTA on the recently-proposed, large Arabic language understanding evaluation benchmark ARLUE (Abdul-Mageed et al., 2021). Our new models are publicly available. We also link to ARGEN datasets through our repository: https://github.com/UBC-NLP/araT5.",
}
```
**AraT5v2-base-1024**
``` bibtex
@inproceedings{elmadany-etal-2023-octopus,
    title = "Octopus: A Multitask Model and Toolkit for {A}rabic Natural Language Generation",
    author = "Elmadany, AbdelRahim  and
      Nagoudi, El Moatez Billah  and
      Abdul-Mageed, Muhammad",
    booktitle = "Proceedings of ArabicNLP 2023",
    month = dec,
    year = "2023",
    address = "Singapore (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.arabicnlp-1.20",
    doi = "10.18653/v1/2023.arabicnlp-1.20",
    pages = "232--243",
}
```