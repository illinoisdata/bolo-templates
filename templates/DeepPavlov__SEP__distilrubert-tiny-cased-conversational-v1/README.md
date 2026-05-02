---
language:
- ru
---
# distilrubert-tiny-cased-conversational
Conversational DistilRuBERT-tiny \(Russian, cased, 3‑layers, 264‑hidden, 12‑heads, 10.4M parameters\) was trained on OpenSubtitles\[1\], [Dirty](https://d3.ru/), [Pikabu](https://pikabu.ru/), and a Social Media segment of Taiga corpus\[2\] (as [Conversational RuBERT](https://huggingface.co/DeepPavlov/rubert-base-cased-conversational)). It can be considered as tiny copy of [Conversational DistilRuBERT-small](https://huggingface.co/DeepPavlov/distilrubert-tiny-cased-conversational).

Our DistilRuBERT-tiny is highly inspired by \[3\], \[4\] and architecture is very close to \[5\]. Namely, we use 
* MLM loss (between token labels and student output distribution)
* MSE loss (between averaged student and teacher hidden states)

The key features are:
* unlike most of distilled language models, we **didn't** use KL loss during pre-training
* reduced vocabulary size (30K in *tiny* vs. 100K in *base* and *small* )
* two separate inputs for student: tokens obtained using student tokenizer (for MLM) and teacher tokens greedily splitted by student tokens (for MSE)

Here is comparison between teacher model (`Conversational RuBERT`) and other distilled models.

| Model name  | \# params, M  | \# vocab, K  | Mem., MB |
|---|---|---|---|
| `rubert-base-cased-conversational` | 177.9 | 120 | 679 |
| `distilrubert-base-cased-conversational` | 135.5 | 120 | 517 |
| `distilrubert-small-cased-conversational` | 107.1 | 120 | 409 |
| `cointegrated/rubert-tiny` | 11.8 | **30** | 46 |
| **distilrubert-tiny-cased-conversational** | **10.4** | 31 |  **41** |


DistilRuBERT-tiny was trained for about 100 hrs. on 7 nVIDIA Tesla P100-SXM2.0 16Gb.

We used `PyTorchBenchmark` from `transformers` to evaluate model's performance and compare it with other pre-trained language models for Russian. All tests were performed on Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz and nVIDIA Tesla P100-SXM2.0 16Gb.

| Model name  | Batch size  |  Seq len | Time, s  ||   Mem, MB  ||
|---|---|---|------||------||
|   |   |   |  CPU |  GPU |  CPU |  GPU |
| `rubert-base-cased-conversational` | 1  | 512 |  0.147 |  0.014 | 897  | 1531  |
| `distilrubert-base-cased-conversational` | 1  | 512  | 0.083  |  0.006 | 766  |  1423 |
| `distilrubert-small-cased-conversational` | 1 |  512 | 0.03  | **0.002**  |  600 |  1243 |
| `cointegrated/rubert-tiny` | 1  |  512 |  0.041 | 0.003  |  272 |  919 |
| **distilrubert-tiny-cased-conversational** | 1  | 512  | **0.023**  |  0.003 | **206**  | **855** | 
| `rubert-base-cased-conversational` | 16  | 512  | 2.839  | 0.182  | 1499  |  2071 |
| `distilrubert-base-cased-conversational` |  16 |  512 | 1.065  | 0.055  |  2541 |  2927 |
| `distilrubert-small-cased-conversational` |  16 |  512 | 0.373  |  **0.003** | 1360  |  1943 |
| `cointegrated/rubert-tiny` |  16 |  512 |  0.628 | 0.004  |  1293 |  2221 |
| **distilrubert-tiny-cased-conversational** | 16 | 512  |  **0.219** | **0.003**  | **633**  | **1291** |


To evaluate model quality, we fine-tuned DistilRuBERT-tiny on classification (RuSentiment, ParaPhraser), NER and question answering data sets for Russian and obtained scores very similar to the [Conversational DistilRuBERT-small](https://huggingface.co/DeepPavlov/distilrubert-tiny-cased-conversational). 

# Citation
If you found the model useful for your research, we are kindly ask to cite [this](https://arxiv.org/abs/2205.02340) paper:
```
@misc{https://doi.org/10.48550/arxiv.2205.02340,
  doi = {10.48550/ARXIV.2205.02340},
  
  url = {https://arxiv.org/abs/2205.02340},
  
  author = {Kolesnikova, Alina and Kuratov, Yuri and Konovalov, Vasily and Burtsev, Mikhail},
  
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {Knowledge Distillation of Russian Language Models with Reduction of Vocabulary},
  
  publisher = {arXiv},
  
  year = {2022},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

\[1\]: P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles. In Proceedings of the 10th International Conference on Language Resources and Evaluation \(LREC 2016\)

\[2\]: Shavrina T., Shapovalova O. \(2017\) TO THE METHODOLOGY OF CORPUS CONSTRUCTION FOR MACHINE LEARNING: «TAIGA» SYNTAX TREE CORPUS AND PARSER. in proc. of “CORPORA2017”, international conference , Saint-Petersbourg, 2017.

\[3\]: Sanh, V., Debut, L., Chaumond, J., & Wolf, T. \(2019\). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. arXiv preprint arXiv:1910.01108.

\[4\]: <https://github.com/huggingface/transformers/tree/master/examples/research_projects/distillation>

\[5\]: <https://habr.com/ru/post/562064/>, <https://huggingface.co/cointegrated/rubert-tiny>