---
license: cc-by-sa-4.0
language: 
- ja
---
# Model card for model ID

This is a T5 v1.1 model, pre-trained on a Japanese corpus.

## Model details

T5 is a Transformer-based Encoder-Decoder model, now in v1.1, with the following improvements over the original T5.
- GEGLU activation in feed-forward hidden layer, rather than ReLU - see https://arxiv.org/abs/2002.05202 .
- Dropout was turned off in pre-training (quality win). Dropout should be re-enabled during fine-tuning.
- no parameter sharing between embedding and classifier layer
- "xl" and "xxl" replace "3B" and "11B". The model shapes are a bit different - larger d_model and smaller num_heads and d_ff.

This model is based on T5 v1.1. It was pre-trained on a Japanese corpus. For the Japanese corpus, Japanese Wikipedia and mC4/ja were used.

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Retrieva, Inc.
- **Model type:** T5 v1.1
- **Language(s) (NLP):** Japanese
- **License:** CC-BY-SA 4.0 Although commercial use is permitted, we kindly request that you contact us beforehand.


## Training Details

We use T5X (https://github.com/google-research/t5x) for the training of this model, and it has been converted to the Huggingface transformer format.

## Training Data

The training data used is
- The Japanese part of the multilingual C4(mC4/ja).
- Japanese Wikipedia(20220920).
  
#### Preprocessing
The following filtering is done
- Remove documents that do not use a single hiragana character. This removes English-only documents and documents in Chinese.
- Whitelist-style filtering using the top level domain of URL to remove affiliate sites.

#### Training Hyperparameters

- dropout rate: 0.0
- batch size: 256
- fp32
- input length: 512
- output length: 114

- Otherwise, the default value of T5X (https://github.com/google-research/t5x/blob/main/t5x/examples/t5/t5_1_1/base.gin) is followed, including the following.
  - optimizer: Adafactor
  - base_learning_rate: 1.0
  - warmup steps: 10000

#### Speeds, Sizes, Times

We trained 2097152 steps.

## Technical Specifications

### Model Architecture and Objective
Model architecture.
- T5 v1.1(https://github.com/google-research/text-to-text-transfer-transformer/blob/main/released_checkpoints.md#t511)
- Size: Base(~220 million parameters)

### Compute Infrastructure

Google Cloud TPU v4-8.

#### Software

- T5X(https://github.com/google-research/t5x).

## More Information

https://note.com/retrieva/n/n7b4186dc5ada (in Japanese)

## Model Card Authors

Jiro Nishitoba

## Model Card Contact

pr@retrieva.jp