---
language: ja
thumbnail: https://github.com/studio-ousia/luke/raw/master/resources/luke_logo.png
tags:
  - luke
  - named entity recognition
  - entity typing
  - relation classification
  - question answering
license: apache-2.0
---

## luke-japanese-large

**luke-japanese** is the Japanese version of **LUKE** (**L**anguage
**U**nderstanding with **K**nowledge-based **E**mbeddings), a pre-trained
_knowledge-enhanced_ contextualized representation of words and entities. LUKE
treats words and entities in a given text as independent tokens, and outputs
contextualized representations of them. Please refer to our
[GitHub repository](https://github.com/studio-ousia/luke) for more details and
updates.

This model contains Wikipedia entity embeddings which are not used in general
NLP tasks. Please use the
[lite version](https://huggingface.co/studio-ousia/luke-japanese-large-lite/)
for tasks that do not use Wikipedia entities as inputs.

**luke-japanese**は、単語とエンティティの知識拡張型訓練済み Transformer モデル**LUKE**の日本語版です。LUKE は単語とエンティティを独立したトークンとして扱い、これらの文脈を考慮した表現を出力します。詳細については、[GitHub リポジトリ](https://github.com/studio-ousia/luke)を参照してください。

このモデルは、通常の NLP タスクでは使われない Wikipedia エンティティのエンベディングを含んでいます。単語の入力のみを使うタスクには、[lite version](https://huggingface.co/studio-ousia/luke-japanese-large-lite/)を使用してください。

### Experimental results on JGLUE

The experimental results evaluated on the dev set of
[JGLUE](https://github.com/yahoojapan/JGLUE) is shown as follows:

| Model                         | MARC-ja   | JSTS                | JNLI      | JCommonsenseQA |
| ----------------------------- | --------- | ------------------- | --------- | -------------- |
|                               | acc       | Pearson/Spearman    | acc       | acc            |
| **LUKE Japanese large**       | **0.965** | **0.932**/**0.902** | **0.927** | 0.893          |
| _Baselines:_                  |           |
| Tohoku BERT large             | 0.955     | 0.913/0.872         | 0.900     | 0.816          |
| Waseda RoBERTa large (seq128) | 0.954     | 0.930/0.896         | 0.924     | **0.907**      |
| Waseda RoBERTa large (seq512) | 0.961     | 0.926/0.892         | 0.926     | 0.891          |
| XLM RoBERTa large             | 0.964     | 0.918/0.884         | 0.919     | 0.840          |

The baseline scores are obtained from
[here](https://github.com/yahoojapan/JGLUE/blob/a6832af23895d6faec8ecf39ec925f1a91601d62/README.md).

### Citation

```latex
@inproceedings{yamada2020luke,
  title={LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention},
  author={Ikuya Yamada and Akari Asai and Hiroyuki Shindo and Hideaki Takeda and Yuji Matsumoto},
  booktitle={EMNLP},
  year={2020}
}
```
