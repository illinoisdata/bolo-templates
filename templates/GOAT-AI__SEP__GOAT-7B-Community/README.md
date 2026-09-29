---
license: llama2
model_type: llama
tags:
  - facebook
  - meta
  - pytorch
  - llama
  - llama-2
---

# GOAT-7B-Community model

![GOAT-7B-Community](https://api-adaptive-li.s3.us-west-2.amazonaws.com/goat-ai/Comp+2_00000.png)

GOAT-7B-Community model is supervised finetuned (SFT) version of LLaMA 2 developed by GOAT.AI lab on user-shared conversations from GoatChat app.

# Model description
 - **Base Architecture:** LLaMA 2 7B flavour
 - **Dataset size:** 72K multi-turn dialogues
 - **License:** llama2
 - **Context window length:** 4096 tokens

### Learn more

- **Blog:** https://www.blog.goat.ai/goat-7b-community-tops-among-7b-models/
- **Paper:** https://arxiv.org/abs/2308.13449
- **Demo:** https://3f3fb57083197123c8.gradio.live/

## Uses

The main purpose of GOAT-7B-Community is to facilitate research on large language models and chatbots. It is specifically designed for researchers and hobbyists working in the fields of natural language processing, machine learning, and artificial intelligence.

## Usage

Usage can be either self-hosted via `transformers` or used with Spaces

```
import torch

from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "GOAT-AI/GOAT-7B-Community"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16
)
```

## Training dataset

Training dataset was collected from users conversations with GoatChat app and OpenAssistant. We will not release the dataset. 

## Evaluation

GOAT-7B-Community model is evaluated against common metrics for evaluating language models, including MMLU and BigBench Hard. We still continue to evaluate all our models and will share details soon.

- **MMLU:** 49.31
- **BBH:** 35.7

## License

GOAT-7B-Community model is based on [Meta's LLaMA-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf), and using own datasets.  

GOAT-7B-Community model weights are available under LLAMA-2 license. Note that the GOAT-7B-Community model weights require access to the LLaMA-2 model weighs. The GOAT-7B-Community model is based on LLaMA-2 and should be used according to the LLaMA-2 license. 

### Risks and Biases 

GOAT-7B-Community model can produce factually incorrect output and should not be relied on to deliver factually accurate information. The model was trained on various private and public datasets. Therefore, the GOAT-7B-Community model could possibly generate wrong, biased, or otherwise offensive outputs.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_GOAT-AI__GOAT-7B-Community)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 42.74   |
| ARC (25-shot)         | 48.81          |
| HellaSwag (10-shot)   | 74.63    |
| MMLU (5-shot)         | 49.58         |
| TruthfulQA (0-shot)   | 42.48   |
| Winogrande (5-shot)   | 72.3   |
| GSM8K (5-shot)        | 4.47        |
| DROP (3-shot)         | 6.91         |
