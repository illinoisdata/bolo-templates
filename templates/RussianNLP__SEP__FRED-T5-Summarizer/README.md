---
license: mit
language:
- ru
pipeline_tag: summarization
---
# FRED-T5 1.7B Summarizer

The model was trained by [SberDevices](https://sberdevices.ru/). 

The model is trained on a mix of open summarisation data [RussianNLP/Mixed-Summarization-Dataset](https://huggingface.co/datasets/RussianNLP/Mixed-Summarization-Dataset) for the Russian language and use prefix tokenen '\<LM\>'

## Usage
```python
import torch
from transformers import GPT2Tokenizer, T5ForConditionalGeneration 
tokenizer = GPT2Tokenizer.from_pretrained('RussianNLP/FRED-T5-Summarizer',eos_token='</s>')
model = T5ForConditionalGeneration.from_pretrained('RussianNLP/FRED-T5-Summarizer')
device='cuda'
model.to(device)

input_text='<LM> Сократи текст.\n В деревне, затерянной среди зелёных холмов, жил старик по имени Иван. Его жизнь протекала медленно и размеренно. Каждое утро Иван выходил на поля, чтобы заботиться о своём скромном участке земли. Он выращивал картофель и морковь, которые были его главным источником пищи. Вечера старик проводил у камина, читая книги и вспоминая молодость. Жизнь в деревне была тяжёлая, но Иван находил в ней простые радости.'
input_ids=torch.tensor([tokenizer.encode(input_text)]).to(device)
outputs=model.generate(input_ids,eos_token_id=tokenizer.eos_token_id,
                    num_beams=5,
                    min_new_tokens=17,
                    max_new_tokens=200,
                    do_sample=True,
                    no_repeat_ngram_size=4,
                    top_p=0.9)
print(tokenizer.decode(outputs[0][1:]))

# print result: Старик Иван живёт размеренной жизнью в деревне, выращивая овощи и находя радость в простых вещах.

```

# Authors
+ Sber Devices:
  + Albina Akhmetgareeva
  + Ilia Kuleshov 
  + Vlad Leschuk 
  + Alexander Abramov
  + Alena Fenogenova

# Cite us
```
@misc{akhmetgareeva2024summary,
      title={Towards Russian Summarization: can architecture solve data limitations problems?}, 
      author={Albina Akhmetgareeva and Ilia Kuleshov and Vlad Leschuk and Alexander Abramov and Alena Fenogenova},
      year={2024},
}
```