---
language:
- he
pipeline_tag: summarization
---


```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, SummarizationPipeline


model_name = "imvladikon/het5_summarization"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
summarizer = SummarizationPipeline(model=model, tokenizer=tokenizer)
```      
     
example     
```python
text = """
צרפת ממשיכה לבעור: לאחר ארבעה ימים של עימותים אלימים בין מתפרעים לכוחות הביטחון בכל רחבי צרפת, היום (שבת) התקיימה הלוויתו של הנער האלג'יראי, נאהל בן ה-17, שנורה למוות על ידי שוטר לאחר שנחשד בגניבת רכב. לבקשת משפחתו, ההלוויה התקיימה כאירוע מצומצמם שבו השתתפו בני משפחה וחברים בלבד. לאחר שארונו של נאהל הוצא מהמסגד בעיר נאנטר, אלפים קראו "לעשיית צדק עבורו".במקביל, המשטרה הצרפתית נערכת להמשך המהומות בעשרות מוקדים ברחבי המדינה, כשבמהלך הלילה נעצרו 1,300 בני אדם. משרד הפנים הצרפתי הודיע כי במהלך האירועים הוצתו 1,350 כלי רכב, ו-234 הצתות של מבנים. כמו כן, על פי הנתונים נגרם נזק ל-200 מרכזי קניות, 200 סופרמרקטים ו-250 סניפי בנק.
""".strip()
summarizer(text,
           max_length=50,
           num_beams=4,
           no_repeat_ngram_size=2,
           early_stopping=True)[0]["summary_text"]
#לאחר ארבעה ימים של עימותים אלימים בין מתפרעים לכוחות הביטחון בכל רחבי צרפת, הלוויתו של נאהל בן ה-17 התקיימה כאירוע מצומצם
```