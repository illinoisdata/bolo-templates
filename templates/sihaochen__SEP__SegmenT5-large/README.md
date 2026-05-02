---
license: cc
language:
- en
---
This is the proposition segmentation model from "Sub-Sentence Encoder: Contrastive Learning of Propositional Semantic Representations" by Chen et. al. 2023. 

## What does the model do?
It splits a complex, long-form sentence into a list of propositions -- i.e. self-contained, atomic pieces of meaning in the sentence. For example, the following sentence --
```
"Dracula is a novel by Bram Stoker featuring Count Dracula as the protagonist."
```
will be split into --
```
['Dracula is a novel by Bram Stoker.', 'Count Dracula is the protagonist of Dracula.']
```
## Usage
The prompt to the model is formatted like: `segment sentence: {input_sentence}`. 

For each sentence, the model will output the propositions concatenated by `[sep]` as a string.  

For example, if we use the following example code to segment `"Dracula is a novel by Bram Stoker featuring Count Dracula as the protagonist."`. 

The model output will be `['Dracula is a novel by Bram Stoker.[sep]Count Dracula is the protagonist of Dracula.']`

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

gen_kwargs = {
    "length_penalty": 0,
    "max_new_tokens": 256,
    "min_length": 10,
    "no_repeat_ngram_size": 0,
    "num_beams": 1,
}

SEGMENT5_PROMPT = "segment sentence: {}"
SEGMENT5_SEP_TOKEN = "[sep]"

model = AutoModelForSeq2SeqLM.from_pretrained("sihaochen/SegmenT5-large")
tokenizer = AutoTokenizer.from_pretrained("sihaochen/SegmenT5-large")

model.eval()

# define an example input sentence
example_sentence = "Dracula is a novel by Bram Stoker featuring Count Dracula as the protagonist."
example_input = SEGMENT5_PROMPT.format(example_sentence)

input_ids = tokenizer(example_input,
                      return_tensors="pt",
                      padding="max_length",
                      max_length=512,
                      truncation=True).input_ids

logits = model.generate(input_ids, **gen_kwargs)
outputs = tokenizer.batch_decode(logits, skip_special_tokens=True)


output = outputs[0].split(SEGMENT5_SEP_TOKEN)

print(output)
# Output: ['Dracula is a novel by Bram Stoker.', 'Count Dracula is the protagonist of Dracula.']
```

## Sub-Sentence Encoder
For model checkpoints + code for the sub-sentence encoders, checkout: https://github.com/schen149/sub-sentence-encoder/

## Citation 
```
@article{chen2023subsentence,
  title={Sub-Sentence Encoder: Contrastive Learning of Propositional Semantic Representations},
  author={Sihao Chen and Hongming Zhang and Tong Chen and Ben Zhou and Wenhao Yu and Dian Yu and Baolin Peng and Hongwei Wang and Dan Roth and Dong Yu},
  journal={arXiv preprint arXiv:2311.04335},
  year={2023},
  URL = {https://arxiv.org/pdf/2311.04335.pdf}
}
```