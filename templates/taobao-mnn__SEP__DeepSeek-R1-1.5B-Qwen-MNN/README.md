---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
tags:
- chat
---
# DeepSeek-R1-1.5B-Qwen-MNN

## Introduction
This model is a 4-bit quantized version of the MNN model exported from DeepSeek-R1-1.5B-Qwen using [llmexport](https://github.com/alibaba/MNN/tree/master/transformers/llm/export).

## Download
```bash
# install huggingface
pip install huggingface
```
```bash
# shell download
huggingface download --model 'taobao-mnn/DeepSeek-R1-1.5B-Qwen-MNN' --local_dir 'path/to/dir'
```
```python
# SDK download
from huggingface_hub import snapshot_download
model_dir = snapshot_download('taobao-mnn/DeepSeek-R1-1.5B-Qwen-MNN')
```

```bash
# git clone
git clone https://www.modelscope.cn/taobao-mnn/DeepSeek-R1-1.5B-Qwen-MNN
```

## Usage
```bash
# clone MNN source
git clone https://github.com/alibaba/MNN.git

# compile
cd MNN
mkdir build && cd build
cmake .. -DMNN_LOW_MEMORY=true -DMNN_CPU_WEIGHT_DEQUANT_GEMM=true -DMNN_BUILD_LLM=true -DMNN_SUPPORT_TRANSFORMER_FUSE=true
make -j

# run
./llm_demo /path/to/DeepSeek-R1-1.5B-Qwen-MNN/config.json prompt.txt
```

## Document
[MNN-LLM](https://mnn-docs.readthedocs.io/en/latest/transformers/llm.html#)