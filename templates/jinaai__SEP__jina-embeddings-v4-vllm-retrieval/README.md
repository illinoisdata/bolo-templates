---
tags:
- vidore
- colpali
- multimodal-embedding
- multilingual-embedding
- Text-to-Visual Document (T→VD) retrieval
- feature-extraction
- sentence-similarity
- mteb
language:
- multilingual
library_name: transformers
pipeline_tag: visual-document-retrieval
---
<br><br>

<p align="center">
<img src="https://huggingface.co/datasets/jinaai/documentation-images/resolve/main/logo.webp" alt="Jina AI: Your Search Foundation, Supercharged!" width="150px">
</p>


<p align="center">
<b>The embedding model trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

# Jina Embeddings v4: Universal Embeddings for Multimodal Multilingual Retrieval


[Original Model](https://huggingface.co/jinaai/jina-embeddings-v4) | [Blog](https://jina.ai/news/jina-embeddings-v4-universal-embeddings-for-multimodal-multilingual-retrieval) | [Technical Report](https://arxiv.org/abs/2506.18902) | [API](https://jina.ai/embeddings)


## Model Overview

This repository hosts a vLLM-compatible version of [`jina-embeddings-v4`](https://huggingface.co/jinaai/jina-embeddings-v4) with the **retrieval** adapter merged into the base `Qwen2.5-VL` weights. This architecture modification enables native compatibility with vLLM without requiring custom adapter-handling code.


## Usage

```python
import torch
from PIL import Image

from vllm import LLM
from vllm.config import PoolerConfig
from vllm.inputs.data import TextPrompt

# Initialize model
model = LLM(
    model="jinaai/jina-embeddings-v4-vllm-retrieval",
    task="auto",
    override_pooler_config=PoolerConfig(pooling_type="ALL", normalize=False),
    dtype="float16",
)

# Create text prompts
query = "Overview of climate change impacts on coastal cities"
query_prompt = TextPrompt(
    prompt=f"Query: {query}"
)

passage = "The impacts of climate change on coastal cities are significant.."
passage_prompt = TextPrompt(
    prompt=f"Passage: {passage}"
)

# Create image prompt
image = Image.open("<path_to_image>")
image_prompt = TextPrompt(
    prompt="<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>Describe the image.<|im_end|>\n",
    multi_modal_data={"image": image},
)

# Encode all prompts
prompts = [query_prompt, passage_prompt, image_prompt]
outputs = model.encode(prompts)


def get_embeddings(outputs):
    VISION_START_TOKEN_ID, VISION_END_TOKEN_ID = 151652, 151653

    embeddings = []
    for output in outputs:
        if VISION_START_TOKEN_ID in output.prompt_token_ids:
            # Gather only vision tokens
            img_start_pos = torch.where(
                torch.tensor(output.prompt_token_ids) == VISION_START_TOKEN_ID
            )[0][0]
            img_end_pos = torch.where(
                torch.tensor(output.prompt_token_ids) == VISION_END_TOKEN_ID
            )[0][0]
            embeddings_tensor = output.outputs.data.detach().clone()[
                img_start_pos : img_end_pos + 1
            ]
        else:
            # Use all tokens for text-only prompts
            embeddings_tensor = output.outputs.data.detach().clone()
        
        # Pool and normalize embeddings
        pooled_output = (
            embeddings_tensor.sum(dim=0, dtype=torch.float32)
            / embeddings_tensor.shape[0]
        )
        embeddings.append(torch.nn.functional.normalize(pooled_output, dim=-1))
    return embeddings

embeddings = get_embeddings(outputs)
```