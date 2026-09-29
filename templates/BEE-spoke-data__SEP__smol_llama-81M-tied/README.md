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
- text: My name is El Microondas the Wise and
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


# smol_llama-81M-tied

<img src="smol-llama-banner.png" alt="banner" style="max-width:80%; height:auto;">

A small 81M param (total) decoder model, enabled through tying the input/output embeddings. This is the first version of the model.

- 768 hidden size, 6 layers
- standard multi-head attention (24 heads), context length 1024
- input/output embeddings **are tied**
- train-from-scratch

## Notes

**This checkpoint** is the 'raw' pre-trained model and has not been tuned to a more specific task. **It should be fine-tuned** before use in most cases.

- slightly larger 101M param GQA pretrained version: [here](https://huggingface.co/BEE-spoke-data/smol_llama-101M-GQA)
- For the chat version of this model, please [see here](https://youtu.be/dQw4w9WgXcQ?si=3ePIqrY1dw94KMu4)

---
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_BEE-spoke-data__smol_llama-81M-tied)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 24.52   |
| ARC (25-shot)         | 22.18          |
| HellaSwag (10-shot)   | 29.33    |
| MMLU (5-shot)         | 24.06         |
| TruthfulQA (0-shot)   | 43.97   |
| Winogrande (5-shot)   | 49.25   |
| GSM8K (5-shot)        | 0.23        |
| DROP (3-shot)         | 2.64         |
