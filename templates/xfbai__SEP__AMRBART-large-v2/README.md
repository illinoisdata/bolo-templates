---
language: en
tags:
- AMRBART
license: mit
---

**AMRBART** is a pretrained semantic parser which converts a sentence into an abstract meaning graph. You may find our paper [here](https://arxiv.org/pdf/2203.07836.pdf) (Arxiv). The original implementation is avaliable [here](https://github.com/goodbai-nlp/AMRBART/tree/acl2022)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/graph-pre-training-for-amr-parsing-and-1/amr-to-text-generation-on-ldc2017t10)](https://paperswithcode.com/sota/amr-to-text-generation-on-ldc2017t10?p=graph-pre-training-for-amr-parsing-and-1)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/graph-pre-training-for-amr-parsing-and-1/amr-to-text-generation-on-ldc2020t02)](https://paperswithcode.com/sota/amr-to-text-generation-on-ldc2020t02?p=graph-pre-training-for-amr-parsing-and-1)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/graph-pre-training-for-amr-parsing-and-1/amr-parsing-on-ldc2017t10)](https://paperswithcode.com/sota/amr-parsing-on-ldc2017t10?p=graph-pre-training-for-amr-parsing-and-1)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/graph-pre-training-for-amr-parsing-and-1/amr-parsing-on-ldc2020t02)](https://paperswithcode.com/sota/amr-parsing-on-ldc2020t02?p=graph-pre-training-for-amr-parsing-and-1)

**News**🎈

- (2022/12/10) fix max_length bugs in AMR parsing and update results.
- (2022/10/16) release the AMRBART-v2 model which is simpler, faster, and stronger.

# Requirements
+ python 3.8
+ pytorch 1.8
+ transformers 4.21.3
+ datasets 2.4.0
+ Tesla V100 or A100

We recommend to use conda to manage virtual environments:
```
conda env update --name <env> --file requirements.yml
```

# Data Processing

<!-- Since AMR corpus require LDC license, we upload some examples for format reference. If you have the license, feel free to contact us for getting the preprocessed data. -->
You may download the AMR corpora at [LDC](https://www.ldc.upenn.edu).

Please follow [this respository](https://github.com/goodbai-nlp/AMR-Process) to preprocess AMR graphs:
``` 
bash run-process-acl2022.sh
```

# Usage

Our model is avaliable at [huggingface](https://huggingface.co/xfbai). Here is how to initialize a AMR parsing model in PyTorch:

```
from transformers import BartForConditionalGeneration
from model_interface.tokenization_bart import AMRBartTokenizer      # We use our own tokenizer to process AMRs

model = BartForConditionalGeneration.from_pretrained("xfbai/AMRBART-large-finetuned-AMR3.0-AMRParsing-v2")
tokenizer = AMRBartTokenizer.from_pretrained("xfbai/AMRBART-large-finetuned-AMR3.0-AMRParsing-v2")
```