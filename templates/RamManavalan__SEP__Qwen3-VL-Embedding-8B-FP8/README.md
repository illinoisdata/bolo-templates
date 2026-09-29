---
library_name: transformers
tags:
- fp8
- vllm
- vision
- quantized
- compressed-tensors
- qwen3_vl
- embedding
- multimodal embedding
- feature-extraction
license: apache-2.0
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
base_model: Qwen/Qwen3-VL-Embedding-8B
pipeline_tag: feature-extraction
---

# Qwen3-VL-Embedding-8B-FP8

This is an **FP8 quantized** version of [Qwen/Qwen3-VL-Embedding-8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B), optimized for efficient inference with vLLM.

## Model Overview

| Attribute | Value |
|-----------|-------|
| Base Model | [Qwen/Qwen3-VL-Embedding-8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B) |
| Quantization | FP8 Dynamic (W8A8) |
| Original Size | ~16 GB (BF16) |
| Quantized Size | ~9 GB (FP8) |
| Memory Savings | ~45% |
| Embedding Dimension | 4096 |
| Supported Inputs | Text, Images, Videos, Multimodal |
| Context Length | 32K tokens |

## Highlights

- **Multimodal Versatility**: Handles text, images, screenshots, and video inputs
- **Efficient Inference**: ~45% memory reduction with minimal accuracy loss
- **vLLM Compatible**: Works with vLLM's pooling runner for high-throughput embedding
- **No Calibration Required**: Uses FP8_DYNAMIC scheme (data-free quantization)

## Quantization Details

| Component | Precision | Notes |
|-----------|-----------|-------|
| Vision Encoder (ViT) | BF16 | Preserved for accuracy |
| LLM Decoder Layers | FP8 | Quantized for efficiency |
| Embeddings | BF16 | Preserved |

- **Scheme**: FP8_DYNAMIC
  - Weights: FP8_E4M3 (per-channel quantization)
  - Activations: Dynamic per-token quantization at runtime
- **Tool**: [llm-compressor](https://github.com/vllm-project/llm-compressor)
- **Calibration**: None required (data-free quantization)

## Hardware Requirements

- **GPU**: NVIDIA GPU with FP8 support (compute capability >= 8.9)
  - Blackwell: RTX 5090, RTX 5080
  - Ada Lovelace: RTX 4090, RTX 4080
  - Hopper: H100, H200
- **VRAM**: ~10GB minimum for inference

## Usage

### With vLLM (>=0.14.0) (Recommended)

```python
from vllm import LLM, EngineArgs
import numpy as np

# Initialize vLLM with pooling runner
engine_args = EngineArgs(
    model="RamManavalan/Qwen3-VL-Embedding-8B-FP8",
    runner="pooling",
    dtype="bfloat16",
    trust_remote_code=True,
)
llm = LLM(**vars(engine_args))

# Prepare inputs
tokenizer = llm.get_tokenizer()

def format_input(text, instruction="Represent the user's input."):
    conversation = [
        {"role": "system", "content": [{"type": "text", "text": instruction}]},
        {"role": "user", "content": [{"type": "text", "text": text}]}
    ]
    prompt = tokenizer.apply_chat_template(
        conversation, tokenize=False, add_generation_prompt=True
    )
    return {"prompt": prompt}

# Get embeddings
inputs = [
    format_input("A woman playing with her dog on the beach."),
    format_input("Machine learning for image classification."),
]
outputs = llm.embed(inputs)

# Extract embeddings
embeddings = np.array([o.outputs.embedding for o in outputs])
print(f"Embeddings shape: {embeddings.shape}")  # (2, 4096)

# Compute similarity
similarity = embeddings[0] @ embeddings[1]
print(f"Similarity: {similarity:.4f}")
```

### With vLLM (>=0.14.0) Server

```bash
# Start the server
vllm serve RamManavalan/Qwen3-VL-Embedding-8B-FP8 --task embed

# Query via API
curl http://localhost:8000/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{"input": "Your text here", "model": "RamManavalan/Qwen3-VL-Embedding-8B-FP8"}'
```

### With Transformers

```python
import torch
from transformers import AutoProcessor, Qwen3VLForConditionalGeneration

model = Qwen3VLForConditionalGeneration.from_pretrained(
    "RamManavalan/Qwen3-VL-Embedding-8B-FP8",
    dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(
    "RamManavalan/Qwen3-VL-Embedding-8B-FP8",
    trust_remote_code=True,
)

# Prepare input
messages = [
    {"role": "system", "content": [{"type": "text", "text": "Represent the user's input."}]},
    {"role": "user", "content": [{"type": "text", "text": "Your text here"}]}
]
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=[prompt], return_tensors="pt", padding=True).to(model.device)

# Get embedding (last-token pooling)
with torch.no_grad():
    outputs = model.model(**inputs, output_hidden_states=True)
    # Get the last non-padding token
    seq_len = inputs['attention_mask'].sum(dim=1) - 1
    embedding = outputs.last_hidden_state[0, seq_len[0]]
    embedding = torch.nn.functional.normalize(embedding, p=2, dim=-1)

print(f"Embedding shape: {embedding.shape}")  # (4096,)
```

### Using the Helper Class

This repository includes a helper class for easier embedding extraction:

```python
from scripts.qwen3_vl_embedding import Qwen3VLEmbedder

# Initialize
model = Qwen3VLEmbedder(model_name_or_path="RamManavalan/Qwen3-VL-Embedding-8B-FP8")

# Get embeddings for text, images, or multimodal inputs
inputs = [
    {"text": "A dog on the beach"},
    {"image": "path/to/image.jpg"},
    {"text": "What is in this image?", "image": "path/to/image.jpg"},
]
embeddings = model.process(inputs)
print(f"Embeddings shape: {embeddings.shape}")  # (3, 4096)
```

## Benchmark Results

The base model achieves state-of-the-art performance on multimodal benchmarks:

| Benchmark | Score |
|-----------|-------|
| MMEB-V2 Overall | 77.9 |
| MMTEB Mean | 67.88 |

*FP8 quantization typically preserves >95% of the original model's accuracy.*

## Creation

This model was quantized using [llm-compressor](https://github.com/vllm-project/llm-compressor):

```python
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier

# Load model
model = Qwen3VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-VL-Embedding-8B",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

# FP8 quantization recipe (data-free)
recipe = QuantizationModifier(
    targets="Linear",
    scheme="FP8_DYNAMIC",
    ignore=[
        "lm_head",
        r"re:model\.visual\..*",  # Keep vision encoder in BF16
    ]
)

# Apply quantization
oneshot(model=model, recipe=recipe)

# Save
model.save_pretrained("Qwen3-VL-Embedding-8B-FP8", save_compressed=True)
```

## Citation

If you use this model, please cite the original Qwen3-VL-Embedding paper:

```bibtex
@article{qwen3vlembedding,
  title={Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking},
  author={Li, Mingxin and Zhang, Yanzhao and Long, Dingkun and Chen, Keqin and Song, Sibo and Bai, Shuai and Yang, Zhibo and Xie, Pengjun and Yang, An and Liu, Dayiheng and Zhou, Jingren and Lin, Junyang},
  journal={arXiv preprint arXiv:2601.04720},
  year={2026}
}
```

## License

Apache 2.0 (same as base model)

## Acknowledgments

- [Qwen Team](https://github.com/QwenLM) for the original Qwen3-VL-Embedding model
- [vLLM Team](https://github.com/vllm-project/vllm) for the inference engine
- [Neural Magic](https://github.com/vllm-project/llm-compressor) for llm-compressor
