---
language:
- ja
- en
license: mit
---

# Sarashina2.2-0.5B

This repository provides large language models trained by [SB Intuitions](https://www.sbintuitions.co.jp/).

## How to use

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, set_seed
 
model = AutoModelForCausalLM.from_pretrained("sbintuitions/sarashina2.2-0.5b", torch_dtype=torch.bfloat16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("sbintuitions/sarashina2.2-0.5b")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
set_seed(123)
 
text = generator(
    "おはようございます、今日の天気は",
    max_length=30,
    do_sample=True,
    pad_token_id=tokenizer.pad_token_id,
    num_return_sequences=3,
)

for t in text:
    print(t)


```

## Model Description

We constructed the Sarashina2.2-0.5B model, which consists of about 0.5 billion parameters (excluding embeddings and the LM head when calculating the number of parameters), using a three-phase training process.
First, we trained the model on 10 trillion tokens, including Japanese, English, and code data extracted from web corpora.
Next, we trained the model using synthetic data to improve its performance on math and coding tasks.
Finally, we trained the model with a small amount of data to enhance its performance on various application tasks.

The following tables show the model's performance on Japanese tasks.
For reference, we also present the performance of our previous LLMs.
As shown in the table, our Sarashina2.2-3B outperforms Sarashina2-7B in Japanese QA tasks such as NIILC and JMMLU.
In addition, Sarashina2.2-3B outperforms Sarashina2-70B in Japanese math and coding tasks such as MGSM-ja and JHumanEval.

#### Evaluation in Japanese tasks

| Model                                                                          | NIILC      | JMMLU     | MGSM-ja    | JHumanEval  |
|--------------------------------------------------------------------------------|------------|-----------|------------|-------------|
| [Sarashina2-7B](https://huggingface.co/sbintuitions/sarashina2-7b)             | 61.4       | 42.5      | 8.4        | 12.8        |
| [Sarashina2-70B](https://huggingface.co/sbintuitions/sarashina2-70b)           | **65.4**   | **62.7**  | 54.0       | 22.0        |
| **[Sarashina2.2-0.5B](https://huggingface.co/sbintuitions/sarashina2.2-0.5b)** | 33.9       | 28.8      | 21.6       | 15.2        |
| **[Sarashina2.2-1B](https://huggingface.co/sbintuitions/sarashina2.2-1b)**     | 47.2       | 38.2      | 39.6       | 20.7        |
| **[Sarashina2.2-3B](https://huggingface.co/sbintuitions/sarashina2.2-3b)**     | 63.0       | 52.7      | **63.6**   | **39.0**    |


## Ethical Considerations and Limitations
This repository contains the pre-trained model, which has not yet been tuned to follow instructions.
Therefore, this model may generate meaningless sequences, inaccurate instances, or biased/objectionable outputs.
As post-trained Sarashina2.2 models, we have published [Sarashina2.2-0.5B-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1), [Sarashina2.2-1B-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1), and [Sarashina2.2-3B-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1).

## License
[MIT License](https://huggingface.co/sbintuitions/sarashina2.2-0.5b/blob/main/LICENSE)