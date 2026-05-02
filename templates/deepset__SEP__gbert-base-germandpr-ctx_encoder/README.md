---
language: de
datasets:
- deepset/germandpr
license: mit
thumbnail: https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg
tags:
- exbert
---

![bert_image](https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg)

## Overview
**Language model:** gbert-base-germandpr   
**Language:** German  
**Training data:** GermanDPR train set (~ 56MB)  
**Eval data:** GermanDPR test set (~ 6MB)   
**Infrastructure**: 4x V100 GPU  
**Published**: Apr 26th, 2021

## Details
- We trained a dense passage retrieval model with two gbert-base models as encoders of questions and passages.
- The dataset is GermanDPR, a new, German language dataset, which we hand-annotated and published [online](https://deepset.ai/germanquad).
- It comprises 9275 question/answer pairs in the training set and 1025 pairs in the test set.
For each pair, there are one positive context and three hard negative contexts.
- As the basis of the training data, we used our hand-annotated GermanQuAD dataset as positive samples and generated hard negative samples from the latest German Wikipedia dump (6GB of raw txt files).
- The data dump was cleaned with tailored scripts, leading to 2.8 million indexed passages from German Wikipedia.

See https://deepset.ai/germanquad for more details and dataset download.

## Hyperparameters
```
batch_size = 40
n_epochs = 20
num_training_steps = 4640
num_warmup_steps = 460
max_seq_len = 32 tokens for question encoder and 300 tokens for passage encoder
learning_rate = 1e-6
lr_schedule = LinearWarmup
embeds_dropout_prob = 0.1
num_hard_negatives = 2
```
## Performance
During training, we monitored the in-batch average rank and the loss and evaluated different batch sizes, numbers of epochs, and number of hard negatives on a dev set split from the train set.
The dev split contained 1030 question/answer pairs.
Even without thorough hyperparameter tuning, we observed quite stable learning. Multiple restarts with different seeds produced quite similar results.
Note that the in-batch average rank is influenced by settings for batch size and number of hard negatives. A smaller number of hard negatives makes the task easier.
After fixing the hyperparameters we trained the model on the full GermanDPR train set.
  
We further evaluated the retrieval performance of the trained model on the full German Wikipedia with the GermanDPR test set as labels. To this end, we converted the GermanDPR test set to SQuAD format. The DPR model drastically outperforms the BM25 baseline with regard to recall@k.
![performancetable](https://lh3.google.com/u/0/d/1lX6G0cp4NTx1yUWs74LI0Gcs41sYy_Fb=w2880-h1578-iv1)

## Authors
- Timo Möller: `timo.moeller [at] deepset.ai`
- Julian Risch: `julian.risch [at] deepset.ai`
- Malte Pietsch: `malte.pietsch [at] deepset.ai`

## About us

<div class="grid lg:grid-cols-2 gap-x-4 gap-y-3">
    <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/deepset-logo-colored.png" class="w-40"/>
     </div>
     <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/haystack-logo-colored.png" class="w-40"/>
     </div>
</div>

[deepset](http://deepset.ai/) is the company behind the production-ready open-source AI framework [Haystack](https://haystack.deepset.ai/).

Some of our other work: 
- [Distilled roberta-base-squad2 (aka "tinyroberta-squad2")](https://huggingface.co/deepset/tinyroberta-squad2)
- [German BERT](https://deepset.ai/german-bert), [GermanQuAD and GermanDPR](https://deepset.ai/germanquad), [German embedding model](https://huggingface.co/mixedbread-ai/deepset-mxbai-embed-de-large-v1)
- [deepset Cloud](https://www.deepset.ai/deepset-cloud-product), [deepset Studio](https://www.deepset.ai/deepset-studio)

## Get in touch and join the Haystack community

<p>For more info on Haystack, visit our <strong><a href="https://github.com/deepset-ai/haystack">GitHub</a></strong> repo and <strong><a href="https://docs.haystack.deepset.ai">Documentation</a></strong>. 

We also have a <strong><a class="h-7" href="https://haystack.deepset.ai/community">Discord community open to everyone!</a></strong></p>

[Twitter](https://twitter.com/Haystack_AI) | [LinkedIn](https://www.linkedin.com/company/deepset-ai/) | [Discord](https://haystack.deepset.ai/community) | [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) | [Website](https://haystack.deepset.ai/) | [YouTube](https://www.youtube.com/@deepset_ai)

By the way: [we're hiring!](http://www.deepset.ai/jobs)