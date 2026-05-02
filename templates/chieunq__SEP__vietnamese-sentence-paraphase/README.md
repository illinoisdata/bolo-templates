---
language:
- vi
tags:
- vi-T5
- paraphase
- sentence-paraphase
---
This is tool for paraphase Vietnamese sentence. 
### How to run
For more details, do check out [our Github repo](https://github.com/nqchieutb01/vietnamese-sentence-paraphase). 

```python
CKPT = 'chieunq/vietnamese-sentence-paraphase'
from transformers import MT5Tokenizer, MT5ForConditionalGeneration
tokenizer = MT5Tokenizer.from_pretrained(CKPT)
model = MT5ForConditionalGeneration.from_pretrained(CKPT)
def paraphase(text):
    inputs = tokenizer(text, padding='longest', max_length=64, return_tensors='pt')
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=64)
    return tokenizer.decode(output[0], skip_special_tokens=True)

texts = [
        "Thật tự hào khi là sinh viên trường Đại học Công nghệ",
        "Cách kiếm nhiều tiền ?",
        "Những nguyên lí cơ bản của vật lý ?",
        "Làm thế nào để học ngôn ngữ Java",
        "Ngoài ra, nắng nóng còn có thể gây tình trạng mất nước, kiệt sức, đột qụy do sốc nhiệt đối với cơ thể người khi tiếp xúc lâu với nền nhiệt độ cao."
        ]
for text in texts:
    print(f'Input: {text}')
    print(f'Output: {paraphase(text)}')
    print('-'*100)

```
### Output
```
Input: Thật tự hào khi là sinh viên trường Đại học Công nghệ
Output: Là sinh viên Đại học Công nghệ, tôi rất tự hào về điều đó.
----------------------------------------------------------------------------------------------------
Input: Cách kiếm nhiều tiền ?
Output: Một số cách để kiếm được nhiều tiền là gì?
----------------------------------------------------------------------------------------------------
Input: Những nguyên lí cơ bản của vật lý ?
Output: Các nguyên tắc cơ bản của vật lý là gì?
----------------------------------------------------------------------------------------------------
Input: Làm thế nào để học ngôn ngữ Java
Output: Các bước để thành thạo ngôn ngữ Java là gì?
----------------------------------------------------------------------------------------------------
Input: Ngoài ra, nắng nóng còn có thể gây tình trạng mất nước, kiệt sức, đột qụy do sốc nhiệt đối với cơ thể người khi tiếp xúc lâu với nền nhiệt độ cao.
Output: Hơn nữa, nắng nóng có thể dẫn đến mất nước, kiệt sức, đột quỵ do sốc nhiệt đối với cơ thể người khi tiếp xúc lâu với nền nhiệt độ cao.
----------------------------------------------------------------------------------------------------
```