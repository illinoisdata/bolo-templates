---
language:
- ja
tags:
- t5
- text2text-generation
- seq2seq
license: cc-by-sa-4.0
datasets:
- wikipedia
- oscar
- cc100
---

# 日本語T5事前学習済みモデル

This is a T5 (Text-to-Text Transfer Transformer) model pretrained on Japanese corpus.

次の日本語コーパス（約100GB）を用いて事前学習を行ったT5 (Text-to-Text Transfer Transformer) [v1.1アーキテクチャ](https://github.com/google-research/text-to-text-transfer-transformer/blob/main/released_checkpoints.md)のモデルです。  

* [Wikipedia](https://ja.wikipedia.org)の日本語ダンプデータ (2022年6月27日時点のもの)
* [OSCAR](https://oscar-corpus.com)の日本語コーパス
* [CC-100](http://data.statmt.org/cc-100/)の日本語コーパス

このモデルは事前学習のみを行なったものであり、特定のタスクに利用するにはファインチューニングする必要があります。  
本モデルにも、大規模コーパスを用いた言語モデルにつきまとう、学習データの内容の偏りに由来する偏った（倫理的ではなかったり、有害だったり、バイアスがあったりする）出力結果になる問題が潜在的にあります。
この問題が発生しうることを想定した上で、被害が発生しない用途にのみ利用するよう気をつけてください。

SentencePieceトークナイザーの学習には、上記WikipediaとCC-100を約10:1の比率で混ぜたデータを用いました。byte-fallbackあり設定で学習しており、実質未知語が発生しません。


# 転移学習のサンプルコード

https://github.com/sonoisa/t5-japanese


# ベンチマーク

準備中

# 免責事項

本モデルの作者は本モデルを作成するにあたって、その内容、機能等について細心の注意を払っておりますが、モデルの出力が正確であるかどうか、安全なものであるか等について保証をするものではなく、何らの責任を負うものではありません。本モデルの利用により、万一、利用者に何らかの不都合や損害が発生したとしても、モデルやデータセットの作者や作者の所属組織は何らの責任を負うものではありません。利用者には本モデルやデータセットの作者や所属組織が責任を負わないことを明確にする義務があります。


# ライセンス

[CC-BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.ja)

[Common Crawlの利用規約](http://commoncrawl.org/terms-of-use/)も守るようご注意ください。