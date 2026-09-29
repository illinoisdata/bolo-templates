---
inference: false
---

# Robin Model Card

## Model Details

Robin is a series of models finetuned from LLaMA on several high-quality data.

- **Developed by:** [LMFlow](https://github.com/OptimalScale/LMFlow/)
- **Model type:** An auto-regressive language model based on the transformer architecture.
- **License:** Non-commercial license
- **Finetuned from model:** [LLaMA](https://arxiv.org/abs/2302.13971).

### Model Sources

- **Repository:** https://github.com/OptimalScale/LMFlow/
- **Blog:** https://medium.com/@hkust.ml/robin-v2-launches-achieves-unparalleled-performance-on-openllm-4f6886e822c1
- **Paper:** https://arxiv.org/abs/2306.12420
- **Demo:** https://lmflow.com/

## Uses

Robin is primarily utilized for conducting research on extensive language models and chatbots, catering to users specializing in natural language processing, machine learning, and artificial intelligence research.

## How to Get Started with the Model

We provide four kinds of demos including:

- Online Service: If you don't want to run any code and just want to try our models, we deploy our instruction-tuned LLaMA you to have a try.
- Colab Chatbot (shell): An interactive shell-based chatbot for you to easily deploy a chatbot on colab.
- Colab Chatbot (web): An interactive web-based chatbot for you to easily deploy your own chatbot on colab.
- Local Deploy: We also provide a way for you to deploy your model/chatbot locally, which means you can deploy much larger model than previous three methods if you have enough resource.

Please refer to https://github.com/OptimalScale/LMFlow#demos

## Training Details


Expanding upon the initial idea of self-instruct techniques, we incorporated several different data sources and build a new dataset called [LMFlow Dataset](http://lmflow.org:5000/lmflow_data.tar.gz). 
The new training split is created by merging the following datasets:
- ShareGPT: randomly sample 50K English data and 10K Chinese data from ShareGPT.
- GPT-4-LLM: 52K English data from GPT-4-LLM.
- BELLE: randomly sample 80K Chinese data from BELLE.

See more details in the "Instruction Tuning" section in our [paper](https://arxiv.org/pdf/2306.12420.pdf).

## Evaluation

Robin is evaluated with [LMFlow Benchmark](https://blog.gopenai.com/lmflow-benchmark-an-automatic-evaluation-framework-for-open-source-llms-ef5c6f142418).
See more details in this [paper](https://arxiv.org/pdf/2306.12420.pdf).

## Citation
If you find this repository useful, please consider giving ⭐ and citing our [paper](https://arxiv.org/abs/2306.12420):

```
@misc{lmflow,
  author = {Shizhe Diao and Rui Pan and Hanze Dong and KaShun Shum and Jipeng Zhang and Wei Xiong and Tong Zhang},
  title = {LMFlow: An Extensible Toolkit for Finetuning and Inference of Large Foundation Models},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://optimalscale.github.io/LMFlow/}},
}
```