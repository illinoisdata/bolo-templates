---
tags:
- summarization
- mT5
language:
- th
widget:
- text: "simplify: ถ้าพูดถึงขนมหวานในตำนานที่ชื่นใจที่สุดแล้วละก็ต้องไม่พ้น น้ำแข็งใส แน่เพราะว่าเป็นอะไรที่ชื่นใจสุด"

---

# mt5-cpe-kmutt-thai-sentence-sum
This repository contains the finetuned mT5-base model for Thai sentence summarization. The architecture of the model is based on mT5 model and fine-tuned on text-summarization pairs in Thai.  Also, this project is a Senior Project of Computer Engineering Student at King Mongkut’s University of Technology Thonburi.

## Usage on SimpleTransformer (Tested on version 0.63.4)
```python
from simpletransformers.t5 import T5Model, T5Args
from torch import cuda

model = T5Model("t5", "thanathorn/mt5-cpe-kmutt-thai-sentence-sum", use_cuda=cuda.is_available())

sentence = "simplify: ถ้าพูดถึงขนมหวานในตำนานที่ชื่นใจที่สุดแล้วละก็ต้องไม่พ้น น้ำแข็งใส แน่เพราะว่าเป็นอะไรที่ชื่นใจสุด"
prediction = model.predict([sentence])
print(prediction[0])
```
(See the example on <a href="https://colab.research.google.com/drive/1XiNkZLgy1USwHYFVf_nEzOSWbHGSnYdg?usp=sharing">Google Colab</a>)

### Score
<ul>
  <li>ROUGE-1: 61.7805</li>
  <li>ROUGE-2: 45.9689</li>
  <li>ROUGE-L: 59.3542</li>
</ul>

### Intended uses & limitations
<ul>
  <li>You can use this model for Thai sentence text summarization.</li>
  <li>Not intended to use with paragraph text.</li>
</ul>