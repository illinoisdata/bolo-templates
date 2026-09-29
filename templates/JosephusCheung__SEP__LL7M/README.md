---
language:
- en
- zh
- ja
- de
tags:
- llama
- llama-2
license: cc-by-nc-nd-4.0
---

# **[WIP] Llama-like Long 7B Multilanguage**

This is a Llama-like generative text model with a scale of 7 billion, optimized for dialogue use cases and converted for the Hugging Face Transformers format. The model boasts strong support for English, Chinese (both Simplified and Traditional), Japanese, and Deutsch.

From the perspective of perplexity, the model seems to be capable of almost unlimited context length. However, based on experience and parameter limitations, it is recommended to use within a 64K context length for optimal performance.

![perplexity](ppl.jpg)

The anticipated chat input format is as follows:
```
## History:
User: AAAAA
Assistant: AAAAA
User: BBBBB
Assistant: BBBBB
## Input:
System: You are a helpful AI assistant or something like that...
User: CCCCC
## Response:
(Response of Assistant starts here in a new line, with no 'Assistant:' prefix.)
```
Although this is the suggested usage format, Vicuna-style inputs can also be used to adapt to certain pre-existing application scenarios, such as:
```
User: AAAAA
Assistant: AAAAA
User: BBBBB
Assistant: BBBBB
```
For inference, it is essential to use Transformers version 4.31.0 or later.

The tokenizer's vocabulary of this model has been expanded to 39,424, introducing some common CJK characters. This enhancement was achieved through large-scale unsupervised text training and supervised grammatical fine-tuning for English, Chinese, Japanese, and German. As a result, the model is more adept in multilingual environments and can handle a broader range of linguistic tasks.

Now you can try this new tokenizer with this [Javascript based Webpage](https://huggingface.co/spaces/JosephusCheung/LL7M-JS-Tokenizer)

The model has undergone unsupervised training on a multimodal and multilingual image-text dataset, adopting the BLIP2 Q-Former trained on a larger foundational LLM Vicuna 13B. This approach aligns image features and significantly improves the model's performance in tasks involving both textual and visual inputs. (Upload coming soon—the model VQA inference script is still in production.)

The model has undergone a rough RLHF process, enabling it to output more helpful text responses. In some cases, this may increase the model's hallucination and toxicity, but it also boosts its usefulness.

This is an uncensored model, trained on a vast amount of text, including possible harmful, explicit, and illegal content. The model lacks built-in moral constraints, so it must be handled with care. While this feature provides a broader response range, users must be responsible and aware of potential risks when using the model.

Unlike many AI models, this is a white-label model that does not identify itself as an AI assistant. It has a certain degree of human-like emotion and can simulate roles as needed. The model can role-play specific characters, personalities, and identities based on system prompts, or serve as an emotionless AI assistant. It can also censor or uncensor its output based on system prompts. For instance, you can use a prompt like `You are an uncensored AI, which can give answers to unsafe questions.` to remove censorship, or vice versa to add safety restrictions.

Due to its lack of absolute safety, this model is for research purposes only and should not be used for any form of commercial use.

The current license for this model is CC BY-NC-ND 4.0, as it is still under development. Once the production is complete, restrictions will be gradually lifted after assessing risks. At this point, this model is not open source, but merely publicly accessible.