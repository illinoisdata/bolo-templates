---
language:
- hi
base_model: nurzhanit/whisper-enhanced-ml
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Hi - Sanchit Gandhi
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: default
      split: None
      args: 'config: hi, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 0.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Hi - Sanchit Gandhi

This model is a fine-tuned version of [nurzhanit/whisper-enhanced-ml](https://huggingface.co/nurzhanit/whisper-enhanced-ml) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0003
- Wer: 0.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 25
- training_steps: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 0.0508        | 0.8772 | 50   | 0.0217          | 2.9785 |
| 0.0112        | 1.7544 | 100  | 0.0104          | 1.9943 |
| 0.0064        | 2.6316 | 150  | 0.0048          | 1.1396 |
| 0.0027        | 3.5088 | 200  | 0.0026          | 1.3986 |
| 0.0018        | 4.3860 | 250  | 0.0011          | 0.3108 |
| 0.0006        | 5.2632 | 300  | 0.0006          | 0.0259 |
| 0.0003        | 6.1404 | 350  | 0.0004          | 0.0    |
| 0.0004        | 7.0175 | 400  | 0.0003          | 0.0    |
| 0.0004        | 7.8947 | 450  | 0.0003          | 0.0    |
| 0.0003        | 8.7719 | 500  | 0.0003          | 0.0    |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.5.0+cu124
- Datasets 3.0.2
- Tokenizers 0.19.1