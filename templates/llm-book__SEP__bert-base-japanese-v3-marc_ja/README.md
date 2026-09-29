---
language:
- ja
license: apache-2.0
library_name: transformers
datasets:
- llm-book/JGLUE
pipeline_tag: text-classification
---

# bert-base-japanese-v3-marc_ja

「[大規模言語モデル入門](https://www.amazon.co.jp/dp/4297136333)」の第5章で紹介している(感情分析)のモデルです。
[cl-tohoku/bert-base-japanese-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-v3)を[JGLUE](https://huggingface.co/datasets/llm-book/JGLUE)のMARC-jaデータセットでファインチューニングして構築されています。

## 関連リンク

* [GitHubリポジトリ](https://github.com/ghmagazine/llm-book)
* [Colabノートブック（訓練）](https://colab.research.google.com/github/ghmagazine/llm-book/blob/main/chapter5/5-2-sentiment-analysis-finetuning.ipynb)
* [Colabノートブック（推論）](https://colab.research.google.com/github/ghmagazine/llm-book/blob/main/chapter5/5-3-sentiment-analysis-analysis.ipynb)
* [データセット](https://huggingface.co/datasets/llm-book/JGLUE)
* [大規模言語モデル入門（Amazon.co.jp）](https://www.amazon.co.jp/dp/4297136333/)
* [大規模言語モデル入門（gihyo.jp）](https://gihyo.jp/book/2023/978-4-297-13633-8)

## 使い方
```python
from transformers import pipeline

text_classification_pipeline = pipeline(model="llm-book/bert-base-japanese-v3-marc_ja")
print(text_classification_pipeline("世界には言葉がわからなくても感動する音楽がある。")[0])
# {'label': 'positive', 'score': 0.9993619322776794}
```

## ライセンス

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)