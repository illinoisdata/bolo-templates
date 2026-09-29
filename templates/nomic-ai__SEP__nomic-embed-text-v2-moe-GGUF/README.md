---
quantized_by: Nomic
pipeline_tag: sentence-similarity
base_model: nomic-ai/nomic-embed-text-v2-moe
base_model_relation: quantized
tags:
- sentence-similarity
- feature-extraction
license: apache-2.0
language:
- en
- es
- fr
- de
- it
- pt
- pl
- nl
- tr
- ja
- vi
- ru
- id
- ar
- cs
- ro
- sv
- el
- uk
- zh
- hu
- da
- 'no'
- hi
- fi
- bg
- ko
- sk
- th
- he
- ca
- lt
- fa
- ms
- sl
- lv
- mr
- bn
- sq
- cy
- be
- ml
- kn
- mk
- ur
- fy
- te
- eu
- sw
- so
- sd
- uz
- co
- hr
- gu
- ce
- eo
- jv
- la
- zu
- mn
- si
- ga
- ky
- tg
- my
- km
- mg
- pa
- sn
- ha
- ht
- su
- gd
- ny
- ps
- ku
- am
- ig
- lo
- mi
- nn
- sm
- yi
- st
- tl
- xh
- yo
- af
- ta
- tn
- ug
- az
- ba
- bs
- dv
- et
- gl
- gn
- gv
- hy
---

# Llama.cpp Quantizations of nomic-embed-text-v2-moe: Multilingual Mixture of Experts Text Embeddings

