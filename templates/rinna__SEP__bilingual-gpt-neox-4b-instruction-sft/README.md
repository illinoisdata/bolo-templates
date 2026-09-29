---
thumbnail: https://github.com/rinnakk/japanese-pretrained-models/blob/master/rinna.png
license: mit
datasets:
- Anthropic/hh-rlhf
language:
- ja
- en
inference: false
base_model: rinna/bilingual-gpt-neox-4b
---

# bilingual-gpt-neox-4b-instruction-sft

![rinna-icon](./rinna.png)

---
# Update

- **2023/08/02** We uploaded the newly trained `rinna/bilingual-gpt-neox-4b-instruction-sft` with the MIT license.
  - Please refrain from using the previous model released on 2023/07/31 for commercial purposes if you have already downloaded it.
  - The new model released on 2023/08/02 is built from datasets with less strict licenses and has better evaluation performance, so we suggest using the new model.
  - For reference, we provide the MD5 checksum values for the `pytorch_model.bin` files of the previous and current models.
    -  2023/07/31 model: `edf190a323c0ae63f71476700fb0b462`
    -  2023/08/02 model: `de72aa5b66beee7b65783c96f687d186`
- **2023/07/31** In the previously released `rinna/bilingual-gpt-neox-4b-instruction-sft`, we found that part of the training data (i.e. Openchat ShareGPT4 and WizardLM) have a non-commercial license, and thus it does not comply with **the MIT license**. We decided to remove the previous version and build a new SFT model from datasets with less strict licenses. The new model will be uploaded in a few days. We sincerely apologize for our careless mistake.

---

# Overview
This repository provides an English-Japanese bilingual GPT-NeoX model of 3.8 billion parameters.

