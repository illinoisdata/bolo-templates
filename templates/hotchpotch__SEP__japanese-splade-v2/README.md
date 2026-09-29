---
license: mit
datasets:
- hpprc/emb
- hotchpotch/japanese-splade-v1-hard-negatives
- hpprc/msmarco-ja
language:
- ja
base_model:
- hotchpotch/japanese-splade-base-v1_5
---

高性能な日本語 [SPLADE](https://github.com/naver/splade) (Sparse Lexical and Expansion Model) モデルです。[テキストからスパースベクトルへの変換デモ](https://huggingface.co/spaces/hotchpotch/japanese-splade-demo-streamlit)で、どのようなスパースベクトルに変換できるか、WebUI から気軽にお試しいただけます。

- [情報検索モデルで最高性能(512トークン以下)・日本語版SPLADE v2をリリース](https://secon.dev/entry/2024/12/19/100000-japanese-splade-v2-release/)

また、モデルの学習には[YAST - Yet Another SPLADE or Sparse Trainer](https://github.com/hotchpotch/yast)を使っています。


# 利用方法

## [YASEM (Yet Another Splade|Sparse Embedder)](https://github.com/hotchpotch/yasem)

[YASEM](https://github.com/hotchpotch/yasem) を利用することで、SPLADEの推論・単語トークンの確認を簡単に行えます。

```bash
pip install yasem
```

```python
from yasem import SpladeEmbedder

model_name = "hotchpotch/japanese-splade-v2"
embedder = SpladeEmbedder(model_name)

query = "車の燃費を向上させる方法は？"
docs = [
    "急発進や急ブレーキを避け、一定速度で走行することで燃費が良くなります。",
    "車の運転時、急発進や急ブレーキをすると、燃費が悪くなります。",
    "車を長持ちさせるには、消耗品を適切なタイミングで交換することが重要です。",
]

print(embedder.rank(query, docs, return_documents=True))
```

```python
[
 { 'corpus_id': 0
 , 'score': 4.28
 , 'text': '急発進や急ブレーキを避け、一定速度で走行することで燃費が良くなります。' }
 ,
 { 'corpus_id': 2
 , 'score': 2.47
 , 'text': '車を長持ちさせるには、消耗品を適切なタイミングで交換することが重要です。' }
 ,
 { 'corpus_id': 1
 , 'score': 2.34
 , 'text': '車の運転時、急発進や急ブレーキをすると、燃費が悪くなります。' }
]
```

```python
sentences = [query] + docs

embeddings = embedder.encode(sentences)
similarity = embedder.similarity(embeddings, embeddings)

print(similarity)
```

```json
[[5.19151189, 4.28027662, 2.34164901, 2.47221905],
[4.28027662, 11.64426784, 5.00328318, 2.15031016],
[2.34164901, 5.00328318, 6.05594296, 1.33752085],
[2.47221905, 2.15031016, 1.33752085, 9.39414744]]
```


```python
token_values = embedder.get_token_values(embeddings[0])
print(token_values)
```

```python
{
 '燃費': 1.13,
 '方法': 1.07,
 '車': 1.05,
 '高める': 0.67,
 '向上': 0.56,
 '増加': 0.52,
 '都市': 0.44,
 'ガソリン': 0.32,
 '改善': 0.30,
 ...
```

## transformers からの利用

```python

from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch

model = AutoModelForMaskedLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def splade_max_pooling(logits, attention_mask):
    relu_log = torch.log(1 + torch.relu(logits))
    weighted_log = relu_log * attention_mask.unsqueeze(-1)
    max_val, _ = torch.max(weighted_log, dim=1)
    return max_val

tokens = tokenizer(
    sentences, return_tensors="pt", padding=True, truncation=True, max_length=512
)
tokens = {k: v.to(model.device) for k, v in tokens.items()}

with torch.no_grad():
    outputs = model(**tokens)
embeddings = splade_max_pooling(outputs.logits, tokens["attention_mask"])

similarity = torch.matmul(embeddings.unsqueeze(0), embeddings.T).squeeze(0)
print(similarity)
```

```python
tensor([
   [5.1872, 4.2792, 2.3440, 2.4680],
   [4.2792, 11.6327, 4.9983, 2.1470],
   [2.3440, 4.9983, 6.0517, 1.3377],
   [2.4680, 2.1470, 1.3377, 9.3801]
])
```

# ベンチマークスコア

## retrieval (JMTEB)

[JMTEB](https://github.com/sbintuitions/JMTEB) の評価結果です。

japanese-splade-v2 は [JMTEB をスパースベクトルで評価できるように変更したコード](https://github.com/hotchpotch/JMTEB/tree/add_splade)での評価となっています。 
なお、japanese-splade-v2 は JMTEB タスクである jaqket(や派生のjaqra), mrtydi(と派生のmiracl), jagovfaqs, nlp_jornal のデータセットのtrain,dev, testなどのデータは **学習に利用していません**。


| モデル名                          | jagovfaqs | jaqket | mrtydi     | nlp_journal <br>title_abs | nlp_journal <br>abs_intro | nlp_journal <br>title_intro | Avg  <br><512 | Avg  <br>ALL |
| ----------------------------- | --------- | ------ | ---------- | ------------------------- | ------------------------- | --------------------------- | ------------- | ------------ |
| japanese-splade-v2       | 0.7313    | 0.6986 | **0.5106** | **0.9831**                | 0.9067                    | 0.8026                      | **0.7309**    | 0.7722   |
| japanese-splade-base-v1 | 0.6499    | 0.6992 | 0.4365 | 0.8967 | 0.9766 | 0.8203 | 0.6906 | 0.7465 |
| GLuCoSE-base-ja-v2            | 0.6979    | 0.6729 | 0.4186     | 0.9511                    | 0.9029                    | 0.7580                      | 0.6851        | 0.7336       |
| multilingual-e5-large         | 0.7030    | 0.5878 | 0.4363     | 0.9470                    | 0.8600                    | 0.7248                      | 0.6685        | 0.7098       |
| ruri-large                    | **0.7668**    | 0.6174 | 0.3803     | 0.9658                    | 0.8712                    | 0.7797                      | 0.6826        | 0.7302       |
| jinaai/jina-embeddings-v3     | 0.7150    | 0.4648 | 0.4545     | 0.9562                    | 0.9843                    | 0.9385                      | 0.6476        | 0.7522       |
| sarashina-embedding-v1-1b     | 0.7168    | **0.7279** | 0.4195     | 0.9696                    | 0.9394                    | 0.8833                      | 0.7085        | **0.7761**       |
| OpenAI/text-embedding-3-large | 0.7241    | 0.4821 | 0.3488     | 0.9655                    | **0.9933**                    | **0.9547**                      | 0.6301        | 0.7448       |

## スパース性

v1 ではスパース性が強すぎたので、v2 ではバランスをとったスパース性を持たせています。

- https://github.com/hotchpotch/yast/blob/main/utils/JMTEB_L0.py

で計測しています。

| Target                                  | jaqket-query | jaqket-docs | mrtydi-query | mrtydi-docs | jagovfaqs_22k-query | jagovfaqs_22k-docs | nlp_journal_title_abs-query | nlp_journal_title_abs-docs | nlp_journal_title_intro-query | nlp_journal_title_intro-docs | nlp_journal_abs_intro-query | nlp_journal_abs_intro-docs |
|-----------------------------------------|--------------|-------------|--------------|-------------|---------------------|--------------------|-----------------------------|----------------------------|------------------------------|-----------------------------|-----------------------------|----------------------------|
| v1                                      | 23.3         | 146.2       | 13.8         | 89.3        | 27.9               | 73.2               | 19                          | 75.2                      | 19                           | 95.7                       | 75.3                        | 95.7                       |
| v1-mmarco-only                          | 38.9         | 231.8       | 20.5         | 100.4       | 43.4               | 97.9               | 26.4                        | 126.9                     | 26.4                         | 182                        | 127.2                       | 182                        |
| v1_5 | 36.7         | 268.7       | 22.8         | 237.6       | 47.9               | 237.3              | 34.9                        | 225.6                     | 34.9                         | 235.2                      | 224.5                       | 235.2                      |
| v2 | 29.8         | 379.6       | 19.4         | 176.4       | 42                 | 189.8              | 29                          | 235.8                     | 29                           | 304.9                      | 233.8                       | 304.9                      |



# 学習元データセット

-  [hpprc/emb](https://huggingface.co/datasets/hpprc/emb) 
	- auto-wiki-qa
	- jsquad
	- jaquad
	- auto-wiki-qa-nemotron
	- quiz-works
	- quiz-no-mori
	- baobab-wiki-retrieval
	- mkqa
- [hotchpotch/japanese-splade-v1-hard-negatives](https://huggingface.co/datasets/hotchpotch/japanese-splade-v1-hard-negatives)
	- mmarco
	- mqa
	- msmarco-ja
- [hotchpotch/mmarco-hard-negatives-reranker-score](https://huggingface.co/datasets/hotchpotch/mmarco-hard-negatives-reranker-score)
    - english
 
# ライセンス

MIT