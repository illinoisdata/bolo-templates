---
license: apache-2.0
datasets:
- uonlp/CulturaX
language:
- tr
- en
pipeline_tag: text-generation
metrics:
- accuracy
- bleu
base_model: mistralai/Mistral-7B-Instruct-v0.1
---



# Commencis-LLM

<!-- Provide a quick summary of what the model is/does. -->
Commencis LLM is a generative model based on the Mistral 7B model. The base model adapts Mistral 7B to Turkish Banking specifically by training on a diverse dataset obtained through various methods, encompassing general Turkish and banking data.
## Model Description
<!-- Provide a longer summary of what this model is. -->

- **Developed by:** [Commencis](https://www.commencis.com)
- **Language(s):** Turkish
- **Finetuned from model:** [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
- **Blog Post**: [LLM Blog](https://www.commencis.com/thoughts/commencis-introduces-its-purpose-built-turkish-fluent-llm-for-banking-and-finance-industry-a-detailed-overview/)

## Training Details
Alignment phase consists of two stages: supervised fine-tuning (SFT) and Reward Modeling with Reinforcement learning from human feedback (RLHF).

The SFT phase was done on the a mixture of synthetic datasets generated from comprehensive banking dictionary data, synthetic datasets generated from banking-based domain and sub-domain headings, and derived from the CulturaX Turkish dataset by filtering. It was trained with three epochs. We used a learning rate 2e-5, lora rank 64 and maximum sequence length 1024 tokens.

### Usage

### Suggested Inference Parameters
- Temperature: 0.5
- Repetition penalty: 1.0
- Top-p: 0.9

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

class TextGenerationAssistant:
    def __init__(self, model_id:str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id, device_map='auto',load_in_8bit=True,load_in_4bit=False)
        self.pipe = pipeline("text-generation", 
                             model=self.model, 
                             tokenizer=self.tokenizer,
                             device_map="auto",
                             max_new_tokens=1024, 
                             return_full_text=True,
                             repetition_penalty=1.0
                            )

        self.sampling_params = dict(do_sample=True, temperature=0.5, top_k=50, top_p=0.9)
        self.system_prompt = "Sen yardımcı bir asistansın. Sana verilen talimat ve girdilere en uygun cevapları üreteceksin. \n\n\n"

    def format_prompt(self, user_input):
        return "[INST] " + self.system_prompt + user_input + " [/INST]"

    def generate_response(self, user_query):
        prompt = self.format_prompt(user_query)
        outputs = self.pipe(prompt, **self.sampling_params)
        return outputs[0]["generated_text"].split("[/INST]")[1].strip()


assistant = TextGenerationAssistant(model_id="Commencis/Commencis-LLM")

# Enter your query here.
user_query = "Faiz oranı yükseldiğinde kredi maliyetim nasıl etkilenir?"
response = assistant.generate_response(user_query)
print(response)

```

### Chat Template

```python
from transformers import AutoTokenizer
import transformers
import torch

model = "Commencis/Commencis-LLM"
messages = [{"role": "user", "content": "Faiz oranı yükseldiğinde kredi maliyetim nasıl etkilenir?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=1024, do_sample=True, temperature=0.5, top_k=50, top_p=0.9)
print (outputs[0]["generated_text"].split("[/INST]")[1].strip())
```

# Quantized Models:

GGUF: https://huggingface.co/Commencis/Commencis-LLM-GGUF

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

Like all LLMs, Commencis-LLM has certain limitations:
- Hallucination: Model may sometimes generate responses that contain plausible-sounding but factually incorrect or irrelevant information.
- Code Switching: The model might unintentionally switch between languages or dialects within a single response, affecting the coherence and understandability of the output.
- Repetition: The Model may produce repetitive phrases or sentences, leading to less engaging and informative responses.
- Coding and Math: The model's performance in generating accurate code or solving complex mathematical problems may be limited.
- Toxicity: The model could inadvertently generate responses containing inappropriate or harmful content.