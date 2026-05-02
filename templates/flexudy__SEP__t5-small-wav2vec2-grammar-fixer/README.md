# flexudy-pipe-question-generation-v2
After transcribing your audio with Wav2Vec2, you might be interested in a post processor.

All paragraphs had at most 128 tokens (separated by white spaces)

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "flexudy/t5-small-wav2vec2-grammar-fixer"

tokenizer = T5Tokenizer.from_pretrained(model_name)

model = T5ForConditionalGeneration.from_pretrained(model_name)

sent = """GOING ALONG SLUSHY COUNTRY ROADS AND SPEAKING TO DAMP AUDIENCES IN DRAUGHTY SCHOOL ROOMS DAY AFTER DAY FOR A FORTNIGHT HE'LL HAVE TO PUT IN AN APPEARANCE AT SOME PLACE OF WORSHIP ON SUNDAY MORNING AND HE CAN COME TO US IMMEDIATELY AFTERWARDS"""

input_text = "fix: { " + sent + " } </s>"

input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=256, truncation=True, add_special_tokens=True)

outputs = model.generate(
    input_ids=input_ids,
    max_length=256,
    num_beams=4,
    repetition_penalty=1.0,
    length_penalty=1.0,
    early_stopping=True
)

sentence = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

print(f"{sentence}")
```

INPUT 1:
```
WHEN ARE YOU COMING TOMORROW I AM ASKING BECAUSE OF THE MONEY YOU OWE ME PLEASE GIVE IT TO ME I AM WAITING YOU HAVE BEEN AVOIDING ME SINCE TWO THOUSAND AND THREE
```
OUTPUT 1:
```
When are you coming tomorrow? I am asking because of the money you owe me, please give it to me. I am waiting. You have been avoiding me since 2003.
```

INPUT 2:
```
GOING ALONG SLUSHY COUNTRY ROADS AND SPEAKING TO DAMP AUDIENCES IN DRAUGHTY SCHOOL ROOMS DAY AFTER DAY FOR A FORTNIGHT HE'LL HAVE TO PUT IN AN APPEARANCE AT SOME PLACE OF WORSHIP ON SUNDAY MORNING AND HE CAN COME TO US IMMEDIATELY AFTERWARDS
```

OUTPUT 2:
```
Going along Slushy Country Roads and speaking to Damp audiences in Draughty School rooms day after day for a fortnight, he'll have to put in an appearance at some place of worship on Sunday morning and he can come to us immediately afterwards.
```
I strongly recommend improving the performance via further fine-tuning or by training more examples.
- Possible Quick Rule based improvements: Align the transcribed version and the generated version. If the similarity of two words (case-insensitive) vary by more than some threshold based on some similarity metric (e.g. Levenshtein), then keep the transcribed word.