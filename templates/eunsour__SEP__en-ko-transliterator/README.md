---
license: apache-2.0
language:
- en
- ko
tags:
- transliteration
- multilingual
---
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def transliteration(word: str):
    model_checkpoint = "eunsour/en-ko-transliterator"
    
    model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, src_lang="en", tgt_lang="ko")
    
    encoded_en = tokenizer(word, truncation=True, max_length=48, return_tensors="pt")
    generated_tokens = model.generate(**encoded_en)
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
    return result

transliteration("transformer")
# ['트랜스포머']
```