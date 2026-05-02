---
pipeline_tag: time-series-forecasting
license: mit
datasets:
- monash_tsf
---

# Time Series Transformer (trained on monash_tsf/tourism-monthly) 

Time Series Transformer model trained on the tourism-monthly dataset for 30 epochs. 

## Model description

The Time Series Transformer is a vanilla encoder-decoder Transformer for time-series forecasting. The model is trained in the same way as one trains a Transformer for machine translation. At inference time, the model autoregressively generates samples, one time step at a time.

## Usage

We refer to the [documentation](https://huggingface.co/transformers/main/model_doc/time_series_transformer.html) regarding usage.