---
language:
- en
license: apache-2.0
tags:
- summarization
- azureml
- azure
- codecarbon
- bart
datasets:
- samsum
metrics:
- rouge
model-index:
- name: bart-large-samsum
  results:
  - task: 
      name: Abstractive Text Summarization
      type: abstractive-text-summarization
    dataset:
      name: "SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization" 
      type: samsum
    metrics:
    - name: Validation ROGUE-1
      type: rouge-1
      value: 55.0234
    - name: Validation ROGUE-2
      type: rouge-2
      value: 29.6005
    - name: Validation ROGUE-L
      type: rouge-L
      value: 44.914
    - name: Validation ROGUE-Lsum
      type: rouge-Lsum
      value: 50.464
    - name: Test ROGUE-1
      type: rouge-1
      value: 53.4345
    - name: Test ROGUE-2
      type: rouge-2
      value: 28.7445
    - name: Test ROGUE-L
      type: rouge-L
      value: 44.1848
    - name: Test ROGUE-Lsum
      type: rouge-Lsum
      value: 49.1874
widget:
- text: | 
    Henry: Hey, is Nate coming over to watch the movie tonight?
    Kevin: Yea, he said he'll be arriving a bit later at around 7 since he gets off of work at 6. Have you taken out the garbage yet?
    Henry: Oh I forgot. I'll do that once I'm finished with my assignment for my math class.
    Kevin: Yea, you should take it out as soon as possible. And also, Nate is bringing his girlfriend.
    Henry: Nice, I'm really looking forward to seeing them again.
---

## `bart-large-samsum`
This model was trained using Microsoft's [`Azure Machine Learning Service`](https://azure.microsoft.com/en-us/services/machine-learning). It was fine-tuned on the [`samsum`](https://huggingface.co/datasets/samsum) corpus from [`facebook/bart-large`](https://huggingface.co/facebook/bart-large) checkpoint.

## Usage (Inference)
```python
from transformers import pipeline
summarizer = pipeline("summarization", model="linydub/bart-large-samsum")

input_text = '''
    Henry: Hey, is Nate coming over to watch the movie tonight?
    Kevin: Yea, he said he'll be arriving a bit later at around 7 since he gets off of work at 6. Have you taken out the garbage yet?
    Henry: Oh I forgot. I'll do that once I'm finished with my assignment for my math class.
    Kevin: Yea, you should take it out as soon as possible. And also, Nate is bringing his girlfriend.
    Henry: Nice, I'm really looking forward to seeing them again.
'''
summarizer(input_text)
```

## Fine-tune on AzureML
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Flinydub%2Fazureml-greenai-txtsum%2Fmain%2F.cloud%2Ftemplate-hub%2Flinydub%2Farm-bart-large-samsum.json) [![Visualize](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/visualizebutton.svg?sanitize=true)](http://armviz.io/#/?load=https://raw.githubusercontent.com/linydub/azureml-greenai-txtsum/main/.cloud/template-hub/linydub/arm-bart-large-samsum.json)

More information about the fine-tuning process (including samples and benchmarks):  
**[Preview]** https://github.com/linydub/azureml-greenai-txtsum

## Resource Usage
These results were retrieved from [`Azure Monitor Metrics`](https://docs.microsoft.com/en-us/azure/azure-monitor/essentials/data-platform-metrics). All experiments were ran on AzureML low priority compute clusters.

| Key | Value |
| --- | ----- |
| Region | US West 2 |
| AzureML Compute SKU | STANDARD_ND40RS_V2 |
| Compute SKU GPU Device | 8 x NVIDIA V100 32GB (NVLink) |
| Compute Node Count | 1 |
| Run Duration | 6m 48s |
| Compute Cost (Dedicated/LowPriority) | $2.50 / $0.50 USD |
| Average CPU Utilization | 47.9% |
| Average GPU Utilization | 69.8% |
| Average GPU Memory Usage | 25.71 GB |
| Total GPU Energy Usage | 370.84 kJ |


*Compute cost ($) is estimated from the run duration, number of compute nodes utilized, and SKU's price per hour. Updated SKU pricing could be found [here](https://azure.microsoft.com/en-us/pricing/details/machine-learning).  

### Carbon Emissions
These results were obtained using [`CodeCarbon`](https://github.com/mlco2/codecarbon). The carbon emissions are estimated from training runtime only (excl. setup and evaluation runtimes).  

| Key | Value |
| --- | ----- |
| timestamp | 2021-09-16T23:54:25 |
| duration | 263.2430217266083 |
| emissions | 0.029715544634717518 |
| energy_consumed | 0.09985062041235725 |
| country_name | USA |
| region | Washington |
| cloud_provider | azure |
| cloud_region | westus2 |

## Hyperparameters

- max_source_length: 512
- max_target_length: 90
- fp16: True
- seed: 1
- per_device_train_batch_size: 16
- per_device_eval_batch_size: 16
- gradient_accumulation_steps: 1
- learning_rate: 5e-5
- num_train_epochs: 3.0
- weight_decay: 0.1



## Results
| ROUGE | Score |
| ----- | ----- |
| eval_rouge1 | 55.0234 |
| eval_rouge2 | 29.6005 |
| eval_rougeL | 44.914 |
| eval_rougeLsum | 50.464 |
| predict_rouge1 | 53.4345 |
| predict_rouge2 | 28.7445 |
| predict_rougeL | 44.1848 |
| predict_rougeLsum | 49.1874 |

| Metric | Value |
| ------ | ----- |
| epoch | 3.0 |
| eval_gen_len | 30.6027 |
| eval_loss | 1.4327096939086914 |
| eval_runtime | 22.9127 |
| eval_samples | 818 |
| eval_samples_per_second | 35.701 |
| eval_steps_per_second | 0.306 |
| predict_gen_len | 30.4835 |
| predict_loss | 1.4501988887786865 |
| predict_runtime | 26.0269 |
| predict_samples | 819 |
| predict_samples_per_second | 31.467 |
| predict_steps_per_second | 0.269 |
| train_loss | 1.2014821151207233 |
| train_runtime | 263.3678 |
| train_samples | 14732 |
| train_samples_per_second | 167.811 |
| train_steps_per_second | 1.321 |
| total_steps | 348 |
| total_flops | 4.26008990669865e+16 |