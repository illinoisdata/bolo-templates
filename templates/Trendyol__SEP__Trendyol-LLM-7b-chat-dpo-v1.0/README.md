---
language:
- tr
- en
pipeline_tag: text-generation
license: apache-2.0
base_model: Trendyol/Trendyol-LLM-7b-chat-v1.0
---
<img src="https://huggingface.co/Trendyol/Trendyol-LLM-7b-chat-dpo-v1.0/resolve/main/trendyol-llm-mistral.jpg"
alt="drawing" width="400"/>
# **Trendyol LLM v1.0 - DPO**
Trendyol LLM v1.0 - DPO is a generative model that is based on Mistral 7B model. DPO training was applied. This is the repository for the chat model.

## Model Details

**Model Developers** Trendyol

**Variations** [base](https://huggingface.co/Trendyol/Trendyol-LLM-7b-base-v1.0), [chat](https://huggingface.co/Trendyol/Trendyol-LLM-7b-chat-v1.0), and dpo variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** Trendyol LLM is an auto-regressive language model (based on Mistral 7b) that uses an optimized transformer architecture. Huggingface TRL lib was used for training. The DPO version is fine-tuned on 11K sets (prompt-chosen-reject) with the following trainables by using LoRA:

- **lr**=5e-6
- **lora_rank**=64
- **lora_alpha**=128
- **lora_trainable**=q_proj,v_proj,k_proj,o_proj,gate_proj,down_proj,up_proj
- **lora_dropout**=0.05
- **bf16**=True
- **beta**=0.01
- **max_length**= 1024
- **max_prompt_length**= 512
- **lr_scheduler_type**= cosine
- **torch_dtype**= bfloat16

<img src="https://camo.githubusercontent.com/3e61ca080778f62988b459c7321726fa35bb3776ceb07ecaabf71ebca44f95a7/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f74726c2d696e7465726e616c2d74657374696e672f6578616d706c652d696d616765732f7265736f6c76652f6d61696e2f696d616765732f74726c5f62616e6e65725f6461726b2e706e67"
alt="drawing" width="600"/>
<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft/lora_diagram.png"
alt="drawing" width="600"/>

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "Trendyol/Trendyol-LLM-7b-chat-dpo-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, 
                                             device_map='auto', 
                                             load_in_8bit=True)

sampling_params = dict(do_sample=True, temperature=0.3, top_k=50, top_p=0.9)

pipe = pipeline("text-generation", 
                model=model, 
                tokenizer=tokenizer,
                device_map="auto",
                max_new_tokens=1024, 
                return_full_text=True,
                repetition_penalty=1.1
               )

DEFAULT_SYSTEM_PROMPT = "Sen yardımcı bir asistansın ve sana verilen talimatlar doğrultusunda en iyi cevabı üretmeye çalışacaksın.\n"

TEMPLATE = (
    "[INST] {system_prompt}\n\n"
    "{instruction} [/INST]"
)

def generate_prompt(instruction, system_prompt=DEFAULT_SYSTEM_PROMPT):
    return TEMPLATE.format_map({'instruction': instruction,'system_prompt': system_prompt})

def generate_output(user_query, sys_prompt=DEFAULT_SYSTEM_PROMPT):
    prompt = generate_prompt(user_query, sys_prompt)
    outputs = pipe(prompt,
               **sampling_params
              )
    return outputs[0]["generated_text"].split("[/INST]")[-1]

user_query = "Türkiye'de kaç il var?"
response = generate_output(user_query)
print(response)
```

with chat template:
```python
pipe = pipeline("conversational", 
                model=model, 
                tokenizer=tokenizer,
                device_map="auto",
                max_new_tokens=1024,
                repetition_penalty=1.1
               )

messages = [
    {"role": "user", "content": "Türkiye'de kaç il var?"}
]

outputs = pipe(messages, **sampling_params)
print(outputs)
```

## Limitations, Risks, Bias, and Ethical Considerations

### Limitations and Known Biases

- **Primary Function and Application:** Trendyol LLM, an autoregressive language model, is primarily designed to predict the next token in a text string. While often used for various applications, it is important to note that it has not undergone extensive real-world application testing. Its effectiveness and reliability across diverse scenarios remain largely unverified.

- **Language Comprehension and Generation:** The model is primarily trained in standard English and Turkish. Its performance in understanding and generating slang, informal language, or other languages may be limited, leading to potential errors or misinterpretations.

- **Generation of False Information:** Users should be aware that Trendyol LLM may produce inaccurate or misleading information. Outputs should be considered as starting points or suggestions rather than definitive answers.

### Risks and Ethical Considerations

- **Potential for Harmful Use:** There is a risk that Trendyol LLM could be used to generate offensive or harmful language. We strongly discourage its use for any such purposes and emphasize the need for application-specific safety and fairness evaluations before deployment.

- **Unintended Content and Bias:** The model was trained on a large corpus of text data, which was not explicitly checked for offensive content or existing biases. Consequently, it may inadvertently produce content that reflects these biases or inaccuracies.

- **Toxicity:** Despite efforts to select appropriate training data, the model is capable of generating harmful content, especially when prompted explicitly. We encourage the open-source community to engage in developing strategies to minimize such risks.

### Recommendations for Safe and Ethical Usage

- **Human Oversight:** We recommend incorporating a human curation layer or using filters to manage and improve the quality of outputs, especially in public-facing applications. This approach can help mitigate the risk of generating objectionable content unexpectedly.

- **Application-Specific Testing:** Developers intending to use Trendyol LLM should conduct thorough safety testing and optimization tailored to their specific applications. This is crucial, as the model’s responses can be unpredictable and may occasionally be biased, inaccurate, or offensive.

- **Responsible Development and Deployment:** It is the responsibility of developers and users of Trendyol LLM to ensure its ethical and safe application. We urge users to be mindful of the model's limitations and to employ appropriate safeguards to prevent misuse or harmful consequences.