[Blog](https://www.nomic.ai/blog/posts/nomic-embed-text-v2) | [Technical Report](https://huggingface.co/papers/2502.07972) | [AWS SageMaker](https://aws.amazon.com/marketplace/seller-profile?id=seller-tpqidcj54zawi) | [Atlas Embedding and Unstructured Data Analytics Platform](https://atlas.nomic.ai)

This model was presented in the paper [Training Sparse Mixture Of Experts Text Embedding Models](https://huggingface.co/papers/2502.07972).

Using <a href="https://github.com/ggml-org/llama.cpp">llama.cpp</a> commit <a href="https://github.com/ggml-org/llama.cpp/tree/e3a9421b78da5c810d812e6348a405f5acc39f34">e3a9421b7</a> for quantization.

Original model: [nomic-embed-text-v2-moe](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe)

## Usage

This model can be used with the [llama.cpp server](https://github.com/ggml-org/llama.cpp/blob/master/examples/embedding#post-v1embeddings-openai-compatible-embeddings-api) and other software that supports llama.cpp embedding models.

Embedding text with `nomic-embed-text` requires task instruction prefixes at the beginning of each string.

For example, the code below shows how to use the `search_query` prefix to embed user questions, e.g. in a RAG application.

Start a llama.cpp server:
```
llama-server -m nomic-embed-text-v2-moe.bf16.gguf --embeddings
```

And run this code:
```python
import requests

def dot(va, vb):
    return sum(a * b for a, b in zip(va, vb))

def embed(texts):
    resp = requests.post('http://localhost:8080/v1/embeddings', json={'input': texts}).json()
    return [d['embedding'] for d in resp['data']]

docs = ['嵌入很酷', '骆驼很酷']  # 'embeddings are cool', 'llamas are cool'
docs_embed = embed(['search_document: ' + d for d in docs])

query = '跟我讲讲嵌入'  # 'tell me about embeddings'
query_embed = embed(['search_query: ' + query])[0]
print(f'query: {query!r}')
for d, e in zip(docs, docs_embed):
    print(f'similarity {dot(query_embed, e):.2f}: {d!r}')
```

You should see output similar to this:
```
query: '跟我讲讲嵌入'
similarity 0.48: '嵌入很酷'
similarity 0.19: '骆驼很酷'
```

## Download a file (not the whole branch) from below:

| Filename                                                                                                                                            | Quant Type | File Size | Description                                                                                    |
| ----                                                                                                                                                | ---------- | --------: | -----------                                                                                    |
| [nomic-embed-text-v2-moe.f32.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.f32.gguf)         | f32        | 1820MiB  | Full FP32 weights.                                                                             |
| [nomic-embed-text-v2-moe.f16.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.f16.gguf)         | f16        |  913MiB  | Full FP16 weights.                                                                             |
| [nomic-embed-text-v2-moe.bf16.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.bf16.gguf)       | bf16       |  913MiB  | Full BF16 weights.                                                                             |
| [nomic-embed-text-v2-moe.Q8\_0.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q8_0.gguf)      | Q8\_0      |  488MiB  | Extremely high quality, generally unneeded but max available quant.                            |
| [nomic-embed-text-v2-moe.Q6\_K.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q6_K.gguf)      | Q6\_K      |  379MiB  | Very high quality, near perfect, *recommended*.                                                |
| [nomic-embed-text-v2-moe.Q5\_K\_M.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q5_K_M.gguf) | Q5\_K\_M   |  354MiB  | High quality, *recommended*.                                                                   |
| [nomic-embed-text-v2-moe.Q5\_K\_S.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q5_K_S.gguf) | Q5\_K\_S   |  343MiB  | High quality, *recommended*.                                                                   |
| [nomic-embed-text-v2-moe.Q4\_1.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q4_1.gguf)      | Q4\_1      |  326MiB  | Legacy format, similar performance to Q4\_K\_S but with improved tokens/watt on Apple silicon. |
| [nomic-embed-text-v2-moe.Q4\_K\_M.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q4_K_M.gguf) | Q4\_K\_M   |  328MiB  | Good quality, default size for most use cases, *recommended*.                                  |
| [nomic-embed-text-v2-moe.Q4\_K\_S.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q4_K_S.gguf) | Q4\_K\_S   |  310MiB  | Slightly lower quality with more space savings, *recommended*.                                 |
| [nomic-embed-text-v2-moe.Q4\_0.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q4_0.gguf)      | Q4\_0      |  309MiB  | Legacy format, offers online repacking for ARM and AVX CPU inference.                          |
| [nomic-embed-text-v2-moe.Q3\_K\_L.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q3_K_L.gguf) | Q3\_K\_L   |  307MiB  | Lower quality but usable, good for low RAM availability.                                       |
| [nomic-embed-text-v2-moe.Q3\_K\_M.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q3_K_M.gguf) | Q3\_K\_M   |  294MiB  | Low quality.                                                                                   |
| [nomic-embed-text-v2-moe.Q3\_K\_S.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q3_K_S.gguf) | Q3\_K\_S   |  275MiB  | Low quality, not recommended.                                                                  |
| [nomic-embed-text-v2-moe.Q2\_K.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/blob/main/nomic-embed-text-v2-moe.Q2_K.gguf)      | Q2\_K      |  261MiB  | Very low quality but surprisingly usable.                                                      |

## Model Overview
`nomic-embed-text-v2-moe` is a SoTA multilingual MoE text embedding model that excels at multilingual retrieval:

- **High Performance**: SoTA Multilingual performance compared to ~300M parameter models, competitive with models 2x in size
- **Multilinguality**: Supports ~100 languages and trained on over 1.6B pairs
- **Flexible Embedding Dimension**: Trained with [Matryoshka Embeddings](https://arxiv.org/abs/2205.13147) with 3x reductions in storage cost with minimal performance degradations
- **Fully Open-Source**: Model weights, [code](https://github.com/nomic-ai/contrastors), and training data (see code repo) released


| Model | Params (M) | Emb Dim | BEIR | MIRACL | Pretrain Data | Finetune Data | Code |
|-------|------------|----------|------|---------|---------------|---------------|------|
| **Nomic Embed v2** | 305 | 768 | 52.86 | **65.80** | ✅ | ✅ | ✅ |
| mE5 Base | 278 | 768 | 48.88 | 62.30 | ❌   | ❌   | ❌   |
| mGTE Base | 305 | 768 | 51.10 | 63.40 | ❌ | ❌ | ❌ |
| Arctic Embed v2 Base | 305 | 768 | **55.40** | 59.90 | ❌ | ❌ | ❌ |
|   |
| BGE M3 | 568 | 1024 | 48.80 | **69.20** | ❌ | ✅ | ❌ |
| Arctic Embed v2 Large | 568 | 1024 | **55.65** | 66.00 | ❌ | ❌ | ❌ |
| mE5 Large | 560 | 1024 | 51.40 | 66.50 | ❌ | ❌ | ❌ |

## Model Architecture
- **Total Parameters**: 475M
- **Active Parameters During Inference**: 305M
- **Architecture Type**: Mixture of Experts (MoE)
- **MoE Configuration**: 8 experts with top-2 routing
- **Embedding Dimensions**: Supports flexible dimension from 768 to 256 through Matryoshka representation learning
- **Maximum Sequence Length**: 512 tokens
- **Languages**: Supports dozens of languages (see Performance section)

## Paper Abstract

Transformer-based text embedding models have improved their performance on benchmarks like MIRACL and BEIR by increasing their parameter counts. However, this scaling approach introduces significant deployment challenges, including increased inference latency and memory usage. These challenges are particularly severe in retrieval-augmented generation (RAG) applications, where large models' increased memory requirements constrain dataset ingestion capacity, and their higher latency directly impacts query-time performance. While causal language models have addressed similar efficiency challenges using Mixture of Experts (MoE) architectures, this approach hasn't been successfully adapted to the general text embedding setting. In this paper, we introduce Nomic Embed v2, the first general purpose MoE text embedding model. Our model outperforms models in the same parameter class on both monolingual and multilingual benchmarks while also maintaining competitive performance with models twice its size. We open-source all code, models, and evaluation data to ensure full reproducibility of our training pipeline at https://github.com/nomic-ai/contrastors.

## Performance

nomic-embed-text-v2-moe performance on BEIR and MIRACL compared to other open-weights embedding models:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/607997c83a565c15675055b3/xadjrezEIM0Q1jbgmjqO7.png)

nomic-embed-text-v2-moe performance on BEIR at 768 dimension and truncated to 256 dimensions:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/607997c83a565c15675055b3/8hmhWQ_TTmlrviZFIBSxo.png)

## Best Practices
- Add appropriate prefixes to your text:
  - For queries: "search\_query: "
  - For documents: "search\_document: "
- Maximum input length is 512 tokens
- For optimal efficiency, consider using the 256-dimension embeddings if storage/compute is a concern

## Limitations
- Performance may vary across different languages
- Resource requirements may be higher than traditional dense models due to MoE architecture
- Must use `trust_remote_code=True` when loading the model to use our custom architecture implementation

## Training Details
![image/png](https://cdn-uploads.huggingface.co/production/uploads/607997c83a565c15675055b3/F0lyAtV8wXMBmxSbtIgL4.png)

- Trained on 1.6 billion high-quality pairs across multiple languages
- Uses consistency filtering to ensure high-quality training data
- Incorporates Matryoshka representation learning for dimension flexibility
- Training includes both weakly-supervised contrastive pretraining and supervised finetuning

For more details, please check out the [blog post](https://www.nomic.ai/blog/posts/nomic-embed-text-v2) and [technical report](https://www.arxiv.org/abs/2502.07972).



## Join the Nomic Community
- Nomic: [https://nomic.ai](https://nomic.ai)
- Discord: [https://discord.gg/myY5YDR8z8](https://discord.gg/myY5YDR8z8)
- Twitter: [https://twitter.com/nomic\_ai](https://twitter.com/nomic_ai)

# Citation
If you find the model, dataset, or training code useful, please cite our work

```bibtex
@misc{nussbaum2025trainingsparsemixtureexperts,
      title={Training Sparse Mixture Of Experts Text Embedding Models},
      author={Zach Nussbaum and Brandon Duderstadt},
      year={2025},
      eprint={2502.07972},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.07972},
}
```