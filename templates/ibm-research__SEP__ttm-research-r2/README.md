---
license: cc-by-nc-sa-4.0
pipeline_tag: time-series-forecasting
tags:
- time series
- forecasting
- pretrained models
- foundation models
- time series foundation models
- time-series
---

# Tiny Time Mixer (TTM) Research-Use Model Card

<p align="center" width="100%">
<img src="ttm_image.webp" width="600">
</p>

TinyTimeMixers (TTMs) are compact pre-trained models for Multivariate Time-Series Forecasting, open-sourced by IBM Research. 
**With model sizes starting from 1M params, TTM (accepted in NeurIPS 24) introduces the notion of the first-ever “tiny” pre-trained models for Time-Series Forecasting.** 



This model card contains the model-weights for research-use only and full reproducibility of our results published in our [paper](https://arxiv.org/pdf/2401.03955.pdf). 
However - if you are looking for TTM model weights for commercial and enterprise use, please refer to our granite releases [here](https://huggingface.co/ibm-granite/granite-timeseries-ttm-r2)


TTM outperforms several popular benchmarks demanding billions of parameters in zero-shot and few-shot forecasting. TTMs are lightweight 
forecasters, pre-trained on publicly available time series data with various augmentations. TTM provides state-of-the-art zero-shot forecasts and can easily be 
fine-tuned for multi-variate forecasts with just 5% of the training data to be competitive.  Refer to our [paper](https://arxiv.org/pdf/2401.03955.pdf) for more details.


**The current open-source version supports point forecasting use-cases specifically ranging from minutely to hourly resolutions 
(Ex. 10 min, 15 min, 1 hour.).**

**Note that zeroshot, fine-tuning and inference tasks using TTM can easily be executed in 1 GPU machine or in laptops too!!**


## Model Description

TTM falls under the category of “focused pre-trained models”, wherein each pre-trained TTM is tailored for a particular forecasting 
setting (governed by the context length and forecast length). Instead of building one massive model supporting all forecasting settings, 
we opt for the approach of constructing smaller pre-trained models, each focusing on a specific forecasting setting, thereby 
yielding more accurate results. Furthermore, this approach ensures that our models remain extremely small and exceptionally fast, 
facilitating easy deployment without demanding a ton of resources. 

Hence, in this model card, we plan to release several pre-trained 
TTMs that can cater to many common forecasting settings in practice. Additionally, we have released our source code along with 
our pretraining scripts that users can utilize to pretrain models on their own. Pretraining TTMs is very easy and fast and can be enabled in less than a day as opposed to several days or weeks in traditional approaches.

Each pre-trained model will be released in a different branch name in this model card. Kindly access the required model using our 
getting started [notebook](https://github.com/IBM/tsfm/blob/main/notebooks/hfdemo/ttm_getting_started.ipynb) mentioning the branch name.


## Model Releases (along with the branch name where the models are stored):




- **512-96-ft-r2**: Given the last 512 time-points (i.e. context length), this model can forecast up to the next 96 time-points (i.e. forecast length)
    in future. (branch name: main)
  
- **1024-96-ft-r2**: Given the last 1024 time-points (i.e. context length), this model can forecast up to the next 96 time-points (i.e. forecast length)
    in future.  (branch name: 1024-96-ft-r2) [[Benchmarks]]

- **1536-96-ft-r2**: Given the last 1536 time-points (i.e. context length), this model can forecast up to the next 96 time-points (i.e. forecast length)
    in future. (branch name: 1536-96-ft-r2)

- Likewise, we have models released for forecast lengths up to 720 timepoints. The branch names for these are as follows: `512-192-ft-r2`, `1024-192-ft-r2`, `1536-192-ft-r2`, `512-336-r2`,
  `512-336-ft-r2`, `1024-336-ft-r2`, `1536-336-ft-r2`, `512-720-ft-r2`, `1024-720-ft-r2`, `1536-720-ft-r2`

- Please use the [[get_model]](https://github.com/ibm-granite/granite-tsfm/blob/main/tsfm_public/toolkit/get_model.py) utility to automatically select the required model based on your input context length and forecast length requirement.

- We currently allow 3 context lengths (512, 1024 and 1536) and 4 forecast lengths (96, 192, 336, 720). Users need to provide one of the 3 allowed context lengths as input.
but can provide any forecast lengths up to 720 in get_model() to get the required model.


## Benchmarks

<p align="center" width="100%">
<img src="benchmarks.webp" width="600">
</p>

TTM outperforms popular benchmarks such as TimesFM, Moirai, Chronos, Lag-Llama, Moment, GPT4TS, TimeLLM, LLMTime in zero/fewshot forecasting while reducing computational requirements significantly. 
Moreover, TTMs are lightweight and can be executed even on CPU-only machines, enhancing usability and fostering wider
adoption in resource-constrained environments. For more details, refer to our [paper](https://arxiv.org/pdf/2401.03955.pdf).
- TTM-B referred in the paper maps to the 512 context models.
- TTM-E referred in the paper maps to the 1024 context models.
- TTM-A referred in the paper maps to the 1536 context models.

Please note that the Granite TTM models are pre-trained exclusively on datasets
with clear commercial-use licenses that are approved by our legal team. As a result, the pre-training dataset used in this release differs slightly from the one used in the research
paper, which may lead to minor variations in model performance as compared to the published results. Please refer to our paper for more details.

**Benchmarking Scripts: [here](https://github.com/ibm-granite/granite-tsfm/blob/main/notebooks/hfdemo/tinytimemixer/full_benchmarking/research-use-r2.sh)**


## Recommended Use
1. Users have to externally standard scale their data independently for every channel before feeding it to the model (Refer to [TSP](https://github.com/IBM/tsfm/blob/main/tsfm_public/toolkit/time_series_preprocessor.py), our data processing utility for data scaling.)
2. The current open-source version supports only minutely and hourly resolutions(Ex. 10 min, 15 min, 1 hour.). Other lower resolutions (say weekly, or monthly) are currently not supported in this version, as the model needs a minimum context length of 512 or 1024.
3. Enabling any upsampling or prepending zeros to virtually increase the context length for shorter-length datasets is not recommended and will
   impact the model performance. 



## Model Details

For more details on TTM architecture and benchmarks, refer to our [paper](https://arxiv.org/pdf/2401.03955.pdf).

TTM-1 currently supports 2 modes:

 - **Zeroshot forecasting**: Directly apply the pre-trained model on your target data to get an initial forecast (with no training).

 - **Finetuned forecasting**: Finetune the pre-trained model with a subset of your target data to further improve the forecast.

**Since, TTM models are extremely small and fast, it is practically very easy to finetune the model with your available target data in few minutes 
to get more accurate forecasts.**

The current release supports multivariate forecasting via both channel independence and channel-mixing approaches. 
Decoder Channel-Mixing can be enabled during fine-tuning for capturing strong channel-correlation patterns across 
time-series variates, a critical capability lacking in existing counterparts.

In addition, TTM also supports exogenous infusion and categorical data infusion.


### Model Sources

- **Repository:** https://github.com/ibm-granite/granite-tsfm/tree/main/tsfm_public/models/tinytimemixer
- **Paper:** https://arxiv.org/pdf/2401.03955.pdf


### Blogs and articles on TTM:
-  Refer to our [wiki](https://github.com/ibm-granite/granite-tsfm/wiki)

  
## Uses

```
# Load Model from HF Model Hub mentioning the branch name in revision field

model = TinyTimeMixerForPrediction.from_pretrained(
                "https://huggingface.co/ibm/TTM", revision="main"
            ) 

# Do zeroshot
zeroshot_trainer = Trainer(
        model=model,
        args=zeroshot_forecast_args,
        )
    )

zeroshot_output = zeroshot_trainer.evaluate(dset_test)


# Freeze backbone and enable few-shot or finetuning:

# freeze backbone
for param in model.backbone.parameters():
  param.requires_grad = False

finetune_forecast_trainer = Trainer(
        model=model,
        args=finetune_forecast_args,
        train_dataset=dset_train,
        eval_dataset=dset_val,
        callbacks=[early_stopping_callback, tracking_callback],
        optimizers=(optimizer, scheduler),
    )
finetune_forecast_trainer.train()
fewshot_output = finetune_forecast_trainer.evaluate(dset_test)

```

## Citation
Kindly cite the following paper, if you intend to use our model or its associated architectures/approaches in your 
work

**BibTeX:**

```
@inproceedings{ekambaram2024tinytimemixersttms,
      title={Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series},
      author={Vijay Ekambaram and Arindam Jati and Pankaj Dayama and Sumanta Mukherjee and Nam H. Nguyen and Wesley M. Gifford and Chandra Reddy and Jayant Kalagnanam},
      booktitle={Advances in Neural Information Processing Systems (NeurIPS 2024)},
      year={2024},
}
```

## Model Card Authors

Vijay Ekambaram, Arindam Jati, Pankaj Dayama, Wesley M. Gifford, Sumanta Mukherjee, Chandra Reddy and Jayant Kalagnanam


## IBM Public Repository Disclosure: 

All content in this repository including code has been provided by IBM under the associated 
open source software license and IBM is under no obligation to provide enhancements, 
updates, or support. IBM developers produced this code as an 
open source project (not as an IBM product), and IBM makes no assertions as to 
the level of quality nor security, and will not be maintaining this code going forward.