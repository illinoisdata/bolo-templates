---
license: gemma
metrics:
- perplexity
base_model:
- google/gemma-3-27b-it-qat-q4_0-gguf
---

This is a requantized version of https://huggingface.co/google/gemma-3-27b-it-qat-q4_0-gguf.

The official QAT weights released by google use fp16 (instead of Q6_K) for the embeddings table, which makes this model take a significant extra amount of memory (and storage) compared to what Q4_0 quants are supposed to take. 
~~Instead of quantizing the table myself, I extracted it from Bartowski's quantized models.~~ 
Requantizing with llama.cpp achieves a very similar result.

Here are some benchmark results:

| Model | File size ↓ | PPL (wiki.text.raw) ↓ | Hellaswag, 4k tasks ↑ |
| --- | --- | --- | --- |
| [This model](https://huggingface.co/stduhpf/google-gemma-3-27b-it-qat-q4_0-gguf-small/blob/main/gemma-3-27b-it-q4_0_s.gguf) | 15.6 GB | 8.2335 +/- 0.06321 | 82.875% [81.6761%, 84.0108%] |
| [This model (previous version)](https://huggingface.co/stduhpf/google-gemma-3-27b-it-qat-q4_0-gguf-small/blob/d0de6ea76eafadb4ff5ad66ebfa3c1d2cb7c9c3f/gemma-3-27b-it-q4_0_s.gguf) | 15.6 GB | 8.2291 +/- 0.06315 | 82.725% [81.5222%, 83.8650%] |
| [QAT Q4_0 (google)](https://huggingface.co/google/gemma-3-27b-it-qat-q4_0-gguf/blob/main/gemma-3-27b-it-q4_0.gguf) | 17.2 GB | 8.2323 +/- 0.06320 | 82.850% [81.6505%, 83.9865%] |

Note that this model ends up smaller than the Q4_0 from Bartowski. This is because llama.cpp sets some tensors to Q4_1 when quantizing models to Q4_0 with imatrix, but this is a static quant.
The perplexity score for this one is even lower with this model compared to the original model by Google, but the results are within margin of error, so it's probably just luck.

I also fixed the control token metadata, which was slightly degrading the performance of the model in instruct mode. Shoutout to ngxson for [finding the issue](https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-gguf/discussions/3#67f6a2e0207b4bceea793151),
tdh111 for [making me aware of the issue](https://huggingface.co/stduhpf/google-gemma-3-27b-it-qat-q4_0-gguf-small/discussions/3#67f74fdf8411d4d6a82049db), 
and u/dampflokfreund on reddit ([Dampfinchen](https://huggingface.co/Dampfinchen) on Huggingface) for [sharing the steps to fix it](https://www.reddit.com/r/LocalLLaMA/comments/1jvi860/comment/mmcuvw2).