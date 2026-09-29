---
language:
- en
- ar
- zh
- nl
- fr
- ru
- es
- tr
tags:
- multilingual-sentiment-analysis
- sentiment-analysis
- aspect-based-sentiment-analysis
- deberta
- pyabsa
- efficient
- lightweight
- production-ready
- no-llm
license: mit
pipeline_tag: text-classification
widget:
- text: >-
    The user interface is brilliant, but the documentation is a total mess.
    [SEP] user interface [SEP]
- text: >-
    The user interface is brilliant, but the documentation is a total mess.
    [SEP] documentation [SEP]
---

# State-of-the-Art Multilingual Sentiment Analysis 

## Multilingual -> English, Chinese, Arabic, Dutch, French, Russian, Spanish, Turkish, etc.

Tired of the high costs, slow latency, and massive computational footprint of Large Language Models? This is the sentiment analysis model you've been waiting for.

**`deberta-v3-base-absa-v1.1`** delivers **state-of-the-art accuracy** for fine-grained sentiment analysis with the speed, efficiency, and simplicity of a classic encoder model. It represents a paradigm shift in production-ready AI: maximum performance with minimum operational burden.

### Why This Model?
- **🎯 Wide Usage:** This model reaches **one million downloads** already! (Maybe) the most downloaded open-source ABSA model ever.
- **🏆 SOTA Performance:** Built on the powerful `DeBERTa-v3` architecture and fine-tuned with advanced, context-aware methods from [PyABSA](https://github.com/yangheng95/PyABSA), this model achieves top-tier accuracy on complex sentiment tasks.
- **⚡ LLM-Free Efficiency:** No need for A100s or massive GPU clusters. This model runs inference at a fraction of the computational cost, enabling real-time performance on standard CPUs or modest GPUs.
- **💰 Lower Costs:** Slash your hosting and API call expenses. The small footprint and high efficiency translate directly to significant savings, whether you're a startup or an enterprise.
- **🚀 Production-Ready:** Lightweight, fast, and reliable. This model is built to be deployed at scale for applications that demand immediate and accurate sentiment feedback.

### Ideal Use Cases

This model excels where speed, cost, and precision are critical:

- **Real-time Social Media Monitoring:** Analyze brand sentiment towards specific product features as it happens.
- **Intelligent Customer Support:** Automatically route tickets based on the sentiment towards different aspects of a complaint.
- **Product Review Analysis:** Aggregate fine-grained feedback on thousands of reviews to identify precise strengths and weaknesses.
- **Market Intelligence:** Understand nuanced public opinion on key industry topics.

## How to Use

Getting started is incredibly simple. You can use the Hugging Face `pipeline` for a zero-effort implementation.


from transformers import pipeline

### Load the classifier pipeline - it's that easy.
```python
classifier = pipeline("text-classification", model="yangheng/deberta-v3-base-absa-v1.1")
sentence = "The food was exceptional, although the service was a bit slow."
```
### Analyze sentiment for the 'food' aspect
```python
result_food = classifier(sentence, text_pair="food")
result_food ->
{
  'Negative': 0.989
  'Neutral': 0.008
  'Positive': 0.003
}
```
### Analyze sentiment for the Chinese texts.
```python
result_service = classifier("这部手机的性能差劲", text_pair="性能")
result_service = classifier("这台汽车的引擎推力强劲", text_pair="引擎")
```

## Using PyABSA or [Transformers](end2end_absa.py) for End-to-End Analysis
For a more powerful, end-to-end solution that handles both aspect term extraction and sentiment classification in a single call, you can use the PyABSA library. This is the very framework used to train and optimize this model.

First, install PyABSA:

```bash
pip install pyabsa
```
Then, you can perform inference like this. The model will automatically find the aspects in the text and classify their sentiment.

```python3
from pyabsa import AspectTermExtraction as ATEPC, available_checkpoints

# Load the model directly from Hugging Face Hub
aspect_extractor = ATEPC.AspectExtractor(
    'multilingual',          # Can be replaced with a specific checkpoint name or a local file path
    auto_device=True,        # Use GPU/CPU or Auto
    cal_perplexity=True      # Calculate text perplexity
)
texts = [
    "这家餐厅的牛排很好吃，但是服务很慢。",
    "The battery life is terrible but the camera is excellent."
]
# Perform end-to-end aspect-based sentiment analysis
result = aspect_extractor.predict(
    texts,
    print_result=True,       # Console Printing
    save_result=False,       # Save results into a json file
    ignore_error=True,       # Exception handling for error cases
    pred_sentiment=True      # Predict sentiment for extracted aspects
)

# The output automatically identifies aspects and their corresponding sentiments:
# {
#   "text": "The user interface is brilliant, but the documentation is a total mess.",
#   "aspect": ["user interface", "documentation"],
#   "position": [[4, 19], [41, 54]],
#   "sentiment": ["Positive", "Negative"],
#   "probability": [[1e-05, 0.0001, 0.9998], [0.9998, 0.0001, 1e-05]],
#   "confidence": [0.9997, 0.9997]
# }
```
Find more solutions for ABSA tasks in PyASBA.

## The Technology Behind the Performance

### Base Model

It starts with `microsoft/deberta-v3-base`, a highly optimized encoder known for its disentangled attention mechanism, which improves efficiency and performance over original BERT/RoBERTa models.

### Fine-Tuning Architecture

It employs the FAST-LCF-BERT backbone trained from the PyABSA framework. This introduces a Local Context Focus (LCF) layer that dynamically guides the model to concentrate on the words and phrases most relevant to the given aspect, dramatically improving contextual understanding and accuracy.

### Training Data

This model was trained on a robust, aggregated corpus of over 30,000 unique samples (augmented to ~180,000 examples) from canonical ABSA datasets, including SemEval-2014, SemEval-2016, MAMS, and more. The standard test sets were excluded to ensure fair and reliable benchmarking.

## Citation

If you use this model in your research or application, please cite the foundational work on the PyABSA framework.

### BibTeX Citation

```bibtex
@inproceedings{YangCL23PyABSA,
  author       = {Heng Yang and Chen Zhang and Ke Li},
  title        = {PyABSA: {A} Modularized Framework for Reproducible Aspect-based Sentiment Analysis},
  booktitle    = {Proceedings of the 32nd {ACM} International Conference on Information and Knowledge Management, {CIKM} 2023},
  pages        = {5117--5122},
  publisher    = {{ACM}},
  year         = {2023},
  doi          = {10.1145/3583780.3614752}
}

@inproceedings{YangL24LCF/LCA,
  author       = {Heng Yang and
                  Ke Li},
  editor       = {Yvette Graham and
                  Matthew Purver},
  title        = {Modeling Aspect Sentiment Coherency via Local Sentiment Aggregation},
  booktitle    = {Findings of the Association for Computational Linguistics: {EACL}
                  2024, St. Julian's, Malta, March 17-22, 2024},
  pages        = {182--195},
  publisher    = {Association for Computational Linguistics},
  year         = {2024},
  url          = {https://aclanthology.org/2024.findings-eacl.13},
  timestamp    = {Tue, 23 Jul 2024 08:21:59 +0200},
  biburl       = {https://dblp.org/rec/conf/eacl/YangL24.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```