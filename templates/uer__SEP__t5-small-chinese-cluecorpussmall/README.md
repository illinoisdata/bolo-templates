---
language: zh
datasets: CLUECorpusSmall
widget: 
- text: "作为电子extra0的平台，京东绝对是领先者。如今的刘强extra1已经是身价过extra2的老板。"


---


# Chinese T5

## Model description

This is the set of Chinese T5 models pre-trained by [UER-py](https://github.com/dbiir/UER-py/), which is introduced in [this paper](https://arxiv.org/abs/1909.05658). Besides, the models could also be pre-trained by [TencentPretrain](https://github.com/Tencent/TencentPretrain) introduced in [this paper](https://arxiv.org/abs/2212.06385), which inherits UER-py to support models with parameters above one billion, and extends it to a multimodal pre-training framework.

The Text-to-Text Transfer Transformer (T5) leverages a unified text-to-text format and attains state-of-the-art results on a wide variety of English-language NLP tasks. Following their work, we released a series of Chinese T5 models.

You can download the set of Chinese T5 models either from the [UER-py Modelzoo page](https://github.com/dbiir/UER-py/wiki/Modelzoo), or via HuggingFace from the links below:

|          |           Link           |
| -------- | :-----------------------: |
| **T5-Small**  | [**L=6/H=512 (Small)**][small] |
| **T5-Base**  | [**L=12/H=768 (Base)**][base] |

In T5, spans of the input sequence are masked by so-called sentinel token. Each sentinel token represents a unique mask token for the input sequence and should start with `<extra_id_0>`, `<extra_id_1>`, … up to `<extra_id_99>`. However, `<extra_id_xxx>` is separated into multiple parts in Huggingface's Hosted inference API. Therefore, we replace `<extra_id_xxx>` with `extraxxx` in vocabulary and BertTokenizer regards `extraxxx` as one sentinel token.

## How to use

You can use this model directly with a pipeline for text2text generation (take the case of T5-Small):

```python
>>> from transformers import BertTokenizer, T5ForConditionalGeneration, Text2TextGenerationPipeline
>>> tokenizer = BertTokenizer.from_pretrained("uer/t5-small-chinese-cluecorpussmall")
>>> model = T5ForConditionalGeneration.from_pretrained("uer/t5-small-chinese-cluecorpussmall")
>>> text2text_generator = Text2TextGenerationPipeline(model, tokenizer)  
>>> text2text_generator("中国的首都是extra0京", max_length=50, do_sample=False)
    [{'generated_text': 'extra0 北 extra1 extra2 extra3 extra4 extra5'}]
```

## Training data

[CLUECorpusSmall](https://github.com/CLUEbenchmark/CLUECorpus2020/) is used as training data. 

## Training procedure

The model is pre-trained by [UER-py](https://github.com/dbiir/UER-py/) on [Tencent Cloud](https://cloud.tencent.com/). We pre-train 1,000,000 steps with a sequence length of 128 and then pre-train 250,000 additional steps with a sequence length of 512. We use the same hyper-parameters on different model sizes.

Taking the case of T5-Small

Stage1:

```
python3 preprocess.py --corpus_path corpora/cluecorpussmall.txt \
                      --vocab_path models/google_zh_with_sentinel_vocab.txt \
                      --dataset_path cluecorpussmall_t5_seq128_dataset.pt \
                      --processes_num 32 --seq_length 128 \
                      --dynamic_masking --data_processor t5 
```

```
python3 pretrain.py --dataset_path cluecorpussmall_t5_seq128_dataset.pt \
                    --vocab_path models/google_zh_with_sentinel_vocab.txt \
                    --config_path models/t5/small_config.json \
                    --output_model_path models/cluecorpussmall_t5_small_seq128_model.bin \
                    --world_size 8 --gpu_ranks 0 1 2 3 4 5 6 7 \
                    --total_steps 1000000 --save_checkpoint_steps 100000 --report_steps 50000 \
                    --learning_rate 1e-3 --batch_size 64 \
                    --span_masking --span_geo_prob 0.3 --span_max_length 5

```

Stage2:

```
python3 preprocess.py --corpus_path corpora/cluecorpussmall.txt \
                      --vocab_path models/google_zh_with_sentinel_vocab.txt \
                      --dataset_path cluecorpussmall_t5_small_seq512_dataset.pt \
                      --processes_num 32 --seq_length 512 \
                      --dynamic_masking --data_processor t5
```

```
python3 pretrain.py --dataset_path cluecorpussmall_t5_seq512_dataset.pt \
                    --vocab_path models/google_zh_with_sentinel_vocab.txt \
                    --pretrained_model_path models/cluecorpussmall_t5_small_seq128_model.bin-1000000 \
                    --config_path models/t5/small_config.json \
                    --output_model_path models/cluecorpussmall_t5_small_seq512_model.bin \
                    --world_size 8 --gpu_ranks 0 1 2 3 4 5 6 7 \
                    --total_steps 250000 --save_checkpoint_steps 50000 --report_steps 10000 \
                    --learning_rate 5e-4 --batch_size 16 \
                    --span_masking --span_geo_prob 0.3 --span_max_length 5
```

Finally, we convert the pre-trained model into Huggingface's format:

```
python3 scripts/convert_t5_from_uer_to_huggingface.py --input_model_path models/cluecorpussmall_t5_small_seq512_model.bin-250000 \
                                                      --output_model_path pytorch_model.bin \
                                                      --layers_num 6 \
                                                      --type t5
```


### BibTeX entry and citation info

```
@article{2020t5,
  title   = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
  author  = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
  journal = {Journal of Machine Learning Research},
  pages   = {1-67},
  year    = {2020}
}

@article{zhao2019uer,
  title={UER: An Open-Source Toolkit for Pre-training Models},
  author={Zhao, Zhe and Chen, Hui and Zhang, Jinbin and Zhao, Xin and Liu, Tao and Lu, Wei and Chen, Xi and Deng, Haotang and Ju, Qi and Du, Xiaoyong},
  journal={EMNLP-IJCNLP 2019},
  pages={241},
  year={2019}
}

@article{zhao2023tencentpretrain,
  title={TencentPretrain: A Scalable and Flexible Toolkit for Pre-training Models of Different Modalities},
  author={Zhao, Zhe and Li, Yudong and Hou, Cheng and Zhao, Jing and others},
  journal={ACL 2023},
  pages={217},
  year={2023}
```

[small]:https://huggingface.co/uer/t5-small-chinese-cluecorpussmall
[base]:https://huggingface.co/uer/t5-base-chinese-cluecorpussmall