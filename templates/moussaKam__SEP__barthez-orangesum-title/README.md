---
tags:
- summarization

language:
- fr

license: apache-2.0

widget:
- text: Citant les préoccupations de ses clients dénonçant des cas de censure après la suppression du compte de Trump, un fournisseur d'accès Internet de l'État de l'Idaho a décidé de bloquer Facebook et Twitter. La mesure ne concernera cependant que les clients mécontents de la politique de ces réseaux sociaux.
---
### Barthez model finetuned on orangeSum (title generation)

finetuning: examples/seq2seq/ (as of Nov 06, 2020)

Metrics: ROUGE-2 > 23

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