---
language:
- ja
license: apache-2.0
library_name: transformers
datasets:
- llm-book/JGLUE
---

# bert-base-japanese-v3-jsts

「[大規模言語モデル入門](https://www.amazon.co.jp/dp/4297136333)」の第5章で紹介している(意味類似度計算)のモデルです。
[cl-tohoku/bert-base-japanese-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-v3)を[JGLUE](https://huggingface.co/datasets/llm-book/JGLUE)のJSTSデータセットでファインチューニングして構築されています。

## 関連リンク

* [GitHubリポジトリ](https://github.com/ghmagazine/llm-book)
* [Colabノートブック（訓練）](https://colab.research.google.com/github/ghmagazine/llm-book/blob/main/chapter5/5-4-sts-finetuning.ipynb)
* [Colabノートブック（推論）](https://colab.research.google.com/github/ghmagazine/llm-book/blob/main/chapter5/5-4-sts-analysis.ipynb)
* [データセット](https://huggingface.co/datasets/llm-book/JGLUE)
* [大規模言語モデル入門（Amazon.co.jp）](https://www.amazon.co.jp/dp/4297136333/)
* [大規模言語モデル入門（gihyo.jp）](https://gihyo.jp/book/2023/978-4-297-13633-8)

## 使い方
```python
from transformers import pipeline

text_sim_pipeline = pipeline(
    model="llm-book/bert-base-japanese-v3-jsts",
    function_to_apply="none",
)
text = "川べりでサーフボードを持った人たちがいます"
sim_text = "サーファーたちが川べりに立っています"
# textとsim_textの類似度を計算
result = text_sim_pipeline({"text": text, "text_pair": sim_text})
print(result["score"])
# 3.5703558921813965
```

## ライセンス

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)