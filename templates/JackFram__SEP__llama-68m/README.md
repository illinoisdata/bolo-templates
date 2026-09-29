---
license: apache-2.0
language:
- en
datasets:
- wikipedia
pipeline_tag: text-generation
---
## Model description
This is a LLaMA-like model with only 68M parameters trained on Wikipedia and part of the C4-en and C4-realnewslike datasets. 

No evaluation has been conducted yet, so use it with care.

The model is mainly developed as a base Small Speculative Model in the [SpecInfer](https://arxiv.org/abs/2305.09781) paper.

## Evaluations (contributed by [Akshit](https://huggingface.co/GODELEV), huge thanks!)
| Category | Benchmark | Metric | Score / Value | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Linguistics & Grammar** | BLiMP | Accuracy | **70.57%** | Success |
| **Commonsense & Reasoning** | PIQA | Normalized Accuracy | **59.25%** | Success |
| | BoolQ | Accuracy | **57.71%** | Success |
| | COPA | Accuracy | **53.00%** | Success |
| | WinoGrande | Accuracy | **50.59%** | Success |
| | HellaSwag | Normalized Accuracy | **29.04%** | Success |
| | RACE | Accuracy | **25.36%** | Success |
| | CommonsenseQA | Accuracy | **19.82%** | Success |
| **Academic & Knowledge** | SciQ | Normalized Accuracy | **57.80%** | Success |
| | ARC-Easy | Normalized Accuracy | **35.98%** | Success |
| | OpenBookQA | Normalized Accuracy | **25.60%** | Success |
| | MMLU | Accuracy | **22.96%** | Success |
| | ARC-Challenge | Normalized Accuracy | **22.87%** | Success |
| **Language Modeling** | TriviaQA | Accuracy | *TriviaQA Standard* | Success |
| | LAMBADA | Accuracy | **13.24%** | Success |
| | C4-Perplexity | Word Perplexity | **205.79** | Success |
| | WikiText-2 | Word Perplexity | **306.79** | Success |

> **Notes on Failed Tasks:** The `Arithmetic` and `SocialIQA` benchmarks failed during execution due to runtime pipeline incompatibilities, yielding no score. Total evaluation runtime was **44.74 minutes**.


## Citation
To cite the model, please use
```bibtex
@misc{miao2023specinfer,
      title={SpecInfer: Accelerating Generative LLM Serving with Speculative Inference and Token Tree Verification}, 
      author={Xupeng Miao and Gabriele Oliaro and Zhihao Zhang and Xinhao Cheng and Zeyu Wang and Rae Ying Yee Wong and Zhuoming Chen and Daiyaan Arfeen and Reyna Abhyankar and Zhihao Jia},
      year={2023},
      eprint={2305.09781},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```