# XLM-RoBERTa for NER
XLM-RoBERTa finetuned on NER. Check more detail at [TNER repository](https://github.com/asahi417/tner).

## Usage
```
  from transformers import AutoTokenizer, AutoModelForTokenClassification
  
  tokenizer = AutoTokenizer.from_pretrained("asahi417/tner-xlm-roberta-base-uncased-ontonotes5")
  
  model = AutoModelForTokenClassification.from_pretrained("asahi417/tner-xlm-roberta-base-uncased-ontonotes5")
 ```