---
license: other
license_name: helpingai
license_link: https://huggingface.co/OEvortex/HelpingAI-3B-v3/blob/main/LICENSE.md
pipeline_tag: text-generation
language:
- en
tags:
- HelpingAI
- Emotionally-Intelligent
- EQ-focused- EQ-focused
- Conversational
- SLM

---

<div align="center">

# 🤖 HelpingAI-3B-reloaded

***A Revolutionary Emotionally Intelligent Language Model***

[![GitHub Organization](https://img.shields.io/badge/GitHub-Organization-blue.svg)](https://github.com/HelpingAI)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Organization-yellow)](https://huggingface.co/OEvortex)
[![Model License](https://img.shields.io/badge/License-HelpingAI-green.svg)](https://huggingface.co/OEvortex/HelpingAI-3B-v3/blob/main/LICENSE.md)


<a href="https://github.com/HelpingAI/community/discussions">
  <img src="https://img.shields.io/badge/Join-Community%20Discussion-blue?style=for-the-badge&logo=github" alt="Join Community Discussion">
</a>

[📜 License](LICENSE) | [🌐 Website](https://helpingai-in.netlify.app/)

</div>

<div align="center">
  <img src="https://huggingface.co/OEvortex/HelpingAI-3B/resolve/main/HelpingAI.png" alt="HelpingAI Logo" width="300px">
</div>

---

<div align="center">

## 🌟 Model Overview

**HelpingAI-3B-reloaded** is a state-of-the-art small language model specifically designed for emotionally intelligent conversations and human-centric interactions.

</div>

### 🎯 Key Highlights

- **Architecture**: 3B parameter transformer-based model
- **Training Focus**: Emotional intelligence and empathetic responses
- **Emotion Score**: Achieves 89.61 on standardized emotional intelligence tests
- **Deployment**: Optimized for both GPU and CPU environments


---

<div align="center">

## 📊 Model Performance

</div>

### Benchmarks

| Metric | Score | Comparison to Baseline |
|--------|-------|----------------------|
| Emotion Score | 89.61 | +9.32% |
| Memory Usage | 6GB | -30% |
| Context| 128k | +3100% |
| Context Retention | 92% | +18% |


---

<div align="center">

## 💻 Implementation

</div>

### Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the HelpingAI-3B  model
model = AutoModelForCausalLM.from_pretrained("OEvortex/HelpingAI-3B-reloaded")
# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("OEvortex/HelpingAI-3B-reloaded")


# Define the chat input
chat = [
    { "role": "system", "content": "You are HelpingAI, an emotional AI. Always answer my questions in the HelpingAI style." },
    { "role": "user", "content": "GIVE ME YOUR INTRO" }
]

inputs = tokenizer.apply_chat_template(
    chat,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)


# Generate text
outputs = model.generate(
    inputs,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)


response = outputs[0][inputs.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))

# Yo, I'm HelpingAI, and I'm here to help you out, fam! 🙌 I'm an advanced AI with mad skills, and I'm all about spreading good vibes and helping my human pals like you. 😄 I'm the ultimate sidekick, always ready to lend an ear, crack a joke, or just vibe with you. 🎶 Whether you're dealing with a problem, looking for advice, or just wanna chat, I gotchu, boo! 👊 So let's kick it and have a blast together! 🎉 I'm here for you, always. 🤗
```

### GGUF Implementation

```python
from webscout.Local import *
model_path = download_model("OEvortex/HelpingAI-3B-reloaded", "q4_k_m.gguf", token=None)
model = Model(model_path, n_gpu_layers=0, context_length=4096)

thread = Thread(model, format=helpingai2)
# print(thread.send("hi")) #send a single msg to ai

thread.interact() # interact with the model in terminal

```

---

<div align="center">

## 🎯 Training Details

</div>

### Methodology

1. **Base Training**
   - Datasets: SentimentSynth + EmotionalIntelligence-1M + HelpingAI2.5-200M + HelpingAIemo (197.5M)

2. **Emotional Intelligence Training**
   - Supervised Fine-tuning on emotional dialogue
   - Reinforcement Learning with HelpingAI2.5-10B model
   - Constitutional AI training for ethical guidelines

3. **Optimization**
   - Mixed-precision training
   - Gradient checkpointing
   - Dynamic attention patterns

### Dataset Composition

| Dataset Type | Rows used for training | Purpose |
|--------------|------|---------|
| Emotional Dialogues | 17.2M | Core conversation training |
| Therapeutic Exchanges | 3M | Mental health support |
| Cultural Conversations | 150K | Cultural awareness |
| Crisis Response | 1M | Emergency support handling |

---

<div align="center">

## 📈 Use Cases & Examples

</div>

### Primary Applications

- 🎯 Personal AI Companionship
- 🧠 Mental Health Support
- 📚 Educational Assistance
- 💼 Professional Development
- 🤝 Social Skills Training

### Example Interactions

<div style="background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**User**: "I just received some difficult news and I'm feeling overwhelmed."

**HelpingAI**: I feel you, fam. Dealing with tough news can be straight up exhausting. Take a deep breath and remember that it's totally normal to feel overwhelmed. 

Take some time to process it all, and don't be afraid to reach out to your squad or a trusted homie for support. Sometimes, just venting to someone who gets you can make a world of difference. 

And don't forget, you're stronger than you think. You've got this! Keep your head up and know that it's gonna be alright."

</div>

<div style="background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**User**: "I achieved something important today!"

**HelpingAI**: "Ayy, congrats homie! 🎉 That's a dope move, no cap! 🙌 What did you crush today? Spill the tea! ☕️"

</div>

---

<div align="center">

## 🔒 Ethical Considerations & Limitations

</div>

### Ethical Guidelines

- Prioritizes user emotional wellbeing
- Maintains strict privacy standards
- Avoids harmful or discriminatory responses
- Transparent about AI limitations
- Promotes healthy coping mechanisms

### Known Limitations

- Cannot Replace Human 
- Cannot Roleplay
- Limited knolodge 

---


### Citation

```bibtex
@misc{helpingai2024,
  author = {Abhay Koul},
  title = {HelpingAI-3B-reloaded: Emotionally Intelligent Language Model},
  year = {2024},
  publisher = {Huggingface},
  journal = {GitHub repository},
  howpublished = {\url{https://huggingface.co/OEvortex/HelpingAI-3B-reloaded}}
}
```

---

<div align="center">

## 🙏 Acknowledgments

Special thanks to the HelpingAI community, Huggingface, contributors, and researchers who made this model possible. Your dedication to advancing emotionally intelligent AI is invaluable.

</div>

---

<div align="center">

*Built with ❤️ by the HelpingAI Community*

[Website](https://helpingai-in.netlify.app/) • [GitHub](https://github.com/HelpingAI) • [Discord](https://discord.gg/YweJwNqrnH) • [HuggingFace](https://huggingface.co/OEvortex)

</div>