---
language:
- ru
tags:
- spellchecking
- pytorch
- natural language generation
license: mit
metrics:
- precision
- recall
- f1
library_name: transformers
model-index:
- name: sage-fredt5-distilled-95m
  results:
  - task:
      type: text-generation
    dataset:
      type: spellcheck_benchmark
      name: RUSpellRU (spell&punct)
    metrics:
    - name: F1 (spell)
      type: f1_spell
      value: 78.9
      verified: false
    - name: F1 (punct)
      type: f1_punct
      value: 83.6
      verified: false
    - name: F1 (case)
      type: f1_case
      value: 93.5
      verified: false
  - task:
      type: text-generation
    dataset:
      type: spellcheck_benchmark
      name: MultidomainGold (spell&punct)
    metrics:
    - name: F1 (spell)
      type: f1_spell
      value: 73.4
      verified: false
    - name: F1 (punct)
      type: f1_punct
      value: 65
      verified: false
    - name: F1 (case)
      type: f1_case
      value: 77.9
      verified: false
  - task:
      type: text-generation
    dataset:
      type: spellcheck_benchmark
      name: MedSpellchecker (spell&punct)
    metrics:
    - name: F1 (spell)
      type: f1_spell
      value: 64.9
      verified: false
    - name: F1 (punct)
      type: f1_punct
      value: 70
      verified: false
    - name: F1 (case)
      type: f1_case
      value: 68.7
      verified: false
  - task:
      type: text-generation
    dataset:
      type: spellcheck_benchmark
      name: GitHubTypoCorpusRu (spell&punct)
    metrics:
    - name: F1 (spell)
      type: f1_spell
      value: 52.7
      verified: false
    - name: F1 (punct)
      type: f1_punct
      value: 42.1
      verified: false
    - name: F1 (case)
      type: f1_case
      value: 36.3
      verified: false
datasets:
- ai-forever/spellcheck_punctuation_benchmark
---
# sage-fredt5-distilled-95m

![banner](images/sage_banner.jpg)

## Summary

