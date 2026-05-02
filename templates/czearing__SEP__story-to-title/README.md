---
license: mit
---

## Story to Title
The model is based on the T5 language model and trained using a large collection of movie descriptions and corresponding titles. When given a story it will generate a corresponding title.

## Usage
Example code:
```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("czearing/story-to-title")
model = AutoModel.from_pretrained("czearing/story-to-title")
```

## License
MIT