---
license: mit
language:
- en
library_name: transformers
tags:
- dpo
- phi3
- chatml
datasets: argilla/ultrafeedback-binarized-preferences-cleaned
metrics:
- hellaswag
- arc_challenge
- m_mmlu 5 shot
---

# Model Information


Moxoff-Phi3Mini-DPO is an updated version of [Phi-3-mini-128k-instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct), aligned with DPO and QLora.

- It's trained on [ultrafeedback-binarized-preferences-cleaned](https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences-cleaned).

# Evaluation

We evaluated the model using the same test sets as used for the [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) 

| hellaswag acc_norm | arc_challenge acc_norm | m_mmlu 5-shot acc | Average |
|:----------------------| :--------------- | :-------------------- | :------- |
| 0.7833 | 0.5486 | 0.6847 | 0.6722 |


## Usage

Be sure to install these dependencies before running the program

```python
!pip install transformers torch sentencepiece
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cpu" # if you want to use the gpu make sure to have cuda toolkit installed and change this to "cuda"

model = AutoModelForCausalLM.from_pretrained("MoxoffSpA/Moxoff-Phi3Mini-DPO")
tokenizer = AutoTokenizer.from_pretrained("MoxoffSpA/Moxoff-Phi3Mini-DPO")

question = """Quanto è alta la torre di Pisa?"""
context = """
La Torre di Pisa è un campanile del XII secolo, famoso per la sua inclinazione. Alta circa 56 metri.
"""

prompt = f"Domanda: {question}, contesto: {context}"

messages = [
    {"role": "user", "content": prompt}
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(
    model_inputs, # The input to the model
    max_new_tokens=128, # Limiting the maximum number of new tokens generated
    do_sample=True, # Enabling sampling to introduce randomness in the generation
    temperature=0.1, # Setting temperature to control the randomness, lower values make it more deterministic
    top_p=0.95, # Using nucleus sampling with top-p filtering for more coherent generation       
    eos_token_id=tokenizer.eos_token_id # Specifying the token that indicates the end of a sequence
)

decoded_output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
trimmed_output = decoded_output.strip()
print(trimmed_output)
```

## Bias, Risks and Limitations

Moxoff-Phi3Mini-DPO has not been aligned to human preferences for safety within the RLHF phase or deployed with in-the-loop filtering of 
responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). It is also unknown what the size and composition 
of the corpus was used to train the base model, however it is likely to have included a mix of Web data and technical sources 
like books and code.

## Links to resources

- ultrafeedback-binarized-preferences-cleaned dataset: https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences-cleaned
- Phi-3-mini-128k-instruct model: https://huggingface.co/microsoft/Phi-3-mini-128k-instruct
- Open LLM Leaderbord: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard

## The Moxoff Team

Jacopo Abate, Marco D'Ambra, Dario Domanin, Luigi Simeone, Gianpaolo Francesco Trotta