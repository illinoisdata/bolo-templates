---
tags:
- generated_from_keras_callback
model-index:
- name: t5-small-medium-title-generation
  results: []
widget:
- text: "summarize: Many financial institutions started building conversational AI, prior to the Covid19 pandemic, as part of a digital transformation initiative. These initial solutions were high profile, highly personalized virtual assistants — like the Erica chatbot from Bank of America. As the pandemic hit, the need changed as contact centers were under increased pressures. As Cathal McGloin of ServisBOT explains in 'how it started, and how it is going,' financial institutions were looking for ways to automate solutions to help get back to 'normal' levels of customer service. This resulted in a change from the 'future of conversational AI' to a real tactical assistant that can help in customer service. Haritha Dev of Wells Fargo, saw a similar trend. Banks were originally looking to conversational AI as part of digital transformation to keep up with the times. However, with the pandemic, it has been more about customer retention and customer satisfaction. In addition, new use cases came about as a result of Covid-19 that accelerated adoption of conversational AI. As Vinita Kumar of Deloitte points out, banks were dealing with an influx of calls about new concerns, like questions around the Paycheck Protection Program (PPP) loans. This resulted in an increase in volume, without enough agents to assist customers, and tipped the scale to incorporate conversational AI. When choosing initial use cases to support, financial institutions often start with high volume, low complexity tasks. For example, password resets, checking account balances, or checking the status of a transaction, as Vinita points out. From there, the use cases can evolve as the banks get more mature in developing conversational AI, and as the customers become more engaged with the solutions. Cathal indicates another good way for banks to start is looking at use cases that are a pain point, and also do not require a lot of IT support. Some financial institutions may have a multi-year technology roadmap, which can make it harder to get a new service started. A simple chatbot for document collection in an onboarding process can result in high engagement, and a high return on investment. For example, Cathal has a banking customer that implemented a chatbot to capture a driver’s license to be used in the verification process of adding an additional user to an account — it has over 85% engagement with high satisfaction. An interesting use case Haritha discovered involved educating customers on financial matters. People feel more comfortable asking a chatbot what might be considered a 'dumb' question, as the chatbot is less judgmental. Users can be more ambiguous with their questions as well, not knowing the right words to use, as chatbot can help narrow things down."
  example_title: "Banking on Bots"
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Model description

This model is [t5-small](https://huggingface.co/t5-small) fine-tuned on the [190k Medium Articles](https://www.kaggle.com/datasets/fabiochiusano/medium-articles) dataset for predicting article titles using the article textual content as input.

There are two versions of the model:
- [t5-small-medium-title-generation](https://huggingface.co/fabiochiu/t5-small-medium-title-generation): trained from [t5-small](https://huggingface.co/t5-small).
- [t5-base-medium-title-generation](https://huggingface.co/fabiochiu/t5-base-medium-title-generation): trained from [t5-base](https://huggingface.co/t5-base).

Visit the [title-generation space](https://huggingface.co/spaces/fabiochiu/title-generation) to try the model with different text generation parameters.

# How to use the model

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
nltk.download('punkt')

tokenizer = AutoTokenizer.from_pretrained("fabiochiu/t5-small-medium-title-generation")
model = AutoModelForSeq2SeqLM.from_pretrained("fabiochiu/t5-small-medium-title-generation")

text = """
Many financial institutions started building conversational AI, prior to the Covid19
pandemic, as part of a digital transformation initiative. These initial solutions
were high profile, highly personalized virtual assistants — like the Erica chatbot
from Bank of America. As the pandemic hit, the need changed as contact centers were
under increased pressures. As Cathal McGloin of ServisBOT explains in “how it started,
and how it is going,” financial institutions were looking for ways to automate
solutions to help get back to “normal” levels of customer service. This resulted
in a change from the “future of conversational AI” to a real tactical assistant
that can help in customer service. Haritha Dev of Wells Fargo, saw a similar trend.
Banks were originally looking to conversational AI as part of digital transformation
to keep up with the times. However, with the pandemic, it has been more about
customer retention and customer satisfaction. In addition, new use cases came about
as a result of Covid-19 that accelerated adoption of conversational AI. As Vinita
Kumar of Deloitte points out, banks were dealing with an influx of calls about new
concerns, like questions around the Paycheck Protection Program (PPP) loans. This
resulted in an increase in volume, without enough agents to assist customers, and
tipped the scale to incorporate conversational AI. When choosing initial use cases
to support, financial institutions often start with high volume, low complexity
tasks. For example, password resets, checking account balances, or checking the
status of a transaction, as Vinita points out. From there, the use cases can evolve
as the banks get more mature in developing conversational AI, and as the customers
become more engaged with the solutions. Cathal indicates another good way for banks
to start is looking at use cases that are a pain point, and also do not require a
lot of IT support. Some financial institutions may have a multi-year technology
roadmap, which can make it harder to get a new service started. A simple chatbot
for document collection in an onboarding process can result in high engagement,
and a high return on investment. For example, Cathal has a banking customer that
implemented a chatbot to capture a driver’s license to be used in the verification
process of adding an additional user to an account — it has over 85% engagement
with high satisfaction. An interesting use case Haritha discovered involved
educating customers on financial matters. People feel more comfortable asking a
chatbot what might be considered a “dumb” question, as the chatbot is less judgmental.
Users can be more ambiguous with their questions as well, not knowing the right
words to use, as chatbot can help narrow things down.
"""

inputs = ["summarize: " + text]

inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, return_tensors="pt")
output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=10, max_length=64)
decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
predicted_title = nltk.sent_tokenize(decoded_output.strip())[0]

print(predicted_title)
# Conversational AI: The Future of Customer Service
```

## Training and evaluation data

The model has been trained on a single epoch spanning about 16000 articles, evaluating on 1000 random articles not used during training.

### Training results

The model has been evaluated on a random dataset split of 1000 articles not used during training and validation.

- Rouge-1: 27.8%
- Rouge-2: 14.9%
- Rouge-L: 26.9%
- Rouge-Lsum: 26.9%
- Average length of the generated titles: 13 tokens (about 9 English words)

### Framework versions

- Transformers 4.18.0
- TensorFlow 2.8.0
- Datasets 2.1.0
- Tokenizers 0.12.1