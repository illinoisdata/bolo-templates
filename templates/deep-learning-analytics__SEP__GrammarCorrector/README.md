## Model description
T5 model trained for Grammar Correction. This model corrects grammatical mistakes in input sentences

### Dataset Description
The T5-base model has been trained on C4_200M dataset. 
### Model in Action 🚀
```
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
model_name = 'deep-learning-analytics/GrammarCorrector'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(torch_device)

def correct_grammar(input_text,num_return_sequences):
  batch = tokenizer([input_text],truncation=True,padding='max_length',max_length=64, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=64,num_beams=num_beams, num_return_sequences=num_return_sequences, temperature=1.5)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text
  
```

### Example Usage
```
text = 'He are moving here.'
print(correct_grammar(text, num_return_sequences=2))
['He is moving here.', 'He is moving here now.']
```

Another example
```
text = 'Cat drinked milk'
print(correct_grammar(text, num_return_sequences=2))
['Cat drank milk.', 'Cat drink milk.']
```

Model Developed by [Priya-Dwivedi](https://www.linkedin.com/in/priyanka-dwivedi-6864362)