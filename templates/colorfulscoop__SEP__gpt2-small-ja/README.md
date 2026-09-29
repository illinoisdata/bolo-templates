---
language: ja
datasets: wikipedia
widget:
- text: 統計的機械学習でのニューラルネットワーク
license: cc
---

# GPT-2 small Japanese model

This repository contains a GPT2-small model trained on Japanese Wikipedia dataset.

## Training data

[Japanese Wikipedia](https://ja.wikipedia.org/wiki/Wikipedia:データベースダウンロード) dataset as of Aug20, 2021 released under [Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/) is used for both tokenizer and GPT-2 model.

We splitted the dataset into three subsets - train, valid and test sets. Both tokenizer and model were trained on the train set.
Train set contains around 540M tokens.

## Model description

The model architecture is the same as GPT-2 small model (n_ctx: 1024, n_embd 768, n_head: 12, n_layer: 12) except for a vocabulary size.
The vocabulary size is set to 32,000 instead of an original size of 50,257.
`transformers.GPT2LMHeadModel` is used for training.

## Tokenizer description

[SentencePiece](https://github.com/google/sentencepiece) is used as a tokenizer for this model.

We utilized 1,000,000 sentences from train set.
The vocabulary size was 32,000.
A `add_dummy_prefix` option was set to `True` because Japanese words are not separated by whitespaces.

After training, the tokenizer model was imported as `transformers.BERTGenerationTokenizer`
because it supports SentencePiece models and it does not add any special tokens as default,
which is useful expecially for a text generation task.

## Training

The model was trained on the train set for 30 epochs with batch size 32. Each sample contained 1024 tokens.

We utilized Adam optimizer. Learning rate was linearly increased from `0` to `1e-4` during the first 10,000 steps.
A clip norm was set to `1.0`.

Test set perplexity of the trained model was 29.13.

Please refer to [GitHub](https://github.com/colorfulscoop/gpt-ja) for more training details.

## Usage

First, install dependecies.

```sh
$ pip install transformers==4.10.0 torch==1.8.1 sentencepiece==0.1.96
```

Then use pipeline to generate sentences.

```sh
>>> import transformers
>>> pipeline = transformers.pipeline("text-generation", "colorfulscoop/gpt2-small-ja")
>>> pipeline("統計的機械学習でのニューラルネットワーク", do_sample=True, top_p=0.95, top_k=50, num_return_sequences=3)
```

**Note:** The default model configuration `config.json` sets parameters for text generation with `do_sample=True`, `top_k=50`, `top_p=0.95`.
Please set these parameters when you need to use different parameters.

## Versions

We recommend to specify `revision` to load the model for reproducibility.

| Revision | Date of Wikipedia dump |
| --- | --- |
| 20210820.1.0 | Aug 20, 2021 |
| 20210301.1.0 | March 1, 2021 |

You can specify `revision` as follows.

```py
# Example of pipeline
>>> transformers.pipeline("text-generation", "colorfulscoop/gpt2-small-ja", revision="20210820.1.0")
# Example of AutoModel
>>> transformers.AutoModel.from_pretrained("colorfulscoop/gpt2-small-ja", revision="20210820.1.0")
```

## License

All the models included in this repository are licensed under [Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

**Disclaimer:** The model potentially has possibility that it generates similar texts in the training data, texts not to be true, or biased texts. Use of the model is at your sole risk. Colorful Scoop makes no warranty or guarantee of any outputs from the model. Colorful Scoop is not liable for any trouble, loss, or damage arising from the model output.

**Author:** Colorful Scoop
