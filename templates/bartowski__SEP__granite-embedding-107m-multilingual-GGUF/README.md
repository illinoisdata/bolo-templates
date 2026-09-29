---
quantized_by: bartowski
pipeline_tag: text-generation
language:
- en
- ar
- cs
- de
- es
- fr
- it
- ja
- ko
- nl
- pt
- zh
tags:
- language
- granite
- embeddings
- multilingual
license: apache-2.0
base_model: ibm-granite/granite-embedding-107m-multilingual
model-index:
- name: ibm-granite/granite-embedding-107m-multilingual
  results:
  - task:
      type: Retrieval
    dataset:
      name: Miracl (en)
      type: miracl/mmteb-miracl
      config: en
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.41176
    - type: ndcg_at_10
      value: 0.46682
    - type: ndcg_at_100
      value: 0.54326
    - type: ndcg_at_1000
      value: 0.56567
    - type: ndcg_at_20
      value: 0.50157
    - type: ndcg_at_3
      value: 0.41197
    - type: ndcg_at_5
      value: 0.42086
    - type: recall_at_1
      value: 0.19322
    - type: recall_at_10
      value: 0.57721
    - type: recall_at_100
      value: 0.83256
    - type: recall_at_1000
      value: 0.95511
    - type: recall_at_20
      value: 0.6757
    - type: recall_at_3
      value: 0.37171
    - type: recall_at_5
      value: 0.44695
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ar)
      type: miracl/mmteb-miracl
      config: ar
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.55559
    - type: ndcg_at_10
      value: 0.62541
    - type: ndcg_at_100
      value: 0.67101
    - type: ndcg_at_1000
      value: 0.6805
    - type: ndcg_at_20
      value: 0.64739
    - type: ndcg_at_3
      value: 0.56439
    - type: ndcg_at_5
      value: 0.59347
    - type: recall_at_1
      value: 0.37009
    - type: recall_at_10
      value: 0.73317
    - type: recall_at_100
      value: 0.90066
    - type: recall_at_1000
      value: 0.96272
    - type: recall_at_20
      value: 0.80205
    - type: recall_at_3
      value: 0.56903
    - type: recall_at_5
      value: 0.6518
  - task:
      type: Retrieval
    dataset:
      name: Miracl (bn)
      type: miracl/mmteb-miracl
      config: bn
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.56691
    - type: ndcg_at_10
      value: 0.65484
    - type: ndcg_at_100
      value: 0.70142
    - type: ndcg_at_1000
      value: 0.70994
    - type: ndcg_at_20
      value: 0.67838
    - type: ndcg_at_3
      value: 0.5988
    - type: ndcg_at_5
      value: 0.62718
    - type: recall_at_1
      value: 0.3605
    - type: recall_at_10
      value: 0.76854
    - type: recall_at_100
      value: 0.9285
    - type: recall_at_1000
      value: 0.97928
    - type: recall_at_20
      value: 0.83667
    - type: recall_at_3
      value: 0.61596
    - type: recall_at_5
      value: 0.69766
  - task:
      type: Retrieval
    dataset:
      name: Miracl (de)
      type: miracl/mmteb-miracl
      config: de
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.41967
    - type: ndcg_at_10
      value: 0.45141
    - type: ndcg_at_100
      value: 0.53461
    - type: ndcg_at_1000
      value: 0.55463
    - type: ndcg_at_20
      value: 0.49012
    - type: ndcg_at_3
      value: 0.39486
    - type: ndcg_at_5
      value: 0.41496
    - type: recall_at_1
      value: 0.19494
    - type: recall_at_10
      value: 0.53774
    - type: recall_at_100
      value: 0.83314
    - type: recall_at_1000
      value: 0.95045
    - type: recall_at_20
      value: 0.65659
    - type: recall_at_3
      value: 0.3556
    - type: recall_at_5
      value: 0.44448
  - task:
      type: Retrieval
    dataset:
      name: Miracl (es)
      type: miracl/mmteb-miracl
      config: es
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.54475
    - type: ndcg_at_10
      value: 0.46593
    - type: ndcg_at_100
      value: 0.58079
    - type: ndcg_at_1000
      value: 0.60656
    - type: ndcg_at_20
      value: 0.51858
    - type: ndcg_at_3
      value: 0.4578
    - type: ndcg_at_5
      value: 0.44321
    - type: recall_at_1
      value: 0.15966
    - type: recall_at_10
      value: 0.49343
    - type: recall_at_100
      value: 0.82684
    - type: recall_at_1000
      value: 0.95299
    - type: recall_at_20
      value: 0.62367
    - type: recall_at_3
      value: 0.2949
    - type: recall_at_5
      value: 0.37983
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fa)
      type: miracl/mmteb-miracl
      config: fa
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.36709
    - type: ndcg_at_10
      value: 0.46961
    - type: ndcg_at_100
      value: 0.53262
    - type: ndcg_at_1000
      value: 0.55024
    - type: ndcg_at_20
      value: 0.49892
    - type: ndcg_at_3
      value: 0.40235
    - type: ndcg_at_5
      value: 0.42866
    - type: recall_at_1
      value: 0.22735
    - type: recall_at_10
      value: 0.59949
    - type: recall_at_100
      value: 0.83867
    - type: recall_at_1000
      value: 0.95007
    - type: recall_at_20
      value: 0.68947
    - type: recall_at_3
      value: 0.41781
    - type: recall_at_5
      value: 0.49374
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fi)
      type: miracl/mmteb-miracl
      config: fi
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.59245
    - type: ndcg_at_10
      value: 0.65551
    - type: ndcg_at_100
      value: 0.6967
    - type: ndcg_at_1000
      value: 0.70521
    - type: ndcg_at_20
      value: 0.67552
    - type: ndcg_at_3
      value: 0.58876
    - type: ndcg_at_5
      value: 0.61779
    - type: recall_at_1
      value: 0.37669
    - type: recall_at_10
      value: 0.76529
    - type: recall_at_100
      value: 0.9156
    - type: recall_at_1000
      value: 0.96977
    - type: recall_at_20
      value: 0.82685
    - type: recall_at_3
      value: 0.60234
    - type: recall_at_5
      value: 0.67135
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fr)
      type: miracl/mmteb-miracl
      config: fr
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.38776
    - type: ndcg_at_10
      value: 0.47589
    - type: ndcg_at_100
      value: 0.54641
    - type: ndcg_at_1000
      value: 0.5629
    - type: ndcg_at_20
      value: 0.51203
    - type: ndcg_at_3
      value: 0.38924
    - type: ndcg_at_5
      value: 0.42572
    - type: recall_at_1
      value: 0.22082
    - type: recall_at_10
      value: 0.61619
    - type: recall_at_100
      value: 0.87237
    - type: recall_at_1000
      value: 0.97449
    - type: recall_at_20
      value: 0.72689
    - type: recall_at_3
      value: 0.39527
    - type: recall_at_5
      value: 0.48983
  - task:
      type: Retrieval
    dataset:
      name: Miracl (hi)
      type: miracl/mmteb-miracl
      config: hi
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.33143
    - type: ndcg_at_10
      value: 0.42084
    - type: ndcg_at_100
      value: 0.48647
    - type: ndcg_at_1000
      value: 0.50712
    - type: ndcg_at_20
      value: 0.45399
    - type: ndcg_at_3
      value: 0.34988
    - type: ndcg_at_5
      value: 0.37938
    - type: recall_at_1
      value: 0.17852
    - type: recall_at_10
      value: 0.55217
    - type: recall_at_100
      value: 0.79929
    - type: recall_at_1000
      value: 0.93434
    - type: recall_at_20
      value: 0.65231
    - type: recall_at_3
      value: 0.33765
    - type: recall_at_5
      value: 0.43828
  - task:
      type: Retrieval
    dataset:
      name: Miracl (id)
      type: miracl/mmteb-miracl
      config: id
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.43854
    - type: ndcg_at_10
      value: 0.45459
    - type: ndcg_at_100
      value: 0.53643
    - type: ndcg_at_1000
      value: 0.56052
    - type: ndcg_at_20
      value: 0.48795
    - type: ndcg_at_3
      value: 0.41041
    - type: ndcg_at_5
      value: 0.42235
    - type: recall_at_1
      value: 0.19193
    - type: recall_at_10
      value: 0.5289
    - type: recall_at_100
      value: 0.79649
    - type: recall_at_1000
      value: 0.92937
    - type: recall_at_20
      value: 0.61813
    - type: recall_at_3
      value: 0.35431
    - type: recall_at_5
      value: 0.43348
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ja)
      type: miracl/mmteb-miracl
      config: ja
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.53256
    - type: ndcg_at_10
      value: 0.59922
    - type: ndcg_at_100
      value: 0.65407
    - type: ndcg_at_1000
      value: 0.66484
    - type: ndcg_at_20
      value: 0.62596
    - type: ndcg_at_3
      value: 0.53717
    - type: ndcg_at_5
      value: 0.56523
    - type: recall_at_1
      value: 0.34555
    - type: recall_at_10
      value: 0.71476
    - type: recall_at_100
      value: 0.91152
    - type: recall_at_1000
      value: 0.97728
    - type: recall_at_20
      value: 0.79811
    - type: recall_at_3
      value: 0.53482
    - type: recall_at_5
      value: 0.62327
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ko)
      type: miracl/mmteb-miracl
      config: ko
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.5493
    - type: ndcg_at_10
      value: 0.58413
    - type: ndcg_at_100
      value: 0.64374
    - type: ndcg_at_1000
      value: 0.65655
    - type: ndcg_at_20
      value: 0.61732
    - type: ndcg_at_3
      value: 0.53068
    - type: ndcg_at_5
      value: 0.55202
    - type: recall_at_1
      value: 0.32602
    - type: recall_at_10
      value: 0.68647
    - type: recall_at_100
      value: 0.87746
    - type: recall_at_1000
      value: 0.95524
    - type: recall_at_20
      value: 0.78089
    - type: recall_at_3
      value: 0.49173
    - type: recall_at_5
      value: 0.5827
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ru)
      type: miracl/mmteb-miracl
      config: ru
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.43131
    - type: ndcg_at_10
      value: 0.48262
    - type: ndcg_at_100
      value: 0.56158
    - type: ndcg_at_1000
      value: 0.57929
    - type: ndcg_at_20
      value: 0.52023
    - type: ndcg_at_3
      value: 0.42808
    - type: ndcg_at_5
      value: 0.44373
    - type: recall_at_1
      value: 0.22018
    - type: recall_at_10
      value: 0.58034
    - type: recall_at_100
      value: 0.84074
    - type: recall_at_1000
      value: 0.93938
    - type: recall_at_20
      value: 0.68603
    - type: recall_at_3
      value: 0.39307
    - type: recall_at_5
      value: 0.47077
  - task:
      type: Retrieval
    dataset:
      name: Miracl (sw)
      type: miracl/mmteb-miracl
      config: sw
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.50415
    - type: ndcg_at_10
      value: 0.59111
    - type: ndcg_at_100
      value: 0.64312
    - type: ndcg_at_1000
      value: 0.65089
    - type: ndcg_at_20
      value: 0.61651
    - type: ndcg_at_3
      value: 0.5304
    - type: ndcg_at_5
      value: 0.56139
    - type: recall_at_1
      value: 0.33267
    - type: recall_at_10
      value: 0.72082
    - type: recall_at_100
      value: 0.91377
    - type: recall_at_1000
      value: 0.96152
    - type: recall_at_20
      value: 0.79943
    - type: recall_at_3
      value: 0.5548
    - type: recall_at_5
      value: 0.64302
  - task:
      type: Retrieval
    dataset:
      name: Miracl (te)
      type: miracl/mmteb-miracl
      config: te
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.64372
    - type: ndcg_at_10
      value: 0.78175
    - type: ndcg_at_100
      value: 0.79523
    - type: ndcg_at_1000
      value: 0.79774
    - type: ndcg_at_20
      value: 0.78826
    - type: ndcg_at_3
      value: 0.74856
    - type: ndcg_at_5
      value: 0.77128
    - type: recall_at_1
      value: 0.63688
    - type: recall_at_10
      value: 0.90358
    - type: recall_at_100
      value: 0.96558
    - type: recall_at_1000
      value: 0.9847
    - type: recall_at_20
      value: 0.92834
    - type: recall_at_3
      value: 0.81804
    - type: recall_at_5
      value: 0.87198
  - task:
      type: Retrieval
    dataset:
      name: Miracl (th)
      type: miracl/mmteb-miracl
      config: th
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.65484
    - type: ndcg_at_10
      value: 0.71774
    - type: ndcg_at_100
      value: 0.75362
    - type: ndcg_at_1000
      value: 0.75898
    - type: ndcg_at_20
      value: 0.73709
    - type: ndcg_at_3
      value: 0.66199
    - type: ndcg_at_5
      value: 0.68451
    - type: recall_at_1
      value: 0.45911
    - type: recall_at_10
      value: 0.82619
    - type: recall_at_100
      value: 0.95515
    - type: recall_at_1000
      value: 0.98854
    - type: recall_at_20
      value: 0.88447
    - type: recall_at_3
      value: 0.67437
    - type: recall_at_5
      value: 0.73786
  - task:
      type: Retrieval
    dataset:
      name: Miracl (yo)
      type: miracl/mmteb-miracl
      config: yo
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.46218
    - type: ndcg_at_10
      value: 0.64685
    - type: ndcg_at_100
      value: 0.66941
    - type: ndcg_at_1000
      value: 0.67361
    - type: ndcg_at_20
      value: 0.65548
    - type: ndcg_at_3
      value: 0.57609
    - type: ndcg_at_5
      value: 0.62021
    - type: recall_at_1
      value: 0.42787
    - type: recall_at_10
      value: 0.82913
    - type: recall_at_100
      value: 0.93277
    - type: recall_at_1000
      value: 0.96499
    - type: recall_at_20
      value: 0.85994
    - type: recall_at_3
      value: 0.65406
    - type: recall_at_5
      value: 0.7542
  - task:
      type: Retrieval
    dataset:
      name: Miracl (zh)
      type: miracl/mmteb-miracl
      config: zh
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.41985
    - type: ndcg_at_10
      value: 0.4837
    - type: ndcg_at_100
      value: 0.55961
    - type: ndcg_at_1000
      value: 0.5762
    - type: ndcg_at_20
      value: 0.51595
    - type: ndcg_at_3
      value: 0.42094
    - type: ndcg_at_5
      value: 0.44273
    - type: recall_at_1
      value: 0.21446
    - type: recall_at_10
      value: 0.59695
    - type: recall_at_100
      value: 0.87388
    - type: recall_at_1000
      value: 0.96833
    - type: recall_at_20
      value: 0.69252
    - type: recall_at_3
      value: 0.40377
    - type: recall_at_5
      value: 0.4903
