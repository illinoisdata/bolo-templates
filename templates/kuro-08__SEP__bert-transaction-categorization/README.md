---
license: apache-2.0
language:
- en
metrics:
- character
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
---

# Fine-Tuned BERT for Transaction Categorization

This is a fine-tuned [BERT model](https://huggingface.co/transformers/model_doc/bert.html) specifically trained to categorize financial transactions into predefined categories. The model was trained on a dataset of English transaction descriptions to classify them into categories like "Groceries," "Transport," "Entertainment," and more.

## Model Details

- **Base Model**: [bert-base-uncased](https://huggingface.co/bert-base-uncased).
- **Fine-Tuning Task**: Transaction Categorization (multi-class classification).
- **Languages**: English.

### Example Categories
The model classifies transactions into categories such as:
```python
CATEGORIES = {

0: "Utilities",
1: "Health",
2: "Dining",
3: "Travel",
4: "Education",
5: "Subscription",
6: "Family",
7: "Food",
8: "Festivals",
9: "Culture",
10: "Apparel",
11: "Transportation",
12: "Investment",
13: "Shopping",
14: "Groceries",
15: "Documents",
16: "Grooming",
17: "Entertainment",
18: "Social Life",
19: "Beauty",
20: "Rent",
21: "Money transfer",
22: "Salary",
23: "Tourism",
24: "Household",
}
```
---

## How to Use the Model

To use this model, you can load it directly with Hugging Face's `transformers` library:

```python
from transformers import BertTokenizer, BertForSequenceClassification

# Load the model
model_name = "kuro-08/bert-transaction-categorization"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Sample transaction description
transaction = "Transaction: Payment at Starbucks for coffee - Type: income/expense"
inputs = tokenizer(transaction, return_tensors="pt", truncation=True, padding=True)

# Predict the category
outputs = model(**inputs)
logits = outputs.logits
predicted_category = logits.argmax(-1).item()

print(f"Predicted category: {predicted_category}")