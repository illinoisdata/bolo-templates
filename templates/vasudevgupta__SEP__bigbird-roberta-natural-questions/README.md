---
language: en
license: apache-2.0
datasets: natural_questions
widget:
- text: "Who added BigBird to HuggingFace Transformers?"
  context: "BigBird Pegasus just landed! Thanks to Vasudev Gupta, BigBird Pegasus from Google AI is merged into HuggingFace Transformers. Check it out today!!!"
---

This checkpoint is obtained after training `BigBirdForQuestionAnswering` (with extra pooler head) on [`natural_questions`](https://huggingface.co/datasets/natural_questions) dataset for ~ 2 weeks on 2 K80 GPUs. Script for training can be found here: https://github.com/vasudevgupta7/bigbird

| Exact Match | 47.44 |
|-------------|-------|

**Use this model just like any other model from 🤗Transformers**

```python
from transformers import BigBirdForQuestionAnswering

model_id = "vasudevgupta/bigbird-roberta-natural-questions"
model = BigBirdForQuestionAnswering.from_pretrained(model_id)
tokenizer = BigBirdTokenizer.from_pretrained(model_id)
```

In case you are interested in predicting category (null, long, short, yes, no) as well, use `BigBirdForNaturalQuestions` (instead of `BigBirdForQuestionAnswering`) from my training script.