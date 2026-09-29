---
language: zh
tags:
- roformer
- pytorch
- tf2.0
widget:
- text: "今天[MASK]很好，我想去公园玩！"
---
## 介绍
### tf版本 
https://github.com/ZhuiyiTechnology/roformer

### pytorch版本+tf2.0版本
https://github.com/JunnYu/RoFormer_pytorch

## pytorch使用
```python
import torch
from transformers import RoFormerForMaskedLM, RoFormerTokenizer

text = "今天[MASK]很好，我[MASK]去公园玩。"
tokenizer = RoFormerTokenizer.from_pretrained("junnyu/roformer_chinese_small")
pt_model = RoFormerForMaskedLM.from_pretrained("junnyu/roformer_chinese_small")
pt_inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    pt_outputs = pt_model(**pt_inputs).logits[0]
pt_outputs_sentence = "pytorch: "
for i, id in enumerate(tokenizer.encode(text)):
    if id == tokenizer.mask_token_id:
        tokens = tokenizer.convert_ids_to_tokens(pt_outputs[i].topk(k=5)[1])
        pt_outputs_sentence += "[" + "||".join(tokens) + "]"
    else:
        pt_outputs_sentence += "".join(
            tokenizer.convert_ids_to_tokens([id], skip_special_tokens=True))
print(pt_outputs_sentence)
# pytorch: 今天[天气||心情||感觉||环境||下午]很好，我[要||想||就||可以||去]去公园玩。
```


## tensorflow2.0使用
```python
import tensorflow as tf
from transformers import RoFormerTokenizer, TFRoFormerForMaskedLM
text = "今天[MASK]很好，我[MASK]去公园玩。"
tokenizer = RoFormerTokenizer.from_pretrained("junnyu/roformer_chinese_small")
tf_model = TFRoFormerForMaskedLM.from_pretrained("junnyu/roformer_chinese_small")
tf_inputs = tokenizer(text, return_tensors="tf")
tf_outputs = tf_model(**tf_inputs, training=False).logits[0]
tf_outputs_sentence = "tf2.0: "
for i, id in enumerate(tokenizer.encode(text)):
    if id == tokenizer.mask_token_id:
        tokens = tokenizer.convert_ids_to_tokens(
            tf.math.top_k(tf_outputs[i], k=5)[1])
        tf_outputs_sentence += "[" + "||".join(tokens) + "]"
    else:
        tf_outputs_sentence += "".join(
            tokenizer.convert_ids_to_tokens([id], skip_special_tokens=True))
print(tf_outputs_sentence)
# tf2.0 今天[天气||心情||感觉||环境||下午]很好，我[要||想||就||可以||去]去公园玩。
```

## 引用

Bibtex：

```tex
@misc{su2021roformer,
      title={RoFormer: Enhanced Transformer with Rotary Position Embedding}, 
      author={Jianlin Su and Yu Lu and Shengfeng Pan and Bo Wen and Yunfeng Liu},
      year={2021},
      eprint={2104.09864},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```