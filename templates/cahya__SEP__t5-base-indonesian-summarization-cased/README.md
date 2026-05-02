---
language: id
tags:
- pipeline:summarization
- summarization
- t5
datasets:
- id_liputan6
---

# Indonesian T5 Summarization Base Model

Finetuned T5 base summarization model for Indonesian. 

## Finetuning Corpus

`t5-base-indonesian-summarization-cased` model is based on `t5-base-bahasa-summarization-cased` by [huseinzol05](https://huggingface.co/huseinzol05), finetuned using [id_liputan6](https://huggingface.co/datasets/id_liputan6) dataset.

## Load Finetuned Model

```python
from transformers import T5Tokenizer, T5Model, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("cahya/t5-base-indonesian-summarization-cased")
model = T5ForConditionalGeneration.from_pretrained("cahya/t5-base-indonesian-summarization-cased")
```

## Code Sample

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("cahya/t5-base-indonesian-summarization-cased")
model = T5ForConditionalGeneration.from_pretrained("cahya/t5-base-indonesian-summarization-cased")

# 
ARTICLE_TO_SUMMARIZE = ""

# generate summary
input_ids = tokenizer.encode(ARTICLE_TO_SUMMARIZE, return_tensors='pt')
summary_ids = model.generate(input_ids,
            min_length=20,
            max_length=80,
            num_beams=10,
            repetition_penalty=2.5,
            length_penalty=1.0,
            early_stopping=True,
            no_repeat_ngram_size=2,
            use_cache=True,
            do_sample = True,
            temperature = 0.8,
            top_k = 50,
            top_p = 0.95)

summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(summary_text)
```

Output:

```

```