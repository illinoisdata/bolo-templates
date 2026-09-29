---
library_name: peft
license: apache-2.0
base_model: Qwen/Qwen3-8B
tags:
- base_model:adapter:Qwen/Qwen3-8B
- lora
- transformers
pipeline_tag: text-generation
model-index:
- name: qwen3-8b-tfdark-lora2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# qwen3-8b-tfdark-lora2

This model is a fine-tuned version of [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4591

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 2
- seed: 4234
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Use paged_adamw_32bit with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 1

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.7729        | 0.0390 | 10   | 0.6565          |
| 0.7065        | 0.0779 | 20   | 0.5978          |
| 0.6099        | 0.1169 | 30   | 0.5906          |
| 0.6092        | 0.1559 | 40   | 0.5761          |
| 0.5505        | 0.1948 | 50   | 0.6050          |
| 0.7018        | 0.2338 | 60   | 0.5220          |
| 0.5566        | 0.2728 | 70   | 0.5375          |
| 0.543         | 0.3117 | 80   | 0.5034          |
| 0.6447        | 0.3507 | 90   | 0.5423          |
| 0.6051        | 0.3897 | 100  | 0.4697          |
| 0.5981        | 0.4286 | 110  | 0.4928          |
| 0.5585        | 0.4676 | 120  | 0.5155          |
| 0.4779        | 0.5066 | 130  | 0.4886          |
| 0.5191        | 0.5455 | 140  | 0.4917          |
| 0.5945        | 0.5845 | 150  | 0.4524          |
| 0.4891        | 0.6235 | 160  | 0.4709          |
| 0.4458        | 0.6624 | 170  | 0.4862          |
| 0.5644        | 0.7014 | 180  | 0.4712          |
| 0.5789        | 0.7404 | 190  | 0.4574          |
| 0.5884        | 0.7793 | 200  | 0.4560          |
| 0.5019        | 0.8183 | 210  | 0.4572          |
| 0.5367        | 0.8573 | 220  | 0.4591          |
| 0.4303        | 0.8962 | 230  | 0.4589          |
| 0.499         | 0.9352 | 240  | 0.4606          |
| 0.4799        | 0.9742 | 250  | 0.4591          |


### Framework versions

- PEFT 0.17.1
- Transformers 4.56.2
- Pytorch 2.8.0+cu128
- Datasets 4.1.1
- Tokenizers 0.22.1