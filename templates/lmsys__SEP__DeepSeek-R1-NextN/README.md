# DeepSeek-R1-NextN
NextN layer exported from [deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) model with [script](https://github.com/sgl-project/sglang/blob/main/scripts/export_deepseek_nextn.py). Used for speculative decoding in [SGLang](https://github.com/sgl-project/sglang).

## Usage
```
python3 -m sglang.launch_server --model deepseek-ai/DeepSeek-R1 --speculative-algo EAGLE --speculative-draft lmsys/DeepSeek-R1-NextN --speculative-num-steps 2 --speculative-eagle-topk 4 --speculative-num-draft-tokens 4 --trust-remote --tp 8
```