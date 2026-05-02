---
language:
- ms
---
# Noisy Translation Small T5

Trained on 1536 context length, able to translate malay, pasar malay (social media texts or local context), english, manglish, javanese, banjarese and indonesian to target language. It also able to maintain the text structure as it is and only translate necessary texts, eg, programming code.

Added more coding translation dataset, noisy b.cari.com.my translation, noisy ChatGPT4 translation and heavy postfilter.

## how-to

```python
from transformers import T5ForConditionalGeneration, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(
    'mesolitica/translation-t5-small-standard-bahasa-cased-v2',
    use_fast=False
)
model = T5ForConditionalGeneration.from_pretrained(
    'mesolitica/translation-t5-small-standard-bahasa-cased-v2'
)
s = 'Hai, ada yang bisa saya bantu?'
input_ids = tokenizer.encode(f'terjemah ke Melayu: {s}', return_tensors = 'pt')
outputs = model.generate(input_ids, max_length = 100)
all_special_ids = [0, 1, 2]
outputs = [i for i in outputs[0] if i not in all_special_ids]
print(tokenizer.decode(outputs, spaces_between_special_tokens = False))
```