The model is based on [`rinna/bilingual-gpt-neox-4b`](https://huggingface.co/rinna/bilingual-gpt-neox-4b) and has been finetuned to serve as an instruction-following conversational agent.

* **Model architecture**

    A 36-layer, 2816-hidden-size transformer-based language model.

* **Fine-tuning**
    
    The fine-tuning data is the subset of the following datasets.
    * [Anthropic HH RLHF data](https://huggingface.co/datasets/Anthropic/hh-rlhf) and its Japanese translation
    * [FLAN Instruction Tuning data](https://github.com/google-research/FLAN) and its Japanese translation

* **Model Series**

    | Variant | Link |
    | :-- | :--|
    | Bilingual 4B MiniGPT4 | https://huggingface.co/rinna/bilingual-gpt-neox-4b-minigpt4 |
    | Bilingual 4B PPO | https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo |
    | Bilingual 4B SFT | https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft |
    | Bilingual 4B 8K | https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k |
    | Bilingual 4B | https://huggingface.co/rinna/bilingual-gpt-neox-4b |
    | Japanese 3.6B PPO | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo |
    | Japanese 3.6B SFT-v2 | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2 |
    | Japanese 3.6B SFT | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft |
    | Japanese 3.6B | https://huggingface.co/rinna/japanese-gpt-neox-3.6b |

* **Contributors**
    
    [Tianyu Zhao](https://huggingface.co/tianyuz) and [Kei Sawada](https://huggingface.co/keisawada)

* **Release date**

    August 2, 2023

---

# Benchmarking

  Our evaluation experiments suggest that the bilingual-gpt-neox-4b-instruction-sft model performs slightly better than the previous [Japanese GPT-NeoX 3.6B PPO](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) in Japanese tasks. 

  - *The 4-task average accuracy is based on results of JCommonsenseQA, JNLI, MARC-ja, and JSQuAD.*
  - *The 6-task average accuracy is based on results of JCommonsenseQA, JNLI, MARC-ja, JSQuAD, XWinograd, and JAQKET-v2.*
   
  | Model | 4-task average accuracy | 6-task average accuracy |
  | :-- | :-- | :-- |
  | bilingual-gpt-neox-4b-instruction-ppo | 61.01 | 61.16 |
  | **bilingual-gpt-neox-4b-instruction-sft** | **61.02** | **61.69** |
  | bilingual-gpt-neox-4b | 56.12 | 51.83 |
  | japanese-gpt-neox-3.6b-instruction-ppo | 59.86 | 60.07 |
  | japanese-gpt-neox-3.6b | 55.07 | 50.32 |
  
---

# I/O Format
A special format has been adopted to construct inputs.
* An input prompt is formatted as a conversation between `ユーザー` and `システム`.
* Each input utterance consists of (1) its speaker (`"ユーザー"` or `"システム"`), (2) a colon (`":"`), (3) a whitespace (`" "`), and (4) utterance text (e.g. `"世界で一番高い山は？"`).
* The input prompt should be ended with `"システム: "` to acknowledge the model to generate a response.
* All the utterances in the input prompt should be separated by a newline `\n`.

Following is an example to construct input from a conversation.
~~~python
prompt = [
    {
        "speaker": "ユーザー",
        "text": "Hello, you are an assistant that helps me learn Japanese."
    },
    {
        "speaker": "システム",
        "text": "Sure, what can I do for you?"
    },
    {
        "speaker": "ユーザー",
        "text": "VRはなんですか。"
    }
]
prompt = [
    f"{uttr['speaker']}: {uttr['text']}"
    for uttr in prompt
]
prompt = "\n".join(prompt)
prompt = (
    prompt
    + "\n"
    + "システム: "
)
print(prompt)
"""
ユーザー: Hello, you are an assistant that helps me learn Japanese.
システム: Sure, what can I do for you?
ユーザー: VRはなんですか。
システム:
"""
~~~

---

# How to use the model

**Notice:** Since the model is **sensitive to decoding hyper-parameters** (e.g. `temperature`, `top_p`, `top_k`, `repetition_penalty`), it is suggested to explore the best setting for your task.

~~~~python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/bilingual-gpt-neox-4b-instruction-sft", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("rinna/bilingual-gpt-neox-4b-instruction-sft")

if torch.cuda.is_available():
    model = model.to("cuda")

token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=512,
        do_sample=True,
        temperature=1.0,
        top_p=0.85,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

output = tokenizer.decode(output_ids.tolist()[0][token_ids.size(1):])
print(output)
"""VRとはVirtual Realityの略で、仮想現実とも呼ばれます。これは、コンピューターを使用して仮想世界を作り出し、仮想世界上でコンピューターのゲームや仮想世界を体験するための技術です。この技術は、コンピューターやモバイ ルデバイスの進歩によって、2015年以降、ますます普及しています。VRは、ゲームや仮想世界、その他のアプリケー ションなどのさまざまな分野で、コンピューターと人間の相互作用の新しい方法を提供しています。</s>"""
~~~~

---

# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer.
* The tokenizer has a vocabulary size of 65,536.
* It uses *byte fallback* to decompose unknown text pieces into UTF-8 byte pieces to avoid producing `<UNK>` tokens.
* It can recognize *consecutive whitespaces*, *newlines*, and *tabs* to handle structured texts better.
* We turned off the default behaviour of prepending leading whitespace because it is not beneficial for processing Japanese.
* Specifically, single whitespace is always processed as one token so that any English word won't have a preceding whitespace like in many other tokenizers (e.g. `_Hello`).
  * This decision trades the English processing efficiency for a unified way to treat whitespaces.
  * It leads to a significantly lower loss of next token prediction on English data because whitespaces are easy to predict.
* **Don't forget to set `use_fast=False` to make the above features function correctly.**

---

# How to cite
```bibtex
@misc{rinna-bilingual-gpt-neox-4b-instruction-sft,
    title = {rinna/bilingual-gpt-neox-4b-instruction-sft},
    author = {Zhao, Tianyu and Sawada, Kei},
    url = {https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft}
}

@inproceedings{sawada2024release,
    title = {Release of Pre-Trained Models for the {J}apanese Language},
    author = {Sawada, Kei and Zhao, Tianyu and Shing, Makoto and Mitsui, Kentaro and Kaga, Akio and Hono, Yukiya and Wakatsuki, Toshiaki and Mitsuda, Koh},
    booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},
    month = {5},
    year = {2024},
    pages = {13898--13905},
    url = {https://aclanthology.org/2024.lrec-main.1213},
    note = {\url{https://arxiv.org/abs/2404.01657}}
}
```

---

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)