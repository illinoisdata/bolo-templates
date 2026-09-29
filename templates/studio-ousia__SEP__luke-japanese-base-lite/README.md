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

## luke-japanese

**luke-japanese** is the Japanese version of **LUKE** (**L**anguage
**U**nderstanding with **K**nowledge-based **E**mbeddings), a pre-trained
_knowledge-enhanced_ contextualized representation of words and entities. LUKE
treats words and entities in a given text as independent tokens, and outputs
contextualized representations of them. Please refer to our
[GitHub repository](https://github.com/studio-ousia/luke) for more details and
updates.

This model is a lightweight version which does not contain Wikipedia entity
embeddings. Please use the
[full version](https://huggingface.co/studio-ousia/luke-japanese-base/) for
tasks that use Wikipedia entities as inputs.

**luke-japanese**は、単語とエンティティの知識拡張型訓練済み Transformer モデル**LUKE**の日本語版です。LUKE は単語とエンティティを独立したトークンとして扱い、これらの文脈を考慮した表現を出力します。詳細については、[GitHub リポジトリ](https://github.com/studio-ousia/luke)を参照してください。

このモデルは、Wikipedia エンティティのエンベディングを含まない軽量版のモデルです。Wikipedia エンティティを入力として使うタスクには、[full version](https://huggingface.co/studio-ousia/luke-japanese-base/)を使用してください。

### Experimental results on JGLUE

The experimental results evaluated on the dev set of
[JGLUE](https://github.com/yahoojapan/JGLUE) are shown as follows:

| Model                  | MARC-ja   | JSTS                | JNLI      | JCommonsenseQA |
| ---------------------- | --------- | ------------------- | --------- | -------------- |
|                        | acc       | Pearson/Spearman    | acc       | acc            |
| **LUKE Japanese base** | **0.965** | **0.916**/**0.877** | **0.912** | **0.842**      |
| _Baselines:_           |           |
| Tohoku BERT base       | 0.958     | 0.909/0.868         | 0.899     | 0.808          |
| NICT BERT base         | 0.958     | 0.910/0.871         | 0.902     | 0.823          |
| Waseda RoBERTa base    | 0.962     | 0.913/0.873         | 0.895     | 0.840          |
| XLM RoBERTa base       | 0.961     | 0.877/0.831         | 0.893     | 0.687          |

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
