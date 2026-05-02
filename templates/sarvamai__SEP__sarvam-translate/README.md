---
library_name: transformers
license: gpl-3.0
language:
- as
- bn
- brx
- doi
- gom
- gu
- en
- hi
- kn
- ks
- mai
- ml
- mni
- mr
- ne
- or
- pa
- sa
- sat
- sd
- ta
- te
- ur
base_model:
- google/gemma-3-4b-it
base_model_relation: finetune
pipeline_tag: translation
---

# Sarvam-Translate
<p align="center">
  <a href="https://dashboard.sarvam.ai/translate"
     target="_blank" rel="noopener noreferrer">
    <img
      src="https://img.shields.io/badge/🚀 Try on Sarvam&nbsp;Playground-1488CC?style=for-the-badge&logo=rocket"
      alt="Try on Sarvam Playground"
    />
  </a>
</p>
Sarvam-Translate is an advanced translation model built by Sarvam AI in partnership with AI4Bharat, specifically designed for comprehensive, document-level translation across the 22 official Indian languages, built on Gemma3-4B-IT. It addresses modern translation needs by moving beyond isolated sentences to handle long-context inputs, diverse content types, and various formats. Sarvam-Translate aims to provide high-quality, contextually aware translations for Indian languages, which have traditionally lagged behind high-resource languages in LLM performance.

Learn more about Sarvam-Translate in our detailed [blog post](https://www.sarvam.ai/blogs/sarvam-translate).

## Key Features
- **Comprehensive Indian Language Support**: Focus on the 22 official Indian languages, ensuring nuanced and accurate translations.
- **Advanced Document-Level Translation**: Translates entire documents, web pages, speeches, textbooks, and scientific articles, not just isolated sentences. Maximum context length: 8k tokens
- **Versatile Format Handling**: Processes a wide array of input formats, including markdown, digitized content (handling OCR errors), documents with embedded math and chemistry equations, and code files (translating only comments).
- **Context-Aware & Inclusive**: Engineered to respect different contexts, formats, styles (formal/informal), and ensure inclusivity (e.g., appropriate gender attribution).

## Supported languages list

`Assamese`, `Bengali`, `Bodo`, `Dogri`, `Gujarati`, `English`, `Hindi`, `Kannada`, `Kashmiri`, `Konkani`, `Maithili`, `Malayalam`, `Manipuri`, `Marathi`, `Nepali`, `Odia`, `Punjabi`, `Sanskrit`, `Santali`, `Sindhi`, `Tamil`, `Telugu`, `Urdu`

## Quickstart
The following code snippet demonstrates how to use Sarvam-Translate using Transformers.
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "sarvamai/sarvam-translate"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to('cuda:0')

# Translation task
tgt_lang = "Hindi"
input_txt = "Be the change you wish to see in the world."

# Chat-style message prompt
messages = [
    {"role": "system", "content": f"Translate the text below to {tgt_lang}."},
    {"role": "user", "content": input_txt}
]

# Apply chat template to structure the conversation
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

# Tokenize and move input to model device
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Generate the output
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=1024,
    do_sample=True,
    temperature=0.01,
    num_return_sequences=1
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()
output_text = tokenizer.decode(output_ids, skip_special_tokens=True)

print("Input:", input_txt)
print("Translation:", output_text)

```

## vLLM Deployment


### Server:
```bash
vllm serve sarvamai/sarvam-translate --port 8000 --dtype bfloat16 --max-model-len 8192
```

### Client:
```python
from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id


tgt_lang = 'Hindi'
input_txt = 'Be the change you wish to see in the world.'
messages = [{"role": "system", "content": f"Translate the text below to {tgt_lang}."}, {"role": "user", "content": input_txt}]


response = client.chat.completions.create(model=model, messages=messages, temperature=0.01)
output_text = response.choices[0].message.content

print("Input:", input_txt)
print("Translation:", output_text)
```

## With Sarvam APIs

Refer our [python client documentation](https://pypi.org/project/sarvamai/).

Sample code:

```python
from sarvamai import SarvamAI
client = SarvamAI()
response = client.text.translate(
    input="Be the change you wish to see in the world.",
    source_language_code="en-IN",
    target_language_code="hi-IN",
    speaker_gender="Male",
    model="sarvam-translate:v1",
)
```