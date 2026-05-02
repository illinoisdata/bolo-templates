---
language:
- ru
tags:
- PyTorch
- Transformers
thumbnail: "https://github.com/sberbank-ai/model-zoo"
---
# ruT5-base
The model architecture design, pretraining, and evaluation are documented in our preprint: [**A Family of Pretrained Transformer Language Models for Russian**](https://arxiv.org/abs/2309.10931).

The model was trained by the [SberDevices](https://sberdevices.ru/).  
* Task: `text2text generation`
* Type: `encoder-decoder`
* Tokenizer: `bpe`
* Dict size: `32 101`
* Num Parameters: `222 M`	
* Training Data Volume `300 GB`

# Authors
+ NLP core team RnD [Telegram channel](https://t.me/nlpcoreteam):
  + Dmitry Zmitrovich
 
# Cite us
```
@misc{zmitrovich2023family,
      title={A Family of Pretrained Transformer Language Models for Russian}, 
      author={Dmitry Zmitrovich and Alexander Abramov and Andrey Kalmykov and Maria Tikhonova and Ekaterina Taktasheva and Danil Astafurov and Mark Baushenko and Artem Snegirev and Tatiana Shavrina and Sergey Markov and Vladislav Mikhailov and Alena Fenogenova},
      year={2023},
      eprint={2309.10931},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```