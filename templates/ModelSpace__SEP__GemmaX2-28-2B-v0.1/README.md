---
license: gemma
license_name: license
license_link: LICENSE
metrics:
- bleu
- comet
base_model:
- ModelSpace/GemmaX2-28-2B-Pretrain
pipeline_tag: translation
library_name: transformers
language:
- ar
- bn
- cs
- de
- en
- es
- fa
- fr
- he
- hi
- id
- it
- ja
- km
- ko
- lo
- ms
- my
- nl
- pl
- pt
- ru
- th
- tl
- tr
- ur
- vi
- zh
---

## Updates

New multilingual machine translation model (MiLMMT-46) is now available. Please check the [link](https://huggingface.co/collections/xiaomi-research/milmmt-46) for detailed information.


## Model Description

GemmaX2-28-2B-v0.1 is an LLM-based translation model. It has been fintuned on GemmaX2-28-2B-Pretrain, which is a language model developed through continual pretraining of Gemma2-2B using a mix of 56 billion tokens from both monolingual and parallel data across 28 different languages. Please find more details in our paper: [Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study](https://arxiv.org/pdf/2502.02481).


- **Developed by:** Xiaomi
- **Model type:** GemmaX2-28-2B-Pretrain is obtained by continually pretraining Gemma2-2B on a large amount of monolingual and parallel data. Subsequently, GemmaX2-28-2B-v0.1 is derived through supervised finetuning on a small set of high-quality translation instruction data.
- **Languages:** Arabic, Bengali, Czech, German, English, Spanish, Persian, French, Hebrew, Hindi, Indonesian, Italian, Japanese, Khmer, Korean, Lao, Malay, Burmese, Dutch, Polish, Portuguese, Russian, Thai, Tagalog, Turkish, Urdu, Vietnamese, Chinese.
- **Github:** Please find more details in our [Github repository](https://github.com/xiaomi-research/gemmax).

## Model Performance

![Experimental Result](main.png)


## Run the model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ModelSpace/GemmaX2-28-2B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id)

text = "Translate this from Chinese to English:\nChinese: 我爱机器翻译\nEnglish:"
inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```


## Citation 

```bibtex
@misc{cui2025multilingualmachinetranslationopen,
      title={Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study}, 
      author={Menglong Cui and Pengzhi Gao and Wei Liu and Jian Luan and Bin Wang},
      year={2025},
      eprint={2502.02481},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.02481}, 
}
```


## Limitations

GemmaX2-28-2B-v0.1 only supports the 28 languages listed above and does not guarantee strong translation performance for other languages. We will continue to enhance the translation performance of GemmaX2-28-2B, and future models will be released in due course.