---
language: ja
thumbnail: https://github.com/rinnakk/japanese-pretrained-models/blob/master/rinna.png
tags:
- gpt-neox
- text-generation
- lm
- nlp
license: mit
datasets:
- cc100
- Wikipedia
- mc4
inference: false
---

# japanese-gpt-neox-small

![rinna-icon](./rinna.png)

This repository provides a small-sized Japanese GPT-NeoX model. The model was trained using code based on [EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox).

# Update log
* 2023/03/20 Update the model weight and config files such that it can be loaded via Huggingface's official GPT-NeoX implementation.

# How to use the model

~~~~
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-small", use_fast=False)
model = GPTNeoXForCausalLM.from_pretrained("rinna/japanese-gpt-neox-small")
~~~~

# Model architecture
A 12-layer, 768-hidden-size transformer-based language model.

# Training
The model was trained on [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz), [Japanese C4](https://huggingface.co/datasets/mc4), and [Japanese Wikipedia](https://dumps.wikimedia.org/other/cirrussearch) to optimize a traditional language modelling objective.

# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer.

# A toy prefix-tuning weight file
Along with pretrained model, we also release a [prefix-tuning](https://arxiv.org/abs/2101.00190) weight file named `smileface_suffix.task0.weight` for demonstration. The toy prefix-tuning weights here is trained to encourage the model to end every generated sentence with a smiling face emoji 😃. Find the training/inference code for prefix-tuning at our Github repo [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt).

Here are a few samples generated with and without the toy prefix weights, respectively.

3 samples without the prefix weights

> 1. 「きっとそれは絶対間違ってないね。 わたしには5か国語に4つの外国語の意味なんてわからない。 でも、とりあえずこの簡単な英文がどんな意味を持つのか知りたいよね!」
> 2. 25分頃に公園に着いて、ベンチに座って待っていると、またしてもS先生から連絡が入りました。 確か、午後の礼拝の時に自分の持ってきたお弁当を食べた記憶が鮮明に残っています。 後でインターネットで検索したら、S先生のブログに飛びました。 今日の晩ごはんは焼きナスを作ってみました! * 上の写真は昨日の朝焼けです。
> 3. CTで歯形ができて、その後さらにその歯形が再び噛めるようになるのは、何が原因だろう? 虫歯になった原因も、口臭かな? それとも歯周病かな? 歯石がとれるまで、、、もうちょっとかかりそう。 子供の虫歯って、なかなか治らないですよね。親兄弟で何度か。 子供の歯根は、親のものになります。 そして自分のものだったり、知らない間に抜いたりし、生えてきたりもします。 大人になって親からみた場合は、白い歯に変わってきて、金属のようーでも悪くなく、親からのむし歯の心配はないですよね。

3 samples with the prefix weights:
> 1. ※海外ブランド品の場合は、返品・返金等はお受け致しかねますので予めご了承願います。 ※ 商品発送後、お客様へ商品返送完了までのスピードを重視する方は海外ブランド品を先に送り付けさせて頂く ケースがございます。 😃
> 2. 私は過去に持っていた不動産を、中古住宅として売却していましたが、その後の私の状況はどうだったのでしょうか? 😃 結果としては、投資物件として売却を考えていますが、今までの相場も読んでいただけばわかると思います。 😃 今まで、物件に対しての投資は非常に控えめにしてきたのですが、今回の提案を読んで、実際に物件を購入する際にはきちんと確認をしようと思います。 😃
> 3. この写真集の表紙をこの台紙にしている作家さんは、まるで誰かの指示を受けて行動している人物のように見える、というのが、この作品をやぶにらんだ「殺し屋集団」の描いている作品であるように思 います。 😃

# Inference with FasterTransformer
After version 5.1, [NVIDIA FasterTransformer](https://github.com/NVIDIA/FasterTransformer) now supports both inference for GPT-NeoX and a variety of soft prompts (including prefix-tuning). The released pretrained model and prefix weights in this repo have been verified to work with FasterTransformer 5.1.

# Release date
September 5, 2022

# How to cite
```bibtex
@misc{rinna-japanese-gpt-neox-small,
    title = {rinna/japanese-gpt-neox-small},
    author = {Zhao, Tianyu and Sawada, Kei},
    url = {https://huggingface.co/rinna/japanese-gpt-neox-small}
}

@inproceedings{sawada2024release,
    title = {Release of Pre-Trained Models for the {J}apanese Language},
    author = {Sawada, Kei and Zhao, Tianyu and Shing, Makoto and Mitsui, Kentaro and Kaga, Akio and Hono, Yukiya and Wakatsuki, Toshiaki and Mitsuda, Koh},
    booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},
    month = {5},
    year = {2024},
    pages = {13898--13905},
    url = {https://aclanthology.org/2024.lrec-main.1213},
    note = {\url{https://arxiv.org/abs/2404.01657}}
}
```

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)
