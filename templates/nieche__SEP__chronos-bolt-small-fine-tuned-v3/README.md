---
library_name: transformers
base_model:
- amazon/chronos-bolt-small
- autogluon/chronos-bolt-small
pipeline_tag: time-series-forecasting
tags:
- forecasting
- time series
- intermitent demand
---
# Model Card for Chronos Bolt Small Fine-Tuned Model v3


<img align="center" height="350" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjRmcWUwaGFkbW1lczJoYzBjbHBxZjMyeDdhdDQycGdzamwyOGhiZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZtB2l3jHiJsFa/giphy.gif"/> </p>



The model was fine-tuned on a proprietary dataset containing 25 million rows of time-series data. While details about the dataset are confidential, the following general characteristics are provided:
- The dataset consists of multi-dimensional time-series data.
- Also added additional exogenous information about the target series (5 additional columns; 2 of them are different types of volumes of the target series). 
 
WQL = 0.5908

This large-scale dataset ensures the model captures complex patterns and temporal dependencies necessary for accurate forecasting.


#### Summary

The fine-tuned model performs well on intermitent demand forecasting.

## Technical Specifications

### Model Architecture and Objective

The model is based on the `amazon/chronos-bolt-small` architecture, fine-tuned specifically for intermittent time-series forecasting tasks. It leverages pre-trained capabilities for sequence-to-sequence modeling, adapted to handle multi-horizon forecasting scenarios.

## Contact:

[NIEXCHE](https://niexche.github.io/) 

[NIEXCHE (Fevzi KILAS)](https://fevzikilas.github.io/)