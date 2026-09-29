---
license: apache-2.0
library_name: videoprism
tags:
- video-classification
- video-embedding
---

# VideoPrism Model Card

**Paper**: https://huggingface.co/papers/2402.13217

**arXiv**: https://arxiv.org/pdf/2402.13217

**GitHub**: https://github.com/google-deepmind/videoprism

**Blog**: https://research.google/blog/videoprism-a-foundational-visual-encoder-for-video-understanding/

VideoPrism is a foundational video encoder that enables state-of-the-art performance on a large variety of video understanding tasks. It takes video frames as input and outputs compact embeddings of the frames, which one can conveniently feed into classifiers, LLMs, retrieval models, etc. When tested on 33 public video understanding benchmarks over four task categories, a single frozen VideoPrism checkpoint outperforms previous best-performing foundation models on 31 of them, with no fine-tuning on target task datasets.

## Model details

We release the following model variants:

| Model Name | Configuration Name | Model Type | Backbone | #Params | File Size | Checkpoint |
| -------- | -------- | ------- | :-------: | :-------: | :-------: | :-------: |
| VideoPrism-B | `videoprism_public_v1_base`  | Video encoder | ViT-B | 114M | 458MB | [link](https://huggingface.co/google/videoprism-base-f16r288) |
| VideoPrism-L | `videoprism_public_v1_large` | Video encoder | ViT-L | 354M | 1.42GB | [link](https://huggingface.co/google/videoprism-large-f8r288) |
| VideoPrism-LvT-B | `videoprism_lvt_public_v1_base`  | Video-text encoders | ViT-B | 248M | 991MB | [link](https://huggingface.co/google/videoprism-lvt-base-f16r288) |
| VideoPrism-LvT-L | `videoprism_lvt_public_v1_large` | Video-text encoders | ViT-L | 580M | 2.30GB | [link](https://huggingface.co/google/videoprism-lvt-large-f8r288) |


### Model description

VideoPrism-B/L are the composition of a Vision Transformer image encoder and four temporal-attention Transformer layers. The image encoder and text encoder are initialized from [CoCa](https://arxiv.org/abs/2205.01917), which is trained on WebLI following the CoCa recipes. VideoPrism is based on the [ViViT](https://arxiv.org/abs/2103.15691) factorized video encoder architecture.

### Inputs and outputs
The models take videos with shape (num_frames, 288, 288, 3) as inputs and outputs embeddings with shape (num_frames * 16 * 16, feature_channels) which could be reshaped into (num_frames, 16, 16, feature_channels) for spatiotemporal representations. During model training, num_frames is set to 16 and 8 for VideoPrism-B and VideoPrism-L, respectively. Both models are expected to work with arbitrary num_frames by interpolating the temporal positional embeddings.

In video-text models, both video and text encoders produce global embeddings with shape `(feature_channels)`, whose similarities could be measured by cosine distances. We use the `c4_en` [SentencePiece](https://github.com/google/sentencepiece) model for text tokenization. During inference, embedding calculation for either modality can be skipped by providing `None` as the input.

## Uses
VideoPrism has a wide range of applications across various video understanding scenarios. The following lists some primary use cases and yet is not comprehensive. The purpose of this list is to provide contextual information the model creators considered as part of model training and development.
*    **Video classification**: By feeding the video embeddings to a lightweight classifier, we can tackle video action recognition, a fundamental task in video understanding, under various scenarios.
*    **Temporal and spatiotemporal localization**: We can also use the model to localize actions of interest spatially across time by equipping it with a bounding box proposal.
*    **Video retrieval and open-set classification**: By pairing up the video embeddings with a text encoder in the CLIP fashion, we can do text-video retrieval and open-set video classification.


## Ethical considerations and risks
The model inherits the safety benefits and safety risks associated with the image encoder CoCa and the training datasets described above. We recommend that the model should not be used for downstream applications without prior assessment and mitigation of downstream application-specific security and fairness concerns.
*    Data bias: Large datasets scraped from the internet can contain inherent biases, leading to skewed model performance and potentially discriminatory outputs. The presence of "noisy parallel text" like ASR transcripts introduces potential inaccuracies and biases from the speech-to-text process.
*    Content moderation: The sheer volume of data (36M video-caption pairs and 582M video clips) raises concerns about the presence of objectionable or inappropriate content within the training data, which could lead to harmful model outputs.
*    Ethical use: As with any powerful video understanding model, there are risks of misuse, such as in surveillance or the propagation of misinformation.
*    Limitations: The reliance on potentially noisy text data can limit the models understanding of the true video content. Further research is needed to refine the models ability to understand long form videos, geometric information in videos, and non-semantic cues.


## How to get started with the model
To get started with our models, please see the code and examples in our [GitHub Repository](https://github.com/google-deepmind/videoprism). 

### Feedback and Questions

We welcome all questions and feedback! If you find a bug, have a feature request, or want to ask a question, please don't hesitate to **open an issue** on our GitHub repository.

We're excited to see what you build with VideoPrism! 🚀


## Training details

### Training data

VideoPrism is pre-trained on a wide range of videos (36M video-caption pairs and 582M video clips), including the datasets below. Note that the number of clips are subject to change due to wipeout according to policy.

| Pretraining datasets | Public | Domain | Caption source | Caption quality | # of videos | # of clips |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Anonymous-Corpus #1 | ❌ | Web video | Manual labelled | High | 36.1M | 36.1M |
| [WTS-70M](https://arxiv.org/pdf/2007.14937) | ✅ | YouTube video | Metadata | Low | 55.1M | 55.1M |
| [YT-Temporal-180M](https://arxiv.org/pdf/2106.02636) | ✅ | YouTube video | ASR | Low | 2.3M | 87.8M |
| [VideoCC](https://arxiv.org/pdf/2204.00679) | ❌ | YouTube video | Image captions for mining | Low | 133.5M | 191.1M |
| [InternVid](https://arxiv.org/pdf/2307.06942) | ✅ | YouTube video | Generated by VLM/LLM | Medium | 2.8M | 7.0M |
| Anonymous-Corpus #2 | ❌ | YouTube video | ASR | Low | 44.6M | 170.3M |
| Anonymous-Corpus #3 | ❌ | YouTube video | Generated by VLM/LLM | Medium | 36.7M | 71.5M |

## Evaluation

In the tables below, "Public" denotes models we released in this repository. "Paper" and "Prior SOTA" denote our models and previous best-performing models reported in the paper, respectively. Our public models perform slightly worse than the paper models due to different pre-training image-text data we used subject to data policy.


### Results on video-focused tasks with frozen backbones

| Dataset | K400 | MiT | SSv2 | D48 | Charades | ActivityNet | AVA | AVA-K |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **VideoPrism-B (public)** | 82.9 | 39.7 | 62.2 | 64.3 | 43.5 | 36.5 | 28.3 | 30.8 |
| **VideoPrism-L (public)** | 85.0 | 43.3 | 64.6 | 67.6 | 53.2 | 37.0 | 32.4 | 34.5 |
| VideoPrism-B (paper) | 84.2 | 40.8 | 63.6 | 67.4 | 40.4 | 36.6 | 30.6 | 31.8 |
| VideoPrism-g (paper) | 87.2 | 45.5 | 68.5 | 71.3 | 62.3 | 37.8 | 36.2 | 37.3 |
| Prior SOTA (B) | 77.1 | 34.0 | 58.2 | 55.6 | 33.3 | 35.8 | 21.1 | 25.9 |
| Prior SOTA (L+) | 82.8 | 40.3 | 67.4 | 69.6 | 39.9 | 36.7 | 24.4 | 26.2 |

### Zero-shot video-text retrieval

| Models | MSRVTT-1K (v2t)  | MSRVTT-1K (t2v) | VATEX (v2t) | VATEX (t2v) | ActivityNet (v2t) | ActivityNet (t2v) |
| -------- | :-------: | :-------: | :-------: | :-------: | :-------: | :-------: |
| **VideoPrism-LvT-B (public)** | 49.8 | 50.1 | 73.1 | 56.2 | 47.9 | 48.8 |
| **VideoPrism-LvT-L (public)** | 50.6 | 50.1 | 75.0 | 57.2 | 49.1 | 51.3 |
| VideoPrism-LvT-B (paper) | 50.2 | 51.4 | 76.2 | 57.7 | 47.9 | 49.6 |
| VideoPrism-LvT-g (paper) | 51.7 | 52.7 | 77.1 | 62.5 | 50.3 | 52.7 |
| Prior SOTA (B) | - | 34.0 | - | - | - | 30.6 |
| Prior SOTA (L+) | 45.4 | 43.9 | 73.6 | 53.2 | 40.7 | 42.8 |

### Zero-shot video classification

| Models | K400 | SSv2 (Temporal) | SSv2 (Events) | NExT-QA (Hard) | Charades | Charades (STA) |
| -------- | :-------: | :-------: | :-------: | :-------: | :-------: | :-------: |
| **VideoPrism-LvT-B (public)** | 69.2 | 14.6 | 11.3 | 31.1 | 26.9 | 48.6 |
| **VideoPrism-LvT-L (public)** | 72.4 | 18.0 | 12.4 | 32.1 | 32.4 | 50.2 |
| VideoPrism-LvT-B (paper) | 71.3 | 16.1 | 11.9 | 31.3 | 29.2 | 50.0 |
| VideoPrism-LvT-g (paper) | 74.6 | 18.6 | 15.7 | 32.7 | 32.4 | 50.4 |
| Prior SOTA (B) | - | 9.8 | 6.4 | 27.6 | 21.1 | - |
| Prior SOTA (L+) | 72.0 | 15.2 | 11.4 | 25.2 | 25.8 | 47.2 |


## Implementation information

### Model architecture

Vision model is a [ViViT](https://arxiv.org/abs/2103.15691) factorized video encoder architecture, initialized from the Vision Transformer image encoder ([CoCa](https://arxiv.org/abs/2205.01917)) followed by four temporal-attention Transformer layers.

### Hardware

VideoPrism was trained using [Tensor Processing Unit
(TPU)](https://cloud.google.com/tpu/docs/intro-to-tpu) hardware.

#### Software

JAX, Flax

## Citation

VideoPrism:
```
@inproceedings{zhao2024videoprism,
  title = {{VideoPrism}: A Foundational Visual Encoder for Video Understanding},
  author = {Long Zhao and Nitesh B. Gundavarapu and Liangzhe Yuan and Hao Zhou and Shen Yan and Jennifer J. Sun and Luke Friedman and Rui Qian and Tobias Weyand and Yue Zhao and Rachel Hornung and Florian Schroff and Ming-Hsuan Yang and David A. Ross and Huisheng Wang and Hartwig Adam and Mikhail Sirotenko and Ting Liu and Boqing Gong},
  booktitle = {International Conference on Machine Learning (ICML)},
  year = {2024}
}
```

VideoGLUE benchmarks:
```
@article{yuan2024videoglue,
  title = {{VideoGLUE}: Video General Understanding Evaluation of Foundation Models},
  author = {Liangzhe Yuan and Nitesh Bharadwaj Gundavarapu and Long Zhao and Hao Zhou and Yin Cui and Lu Jiang and Xuan Yang and Menglin Jia and Tobias Weyand and Luke Friedman and Mikhail Sirotenko and Huisheng Wang and Florian Schroff and Hartwig Adam and Ming-Hsuan Yang and Ting Liu and Boqing Gong},
  journal = {Transactions on Machine Learning Research (TMLR)},
  year = {2024}
}
```