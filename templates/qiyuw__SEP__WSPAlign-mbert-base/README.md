---
license: cc-by-nc-sa-4.0
language:
- en
- de
- fr
- zh
- ja
- ro
tags:
- word alignment
- multilingual
- translation
---
# Model Description 
Refer to [https://github.com/qiyuw/WSPAlign](https://github.com/qiyuw/WSPAlign) and [https://github.com/qiyuw/WSPAlign.InferEval](https://github.com/qiyuw/WSPAlign.InferEval) for details.

# Qucik Usage

First clone inference repository:
```
git clone https://github.com/qiyuw/WSPAlign.InferEval.git
```
Then install the requirements following [https://github.com/qiyuw/WSPAlign.InferEval](https://github.com/qiyuw/WSPAlign.InferEval). For inference only `transformers`, `SpaCy` and `torch` are required.

Finally, run the following example:
```
python inference.py --model_name_or_path qiyuw/WSPAlign-ft-kftt --src_lang ja --src_text="私は猫が好きです。" --tgt_lang en --tgt_text="I like cats."
```
Check `inference.py` for details usage.

# Citation
Cite our paper if WSPAlign helps your work:

```bibtex
@inproceedings{wu-etal-2023-wspalign,
    title = "{WSPA}lign: Word Alignment Pre-training via Large-Scale Weakly Supervised Span Prediction",
    author = "Wu, Qiyu  and Nagata, Masaaki  and Tsuruoka, Yoshimasa",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.621",
    pages = "11084--11099",
}
```