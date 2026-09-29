---
license: apache-2.0
language:
- en
- pt
library_name: model2vec
base_model:
- nomic-ai/nomic-embed-text-v2-moe
pipeline_tag: feature-extraction
tags:
- mteb
model-index:
- name: cnmoro/static-nomic-large
  results:
  - dataset:
      config: default
      name: MTEB Assin2STS (default)
      revision: 0ff9c86779e06855536d8775ce5550550e1e5a2d
      split: test
      type: nilc-nlp/assin2
    metrics:
    - type: pearson
      value: 64.5329
    - type: spearman
      value: 58.7463
    - type: cosine_pearson
      value: 64.5329
    - type: cosine_spearman
      value: 58.7462
    - type: manhattan_pearson
      value: 62.2038
    - type: manhattan_spearman
      value: 58.8366
    - type: euclidean_pearson
      value: 62.0719
    - type: euclidean_spearman
      value: 58.7463
    - type: main_score
      value: 58.7462
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: pearson
      value: 69.0557
    - type: spearman
      value: 68.7811
    - type: cosine_pearson
      value: 69.0557
    - type: cosine_spearman
      value: 68.7811
    - type: manhattan_pearson
      value: 68.0266
    - type: manhattan_spearman
      value: 68.4931
    - type: euclidean_pearson
      value: 67.8127
    - type: euclidean_spearman
      value: 68.7811
    - type: main_score
      value: 68.7811
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SICK-BR-STS (default)
      revision: 0cdfb1d51ef339011c067688a3b75b82f927c097
      split: test
      type: eduagarcia/sick-br
    metrics:
    - type: pearson
      value: 69.4947
    - type: spearman
      value: 62.73950000000001
    - type: cosine_pearson
      value: 69.4947
    - type: cosine_spearman
      value: 62.739599999999996
    - type: manhattan_pearson
      value: 66.1733
    - type: manhattan_spearman
      value: 62.8382
    - type: euclidean_pearson
      value: 66.0829
    - type: euclidean_spearman
      value: 62.739599999999996
    - type: main_score
      value: 62.739599999999996
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: pearson
      value: 64.34349999999999
    - type: spearman
      value: 58.133
    - type: cosine_pearson
      value: 64.34349999999999
    - type: cosine_spearman
      value: 58.1329
    - type: manhattan_pearson
      value: 58.9803
    - type: manhattan_spearman
      value: 57.7487
    - type: euclidean_pearson
      value: 59.47280000000001
    - type: euclidean_spearman
      value: 58.133
    - type: main_score
      value: 58.1329
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: pearson
      value: 64.1057
    - type: spearman
      value: 56.583099999999995
    - type: cosine_pearson
      value: 64.1057
    - type: cosine_spearman
      value: 56.5833
    - type: manhattan_pearson
      value: 60.131299999999996
    - type: manhattan_spearman
      value: 56.4581
    - type: euclidean_pearson
      value: 60.3895
    - type: euclidean_spearman
      value: 56.5847
    - type: main_score
      value: 56.5833
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: pearson
      value: 64.35300000000001
    - type: spearman
      value: 64.21679999999999
    - type: cosine_pearson
      value: 64.35300000000001
    - type: cosine_spearman
      value: 64.21679999999999
    - type: manhattan_pearson
      value: 64.95779999999999
    - type: manhattan_spearman
      value: 63.9915
    - type: euclidean_pearson
      value: 65.1861
    - type: euclidean_spearman
      value: 64.2166
    - type: main_score
      value: 64.21679999999999
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: pearson
      value: 64.445
    - type: spearman
      value: 62.6363
    - type: cosine_pearson
      value: 64.445
    - type: cosine_spearman
      value: 62.6364
    - type: manhattan_pearson
      value: 62.79280000000001
    - type: manhattan_spearman
      value: 62.363800000000005
    - type: euclidean_pearson
      value: 63.1601
    - type: euclidean_spearman
      value: 62.6364
    - type: main_score
      value: 62.6364
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: pearson
      value: 74.6721
    - type: spearman
      value: 74.7446
    - type: cosine_pearson
      value: 74.6721
    - type: cosine_spearman
      value: 74.7445
    - type: manhattan_pearson
      value: 73.4179
    - type: manhattan_spearman
      value: 74.51950000000001
    - type: euclidean_pearson
      value: 73.694
    - type: euclidean_spearman
      value: 74.7446
    - type: main_score
      value: 74.7445
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: pearson
      value: 64.2321
    - type: spearman
      value: 64.78059999999999
    - type: cosine_pearson
      value: 64.2321
    - type: cosine_spearman
      value: 64.78059999999999
    - type: manhattan_pearson
      value: 64.5397
    - type: manhattan_spearman
      value: 64.4554
    - type: euclidean_pearson
      value: 64.84450000000001
    - type: euclidean_spearman
      value: 64.78059999999999
    - type: main_score
      value: 64.78059999999999
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 73.3702
    - type: spearman
      value: 73.34049999999999
    - type: cosine_pearson
      value: 73.3702
    - type: cosine_spearman
      value: 73.34049999999999
    - type: manhattan_pearson
      value: 73.3631
    - type: manhattan_spearman
      value: 73.1052
    - type: euclidean_pearson
      value: 73.4993
    - type: euclidean_spearman
      value: 73.34049999999999
    - type: main_score
      value: 73.34049999999999
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22.v2 (en)
      revision: d31f33a128469b20e357535c39b82fb3c3f6f2bd
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 45.0436
    - type: spearman
      value: 50.741899999999994
    - type: cosine_pearson
      value: 45.0436
    - type: cosine_spearman
      value: 50.741899999999994
    - type: manhattan_pearson
      value: 48.2923
    - type: manhattan_spearman
      value: 50.9881
    - type: euclidean_pearson
      value: 47.903600000000004
    - type: euclidean_spearman
      value: 50.741899999999994
    - type: main_score
      value: 50.741899999999994
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: pearson
      value: 60.2024
    - type: spearman
      value: 58.4387
    - type: cosine_pearson
      value: 60.2024
    - type: cosine_spearman
      value: 58.4387
    - type: manhattan_pearson
      value: 59.1592
    - type: manhattan_spearman
      value: 58.1857
    - type: euclidean_pearson
      value: 59.4892
    - type: euclidean_spearman
      value: 58.4387
    - type: main_score
      value: 58.4387
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STSBenchmarkMultilingualSTS (en)
      revision: 29afa2569dcedaaa2fe6a3dcfebab33d28b82e8c
      split: dev
      type: mteb/stsb_multi_mt
    metrics:
    - type: pearson
      value: 71.8027
    - type: spearman
      value: 71.6553
    - type: cosine_pearson
      value: 71.8027
    - type: cosine_spearman
      value: 71.6549
    - type: manhattan_pearson
      value: 70.0193
    - type: manhattan_spearman
      value: 71.2307
    - type: euclidean_pearson
      value: 70.5146
    - type: euclidean_spearman
      value: 71.6549
    - type: main_score
      value: 71.6549
    task:
      type: STS
  - dataset:
      config: pt
      name: MTEB STSBenchmarkMultilingualSTS (pt)
      revision: 29afa2569dcedaaa2fe6a3dcfebab33d28b82e8c
      split: dev
      type: mteb/stsb_multi_mt
    metrics:
    - type: pearson
      value: 71.5035
    - type: spearman
      value: 71.2337
    - type: cosine_pearson
      value: 71.5035
    - type: cosine_spearman
      value: 71.2337
    - type: manhattan_pearson
      value: 70.7969
    - type: manhattan_spearman
      value: 71.27459999999999
    - type: euclidean_pearson
      value: 70.7449
    - type: euclidean_spearman
      value: 71.2337
    - type: main_score
      value: 71.2337
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STSBenchmarkMultilingualSTS (en)
      revision: 29afa2569dcedaaa2fe6a3dcfebab33d28b82e8c
      split: test
      type: mteb/stsb_multi_mt
    metrics:
    - type: pearson
      value: 60.2024
    - type: spearman
      value: 58.4387
    - type: cosine_pearson
      value: 60.2024
    - type: cosine_spearman
      value: 58.4387
    - type: manhattan_pearson
      value: 59.1592
    - type: manhattan_spearman
      value: 58.1857
    - type: euclidean_pearson
      value: 59.4892
    - type: euclidean_spearman
      value: 58.4387
    - type: main_score
      value: 58.4387
    task:
      type: STS
  - dataset:
      config: pt
      name: MTEB STSBenchmarkMultilingualSTS (pt)
      revision: 29afa2569dcedaaa2fe6a3dcfebab33d28b82e8c
      split: test
      type: mteb/stsb_multi_mt
    metrics:
    - type: pearson
      value: 63.5201
    - type: spearman
      value: 62.578100000000006
    - type: cosine_pearson
      value: 63.5201
    - type: cosine_spearman
      value: 62.5783
    - type: manhattan_pearson
      value: 62.4579
    - type: manhattan_spearman
      value: 62.52910000000001
    - type: euclidean_pearson
      value: 62.49209999999999
    - type: euclidean_spearman
      value: 62.5783
    - type: main_score
      value: 62.5783
    task:
      type: STS
  - dataset:
      config: eng
      name: MTEB SemRel24STS (eng)
      revision: ef5c383d1b87eb8feccde3dfb7f95e42b1b050dd
      split: test
      type: SemRel/SemRel2024
    metrics:
    - type: pearson
      value: 71.6465
    - type: spearman
      value: 70.3151
    - type: cosine_pearson
      value: 71.6465
    - type: cosine_spearman
      value: 70.3151
    - type: manhattan_pearson
      value: 70.49260000000001
    - type: manhattan_spearman
      value: 70.1974
    - type: euclidean_pearson
      value: 70.763
    - type: euclidean_spearman
      value: 70.3151
    - type: main_score
      value: 70.3151
    task:
      type: STS
---

This [Model2Vec](https://github.com/MinishLab/model2vec) model was created by using [Tokenlearn](https://github.com/MinishLab/tokenlearn), with [nomic-embed-text-v2-moe](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) as a base.

The output dimension is 768.

## Usage

Load this model using the `from_pretrained` method:
```python
from model2vec import StaticModel

# Load a pretrained Model2Vec model
model = StaticModel.from_pretrained("cnmoro/nomic-embed-text-v2-moe-distilled-high-quality")

# Compute text embeddings
embeddings = model.encode(["Example sentence"])
```