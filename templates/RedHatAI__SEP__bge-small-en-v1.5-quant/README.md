---
tags:
- mteb
- sparse 
- sparsity 
- quantized 
- onnx 
- embeddings 
- int8
- deepsparse
model-index:
- name: bge-small-en-v1.5-quant
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 74.19402985074626
    - type: ap
      value: 37.562368912364036
    - type: f1
      value: 68.47046663470138
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
    metrics:
    - type: accuracy
      value: 91.89432499999998
    - type: ap
      value: 88.64572979375352
    - type: f1
      value: 91.87171177424113
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 46.71799999999999
    - type: f1
      value: 46.25791412217894
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 34.424
    - type: map_at_10
      value: 49.63
    - type: map_at_100
      value: 50.477000000000004
    - type: map_at_1000
      value: 50.483
    - type: map_at_3
      value: 45.389
    - type: map_at_5
      value: 47.888999999999996
    - type: mrr_at_1
      value: 34.78
    - type: mrr_at_10
      value: 49.793
    - type: mrr_at_100
      value: 50.632999999999996
    - type: mrr_at_1000
      value: 50.638000000000005
    - type: mrr_at_3
      value: 45.531
    - type: mrr_at_5
      value: 48.010000000000005
    - type: ndcg_at_1
      value: 34.424
    - type: ndcg_at_10
      value: 57.774
    - type: ndcg_at_100
      value: 61.248000000000005
    - type: ndcg_at_1000
      value: 61.378
    - type: ndcg_at_3
      value: 49.067
    - type: ndcg_at_5
      value: 53.561
    - type: precision_at_1
      value: 34.424
    - type: precision_at_10
      value: 8.364
    - type: precision_at_100
      value: 0.985
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 19.915
    - type: precision_at_5
      value: 14.124999999999998
    - type: recall_at_1
      value: 34.424
    - type: recall_at_10
      value: 83.64200000000001
    - type: recall_at_100
      value: 98.506
    - type: recall_at_1000
      value: 99.502
    - type: recall_at_3
      value: 59.744
    - type: recall_at_5
      value: 70.626
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
    metrics:
    - type: v_measure
      value: 46.91874634333147
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
    metrics:
    - type: v_measure
      value: 39.1201020016146
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
    metrics:
    - type: map
      value: 62.40334669601722
    - type: mrr
      value: 75.33175042870333
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_pearson
      value: 88.00433892980047
    - type: cos_sim_spearman
      value: 86.65558896421105
    - type: euclidean_pearson
      value: 85.98927300398377
    - type: euclidean_spearman
      value: 86.0905158476729
    - type: manhattan_pearson
      value: 86.0272425017433
    - type: manhattan_spearman
      value: 85.8929209838941
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
    metrics:
    - type: accuracy
      value: 85.1038961038961
    - type: f1
      value: 85.06851570045757
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
    metrics:
    - type: v_measure
      value: 37.42637694389153
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
    metrics:
    - type: v_measure
      value: 33.89440321125906
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 28.111000000000004
    - type: map_at_10
      value: 39.067
    - type: map_at_100
      value: 40.519
    - type: map_at_1000
      value: 40.652
    - type: map_at_3
      value: 35.571999999999996
    - type: map_at_5
      value: 37.708999999999996
    - type: mrr_at_1
      value: 34.335
    - type: mrr_at_10
      value: 44.868
    - type: mrr_at_100
      value: 45.607
    - type: mrr_at_1000
      value: 45.655
    - type: mrr_at_3
      value: 41.798
    - type: mrr_at_5
      value: 43.786
    - type: ndcg_at_1
      value: 34.335
    - type: ndcg_at_10
      value: 45.513
    - type: ndcg_at_100
      value: 51.037
    - type: ndcg_at_1000
      value: 53.171
    - type: ndcg_at_3
      value: 40.131
    - type: ndcg_at_5
      value: 43.027
    - type: precision_at_1
      value: 34.335
    - type: precision_at_10
      value: 8.784
    - type: precision_at_100
      value: 1.4460000000000002
    - type: precision_at_1000
      value: 0.193
    - type: precision_at_3
      value: 19.361
    - type: precision_at_5
      value: 14.249
    - type: recall_at_1
      value: 28.111000000000004
    - type: recall_at_10
      value: 58.372
    - type: recall_at_100
      value: 81.631
    - type: recall_at_1000
      value: 95.192
    - type: recall_at_3
      value: 42.863
    - type: recall_at_5
      value: 50.924
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 28.437
    - type: map_at_10
      value: 37.942
    - type: map_at_100
      value: 39.108
    - type: map_at_1000
      value: 39.242
    - type: map_at_3
      value: 35.419
    - type: map_at_5
      value: 36.825
    - type: mrr_at_1
      value: 35.35
    - type: mrr_at_10
      value: 43.855
    - type: mrr_at_100
      value: 44.543
    - type: mrr_at_1000
      value: 44.588
    - type: mrr_at_3
      value: 41.826
    - type: mrr_at_5
      value: 42.937
    - type: ndcg_at_1
      value: 35.35
    - type: ndcg_at_10
      value: 43.32
    - type: ndcg_at_100
      value: 47.769
    - type: ndcg_at_1000
      value: 49.979
    - type: ndcg_at_3
      value: 39.709
    - type: ndcg_at_5
      value: 41.316
    - type: precision_at_1
      value: 35.35
    - type: precision_at_10
      value: 7.994
    - type: precision_at_100
      value: 1.323
    - type: precision_at_1000
      value: 0.182
    - type: precision_at_3
      value: 18.96
    - type: precision_at_5
      value: 13.236
    - type: recall_at_1
      value: 28.437
    - type: recall_at_10
      value: 52.531000000000006
    - type: recall_at_100
      value: 71.79299999999999
    - type: recall_at_1000
      value: 85.675
    - type: recall_at_3
      value: 41.605
    - type: recall_at_5
      value: 46.32
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 37.364999999999995
    - type: map_at_10
      value: 49.324
    - type: map_at_100
      value: 50.458999999999996
    - type: map_at_1000
      value: 50.512
    - type: map_at_3
      value: 45.96
    - type: map_at_5
      value: 47.934
    - type: mrr_at_1
      value: 43.009
    - type: mrr_at_10
      value: 52.946000000000005
    - type: mrr_at_100
      value: 53.74100000000001
    - type: mrr_at_1000
      value: 53.76800000000001
    - type: mrr_at_3
      value: 50.554
    - type: mrr_at_5
      value: 51.964
    - type: ndcg_at_1
      value: 43.009
    - type: ndcg_at_10
      value: 55.143
    - type: ndcg_at_100
      value: 59.653999999999996
    - type: ndcg_at_1000
      value: 60.805
    - type: ndcg_at_3
      value: 49.605
    - type: ndcg_at_5
      value: 52.437
    - type: precision_at_1
      value: 43.009
    - type: precision_at_10
      value: 8.984
    - type: precision_at_100
      value: 1.209
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_3
      value: 22.09
    - type: precision_at_5
      value: 15.423
    - type: recall_at_1
      value: 37.364999999999995
    - type: recall_at_10
      value: 68.657
    - type: recall_at_100
      value: 88.155
    - type: recall_at_1000
      value: 96.48400000000001
    - type: recall_at_3
      value: 54.186
    - type: recall_at_5
      value: 60.848
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 23.827
    - type: map_at_10
      value: 31.721
    - type: map_at_100
      value: 32.812999999999995
    - type: map_at_1000
      value: 32.89
    - type: map_at_3
      value: 29.238999999999997
    - type: map_at_5
      value: 30.584
    - type: mrr_at_1
      value: 25.650000000000002
    - type: mrr_at_10
      value: 33.642
    - type: mrr_at_100
      value: 34.595
    - type: mrr_at_1000
      value: 34.650999999999996
    - type: mrr_at_3
      value: 31.205
    - type: mrr_at_5
      value: 32.499
    - type: ndcg_at_1
      value: 25.650000000000002
    - type: ndcg_at_10
      value: 36.366
    - type: ndcg_at_100
      value: 41.766
    - type: ndcg_at_1000
      value: 43.735
    - type: ndcg_at_3
      value: 31.447000000000003
    - type: ndcg_at_5
      value: 33.701
    - type: precision_at_1
      value: 25.650000000000002
    - type: precision_at_10
      value: 5.582
    - type: precision_at_100
      value: 0.872
    - type: precision_at_1000
      value: 0.108
    - type: precision_at_3
      value: 13.107
    - type: precision_at_5
      value: 9.198
    - type: recall_at_1
      value: 23.827
    - type: recall_at_10
      value: 48.9
    - type: recall_at_100
      value: 73.917
    - type: recall_at_1000
      value: 88.787
    - type: recall_at_3
      value: 35.498000000000005
    - type: recall_at_5
      value: 40.929
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 15.47
    - type: map_at_10
      value: 22.679
    - type: map_at_100
      value: 23.823
    - type: map_at_1000
      value: 23.94
    - type: map_at_3
      value: 20.535999999999998
    - type: map_at_5
      value: 21.61
    - type: mrr_at_1
      value: 18.781
    - type: mrr_at_10
      value: 26.979
    - type: mrr_at_100
      value: 27.945999999999998
    - type: mrr_at_1000
      value: 28.016000000000002
    - type: mrr_at_3
      value: 24.648
    - type: mrr_at_5
      value: 25.947
    - type: ndcg_at_1
      value: 18.781
    - type: ndcg_at_10
      value: 27.55
    - type: ndcg_at_100
      value: 33.176
    - type: ndcg_at_1000
      value: 36.150999999999996
    - type: ndcg_at_3
      value: 23.456
    - type: ndcg_at_5
      value: 25.16
    - type: precision_at_1
      value: 18.781
    - type: precision_at_10
      value: 5.050000000000001
    - type: precision_at_100
      value: 0.9039999999999999
    - type: precision_at_1000
      value: 0.129
    - type: precision_at_3
      value: 11.235000000000001
    - type: precision_at_5
      value: 8.01
    - type: recall_at_1
      value: 15.47
    - type: recall_at_10
      value: 38.446000000000005
    - type: recall_at_100
      value: 63.199000000000005
    - type: recall_at_1000
      value: 84.719
    - type: recall_at_3
      value: 26.687
    - type: recall_at_5
      value: 31.196
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.285999999999998
    - type: map_at_10
      value: 35.701
    - type: map_at_100
      value: 37.062
    - type: map_at_1000
      value: 37.175999999999995
    - type: map_at_3
      value: 32.65
    - type: map_at_5
      value: 34.129
    - type: mrr_at_1
      value: 32.05
    - type: mrr_at_10
      value: 41.105000000000004
    - type: mrr_at_100
      value: 41.996
    - type: mrr_at_1000
      value: 42.047000000000004
    - type: mrr_at_3
      value: 38.466
    - type: mrr_at_5
      value: 39.766
    - type: ndcg_at_1
      value: 32.05
    - type: ndcg_at_10
      value: 41.516999999999996
    - type: ndcg_at_100
      value: 47.083999999999996
    - type: ndcg_at_1000
      value: 49.309
    - type: ndcg_at_3
      value: 36.254999999999995
    - type: ndcg_at_5
      value: 38.346999999999994
    - type: precision_at_1
      value: 32.05
    - type: precision_at_10
      value: 7.536
    - type: precision_at_100
      value: 1.202
    - type: precision_at_1000
      value: 0.158
    - type: precision_at_3
      value: 17.004
    - type: precision_at_5
      value: 11.973
    - type: recall_at_1
      value: 26.285999999999998
    - type: recall_at_10
      value: 53.667
    - type: recall_at_100
      value: 76.97
    - type: recall_at_1000
      value: 91.691
    - type: recall_at_3
      value: 38.571
    - type: recall_at_5
      value: 44.131
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 22.595000000000002
    - type: map_at_10
      value: 31.352000000000004
    - type: map_at_100
      value: 32.652
    - type: map_at_1000
      value: 32.774
    - type: map_at_3
      value: 28.238000000000003
    - type: map_at_5
      value: 30.178
    - type: mrr_at_1
      value: 27.626
    - type: mrr_at_10
      value: 36.351
    - type: mrr_at_100
      value: 37.297000000000004
    - type: mrr_at_1000
      value: 37.362
    - type: mrr_at_3
      value: 33.885
    - type: mrr_at_5
      value: 35.358000000000004
    - type: ndcg_at_1
      value: 27.626
    - type: ndcg_at_10
      value: 36.795
    - type: ndcg_at_100
      value: 42.808
    - type: ndcg_at_1000
      value: 45.417
    - type: ndcg_at_3
      value: 31.744
    - type: ndcg_at_5
      value: 34.407
    - type: precision_at_1
      value: 27.626
    - type: precision_at_10
      value: 6.781
    - type: precision_at_100
      value: 1.159
    - type: precision_at_1000
      value: 0.155
    - type: precision_at_3
      value: 15.221000000000002
    - type: precision_at_5
      value: 11.279
    - type: recall_at_1
      value: 22.595000000000002
    - type: recall_at_10
      value: 48.126000000000005
    - type: recall_at_100
      value: 74.24300000000001
    - type: recall_at_1000
      value: 92.276
    - type: recall_at_3
      value: 34.346
    - type: recall_at_5
      value: 41.065000000000005
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 22.237000000000002
    - type: map_at_10
      value: 28.626
    - type: map_at_100
      value: 29.494999999999997
    - type: map_at_1000
      value: 29.587999999999997
    - type: map_at_3
      value: 26.747
    - type: map_at_5
      value: 27.903
    - type: mrr_at_1
      value: 24.847
    - type: mrr_at_10
      value: 31.091
    - type: mrr_at_100
      value: 31.91
    - type: mrr_at_1000
      value: 31.977
    - type: mrr_at_3
      value: 29.218
    - type: mrr_at_5
      value: 30.391000000000002
    - type: ndcg_at_1
      value: 24.847
    - type: ndcg_at_10
      value: 32.452999999999996
    - type: ndcg_at_100
      value: 37.009
    - type: ndcg_at_1000
      value: 39.425
    - type: ndcg_at_3
      value: 28.848000000000003
    - type: ndcg_at_5
      value: 30.752000000000002
    - type: precision_at_1
      value: 24.847
    - type: precision_at_10
      value: 4.968999999999999
    - type: precision_at_100
      value: 0.8009999999999999
    - type: precision_at_1000
      value: 0.107
    - type: precision_at_3
      value: 12.321
    - type: precision_at_5
      value: 8.62
    - type: recall_at_1
      value: 22.237000000000002
    - type: recall_at_10
      value: 41.942
    - type: recall_at_100
      value: 62.907000000000004
    - type: recall_at_1000
      value: 81.035
    - type: recall_at_3
      value: 32.05
    - type: recall_at_5
      value: 36.695
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 14.835
    - type: map_at_10
      value: 21.124000000000002
    - type: map_at_100
      value: 22.133
    - type: map_at_1000
      value: 22.258
    - type: map_at_3
      value: 19.076999999999998
    - type: map_at_5
      value: 20.18
    - type: mrr_at_1
      value: 17.791
    - type: mrr_at_10
      value: 24.438
    - type: mrr_at_100
      value: 25.332
    - type: mrr_at_1000
      value: 25.417
    - type: mrr_at_3
      value: 22.425
    - type: mrr_at_5
      value: 23.524
    - type: ndcg_at_1
      value: 17.791
    - type: ndcg_at_10
      value: 25.27
    - type: ndcg_at_100
      value: 30.362000000000002
    - type: ndcg_at_1000
      value: 33.494
    - type: ndcg_at_3
      value: 21.474
    - type: ndcg_at_5
      value: 23.189999999999998
    - type: precision_at_1
      value: 17.791
    - type: precision_at_10
      value: 4.58
    - type: precision_at_100
      value: 0.839
    - type: precision_at_1000
      value: 0.128
    - type: precision_at_3
      value: 10.071
    - type: precision_at_5
      value: 7.337000000000001
    - type: recall_at_1
      value: 14.835
    - type: recall_at_10
      value: 34.534
    - type: recall_at_100
      value: 57.812
    - type: recall_at_1000
      value: 80.467
    - type: recall_at_3
      value: 23.938000000000002
    - type: recall_at_5
      value: 28.269
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 23.400000000000002
    - type: map_at_10
      value: 31.55
    - type: map_at_100
      value: 32.72
    - type: map_at_1000
      value: 32.830999999999996
    - type: map_at_3
      value: 28.942
    - type: map_at_5
      value: 30.403000000000002
    - type: mrr_at_1
      value: 27.705000000000002
    - type: mrr_at_10
      value: 35.778
    - type: mrr_at_100
      value: 36.705
    - type: mrr_at_1000
      value: 36.773
    - type: mrr_at_3
      value: 33.458
    - type: mrr_at_5
      value: 34.778
    - type: ndcg_at_1
      value: 27.705000000000002
    - type: ndcg_at_10
      value: 36.541000000000004
    - type: ndcg_at_100
      value: 42.016999999999996
    - type: ndcg_at_1000
      value: 44.571
    - type: ndcg_at_3
      value: 31.845000000000002
    - type: ndcg_at_5
      value: 34.056
    - type: precision_at_1
      value: 27.705000000000002
    - type: precision_at_10
      value: 6.166
    - type: precision_at_100
      value: 0.993
    - type: precision_at_1000
      value: 0.132
    - type: precision_at_3
      value: 14.302999999999999
    - type: precision_at_5
      value: 10.187
    - type: recall_at_1
      value: 23.400000000000002
    - type: recall_at_10
      value: 47.61
    - type: recall_at_100
      value: 71.69200000000001
    - type: recall_at_1000
      value: 89.652
    - type: recall_at_3
      value: 35.026
    - type: recall_at_5
      value: 40.48
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 21.409
    - type: map_at_10
      value: 29.642000000000003
    - type: map_at_100
      value: 31.213
    - type: map_at_1000
      value: 31.418000000000003
    - type: map_at_3
      value: 26.811
    - type: map_at_5
      value: 28.433999999999997
    - type: mrr_at_1
      value: 25.494
    - type: mrr_at_10
      value: 33.735
    - type: mrr_at_100
      value: 34.791
    - type: mrr_at_1000
      value: 34.848
    - type: mrr_at_3
      value: 31.225
    - type: mrr_at_5
      value: 32.688
    - type: ndcg_at_1
      value: 25.494
    - type: ndcg_at_10
      value: 35.038000000000004
    - type: ndcg_at_100
      value: 41.499
    - type: ndcg_at_1000
      value: 44.183
    - type: ndcg_at_3
      value: 30.305
    - type: ndcg_at_5
      value: 32.607
    - type: precision_at_1
      value: 25.494
    - type: precision_at_10
      value: 6.739000000000001
    - type: precision_at_100
      value: 1.439
    - type: precision_at_1000
      value: 0.233
    - type: precision_at_3
      value: 14.163
    - type: precision_at_5
      value: 10.474
    - type: recall_at_1
      value: 21.409
    - type: recall_at_10
      value: 46.033
    - type: recall_at_100
      value: 74.932
    - type: recall_at_1000
      value: 92.35600000000001
    - type: recall_at_3
      value: 32.858
    - type: recall_at_5
      value: 38.675
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 18.145
    - type: map_at_10
      value: 24.712
    - type: map_at_100
      value: 25.813000000000002
    - type: map_at_1000
      value: 25.935000000000002
    - type: map_at_3
      value: 22.33
    - type: map_at_5
      value: 23.524
    - type: mrr_at_1
      value: 19.224
    - type: mrr_at_10
      value: 26.194
    - type: mrr_at_100
      value: 27.208
    - type: mrr_at_1000
      value: 27.3
    - type: mrr_at_3
      value: 23.906
    - type: mrr_at_5
      value: 24.988
    - type: ndcg_at_1
      value: 19.224
    - type: ndcg_at_10
      value: 29.015
    - type: ndcg_at_100
      value: 34.224
    - type: ndcg_at_1000
      value: 37.235
    - type: ndcg_at_3
      value: 24.22
    - type: ndcg_at_5
      value: 26.176
    - type: precision_at_1
      value: 19.224
    - type: precision_at_10
      value: 4.713
    - type: precision_at_100
      value: 0.787
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 10.290000000000001
    - type: precision_at_5
      value: 7.32
    - type: recall_at_1
      value: 18.145
    - type: recall_at_10
      value: 40.875
    - type: recall_at_100
      value: 64.371
    - type: recall_at_1000
      value: 86.67399999999999
    - type: recall_at_3
      value: 27.717000000000002
    - type: recall_at_5
      value: 32.381
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
    metrics:
    - type: accuracy
      value: 46.845
    - type: f1
      value: 41.70045120106269
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
    metrics:
    - type: accuracy
      value: 89.3476
    - type: ap
      value: 85.26891728027032
    - type: f1
      value: 89.33488973832894
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 92.67441860465115
    - type: f1
      value: 92.48821366022861
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 74.02872777017784
    - type: f1
      value: 57.28822860484337
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 74.01479488903833
    - type: f1
      value: 71.83716204573571
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 77.95897780766644
    - type: f1
      value: 77.80380046125542
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
    metrics:
    - type: v_measure
      value: 31.897956840478948
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
    metrics:
    - type: v_measure
      value: 30.71493744677591
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 31.279419910393734
    - type: mrr
      value: 32.41989483774563
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
    metrics:
    - type: v_measure
      value: 50.49612915002382
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
    metrics:
    - type: v_measure
      value: 60.29912718965653
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_pearson
      value: 83.86793477948164
    - type: cos_sim_spearman
      value: 79.43675709317894
    - type: euclidean_pearson
      value: 81.42564463337872
    - type: euclidean_spearman
      value: 79.39138648510273
    - type: manhattan_pearson
      value: 81.31167449689285
    - type: manhattan_spearman
      value: 79.28411420758785
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_pearson
      value: 84.43490408077298
    - type: cos_sim_spearman
      value: 76.16878340109265
    - type: euclidean_pearson
      value: 80.6016219080782
    - type: euclidean_spearman
      value: 75.67063072565917
    - type: manhattan_pearson
      value: 80.7238920179759
    - type: manhattan_spearman
      value: 75.85631683403953
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_pearson
      value: 83.03882477767792
    - type: cos_sim_spearman
      value: 84.15171505206217
    - type: euclidean_pearson
      value: 84.11692506470922
    - type: euclidean_spearman
      value: 84.78589046217311
    - type: manhattan_pearson
      value: 83.98651139454486
    - type: manhattan_spearman
      value: 84.64928563751276
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_pearson
      value: 83.11158600428418
    - type: cos_sim_spearman
      value: 81.48561519933875
    - type: euclidean_pearson
      value: 83.21025907155807
    - type: euclidean_spearman
      value: 81.68699235487654
    - type: manhattan_pearson
      value: 83.16704771658094
    - type: manhattan_spearman
      value: 81.7133110412898
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_pearson
      value: 87.1514510686502
    - type: cos_sim_spearman
      value: 88.11449450494452
    - type: euclidean_pearson
      value: 87.75854949349939
    - type: euclidean_spearman
      value: 88.4055148221637
    - type: manhattan_pearson
      value: 87.71487828059706
    - type: manhattan_spearman
      value: 88.35301381116254
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_pearson
      value: 83.36838640113687
    - type: cos_sim_spearman
      value: 84.98776974283366
    - type: euclidean_pearson
      value: 84.0617526427129
    - type: euclidean_spearman
      value: 85.04234805662242
    - type: manhattan_pearson
      value: 83.87433162971784
    - type: manhattan_spearman
      value: 84.87174280390242
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 87.72465270691285
    - type: cos_sim_spearman
      value: 87.97672332532184
    - type: euclidean_pearson
      value: 88.78764701492182
    - type: euclidean_spearman
      value: 88.3509718074474
    - type: manhattan_pearson
      value: 88.73024739256215
    - type: manhattan_spearman
      value: 88.24149566970154
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 64.65195562203238
    - type: cos_sim_spearman
      value: 65.0726777678982
    - type: euclidean_pearson
      value: 65.84698245675273
    - type: euclidean_spearman
      value: 65.13121502162804
    - type: manhattan_pearson
      value: 65.96149904857049
    - type: manhattan_spearman
      value: 65.39983948112955
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_pearson
      value: 85.2642818050049
    - type: cos_sim_spearman
      value: 86.30633382439257
    - type: euclidean_pearson
      value: 86.46510435905633
    - type: euclidean_spearman
      value: 86.62650496446
    - type: manhattan_pearson
      value: 86.2546330637872
    - type: manhattan_spearman
      value: 86.46309860938591
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
    metrics:
    - type: map
      value: 85.009977767778
    - type: mrr
      value: 95.59795143128476
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_accuracy
      value: 99.84257425742574
    - type: cos_sim_ap
      value: 96.25445889914926
    - type: cos_sim_f1
      value: 92.03805708562844
    - type: cos_sim_precision
      value: 92.1765295887663
    - type: cos_sim_recall
      value: 91.9
    - type: dot_accuracy
      value: 99.83069306930693
    - type: dot_ap
      value: 96.00517778550396
    - type: dot_f1
      value: 91.27995920448751
    - type: dot_precision
      value: 93.1321540062435
    - type: dot_recall
      value: 89.5
    - type: euclidean_accuracy
      value: 99.84455445544555
    - type: euclidean_ap
      value: 96.14761524546034
    - type: euclidean_f1
      value: 91.97751660705163
    - type: euclidean_precision
      value: 94.04388714733543
    - type: euclidean_recall
      value: 90
    - type: manhattan_accuracy
      value: 99.84158415841584
    - type: manhattan_ap
      value: 96.17014673429341
    - type: manhattan_f1
      value: 91.93790686029043
    - type: manhattan_precision
      value: 92.07622868605817
    - type: manhattan_recall
      value: 91.8
    - type: max_accuracy
      value: 99.84455445544555
    - type: max_ap
      value: 96.25445889914926
    - type: max_f1
      value: 92.03805708562844
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
    metrics:
    - type: v_measure
      value: 59.26454683321409
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
    metrics:
    - type: v_measure
      value: 33.75520575713765
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
    metrics:
    - type: map
      value: 52.74607778008495
    - type: mrr
      value: 53.55101699770818
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
    metrics:
    - type: accuracy
      value: 69.5008
    - type: ap
      value: 13.64158304183089
    - type: f1
      value: 53.50073331072236
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
    metrics:
    - type: accuracy
      value: 60.01980758347483
    - type: f1
      value: 60.35679678249753
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
    metrics:
    - type: v_measure
      value: 45.09419243325077
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 85.68874053764081
    - type: cos_sim_ap
      value: 73.26334732095694
    - type: cos_sim_f1
      value: 68.01558376272465
    - type: cos_sim_precision
      value: 64.93880489560834
    - type: cos_sim_recall
      value: 71.39841688654354
    - type: dot_accuracy
      value: 84.71121177802945
    - type: dot_ap
      value: 70.33606362522605
    - type: dot_f1
      value: 65.0887573964497
    - type: dot_precision
      value: 63.50401606425703
    - type: dot_recall
      value: 66.75461741424802
    - type: euclidean_accuracy
      value: 85.80795136198367
    - type: euclidean_ap
      value: 73.43201285001163
    - type: euclidean_f1
      value: 68.33166833166834
    - type: euclidean_precision
      value: 64.86486486486487
    - type: euclidean_recall
      value: 72.18997361477572
    - type: manhattan_accuracy
      value: 85.62317458425225
    - type: manhattan_ap
      value: 73.21212085536185
    - type: manhattan_f1
      value: 68.01681314482232
    - type: manhattan_precision
      value: 65.74735286875153
    - type: manhattan_recall
      value: 70.44854881266491
    - type: max_accuracy
      value: 85.80795136198367
    - type: max_ap
      value: 73.43201285001163
    - type: max_f1
      value: 68.33166833166834
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 88.81709162882757
    - type: cos_sim_ap
      value: 85.63540257309367
    - type: cos_sim_f1
      value: 77.9091382258904
    - type: cos_sim_precision
      value: 75.32710280373833
    - type: cos_sim_recall
      value: 80.67446874037573
    - type: dot_accuracy
      value: 88.04478596654636
    - type: dot_ap
      value: 84.16371725220706
    - type: dot_f1
      value: 76.45949643213666
    - type: dot_precision
      value: 73.54719396827655
    - type: dot_recall
      value: 79.61194949183862
    - type: euclidean_accuracy
      value: 88.9296386851399
    - type: euclidean_ap
      value: 85.71894615274715
    - type: euclidean_f1
      value: 78.12952767313823
    - type: euclidean_precision
      value: 73.7688098495212
    - type: euclidean_recall
      value: 83.03818909762857
    - type: manhattan_accuracy
      value: 88.89276982186519
    - type: manhattan_ap
      value: 85.6838514059479
    - type: manhattan_f1
      value: 78.06861875184856
    - type: manhattan_precision
      value: 75.09246088193457
    - type: manhattan_recall
      value: 81.29042192793348
    - type: max_accuracy
      value: 88.9296386851399
    - type: max_ap
      value: 85.71894615274715
    - type: max_f1
      value: 78.12952767313823
