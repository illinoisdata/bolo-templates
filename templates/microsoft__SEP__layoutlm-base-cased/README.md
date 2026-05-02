# LayoutLM
**Multimodal (text + layout/format + image) pre-training for document AI**

[Microsoft Document AI](https://www.microsoft.com/en-us/research/project/document-ai/) | [GitHub](https://aka.ms/layoutlm)

## Model description

LayoutLM is a simple but effective pre-training method of text and layout for document image understanding and information extraction tasks, such as form understanding and receipt understanding. LayoutLM archives the SOTA results on multiple datasets. For more details, please refer to our paper: 

[LayoutLM: Pre-training of Text and Layout for Document Image Understanding](https://arxiv.org/abs/1912.13318)
Yiheng Xu, Minghao Li, Lei Cui, Shaohan Huang, Furu Wei, Ming Zhou, [KDD 2020](https://www.kdd.org/kdd2020/accepted-papers)

## Different Tokenizer
Note that LayoutLM-Cased requires a different tokenizer, based on RobertaTokenizer. You can
initialize it as follows:

~~~
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('microsoft/layoutlm-base-cased') 
~~~

## Citation

If you find LayoutLM useful in your research, please cite the following paper:

``` latex
@misc{xu2019layoutlm,
    title={LayoutLM: Pre-training of Text and Layout for Document Image Understanding},
    author={Yiheng Xu and Minghao Li and Lei Cui and Shaohan Huang and Furu Wei and Ming Zhou},
    year={2019},
    eprint={1912.13318},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```