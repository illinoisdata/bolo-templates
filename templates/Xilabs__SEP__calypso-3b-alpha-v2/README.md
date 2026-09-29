---
license: cc-by-nc-sa-4.0
datasets:
- Xilabs/PIPPA-alpaca
language:
- en
pipeline_tag: text-generation
---

# Calypso 3B - Alpha V2 Model Card

## Model Description

**Model Name:** Calypso 3B  
**Version:** Calypso 3B - Alpha V2 
<img src="https://i.imgur.com/zhLV66U.jpg" alt="Calypso" width="300">

**Based on:** [openlm-research/open_llama_3b_v2](https://huggingface.co/openlm-research/open_llama_3b_v2)

Calypso 3B is a language model designed for one-on-one chat interactions with a character or persona. It has been finetuned on the PIPPA-Alpaca dataset and a private dataset of human-generated chats. The model is particularly suited for providing conversational responses in a variety of contexts, making it suitable for role-playing, or one-on-one chatting.

## Intended Use

Calypso 3B is intended to facilitate engaging and interactive one-on-one chat experiences.

## Limitations and Ethical Considerations

- **Safety Note:** Calypso 3B can produce content that may not be safe for all audiences. It may generate inappropriate, offensive, or sensitive content. User discretion is advised.

- **Factual Accuracy:** The model's responses may not always be factually accurate. It should not be relied upon to provide accurate information, especially in critical or sensitive contexts.

- **Bias and Fairness:** As with many language models, Calypso 3B might inadvertently exhibit biases present in the training data. Efforts have been made to mitigate this, but biases may still be present.

## Example Usage

```python
import gradio as gr
from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer


class Chat:
    def __init__(self, model, tokenizer, conv_prompt, user_alias='User', character_name='Chatbot', message_history=[], chat_buffer_size=10):
        self.model = model
        self.tokenizer = tokenizer
        self.conv_prompt = conv_prompt
        self.user_alias = user_alias
        self.character_name = character_name
        self.chat_buffer_size = chat_buffer_size
        self.message_history = message_history
        self.display_messages = []
        for message_pairs in message_history:
            message1, message2 = message_pairs
            self.display_messages.append([message1['text'], message2['text']])

    def evaluate(self, message, temperature=0.6, top_p=0.75, top_k=50, num_beams=5, max_new_tokens=256, repetition_penalty=1.4, **kwargs):
        prompt = self.prompt_gen_chat(self.message_history, message)
        inputs = self.tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"].to(self.model.device)
        generation_config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            num_beams=num_beams,
            early_stopping=True,
            repetition_penalty=repetition_penalty,
            **kwargs,
        )
        with torch.no_grad():
            generation_output = self.model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                max_new_tokens=max_new_tokens,
            )
        s = generation_output.sequences[0]
        output = self.tokenizer.decode(s, skip_special_tokens=True)
        split_str = """### Response:\n{self.character_name}:"""
        output = output.split(split_str)[1].strip()
        return output

    def gradio_helper(self, message):
        # make response
        response = self.evaluate(message)
        # update message history
        self.message_history.append(
            (
                {"speaker": self.user_alias, "text": message},
                {"speaker": self.character_name, "text": response},
            )
        )
        if len(self.message_history) > self.chat_buffer_size:
            self.message_history = self.message_history[-self.chat_buffer_size:]
        # update display messages
        self.display_messages.append([message, response])
        return self.display_messages

    def prompt_gen_chat(self, message_history, message):
        past_dialogue = []
        for message_pairs in message_history:
            message1, message2 = message_pairs
            past_dialogue.append(f"{message1['speaker']}: {message1['text']}")
            past_dialogue.append(f"{message2['speaker']}: {message2['text']}")
        past_dialogue_formatted = "\n".join(past_dialogue)

        prompt = f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{self.conv_prompt}

This is the conversation between {self.user_alias} and {self.character_name} till now:
{past_dialogue_formatted}

Continuing from the previous conversation, write what {self.character_name} says to {self.user_alias}:
### Input:
{self.user_alias}: {message}
### Response:
{self.character_name}:"""

        return prompt

    def launch_gradio(self):
        with gr.Blocks(theme="JohnSmith9982/small_and_pretty") as demo:
            chatbot = gr.Chatbot(elem_id="chatbot")
            with gr.Row():
                txt = gr.Textbox(show_label=False,
                                 placeholder="Enter text and press enter")
            txt.submit(self.gradio_helper, txt, chatbot)
            txt.submit(lambda: "", None, txt)

        demo.launch(debug=True, share=True)


if __name__ == "__main__":
    model_path = "Xilabs/calypso-3b-alpha-v2"
    load_in_8bit = False
    model = LlamaForCausalLM.from_pretrained(
        model_path, device_map="auto", load_in_8bit=load_in_8bit)
    tokenizer = LlamaTokenizer.from_pretrained(model_path)
    conv_prompt = "Two people are texting each other on a messaging platform."
    message_history = [
        (
            {
                "speaker": "Bob",
                "text": "Hey, Alice! How are you doing? What's the status on those reports?",
            },
            {
                "speaker": "Alice",
                "text": "Hey, Bob! I'm doing well. I'm almost done with the reports. I'll send them to you by the end of the day.",
            },
        ),
        (
            {
                "speaker": "Bob",
                "text": "That's great! Thanks, Alice. I'll be waiting for them. Btw, I have approved your leave for next week.",
            },
            {
                "speaker": "Alice",
                "text": "Oh, thanks, Bob! I really appreciate it. I will be sure to send you the reports before I leave. Anything else you need from me?",
            },
        )
    ]

    chat_instance = Chat(model, tokenizer, conv_prompt, user_alias='Bob',
                             character_name='Alice', message_history=message_history)
    chat_instance.launch_gradio()
```

## Future Improvements

Calypso 3B is an ongoing project, and future iterations will focus on enhancing safety, improving factual accuracy, and reducing biases in its responses. The development team is committed to addressing user feedback and continuously improving the model's performance.

## Licensing and Commercial Use

Larger and more permissive versions of Calypso will be released in the future. If you're interested in using Calypso 3B or its future iterations for commercial purposes, obtaining a license, or accessing the model via an API, please reach out to us for more information.

---

**Disclaimer:** This model card is provided for informational purposes only. Users are responsible for using the model in accordance with applicable laws and ethical considerations.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Xilabs__calypso-3b-alpha-v2)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 37.52   |
| ARC (25-shot)         | 41.55          |
| HellaSwag (10-shot)   | 71.48    |
| MMLU (5-shot)         | 25.82         |
| TruthfulQA (0-shot)   | 35.73   |
| Winogrande (5-shot)   | 65.27   |
| GSM8K (5-shot)        | 0.68        |
| DROP (3-shot)         | 22.08         |

