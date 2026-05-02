---
language:
- ko
tags:
- ocr
widget:
- src: https://raw.githubusercontent.com/ddobokki/ocr_img_example/master/g.jpg
  example_title: word1
- src: https://raw.githubusercontent.com/ddobokki/ocr_img_example/master/khs.jpg
  example_title: word2
- src: https://raw.githubusercontent.com/ddobokki/ocr_img_example/master/m.jpg
  example_title: word3
pipeline_tag: image-to-text
license: apache-2.0
---

# korean trocr model
- trocr 모델은 디코더의 토크나이저에 없는 글자는 ocr 하지 못하기 때문에, 초성을 사용하는 토크나이저를 사용하는 디코더 모델을 사용하여 초성도 UNK로 나오지 않게 만든 trocr 모델입니다.
- [2023 교원그룹 AI OCR 챌린지](https://dacon.io/competitions/official/236042/overview/description) 에서 얻었던 노하우를 활용하여 제작하였습니다.
## train datasets
AI Hub
- [다양한 형태의 한글 문자 OCR](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=91)
- [공공행정문서 OCR](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=88)

## model structure
- encoder : [trocr-base-stage1's encoder](https://huggingface.co/microsoft/trocr-base-stage1)
- decoder : [KR-BERT-char16424](https://huggingface.co/snunlp/KR-BERT-char16424)

## how to use

```python
from transformers import TrOCRProcessor, VisionEncoderDecoderModel, AutoTokenizer
import requests 
import unicodedata
from io import BytesIO
from PIL import Image

processor = TrOCRProcessor.from_pretrained("ddobokki/ko-trocr") 
model = VisionEncoderDecoderModel.from_pretrained("ddobokki/ko-trocr")
tokenizer = AutoTokenizer.from_pretrained("ddobokki/ko-trocr")

url = "https://raw.githubusercontent.com/ddobokki/ocr_img_example/master/g.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

pixel_values = processor(img, return_tensors="pt").pixel_values 
generated_ids = model.generate(pixel_values, max_length=64)
generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
generated_text = unicodedata.normalize("NFC", generated_text)
print(generated_text)
```