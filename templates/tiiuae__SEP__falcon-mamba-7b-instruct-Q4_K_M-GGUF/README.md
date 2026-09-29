---
license: other
license_name: falcon-mamba-license
license_link: https://falconllm.tii.ae/falcon-mamba-7b-terms-and-conditions.html
base_model: tiiuae/falcon-mamba-7b-instruct
language:
- en
datasets:
- tiiuae/falcon-refinedweb
---

<img src="https://huggingface.co/datasets/tiiuae/documentation-images/resolve/main/falcon_mamba/thumbnail.png" alt="drawing" width="800"/>

**GGUF quantization of [`falcon-mamba-7b-instruct`](https://huggingface.co/tiiuae/falcon-mamba-7b-instruct) in the format `Q4_K_M`**

#  Table of Contents

0. [TL;DR](#TL;DR)
1. [Model Details](#model-details)
2. [Usage](#usage)
3. [Training Details](#training-details)
4. [Evaluation](#evaluation)


# TL;DR

# Model Details

## Model Description

- **Developed by:** [https://www.tii.ae](https://www.tii.ae)
- **Model type:** Causal decoder-only
- **Architecture:** Mamba
- **Language(s) (NLP):** Mainly English
- **License:** TII Falcon-Mamba License 2.0

<br>

# Usage

Refer to the documentation of [`llama.cpp`](https://github.com/ggerganov/llama.cpp) to understand how to run this model locally on your machine.

Download the GGUF weights with the command below:

```bash
huggingface-cli download tiiuae/falcon-mamba-7b-instruct-Q4_K_M-GGUF --include falcon-mamba-7B-instruct-Q4_K_M.gguf --local-dir ./
```
Then you can run it with:
```bash
./llama-cli -m falcon-mamba-7b-instruct-Q4_K_M-GGUF -p "Hello how are you?"
```

# Training Details

## Training Data

Falcon-Mamba has been trained with ~ 5,500 GT mainly coming from [Refined-Web](https://huggingface.co/datasets/tiiuae/falcon-refinedweb), a large volume web-only dataset filtered and deduplicated.
Similar to the others [Falcon](https://huggingface.co/tiiuae/falcon-11B) suite models, Falcon-Mamba has been trained leveraging a multi-stage training strategy to increase the context-length from 2,048 to 8,192. 
Moreover, inspired by the concept of Curriculum Learning, we carefully selected data mixtures throughout the training stages, considering both data diversity and complexity. 
Note that at inference the context-length is not relevant as the Mamba architecture has no limit on long range dependency.
At the last training stage, small portion of high-quality curated data was used to further enhance performance.

Overall, the data sources included RefinedWeb-English, high quality technical data, code data and math data extracted from public sources.
In particular, we used samples coming from [Fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) during our last training stage.

The data was tokenized with the Falcon-[7B](https://huggingface.co/tiiuae/falcon-7B)/[11B](https://huggingface.co/tiiuae/falcon-11B) tokenizer.

## Training Procedure
Falcon-Mamba-7B was trained on 256 H100 80GB GPUs for the majority of the training, using a 3D parallelism strategy (TP=1, PP=1, DP=256) combined with ZeRO.

### Training Hyperparameters

| **Hyperparameter** | **Value**  | **Comment**                               |
|--------------------|------------|-------------------------------------------|
| Precision          | `bfloat16` |                                           |
| Optimizer          | AdamW      |                                           |
| Max learning rate  | 6.4e-4     | Following a WSD (warmup-stable-decay) learning rate schedule |
| Weight decay       | 1e-1       |                                           |
| Batch size         | 2048       |                                           |


The model was trained AdamW optimizer, WSD (warmup-stable-decay) learning rate schedule, and a batch size rampup from \\(b_{\mathrm{min}}=128\\) to \\(b_{\mathrm{max}}=2048\\) during first 50 GT of training. 
In the stable phase we used maximal learning rate \\(\eta_{\mathrm{max}}=6.4 \times 10^{-4}\\), and decayed it to the minimal value \\(\eta_{\mathrm{min}}=\frac{\eta_{\mathrm{max}}}{256}\\) with exponential schedule over 500 GT. 
Also, we applied *BatchScaling* during the rampup — rescaling learning rate \\(\eta\\) so that the Adam noise temperature \\(T_{\mathrm{noise}}\equiv\frac{\eta}{\sqrt{b}}\\) is kept constant.  

### Speeds, Sizes, Times

The model training took roughly two months. 

<br>

# Evaluation

## Benchmarks

We evaluate our model on all benchmarks of the new leaderboard's version using the `lm-evaluation-harness` package, and then normalize the evaluation results with HuggingFace score normalization.


| `model name`              |`IFEval`| `BBH` |`MATH LvL5`| `GPQA`| `MUSR`|`MMLU-PRO`|`Average`| 
|:--------------------------|:------:|:-----:|:---------:|:-----:|:-----:|:--------:|:-------:|
| ***Pure SSM models***     |        |       |           |       |       |          |         |
| `FalconMamba-7B`          |  33.36 | 19.88 |    3.63   |8.05   |10.86  | 14.47    |**15.04**|
| `TRI-ML/mamba-7b-rw`<sup>*</sup>| 22.46  | 6.71  | 0.45      | 1.12  | 5.51  | 1.69     | 6.25    |
|***Hybrid SSM-attention models***   |       |           |       |       |          |         |
|`recurrentgemma-9b`        | 30.76  | 14.80 | 4.83      | 4.70  | 6.60  | 17.88    |  13.20  |
| `Zyphra/Zamba-7B-v1`<sup>*</sup>      | 24.06  | 21.12 | 3.32      | 3.03  | 7.74  | 16.02    | 12.55   |
|***Transformer models***   |        |       |           |       |       |          |         |
| `Falcon2-11B`             | 32.61  | 21.94 |    2.34   | 2.80  | 7.53  | 15.44    |  13.78  |
| `Meta-Llama-3-8B`         | 14.55  | 24.50 |    3.25   | 7.38  | 6.24  | 24.55    |  13.41  |
| `Meta-Llama-3.1-8B`       | 12.70  | 25.29 |    4.61   | 6.15  | 8.98  | 24.95    |  13.78  |
| `Mistral-7B-v0.1`         | 23.86  | 22.02 |    2.49   | 5.59  | 10.68 | 22.36    |  14.50  |
| `Mistral-Nemo-Base-2407 (12B)`       | 16.83  | 29.37 |    4.98   | 5.82  | 6.52  | 27.46    |  15.08  |
| `gemma-7B`                | 26.59  | 21.12 |    6.42   | 4.92  | 10.98 | 21.64    |**15.28**|


Also, we evaluate our model on the benchmarks of the first leaderboard using `lighteval`.


| `model name`                 |`ARC`|`HellaSwag`   |`MMLU` |`Winogrande`|`TruthfulQA`|`GSM8K`|`Average`         | 
|:-----------------------------|:------:|:---------:|:-----:|:----------:|:----------:|:-----:|:----------------:|
| ***Pure SSM models***        |        |           |       |            |            |       |                  |
| `FalconMamba-7B`<sup>*</sup>          | 62.03 |   80.82   | 62.11 |   73.64    |  53.42  | 52.54 |  **64.09**       |
| `TRI-ML/mamba-7b-rw`<sup>*</sup>         | 51.25  | 80.85     | 33.41 | 71.11      | 32.08      | 4.70  | 45.52            |
|***Hybrid SSM-attention models***|     |           |       |            |            |       |                  |
| `recurrentgemma-9b`<sup>**</sup>          |52.00   |   80.40   | 60.50 |   73.60    |   38.60    | 42.60 |  57.95           |
| `Zyphra/Zamba-7B-v1`<sup>*</sup>         | 56.14  | 82.23     | 58.11 | 79.87      | 52.88      | 30.78 |  60.00           |
|***Transformer models***      |        |           |       |            |            |       |                  |
| `Falcon2-11B`                | 59.73  | 82.91     | 58.37 | 78.30      | 52.56      | 53.83 | **64.28**        |
| `Meta-Llama-3-8B`            | 60.24  | 82.23     | 66.70 | 78.45      | 42.93      | 45.19 | 62.62            |
| `Meta-Llama-3.1-8B`            | 58.53  | 82.13     | 66.43 | 74.35      | 44.29      | 47.92 | 62.28            |
| `Mistral-7B-v0.1`            | 59.98  | 83.31     | 64.16 | 78.37      | 42.15      | 37.83 | 60.97            |
| `gemma-7B`                   | 61.09  |   82.20   | 64.56 |   79.01    |   44.79    | 50.87 |  63.75           |

Mostly, we took evaluation results from both leaderboards. For the models marked by *star* we evaluated the tasks internally, while for the models marked by two *stars* the results were taken from paper or model card.

# Technical Specifications 

## Model Architecture and Objective

Falcon-Mamba-7B is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).

The model is based on the Mamba architecture ([Gu et al., 2023](https://arxiv.org/abs/2312.00752)).

| **Hyperparameter** | **Value** | **Comment**                            |
|--------------------|-----------|----------------------------------------|
| Layers             | 64        | Number of layers                       |
| `d_model`          | 4096      | Hidden dimension                       |
| `d_state`          | 16        | The SSM state dimension                |
| Vocabulary         | 65024     | Vocabulary Size                        |
| Sequence length    | 8192      | During the last training stages        |

## Compute Infrastructure

### Hardware

Falcon-Mamba-7B was trained on AWS SageMaker, using on average 256 H100 80GB GPUs in 32 p5 instances. 

### Software

Falcon-Mamba-7B was trained on an internal distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO, high-performance Triton kernels.

<br>

# Citation

You can use the following bibtex citation: 
```
@misc{zuo2024falconmambacompetitiveattentionfree,
      title={Falcon Mamba: The First Competitive Attention-free 7B Language Model}, 
      author={Jingwei Zuo and Maksim Velikanov and Dhia Eddine Rhaiem and Ilyas Chahed and Younes Belkada and Guillaume Kunsch and Hakim Hacid},
      year={2024},
      eprint={2410.05355},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.05355}, 
}
```