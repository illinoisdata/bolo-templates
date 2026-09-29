---
tags:
- summarization
- bart

language:
- fr

widget:
- text: Barthez est le meilleur <mask> du monde.

license: apache-2.0

pipeline_tag: "fill-mask"
---
A french sequence to sequence pretrained model based on [BART](https://huggingface.co/facebook/bart-large). <br>
BARThez is pretrained by learning to reconstruct a corrupted input sentence. A corpus of 66GB of french raw text is used to carry out the pretraining. <br>
Unlike already existing BERT-based French language models such as CamemBERT and FlauBERT, BARThez is particularly well-suited for generative tasks (such as abstractive summarization), since not only its encoder but also its decoder is pretrained. 

In addition to BARThez that is pretrained from scratch, we continue the pretraining of a multilingual BART [mBART](https://huggingface.co/facebook/mbart-large-cc25) which boosted its performance in both discriminative and generative tasks. We call the french adapted version [mBARThez](https://huggingface.co/moussaKam/mbarthez).

| Model                                                      | Architecture  | #layers | #params |
| -------------                                              |:-------------:| :-----:|:-----:|
| [BARThez](https://huggingface.co/moussaKam/barthez)        | BASE          | 12     | 165M  |
| [mBARThez](https://huggingface.co/moussaKam/mbarthez)      | LARGE         | 24     | 458M  |

<br>

paper: https://arxiv.org/abs/2010.12321 \
github: https://github.com/moussaKam/BARThez

```
@article{eddine2020barthez,
  title={BARThez: a Skilled Pretrained French Sequence-to-Sequence Model},
  author={Eddine, Moussa Kamal and Tixier, Antoine J-P and Vazirgiannis, Michalis},
  journal={arXiv preprint arXiv:2010.12321},
  year={2020}
}
```
