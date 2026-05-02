---
license: mit
language:
- en
tags:
- spellchecking
- NLP
- T5
- pytorch
- natural language generation
---

# T5-large-spell model

### Summary
The model corrects spelling errors and typos by bringing all words in the text to the standard English language.
The proofreader was trained based on the [T5-large](https://huggingface.co/t5-large) model. 
An extensive dataset with “artificial” errors was taken as a training corpus: the corpus was assembled on the basis of the English-language Wikipedia and News blogs, then typos and spelling errors were automatically introduced into it using the functionality of the [SAGE library](https://github.com/ai-forever/sage).

### Public references
- [SAGE library announcement](https://youtu.be/yFfkV0Qjuu0), DataFest 2023
- [Paper about synthetic error generation methods](https://www.dialog-21.ru/media/5914/martynovnplusetal056.pdf), Dialogue 2023
- [Paper about SAGE and our best solution](https://arxiv.org/abs/2308.09435), Review EACL 2024

### Examples
| Input | Output |
| --- | --- |
| Th festeivаl was excelzecnt in many ways, and in particular it beinganinternational festjival sss a chаllenging, bet brilli an t ea. | The festival was excellent in many ways, and in particular it beinganinternational festival is a challenging, but brilliant one to see. |
| That 's why I believe in the solution which is the closest to human nature and can help us to avoid boredome. I am sure that eventually we will take off our clothes and in the future we will be undressed and free. There wo n't be any problem with being up - do - date . | That's why I believe in the solution which is the closest to human nature and can help us to avoid boredom. I am sure that eventually we will take off our clothes and in the future we will be undressed and free. There won't be any problem with being up - do - date. |
| If you bought something goregous, you well be very happy. | If you bought something gorgeous, you will be very happy. |

## Metrics
### Quality
Below are automatic metrics for determining the correctness of the spell checkers. 
We present a comparison of our solution both with open automatic spell checkers and with the ChatGPT family of models on two available datasets:
- **BEA60K**: English spelling errors collected from several domains;
- **JFLEG**: 1601 sentences in English, which contain about 2 thousand spelling errors;

**BEA60K**
| Model | Precision | Recall | F1 |
| --- | --- | --- | --- |
| T5-large-spell | 66.5 | 83.1 | 73.9 |
| ChatGPT gpt-3.5-turbo-0301 | 66.9 | 84.1 | 74.5 |
| ChatGPT gpt-4-0314 | 68.6 | 85.2 | 76.0 |
| ChatGPT text-davinci-003 | 67.8 | 83.9 | 75.0 |
| Bert (https://github.com/neuspell/neuspell) | 65.8 | 79.6 | 72.0 |
| SC-LSTM (https://github.com/neuspell/neuspell) | 62.2 | 80.3 | 72.0 |

**JFLEG**
| Model | Precision | Recall | F1 |
| --- | --- | --- | --- |
| T5-large-spell | 83.4 | 84.3 | 83.8 |
| ChatGPT gpt-3.5-turbo-0301 | 77.8 | 88.6 | 82.9 |
| ChatGPT gpt-4-0314 | 77.9 | 88.3 | 82.8 |
| ChatGPT text-davinci-003 | 76.8 | 88.5 | 82.2 |
| Bert (https://github.com/neuspell/neuspell) | 78.5 | 85.4 | 81.8 |
| SC-LSTM (https://github.com/neuspell/neuspell) | 80.6 | 86.1 | 83.2 |

## How to use
```python
from transformers import T5ForConditionalGeneration, AutoTokenizer

path_to_model = "ai-forever/T5-large-spell"

model = T5ForConditionalGeneration.from_pretrained(path_to_model)
tokenizer = AutoTokenizer.from_pretrained(path_to_model)
prefix = "grammar: "

sentence = "If you bought something goregous, you well be very happy."
sentence = prefix + sentence

encodings = tokenizer(sentence, return_tensors="pt")
generated_tokens = model.generate(**encodings)
answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(answer)

# ["If you bought something gorgeous, you will be very happy."]
```

## Resources
- [SAGE library](https://github.com/ai-forever/sage), GitHub
- [ruM2M100-1.2B](https://huggingface.co/ai-forever/RuM2M100-1.2B), HuggingFace
- [ruM2M100-418M](https://huggingface.co/ai-forever/RuM2M100-420M), HuggingFace
- [FredT5-large-spell](https://huggingface.co/ai-forever/FRED-T5-large-spell), HuggingFace
- [T5-large-spell](https://huggingface.co/ai-forever/T5-large-spell), HuggingFace

## License
The [T5-large](https://huggingface.co/t5-large) model, on which our solution is based, and its source code are supplied under the APACHE-2.0 license. 
Our solution is supplied under MIT license.

## Specifications
- File size: 3 Gb;
- Framework: pytorch
- Format: AI Service
- Version: v1.0
- Developer: SberDevices, AGI NLP

## Contacts
nikita.martynov.98@list.ru