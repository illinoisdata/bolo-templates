---
license: other
license_name: tongyi-qianwen-research
license_link: https://huggingface.co/Qwen/Qwen1.5-1.8B-Chat-GGUF/blob/main/LICENSE
language:
- en
pipeline_tag: text-generation
tags:
- chat
---

# Qwen1.5-1.8B-Chat-GGUF


## Introduction

Qwen1.5 is the beta version of Qwen2, a transformer-based decoder-only language model pretrained on a large amount of data. In comparison with the previous released Qwen, the improvements include: 

* 8 model sizes, including 0.5B, 1.8B, 4B, 7B, 14B, 32B and 72B dense models, and an MoE model of 14B with 2.7B activated;
* Significant performance improvement in human preference for chat models;
* Multilingual support of both base and chat models;
* Stable support of 32K context length for models of all sizes
* No need of `trust_remote_code`.

For more details, please refer to our [blog post](https://qwenlm.github.io/blog/qwen1.5/) and [GitHub repo](https://github.com/QwenLM/Qwen1.5). 
In this repo, we provide quantized models in the GGUF formats, including `q2_k`, `q3_k_m`, `q4_0`, `q4_k_m`, `q5_0`, `q5_k_m`, `q6_k` and `q8_0`. 
To demonstrate their model quality, we follow [`llama.cpp`](https://github.com/ggerganov/llama.cpp) to evaluate their perplexity on wiki test set. Results are shown below:

|Size    | fp16    | q8_0    | q6_k    | q5_k_m  | q5_0    | q4_k_m  | q4_0    | q3_k_m  | q2_k    |
|--------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
|0.5B    | 34.20   | 34.22   | 34.31   | 33.80   | 34.02   | 34.27   | 36.74   | 38.25   | 62.14   |
|1.8B    | 15.99   | 15.99   | 15.99   | 16.09   | 16.01   | 16.22   | 16.54   | 17.03   | 19.99   |
|4B      | 13.20   | 13.21   | 13.28   | 13.24   | 13.27   | 13.61   | 13.44   | 13.67   | 15.65   |
|7B      | 14.21   | 14.24   | 14.35   | 14.32   | 14.12   | 14.35   | 14.47   | 15.11   | 16.57   |
|14B     | 10.91   | 10.91   | 10.93   | 10.98   | 10.88   | 10.92   | 10.92   | 11.24   | 12.27   |
|32B     | 8.87    | 8.89    | 8.91    | 8.94    | 8.93    | 8.96    | 9.17    | 9.14    | 10.51   |
|72B     | 7.97    | 7.99    | 7.99    | 7.99    | 8.01    | 8.00    | 8.01    | 8.06    | 8.63    |

## Model Details
Qwen1.5 is a language model series including decoder language models of different model sizes. For each size, we release the base language model and the aligned chat model. It is based on the Transformer architecture with SwiGLU activation, attention QKV bias, group query attention, mixture of sliding window attention and full attention, etc. Additionally, we have an improved tokenizer adaptive to multiple natural languages and codes. For the beta version, temporarily we did not include GQA (except for 32B) and the mixture of SWA and full attention.


## Training details
We pretrained the models with a large amount of data, and we post-trained the models with both supervised finetuning and direct preference optimization.


## Requirements
We advise you to clone [`llama.cpp`](https://github.com/ggerganov/llama.cpp) and install it following the official guide.


## How to use
Cloning the repo may be inefficient, and thus you can manually download the GGUF file that you need or use `huggingface-cli` (`pip install huggingface_hub`) as shown below:
```shell
huggingface-cli download Qwen/Qwen1.5-1.8B-Chat-GGUF qwen1_5-1_8b-chat-q8_0.gguf --local-dir . --local-dir-use-symlinks False
```

We demonstrate how to use `llama.cpp` to run Qwen1.5:
```shell
./main -m qwen1_5-1_8b-chat-q8_0.gguf -n 512 --color -i -cml -f prompts/chat-with-qwen.txt
```


## Citation

If you find our work helpful, feel free to give us a cite.

```
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}
```