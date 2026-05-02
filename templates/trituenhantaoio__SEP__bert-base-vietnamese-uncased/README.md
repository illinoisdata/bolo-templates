## Usage
```python
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
model = BertForSequenceClassification.from_pretrained("trituenhantaoio/bert-base-vietnamese-uncased")
tokenizer = BertTokenizer.from_pretrained("trituenhantaoio/bert-base-vietnamese-uncased")
```

### References

```
@article{ttnt2020bert,
  title={Vietnamese BERT: Pretrained on News and Wiki},
  author={trituenhantao.io},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/trituenhantaoio/vn-bert-base-uncased}},
}
```

[trituenhantao.io](https://trituenhantao.io)