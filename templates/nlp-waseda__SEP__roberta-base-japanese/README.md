---
language: ja
license: apache-2.0
datasets:
- wikipedia
- cc100
mask_token: '[MASK]'
widget:
- text: 早稲田 大学 で 自然 言語 処理 を [MASK] する 。
---

# nlp-waseda/roberta-base-japanese

## Model description

This is a Japanese RoBERTa base model pretrained on Japanese Wikipedia and the Japanese portion of CC-100.

As of 2026-04-20, the license of this model has been changed from CC BY-SA 4.0 to Apache License 2.0, as Creative Commons licenses are generally not well-suited for machine learning models.

## How to use

You can use this model for masked language modeling as follows:
```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("nlp-waseda/roberta-base-japanese")
model = AutoModelForMaskedLM.from_pretrained("nlp-waseda/roberta-base-japanese")

sentence = '早稲田 大学 で 自然 言語 処理 を [MASK] する 。' # input should be segmented into words by Juman++ in advance
encoding = tokenizer(sentence, return_tensors='pt')
...
```

You can fine-tune this model on downstream tasks.

## Tokenization

The input text should be segmented into words by [Juman++](https://github.com/ku-nlp/jumanpp) in advance. Juman++ 2.0.0-rc3 was used for pretraining. Each word is tokenized into tokens by [sentencepiece](https://github.com/google/sentencepiece).

`BertJapaneseTokenizer` now supports automatic `JumanppTokenizer` and `SentencepieceTokenizer`. You can use [this model](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) without any data preprocessing.

## Vocabulary

The vocabulary consists of 32000 tokens including words ([JumanDIC](https://github.com/ku-nlp/JumanDIC)) and subwords induced by the unigram language model of [sentencepiece](https://github.com/google/sentencepiece).

## Training procedure

This model was trained on Japanese Wikipedia (as of 20210920) and the Japanese portion of CC-100. It took a week using eight NVIDIA A100 GPUs.

The following hyperparameters were used during pretraining:
- learning_rate: 1e-4
- per_device_train_batch_size: 256
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 2
- total_train_batch_size: 4096
- max_seq_length: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 700000
- warmup_steps: 10000
- mixed_precision_training: Native AMP

## Performance on JGLUE

See the [Baseline Scores](https://github.com/yahoojapan/JGLUE#baseline-scores) of JGLUE.