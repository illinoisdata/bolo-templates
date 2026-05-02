---
language:
- en
license:
- apache-2.0
- bsd-3-clause
tags:
- summarization
- extractive
- summary
- abstractive
- multi-task
- document summary
datasets:
- jordiclive/scored_summarization_datasets
metrics:
- rouge
---

# Multi-purpose Summarizer (Fine-tuned 3B google/flan-t5-xl on several Summarization datasets)

 <a href="https://colab.research.google.com/drive/1EYfnIoG-r5lL2-3oiO_YdYEVKB0pAa9h">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

A fine-tuned version of [google/flan-t5-xl](https://huggingface.co/google/flan-t5-xl) on various summarization datasets (xsum, wikihow, cnn_dailymail/3.0.0, samsum, scitldr/AIC, billsum, TLDR)

Goal: a model that can be used for a general-purpose summarizer for academic and general usage. Control over the type of summary can be given by varying the instruction prepended to the source document. The result works well on lots of text, although trained with a max source length of 512 tokens and 150 max summary length. 

---

## Usage 
Check the colab notebook for desired usage
**The model expects a prompt prepended to the source document to indicate the type of summary**, examples of prompts used to train the model here:
Prompts should be formatted with a colon at the end so that the input to the model is formatted as e.g. "Summarize the following: {input_text}". Note this model was trained with far fewer prompts than models like `jordiclive/flan-t5-11b-summarizer-filtered` so new prompts might not generalize as well.
```

. 
prompts = {
    "article": "Produce an article summary of the following news article:",
    "one_sentence": "Given the following news article, summarize the article in one sentence:",
    "conversation": "Briefly summarize in third person the following conversation:",
    "scitldr": "Given the following scientific article, provide a TL;DR summary:",
    "bill": "Summarize the following proposed legislation (bill):",
    "outlines": "Produce an article summary including outlines of each paragraph of the following article:",
}
```
After `pip install transformers` run the following code:

This pipeline will run slower and not have some of the tokenization parameters as the colab.
```python
from transformers import pipeline

summarizer = pipeline("summarization", "jordiclive/flan-t5-3b-summarizer", torch_dtype=torch.bfloat16)

raw_document = 'You must be 18 years old to live or work in New York State...'
prompt = "Produce an article summary of the following news article:"
results = summarizer(
        f"{prompt} {raw_document}",
        num_beams=5,
        min_length=5,
        no_repeat_ngram_size=3,
        truncation=True,
        max_length=512,
    )
```

---

## Training procedure

- Training was done in BF16, deepspeed stage 2 for 6 epochs with ROUGE-2 monitored on the validation set.

## Hardware
- GPU count	8 NVIDIA A100-SXM4-40GB
- CPU count	48
### Training hyperparameters


The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 5
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 2
- effective_train_batch_size: 80
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- warmup_steps: 2000
- num_epochs: 10


### Framework versions

- Transformers 4.24.0
- Pytorch 1.9.1+cu111
- Deepspeed 0.7.4
- Pytorch-lightning 1.8.1


### Citation
```
@misc{jordiclive_flan_t5_3b_summarizer_2023,
  title={{Multi-purpose Summarizer (Fine-tuned google/flan-t5-xl on several Summarization datasets)}},
  author={{Jordan Clive}},
  howpublished={\url{https://huggingface.co/jordiclive/flan-t5-3b-summarizer}},
  year={2023},
  note={Apache 2.0 and BSD-3-Clause License. Fine-tuned on various summarization datasets including xsum, wikihow, cnn_dailymail/3.0.0, samsum, scitldr/AIC, billsum, TLDR. Designed for academic and general usage with control over summary type by varying the instruction prepended to the source document.},
  url={https://huggingface.co/jordiclive/flan-t5-3b-summarizer},
}
```