---
license: llama3.2
---


# Llama-3.2-3B-ARChitects-ReArc-bnb-4bit

## Model Overview

Llama-3.2-3B-ARChitects-ReArc-bnb-4bit is a retrained variant of [Llama-3.2-3B-Instruct-uncensored](https://huggingface.co/chuanli11/Llama-3.2-3B-Instruct-uncensored), finetuned specifically to solve [ARC-AGI](https://arcprize.org/) tasks. In order to save GPU memory, the embedding and vocabulary size have been reduced to only 77 tokens. The model achieved a score of 61.4% (with test-time retraining) on the ARC-AGI public evaluation set, with only the [ReArc](https://github.com/michaelhodel/re-arc) data set being used during finetuning. Please refer to our [github repository](https://da-fr.github.io/Product-of-Experts-ARC-Paper/) for more details. For more models tuned for ARC-AGI, check out our [model collection](https://huggingface.co/collections/da-fr/arc-agi-models-674f0d88c8b2fa1edecffadb).

## Finetuning Datasets

This model was finetuned on the following datasets:

* the [ReArc data set](https://github.com/michaelhodel/re-arc) by Michael Hodel

## License

This model is released under the Llama 3.2 Community License Agreement.

## Usage
This model can be used with the `transformers` or `unsloth` packages. For more information on preprocessing the ARC Prize tasks to generate prompts for the model, please refer to our [github repository](https://da-fr.github.io/Product-of-Experts-ARC-Paper).

## References
* ICML 2025 Paper "Product of Experts with LLMs: Boosting Performance on ARC is a Matter of Perspective" [[github]](https://da-fr.github.io/Product-of-Experts-ARC-Paper) [[arxiv]](https://arxiv.org/abs/2505.07859)
* Arc Prize 2024 Technical Report [[github]](https://github.com/da-fr/arc-prize-2024/) [[pdf]](https://github.com/da-fr/arc-prize-2024/blob/main/the_architects.pdf)