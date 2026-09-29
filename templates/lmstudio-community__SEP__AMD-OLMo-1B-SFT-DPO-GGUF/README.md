---
base_model: amd/AMD-OLMo-1B-SFT-DPO
datasets:
- allenai/dolma
license: apache-2.0
pipeline_tag: text-generation
quantized_by: bartowski
---
## 💫 Community Model> AMD OLMo 1B SFT DPO by Amd

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [amd](https://huggingface.co/amd)<br>
**Original model**: [AMD-OLMo-1B-SFT-DPO](https://huggingface.co/amd/AMD-OLMo-1B-SFT-DPO)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b3991](https://github.com/ggerganov/llama.cpp/releases/tag/b3991)<br>

## Technical Details

AMD-OLMo-1B is based on the model architecture and training set up of fully open source 1 billion version of OLMo-1B

Context length of 2048

Vocab size of 50,280

Pretrained on 1.3 trillion tokens from https://huggingface.co/datasets/allenai/dolma

Supervised fine-tuned (SFT) on [Tulu V2](https://huggingface.co/datasets/allenai/tulu-v2-sft-mixture) dataset (1st phase) and then [OpenHermes-2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5), [WebInstructSub](https://huggingface.co/datasets/TIGER-Lab/WebInstructSub), and [Code-Feedback](https://huggingface.co/datasets/m-a-p/Code-Feedback) datasets (2nd phase).

Aligned with human preferences using Direct Preference Optimization (DPO) on [UltraFeedback](https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences-cleaned) dataset.

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.