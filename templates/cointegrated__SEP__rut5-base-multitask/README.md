---
language: ["ru", "en"]
tags:
- russian
license: mit
widget:
- text: "fill | Почему они не ___ на меня?"
---
This is a smaller version of the [google/mt5-base](https://huggingface.co/google/mt5-base) with only some Rusian and English embeddings left. 

More details are given in a Russian post: https://habr.com/ru/post/581932/

The model has been fine-tuned for several tasks with sentences or short paragraphs:
* translation (`translate ru-en` and `translate en-ru`)
* Paraphrasing (`paraphrase`)
* Filling gaps in a text (`fill`). The gaps can be denoted as `___` or `_3_`, where `3` is the approximate number of words that should be inserted.
* Restoring the text from a noisy bag of words (`assemble`)
* Simplification of texts (`simplify`)
* Dialogue response generation (`reply` based on fiction and `answer` based on online forums)
* Open-book question answering (`comprehend`)
* Asking questions about a text (`ask`)
* News title generation (`headline`)

For each task, the task name is joined with the input text by the ` | ` separator.

The model can be run with the following code:
```
# !pip install transformers sentencepiece
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
tokenizer = T5Tokenizer.from_pretrained("cointegrated/rut5-base-multitask")
model = T5ForConditionalGeneration.from_pretrained("cointegrated/rut5-base-multitask")

def generate(text, **kwargs):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5, **kwargs)
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)
```

The model can be applied to each of the pretraining tasks:

```
print(generate('translate ru-en | Каждый охотник желает знать, где сидит фазан.'))
# Each hunter wants to know, where he is.

print(generate('paraphrase | Каждый охотник желает знать, где сидит фазан.', 
               encoder_no_repeat_ngram_size=1, repetition_penalty=0.5, no_repeat_ngram_size=1))
# В любом случае каждый рыбак мечтает познакомиться со своей фермой

print(generate('fill | Каждый охотник _3_, где сидит фазан.'))
# смотрит на озеро

print(generate('assemble | охотник каждый знать фазан сидит'))
# Каждый охотник знает, что фазан сидит.

print(generate('simplify | Местным продуктом-специалитетом с защищённым географическим наименованием по происхождению считается люнебургский степной барашек.', max_length=32))
# Местным продуктом-специалитетом считается люнебургский степной барашек.

print(generate('reply | Помогите мне закадрить девушку'))
# Что я хочу?

print(generate('answer | Помогите мне закадрить девушку'))
# я хочу познакомиться с девушкой!!!!!!!!

print(generate("comprehend | На фоне земельного конфликта между владельцами овец и ранчеро разворачивается история любви овцевода Моргана Лейна, "
    "прибывшего в США из Австралии, и Марии Синглетон, владелицы богатого скотоводческого ранчо. Вопрос: откуда приехал Морган?"))
# из Австралии

print(generate("ask | На фоне земельного конфликта между владельцами овец и ранчеро разворачивается история любви овцевода Моргана Лейна, "
    "прибывшего в США из Австралии, и Марии Синглетон, владелицы богатого скотоводческого ранчо.", max_length=32))
# Что разворачивается на фоне земельного конфликта между владельцами овец и ранчеро?

print(generate("headline | На фоне земельного конфликта между владельцами овец и ранчеро разворачивается история любви овцевода Моргана Лейна, "
    "прибывшего в США из Австралии, и Марии Синглетон, владелицы богатого скотоводческого ранчо.", max_length=32))
# На фоне земельного конфликта разворачивается история любви овцевода Моргана Лейна и Марии Синглетон
```

However, it is strongly recommended that you fine tune the model for your own task.