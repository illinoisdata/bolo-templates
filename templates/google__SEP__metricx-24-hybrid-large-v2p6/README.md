---
license: apache-2.0
---
# MetricX-24 (Large)

*This is not an officially supported Google product.*

> ℹ️ For the bfloat16 variant of this model, see [MetricX-24 (Large, bfloat16)](https://huggingface.co/google/metricx-24-hybrid-large-v2p6-bfloat16).

**GitHub repository**: https://github.com/google-research/metricx

The repository contains the code for running inference on MetricX-24 models,
a family of models for automatic evaluation of translations that were proposed
in the WMT'24 Metrics Shared Task submission
[MetricX-24: The Google Submission to the WMT 2024 Metrics Shared Task](https://aclanthology.org/2024.wmt-1.35/).
The models were trained in [T5X](https://github.com/google-research/t5x) and
then converted for use in PyTorch.


## Available Models

There are 3 MetricX-24 models available on Hugging Face that vary in the number
of parameters. Unlike the MetricX-23 models, the MetricX-24 models are all
hybrid models that can do both reference-based and reference-free (also known as
quality estimation, or QE) inference:

* [MetricX-24-Hybrid-XXL](https://huggingface.co/google/metricx-24-hybrid-xxl-v2p6)
* [MetricX-24-Hybrid-XL](https://huggingface.co/google/metricx-24-hybrid-xl-v2p6)
* [MetricX-24-Hybrid-Large](https://huggingface.co/google/metricx-24-hybrid-large-v2p6)

We recommend using the XXL model versions for the best agreement with human
judgments of translation quality, the Large versions for best speed, and the
XL for an intermediate use case.


## Changes to the WMT'24 Submission

The MetricX-24 models available here are most similar to the primary submission
to the WMT'24 Metrics Shared Task. They are initialized with
[mT5](https://aclanthology.org/2021.naacl-main.41/),
then fine-tuned on a combination of direct assessment and MQM data from
WMT'15-'22. However, we made a couple of small changes that make these models
different from the WMT'24 submissions.

First, the metric scores get automatically clipped at 0 and 25, to ensure they
are strictly in the [0, 25] range, as due to the nature of regression models,
the scores could otherwise sometimes fall outside the range.

Second, we included one additional type of synthetic training examples that
weren't ready in time for the official submission. These are examples of perfect
translations of multi-sentence segments, generated from the MQM data from
WMT'20-'22. The purpose of this category of synthetic data is to reduce the
model's bias against longer translations when the source segment and/or
reference are also long.


## Model Performance

For comparison with the submissions to
[WMT'24 Metrics Shared Task](https://www2.statmt.org/wmt24/pdf/2024.wmt-1.2.pdf),
we provide an overview of the system- and segment-level correlation scores
between the MetricX-24 scores and MQM ratings of translation quality, as
calculated on the shared task's test sets:

| Model | Sys-Level SPA (en-de) | Seg-Level Acc (en-de) | Sys-Level SPA (en-es) | Seg-Level Acc (en-es) | Sys-Level SPA (ja-zh) | Seg-Level Acc (ja-zh) |
| -------------------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| MetricX-24-Hybrid-XXL      | 0.865 | 0.543 | 0.785 | 0.685 | 0.878 | 0.541 |
| MetricX-24-Hybrid-XL       | 0.884 | 0.522 | 0.806 | 0.683 | 0.859 | 0.528 |
| MetricX-24-Hybrid-Large    | 0.879 | 0.511 | 0.795 | 0.686 | 0.845 | 0.514 |
| MetricX-24-Hybrid-QE-XXL   | 0.884 | 0.525 | 0.789 | 0.685 | 0.863 | 0.527 |
| MetricX-24-Hybrid-QE-XL    | 0.879 | 0.502 | 0.774 | 0.683 | 0.849 | 0.509 |
| MetricX-24-Hybrid-QE-Large | 0.809 | 0.490 | 0.762 | 0.684 | 0.847 | 0.508 |

Below are the above correlation scores averaged, as used in the shared task to
determine the final ranking of the submissions:

| Model | Average Correlation |
| -------------------------- | ----- |
| MetricX-24-Hybrid-XXL      | 0.716 |
| MetricX-24-Hybrid-XL       | 0.714 |
| MetricX-24-Hybrid-Large    | 0.705 |
| MetricX-24-Hybrid-QE-XXL   | 0.712 |
| MetricX-24-Hybrid-QE-XL    | 0.699 |
| MetricX-24-Hybrid-QE-Large | 0.683 |

NOTE: Since MetricX-24 models are hybrid models, MetricX-24-\<size\> and
MetricX-24-QE-\<size\> correspond to the same model, evaluated *with* and
*without* the references, respectively.


## Citation

If you use MetricX-24 in your research, please cite the following publication:

```bibtex
@inproceedings{juraska-etal-2024-metricx,
    title = "{M}etric{X}-24: The {G}oogle Submission to the {WMT} 2024 Metrics Shared Task",
    author = "Juraska, Juraj  and
      Deutsch, Daniel  and
      Finkelstein, Mara  and
      Freitag, Markus",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Ninth Conference on Machine Translation",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.wmt-1.35",
    pages = "492--504",
}
```