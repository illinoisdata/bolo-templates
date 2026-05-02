---
language: zh
datasets: CLUECorpusSmall
widget: 
- text: "作为电子[MASK]的平台，京东绝对是领先者。如今的刘强[MASK]已经是身价过[MASK]的老板。"


---

# Chinese BART

## Model description

This model is pre-trained by [UER-py](https://github.com/dbiir/UER-py/), which is introduced in [this paper](https://arxiv.org/abs/1909.05658). Besides, the models could also be pre-trained by [TencentPretrain](https://github.com/Tencent/TencentPretrain) introduced in [this paper](https://arxiv.org/abs/2212.06385), which inherits UER-py to support models with parameters above one billion, and extends it to a multimodal pre-training framework.

You can download the set of Chinese BART models either from the [UER-py Modelzoo page](https://github.com/dbiir/UER-py/wiki/Modelzoo), or via HuggingFace from the links below:

|                   |              Link              |
| ----------------- | :----------------------------: |
| **BART-Base** | [**L=6/H=768 (Base)**][base] |
| **BART-Large**  | [**L=12/H=1024 (Large)**][large] |

## How to use

You can use this model directly with a pipeline for text2text generation (take the case of BART-Base):

```python
>>> from transformers import BertTokenizer, BartForConditionalGeneration, Text2TextGenerationPipeline
>>> tokenizer = BertTokenizer.from_pretrained("uer/bart-base-chinese-cluecorpussmall")
>>> model = BartForConditionalGeneration.from_pretrained("uer/bart-base-chinese-cluecorpussmall")
>>> text2text_generator = Text2TextGenerationPipeline(model, tokenizer)  
>>> text2text_generator("中国的首都是[MASK]京", max_length=50, do_sample=False)
    [{'generated_text': '中 国 的 首 都 是 北 京'}]
```

## Training data

[CLUECorpusSmall](https://github.com/CLUEbenchmark/CLUECorpus2020/) is used as training data. 

## Training procedure

The model is pre-trained by [UER-py](https://github.com/dbiir/UER-py/) on [Tencent Cloud](https://cloud.tencent.com/). We pre-train 1,000,000 steps with a sequence length of 512.
Taking the case of BART-Base

```
python3 preprocess.py --corpus_path corpora/cluecorpussmall_bert.txt \
                      --vocab_path models/google_zh_vocab.txt \
                      --dataset_path cluecorpussmall_bart_seq512_dataset.pt \
                      --processes_num 32 --seq_length 512 \
                      --data_processor bart
```

```
python3 pretrain.py --dataset_path cluecorpussmall_bart_seq512_dataset.pt \
                    --vocab_path models/google_zh_vocab.txt \
                    --config_path models/bart/base_config.json \
                    --output_model_path models/cluecorpussmall_bart_base_seq512_model.bin \
                    --world_size 8 --gpu_ranks 0 1 2 3 4 5 6 7 \
                    --total_steps 1000000 --save_checkpoint_steps 100000 --report_steps 50000 \
                    --learning_rate 5e-5 --batch_size 8 \
                    --span_masking --span_max_length 3
```

Finally, we convert the pre-trained model into Huggingface's format:

```
python3 scripts/convert_bart_from_uer_to_huggingface.py --input_model_path models/cluecorpussmall_bart_base_seq512_model.bin-1000000 \                                                                
                                                        --output_model_path pytorch_model.bin \                                                                                            
                                                        --layers_num 6
```


### BibTeX entry and citation info

```
@article{lewis2019bart,
  title={Bart: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension},
  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Ves and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:1910.13461},
  year={2019}
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

[base]:https://huggingface.co/uer/bart-base-chinese-cluecorpussmall
[large]:https://huggingface.co/uer/bart-large-chinese-cluecorpussmall