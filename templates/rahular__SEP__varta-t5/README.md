---
license: apache-2.0
datasets:
- rahular/varta
language:
- as
- bh
- bn
- en
- gu
- hi
- kn
- ml
- mr
- ne
- or
- pa
- ta
- te
- ur
---

# Varta-T5

## Model Description
Varta-T5 is a model pre-trained on the `full` training set of [Varta](https://huggingface.co/datasets/rahular/varta) in 14 Indic languages (Assamese, Bhojpuri, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Oriya, Punjabi, Tamil, Telugu, and Urdu) and English, using span corruption and gap-sentence generation as objectives. 

[Varta](https://huggingface.co/datasets/rahular/varta) is a large-scale news corpus for Indic languages, including 41.8 million news articles in 14 different Indic languages (and English), which come from a variety of high-quality sources. 
The dataset and the model are introduced in [this paper](https://arxiv.org/abs/2305.05858). The code is released in [this repository](https://github.com/rahular/varta).

## Uses
You can use this model for causal language modeling, but it's mostly intended to be fine-tuned on a downstream task.

Note that the text-to-text framework allows us to use the same model on any NLP task, including text generation tasks (e.g., machine translation, document summarization, question answering), and classification tasks (e.g., sentiment analysis). 


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

This work is mainly dedicated to the curation of a new multilingual dataset for Indic languages, many of which are low-resource languages. During data collection, we face several limitations that can potentially result in ethical concerns. Some of the important ones are mentioned below: <br>

- Our dataset contains only those articles written by DailyHunt's partner publishers. This has the potential to result in a bias towards a particular narrative or ideology that can affect the representativeness and diversity of the dataset.
- Another limitation is the languages represented in Varta. Out of 22 languages with official status in India, our dataset has only 13. There are 122 major languages spoken by at least 10,000 people and 159 other languages which are extremely low-resourced. None of these languages are represented in our dataset.
- We do not perform any kind of debiasing on Varta. This means that societal and cultural biases may exist in the dataset, which can adversely affect the fairness and inclusivity of the models trained on it.


## How to Get Started with the Model

You can use this model directly for span in-filling. 

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("rahular/varta-t5")

model = AutoModelForSeq2SeqLM.from_pretrained("rahular/varta-t5")
```


## Training Details

### Training Data
Varta contains 41.8 million high-quality news articles in 14 Indic languages and English. 
With 34.5 million non-English article-headline pairs, it is the largest document-level dataset of its kind. 

### Pretraining
- We use span corruption and gap-sentence generation as the pretraining objectives. 
- Both objectives are sampled uniformly during pretraining. 
- Span corruption is similar to masked language modeling except that instead of masking random tokens, we mask spans of tokens with an average length of 3. 
- In gap-sentence prediction, whole sentences are masked instead of spans. We follow [the original work](https://arxiv.org/abs/1912.08777), and select sentences based on their `importance'. 
- Rouge-1 F1-score between the sentence and the document is used as a proxy for importance. 
- We use 0.15 and 0.2 as the masking ratios for span corruption and gap-sentence generation, respectively.

Since data sizes across languages in Varta vary from 1.5K (Bhojpuri) to 14.4M articles (Hindi), we use standard temperature-based sampling to upsample data when necessary.

- We pretrain Varta-T5 using the T5 1.1 base architecture with 12 encoder and decoder layers. 
- We train with maximum sequence lengths of 512 and 256 for the encoder and decoder respectively. 
- We use 12 attention heads with an embedding dimension of 768 and a feed-forward width of 2048. 
- We use a 128K sentencepiece vocabulary. 
- In total, the model has 395M parameters. 
- The model is trained with Adafactor optimizer with a warm-up of 10K steps. 
- We use an initial learning rate of 1e-3 and use square root decay till we reach 2M steps. 
- We use an effective batch size of 256 and train the model on TPU v3-8 chips. 
- The model takes 11 days to train.

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

### Evaluation Results
Please see [the paper](https://arxiv.org/pdf/2305.05858.pdf).

## Citation
```
@misc{aralikatte2023varta,
      title={V\=arta: A Large-Scale Headline-Generation Dataset for Indic Languages}, 
      author={Rahul Aralikatte and Ziling Cheng and Sumanth Doddapaneni and Jackie Chi Kit Cheung},
      year={2023},
      eprint={2305.05858},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```