license: mit
language:
- en
---

# bge-small-en-v1.5-quant

<div>
  <img src="https://huggingface.co/zeroshot/bge-small-en-v1.5-quant/resolve/main/latency.png" alt="latency" width="500" style="display:inline-block; margin-right:10px;"/>
</div>

[DeepSparse](https://github.com/neuralmagic/deepsparse) is able to improve latency performance on a 10 core laptop by 3X and up to 5X on a 16 core AWS instance.

## Usage

This is the quantized (INT8) ONNX variant of the [bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) embeddings model accelerated with [Sparsify](https://github.com/neuralmagic/sparsify) for quantization and [DeepSparseSentenceTransformers](https://github.com/neuralmagic/deepsparse/tree/main/src/deepsparse/sentence_transformers) for inference.

```bash
pip install -U deepsparse-nightly[sentence_transformers]
```

```python
from deepsparse.sentence_transformers import DeepSparseSentenceTransformer
model = DeepSparseSentenceTransformer('neuralmagic/bge-small-en-v1.5-quant', export=False)

# Our sentences we like to encode
sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.',
    'The quick brown fox jumps over the lazy dog.']

# Sentences are encoded by calling model.encode()
embeddings = model.encode(sentences)

# Print the embeddings
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding.shape)
    print("")
```

For general questions on these models and sparsification methods, reach out to the engineering team on our [community Slack](https://join.slack.com/t/discuss-neuralmagic/shared_invite/zt-q1a1cnvo-YBoICSIw3L1dmQpjBeDurQ).