---
license: apache-2.0
language:
- ko
library_name: nemo
pipeline_tag: automatic-speech-recognition
tags:
- conformer-ctc
metrics:
- wer
---
# Conformer-ctc-medium-ko
해당 모델은 [RIVA Conformer ASR Korean](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/speechtotext_ko_kr_conformer)을 AI hub dataset에 대해 파인튜닝을 진행했습니다. <br>
Conformer 기반의 모델은 whisper와 같은 attention 기반 모델과 달리 streaming을 진행하여도 성능이 크게 떨어지지 않고, 속도가 빠르다는 장점이 있습니다.<br>
V100 GPU에서는 RTF가 0.05, CPU(7 cores)에서는 0.35 정도 나오는 것을 확인할 수 있었습니다.<br>
오디오 chunk size 2초의 streaming 테스트에서는 전체 오디오를 넣는 것에 비해서는 20% 정도 성능저하가 있으나 충분히 사용할 수 있는 성능입니다.<br>
추가로 open domain이 아닌 고객 응대 음성과 같은 domain에서는 kenlm을 추가하였을 때 WER 13.45에서 WER 5.27로 크게 성능 향상이 있었습니다.<br>
하지만 그 외의 domain에서는 kenlm의 추가가 큰 성능 향상으로 이어지지 않았습니다.

Streaming 코드와 Denoise model이 포함된 코드는 아래 깃헙에서 확인할 수 있습니다.
[https://github.com/SUNGBEOMCHOI/Korean-Streaming-ASR](https://github.com/SUNGBEOMCHOI/Korean-Streaming-ASR)

### Training results

| Training Loss | Epoch | Wer     |
|:-------------:|:-----:|:-------:|
| 9.09          |  1.0  | 11.51   |


### dataset

| 데이터셋 이름 | 데이터 샘플 수(train/test) |
| --- | --- |
| 고객응대음성 | 2067668/21092 |
| 한국어 음성 | 620000/3000 |
| 한국인 대화 음성 | 2483570/142399 |
| 자유대화음성(일반남녀) | 1886882/263371 |
| 복지 분야 콜센터 상담데이터 | 1096704/206470 |
| 차량내 대화 데이터 | 2624132/332787 |
| 명령어 음성(노인남여) | 137467/237469 |
| 전체 | 10916423(13946시간)/1206588(1474시간) |


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- num_train_epoch: 1
- sample_rate: 16000
- max_duration: 20.0