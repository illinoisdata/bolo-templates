---
library_name: transformers
tags: []
---

# Model Card for Model ID

This model is a 4-bit quantized version of Qwen2-Audio-7B-Instruct.
(https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct)

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed:** based on the original Qwen model by Alibaba Cloud
- **Model type:** Audio-Text Multimodal Large Language Model

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
The 4-bit quantization allows for reduced memory usage and potentially faster inference times, especially on hardware with limited resources. 
However, there might be a slight degradation in performance compared to the full-precision model. 

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
GPU is needed

## How to Get Started with the Model

Refer to the Qwen2-Audio-7B-Instruct model page on Hugging Face for usage examples and code snippets.

To use this model, you'll need to have the transformers library installed, along with bitsandbytes for 4-bit quantization support.

Here's a basic example of how to load and use the model:

```python
import torch
from io import BytesIO
from urllib.request import urlopen
import librosa
from transformers import Qwen2AudioForConditionalGeneration, AutoProcessor, BitsAndBytesConfig

processor = AutoProcessor.from_pretrained("alicekyting/Qwen2-Audio-7B-Instruct-4bit")
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)
model = Qwen2AudioForConditionalGeneration.from_pretrained(
    "alicekyting/Qwen2-Audio-7B-Instruct-4bit",
    device_map="auto",
    quantization_config=bnb_config
)

conversation = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {"role": "user", "content": [
        {"type": "audio", "audio_url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2-Audio/audio/glass-breaking-151256.mp3"},
        {"type": "text", "text": "What's that sound?"},
    ]},
    {"role": "assistant", "content": "It is the sound of glass shattering."},
    {"role": "user", "content": [
        {"type": "text", "text": "What can you do when you hear that?"},
    ]},
    {"role": "assistant", "content": "Stay alert and cautious, and check if anyone is hurt or if there is any damage to property."},
    {"role": "user", "content": [
        {"type": "audio", "audio_url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2-Audio/audio/1272-128104-0000.flac"},
        {"type": "text", "text": "What does the person say?"},
    ]},
]
text = processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=False)
audios = []
for message in conversation:
    if isinstance(message["content"], list):
        for ele in message["content"]:
            if ele["type"] == "audio":
                audios.append(
                    librosa.load(
                        BytesIO(urlopen(ele['audio_url']).read()),
                        sr=processor.feature_extractor.sampling_rate,
                        mono=True
                    )[0]
                )

inputs = processor(text=text, audios=audios, return_tensors="pt", padding=True)
inputs = {k: v.to(model.device) for k, v in inputs.items()}

generate_ids = model.generate(**inputs, max_length=256)
generate_ids = generate_ids[:, inputs['input_ids'].size(1):]

response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
print(response)