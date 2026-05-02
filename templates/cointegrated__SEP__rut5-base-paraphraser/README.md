---
language: ["ru"]
tags:
- russian
- paraphrasing
- paraphraser
- paraphrase
license: mit
widget:
- text: "Каждый охотник желает знать, где сидит фазан."
datasets:
- cointegrated/ru-paraphrase-NMT-Leipzig
---

This is a paraphraser for Russian sentences described [in this Habr post](https://habr.com/ru/post/564916/). 

It is recommended to use the model with the `encoder_no_repeat_ngram_size` argument:
```
from transformers import T5ForConditionalGeneration, T5Tokenizer
MODEL_NAME = 'cointegrated/rut5-base-paraphraser'
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model.cuda();
model.eval();

def paraphrase(text, beams=5, grams=4, do_sample=False):
    x = tokenizer(text, return_tensors='pt', padding=True).to(model.device)
    max_size = int(x.input_ids.shape[1] * 1.5 + 10)
    out = model.generate(**x, encoder_no_repeat_ngram_size=grams, num_beams=beams, max_length=max_size, do_sample=do_sample)
    return tokenizer.decode(out[0], skip_special_tokens=True)

print(paraphrase('Каждый охотник желает знать, где сидит фазан.'))
# Все охотники хотят знать где фазан сидит.
```