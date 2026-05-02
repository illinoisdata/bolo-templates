---
license: mit
language:
- ru
tags:
- spellchecking
- NLP
- M2M100
- pytorch
- natural language generation
---

# RuM2M100-418M model

### Summary
The model corrects spelling errors and typos by bringing all the words in the text to the norm of the Russian language.
The proofreader was trained based on the [M2M100-418M](https://huggingface.co/facebook/m2m100_418M) model. 
An extensive dataset with “artificial” errors was taken as a training corpus: the corpus was assembled on the basis of the Russian-language Wikipedia and transcripts of Russian-language videos, then typos and spelling errors were automatically introduced into it using the functionality of the [SAGE library](https://github.com/ai-forever/sage).

### Public references
- [SAGE library announcement](https://youtu.be/yFfkV0Qjuu0), DataFest 2023
- [Paper about synthetic error generation methods](https://www.dialog-21.ru/media/5914/martynovnplusetal056.pdf), Dialogue 2023
- [Paper about SAGE and our best solution](https://arxiv.org/abs/2308.09435), Review EACL 2024

### Examples
| Input | Output |
| --- | --- |
| Думю ешцъа лет череа 10 ретроспективно просматривотьэ то будкетцц мне невероя тна ин те р но | Думаю, еш цъа лет через 10 ретроспективно просматривать, що буде ТЦ. Мне невероятна нтерно. |
| Основая цель мероприятия - практическая отработка навыков по оказанию помощи гражданам, попавшим в ДТП, а также повышение и совершенствование уровня профессиональной подготовки сотрудников МЧС при проведении аварийно-спасательных работ по ликвидации последствий дорожно-транспортных проишествий, сокращение временных показателей реагирования. | Основная цель мероприятия - практическая отработка навыков по оказанию помощи гражданам, попавшим в ДТП, а также повышение и совершенствование уровня профессиональной подготовки сотрудников МЧС при проведении аварийно-спасательных работ по ликвидации последствий дорожно-транспортных происшествий, сокращение временных показателей реагирования. |
| прийдя в МГТУ я был удивлен никого необноружив там… | прийдя в МГТУ я был удивлен никого не обнаружив там... |

## Metrics
### Quality
Below are automatic metrics for determining the correctness of the spell checkers. 
We compare our solution with both open automatic spell checkers and the ChatGPT family of models on all four available datasets:
- **RUSpellRU**: texts collected from ([LiveJournal](https://www.livejournal.com/media)), with manually corrected typos and errors;
- **MultidomainGold**: examples from 7 text sources, including the open web, news, social media, reviews, subtitles, policy documents and literary works;
- **MedSpellChecker**: texts with errors from medical anamnesis;
- **GitHubTypoCorpusRu**: spelling errors and typos in commits from [GitHub](https://github.com);

**RUSpellRU**
| Model | Precision | Recall | F1 |
| --- | --- | --- | --- |
| M2M100-418M | 57.7 | 61.2 | 59.4 |
| ChatGPT gpt-3.5-turbo-0301 | 55.8 | 75.3 | 64.1 |
| ChatGPT gpt-4-0314 | 57.0 | 75.9 | 63.9 |
| ChatGPT text-davinci-003 | 55.9 | 75.3 | 64.2 |
| Yandex.Speller | 83.0 | 59.8 | 69.5 |
| JamSpell | 42.1 | 32.8 | 36.9 |
| HunSpell | 31.3 | 34.9 | 33.0 |

**MultidomainGold**
| Model | Precision | Recall | F1 |
| --- | --- | --- | --- |
| M2M100-418M | 32.8 | 56.3 | 41.5 |
| ChatGPT gpt-3.5-turbo-0301 | 33.8 | 72.1 | 46.0 |
| ChatGPT gpt-4-0314 | 34.0 | 73.2 | 46.4 |
| ChatGPT text-davinci-003 | 33.6 | 72.0 | 45.8 |
| Yandex.Speller | 52.9 | 51.4 | 52.2 |
| JamSpell | 25.7 | 30.6 | 28.0 |
| HunSpell | 16.2 | 40.1 | 23.0 |

**MedSpellChecker**
| Модель | Precision | Recall | F1 |
| --- | --- | --- | --- |
| M2M100-418M | 23.2 | 64.5 | 34.1 |
| ChatGPT gpt-3.5-turbo-0301 | 53.2 | 67.6 | 59.6 |
| ChatGPT gpt-4-0314 | 54.2 | 69.4 | 60.9 |
| ChatGPT text-davinci-003 | 47.8 | 68.4 | 56.3 |
| Yandex.Speller | 80.6 | 47.8 | 60.0 |
| JamSpell | 24.6 | 29.7 | 26.9 |
| HunSpell | 10.3 | 40.2 | 16.4 |

**GitHubTypoCorpusRu**
| Модель | Precision | Recall | F1 |
| --- | --- | --- | --- |
| M2M100-418M | 27.5 | 42.6 | 33.4 |
| ChatGPT gpt-3.5-turbo-0301 | 43.8 | 57.0 | 49.6 |
| ChatGPT gpt-4-0314 | 45.2 | 58.2 | 51.0 |
| ChatGPT text-davinci-003 | 46.5 | 58.1 | 51.7 |
| Yandex.Speller | 67.7 | 37.5 | 48.3 |
| JamSpell | 49.5 | 29.9 | 37.3 |
| HunSpell | 28.5 | 30.7 | 29.6 |

## How to use
```python
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

path_to_model = "ai-forever/RuM2M100-418M"

model = M2M100ForConditionalGeneration.from_pretrained(path_to_model)
tokenizer = M2M100Tokenizer.from_pretrained(path_to_model, src_lang="ru", tgt_lang="ru")

sentence = "прийдя в МГТУ я был удивлен никого необноружив там…"

encodings = tokenizer(sentence, return_tensors="pt")
generated_tokens = model.generate(
        **encodings, forced_bos_token_id=tokenizer.get_lang_id("ru"))
answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(answer)

# ["прийдя в МГТУ я был удивлен никого не обнаружив там..."]
```

## Resources
- [SAGE library](https://github.com/ai-forever/sage), GitHub
- [ruM2M100-1.2B](https://huggingface.co/ai-forever/RuM2M100-1.2B), HuggingFace
- [ruM2M100-418M](https://huggingface.co/ai-forever/RuM2M100-420M), HuggingFace
- [FredT5-large-spell](https://huggingface.co/ai-forever/FRED-T5-large-spell), HuggingFace
- [T5-large-spell](https://huggingface.co/ai-forever/T5-large-spell), HuggingFace

## License
Model [M2M100-418M](https://huggingface.co/facebook/m2m100_418M), on the basis of which our solution is made, and its source code are supplied under the MIT open license. 
Our solution also comes with MIT license.

## Specifications
- File size: 2 Gb;
- Framework: pytorch
- Format: AI Service
- Version: v1.0
- Developer: SberDevices, AGI NLP

## Contacts
nikita.martynov.98@list.ru