---
license: apache-2.0
language:
- vi
- zh
metrics:
- bleu
library_name: transformers
pipeline_tag: translation
---
# viT5 for Sino-Vietnamese transliteration

<!-- Provide a quick summary of what the model is/does. -->

Finetuned model from viT5 for Chinese MMORPG translation.

# Model Description

<!-- Provide a longer summary of what this model is. -->

Enhanced version from version 1.0 with larger dataset.

# Uses
### Default
<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
Step 1: Map all Chinese word from original text to Sino-Vietnamese with [map.json](https://huggingface.co/haruyuu/viT5_han-vie_v1.1/blob/main/map.json) file
```python
with open('map.json', encoding = 'utf-8') as f:
    map = json.load(f)
global map

def mapping(text):
    for i in text:
        try:
            x = ' ' + map[i] + ' '
            text = text.replace(i, x)
        except:
            continue
    return text.strip()

input_text = mapping('谁知道 “ 你三更半夜回家发现自己忘记带钥匙，家里又没有其他人在，这时你最大的愿望是什么？ ” 的正确答案是什么呀？')
```
Step 2: Load model and generate
```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained('haruyuu/viT5_han-vie_v1.1')
tokenizer = T5Tokenizer.from_pretrained('haruyuu/viT5_han-vie_v1.1')

input_ids = tokenizer.encode(input_text, return_tensors="pt")
translated_ids = model.generate(input_ids)
translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)

print("Vietnamese Translation:", translated_text) # 'Ai biết, nửa đêm về nhà phát hiện ra mình quên chìa khóa, trong nhà không có ai, lúc này nguyện vọng lớn nhất của ngươi là gì? Đáp án chính xác là gì?'
print("\nTruth:", truth) # 'Ai biết nửa đêm về nhà phát hiện mình quên chìa khoá , trong nhà lại không có ai thì lúc này muốn nhất là cái gì ? Câu trả lời là gì thế anh em ?'
```

### Faster inference on OnnxT5 model
```python
from fastT5 import get_onnx_runtime_sessions, OnnxT5
from transformers import T5Config, AutoTokenizer, T5ForConditionalGeneration

quant_model_paths= tuple(['viT5_han-vie_v1-encoder-quantized.onnx',
                          'viT5_han-vie_v1-decoder-quantized.onnx',
                          'viT5_han-vie_v1-init-decoder-quantized.onnx'])

model_sessions = get_onnx_runtime_sessions(quant_model_paths)
model = OnnxT5('haruyuu/viT5_han-vie_v1.1', model_sessions)

input_text = mapping('谁知道 “ 你三更半夜回家发现自己忘记带钥匙，家里又没有其他人在，这时你最大的愿望是什么？ ” 的正确答案是什么呀？')
input_ids = tokenizer.encode(input_text, return_tensors="pt")
translated_ids = model.generate(input_ids, 
                                     num_beams = 6,
                                     max_length = 512,
                                     bad_words_ids = [[6270]])
translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)

print("Vietnamese Translation:", translated_text) # 'Ai biết, nửa đêm về nhà phát hiện ra mình quên chìa khóa, trong nhà không có ai, lúc này nguyện vọng lớn nhất của ngươi là gì? Đáp án chính xác là gì?'
print("\nTruth:", truth) # 'Ai biết nửa đêm về nhà phát hiện mình quên chìa khoá , trong nhà lại không có ai thì lúc này muốn nhất là cái gì ? Câu trả lời là gì thế anh em ?'
```

# Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

450k rows of system notifications, names and conversations translated from Chinese MMORPG games.