---
license: apache-2.0
thumbnail: https://i.ibb.co/TvyMrRc/rsz-smol-llama-banner.png
language:
- en
inference:
  parameters:
    max_new_tokens: 64
    do_sample: true
    temperature: 0.8
    repetition_penalty: 1.15
    no_repeat_ngram_size: 4
    eta_cutoff: 0.0006
    renormalize_logits: true
widget:
- text: My name is El Microondas the Wise, and
  example_title: El Microondas
- text: Kennesaw State University is a public
  example_title: Kennesaw State University
- text: >-
    Bungie Studios is an American video game developer. They are most famous for
    developing the award winning Halo series of video games. They also made
    Destiny. The studio was founded
  example_title: Bungie
- text: The Mona Lisa is a world-renowned painting created by
  example_title: Mona Lisa
- text: >-
    The Harry Potter series, written by J.K. Rowling, begins with the book
    titled
  example_title: Harry Potter Series
- text: >-
    Question: I have cities, but no houses. I have mountains, but no trees. I
    have water, but no fish. What am I?

    Answer:
  example_title: Riddle
- text: The process of photosynthesis involves the conversion of
  example_title: Photosynthesis
- text: >-
    Jane went to the store to buy some groceries. She picked up apples, oranges,
    and a loaf of bread. When she got home, she realized she forgot
  example_title: Story Continuation
- text: >-
    Problem 2: If a train leaves Station A at 9:00 AM and travels at 60 mph, and
    another train leaves Station B at 10:00 AM and travels at 80 mph, when will
    they meet if the distance between the stations is 300 miles?

    To determine
  example_title: Math Problem
- text: In the context of computer programming, an algorithm is
  example_title: Algorithm Definition
pipeline_tag: text-generation
tags:
- smol_llama
- llama2
datasets:
- JeanKaddour/minipile
- pszemraj/simple_wikipedia_LM
- BEE-spoke-data/wikipedia-20230901.en-deduped
- mattymchen/refinedweb-3m
---


# smol_llama-101M-GQA

<img src="smol-llama-banner.png" alt="banner" style="max-width:95%; height:auto;">

A small 101M param (total) decoder model. This is the first version of the model.

- 768 hidden size, 6 layers
- GQA (24 heads, 8 key-value), context length 1024
- train-from-scratch


## Features

Some cool anecdotes about this model:

- this model was pretrained on **one GPU** for 5 compute-days. You can DIY pretrain too!
- 0% of the training data (to our knowledge) comes from OpenAI synthetic generation

## Notes

**This checkpoint** is the 'raw' pre-trained model and has not been tuned to a more specific task. **It should be fine-tuned** before use in most cases.

### Checkpoints  & Links

- _smol_-er 81M parameter checkpoint with in/out embeddings tied: [here](https://huggingface.co/BEE-spoke-data/smol_llama-81M-tied)
- Fine-tuned on `pypi` to generate Python code - [link](https://huggingface.co/BEE-spoke-data/smol_llama-101M-GQA-python)
- For the chat version of this model, please [see here](https://youtu.be/dQw4w9WgXcQ?si=3ePIqrY1dw94KMu4)


### Citation Info

If you find this experiment useful and would like to add some words to your `.bib` file, it would make us happy. 


```
@misc {beespoke_data_2023,
	author       = { {Peter Szemraj and Vincent Haines} },
	title        = { smol_llama-101M-GQA (Revision 9c9c090) },
	year         = 2023,
	url          = { https://huggingface.co/BEE-spoke-data/smol_llama-101M-GQA },
	doi          = { 10.57967/hf/1440 },
	publisher    = { Hugging Face }
}
```

---


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_BEE-spoke-data__smol_llama-101M-GQA)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 25.32   |
| ARC (25-shot)         | 23.55          |
| HellaSwag (10-shot)   | 28.77    |
| MMLU (5-shot)         | 24.24         |
| TruthfulQA (0-shot)   | 45.76   |
| Winogrande (5-shot)   | 50.67   |
| GSM8K (5-shot)        | 0.83        |
| DROP (3-shot)         | 3.39         |
