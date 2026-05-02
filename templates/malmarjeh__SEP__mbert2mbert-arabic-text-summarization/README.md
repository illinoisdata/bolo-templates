---
language: 
  - ar
tags:
  - Multilingual BERT
  - BERT2BERT
  - MSA
  - Arabic Text Summarization
  - Arabic News Title Generation
  - Arabic Paraphrasing
---

# An Arabic abstractive text summarization model
A BERT2BERT-based model whose parameters are initialized with mBERT weights and which has been fine-tuned on a dataset of 84,764 paragraph-summary pairs.

Paper: [Arabic abstractive text summarization using RNN-based and transformer-based architectures](https://www.sciencedirect.com/science/article/abs/pii/S0306457322003284).

Dataset: [link](https://data.mendeley.com/datasets/7kr75c9h24/1).

The model can be used as follows:
```python
from transformers import BertTokenizer, AutoModelForSeq2SeqLM, pipeline
from arabert.preprocess import ArabertPreprocessor

model_name="malmarjeh/mbert2mbert-arabic-text-summarization"
preprocessor = ArabertPreprocessor(model_name="")

tokenizer = BertTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
pipeline = pipeline("text2text-generation",model=model,tokenizer=tokenizer)

text = "شهدت مدينة طرابلس، مساء أمس الأربعاء، احتجاجات شعبية وأعمال شغب لليوم الثالث على التوالي، وذلك بسبب تردي الوضع المعيشي والاقتصادي. واندلعت مواجهات عنيفة وعمليات كر وفر ما بين الجيش اللبناني والمحتجين استمرت لساعات، إثر محاولة فتح الطرقات المقطوعة، ما أدى إلى إصابة العشرات من الطرفين."
text = preprocessor.preprocess(text)

result = pipeline(text,
            pad_token_id=tokenizer.eos_token_id,
            num_beams=3,
            repetition_penalty=3.0,
            max_length=200,
            length_penalty=1.0,
            no_repeat_ngram_size = 3)[0]['generated_text']
result
>>> 'احتجاجات في طرابلس على خلفية مواجهات عنيفة بين الجيش اللبناني والمحتجين'
```

## Contact:
<banimarje@gmail.com>