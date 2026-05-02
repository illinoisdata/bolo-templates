---
language: 
- bn
licenses:
- cc-by-nc-sa-4.0
---

# banglat5_banglaparaphrase

This repository contains the pretrained checkpoint of the model **BanglaT5** finetuned on [BanglaParaphrase](https://huggingface.co/datasets/csebuetnlp/BanglaParaphrase) dataset. This is a sequence to sequence transformer model pretrained with the ["Span Corruption"]() objective. Finetuned models using this checkpoint achieve    competitive results on the dataset.

For finetuning and inference, refer to the scripts in the official GitHub repository of [BanglaNLG](https://github.com/csebuetnlp/BanglaNLG).

**Note**: This model was pretrained using a specific normalization pipeline available [here](https://github.com/csebuetnlp/normalizer). All finetuning scripts in the official GitHub repository use this normalization by default. If you need to adapt the pretrained model for a different task make sure the text units are normalized using this pipeline before tokenizing to get best results. A basic example is given below:

## Using this model in `transformers`

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize # pip install git+https://github.com/csebuetnlp/normalizer

model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_banglaparaphrase")
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_banglaparaphrase", use_fast=False)

input_sentence = ""
input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
generated_tokens = model.generate(input_ids)
decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]

print(decoded_tokens)
```

## Benchmarks
 
* Supervised fine-tuning

| Test Set | Model | sacreBLEU | ROUGE-L | PINC | BERTScore | BERT-iBLEU |
| -------- | ----- | --------- | ------- | ---- | --------- | ---------- |
| [BanglaParaphrase](https://huggingface.co/datasets/csebuetnlp/BanglaParaphrase) | [BanglaT5](https://huggingface.co/csebuetnlp/banglat5)<br>[IndicBART](https://huggingface.co/ai4bharat/IndicBART)<br>[IndicBARTSS](https://huggingface.co/ai4bharat/IndicBARTSS)| 32.8<br>5.60<br>4.90 | 63.58<br>35.61<br>33.66 | 74.40<br>80.26<br>82.10 | 94.80<br>91.50<br>91.10 | 92.18<br>91.16<br>90.95 |
| [IndicParaphrase](https://huggingface.co/datasets/ai4bharat/IndicParaphrase) |BanglaT5<br>IndicBART<br>IndicBARTSS| 11.0<br>12.0<br>10.7| 19.99<br>21.58<br>20.59| 74.50<br>76.83<br>77.60| 94.80<br>93.30<br>93.10 | 87.738<br>90.65<br>90.54|


The dataset can be found in the link below:
* **[BanglaParaphrase](https://huggingface.co/datasets/csebuetnlp/BanglaParaphrase)**

## Citation

If you use this model, please cite the following paper:
```
@article{akil2022banglaparaphrase,
  title={BanglaParaphrase: A High-Quality Bangla Paraphrase Dataset},
  author={Akil, Ajwad and Sultana, Najrin and Bhattacharjee, Abhik and Shahriyar, Rifat},
  journal={arXiv preprint arXiv:2210.05109},
  year={2022}
}
```