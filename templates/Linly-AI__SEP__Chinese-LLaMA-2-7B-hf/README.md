基于中英文混合语料增量训练，词表扩充汉字。

训练细节和benchmark指标： https://github.com/CVI-SZU/Linly


```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Linly-AI/Chinese-LLaMA-2-7B-hf", device_map="cuda:0", torch_dtype=torch.float16, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("Linly-AI/Chinese-LLaMA-2-7B-hf", use_fast=False, trust_remote_code=True)
prompt = "北京有什么好玩的地方？"

prompt = f"### Instruction:{prompt.strip()}  ### Response:"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")
generate_ids = model.generate(inputs.input_ids, do_sample=True, max_new_tokens=2048, top_k=10, top_p=0.85, temperature=1, repetition_penalty=1.15, eos_token_id=2, bos_token_id=1, pad_token_id=0)
response = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
response = response.lstrip(prompt)
```

