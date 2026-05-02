---
library_name: transformers
tags:
- colpali
license: gemma
datasets:
- vidore/colpali_train_set
language:
- en
base_model:
- vidore/colpaligemma-3b-pt-448-base
new_version: vidore/colpali-v1.3-hf
pipeline_tag: visual-document-retrieval
---

> [!IMPORTANT]
> This version of ColPali should be loaded with the `transformers 🤗` release, not with `colpali-engine`.
> It was converted using the [`convert_colpali_weights_to_hf.py` script](https://github.com/tonywu71/transformers/blob/21c1309637aee97ca4fb8eb3b31830913a0f99a5/src/transformers/models/colpali/convert_colpali_weights_to_hf.py)
> from the [`vidore/colpali-v1.2-merged`](https://huggingface.co/vidore/colpali-v1.2-merged) checkpoint.

# ColPali: Visual Retriever based on PaliGemma-3B with ColBERT strategy

ColPali is a model based on a novel model architecture and training strategy based on Vision Language Models (VLMs) to efficiently index documents from their visual features.
It is a [PaliGemma-3B](https://huggingface.co/google/paligemma-3b-mix-448) extension that generates [ColBERT](https://arxiv.org/abs/2004.12832)- style multi-vector representations of text and images. 
It was introduced in the paper [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449) and first released in [this repository](https://github.com/ManuelFay/colpali)

The HuggingFace `transformers` 🤗 implementation was contributed by Tony Wu ([@tonywu71](https://huggingface.co/tonywu71)) and Yoni Gozlan ([@yonigozlan](https://huggingface.co/yonigozlan)).

<p align="center"><img width=800 src="https://github.com/illuin-tech/colpali/blob/main/assets/colpali_architecture.webp?raw=true"/></p>


## Model Description

This model is built iteratively starting from an off-the-shelf [SigLIP](https://huggingface.co/google/siglip-so400m-patch14-384) model. 
We finetuned it to create [BiSigLIP](https://huggingface.co/vidore/bisiglip) and fed the patch-embeddings output by SigLIP to an LLM, [PaliGemma-3B](https://huggingface.co/google/paligemma-3b-mix-448) to create [BiPali](https://huggingface.co/vidore/bipali). 

One benefit of inputting image patch embeddings through a language model is that they are natively mapped to a latent space similar to textual input (query). 
This enables leveraging the [ColBERT](https://arxiv.org/abs/2004.12832) strategy to compute interactions between text tokens and image patches, which enables a step-change improvement in performance compared to BiPali. 

## Model Training

### Dataset
Our training dataset of 127,460 query-page pairs is comprised of train sets of openly available academic datasets (63%) and a synthetic dataset made up of pages from web-crawled PDF documents and augmented with VLM-generated (Claude-3 Sonnet) pseudo-questions (37%). 
Our training set is fully English by design, enabling us to study zero-shot generalization to non-English languages. We explicitly verify no multi-page PDF document is used both [*ViDoRe*](https://huggingface.co/collections/vidore/vidore-benchmark-667173f98e70a1c0fa4db00d) and in the train set to prevent evaluation contamination. 
A validation set is created with 2% of the samples to tune hyperparameters.

*Note: Multilingual data is present in the pretraining corpus of the language model (Gemma-2B) and potentially occurs during PaliGemma-3B's multimodal training.*

### Parameters

All models are trained for 1 epoch on the train set. Unless specified otherwise, we train models in `bfloat16` format, use low-rank adapters ([LoRA](https://arxiv.org/abs/2106.09685)) 
with `alpha=32`  and `r=32` on the transformer layers from the language model, 
as well as the final randomly initialized projection layer, and use a `paged_adamw_8bit` optimizer. 
We train on an 8 GPU setup with data parallelism, a learning rate of 5e-5 with linear decay with 2.5% warmup steps, and a batch size of 32.

## Usage

```python
import torch
from PIL import Image

from transformers import ColPaliForRetrieval, ColPaliProcessor

model_name = "vidore/colpali-v1.2-hf"

model = ColPaliForRetrieval.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",  # or "mps" if on Apple Silicon
).eval()

processor = ColPaliProcessor.from_pretrained(model_name)

# Your inputs
images = [
    Image.new("RGB", (32, 32), color="white"),
    Image.new("RGB", (16, 16), color="black"),
]
queries = [
    "What is the organizational structure for our R&D department?",
    "Can you provide a breakdown of last year’s financial performance?",
]

# Process the inputs
batch_images = processor(images=images).to(model.device)
batch_queries = processor(text=queries).to(model.device)

# Forward pass
with torch.no_grad():
    image_embeddings = model(**batch_images)
    query_embeddings = model(**batch_queries)

# Score the queries against the images
scores = processor.score_retrieval(query_embeddings.embeddings, image_embeddings.embeddings)
```

## Resources

- The *ColPali* arXiv paper can be found [here](https://doi.org/10.48550/arXiv.2407.01449). 📄
- The official blog post detailing ColPali can be found [here](https://huggingface.co/blog/manu/colpali). 📝
- The original model implementation code for the ColPali model and for the `colpali-engine` package can be found [here](https://github.com/illuin-tech/colpali). 🌎
- Cookbooks for learning to use the transformers-native version of *ColPali*, fine-tuning, and similarity maps generation can be found [here](https://github.com/tonywu71/colpali-cookbooks). 📚

## Limitations

 - **Focus**: The model primarily focuses on PDF-type documents and high-ressources languages, potentially limiting its generalization to other document types or less represented languages.
 - **Support**: The model relies on multi-vector retreiving derived from the ColBERT late interaction mechanism, which may require engineering efforts to adapt to widely used vector retrieval frameworks that lack native multi-vector support.

## License

ColPali's vision language backbone model (PaliGemma) is under `gemma` license as specified in its [model card](https://huggingface.co/google/paligemma-3b-mix-448). ColPali inherits from this `gemma` license.

## Contact

- Manuel Faysse: manuel.faysse@illuin.tech
- Hugues Sibille: hugues.sibille@illuin.tech
- Tony Wu: tony.wu@illuin.tech


## Citation

If you use any datasets or models from this organization in your research, please cite the original dataset as follows:

```bibtex
@misc{faysse2024colpaliefficientdocumentretrieval,
  title={ColPali: Efficient Document Retrieval with Vision Language Models}, 
  author={Manuel Faysse and Hugues Sibille and Tony Wu and Bilel Omrani and Gautier Viaud and Céline Hudelot and Pierre Colombo},
  year={2024},
  eprint={2407.01449},
  archivePrefix={arXiv},
  primaryClass={cs.IR},
  url={https://arxiv.org/abs/2407.01449}, 
}
```