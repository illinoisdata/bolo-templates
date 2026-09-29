---
license: cc-by-sa-4.0
datasets:
- globis-university/aozorabunko-clean
- oscar-corpus/OSCAR-2301
- Wikipedia
- WikiBooks
- CC-100
- allenai/c4
language:
- ja
library_name: transformers
---

# What’s this?
日本語リソースで学習した [DeBERTa V3](https://huggingface.co/microsoft/deberta-v3-large) モデルです。

以下のような特徴を持ちます:

- 定評のある [DeBERTa V3](https://huggingface.co/microsoft/deberta-v3-large) を用いたモデル
- 日本語特化
- 推論時に形態素解析器を用いない
- 単語境界をある程度尊重する (`の都合上` や `の判定負けを喫し` のような複数語のトークンを生じさせない)

---
This is a model based on [DeBERTa V3](https://huggingface.co/microsoft/deberta-v3-large) pre-trained on Japanese resources.

The model has the following features:
- Based on the well-known [DeBERTa V3](https://huggingface.co/microsoft/deberta-v3-large) model
- Specialized for the Japanese language
- Does not use a morphological analyzer during inference
- Respects word boundaries to some extent (does not produce tokens spanning multiple words like `の都合上` or `の判定負けを喫し`)

# How to use
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = 'globis-university/deberta-v3-japanese-large'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)
```

# Tokenizer
[工藤氏によって示された手法](https://qiita.com/taku910/items/fbaeab4684665952d5a9)で学習しました。

以下のことを意識しています:

- 推論時の形態素解析器なし
- トークンが単語の境界を跨がない (辞書: `unidic-cwj-202302`)
- Hugging Faceで使いやすい
- 大きすぎない語彙数

本家の DeBERTa V3 は大きな語彙数で学習されていることに特徴がありますが、反面埋め込み層のパラメータ数が大きくなりすぎる ([microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) モデルの場合で埋め込み層が全体の 54%) ことから、本モデルでは小さめの語彙数を採用しています。

注意点として、 `xsmall` 、 `base` 、 `large` の 3 つのモデルのうち、前者二つは unigram アルゴリズムで学習しているが、 `large` モデルのみ BPE アルゴリズムで学習している。
深い理由はなく、  `large` モデルのみ語彙サイズを増やすために独立して学習を行ったが、なぜか unigram アルゴリズムでの学習がうまくいかなかったことが原因である。
原因の探究よりモデルの完成を優先して、 BPE アルゴリズムに切り替えた。

---
The tokenizer is trained using [the method introduced by Kudo](https://qiita.com/taku910/items/fbaeab4684665952d5a9).

Key points include:
- No morphological analyzer needed during inference
- Tokens do not cross word boundaries (dictionary: `unidic-cwj-202302`)
- Easy to use with Hugging Face
- Smaller vocabulary size

Although the original DeBERTa V3 is characterized by a large vocabulary size, which can result in a significant increase in the number of parameters in the embedding layer (for the [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) model, the embedding layer accounts for 54% of the total), this model adopts a smaller vocabulary size to address this.

Note that, among the three models: xsmall, base, and large, the first two were trained using the unigram algorithm, while only the large model was trained using the BPE algorithm.
The reason for this is simple: while the large model was independently trained to increase its vocabulary size, for some reason, training with the unigram algorithm was not successful.
Thus, prioritizing the completion of the model over investigating the cause, we switched to the BPE algorithm.

# Data
| Dataset Name  | Notes | File Size (with metadata) | Factor |
| ------------- | ----- | ------------------------- | ---------- |
| Wikipedia     | 2023/07; [WikiExtractor](https://github.com/attardi/wikiextractor) | 3.5GB | x2 |
| Wikipedia     | 2023/07; [cl-tohoku's method](https://github.com/cl-tohoku/bert-japanese/blob/main/make_corpus_wiki.py) | 4.8GB | x2 |
| WikiBooks     | 2023/07; [cl-tohoku's method](https://github.com/cl-tohoku/bert-japanese/blob/main/make_corpus_wiki.py) | 43MB | x2 |
| Aozora Bunko  | 2023/07; [globis-university/aozorabunko-clean](https://huggingface.co/globis-university/globis-university/aozorabunko-clean) | 496MB | x4 |
| CC-100        | ja | 90GB | x1 |
| mC4           | ja; extracted 10%, with Wikipedia-like focus via [DSIR](https://arxiv.org/abs/2302.03169) | 91GB | x1 |
| OSCAR 2023    | ja; extracted 10%, with Wikipedia-like focus via [DSIR](https://arxiv.org/abs/2302.03169) | 26GB | x1 |

# Training parameters
- Number of devices: 8
- Batch size: 8 x 8
- Learning rate: 6.4e-5
- Maximum sequence length: 512
- Optimizer: AdamW
- Learning rate scheduler: Linear schedule with warmup
- Training steps: 2,000,000
- Warmup steps: 100,000
- Precision: Mixed (fp16)
- Vocabulary size: 48,000

# Evaluation
| Model | #params | JSTS | JNLI | JSQuAD | JCQA |
| ----- | ------- | ---- | ---- | ------ | ---- |
| ≤ small | | | | | |
| [izumi-lab/deberta-v2-small-japanese](https://huggingface.co/izumi-lab/deberta-v2-small-japanese) | 17.8M | 0.890/0.846 | 0.880 | - | 0.737 |
| [globis-university/deberta-v3-japanese-xsmall](https://huggingface.co/globis-university/deberta-v3-japanese-xsmall) | 33.7M | **0.916**/**0.880** | **0.913** | **0.869**/**0.938** | **0.821** |
| base | | | | |
| [cl-tohoku/bert-base-japanese-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-v3) | 111M | 0.919/0.881 | 0.907 | 0.880/0.946 | 0.848 |
| [nlp-waseda/roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) | 111M | 0.913/0.873 | 0.895 | 0.864/0.927 | 0.840 |
| [izumi-lab/deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) | 110M | 0.919/0.882 | 0.912 | - | 0.859 |
| [ku-nlp/deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) | 112M | 0.922/0.886 | 0.922 | **0.899**/**0.951** | - |
| [ku-nlp/deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) | 160M | **0.927**/0.891 | **0.927** | 0.896/- | - |
| [globis-university/deberta-v3-japanese-base](https://huggingface.co/globis-university/deberta-v3-japanese-base) | 110M | 0.925/**0.895** | 0.921 | 0.890/0.950 | **0.886** |
| large | | | | | |
| [cl-tohoku/bert-large-japanese-v2](https://huggingface.co/cl-tohoku/bert-large-japanese-v2) | 337M | 0.926/0.893 | **0.929** | 0.893/0.956 | 0.893 |
| [nlp-waseda/roberta-large-japanese](https://huggingface.co/nlp-waseda/roberta-large-japanese) | 337M | **0.930**/**0.896** | 0.924 | 0.884/0.940 | **0.907** |
| [nlp-waseda/roberta-large-japanese-seq512](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512) | 337M | 0.926/0.892 | 0.926 | **0.918**/**0.963** | 0.891 |
| [ku-nlp/deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) | 339M | 0.925/0.892 | 0.924 | 0.912/0.959 | - |
| [**globis-university/deberta-v3-japanese-large**](https://huggingface.co/globis-university/deberta-v3-japanese-large) | 352M | 0.928/**0.896** | 0.924 | 0.896/0.956 | 0.900 |

## License
CC BY SA 4.0

## Acknowledgement
計算リソースに [ABCI](https://abci.ai/) を利用させていただきました。ありがとうございます。

---
We used [ABCI](https://abci.ai/) for computing resources. Thank you.