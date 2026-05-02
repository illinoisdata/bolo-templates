---
license: apache-2.0
base_model: xiuyul/mamba-2.8b-ultrachat
datasets:
- HuggingFaceH4/ultrafeedback_binarized
model-index:
- name: mamba-2.8b-zephyr
  results: []
---


# mamba-2.8b-zephyr

This model is a fine-tuned version of [xiuyul/mamba-2.8b-ultrachat](https://huggingface.co/xiuyul/mamba-2.8b-ultrachat) on the [HuggingFaceH4/ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized) dataset trained using [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290). 

The base model, [xiuyul/mamba-2.8b-ultrachat](https://huggingface.co/xiuyul/mamba-2.8b-ultrachat), was instruction-tuned from [state-spaces/mamba-2.8b-slimpj](https://huggingface.co/state-spaces/mamba-2.8b-slimpj) on the [HuggingFaceH4/ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) dataset. 

It achieves the following results on the evaluation set:
- Loss: 0.4996
- Rewards/chosen: -0.4523
- Rewards/rejected: -1.6105
- Rewards/accuracies: 0.7857
- Rewards/margins: 1.1582
- Logps/rejected: -290.1885
- Logps/chosen: -359.0926
- Logits/rejected: 23.0423
- Logits/chosen: 23.1861

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6639        | 0.1   | 100  | 0.6593          | 0.1762         | 0.0957           | 0.6151             | 0.0805          | -273.1268      | -352.8086    | 23.5852         | 23.8356       |
| 0.5804        | 0.21  | 200  | 0.5836          | 0.0780         | -0.3396          | 0.6508             | 0.4176          | -277.4798      | -353.7904    | 23.5872         | 23.8302       |
| 0.5815        | 0.31  | 300  | 0.5510          | -0.1923        | -0.7857          | 0.7421             | 0.5934          | -281.9403      | -356.4929    | 23.5224         | 23.7498       |
| 0.5526        | 0.41  | 400  | 0.5361          | -0.1953        | -0.8928          | 0.7341             | 0.6975          | -283.0119      | -356.5235    | 23.5033         | 23.7264       |
| 0.5225        | 0.52  | 500  | 0.5262          | -0.1041        | -0.8809          | 0.7540             | 0.7768          | -282.8929      | -355.6114    | 23.4578         | 23.6718       |
| 0.5577        | 0.62  | 600  | 0.5156          | -0.1946        | -1.0285          | 0.7659             | 0.8339          | -284.3683      | -356.5158    | 23.4466         | 23.6618       |
| 0.5515        | 0.72  | 700  | 0.5163          | 0.0648         | -0.7650          | 0.7659             | 0.8298          | -281.7334      | -353.9220    | 23.4243         | 23.6343       |
| 0.5159        | 0.83  | 800  | 0.5113          | -0.1400        | -1.0595          | 0.7778             | 0.9195          | -284.6783      | -355.9698    | 23.4095         | 23.6179       |
| 0.5242        | 0.93  | 900  | 0.5089          | -0.0383        | -0.9148          | 0.7659             | 0.8766          | -283.2318      | -354.9529    | 23.4035         | 23.6145       |
| 0.4618        | 1.03  | 1000 | 0.5077          | -0.1223        | -1.0201          | 0.7778             | 0.8978          | -284.2841      | -355.7929    | 23.3805         | 23.5856       |
| 0.4484        | 1.14  | 1100 | 0.5019          | -0.3311        | -1.3299          | 0.7778             | 0.9989          | -287.3827      | -357.8807    | 23.3427         | 23.5381       |
| 0.4228        | 1.24  | 1200 | 0.5034          | -0.0617        | -1.0989          | 0.7619             | 1.0372          | -285.0726      | -355.1871    | 23.3191         | 23.5101       |
| 0.4306        | 1.34  | 1300 | 0.5032          | -0.1585        | -1.1849          | 0.7698             | 1.0264          | -285.9320      | -356.1549    | 23.2889         | 23.4787       |
| 0.4678        | 1.45  | 1400 | 0.5030          | -0.2351        | -1.1601          | 0.7817             | 0.9250          | -285.6841      | -356.9207    | 23.2661         | 23.4551       |
| 0.4317        | 1.55  | 1500 | 0.4997          | -0.1401        | -1.1458          | 0.7619             | 1.0057          | -285.5417      | -355.9716    | 23.2621         | 23.4524       |
| 0.4363        | 1.65  | 1600 | 0.5010          | -0.3313        | -1.3592          | 0.7738             | 1.0279          | -287.6752      | -357.8830    | 23.2320         | 23.4178       |
| 0.408         | 1.76  | 1700 | 0.4989          | -0.2456        | -1.3073          | 0.7778             | 1.0617          | -287.1568      | -357.0265    | 23.2135         | 23.3950       |
| 0.4076        | 1.86  | 1800 | 0.4996          | -0.3904        | -1.4365          | 0.7659             | 1.0461          | -288.4482      | -358.4738    | 23.1866         | 23.3617       |
| 0.4547        | 1.96  | 1900 | 0.5008          | -0.2516        | -1.2648          | 0.7857             | 1.0133          | -286.7317      | -357.0858    | 23.1605         | 23.3298       |
| 0.3469        | 2.07  | 2000 | 0.4977          | -0.2868        | -1.3916          | 0.7778             | 1.1048          | -287.9999      | -357.4383    | 23.1361         | 23.2990       |
| 0.3547        | 2.17  | 2100 | 0.4987          | -0.4251        | -1.5510          | 0.7619             | 1.1259          | -289.5935      | -358.8210    | 23.1142         | 23.2730       |
| 0.3468        | 2.27  | 2200 | 0.4979          | -0.2674        | -1.3945          | 0.7778             | 1.1271          | -288.0285      | -357.2443    | 23.0998         | 23.2561       |
| 0.3432        | 2.37  | 2300 | 0.5026          | -0.3792        | -1.4630          | 0.7738             | 1.0838          | -288.7130      | -358.3621    | 23.0726         | 23.2233       |
| 0.324         | 2.48  | 2400 | 0.5022          | -0.4892        | -1.6090          | 0.7698             | 1.1198          | -290.1737      | -359.4620    | 23.0543         | 23.2006       |
| 0.3556        | 2.58  | 2500 | 0.5010          | -0.5270        | -1.6576          | 0.7817             | 1.1306          | -290.6595      | -359.8404    | 23.0520         | 23.1981       |
| 0.3277        | 2.68  | 2600 | 0.4990          | -0.5401        | -1.6816          | 0.7778             | 1.1415          | -290.8996      | -359.9708    | 23.0449         | 23.1901       |
| 0.3262        | 2.79  | 2700 | 0.4993          | -0.4952        | -1.6410          | 0.7778             | 1.1458          | -290.4932      | -359.5220    | 23.0439         | 23.1878       |
| 0.3566        | 2.89  | 2800 | 0.4985          | -0.4474        | -1.5918          | 0.7778             | 1.1443          | -290.0010      | -359.0445    | 23.0433         | 23.1871       |
| 0.3386        | 2.99  | 2900 | 0.4983          | -0.4598        | -1.6040          | 0.7817             | 1.1442          | -290.1235      | -359.1679    | 23.0427         | 23.1866       |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.1+cu121
- Datasets 2.14.6
- Tokenizers 0.14.1