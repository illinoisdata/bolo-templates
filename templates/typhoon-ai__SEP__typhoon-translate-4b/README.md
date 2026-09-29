---
license: gemma
language:
- th
- en
---

**Typhoon translate**

**Typhoon translate** is a lightweight, 4-billion-parameter language model designed specifically for high-quality Thai ↔ English translation—right from your local device.

Unlike general-purpose models, Typhoon Translate is fine-tuned for translation tasks and works best with dedicated prompts. Its strength lies in generating natural, fluent translations while preserving meaning and tone in both directions.

**Release Blog available on [OpenTyphoon Blog](https://opentyphoon.ai/blog/en/typhoon-translate-release)**

Note: For optimal results, use the system prompts:
`Translate the following text into Thai.` or
`Translate the following text into English.`


## **Performance**

We used GPT-4o-mini as an "AI judge", comparing Typhoon Translate against its own generations and other top systems.

![EN -> TH performance](https://storage.googleapis.com/typhoon-blog-assets/images/EN-TH-translate-eval.png)

![TH -> EN performance](https://storage.googleapis.com/typhoon-blog-assets/images/TH-EN-translate-eval.png)

## **Model Description**

- **Model type**: A 4B instruct decoder-only model based on Gemma3 architecture.
- **Requirement**: transformers 4.51.1 or newer.
- **Primary Language(s)**: Thai 🇹🇭 and English 🇬🇧
- **License**: [Gemma License](https://github.com/google-deepmind/gemma/blob/main/LICENSE)


## Quickstart

This code snippet shows how to use the Typhoon translation model for Thai or English text generation using the transformers library with a specific prompt.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "scb10x/Typhoon-translate-4b"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# Translate English to Thai

messages = [
    {"role": "system", "content": "Translate the following text into Thai."},
    {"role": "user", "content": "A banished celestial, Serai, cursed to walk as a mortal boy, fights against the Empire that slaughtered the skyborn.\nHe trains with humans, bonds with them, bleeds beside them. In secret, he regrows his wings through combat—but each feather only returns when he loses someone he loves.\nAt the climax, he ascends—glorious, radiant, unstoppable—only to find his friends gone, their memories etched into his wings.\nAs he watches the sun rise, his halo returns.\nHe whispers, “Was it worth it?”\nAnd no one answers."},
]

# Translate Thai to English

# messages = [
#     {"role": "system", "content": "Translate the following text into English."},
#     {"role": "user", "content": "เมื่อสิ้นปี 2022 การเปิดตัว ChatGPT ของ OpenAI ถือเป็นจุดเปลี่ยนสำคัญ—โลกได้รู้จักกับ Generative AI (Gen AI) และทุกอย่างก็เปลี่ยนไป สิ่งที่เคยรู้สึกเหมือน frontier ไกลๆ กลายเป็นพลังในปัจจุบัน AI ถูกฝังตัวอย่างรวดเร็วทั้งในกิจวัตรส่วนตัวและกลยุทธ์องค์กร กลายเป็นตัวเปลี่ยนเกมอันทรงพลัง—ช่วยยกระดับชีวิต ปลดล็อกประสิทธิภาพใหม่ๆ และเปลี่ยนวิธีที่องค์กรดำเนินงาน ในการแสวงหาความได้เปรียบเชิงแข่งขัน ธุรกิจในหลากหลายภาคส่วนต่างเร่งทำความเข้าใจ นำไปใช้ และสร้างนวัตกรรมด้วย AI\nSCBX AI Outlook 2025: Beaconing the Future of Artificial Intelligence ถูกออกแบบมาเป็นประภาคารท่ามกลางคลื่นที่เร่งตัวขึ้นนี้—มอบความชัดเจนและทิศทางให้ผู้นำรับมือกับกระแสการเปลี่ยนแปลงทางเทคโนโลยี รายงานนี้สำรวจแนวโน้ม AI ที่กำลังกำหนดทิศทางในปีข้างหน้า และนำเสนอมุมมองเชิงกลยุทธ์ในการเปลี่ยนความไม่แน่นอนให้เป็นโอกาส รายงานแบ่งออกเป็นสี่ส่วน (Acts) แต่ละส่วนเน้นพลังสำคัญที่กำลังเปลี่ยนภูมิทัศน์ AI:\nACT I: Two Philosophies, One Future. The Battle Between Open-Source and Closed-Source AI Intensifies\nACT II: Tiny Titans - Small, but Mighty. More Versatile, Smaller, and Smarter: 3 Trends of the Next AI Evolution\nACT III: AI at Your Fingertips. Agentic AI: Rise of the Agents\nACT IV: Not Quite Human, But Almost There. Artificial General Intelligence (AGI) and the Unresolved Path to Human-Level AI\nรายงานปิดท้ายด้วย EPILOGUE: The AI Storm – Infinite Impact พร้อม Case Studies จากภายในดวงตาของพายุไต้ฝุ่น—นำเสนอกรณีศึกษาจริงจาก SCBX ในการใช้ AI Engine “Typhoon” ของกลุ่มในหน่วยธุรกิจต่างๆ ขณะที่กระแส AI กำลังก้าวไปข้างหน้า รายงานนี้จึงไม่ได้เป็นเพียงการคาดการณ์ แต่เป็นประภาคารเชิงกลยุทธ์สำหรับผู้พร้อมจะก้าวขึ้นไปกับคลื่นและเป็นผู้นำในอนาคต"},
# ]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=8192,
    temperature=0.2,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```

## Prompting

**For translate to Thai**
```
Translate the following text into Thai.
```

**For translate to English**
```
Translate the following text into English.
```

If your environment doesn't support system prompt, you can use system prompt in the user turn.

```python
{system_prompt}\n\n{text_to_translate}
```
example of 
```
Translate the following text into Thai.\n\nA banished celestial, Serai, cursed to walk as a mortal boy, fights against the Empire that slaughtered the skyborn.\nHe trains with humans, bonds with them, bleeds beside them. In secret, he regrows his wings through combat—but each feather only returns when he loses someone he loves.\nAt the climax, he ascends—glorious, radiant, unstoppable—only to find his friends gone, their memories etched into his wings.\nAs he watches the sun rise, his halo returns.\nHe whispers, “Was it worth it?”\nAnd no one answers.
```


## Deploy as Server

This section shows how to run Typhoon translate as an OpenAI-compatible API server using vllm.

- SGLang:
```base
python3 -m sglang.launch_server scb10x/typhoon-translate-4b --context-length 16000 --dtype bfloat16
```
- vLLM:
```bash
vllm serve scb10x/typhoon-translate-4b --max-model-len 16000 --dtype bfloat16
```

## Best Practices
To achieve optimal performance, we recommend the following settings:
- Use system prompt `Translate the following text into Thai.` for English to Thai translation and `Translate the following text into English.` for Thai to English translation.
- Set low temperature. 
- Using an context length less than 8192 tokens.

## Intended Uses & Limitations
This is a task-specific model intended to be used only with the provided prompts. It does not include any guardrails. Due to the nature of large language models (LLMs), a certain level of hallucination may occur. We recommend that developers carefully assess these risks in the context of their specific use case.


## **Follow us**

**https://twitter.com/opentyphoon**

## **Support**

**https://discord.gg/us5gAYmrxw**


## **Citation**

- If you find Typhoon2 useful for your work, please cite it using:
```
@misc{typhoon2,
      title={Typhoon 2: A Family of Open Text and Multimodal Thai Large Language Models}, 
      author={Kunat Pipatanakul and Potsawee Manakul and Natapong Nitarach and Warit Sirichotedumrong and Surapon Nonesung and Teetouch Jaknamon and Parinthapat Pengpun and Pittawat Taveekitworachai and Adisai Na-Thalang and Sittipong Sripaisarnmongkol and Krisanapong Jirayoot and Kasima Tharnpipitchai},
      year={2024},
      eprint={2412.13702},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.13702}, 
}
```