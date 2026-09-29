---
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
license: llama3.2
base_model:
- meta-llama/Llama-3.2-1B-Instruct
---


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64a28db2f1968b7d7f357182/BKHwk3YnJXZyIAHa-QbAi.png)
This model was quantized by [SanctumAI](https://sanctum.ai). To leave feedback, join our community in [Discord](https://discord.gg/7ZNE78HJKh).*

# Llama 3.2 1B Instruct GGUF

**Model creator:** [meta-llama](https://huggingface.co/meta-llama)<br>
**Original model**: [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)<br>

## Model Summary:

The Meta Llama 3.2 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction-tuned generative models in 1B and 3B sizes (text in/text out). The Llama 3.2 instruction-tuned text only models are optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks. They outperform many of the available open source and closed chat models on common industry benchmarks.

## Prompt Template:

If you're using Sanctum app, simply use `Llama 3` model preset.

Prompt template:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```

## Hardware Requirements Estimate

| Name | Quant method | Size | Memory (RAM, vRAM) required |
| ---- | ---- | ---- | ---- |
| [llama-3.2-1b-instruct.Q2_K.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q2_K.gguf) | Q2_K | 0.58 GB | 3.93 GB |
| [llama-3.2-1b-instruct.Q3_K_S.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q3_K_S.gguf) | Q3_K_S | 0.64 GB | 3.99 GB |
| [llama-3.2-1b-instruct.Q3_K_M.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q3_K_M.gguf) | Q3_K_M | 0.69 GB | 4.03 GB |
| [llama-3.2-1b-instruct.Q3_K_L.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q3_K_L.gguf) | Q3_K_L | 0.73 GB | 4.07 GB |
| [llama-3.2-1b-instruct.Q4_0.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q4_0.gguf) | Q4_0 | 0.77 GB | 4.11 GB |
| [llama-3.2-1b-instruct.Q4_K_S.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q4_K_S.gguf) | Q4_K_S | 0.78 GB | 4.11 GB |
| [llama-3.2-1b-instruct.Q4_K_M.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q4_K_M.gguf) | Q4_K_M | 0.81 GB | 4.14 GB |
| [llama-3.2-1b-instruct.Q4_K.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q4_K.gguf) | Q4_K | 0.81 GB | 4.14 GB |
| [llama-3.2-1b-instruct.Q4_1.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q4_1.gguf) | Q4_1 | 0.83 GB | 4.16 GB |
| [llama-3.2-1b-instruct.Q5_0.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q5_0.gguf) | Q5_0 | 0.89 GB | 4.22 GB |
| [llama-3.2-1b-instruct.Q5_K_S.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q5_K_S.gguf) | Q5_K_S | 0.89 GB | 4.22 GB |
| [llama-3.2-1b-instruct.Q5_K_M.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q5_K_M.gguf) | Q5_K_M | 0.91 GB | 4.24 GB |
| [llama-3.2-1b-instruct.Q5_K.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q5_K.gguf) | Q5_K | 0.91 GB | 4.24 GB |
| [llama-3.2-1b-instruct.Q5_1.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q5_1.gguf) | Q5_1 | 0.95 GB | 4.28 GB |
| [llama-3.2-1b-instruct.Q6_K.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q6_K.gguf) | Q6_K | 1.02 GB | 4.34 GB |
| [llama-3.2-1b-instruct.Q8_0.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.Q8_0.gguf) | Q8_0 | 1.32 GB | 4.62 GB |
| [llama-3.2-1b-instruct.f16.gguf](https://huggingface.co/SanctumAI/Llama-3.2-1B-Instruct-GGUF/blob/main/llama-3.2-1b-instruct.f16.gguf) | f16 | 2.48 GB | 5.70 GB |
## Disclaimer

Sanctum is not the creator, originator, or owner of any Model featured in the Models section of the Sanctum application. Each Model is created and provided by third parties. Sanctum does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Model listed there. You understand that supported Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Model is the sole responsibility of the person or entity who originated such Model. Sanctum may not monitor or control the Models supported and cannot, and does not, take responsibility for any such Model. Sanctum disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Models. Sanctum further disclaims any warranty that the Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Models, your downloading of any Model, or use of any other Model provided by or through Sanctum.