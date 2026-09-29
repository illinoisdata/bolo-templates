---
license: apache-2.0
language:
- de
- en
- ar
- fr
- hi
- it
- pt
- es
metrics:
- f1
library_name: transformers
widget:
- text: Warum sollte ich 5 Stunden auf den Zug warten?
- text: das Essen ist :)
- text: Erneuter Streik in der S-Bahn.
- text: انا لا احب هذا المكان.
- text: انا اعشق الاكل هنا
- text: This dorms is very small.
- text: I can stay here for the whole day.
- text: J'attends le train depuis 4 heures.
- text: मुझे समझ नहीं आता कि यह जगह ऐसी क्यों है।
- text: "Adoro le bevande qui"
- text: "Quiero volver aquí, es increíble."
---
# Model Name: XLM-RoBERTa-German-Sentiment
## Overview
XLM-RoBERTa-German-Sentiment model is designed to perform Sentiment Analysis for 8 Languages and more specifically German language.\
This model leverages the XLM-RoBERTa architecture, a choice inspired by the superior performance of Facebook's RoBERTa over Google's BERT across numerous benchmarks.\
The decision to use XLM-RoBERTa stems from its multilingual capabilities. Specifically tailored for the German language, this model has been fine-tuned on over 200,000 German-language sentiment analysis samples, more on the training of the model can be found in the [paper](https://drive.google.com/file/d/1xg7zbCPTS3lyKhQlA2S4b9UOYeIj5Pyt/view?usp=drive_link).\
The dataset utilized for training, available at [this GitHub repository](https://github.com/oliverguhr/german-sentiment-lib) this dataset is developed by Oliver Guhr, We extend our gratitude to him for making the dataset open source,the dataset was influential in refining the model's accuracy and responsiveness to the nuances of German sentiment.
Our model and finetuning is based on sentiment analysis model called xlm-t [https://arxiv.org/abs/2104.12250]. 
## Model Details

- **Architecture**: XLM-RoBERTa
- **Performance**: 87% Weighted F1 score .
- **Limitations**: The model is only train and tested on the German language, but can handle the other 8 languages with lower accuracy.

## How to Use
I have developed Python desktop application for the inference at my [repository](https://github.com/ssary/German-Sentiment-Analysis).\
To use this model, you need to install the Hugging Face Transformers library and PyTorch. You can do this using pip:

```bash
pip install torch transformers
```

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
text = "Erneuter Streik in der S-Bahn"
model = AutoModelForSequenceClassification.from_pretrained('ssary/XLM-RoBERTa-German-sentiment')
tokenizer = AutoTokenizer.from_pretrained('ssary/XLM-RoBERTa-German-sentiment')
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    outputs = model(**inputs)
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
sentiment_classes = ['negative', 'neutral', 'positive']
print(sentiment_classes[predictions.argmax()]) # for the class with highest probability
print(predictions) # for each class probability
```

## Acknowledgments

This model was developed by Sary Nasser at HTW-Berlin under supervision of Martin Steinicke.

## References
- Model's GitHub repository: [https://github.com/ssary/German-Sentiment-Analysis](https://github.com/ssary/German-Sentiment-Analysis)
- Oliver Guhr Dataset paper: [Training a Broad-Coverage German Sentiment Classification Model for Dialog
 Systems](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.202.pdf)
- Model architecture: [XLM-T: Multilingual Language Models in Twitter for Sentiment Analysis and Beyond
](https://arxiv.org/abs/2104.12250)