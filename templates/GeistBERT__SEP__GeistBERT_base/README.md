---
license: mit
language:
- de
base_model:
- TUM/GottBERT_filtered_base_best
---

# GeistBERT
GeistBERT is a **German language model** trained on a **for the most part deduplicated corpus** including **OSCAR23, OPUS, and MC4**. It builds on **GottBERT** while introducing **Whole Word Masking (WWM)** to improve contextual language representation. Achieving state-of-the-art among base models, the model also performs competitively with larger ones on several German NLP benchmarks.

## Training Data
GeistBERT was trained on a **diverse German corpus** combining:
- **OSCAR23, OPUS, and MC4** (for the most part deduplicated)
- **German Wikipedia**
- **OpenLegalData**
- **Europarl, EUbookshop, ECB, and EuroPat**
- **OpenSubtitles and TildeMODEL**

The dataset amounts to **approximately 1.3T tokens**, shuffled for improved variance.

## Training Procedure
### Hardware
- Training was conducted on **multiple GPUs**, including **NVIDIA RTX 3090 (24GB VRAM)**.

### Hyperparameters
| Parameter          | Value                  |
|--------------------|------------------------|
| **Model Architecture** | RoBERTa (Base)      |
| **Batch Size**     | 8,000                  |
| **Training Steps** | 100k                   |
| **Weight Initialization** | [GottBERT filtered base](https://huggingface.co/TUM/GottBERT_filtered_base_best) |
| **Warmup Iterations** | 10k                  |
| **Peak Learning Rate** | 0.0007              |
| **Learning Rate Decay** | Polynomial to zero |

## Performance
GeistBERT achieves **SOTA results** on multiple tasks:
- **NER**: CoNLL 2003, GermEval 2014
- **Text Classification**: GermEval 2018 (coarse & fine), 10kGNAD
- **NLI**: German subset of XNLI

Mertics:
- **NER and Text Classification**: F1 Score
- **NLI**: Accuracy


Details:
- **bold** values indicate the best performing model within one architecure (base, large), <ins>undescored</ins> values the second best.

| Model                               | Accuracy NLI | GermEval\_14 F1 | CoNLL F1 | Coarse F1 | Fine F1 | 10kGNAD F1 |
|-------------------------------------|--------------|----------------|----------|-----------|---------|------------|
| [GeistBERT](https://huggingface.co/GeistBERT/GeistBERT_base)                | **82.67**   | **88.47**   | **86.17**  | **79.67**  | **66.42**   | **90.89**  |
| [GottBERT_base_best](https://huggingface.co/TUM/GottBERT_base_best)                | 80.82       | 87.55          | 85.93  | 78.17     | 53.30   | 89.64      |
| [GottBERT_base_last](https://huggingface.co/TUM/GottBERT_base_last)                | 81.04       | 87.48          | 85.61    | 78.18   | 53.92 | 90.27  |
| [GottBERT_filtered_base_best](https://huggingface.co/TUM/GottBERT_filtered_base_best)         | 80.56       | 87.57 | 86.14 | 78.65 | 52.82   | 89.79      |
| [GottBERT_filtered_base_last](https://huggingface.co/TUM/GottBERT_filtered_base_last)         | 80.74       | 87.59      | 85.66    | 78.08     | 52.39   | 89.92      |
| GELECTRA_base                   | 81.70   | 86.91          | 85.37    | 77.26     | 50.07   | 89.02      |
| GBERT_base                        | 80.06       | 87.24          | 85.16    | 77.37     | 51.51   | 90.30  |
| dbmdzBERT                          | 68.12       | 86.82          | 85.15    | 77.46     | 52.07   | _90.34_  |
| GermanBERT                        | 78.16       | 86.53          | 83.87    | 74.81     | 47.78   | 90.18      |
| XLM-R_base                        | 79.76       | 86.14          | 84.46    | 77.13     | 50.54   | 89.81      |
| mBERT                              | 77.03       | 86.67          | 83.18    | 73.54     | 48.32   | 88.90      |
| [GottBERT_large](https://huggingface.co/TUM/GottBERT_large)                | 82.46       | 88.20          | _86.78_  | 79.40     | 54.61   | 90.24      |
| [GottBERT_filtered_large_best](https://huggingface.co/TUM/GottBERT_filtered_large_best)     | 83.31       | 88.13          | 86.30    | 79.32     | 54.70   | 90.31      |
| [GottBERT_filtered_large_last](https://huggingface.co/TUM/GottBERT_filtered_large_last)     | 82.79       | _88.27_ | 86.28    | 78.96     | 54.72   | 90.17      |
| GELECTRA_large                | **86.33**   | _88.72_ | _86.78_  | **81.28** | _56.17_ | **90.97**  |
| GBERT_large                      | _84.21_     | _88.72_        | **87.19** | _80.84_   | **57.37** | _90.74_   |
| XLM-R_large                      | 84.07       | **88.83**      | 86.54    | 79.05     | 55.06   | 90.17      |


## Intended Use
This model is designed for **German NLP tasks**, including:
- **Text classification**
- **Named Entity Recognition (NER)**
- **Machine Translation Pre-training**
- **Document Understanding**

## Limitations
- Trained on **unfiltered data**, meaning some **redundant or lower-quality samples** may be present.
- While deduplication was applied to **specific subcorpora**, the full corpus **was not manually curated**.

## Fairseq Checkpoint
Get the fairseq checkpoint [here](https://drive.proton.me/urls/P83GCPNM40#2f0f87XEIrQP).

# Citations

If you use GeistBERT in your research, please cite the following paper:

```
@book{scheible-schmitt-frei-2025-geistbert,
  author    = {\textbf{Scheible-Schmitt}, \textbf{Raphael}  and  Frei, Johann},
  title     = {GeistBERT: Breathing Life into German NLP},
  booktitle      = {Proceedings of the Workshop on Beyond English: Natural Language Processing for all Languages in an Era of Large Language Models},
  month          = {September},
  year           = {2025},
  address        = {Varna, Bulgaria},
  publisher      = {INCOMA Ltd., Shoumen, BULGARIA},
  pages     = {42--50},
  abstract  = {Advances in transformer-based language models have highlighted the benefits of language-specific pre-training on high-quality corpora. In this context, German NLP stands to gain from updated architectures and modern datasets tailored to the linguistic characteristics of the German language. GeistBERT seeks to improve German language processing by incrementally training on a diverse corpus and optimizing model performance across various NLP tasks. We pre-trained GeistBERT using fairseq, following the RoBERTa base configuration with Whole Word Masking (WWM), and initialized from GottBERT weights. The model was trained on a 1.3 TB German corpus with dynamic masking and a fixed sequence length of 512 tokens. For evaluation, we fine-tuned the model on standard downstream tasks, including NER (CoNLL 2003, GermEval 2014), text classification (GermEval 2018 coarse/fine, 10kGNAD), and NLI (German XNLI), using $F_1$ score and accuracy as evaluation metrics. GeistBERT achieved strong results across all tasks, leading among base models and setting a new state-of-the-art (SOTA) in GermEval 2018 fine text classification. It also outperformed several larger models, particularly in classification benchmarks. To support research in German NLP, we release GeistBERT under the MIT license.},
  url       = {https://aclanthology.org/2025.globalnlp-1.6},
  doi       = {https://doi.org/10.26615/978-954-452-105-9-006}
}
```