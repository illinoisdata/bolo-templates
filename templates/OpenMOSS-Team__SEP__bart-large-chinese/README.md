---
tags:
- text2text-generation
- Chinese
- seq2seq
language: zh
---
# Chinese BART-Large

### News

**12/30/2022**

An updated version of CPT & Chinese BART are released. In the new version, we changed the following parts:

- **Vocabulary** We replace the old BERT vocabulary with a larger one of size 51271 built from the training data, in which we 1) add missing 6800+ Chinese characters (most of them are traditional Chinese characters); 2) remove redundant tokens (e.g.  Chinese character tokens with ## prefix); 3) add some English tokens to reduce OOV.
- **Position Embeddings** We extend the max_position_embeddings from 512 to 1024.

We initialize the new version of models with the old version of checkpoints with vocabulary alignment. Token embeddings found in the old checkpoints are copied. And other newly added parameters are randomly initialized. We further train the new CPT & Chinese BART 50K steps with batch size 2048, max-seq-length 1024, peak learning rate 2e-5, and warmup ratio 0.1.

The result compared to the previous checkpoints is as followings:

|            | AFQMC | IFLYTEK | CSL-sum | LCSTS |  AVG  |
| :--------- | :---: | :-----: | :-----: | :---: | :---: |
| Previous   |      |        |        |      |      |
| bart-base  | 73.0 |   60   |  62.1  | 37.8 | 58.23 |
| cpt-base   | 75.1 |  60.5  |  63.0  | 38.2 | 59.20 |
| bart-large | 75.7 |  62.1  |  64.2  | 40.6 | 60.65 |
| cpt-large  | 75.9 |  61.8  |  63.7  | 42.0 | 60.85 |
| Updataed   |      |        |        |      |      |
| bart-base  | 73.03 |  61.25  |  61.51  | 38.78 | 58.64 |
| cpt-base   | 74.40 |  61.23  |  62.09  | 38.81 | 59.13 |
| bart-large | 75.81 |  61.52  |  64.62  | 40.90 | 60.71 |
| cpt-large  | 75.97 |  61.63  |  63.83  | 42.08 | 60.88 |

The result shows that the updated models maintain comparative performance compared with previous checkpoints. There are still some cases that the updated model is slightly worse than the previous one, which results from the following reasons: 1) Training additional a few steps did not lead to significant performance improvement; 2) some downstream tasks are not affected by the newly added tokens and longer encoding sequences, but sensitive to the fine-tuning hyperparameters.

- Note that to use updated models, please update the  `modeling_cpt.py` (new version download [Here](https://github.com/fastnlp/CPT/blob/master/finetune/modeling_cpt.py)) and the vocabulary (refresh the cache).

## Model description

This is an implementation of Chinese BART-Large.

[**CPT: A Pre-Trained Unbalanced Transformer for Both Chinese Language Understanding and Generation**](https://arxiv.org/pdf/2109.05729.pdf)

Yunfan Shao, Zhichao Geng, Yitao Liu, Junqi Dai, Fei Yang, Li Zhe, Hujun Bao, Xipeng Qiu

**Github Link:** https://github.com/fastnlp/CPT

## Usage

```python
>>> from transformers import BertTokenizer, BartForConditionalGeneration, Text2TextGenerationPipeline
>>> tokenizer = BertTokenizer.from_pretrained("fnlp/bart-large-chinese")
>>> model = BartForConditionalGeneration.from_pretrained("fnlp/bart-large-chinese")
>>> text2text_generator = Text2TextGenerationPipeline(model, tokenizer)  
>>> text2text_generator("北京是[MASK]的首都", max_length=50, do_sample=False)
    [{'generated_text': '北 京 是 中 华 人 民 共 和 国 的 首 都'}]
```

**Note: Please use BertTokenizer for the model vocabulary. DO NOT use original BartTokenizer.**

## Citation
Shao, Y., Geng, Z., Liu, Y. et al. CPT: a pre-trained unbalanced transformer for both Chinese language understanding and generation. Sci. China Inf. Sci. 67, 152102 (2024). 
https://www.sciengine.com/SCIS/doi/10.1007/s11432-021-3536-5

```bibtex
@Article{Shao2024a,
  author   = {Shao, Yunfan and Geng, Zhichao and Liu, Yitao and Dai, Junqi and Yan, Hang and Yang, Fei and Li, Zhe and Bao, Hujun and Qiu, Xipeng},
  journal  = {Science China Information Sciences},
  title    = {CPT: a pre-trained unbalanced transformer for both Chinese language understanding and generation},
  year     = {2024},
  issn     = {1869-1919},
  number   = {5},
  pages    = {152102},
  volume   = {67},
  abstract = {In this paper, we take the advantage of previous pre-trained models (PTMs) and propose a novel Chinese pre-trained unbalanced transformer (CPT). Different from previous Chinese PTMs, CPT is designed to utilize the shared knowledge between natural language understanding (NLU) and natural language generation (NLG) to boost the performance. CPT consists of three parts: a shared encoder, an understanding decoder, and a generation decoder. Two specific decoders with a shared encoder are pre-trained with masked language modeling (MLM) and denoising auto-encoding (DAE) tasks, respectively. With the partially shared architecture and multi-task pre-training, CPT can (1) learn specific knowledge of both NLU or NLG tasks with two decoders and (2) be fine-tuned flexibly that fully exploits the potential of the model. Moreover, the unbalanced transformer saves the computational and storage cost, which makes CPT competitive and greatly accelerates the inference of text generation. Experimental results on a wide range of Chinese NLU and NLG tasks show the effectiveness of CPT.},
  doi      = {10.1007/s11432-021-3536-5},
  refid    = {Shao2024},
  url      = {https://doi.org/10.1007/s11432-021-3536-5},
}
```