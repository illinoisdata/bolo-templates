---
tags:
- text
- vision
- video
datasets:
- HuggingFaceM4/webvid
pipeline_tag: text-to-video
---


# Model Card for CLIP4Clip/WebVid-150k
## Model Details

A CLIP4Clip video-text retrieval model trained on a subset of the WebVid dataset. 
The model and training method are described in the paper ["Clip4Clip: An Empirical Study of CLIP for End to End Video Clip Retrieval"](https://arxiv.org/pdf/2104.08860.pdf) by Lou et el, and implemented in the accompanying [GitHub repository](https://github.com/ArrowLuo/CLIP4Clip).

The training process utilized the [WebVid Dataset](https://m-bain.github.io/webvid-dataset/), a comprehensive collection of short videos with corresponding textual descriptions sourced from the web. 
For training purposes, a subset consisting of the first 150,000 video-text pairs from the dataset were used.

This HF model is based on the [clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32) architecture, with weights trained by Daphna Idelson at [Searchium](https://www.searchium.ai).


# How to use
### Extracting Text Embeddings:

```python
import numpy as np
import torch
from transformers import CLIPTokenizer, CLIPTextModelWithProjection


search_sentence = "a basketball player performing a slam dunk"

model = CLIPTextModelWithProjection.from_pretrained("Searchium-ai/clip4clip-webvid150k")
tokenizer = CLIPTokenizer.from_pretrained("Searchium-ai/clip4clip-webvid150k")

inputs = tokenizer(text=search_sentence , return_tensors="pt")
outputs = model(input_ids=inputs["input_ids"], attention_mask=inputs["attention_mask"])

# Normalize embeddings for retrieval:
final_output = outputs[0] / outputs[0].norm(dim=-1, keepdim=True)
final_output = final_output.cpu().detach().numpy()
print("final output: ", final_output)
```

### Extracting Video Embeddings:

An additional notebook ["GSI_VideoRetrieval_VideoEmbedding.ipynb"](https://huggingface.co/Searchium-ai/clip4clip-webvid150k/blob/main/Notebooks/GSI_VideoRetrieval_VideoEmbedding.ipynb), provides instructions for extracting video embeddings and includes the necessary tools for preprocessing videos.


## Model Intended Use

This model is intended for use in large scale video-text retrieval applications. 

To illustrate its functionality, refer to the accompanying [**Video Search Space**](https://huggingface.co/spaces/Searchium-ai/Video-Search) which provides a search demonstration on a vast collection of approximately 1.5 million videos. 
This interactive demo showcases the model's capability to effectively retrieve videos based on text queries, highlighting its potential for handling substantial video datasets.

## Motivation

As per the original authors, the main motivation behind this work is to leverage the power of the CLIP image-language pre-training model and apply it to learning 
visual-temporal concepts from videos, thereby improving video-based searches. 

By using the WebVid dataset, the model's capabilities were enhanced even beyond those described in the paper, thanks to the large-scale and diverse nature of the dataset empowering the model's performance.


## Evaluations

To evaluate the model's performance we used the last last 10,000 video clips and their accompanying text from the Webvid dataset.
We evaluate R1, R5, R10, MedianR, and MeanR on:
1. Zero-shot pretrained clip-vit-base-patch32 model
2. CLIP4Clip based weights trained on the dataset [MSR-VTT](https://paperswithcode.com/dataset/msr-vtt), consisting of 10,000 video-text pairs
3. CLIP4Clip based weights trained on a 150K subset of the dataset Webvid-2M
4. CLIP4Clip based weights trained on a 150K subset of the dataset Webvid-2M - binarized and further finetuned on 100 top searches -
   for search acceleration and efficiency [<a href="#footnote1">1</a></sup>].

| Model | R1 &uarr; | R5 &uarr; | R10 &uarr; | MedianR &darr; | MeanR &darr;
|------------------------|-------|-------|-------|-----|---------|
| Zero-shot clip weights | 37.16 | 62.10 | 71.16 | 3.0 | 42.2128
| CLIP4Clip weights trained on msr-vtt | 38.38 | 62.89 | 72.01 | 3.0 |39.3023 
| **CLIP4Clip trained on 150k Webvid** | 50.74 | 77.30 | 85.05 | 1.0 | 14.9535
| Binarized CLIP4Clip trained on 150k Webvid with rerank100 | 50.56 | 76.39 | 83.51 | 1.0 | 43.2964

For an elaborate description of the evaluation refer to the notebook 
[GSI_VideoRetrieval-Evaluation](https://huggingface.co/Searchium-ai/clip4clip-webvid150k/blob/main/Notebooks/GSI_VideoRetrieval-Evaluation.ipynb).

<div id="footnote1">
  
[1] For overall search acceleration capabilities, in order to boost your search application, please refer to [Searchium.ai](https://www.searchium.ai)

</div>



## Acknowledgements
Acknowledging Diana Mazenko of [Searchium](https://www.searchium.ai) for adapting and loading the model to Hugging Face, and for creating a Hugging Face [**SPACE**](https://huggingface.co/spaces/Searchium-ai/Video-Search) for a large-scale video-search demo.

Acknowledgments also to Lou et el for their comprehensive work on CLIP4Clip and openly available code.

## Citations

CLIP4Clip paper
```
@Article{Luo2021CLIP4Clip,
  author  = {Huaishao Luo and Lei Ji and Ming Zhong and Yang Chen and Wen Lei and Nan Duan and Tianrui Li},
  title   = {{CLIP4Clip}: An Empirical Study of CLIP for End to End Video Clip Retrieval},
  journal = {arXiv preprint arXiv:2104.08860},
  year    = {2021},
}
```

OpenAI CLIP paper
```
@inproceedings{Radford2021LearningTV,
  title={Learning Transferable Visual Models From Natural Language Supervision},
  author={Alec Radford and Jong Wook Kim and Chris Hallacy and A. Ramesh and Gabriel Goh and Sandhini Agarwal and Girish Sastry and Amanda Askell and Pamela Mishkin and Jack Clark and Gretchen Krueger and Ilya Sutskever},
  booktitle={ICML},
  year={2021}
}
```