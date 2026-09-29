---
license: other
license_name: openmdw
license_link: LICENSE
pipeline_tag: translation
---
# Seed-X-RM-7B
<a href="https://arxiv.org/pdf/2507.13618">
  <img src="https://img.shields.io/badge/Seed--X-Report-blue"></a>
<a href="https://huggingface.co/collections/ByteDance-Seed/seed-x-6878753f2858bc17afa78543">
  <img src="https://img.shields.io/badge/Seed--X-Hugging Face-brightgreen"></a>
<a href="https://huggingface.co/spaces/ByteDance-Seed/Seed-X">
    <img src="https://img.shields.io/badge/Seed--X-DEMO-purple"></a>
<a href="https://github.com/ByteDance-Seed/Seed-X-7B/blob/main/LICENSE.openmdw">
  <img src="https://img.shields.io/badge/License-OpenMDW-yellow"></a>

## Introduction
We are excited to introduce **Seed-X**, a powerful series of open-source multilingual translation language models, including an instruction model, a reinforcement learning model, and a reward model. It pushes the boundaries of translation capabilities within 7 billion parameters.
We develop Seed-X as an accessible, off-the-shelf tool to support the community in advancing translation research and applications:
* **Exceptional translation capabilities**: Seed-X exhibits state-of-the-art translation capabilities, on par with or outperforming ultra-large models like Gemini-2.5, Claude-3.5, and GPT-4, as validated by human evaluations and automatic metrics.
* **Deployment and inference-friendly**: With a compact 7B parameter count and mistral architecture, Seed-X offers outstanding translation performance in a lightweight and efficient package, ideal for deployment and inference.
* **Broad domain coverage**: Seed-X excels on a highly challenging translation test set spanning diverse domains, including the internet, science and technology, office dialogues, e-commerce, biomedicine, finance, law, literature, and entertainment.
![performance](imgs/model_comparsion.png)

This repo contains the **Seed-X-RM** model, with the following features:
* Type: Causal language models
* Training Stage: Pretraining & Post-training
* Data Source: Human preference data on multilingual translation
* Support: Evaluating translation betweeen 28 languages

| Languages  | Abbr. | Languages  | Abbr. | Languages  | Abbr. | Languages  | Abbr. |
| ----------- | ----------- |-----------|-----------|-----------|-----------| -----------|-----------|
|Arabic | ar  |French              | fr  | Malay            |  ms  | Russian                   | ru                                | 
|Czech  | cs  |Croatian            | hr  | Norwegian Bokmal |  nb                   | Swedish  | sv                | 
|Danish  | da |Hungarian           | hu  |  Dutch           | nl                    |  Thai                      | th      | 
|German  | de |Indonesian          | id  | Norwegian        | no | Turkish                   | tr                   | 
|English | en |Italian             | it  | Polish           | pl  | Ukrainian                 | uk           | 
|Spanish | es |Japanese            | ja  | Portuguese       | pt   | Vietnamese                | vi                   | 
|Finnish | fi |Korean              | ko  | Romanian         | ro                  | Chinese                   | zh  | 

## Model Downloads
| Model Name  | Description | Download |
| ----------- | ----------- |-----------
| Seed-X-Instruct  | Instruction-tuned for alignment with user intent. |🤗 [Model](https://huggingface.co/ByteDance-Seed/Seed-X-Instruct-7B)|
| Seed-X-PPO | RL trained to boost translation capabilities.     | 🤗 [Model](https://huggingface.co/ByteDance-Seed/Seed-X-PPO-7B)|
| Seed-X-PPO-GPTQ-Int8 | Quantization: GPTQ 8-bit.     | 🤗 [Model](https://huggingface.co/ByteDance-Seed/Seed-X-PPO-7B-GPTQ-Int8)|
| Seed-X-PPO-AWQ-Int4 | Quantization: AWQ 4-bit.     | 🤗 [Model](https://huggingface.co/ByteDance-Seed/Seed-X-PPO-7B-AWQ-Int4)|
| 👉 **Seed-X-RM** | Reward model to evaluate the quality of translation.|  🤗 [Model](https://huggingface.co/ByteDance-Seed/Seed-X-RM-7B)| 

## Quickstart
Seed-X-RM assigns a reward score to the given translation using the same prompt format as Seed-X-PPO. It's worth noting that only the scores within the same language direction can be compared. You can refer to the [RM_demo.py](https://huggingface.co/ByteDance-Seed/Seed-X-RM-7B/blob/main/RM_demo.py) script for the calling method.

## Evaluation
We evaluated Seed-X on a diverse set of translation benchmarks, including FLORES-200, WMT-25, and a publicly released [challenge set](https://github.com/ByteDance-Seed/Seed-X-7B/tree/main/challenge_set) accompanied by human evaluations.
![humen_eval](imgs/humen_eval.png)
For detailed benchmark results and analysis, please refer to our [Technical Report](https://arxiv.org/pdf/2507.13618).

## License
This project is licensed under OpenMDW. See the [LICENSE](https://github.com/ByteDance-Seed/Seed-X-7B/blob/main/LICENSE.openmdw) file for details.

## Citation
If you find Seed-X useful for your research and applications, feel free to give us a star ⭐ or cite us using:
```bibtex
@misc{cheng2025seedxbuildingstrongmultilingual,
      title={Seed-X: Building Strong Multilingual Translation LLM with 7B Parameters}, 
      author={Shanbo Cheng and Yu Bao and Qian Cao and Luyang Huang and Liyan Kang and Zhicheng Liu and Yu Lu and Wenhao Zhu and Jingwen Chen and Zhichao Huang and Tao Li and Yifu Li and Huiying Lin and Sitong Liu and Ningxin Peng and Shuaijie She and Lu Xu and Nuo Xu and Sen Yang and Runsheng Yu and Yiming Yu and Liehao Zou and Hang Li and Lu Lu and Yuxuan Wang and Yonghui Wu},
      year={2025},
      eprint={2507.13618},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.13618}, 
}
```