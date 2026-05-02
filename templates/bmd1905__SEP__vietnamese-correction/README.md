---
tags:
- generated_from_trainer
model-index:
- name: bartpho-syllable-finetuned-vietnamese_correction
  results: []
license: apache-2.0
language:
- vi
---

# bartpho-syllable-finetuned-vietnamese_correction

This model is a fine-tuned version of [vinai/bartpho-syllable](https://github.com/VinAIResearch/BARTpho). The original dataset is avaiable at [@duyvuleo/VNTC](https://github.com/duyvuleo/VNTC), I customized it for error correction task, you can find my final dataset at [Huggingface Datasets](https://huggingface.co/datasets/bmd1905/error-correction-vi). All source code are avaible at [my Github repo](https://github.com/bmd1905/vietnamese-correction).

## Usage
```python
from transformers import pipeline

corrector = pipeline("text2text-generation", model="bmd1905/vietnamese-correction")
```
```python
# Example
MAX_LENGTH = 512

# Define the text samples
texts = [
    "côn viec kin doanh thì rất kho khan nên toi quyết dinh chuyển sang nghề khac  ",
    "toi dang là sinh diên nam hai ở truong đạ hoc khoa jọc tự nhiên , trogn năm ke tiep toi sẽ chọn chuyen nganh về trí tue nhana tạo",
    "Tôi  đang học AI ở trun tam AI viet nam  ",
    "Nhưng sức huỷ divt của cơn bão mitch vẫn chưa thấm vào đâu lsovớithảm hoạ tại Bangladesh ăm 1970 ",
    "Lần này anh Phươngqyết xếp hàng mua bằng được 1 chiếc",
    "một số chuyen gia tài chính ngâSn hànG của Việt Nam cũng chung quan điểmnày",
    "Cac so liệu cho thay ngươi dân viet nam đang sống trong 1 cuôc sóng không duojc nhu mong đọi",
    "Nefn kinh té thé giới đang đúng trươc nguyen co của mọt cuoc suy thoai",
    "Khong phai tất ca nhưng gi chung ta thấy dideu là sụ that",
    "chinh phủ luôn cố găng het suc để naggna cao chat luong nền giáo duc =cua nuoc nhà",
    "nèn kinh te thé giới đang đứng trươc nguy co của mọt cuoc suy thoai",
    "kinh tế viet nam dang dứng truoc 1 thoi ky đổi mơi chưa tung có tienf lệ trong lịch sử"
]

# Batch prediction
predictions = corrector(texts, max_length=MAX_LENGTH)

# Print predictions
for text, pred in zip(texts, predictions):
    print("- " + pred['generated_text'])
```
```
Output:
- Công việc kinh doanh thì rất khó khăn nên tôi quyết định chuyển sang nghề khác.
- Tôi đang là sinh viên hai ở trường đại học khoa học tự nhiên, trong năm kế tiếp, tôi sẽ chọn chuyên ngành về trí tuệ nhân tạo.
- Tôi đang học AI ở trung tâm AI Việt Nam.
- Nhưng sức huỷ diệt của cơn bão mitch vẫn chưa thấm vào đâu so với thảm hoạ tại Bangladesh năm 1970 .
- Lần này anh Phương quyết xếp hàng mua bằng được 1 chiếc.
- Một số chuyên gia tài chính ngân hàng của Việt Nam cũng chung quan điểm này.
- Các số liệu cho thấy ngươi dân Việt Nam đang sống trong 1 cuôc sóng không được nhu mong đọc.
- Niên kinh té thé giới đang đúng trương, nguyên cơ của một cuộc suy thoái.
- Không phai tất ca, nhưng giờ chúng ta thấy điều là sự thật.
- Chính phủ luôn cố găng hết sức để nâng cao chất lượng nền giáo dục của nước nhà.
- Nền kinh tế thế giới đang đứng trước nguy cơ của một cuộc suy thoái.
- Kinh tế Việt Nam đang đứng trước 1 thời kỳ đổi mới, chưa từng có tiền lệ trong lịch sử.
```
You can play around with my code at [Colab notebook](https://colab.research.google.com/github/bmd1905/vietnamese-correction/blob/main/inference.ipynb?hl=en).