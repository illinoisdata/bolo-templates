---
license: apache-2.0
language:
  - ko
pipeline_tag: image-to-text
tags:
  - trocr
  - vision-encoder-decoder
---

# trocr-small-korean

## Model Details

TrOCR은 Encoder-Decoder 모델로, 이미지 트랜스포머 인코더와 텍스트 트랜스포머 디코더로 이루어져 있습니다.
이미지 인코더는 DeiT 가중치로 초기화되었고, 텍스트 디코더는 자체적으로 학습한 RoBERTa 가중치로 초기화되었습니다.

이 연구는 구글의 TPU Research Cloud(TRC)를 통해 지원받은 Cloud TPU로 학습되었습니다.

## How to Get Started with the Model

```python
import torch

from transformers import VisionEncoderDecoderModel

model = VisionEncoderDecoderModel.from_pretrained("team-lucid/trocr-small-korean")

pixel_values = torch.rand(1, 3, 384, 384)
generated_ids = model.generate(pixel_values)
```

## Training Details
### Training Data

해당 모델은 [synthtiger](https://github.com/clovaai/synthtiger)로 합성된 6M개의 이미지로 학습되었습니다

### Training Hyperparameters

| Hyperparameter      |   Small |
|:--------------------|--------:|
| Warmup Steps        |   4,000 |
| Learning Rates      |    1e-4 |
| Batch Size          |     512 |
| Weight Decay        |    0.01 |
| Max Steps           | 500,000 |
| Learning Rate Decay |     0.1 |
| \\(Adam\beta_1\\)   |     0.9 |
| \\(Adam\beta_2\\)   |    0.98 |