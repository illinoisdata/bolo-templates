---
language:
- ko
license: llama3.2
base_model:
- meta-llama/Llama-3.2-1B-Instruct
datasets:
- KorQuAD/squad_kor_v1
---

# Llama-3.2-1B-Instruct-korQuAD-v1

이 모델은 Llama-3.2-1B-Instruct를 기반으로 한국어 질의응답 태스크에 대해 파인튜닝된 모델입니다.

📥 Total Download: +23K

## 모델 설명

- 기본 모델: Llama-3.2-1B-Instruct
- 학습 데이터셋: KorQuAD v1.0
- 학습 방법: LoRA (Low-Rank Adaptation)
- 주요 태스크: 한국어 질의응답

## 버전 히스토리
### v1.0.0(2024-10-02)
- 초기 버전 업로드
- KorQuAD v1.0 데이터셋 파인튜닝

### v1.1.0(2024-10-30)
- 모델 프롬프트 및 학습 방법 개선
- KorQuAD evaluate 코드 적용

## 성능
| 모델 | Exact Match | F1 Score |
|------|-------------|----------|
| Llama-3.2-1B-Instruct-v1 | 18.86 | 37.2 |
| Llama-3.2-1B-Instruct-v2 | 36.07 | 59.03 |
※ https://korquad.github.io/category/1.0_KOR.html의 evaluation script 사용

## 사용 방법

다음과 같이 모델을 로드하고 사용할 수 있습니다:
```
#모델, 토크나이저 로드
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
model_path = "NakJun/Llama-3.2-1B-Instruct-ko-QuAD"
model = AutoModelForCausalLM.from_pretrained(
model_path,
torch_dtype=torch.bfloat16,
device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

#입력 형식 설정
prompt = f"""
### Question:
{question}
### Context:
{context}
### Answer:
"""

#토큰화 및 추론
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
output = model.generate(
input_ids,
max_new_tokens=100,
temperature=0.1,
repetition_penalty=1.3,
do_sample=True,
eos_token_id=tokenizer.eos_token_id
)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
answer = generated_text.split("Answer:")[-1].strip().split('\n')[0].strip()
print("생성된 답변:", answer)

```

## 학습 세부 정보
- 에폭: 5
- 배치 크기: 1
- 학습률: 2e-4
- 옵티마이저: AdamW (32-bit)
- LoRA 설정:
  - r: 16
  - lora_alpha: 16
  - 대상 모듈: ["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "down_proj", "up_proj"]
  - lora_dropout: 0.01

## 예시 질문 및 답변
```
[예시 1: 순천향대학교]

Context:
순천향대학교는 충청남도 아산시 신창면 순천향로에 위치한 사립 종합대학교입니다.
순천향대학교에는 1983년 공과대학이 설립되었습니다.

Question: 순천향대학교의 위치는?
Answer: 충청남도 아산시 신창면 순천향로

[예시 2: 아이브(IVE)]

Context:
아이브(IVE)는 대한민국의 스타쉽 엔터테인먼트 소속의 6인조 걸그룹으로, 2021년 12월 1일에 데뷔했습니다.
그룹 이름인 'IVE'는 "I HAVE"에서 유래했으며, "내가 가진 것을 당당하게 보여주겠다"는 의미를 담고 있습니다.
데뷔와 동시에 큰 인기를 끌며 빠르게 주목받는 그룹 중 하나로 자리 잡았습니다.
멤버 구성:
안유진 (리더), 가을, 레이, 장원영, 리즈, 이서
주요 활동 및 히트곡:
ELEVEN (2021년): 데뷔곡으로, 세련된 퍼포먼스와 멜로디로 많은 사랑을 받았습니다.
LOVE DIVE (2022년): 중독성 있는 멜로디와 매혹적인 콘셉트로 큰 인기를 얻으며 음악방송에서 다수의 1위를 차지했습니다.
After LIKE (2022년): 'LOVE DIVE'에 이어 히트를 친 곡으로, 아이브의 개성을 더 확고히 하는 곡이었습니다.
아이브는 독특한 콘셉트와 뛰어난 무대 퍼포먼스로 국내외 팬들에게 사랑받고 있으며, 각 멤버들 역시 개별적인 매력을 발산하며 활발히 활동하고 있습니다.
장원영과 안유진은 데뷔 전부터 아이즈원 활동을 통해 주목받았으며, 이후 아이브로서도 성공적인 활동을 이어가고 있습니다.

Question1: 아이브의 리더는 누구야?
Answer1: 안유진

Question2: 아이브 데뷔곡 알려줘.
Answer2: ELEVEN
```
## 연락처
- njsung1217@gmail.com
- https://github.com/nakjun