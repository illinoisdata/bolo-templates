---
language:
- ja
widget:
- text: 株式会社Jurabiは、東京都台東区に本社を置くIT企業である。
license: cc-by-sa-3.0
---
# BERTによる日本語固有表現抽出のモデル
[BertForTokenClassification](https://huggingface.co/docs/transformers/model_doc/bert#transformers.BertForTokenClassification)を用いて、日本語の文から固有表現を抽出します。

抽出される固有表現のタイプは、以下の8種類です。
- 人名
- 法人名（法人または法人に類する組織）
- 政治的組織名（政治的組織名、政党名、政府組織名、行政組織名、軍隊名、国際組織名）
- その他の組織名	（競技組織名、公演組織名、その他）
- 地名	
- 施設名
- 製品名（商品名、番組名、映画名、書籍名、歌名、ブランド名等）
- イベント名

## 使用方法
必要なライブラリ（transformers、unidic_lite、fugashi）をpipなどでインストールして、下記のコードを実行するだけです。

```python
from transformers import BertJapaneseTokenizer, BertForTokenClassification
from transformers import pipeline

model = BertForTokenClassification.from_pretrained("jurabi/bert-ner-japanese")
tokenizer = BertJapaneseTokenizer.from_pretrained("jurabi/bert-ner-japanese")

ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer)
ner_pipeline("株式会社Jurabiは、東京都台東区に本社を置くIT企業である。")
```

## 事前学習モデル
東北大学乾研究室が公開している日本語BERTモデル（[cl-tohoku/bert-base-japanese-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-v2)）

## 学習データ
ストックマーク株式会社が公開しているWikipediaを用いた日本語の固有表現抽出データセット（[stockmarkteam/ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset)）

## ソースコード
ファインチューニングに使用したプログラムは、[jurabiinc/bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese)で公開しています。

## ライセンス
[Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/)