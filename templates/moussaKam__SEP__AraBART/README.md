---
tags:
- summarization
- bart

language:
- ar
widget:
- text: بيروت هي عاصمة <mask>.

license: apache-2.0

pipeline_tag: "fill-mask"
---

AraBART is the first Arabic model in which the encoder and the decoder are pretrained end-to-end, based on BART. AraBART follows the architecture of BART-Base
which has 6 encoder and 6 decoder layers and 768 hidden dimensions. In total AraBART has 139M parameters.

AraBART achieves the best performance on multiple abstractive summarization datasets, outperforming strong baselines including a pretrained Arabic BERT-based models and multilingual mBART and mT5 models.


