---
license: apache-2.0
datasets:
- ChengsenWang/ChatTime-1-Finetune-100K
base_model:
- ChengsenWang/ChatTime-1-7B-Base
tags:
- time-series
- pretrained-model
- foundation-model
- multimodality
- multimodal-time-series-foundation-model
pipeline_tag: time-series-forecasting
---

# ChatTime: A Multimodal Time Series Foundation Model

## ✨ Introduction

In this paper, we innovatively model time series as a foreign language and construct ChatTime, a unified framework for time series and text processing. As an out-of-the-box multimodal time series foundation model, ChatTime provides zero-shot forecasting capability and supports bimodal input/output for both time series and text. We design a series of experiments to verify the superior performance of ChatTime across multiple tasks and scenarios, and create four multimodal datasets to address data gaps. The experimental results demonstrate the potential and utility of ChatTime.

As depicted in Figure 1(c), during the instruction fine-tuning stage, we fine-tune [ChengsenWang/ChatTime-1-7B-Base](https://huggingface.co/ChengsenWang/ChatTime-1-7B-Base) on [ChengsenWang/ChatTime-1-Finetune-100K](https://huggingface.co/datasets/ChengsenWang/ChatTime-1-Finetune-100K), yielding [ChengsenWang/ChatTime-1-7B-Chat](https://huggingface.co/ChengsenWang/ChatTime-1-7B-Chat).

For details on ChatTime models, training data and procedures, and experimental results, please refer to the [arXiv](https://arxiv.org/abs/2412.11376).

![](architecture.png)

## 📈 Usage

We present three minimal examples showing how to perform the multimodal time series analysis using the ChatTime model. The detailed code is available in the [Github](https://github.com/ForestsKing/ChatTime).

### Zero-Shot Time Series Forecasting

```python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from model.model import ChatTime

dataset = "Traffic"
hist_len = 120
pred_len = 24
model_path = "ChengsenWang/ChatTime-1-7B-Chat"

df = pd.read_csv(f"./dataset/{dataset}.csv")
hist_data = np.array(df["Hist"].apply(eval).values.tolist())[:, -hist_len:][0]
pred_data = np.array(df["Pred"].apply(eval).values.tolist())[:, :pred_len][0]

model = ChatTime(hist_len=hist_len, pred_len=pred_len, model_path=model_path)

out = model.predict(hist_data)

hist_x = np.linspace(0, hist_len-1, hist_len)
pred_x = np.linspace(hist_len, hist_len+pred_len-1, pred_len)

plt.figure(figsize=(8, 2), dpi=500)
plt.plot(hist_x, hist_data, color='#000000')
plt.plot(pred_x, pred_data, color='#000000', label='true')
plt.plot(pred_x, out, color='#FF7F0E', label='pred')
plt.axvline(hist_len, color='red')
plt.legend(loc="upper left")
plt.show()

```

### Context-Guided Time Series Forecasting

```python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from model.model import ChatTime

dataset = "PTF"
hist_len = 120
pred_len = 24
model_path = "ChengsenWang/ChatTime-1-7B-Chat"

df = pd.read_csv(f"./dataset/{dataset}.csv")
hist_data = np.array(df["Hist"].apply(eval).values.tolist())[:, -hist_len:][0]
pred_data = np.array(df["Pred"].apply(eval).values.tolist())[:, :pred_len][0]
context = df["Text"].values[0]

model = ChatTime(hist_len=hist_len, pred_len=pred_len, model_path=model_path)

out_text = model.predict(hist_data, context)
out = model.predict(hist_data)

hist_x = np.linspace(0, hist_len-1, hist_len)
pred_x = np.linspace(hist_len, hist_len+pred_len-1, pred_len)

plt.figure(figsize=(8, 2), dpi=500)
plt.plot(hist_x, hist_data, color='#000000')
plt.plot(pred_x, pred_data, color='#000000', label='true')
plt.plot(pred_x, out_text, color='#FF7F0E', label='pred_text')
plt.plot(pred_x, out, color='#1F77B4', label='pred')
plt.axvline(hist_len, color='red')
plt.legend(loc="upper left")
plt.show()

```

### Time Series Question Answering

```python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from model.model import ChatTime

dataset = "TSQA"
model_path = "ChengsenWang/ChatTime-1-7B-Chat"

df = pd.read_csv(f"./dataset/{dataset}.csv")
series = np.array(df["Series"].apply(eval).values.tolist())[0]
question = df["Question"].values[0]
answer = df["Answer"].values[0]

model = ChatTime(model_path=model_path)

out = model.analyze(question, series)

plt.figure(figsize=(8, 2), dpi=500)
plt.plot(series, color='#000000')
plt.show()

print(question)
print(f"\n{out} / {answer}\n")

```

## 📝 Citation

If you find this repo or our work useful for your research, please consider citing the paper:

```tex
@inproceedings{
  author    = {Chengsen Wang and Qi Qi and Jingyu Wang and Haifeng Sun and Zirui Zhuang and Jinming Wu and Lei Zhang and Jianxin Liao},
  title     = {ChatTime: A Unified Multimodal Time Series Foundation Model Bridging Numerical and Textual Data},
  booktitle = {AAAI Conference on Artificial Intelligence},
  year      = {2025},
}
```

## 📪 Contact

If you have any question, please contact [cswang@bupt.edu.cn]().