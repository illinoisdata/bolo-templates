---
base_model:
- aisingapore/SEA-LION-v1-7B
new_version: aisingapore/Qwen-SEA-LION-v4.5-27B-IT
license: mit
language:
- en
- zh
- id
- ms
- tl
- my
- vi
- th
- lo
- km
- ta
---
# SEA-LION-v1-7B-IT

SEA-LION is a collection of Large Language Models (LLMs) which has been pretrained and instruct-tuned for the Southeast Asia (SEA) region.
The sizes of the models range from 3 billion to 7 billion parameters.

SEA-LION-v1-7B-IT is a multilingual model which has been fine-tuned with **thousands of English and Indonesian instruction-completion pairs** alongside a smaller pool of instruction-completion pairs from other ASEAN languages. 
These instructions have been carefully curated and rewritten to ensure the model was trained on truly open, commercially permissive and high quality datasets.

SEA-LION stands for _Southeast Asian Languages In One Network_.

- **Developed by:** Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Model type:** Decoder
- **Languages:** English, Chinese, Indonesian, Malay, Thai, Vietnamese, Filipino, Tamil, Burmese, Khmer, Lao
- **License:** MIT License

## Model Details
### Base model 
We performed instruction tuning in English and Indonesian on our [pre-trained SEA-LION-v1-7B](https://huggingface.co/aisingapore/SEA-LION-v1-7B), a decoder model using the MPT architecture, to create SEA-LION-v1-7B-IT.

### Benchmark Performance
We evaluated SEA-LION-v1-7B-IT on the BHASA benchmark ([arXiv](https://arxiv.org/abs/2309.06085v2) and [GitHub](https://github.com/aisingapore/bhasa)) across a variety of tasks. 

BHASA stands out amongst other evaluations for SEA languages for its holistic approach to evaluation, including not just traditional Natural Language Processing (NLP) benchmarking tasks (such as sentiment analysis and question answering), but also linguistic and cultural diagnostic tests which are meticulously handcrafted. 

The evaluation was done zero-shot with Indonesian prompts and only a sample of 100-1000 instances for each dataset was used as per the setting described in the BHASA paper. The scores shown in the table below have been adjusted to only consider answers provided in the appropriate language.

| Model                          | QA (F1) | Sentiment (F1) | Toxicity (F1) | Eng>Indo (ChrF++) | Indo>Eng (ChrF++) | Summary (ROUGE-L) | NLI (Acc) | Causal (Acc) |
|--------------------------------|---------|----------------|---------------|-------------------|-------------------|-------------------|-----------|--------------|
| SEA-LION-v1-7B-IT-Research  | 24.86   | 76.13          | 24.45         | 52.50             | 46.82             | 15.44             | 33.20     | 23.80        |
| SEA-LION-v1-7B-IT           | **68.41**| **91.45**     | 17.98         | 57.48             | 58.04             | **17.54**         | 53.10     | 60.80        |
| SeaLLM 7B v1                   | 30.96   | 56.29          | 22.60         | 62.23             | 41.55             | 14.03             | 26.50     | 56.60        |
| SeaLLM 7B v2                   | 44.40   | 80.13          | **55.24**     | 64.01             | **63.28**         | 17.31             | 43.60     | 82.00        |
| Sailor-7B (Base)               | 65.43   | 59.48          | 20.48         | **64.27**         | 60.68             | 8.69              | 15.10     | 38.40        |
| Sailor-7B-Chat                 | 38.02   | 87.64          | 52.07         | 64.25             | 61.87             | 15.28             | **68.30** |**85.60**     |
| Llama 2 7B Chat                | 11.12   | 52.32          | 0.00          | 44.09             | 57.58             | 9.24              | 0.00      | 0.00         |
| Mistral 7B Instruct v0.1       | 38.85   | 74.38          | 20.83         | 30.60             | 51.43             | 15.63             | 28.60     | 50.80        |
| GPT-4 (gpt-4-0314)             | 73.60   | 74.14          | 63.96         | 69.38             | 67.53             | 18.71             | 83.20     | 96.00        |

- For Natural Language Understanding (NLU) tasks, we tested the model on Sentiment Analysis (`Sentiment`) using the NusaX dataset, Question Answering (`QA`) using the TyDiQA dataset, and Toxicity Detection (`Toxicity`) using the Indonesian Multi-Label Hate Speech Detection dataset. The metrics used are F1 scores for all three tasks.
- For Natural Language Generation (NLG) tasks, we tested the model on Machine Translation from English to Indonesian (`Eng>Indo`) and from Indonesian to English (`Indo>Eng`) using the FLORES-200 dataset, and Abstractive Summarization (`Summary`) using the XLSum dataset. The metrics used for Machine Translation and Abstractive Summarization are ChrF++ and ROUGE-L respectively.
- For Natural Language Reasoning (NLR) tasks, we tested the model on Natural Language Inference (`NLI`) using the IndoNLI lay dataset and on Causal Reasoning (`Causal`) using the XCOPA dataset. The metrics are based on accuracy for both tasks.

### Usage
SEA-LION-v1-7B-IT can be run using the 🤗 Transformers library 
```python
# Please use transformers==4.37.2

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("aisingapore/SEA-LION-v1-7B-IT", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("aisingapore/SEA-LION-v1-7B-IT", trust_remote_code=True)

prompt_template = "### USER:\n{human_prompt}\n\n### RESPONSE:\n"
prompt = """Apa sentimen dari kalimat berikut ini?
Kalimat: Buku ini sangat membosankan.
Jawaban: """
full_prompt = prompt_template.format(human_prompt=prompt)

tokens = tokenizer(full_prompt, return_tensors="pt")
output = model.generate(tokens["input_ids"], max_new_tokens=20, eos_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(output[0], skip_special_tokens=True))

```
### Prompting Guide

_Coming soon_

### Caveats
It is important for users to be aware that our model exhibits certain limitations that warrant consideration. Firstly, like many LLMs, the model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies in its reasoning. Finally, it should be noted that the model has not been optimized for multi-turn dialogue interactions, which may result in reduced effectiveness in extended conversations.

## Limitations
### Safety

Current SEA-LION models, including this commercially permissive release, have not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claim, damages, or other liability arising from the use of the released weights and codes.

### Commercially Non-Permissive and Commercially Permissive SEA-LION Releases

The previous release of the commercially non-permissive SEA-LION-v1-7B-IT-Research enabled us to explore the full research potential of SEA-LION when allowed to take full advantage of what is publicly available. In contrast, in building the commercially permissive SEA-LION-v1-7B-IT, we had to leave out high-quality instruction data that was either proprietary, restricted by non-commercial licenses or in a legal gray area, leaving us with a much smaller proportion of commercially permissive data to work with — a problem that is even more pronounced for low-resource languages. We thus hope this will sound a call to action for more initiatives to create commercially viable data in the region, enabling practical benefits for all.


## Technical Specifications
### Fine-Tuning Details
The SEA-LION-v1-7B-IT was fine-tuned using 8x A100-40GB using parameter efficient fine tuning in the form of LoRA.

## Data
SEA-LION-v1-7B-IT was trained on a wide range of instructions that were manually and stringently verified by our team. A large portion of the effort was dedicated to ensuring that each instruction-completion pair that the model sees is of a high quality and any errors were corrected and rewritten by native speakers or else dropped from our mix.

In addition, special care was taken to ensure that the datasets used had commercially permissive licenses through verification with the original data source. 

### Lineage & Versioning

The training counts and dataset mixture details reported in this model card reflect the exact constructed training pool consumed during this specific model run. Figures may differ slightly from public dataset releases, which represent downloadable open-source subsets of the broader corpus.


## Call for Contributions
We encourage researchers, developers, and language enthusiasts to actively contribute to the enhancement and expansion of SEA-LION. Contributions can involve identifying and reporting bugs, sharing pre-training, instruction, and preference data, improving documentation usability, proposing and implementing new model evaluation tasks and metrics, or training versions of the model in additional Southeast Asian languages. Join us in shaping the future of SEA-LION by sharing your expertise and insights to make these models more accessible, accurate, and versatile. Please check out our GitHub for further information on the call for contributions.

## The Team

Lau Wayne<br>
Leong Wei Qi<br>
Li Yier<br>
Liu Bing Jie Darius<br>
Lovenia Holy<br>
Montalan Jann Railey<br>
Ng Boon Cheong Raymond<br>
Ngui Jian Gang<br>
Nguyen Thanh Ngan<br>
Ong Tat-Wee David<br>
Rengarajan Hamsawardhini<br>
Siow Bryan<br>
Susanto Yosephine<br>
Tai Ngee Chia<br>
Tan Choon Meng<br>
Teng Walter<br>
Teo Eng Sipp Leslie<br>
Teo Wei Yi<br>
Tjhi William<br>
Yeo Yeow Tong<br>
Yong Xianbin<br>

## Acknowledgements

[AI Singapore](​​https://aisingapore.org/) is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation or the National University of Singapore. 

## Contact

For more info, please contact us using this [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6)

[Link to SEA-LION's GitHub repository](https://github.com/aisingapore/sealion)

## Disclaimer

This is the repository for the commercial instruction-tuned model.
The model has _not_ been aligned for safety.
Developers and users should perform their own safety fine-tuning and related security measures.
In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.