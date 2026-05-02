# TUNiB-Electra
  
We release several new versions of the [ELECTRA](https://arxiv.org/abs/2003.10555) model, which we name TUNiB-Electra. There are two motivations. First, all the existing pre-trained Korean encoder models are monolingual, that is, they have knowledge about Korean only. Our bilingual models are based on the balanced corpora of Korean and English. Second, we want new off-the-shelf models trained on much more texts. To this end, we collected a large amount of Korean text from various sources such as blog posts, comments, news, web novels, etc., which sum up to 100 GB in total.


## How to use
  
You can use this model directly with [transformers](https://github.com/huggingface/transformers) library:
  
```python
from transformers import AutoModel, AutoTokenizer

# Base Model (Korean-only model)
tokenizer = AutoTokenizer.from_pretrained('tunib/electra-ko-base')
model = AutoModel.from_pretrained('tunib/electra-ko-base')
```

### Tokenizer example

```python
>>> from transformers import AutoTokenizer
>>> tokenizer = AutoTokenizer.from_pretrained('tunib/electra-ko-base')
>>> tokenizer.tokenize("tunib is a natural language processing tech startup.")
['tun', '##ib', 'is', 'a', 'natural', 'language', 'processing', 'tech', 'startup', '.']
>>> tokenizer.tokenize("튜닙은 자연어처리 테크 스타트업입니다.")
['튜', '##닙', '##은', '자연', '##어', '##처리', '테크', '스타트업', '##입니다', '.']
```
  
## Results on Korean downstream tasks
 
  
|                       |**# Params** |**Avg.**| **NSMC**<br/>(acc) | **Naver NER**<br/>(F1) | **PAWS**<br/>(acc) | **KorNLI**<br/>(acc) | **KorSTS**<br/>(spearman) | **Question Pair**<br/>(acc) | **KorQuaD (Dev)**<br/>(EM/F1) |**Korean-Hate-Speech (Dev)**<br/>(F1)|
|  :----------------:| :----------------: | :--------------------: | :----------------: | :------------------: | :-----------------------: | :-------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :----------------: |
|***TUNiB-Electra-ko-base*** |  110M | **85.99** |  90.95 |    87.63         |   84.65   | **82.27**   |    85.00   |  95.77 |   64.01 / 90.32   |71.40 |
|***TUNiB-Electra-ko-en-base*** |  133M |85.34 	|90.59     |        87.25        |  **84.90**   |  80.43    |  83.81	| 94.85 | 83.09 / 92.06   |68.83 |
| [KoELECTRA-base-v3](https://github.com/monologg/KoELECTRA)    |  110M | 85.92   |90.63   |      **88.11**	     |    84.45    |    82.24    |       **85.53**      |     95.25      | **84.83 / 93.45**	     |  67.61 |
| [KcELECTRA-base](https://github.com/Beomi/KcELECTRA) | 124M|  84.75     |**91.71**      |         86.90          |       74.80        |        81.65         |           82.65           |          **95.78**          |         70.60 / 90.11         | **74.49** |
| [KoBERT-base](https://github.com/SKTBrain/KoBERT)        |  90M  |   84.17       |  89.63        |         86.11          |       80.65        |        79.00         |           79.64           |            93.93            |         52.81 / 80.27         | 66.21 |
| [KcBERT-base](https://github.com/Beomi/KcBERT)         |   110M    |   81.37    | 89.62        |         84.34          |       66.95        |        74.85         |           75.57           |            93.93            |         60.25 / 84.39         | 68.77  |
| [XLM-Roberta-base](https://github.com/pytorch/fairseq/tree/master/examples/xlmr)   | 280M  |  85.74    |89.49        |         86.26          |       82.95        |        79.92         |           79.09           |            93.53            |         64.70 / 88.94         |  64.06 |