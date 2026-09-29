---
license: mit
---

The multilingual-e5 family is one of the best options for multilingual embedding models.

This is the GGUF version of https://huggingface.co/intfloat/multilingual-e5-large-instruct.
Check out their prompt recommendations for different tasks!

It is supported since the XLMRoberta addition in llama.cpp was merged on
6th August 2024. https://github.com/ggerganov/llama.cpp/pull/8658

Currently q4_k_m, q6_k, q8_0 and f16 versions are available.
I would recommend q6_k or q8_0. In general you barely have any performance loss going to 8-bit quantization from base models, 
while there usually is a small but noticable dropoff occuring somewhere between q6-q4. 
At some point the dropoff gets pretty massive going towards ~q3 or lower.