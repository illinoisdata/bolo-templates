---
license: apache-2.0
datasets:
- anon8231489123/ShareGPT_Vicuna_unfiltered
language:
- en
pipeline_tag: text-generation
---
## Model description
This is a Vicuna-like model with only 68M parameters, which is fine-tuned from [LLaMA-68m](https://huggingface.co/JackFram/llama-68m) on [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) data.

The training setup follows the [Vicuna suite](https://github.com/lm-sys/FastChat).

The model is mainly developed as a base Small Speculative Model in the [MCSD paper](https://arxiv.org/pdf/2401.06706.pdf). As a comparison, it can be better aligned to the Vicuna models than LLaMA-68m with little loss of alignment to the LLaMA models.


| Draft Model    | Target Model  | Alignment |
| -------------- | ------------- | --------- |
| LLaMA-68/160M  | LLaMA-13/33B  | 😃        |
| LLaMA-68/160M  | Vicuna-13/33B | 😟        |
| Vicuna-68/160M | LLaMA-13/33B  | 😃        |
| Vicuna-68/160M | Vicuna-13/33B | 😃        |