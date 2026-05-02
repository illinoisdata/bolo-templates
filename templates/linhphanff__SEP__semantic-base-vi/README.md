---
license: other
language:
- vi
- en
library_name: transformers
pipeline_tag: sentence-similarity
tags:
- cls token
---

## <a name="sentences-transformers"></a> Using Semantic-base-vi with `transformers` 

### Installation <a name="install2"></a>
- Install `transformers`:

	- `pip install -U transformers`

- Install `pyvi` for word segmentation:

	- `pip install pyvi`

### Example usage <a name="usage2"></a>

```python
import torch
from transformers import AutoModel, AutoTokenizer
from pyvi.ViTokenizer import tokenize

tokenizer = AutoTokenizer.from_pretrained("linhphanff/semantic-base-vi")
model = AutoModel.from_pretrained("linhphanff/semantic-base-vi")

sentences = [
    'Học sinh cần được hướng dẫn kỹ năng học tập.',
    'Thời tiết hôm nay thật đẹp và mát mẻ.',
    'Công nghệ AI đang thay đổi thế giới từng ngày.',
    'Người dân đổ xô đi mua sắm dịp cuối năm.',
    'Giá xăng dầu giảm mạnh so với tháng trước.',
    'Chương trình khuyến mãi hấp dẫn đang diễn ra tại các siêu thị.',
    'Đội tuyển Việt Nam vô địch giải bóng đá Đông Nam Á.',
    'Thủ tướng phát biểu tại hội nghị quốc tế về môi trường.',
    'Nhiều tuyến đường ở thành phố Hồ Chí Minh bị ngập nặng sau cơn mưa lớn.',
    'Sách là nguồn tri thức vô giá cho mỗi con người.'
]

sentences = [tokenize(sentence) for sentence in sentences]

inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

with torch.no_grad():
    embeddings = model(**inputs, output_hidden_states=True, return_dict=True).pooler_output
```