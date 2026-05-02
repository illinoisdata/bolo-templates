---
library_name: transformers
tags:
- colpali
license: apache-2.0
datasets:
- vidore/colpali_train_set
language:
- en
base_model:
- vidore/colqwen2-base
pipeline_tag: visual-document-retrieval
---

> [!IMPORTANT]
> This version of ColQwen2 should be loaded with the `transformers 🤗` release, not with `colpali-engine`.
> It was converted using the `convert_colqwen2_weights_to_hf.py` script
> from the [`vidore/colqwen2-v1.0-merged`](https://huggingface.co/vidore/colqwen2-v1.0-merged) checkpoint.

# ColQwen2: Visual Retriever based on Qwen2-VL-2B-Instruct with ColBERT strategy

ColQwen2 is a model based on a novel model architecture and training strategy based on Vision Language Models (VLMs) to efficiently index documents from their visual features.
It is a [Qwen2-VL-2B](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) extension that generates [ColBERT](https://arxiv.org/abs/2004.12832)- style multi-vector representations of text and images. 
It was introduced in the paper [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449) and first released in [this repository](https://github.com/ManuelFay/colpali)

<p align="center"><img width=800 src="https://github.com/illuin-tech/colpali/blob/main/assets/colpali_architecture.webp?raw=true"/></p>

The HuggingFace `transformers` 🤗 implementation was contributed by Tony Wu ([@tonywu71](https://huggingface.co/tonywu71)) and Yoni Gozlan ([@yonigozlan](https://huggingface.co/yonigozlan)).

## Model Description

Read the `transformers` 🤗 model card: https://huggingface.co/docs/transformers/en/model_doc/colqwen2.

## Model Training

### Dataset
Our training dataset of 127,460 query-page pairs is comprised of train sets of openly available academic datasets (63%) and a synthetic dataset made up of pages from web-crawled PDF documents and augmented with VLM-generated (Claude-3 Sonnet) pseudo-questions (37%). 
Our training set is fully English by design, enabling us to study zero-shot generalization to non-English languages. We explicitly verify no multi-page PDF document is used both [*ViDoRe*](https://huggingface.co/collections/vidore/vidore-benchmark-667173f98e70a1c0fa4db00d) and in the train set to prevent evaluation contamination. 
A validation set is created with 2% of the samples to tune hyperparameters.

## Usage

```python
import requests
import torch
from PIL import Image

from transformers import ColQwen2ForRetrieval, ColQwen2Processor
from transformers.utils.import_utils import is_flash_attn_2_available


# Load the model and the processor
model_name = "vidore/colqwen2-v1.0-hf"

model = ColQwen2ForRetrieval.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",  # "cpu", "cuda", or "mps" for Apple Silicon
    attn_implementation="flash_attention_2" if is_flash_attn_2_available() else "sdpa",
)
processor = ColQwen2Processor.from_pretrained(model_name)

# The document page screenshots from your corpus
url1 = "https://upload.wikimedia.org/wikipedia/commons/8/89/US-original-Declaration-1776.jpg"
url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Romeoandjuliet1597.jpg/500px-Romeoandjuliet1597.jpg"

images = [
    Image.open(requests.get(url1, stream=True).raw),
    Image.open(requests.get(url2, stream=True).raw),
]

# The queries you want to retrieve documents for
queries = [
    "When was the United States Declaration of Independence proclaimed?",
    "Who printed the edition of Romeo and Juliet?",
]

# Process the inputs
inputs_images = processor(images=images).to(model.device)
inputs_text = processor(text=queries).to(model.device)

# Forward pass
with torch.no_grad():
    image_embeddings = model(**inputs_images).embeddings
    query_embeddings = model(**inputs_text).embeddings

# Score the queries against the images
scores = processor.score_retrieval(query_embeddings, image_embeddings)

print("Retrieval scores (query x image):")
print(scores)
```

If you have issue with loading the images with PIL, you can use the following code to create dummy images:

```python
images = [
    Image.new("RGB", (128, 128), color="white"),
    Image.new("RGB", (64, 32), color="black"),
]
```

## Limitations

 - **Focus**: The model primarily focuses on PDF-type documents and high-ressources languages, potentially limiting its generalization to other document types or less represented languages.
 - **Support**: The model relies on multi-vector retreiving derived from the ColBERT late interaction mechanism, which may require engineering efforts to adapt to widely used vector retrieval frameworks that lack native multi-vector support.

## License

ColQwen2's vision language backbone model (Qwen2-VL) is under `apache-2.0` license. ColQwen2 inherits from this `apache-2.0` license.

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