---
language: en
thumbnail: url to a thumbnail used in social sharing
tags:
- array
- of
- tags
widget:
- text: "question: which description describes the word \" java \" best in the following\
    \ context? descriptions: [  \" A drink consisting of an infusion of ground coffee\
    \ beans \" ,  \" a platform-independent programming lanugage \" ,  or \" an island\
    \ in Indonesia to the south of Borneo \" ]  context: I like to drink ' java '\
    \ in the morning ."
---

# T5-large for Word Sense Disambiguation

If you are using this model in your research work, please cite

```bib
@article{wahle2021incorporating,
  title={Incorporating Word Sense Disambiguation in Neural Language Models},
  author={Wahle, Jan Philip and Ruas, Terry and Meuschke, Norman and Gipp, Bela},
  journal={arXiv preprint arXiv:2106.07967},
  year={2021}
}
```

This is the checkpoint for T5-large after being trained on the [SemCor 3.0 dataset](http://lcl.uniroma1.it/wsdeval/).

Additional information about this model:

* [The t5-large model page](https://huggingface.co/t5-large)
* [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf)
* [Official implementation by Google](https://github.com/google-research/text-to-text-transfer-transformer)

The model can be loaded to perform a few-shot classification like so:

```py
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("jpelhaw/t5-word-sense-disambiguation")
tokenizer = AutoTokenizer.from_pretrained("jpelhaw/t5-word-sense-disambiguation")

input = '''question: which description describes the word " java "\
           best in the following context? \
descriptions:[  " A drink consisting of an infusion of ground coffee beans ", 
                " a platform-independent programming language ", or
                " an island in Indonesia to the south of Borneo " ] 
context: I like to drink " java " in the morning .'''


example = tokenizer.tokenize(input, add_special_tokens=True)

answer = model.generate(input_ids=example['input_ids'], 
                                attention_mask=example['attention_mask'], 
                                max_length=135)
                                
# "a drink consisting of an infusion of ground coffee beans"
```