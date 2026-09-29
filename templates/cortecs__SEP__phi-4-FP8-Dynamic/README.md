---

base_model: microsoft/phi-4

---
This is a quantization of the [phi-4](https://huggingface.co/microsoft/phi-4).

The phi-4 model is a cutting-edge open-source LLM developed using a diverse mix of synthetic datasets, curated public domain web content, and acquired academic resources, including books and Q&A datasets. This deliberate data selection ensures the training of compact yet highly capable models with an emphasis on quality and advanced reasoning. To further enhance its performance, phi-4 underwent a rigorous alignment process that included supervised fine-tuning and direct preference optimization, resulting in precise instruction adherence and robust safety measures.
## Evaluations
This model provides an accuracy recovery of 99.68%. 

| __English__   | __[phi-4](https://huggingface.co/microsoft/phi-4)__   | __[phi-4-FP8-Dynamic (this)](https://huggingface.co/cortecs/phi-4-FP8-Dynamic)__   |
|:--------------|:------------------------------------------------------|:-----------------------------------------------------------------------------------|
| Avg.          | 70.75                                                 | 70.7                                                                               |
| Arc           | 68.7                                                  | 68.7                                                                               |
| Hellaswag     | 72.8                                                  | 72.7                                                                               |
|               |                                                       |                                                                                    |
| __French__   | __[phi-4](https://huggingface.co/microsoft/phi-4)__   | __[phi-4-FP8-Dynamic (this)](https://huggingface.co/cortecs/phi-4-FP8-Dynamic)__   |
| Avg.         | 68.67                                                 | 68.87                                                                              |
| Arc          | 59.4                                                  | 59.5                                                                               |
| Hellaswag    | 72.0                                                  | 72.0                                                                               |
| MMLU         | 74.6                                                  | 75.1                                                                               |
|              |                                                       |                                                                                    |
| __German__   | __[phi-4](https://huggingface.co/microsoft/phi-4)__   | __[phi-4-FP8-Dynamic (this)](https://huggingface.co/cortecs/phi-4-FP8-Dynamic)__   |
| Avg.         | 68.73                                                 | 68.33                                                                              |
| Arc          | 60.2                                                  | 60.0                                                                               |
| Hellaswag    | 69.8                                                  | 69.6                                                                               |
| MMLU         | 76.2                                                  | 75.4                                                                               |
|              |                                                       |                                                                                    |
| __Italian__   | __[phi-4](https://huggingface.co/microsoft/phi-4)__   | __[phi-4-FP8-Dynamic (this)](https://huggingface.co/cortecs/phi-4-FP8-Dynamic)__   |
| Avg.          | 69.3                                                  | 69.07                                                                              |
| Arc           | 61.1                                                  | 61.3                                                                               |
| Hellaswag     | 73.1                                                  | 72.5                                                                               |
| MMLU          | 73.7                                                  | 73.4                                                                               |
|               |                                                       |                                                                                    |
| __Spanish__   |   __[phi-4](https://huggingface.co/microsoft/phi-4)__ |   __[phi-4-FP8-Dynamic (this)](https://huggingface.co/cortecs/phi-4-FP8-Dynamic)__ |
| Avg.          |                                                  70.6 |                                                                              70.03 |
| Arc           |                                                  61.6 |                                                                              61    |
| Hellaswag     |                                                  75.3 |                                                                              74.6  |
| MMLU          |                                                  74.9 |                                                                              74.5  |

We did not check for data contamination.
     Evaluation was done using [Eval. Harness](https://github.com/EleutherAI/lm-evaluation-harness) with `limit=1000`. 
    
## Usage
Install **vLLM** and 
    run the [server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#openai-compatible-server):
    
```
python -m vllm.entrypoints.openai.api_server --model cortecs/phi-4-FP8-Dynamic --max-model-len 16384
```
Access the model:
```
curl http://localhost:8000/v1/completions     -H "Content-Type: application/json"     -d ' {
        "model": "cortecs/phi-4-FP8-Dynamic",
        "prompt": "San Francisco is a"
    } '
```
⚡ This model is optimized to handle heavy workloads providing a total throughput of ️**4623 tokens per second** using one NVIDIA L40S ⚡