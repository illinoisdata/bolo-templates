---
language: en
datasets:
- c4
- wikipedia

license: apache-2.0
---

[Google's T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) for **Closed Book Question Answering**.

The model was pre-trained using T5's denoising objective on [C4](https://huggingface.co/datasets/c4) and subsequently additionally pre-trained using [REALM](https://arxiv.org/pdf/2002.08909.pdf)'s salient span masking objective on [Wikipedia](https://huggingface.co/datasets/wikipedia).

**Note**: This model should be fine-tuned on a question answering downstream task before it is useable for closed book question answering.

Other Community Checkpoints: [here](https://huggingface.co/models?search=ssm)

Paper: [How Much Knowledge Can You Pack
Into the Parameters of a Language Model?](https://arxiv.org/abs/1910.10683.pdf)

Authors: *Adam Roberts, Colin Raffel, Noam Shazeer* 


## Abstract

It has recently been observed that neural language models trained on unstructured text can implicitly store and retrieve knowledge using natural language queries. In this short paper, we measure the practical utility of this approach by fine-tuning pre-trained models to answer questions without access to any external context or knowledge. We show that this approach scales with model size and performs competitively with open-domain systems that explicitly retrieve answers from an external knowledge source when answering questions. To facilitate reproducibility and future work, we release our code and trained models at https://goo.gle/t5-cbqa.

![model image](https://raw.githubusercontent.com/patrickvonplaten/scientific_images/master/how_much_know_ledge_image.png)