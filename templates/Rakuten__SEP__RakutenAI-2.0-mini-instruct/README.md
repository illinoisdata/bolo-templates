---
license: apache-2.0
language:
- en
- ja
base_model:
- Rakuten/RakutenAI-2.0-mini
---

# RakutenAI-2.0-mini-instruct
## Model Description
RakutenAI-2.0-mini-instruct is a lightweight yet powerful fine-tuned variant of [RakutenAI-2.0-mini](https://huggingface.co/Rakuten/RakutenAI-2.0-mini), specifically designed for edge devices and resource-constrained environments. While compact in size, this model delivers efficient, high-quality instruction-following capabilities, making it an ideal choice for on-device AI applications, low-latency inference, and cost-effective deployment. It achieves competitive performance within the sub-2B parameter category on Japanese MT Bench, offering a balance of speed, efficiency, and accuracy for real-world use cases. 

*If you are looking for foundation model, check [RakutenAI-2.0-mini](https://huggingface.co/Rakuten/RakutenAI-2.0-mini)*.

## Model Evaluation Results

|Instruct Model Name                                          | Size       | Japanese MT-Bench Score  |
|:-------------------------------------------------------------|:-----------:|:-------------------------:|
| Rakuten/RakutenAI-2.0-mini-instruct                                 | 1.5B | 4.91                     |
| llm-jp/llm-jp-3-1.8b-instruct                    | 1.8B | 4.70                      |
| llm-jp/llm-jp-3-3.7b-instruct                        | 3.7B | 4.98                      |
| SakanaAI/EvoLLM-JP-A-v1-7B            | 7B | 3.80                      |
| SakanaAI/EvoLLM-JP-v1-7B                 | 7B | 4.58                      |


<div style="text-align: center;">Table1: RakutenAI-2.0-mini-instruct performance on MT Bench in comparison with other Japanese open models.</div>


**Note on Evaluation Scores:**
- Japanese MT-bench is a set of 80 challenging open-ended questions for evaluating chat assistants on eight dimensions: writing, roleplay, reasoning, math, coding, extraction, stem, humanities. https://github.com/Stability-AI/FastChat/tree/jp-stable/fastchat/llm_judge Evaluation of responses is conducted with GPT4(gpt-4o-2024-05-13) as a judge, in line with public leaderboard. 
- The Japanese research community cautions against not to evaluate fine-tuned models on LM Harness due to task contamination, so we have not included the LM-Harness scores in this model card for instruct models. ```LLM-jp: jasterを用いてインストラクションチューニングを施したモデルが、テストデータをインストラクションチューニングに使用していない場合でも, llm-jp-evalの評価スコアを非常に高くすることができることが明らかになっている. したがって、高い評価スコアを得たからといって、他のLLMよりも性能が優れていると断言するのは適切ではないことに注意されたい。 Machine Translation: It has become clear that models that have been instruction tuned using Jaster can achieve very high evaluation scores on LLM-JP-EVAL, even if test data is not used for instruction tuning. Therefore, please note that it is not appropriate to assert that a model's performance is superior to other LLMs just because it has a high evaluation score.``` More details can be found at [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval/blob/dev/README.md).
- Final score `(4.91 +/- 0.023)` for RakutenAI-2.0-mini-instruct is average of 3 runs on Japanese MT-Bench. Model outputs and judge outputs are uploaded for reference.


## Model Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "Rakuten/RakutenAI-2.0-mini-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype="auto", device_map="auto")
model.eval()

chat = [
    {"role": "system", "content": "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."},
    {"role": "user", "content": "How to make an authentic Spanish Omelette?"},
]

input_ids = tokenizer.apply_chat_template(chat, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(device=model.device)
attention_mask = input_ids.ne(tokenizer.pad_token_id).long()
tokens = model.generate(
    input_ids,
    max_length=2048,
    do_sample=False,
    num_beams=1,
    pad_token_id=tokenizer.eos_token_id,
    attention_mask=attention_mask,
)
out = tokenizer.decode(tokens[0][len(input_ids[0]):], skip_special_tokens=True)
print("ASSISTANT:\n" + out)
print()
```
## Model Details

* **Developed by**: [Rakuten Group, Inc.](https://ai.rakuten.com/)
* **Language(s)**: Japanese, English
* **License**: This model is licensed under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
* **Model Architecture**: Transformer

### Limitations and Bias

The suite of RakutenAI-2.0 models is capable of generating human-like text on a wide range of topics. However, like all LLMs, they have limitations and can produce biased, inaccurate, or unsafe outputs. Please exercise caution and judgement while interacting with them.

## Citation
For citing our work on the suite of RakutenAI-2.0 models, please use: 

```
@misc{rakutengroup2025rakutenai2.0,
  author = {Rakuten Group, Inc.},
  title = {RakutenAI-2.0},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/Rakuten},
}

```