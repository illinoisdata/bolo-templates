---
library_name: transformers
tags: []
---

# Article Summarizer
The Article Summarizer is a fine-tuned version of the Facebook BART Large CNN model, specifically optimized for generating more 
detailed and informative news summaries. Unlike the base BART Large CNN model, which produces extremely short 
and sometimes disjointed summaries, this model has been fine-tuned to provide more comprehensive and contextually rich summaries.

- **Developed by:** Sarah Yoon
- **Model type:** Summarization
- **Language(s) (NLP):** English
- **Finetuned from model:** facebook/bart-large-cnn

### Model Sources 

The model was trained on a diverse set of news articles to improve its summarization capabilities. The datasets used include:

  1) Steven Devoe's News Article Summary Dataset - https://huggingface.co/datasets/stevendevoe/news-article-summary

  2) TheraPara's Summary of News Articles Dataset - https://huggingface.co/datasets/therapara/summary-of-news-articles

  3) Pranjal Jaiswal's Arrowhead BBC News Summary Dataset - https://huggingface.co/datasets/pranjaljaiswal/arrowhead-bbc-news-summary

  4) Kaggle News Summary Dataset - https://www.kaggle.com/datasets/sunnysai12345/news-summary