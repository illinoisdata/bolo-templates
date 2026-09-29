---
license: mit
datasets:
- RCC-MSU/collection3
language:
- ru
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- cointegrated/rubert-tiny2
pipeline_tag: token-classification
---

# 📰 Ner-rubert-tiny-RuNews

A model for **Named Entity Recognition (NER)** in **Russian-language news texts**.

🔍 Based on [**RuBERT-tiny2**](https://huggingface.co/cointegrated/rubert-tiny2) and fine-tuned on the news corpus [**Collection3**](https://huggingface.co/datasets/RCC-MSU/collection3), focusing on texts mentioning **Sberbank**, **Yandex**, and other media and governmental entities.

---

## 💡 What the model can do

It recognizes the following types of named entities:

| Label      | Meaning                                        |
|------------|------------------------------------------------|
| `PER`      | Persons                                        |
| `ORG`      | Organizations                                  |
| `LOC`      | Locations                                      |
| `GEOPOLIT` | Geopolitical entities (countries, regions)     |
| `MEDIA`    | Media outlets and resources                    |

---


## 🛠️ Example usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

label2id = {
    'O': 0,
    'B-GEOPOLIT': 1, 'I-GEOPOLIT': 2,
    'B-MEDIA': 3,    'I-MEDIA': 4,
    'B-LOC': 5,      'I-LOC': 6,
    'B-ORG': 7,      'I-ORG': 8,
    'B-PER': 9,      'I-PER': 10
}
id2label = {v: k for k, v in label2id.items()}

model_id = "r1char9/ner-rubert-tiny-RuNews"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForTokenClassification.from_pretrained(
    model_id,
    num_labels=len(label2id),
    id2label=id2label,
    label2id=label2id
)

ner_pipeline = pipeline(
    "ner",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple"
)

text = (
    "Генеральный директор Сбербанка Герман Греф на конференции в Москве заявил, "
    "что сотрудничество с Яндексом в области искусственного интеллекта выходит на новый уровень. "
    "Он также отметил, что правительство Российской Федерации поддерживает развитие цифровой экономики, "
    "особенно в рамках Евразийского экономического союза."
)

results = ner_pipeline(text)

for entity in results:
    print(entity)

# {'entity_group': 'ORG', 'score': 0.951569, 'word': 'Сбербанка', 'start': 21, 'end': 30}
# {'entity_group': 'PER', 'score': 0.9922959, 'word': 'Герман Греф', 'start': 31, 'end': 42}
# {'entity_group': 'LOC', 'score': 0.60198957, 'word': 'Москве', 'start': 60, 'end': 66}
# {'entity_group': 'ORG', 'score': 0.6973838, 'word': 'Яндексом', 'start': 96, 'end': 104}
# {'entity_group': 'GEOPOLIT', 'score': 0.9631994, 'word': 'Российской Федерации', 'start': 203, 'end': 223}
# {'entity_group': 'ORG', 'score': 0.85091865, 'word': 'Евразийского экономического союза.', 'start': 284, 'end': 318}
```