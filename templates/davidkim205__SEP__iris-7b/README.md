---
library_name: transformers
license: apache-2.0
language:
- en
- ko
pipeline_tag: translation
tags:
- finetuned
inference: true
widget:
- messages:
  - role: user
    content: 다음 문장을 한글로 번역하세요. Iris is a model for Korean-English sentence translation based on deep learning.
---

# iris

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64241c3d774cc340797429fc/3had0ckV_asjoJB9fKKKy.jpeg)

Iris is a model for Korean-English sentence translation based on deep learning. 

It is used to translate Korean sentences into English or English sentences into Korean by utilizing advanced natural language processing technology. 
The model is trained to understand the grammar, vocabulary, and context of each language and generate appropriate translations. 
Iris provides efficient and accurate translation and can be used in a variety of applications.


## Model Details

* **Model Developers** :  davidkim(changyeon kim)
* **Repository** : will be updated soon.
* **base mode** : mistralai/Mistral-7B-v0.2
* **dataset** : translation_v3_346k

## usage
```
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo = "davidkim205/iris-7b"
model = AutoModelForCausalLM.from_pretrained(repo, torch_dtype=torch.bfloat16, device_map='auto')
tokenizer = AutoTokenizer.from_pretrained(repo)

def generate(prompt):
    encoding = tokenizer(
        prompt,
        return_tensors='pt',
        return_token_type_ids=False
    ).to("cuda")
    gen_tokens = model.generate(
        **encoding,
        max_new_tokens=2048,
        temperature=1.0,
        num_beams=5,
    )
    prompt_end_size = encoding.input_ids.shape[1]
    result = tokenizer.decode(gen_tokens[0, prompt_end_size:])

    return result


def translate_ko2en(text):
    prompt = f"[INST] 다음 문장을 영어로 번역하세요.{text} [/INST]"
    return generate(prompt)


def translate_en2ko(text):
    prompt = f"[INST] 다음 문장을 한글로 번역하세요.{text} [/INST]"
    return generate(prompt)


def main():
    while True:
        text = input('>')
        en_text = translate_ko2en(text)
        ko_text = translate_en2ko(en_text)
        print('en_text', en_text)
        print('ko_text', ko_text)

if __name__ == "__main__":
    main()
```
output

```
$ python iris_test.py 
Downloading shards: 100%|█████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00,  4.72it/s]
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████████████████| 3/3 [00:02<00:00,  1.07it/s]
>아이리스는 딥러닝을 기반으로 한 한-영어 문장 번역을 위한 모델이다.
en_text Iris is a model for Korean-to-English sentence translation based on deep learning.</s>
ko_text 아이리스는 딥러닝을 기반으로 한 한국어-영어 문장 번역을 위한 모델이다.</s>

```
## template
### ko -> en
```
[INST] 다음 문장을 영어로 번역하세요.{text} [/INST]
```
### en -> ko
```
"[INST] 다음 문장을 한글로 번역하세요.{text} [/INST]"
```

## dataset info : translation_v3_346k

The dataset is not made public due to licensing issues.

| src                                        | ratio | description                                                  |
| ------------------------------------------ | ----- | ------------------------------------------------------------ |
| aihub-MTPE                                 | 5.56% | 기계번역 품질 사후검증 데이터셋                              |
| aihub-techsci2                             | 5.56% | ICT, 전기/전자 등 기술과학 분야 한영 번역 데이터셋           |
| aihub-expertise                            | 5.56% | 의료, 금융, 스포츠 등 전문분야 한영 번역 데이터셋            |
| aihub-humanities                           | 5.56% | 인문학 분야 한영 번역 데이터셋                               |
| sharegpt-deepl-ko-translation              | 5.56% | shareGPT 데이터셋을 질답 형식에서 한영 번역 형식으로 변환한 데이터셋 |
| aihub-MT-new-corpus                        | 5.56% | 기계 번역 앱 구축용 한영 번역 데이터셋                       |
| aihub-socialsci                            | 5.56% | 법률, 교육, 경제 등 사회과학 분야 한영 번역 데이터셋         |
| korean-parallel-corpora                    | 5.56% | 한영 번역 병렬 데이터셋                                      |
| aihub-parallel-translation                 | 5.56% | 발화 유형 및 분야별 한영 번역 데이터셋                       |
| aihub-food                                 | 5.56% | 식품 분야 영한 번역 데이터셋                                 |
| aihub-techsci                              | 5.56% | ICT, 전기/전자 등 기술과학 분야 한영 번역 데이터셋           |
| para_pat                                   | 5.56% | ParaPat 데이터셋의 영어-한국어 subset                        |
| aihub-speechtype-based-machine-translation | 5.56% | 발화 유형별 영한 번역 데이터셋                               |
| koopus100                                  | 5.56% | OPUS-100 데이터셋의 영어-한국어 subset                       |
| aihub-basicsci                             | 5.56% | 수학, 물리학 등 기초과학 분야 한영 번역 데이터셋             |
| aihub-broadcast-content                    | 5.56% | 방송 콘텐츠 분야 한영 번역 데이터셋                          |
| aihub-patent                               | 5.56% | 특허명세서 영한 번역 데이터셋                                |
| aihub-colloquial                           | 5.56% | 신조어, 약어 등을 포함하는 구어체 한영 번역 데이터셋         |

Please refer to the url below for information on aihub licensing.

https://aihub.or.kr/partcptnmlrd/inqry/view.do?currMenu=144&topMenu=104

## Evaluation

https://github.com/davidkim205/translation

| TYPE        | Model                               | BLEU | SBLEU | Duplicate | Length Exceeds |
| ----------- | :---------------------------------- | ---- | ----- | --------- | -------------- |
| HuggingFace | facebook/nllb-200-distilled-1.3B    | 0.26 | 0.30  | 1         | 3              |
| HuggingFace | jbochi/madlad400-10b-mt             | 0.29 | 0.38  | 3         | 6              |
| HuggingFace | Unbabel/TowerInstruct-7B-v0.1       | 0.32 | 0.39  | 1         | 9              |
| HuggingFace | squarelike/Gugugo-koen-7B-V1.1      | 0.32 | 0.36  | 1         | 3              |
| HuggingFace | maywell/Synatra-7B-v0.3-Translation | 0.35 | 0.41  | 1         | 2              |
| Cloud       | deepl                               | 0.39 | 0.45  | 0         | 1              |
| Cloud       | azure                               | 0.40 | 0.49  | 0         | 3              |
| Cloud       | google                              | 0.40 | 0.49  | 0         | 2              |
| Cloud       | papago                              | 0.43 | 0.51  | 0         | 3              |
| HuggingFace | davidkim205/iris-7b (**ours**)      | 0.40 | 0.43  | 0         | 3              |