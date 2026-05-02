---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- transformer3/autotrain-data-finance6
co2_eq_emissions:
  emissions: 0.03294976193424359
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 51355121740
- CO2 Emissions (in grams): 0.0329

## Validation Metrics

- Loss: 1.406
- Rouge1: 29.067
- Rouge2: 19.200
- RougeL: 26.900
- RougeLsum: 26.940
- Gen Len: 20.000

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/transformer3/autotrain-finance6-51355121740
```