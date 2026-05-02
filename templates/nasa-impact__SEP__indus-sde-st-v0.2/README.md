---
license: apache-2.0
language:
- en
library_name: transformers
tags:
- earth science
- climate
- biology
pipeline_tag: sentence-similarity
---


# Model Card for Indus SDE Sentence Transformer Stage 2

The model was first further fine tuned on sentence embedding task on top of previous ([nasa-impact/indus-sde-st-v0.1](https://huggingface.co/nasa-impact/indus-sde-st-v0.1)) using stage 2 dataset (scientific dataset) for a epoch.
Then this model is again fined tuned for 2 more epoches on [NASA SDE](https://huggingface.co/datasets/nasa-impact/nasa-sde-st-corpus) and [NASA ADS](https://huggingface.co/datasets/nasa-impact/nasa-ads-corpus) corpus.

The initial stage of Indus-SDE-ST training focused on adapting the base Indus-SDE model to comprehend general domain semantics and sentence-pair relationships. The stage 2 dataset was designed for scieinfic domain adaptation.
The primary objective was to establish a broad linguistic foundation before specializing in scientific content (for subsequent stages).
This was achieved using a diverse corpus comprising pairs from S2ORC, arxiv, PubMed, NASA ADS and NASA SDE set in a contrastive learning objective: Multiple Negatives Ranking loss.

## Dataset table

| Dataset Name              | Data Points | Type                    | Link                                                                |
| ------------------------- | ----------- | ----------------------- | ------------------------------------------------------------------- |
| S2ORC_title_abstract      | ~41.8M      | Title-Body              | [Link](https://huggingface.co/datasets/sentence-transformers/s2orc/viewer/title-abstract-pair)               |
| S2ORC_abstract_citation   | ~39.6M      | Body-Body               | [Link](https://huggingface.co/datasets/sentence-transformers/s2orc/viewer/abstract-citation-pair)               |
| S2ORC_title_citation      | ~51M        | Title-Title             | [Link](https://huggingface.co/datasets/sentence-transformers/s2orc/viewer/title-citation-pair)               |
| arxiv_title_abstract      | ~2.7M       | Title-Body              | [Link](https://www.kaggle.com/datasets/Cornell-University/arxiv/data)    |
| PubMed                    | ~ 24M       | Title-Body              | [Link](https://huggingface.co/datasets/ncbi/pubmed)                      |
| specter                   | ~684K       | Title-Body              | [Link](https://huggingface.co/datasets/sentence-transformers/specter/)             |
| nasa_ads                  | ~2.66M      | Title-Abstract          | [Link](https://huggingface.co/datasets/nasa-impact/nasa-ads-corpus)                |
| SDE-syntisaized           | 177486      | question-answer         | [Link](https://huggingface.co/datasets/nasa-impact/nasa-sde-st-corpus)                 |
| SDE-syntisaized           | 194382      | search_terms-document   |                                                                     |
| CMR-natural               | 53974       | Title-Description       |                                                                     |
| PDS-natural               | 9832        | Title-Description       |                                                                     |
| CMR-syntisaized           | 796097      | search_terms-document   |                                                                     |
| PDS-syntisaized           | 52777       | search_terms-document   |                                                                     |
| **Total** | **~162.4M** |                         |                                                                     |


## Evaluation

We evaluate the model on a variety of benchmark datasets, especially the following:
- [NASA SMD IR benchmark](https://huggingface.co/datasets/nasa-impact/nasa-smd-IR-benchmark)
- [NanoBEIR](https://huggingface.co/collections/zeta-alpha-ai/nanobeir-66e1a0af21dfd93e620cd9f6)
- [BEIR](https://github.com/beir-cellar/beir)

We observe that the model from this stage has overall better performance compared to [original INDUS Sentence Transformer](https://huggingface.co/nasa-impact/nasa-smd-ibm-st-v2) and ModernBERT-based ST.

The model uploaded to the Hf is `indus-sde-st-v0.2_vocal-river-16`
```python
models = {
    "modernbert-embed-base": "ModernBERT based embedding model",
    "nasa-smd-ibm-st-v2": "Original Indus Sentence Transformer",
    "indus-sde-st-v0.1": "Indus-SDE Stage 1 Sentence Transformer",
    "indus-sde-st-v0.2_whole-moon-14": "Indus-SDE Stage 2 Sentence Transformer (Trained on full dataset and faster learning rate)",
    "indus-sde-st-v0.2_atomic-plasma-15": "Indus-SDE Stage 2 Sentence Transformer (Trained just on the sde/ads dataset)",
    "indus-sde-st-v0.2_vocal-river-16": "Indus-SDE Stage 2 Sentence Transformer (Trained on top of model 14 with nasa sde/ads for 2 epoch)",
}
```

### NASA SDE IR Benchmark

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63f0e7de9cf89c9ed1bf92a2/QmnHtn8PJAUgZy0Ujq2-9.png)

### Nano BEIR

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63f0e7de9cf89c9ed1bf92a2/oXpbqQ6wd_Md7Vl9ocUh7.png)

### NASA SMD IR Benchmark

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63f0e7de9cf89c9ed1bf92a2/mBS-fUgXAqn0LqBKMg80S.png)