---

## Llamacpp Static Quantizations of granite-embedding-107m-multilingual

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b4381">b4381</a> for quantization.

Original model: https://huggingface.co/ibm-granite/granite-embedding-107m-multilingual

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

No prompt format found, check original model page

## What's new:

Fix tokenizer

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [granite-embedding-107m-multilingual-f16.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-f16.gguf) | f16 | 0.22GB | false | Full F16 weights. |
| [granite-embedding-107m-multilingual-Q8_0.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q8_0.gguf) | Q8_0 | 0.12GB | false | Extremely high quality, generally unneeded but max available quant. |
| [granite-embedding-107m-multilingual-Q6_K_L.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q6_K_L.gguf) | Q6_K_L | 0.12GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [granite-embedding-107m-multilingual-Q6_K.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q6_K.gguf) | Q6_K | 0.12GB | false | Very high quality, near perfect, *recommended*. |
| [granite-embedding-107m-multilingual-Q5_K_L.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q5_K_L.gguf) | Q5_K_L | 0.12GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [granite-embedding-107m-multilingual-Q5_K_M.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q5_K_M.gguf) | Q5_K_M | 0.12GB | false | High quality, *recommended*. |
| [granite-embedding-107m-multilingual-Q5_K_S.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q5_K_S.gguf) | Q5_K_S | 0.12GB | false | High quality, *recommended*. |
| [granite-embedding-107m-multilingual-Q4_K_L.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q4_K_L.gguf) | Q4_K_L | 0.12GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [granite-embedding-107m-multilingual-Q4_K_M.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q4_K_M.gguf) | Q4_K_M | 0.12GB | false | Good quality, default size for most use cases, *recommended*. |
| [granite-embedding-107m-multilingual-Q4_K_S.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q4_K_S.gguf) | Q4_K_S | 0.12GB | false | Slightly lower quality with more space savings, *recommended*. |
| [granite-embedding-107m-multilingual-Q4_0.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q4_0.gguf) | Q4_0 | 0.12GB | false | Legacy format, offers online repacking for ARM and AVX CPU inference. |
| [granite-embedding-107m-multilingual-IQ4_NL.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-IQ4_NL.gguf) | IQ4_NL | 0.12GB | false | Similar to IQ4_XS, but slightly larger. Offers online repacking for ARM CPU inference. |
| [granite-embedding-107m-multilingual-IQ4_XS.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-IQ4_XS.gguf) | IQ4_XS | 0.12GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [granite-embedding-107m-multilingual-Q3_K_XL.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q3_K_XL.gguf) | Q3_K_XL | 0.12GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [granite-embedding-107m-multilingual-Q3_K_L.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q3_K_L.gguf) | Q3_K_L | 0.12GB | false | Lower quality but usable, good for low RAM availability. |
| [granite-embedding-107m-multilingual-Q3_K_M.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-Q3_K_M.gguf) | Q3_K_M | 0.12GB | false | Low quality. |
| [granite-embedding-107m-multilingual-IQ3_M.gguf](https://huggingface.co/bartowski/granite-embedding-107m-multilingual-GGUF/blob/main/granite-embedding-107m-multilingual-IQ3_M.gguf) | IQ3_M | 0.12GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

## Downloading using huggingface-cli

<details>
  <summary>Click to view download instructions</summary>

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/granite-embedding-107m-multilingual-GGUF --include "granite-embedding-107m-multilingual-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/granite-embedding-107m-multilingual-GGUF --include "granite-embedding-107m-multilingual-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (granite-embedding-107m-multilingual-Q8_0) or download them all in place (./)

</details>

## ARM/AVX information

Previously, you would download Q4_0_4_4/4_8/8_8, and these would have their weights interleaved in memory in order to improve performance on ARM and AVX machines by loading up more data in one pass.

Now, however, there is something called "online repacking" for weights. details in [this PR](https://github.com/ggerganov/llama.cpp/pull/9921). If you use Q4_0 and your hardware would benefit from repacking weights, it will do it automatically on the fly.

As of llama.cpp build [b4282](https://github.com/ggerganov/llama.cpp/releases/tag/b4282) you will not be able to run the Q4_0_X_X files and will instead need to use Q4_0.

Additionally, if you want to get slightly better quality for , you can use IQ4_NL thanks to [this PR](https://github.com/ggerganov/llama.cpp/pull/10541) which will also repack the weights for ARM, though only the 4_4 for now. The loading time may be slower but it will result in an overall speed incrase.

<details>
  <summary>Click to view Q4_0_X_X information (deprecated</summary>

I'm keeping this section to show the potential theoretical uplift in performance from using the Q4_0 with online repacking.

<details>
  <summary>Click to view benchmarks on an AVX2 system (EPYC7702)</summary>

| model                          |       size |     params | backend    | threads |          test |                  t/s |  % (vs Q4_0)  |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | ------------: | -------------------: |-------------: |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         pp512 |        204.03 ± 1.03 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |        pp1024 |        282.92 ± 0.19 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |        pp2048 |        259.49 ± 0.44 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg128 |         39.12 ± 0.27 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg256 |         39.31 ± 0.69 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg512 |         40.52 ± 0.03 |          100% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         pp512 |        301.02 ± 1.74 |          147% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |        pp1024 |        287.23 ± 0.20 |          101% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |        pp2048 |        262.77 ± 1.81 |          101% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg128 |         18.80 ± 0.99 |           48% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg256 |         24.46 ± 3.04 |           83% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg512 |         36.32 ± 3.59 |           90% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         pp512 |        271.71 ± 3.53 |          133% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |        pp1024 |       279.86 ± 45.63 |          100% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |        pp2048 |        320.77 ± 5.00 |          124% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg128 |         43.51 ± 0.05 |          111% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg256 |         43.35 ± 0.09 |          110% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg512 |         42.60 ± 0.31 |          105% |

Q4_0_8_8 offers a nice bump to prompt processing and a small bump to text generation

</details>

</details>

## Which file should I choose?

<details>
  <summary>Click here for details</summary>

A great write up with charts showing various performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.

If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.

If you want to get more into the weeds, you can check out this extremely useful feature chart:

[llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU and Apple Metal, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

The I-quants are *not* compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

</details>

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset.

Thank you ZeroWw for the inspiration to experiment with embed/output.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski