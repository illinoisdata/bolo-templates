---
license: apache-2.0
datasets:
- kobkrit/rd-taxqa
- iapp_wiki_qa_squad
- Thaweewat/alpaca-cleaned-52k-th
- Thaweewat/instruction-wild-52k-th
- Thaweewat/databricks-dolly-15k-th
- Thaweewat/hc3-24k-th
- Thaweewat/gpteacher-20k-th
- Thaweewat/onet-m6-social
- Thaweewat/alpaca-finance-43k-th
language:
- th
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- openthaigpt
- llama
---

# 🇹🇭 OpenThaiGPT 1.0.0-alpha
<img src="https://1173516064-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvvbWvIIe82Iv1yHaDBC5%2Fuploads%2Fb8eiMDaqiEQL6ahbAY0h%2Fimage.png?alt=media&token=6fce78fd-2cca-4c0a-9648-bd5518e644ce
https://openthaigpt.aieat.or.th/" width="200px">

OpenThaiGPT Version 1.0.0-alpha is the first Thai implementation of a 7B-parameter LLaMA v2 Chat model finetuned to follow Thai translated instructions below and makes use of the Huggingface LLaMA implementation. 

# ---- Full Huggingface Checkpoint Model ----

## Upgrade from OpenThaiGPT 0.1.0-beta
- Using Facebook LLama v2 model 7b chat as a base model which is pretrained on over 2 trillion token.
- Context Length is upgrade from 2048 token to 4096 token
- Allow research and commerical use.a

## Pretrain Model
- [https://huggingface.co/meta-llama/Llama-2-7b-chat](https://huggingface.co/meta-llama/Llama-2-7b-chat)

## Support
- Official website: https://openthaigpt.aieat.or.th
- Facebook page: https://web.facebook.com/groups/openthaigpt
- A Discord server for discussion and support [here](https://discord.gg/rUTp6dfVUF)
- E-mail: kobkrit@iapp.co.th
  
## License
**Source Code**: License Apache Software License 2.0.<br>
**Weight**: Research and **Commercial uses**.<br>

## Code and Weight
**Colab Demo**: https://colab.research.google.com/drive/1kDQidCtY9lDpk49i7P3JjLAcJM04lawu?usp=sharing<br>
**Finetune Code**: https://github.com/OpenThaiGPT/openthaigpt-finetune-010beta<br>
**Inference Code**: https://github.com/OpenThaiGPT/openthaigpt<br>
**Weight (Lora Adapter)**: https://huggingface.co/openthaigpt/openthaigpt-1.0.0-alpha-7b-chat<br>
**Weight (Huggingface Checkpoint)**: https://huggingface.co/openthaigpt/openthaigpt-1.0.0-alpha-7b-chat-ckpt-hf<br>
**Weight (GGML)**: https://huggingface.co/openthaigpt/openthaigpt-1.0.0-alpha-7b-chat-ggml<br>
**Weight (Quantized 4bit GGML)**: https://huggingface.co/openthaigpt/openthaigpt-1.0.0-alpha-7b-chat-ggml-q4


## Sponsors
Pantip.com, ThaiSC<br>
<img src="https://1173516064-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvvbWvIIe82Iv1yHaDBC5%2Fuploads%2FiWjRxBQgo0HUDcpZKf6A%2Fimage.png?alt=media&token=4fef4517-0b4d-46d6-a5e3-25c30c8137a6" width="100px">
<img src="https://1173516064-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvvbWvIIe82Iv1yHaDBC5%2Fuploads%2Ft96uNUI71mAFwkXUtxQt%2Fimage.png?alt=media&token=f8057c0c-5c5f-41ac-bb4b-ad02ee3d4dc2" width="100px">

### Powered by
OpenThaiGPT Volunteers, Artificial Intelligence Entrepreneur Association of Thailand (AIEAT), and Artificial Intelligence Association of Thailand (AIAT)

<img src="https://1173516064-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvvbWvIIe82Iv1yHaDBC5%2Fuploads%2F6yWPXxdoW76a4UBsM8lw%2Fimage.png?alt=media&token=1006ee8e-5327-4bc0-b9a9-a02e93b0c032" width="100px">
<img src="https://1173516064-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvvbWvIIe82Iv1yHaDBC5%2Fuploads%2FBwsmSovEIhW9AEOlHTFU%2Fimage.png?alt=media&token=5b550289-e9e2-44b3-bb8f-d3057d74f247" width="100px">

### Authors
* Kobkrit Viriyayudhakorn (kobkrit@aieat.or.th)
* Sumeth Yuenyong (sumeth.yue@mahidol.edu)
* Thaweewat Rugsujarit (thaweewr@scg.com)
* Jillaphat Jaroenkantasima (autsadang41@gmail.com)
* Norapat Buppodom (new@norapat.com)
* Koravich Sangkaew (kwankoravich@gmail.com)
* Peerawat Rojratchadakorn (peerawat.roj@gmail.com)
* Surapon Nonesung (nonesungsurapon@gmail.com)
* Chanon Utupon (chanon.utupon@gmail.com)
* Sadhis Wongprayoon (sadhis.tae@gmail.com)
* Nucharee Thongthungwong (nuchhub@hotmail.com)
* Chawakorn Phiantham (mondcha1507@gmail.com)
* Patteera Triamamornwooth (patt.patteera@gmail.com)
* Nattarika Juntarapaoraya (natt.juntara@gmail.com)
* Kriangkrai Saetan (kraitan.ss21@gmail.com)
* Pitikorn Khlaisamniang (pitikorn32@gmail.com)

<i>Disclaimer: Provided responses are not guaranteed.</i>
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_openthaigpt__openthaigpt-1.0.0-alpha-7b-chat-ckpt-hf)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 42.05   |
| ARC (25-shot)         | 50.85          |
| HellaSwag (10-shot)   | 74.89    |
| MMLU (5-shot)         | 40.02         |
| TruthfulQA (0-shot)   | 47.23   |
| Winogrande (5-shot)   | 69.06   |
| GSM8K (5-shot)        | 3.87        |
| DROP (3-shot)         | 8.42         |
