---
language:
- en
library_name: transformers
tags:
- gpt
- llm
- large language model
inference: false
thumbnail: >-
  https://h2o.ai/etc.clientlibs/h2o/clientlibs/clientlib-site/resources/images/favicon.ico
license: apache-2.0
---
# Model Card

**The Best 3B Model! Surpassing dolly-v2-12b**

The best 3B model on the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard), with performance surpassing dolly-v2-12b

| Metric                | Value |
|-----------------------|-------|
| MMLU (5-shot)         | 27.3  |
| ARC (25-shot)         | 41.7  |
| HellaSwag (10-shot)   | 71.1  |
| TruthfulQA (0-shot)   | 37.9  |
| Avg.                  | 44.5  | 

We use state-of-the-art [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above.


The training code and data will be open sourced later on Github(https://github.com/chi2liu/mamba-gpt-3b)


## Training Dataset

` mamba-gpt-3b-v3 ` is trained on multiply dataset:
  - [Stanford Alpaca (en)](https://github.com/tatsu-lab/stanford_alpaca)
  - [Open Assistant (multilingual)](https://huggingface.co/datasets/OpenAssistant/oasst1)
  - [LIMA (en)](https://huggingface.co/datasets/GAIR/lima)
  - [CodeAlpaca 20k (en)](https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k)


## Summary

We have fine-tuned the open-lama model and surpassed the original model in multiple evaluation subtasks, making it currently the best performing 3B model with comparable performance to llama-7b
- Base model: [openlm-research/open_llama_3b_v2](https://huggingface.co/openlm-research/open_llama_3b_v2)

## Usage

To use the model with the `transformers` library on a machine with GPUs, first make sure you have the `transformers`, `accelerate` and `torch` libraries installed.

```bash
pip install transformers==4.29.2
pip install accelerate==0.19.0
pip install torch==2.0.0
```

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("CobraMamba/mamba-gpt-3b-v3")
model = AutoModelForCausalLM.from_pretrained("CobraMamba/mamba-gpt-3b-v3", trust_remote_code=True, torch_dtype=torch.float16)

input_context = "Your text here"
input_ids = tokenizer.encode(input_context, return_tensors="pt")
output = model.generate(input_ids, max_length=128, temperature=0.7)
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(output_text)

```

## Model Architecture

```
LlamaForCausalLM(
  (model): LlamaModel(
    (embed_tokens): Embedding(32000, 4096, padding_idx=0)
    (layers): ModuleList(
      (0-31): 32 x LlamaDecoderLayer(
        (self_attn): LlamaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (v_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (rotary_emb): LlamaRotaryEmbedding()
        )
        (mlp): LlamaMLP(
          (gate_proj): Linear(in_features=4096, out_features=11008, bias=False)
          (down_proj): Linear(in_features=11008, out_features=4096, bias=False)
          (up_proj): Linear(in_features=4096, out_features=11008, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): LlamaRMSNorm()
        (post_attention_layernorm): LlamaRMSNorm()
      )
    )
    (norm): LlamaRMSNorm()
  )
  (lm_head): Linear(in_features=4096, out_features=32000, bias=False)
)
```

## Citation

If this work is helpful, please kindly cite as:

```bibtex
@Misc{mamba-gpt-3b-v3,
  title = {Mamba-GPT-3b-v3},
  author = {chiliu},
  howpublished = {\url{https://huggingface.co/CobraMamba/mamba-gpt-3b-v3}},
  year = {2023}
}
```


## Disclaimer

Please read this disclaimer carefully before using the large language model provided in this repository. Your use of the model signifies your agreement to the following terms and conditions.

- Biases and Offensiveness: The large language model is trained on a diverse range of internet text data, which may contain biased, racist, offensive, or otherwise inappropriate content. By using this model, you acknowledge and accept that the generated content may sometimes exhibit biases or produce content that is offensive or inappropriate. The developers of this repository do not endorse, support, or promote any such content or viewpoints.
- Limitations: The large language model is an AI-based tool and not a human. It may produce incorrect, nonsensical, or irrelevant responses. It is the user's responsibility to critically evaluate the generated content and use it at their discretion.
- Use at Your Own Risk: Users of this large language model must assume full responsibility for any consequences that may arise from their use of the tool. The developers and contributors of this repository shall not be held liable for any damages, losses, or harm resulting from the use or misuse of the provided model.
- Ethical Considerations: Users are encouraged to use the large language model responsibly and ethically. By using this model, you agree not to use it for purposes that promote hate speech, discrimination, harassment, or any form of illegal or harmful activities.
- Reporting Issues: If you encounter any biased, offensive, or otherwise inappropriate content generated by the large language model, please report it to the repository maintainers through the provided channels. Your feedback will help improve the model and mitigate potential issues.
- Changes to this Disclaimer: The developers of this repository reserve the right to modify or update this disclaimer at any time without prior notice. It is the user's responsibility to periodically review the disclaimer to stay informed about any changes.

By using the large language model provided in this repository, you agree to accept and comply with the terms and conditions outlined in this disclaimer. If you do not agree with any part of this disclaimer, you should refrain from using the model and any content generated by it.
