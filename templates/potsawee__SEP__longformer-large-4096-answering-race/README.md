---
license: apache-2.0
datasets:
- race
language:
- en
library_name: transformers
pipeline_tag: question-answering
inference: false
---
# longformer-large-4096 fine-tuned to RACE for (Multiple-Choice) Question Answering
- Input: `context`, `question`, `options`
- Output: logit (or probability over the options)

## Model Details

longformer-large-4096 model is fine-tuned to the RACE dataset where the input is a concatenation of ```context + question + option```. We follow the architecture/setup described in https://openreview.net/forum?id=HJgJtT4tvB). 
The output is the logit over the options. This is the question answering (QA) component in our [MQAG paper](https://arxiv.org/abs/2301.12307), 
or please refer to the GitHub repo of this project: https://github.com/potsawee/mqag0.

## How to Use the Model

Use the code below to get started with the model. 

```python
>>> import torch
>>> import numpy as np
>>> from transformers import LongformerTokenizer, LongformerForMultipleChoice

>>> tokenizer = LongformerTokenizer.from_pretrained("potsawee/longformer-large-4096-answering-race")
>>> model = LongformerForMultipleChoice.from_pretrained("potsawee/longformer-large-4096-answering-race")

>>> context = r"""Chelsea's mini-revival continued with a third victory in a row as they consigned struggling Leicester City to a fifth consecutive defeat.
Buoyed by their Champions League win over Borussia Dortmund, Chelsea started brightly and Ben Chilwell volleyed in from a tight angle against his old club.
Chelsea's Joao Felix and Leicester's Kiernan Dewsbury-Hall hit the woodwork in the space of two minutes, then Felix had a goal ruled out by the video assistant referee for offside.
Patson Daka rifled home an excellent equaliser after Ricardo Pereira won the ball off the dawdling Felix outside the box.
But Kai Havertz pounced six minutes into first-half injury time with an excellent dinked finish from Enzo Fernandez's clever aerial ball.
Mykhailo Mudryk thought he had his first goal for the Blues after the break but his effort was disallowed for offside.
Mateo Kovacic sealed the win as he volleyed in from Mudryk's header.
The sliding Foxes, who ended with 10 men following Wout Faes' late dismissal for a second booking, now just sit one point outside the relegation zone.
""".replace('\n', ' ')
>>> question = "Who had a goal ruled out for offside?"
>>> options  = ['Ricardo Pereira', 'Ben Chilwell', 'Joao Felix', 'The Foxes']

>>> inputs = prepare_answering_input(
    tokenizer=tokenizer, question=question,
    options=options, context=context,
	)
>>> outputs = model(**inputs)
>>> prob = torch.softmax(outputs.logits, dim=-1)[0].tolist()
>>> selected_answer = options[np.argmax(prob)]

>>> print(prob)
[0.00145158, 0.00460851, 0.99049687, 0.00344302]
>>> print(selected_answer)
Joao Felix
```

where the function that prepare the input to the answering model is:

```python
def prepare_answering_input(
        tokenizer, # longformer_tokenizer
        question,  # str
        options,   # List[str]
        context,   # str
        max_seq_length=4096,
    ):
    c_plus_q   = context + ' ' + tokenizer.bos_token + ' ' + question
    c_plus_q_4 = [c_plus_q] * len(options)
    tokenized_examples = tokenizer(
        c_plus_q_4, options,
        max_length=max_seq_length,
        padding="longest",
        truncation=True,
        return_tensors="pt",
    )
    input_ids = tokenized_examples['input_ids'].unsqueeze(0)
    attention_mask = tokenized_examples['attention_mask'].unsqueeze(0)
    example_encoded = {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
    }
    return example_encoded
```

## Related Models
- Question/Answering Generation ```Context ---> Question + Answer```:
	- https://huggingface.co/potsawee/t5-large-generation-race-QuestionAnswer
	- https://huggingface.co/potsawee/t5-large-generation-squad-QuestionAnswer

- Distractor (False options) Generation: 
	- https://huggingface.co/potsawee/t5-large-generation-race-Distractor

## Citation

```bibtex
@article{manakul2023mqag,
  title={MQAG: Multiple-choice Question Answering and Generation for Assessing Information Consistency in Summarization},
  author={Manakul, Potsawee and Liusie, Adian and Gales, Mark JF},
  journal={arXiv preprint arXiv:2301.12307},
  year={2023}
}
```