The model corrects spelling and punctuation errors and typos by bringing all the words in the text to the norm of the Russian language.
Corrector is a distilled version of the original model that had been trained based on the [FRED-T5-1.7B](https://huggingface.co/ai-forever/FRED-T5-1.7B) architecture. 
An extensive dataset with “artificial” errors was taken as a training corpus: the corpus was assembled on the basis of the Russian-language Wikipedia and transcripts of Russian-language videos, then typos and spelling errors were automatically introduced into it using the library [SAGE](https://github.com/ai-forever/sage).

## Public references
- [SAGE library announcement](https://youtu.be/yFfkV0Qjuu0), DataFest 2023
- [Paper about synthetic error generation methods](https://www.dialog-21.ru/media/5914/martynovnplusetal056.pdf), Dialogue 2023
- [SAGE EACL 2024 paper](https://aclanthology.org/2024.findings-eacl.10/)


## Examples
| Input | Output |
| --- | --- |
| И не чсно прохожим в этот день непогожйи почему я веселый такйо | И не ясно прохожим в этот день непогожий, почему я весёлый такой? |
| Каждй день воттак делой, и спена балеть нибудет. А вотак каждый день ниделай | Каждый день вот так делай, и спена болеть не будет. А вот так каждый день — ни делай. |
| Основая цель мероприятия  практическая отработка навыков по оказанию помощи гражданам, попавшим в ДТП а также повышение и совершенствование уровня профессиональной подготовки сотрудников МЧС при проведении аварийно-спасательных работ по ликвидации последствий дорожно-транспортных проишествий сокращение временных показателей реагирования. | Основная цель мероприятия - практическая отработка навыков по оказанию помощи гражданам, попавшим в ДТП, а также повышение и совершенствование уровня профессиональной подготовки сотрудников МЧС при проведении аварийно-спасательных работ по ликвидации последствий дорожно-транспортных происшествий, сокращение временных показателей реагирования. |
|  |  |

## Metrics
### Quality
Below are automatic metrics for determining the correctness of the spell checkers. 
We compare our solution with both open automatic spell checkers and the ChatGPT family of models on all four available datasets:
- **RUSpellRU**: texts collected from ([LiveJournal](https://www.livejournal.com/media)), with manually corrected typos and errors;
- **MultidomainGold**: examples from 7 text sources, including the open web, news, social media, reviews, subtitles, policy documents and literary works;
- **MedSpellChecker**: texts with errors from medical anamnesis;
- **GitHubTypoCorpusRu**: spelling errors and typos in commits from [GitHub](https://github.com);

**RUSpellRU**
| Model | Pr. (spell) | Rec. (spell) | F1 (spell) | Pr. (punc) | Rec. (punc) | F1 (punc) | Pr. (case) | Rec. (case) | F1 (case) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| sage-fredt5-distilled-95m | 83.5 | 74.8 | 78.9 | 86.8 | 80.6 | 83.6 | 94.4 | 92.5 | 93.5 |
| sage-ai-service | 90.3 | 86.3 | 88.2 | 90.3 | 86.6 | 88.4 | 95.2 | 95.9 | 95.6 |
| gpt-3.5-turbo | 33.6 | 58.5 | 42.7 | 85.9 | 64.6 | 73.7 | 84.9 | 73.9 | 79.0 |
| gpt-4 | 54.9 | 76.7 | 64.0 | 84.0 | 82.3 | 83.2 | 91.5 | 90.2 | 90.9 |


**MultidomainGold**
| Model | Pr. (spell) | Rec. (spell) | F1 (spell) | Pr. (punc) | Rec. (punc) | F1 (punc) | Pr. (case) | Rec. (case) | F1 (case) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| sage-fredt5-distilled-95m | 77.2 | 69.9 | 73.4 | 66.8 | 63.4 | 65.0 | 76.8 | 79.1 | 77.9 |
| sage-ai-service | 81.6 | 77.7 | 79.6 | 70.2 | 67.5 | 68.8 | 80.5 | 80.5 | 80.5 |
| gpt-3.5-turbo | 18.8 | 48.1 | 27.1 | 42.0 | 31.8 | 36.2 | 47.1 | 51.3 | 49.1 |
| gpt-4 | 25.4 | 68.0 | 37.0 | 57.8 | 54.3 | 56.0 | 54.0 | 67.5 | 60.0 |


**MedSpellChecker**
| Model | Pr. (spell) | Rec. (spell) | F1 (spell) | Pr. (punc) | Rec. (punc) | F1 (punc) | Pr. (case) | Rec. (case) | F1 (case) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| sage-fredt5-distilled-95m | 65.1 | 64.8 | 64.9 | 78.6 | 63.1 | 70.0 | 63.5 | 74.7 | 68.7 |
| sage-ai-service | 71.3 | 73.5 | 72.4 | 75.1 | 69.2 | 72.0 | 80.9 | 72.8 | 76.6|
| gpt-3.5-turbo | 14.7 | 45.9 | 22.3 | 69.9 | 52.3 | 59.8 | 26.4 | 41.8 | 32.3 |
| gpt-4 | 37.8 | 72.3 | 49.6 | 81.4 | 64.3 | 71.9 | 73.0 | 62.1 | 67.1 |


**GitHubTypoCorpusRu**
| Model | Pr. (spell) | Rec. (spell) | F1 (spell) | Pr. (punc) | Rec. (punc) | F1 (punc) | Pr. (case) | Rec. (case) | F1 (case) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| sage-fredt5-distilled-95m | 57.8 | 48.5 | 52.7 | 45.2 | 39.5 | 42.1 | 29.9 | 46.2 | 36.3 |
| sage-ai-service | 70.8 | 56.3 | 62.7 | 48.9 | 35.8 | 41.4 | 32.9 | 45.3 | 38.1|
| gpt-3.5-turbo | 23.7 | 38.7 | 29.4 | 37.6 | 23.3 | 28.7 | 19.6 | 35.9 | 25.3 |
| gpt-4 | 27.0 | 52.8 | 35.7 | 45.9 | 32.6 | 38.2 | 25.7 | 36.8 | 30.2 |


## How to use
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("ai-forever/sage-fredt5-distilled-95m")
model = AutoModelForSeq2SeqLM.from_pretrained("ai-forever/sage-fredt5-distilled-95m")

model.to("cuda")

sentence = "И не чсно прохожим в этот день непогожйи почему я веселый такйо"
inputs = tokenizer(sentence, max_length=None, padding="longest", truncation=False, return_tensors="pt")
outputs = model.generate(**inputs.to(model.device), max_length = inputs["input_ids"].size(1) * 1.5)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

# ["И не ясно прохожим в этот день непогожий, почему я весёлый такой?"]

```

## Limitations
- Complex formatting may cause some trouble in output generation.

## Resources
- [SAGE library](https://github.com/ai-forever/sage), GitHub
- [sage-fredt5-large](https://huggingface.co/ai-forever/sage-fredt5-large), HuggingFace
- [sage-fredt5-distilled-95m](https://huggingface.co/ai-forever/sage-fredt5-distilled-95m), HuggingFace
- [sage-m2m100-1.2B](https://huggingface.co/ai-forever/sage-m2m100-1.2B), HuggingFace
- [sage-mt5-large](https://huggingface.co/ai-forever/sage-mt5-large), HuggingFace

## License
Model [FRED-T5-1.7B](https://huggingface.co/ai-forever/FRED-T5-1.7B), on the basis of which our solution is made, and its source code are supplied under the MIT license. 
Our solution comes with MIT license also.

## Specifications
- File size: 0.383 Gb;
- Framework: pytorch
- Version: v1.0
- Developer: SberDevices, AGI NLP

## Contacts
nikita.martynov.98@list.ru