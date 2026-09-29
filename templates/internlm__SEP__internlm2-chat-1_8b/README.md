---
pipeline_tag: text-generation
license: other
---
# InternLM 

<div align="center">

<img src="https://github.com/InternLM/InternLM/assets/22529082/b9788105-8892-4398-8b47-b513a292378e" width="200"/>
  <div>&nbsp;</div>
  <div align="center">
    <b><font size="5">InternLM</font></b>
    <sup>
      <a href="https://internlm.intern-ai.org.cn/">
        <i><font size="4">HOT</font></i>
      </a>
    </sup>
    <div>&nbsp;</div>
  </div>

[![evaluation](https://github.com/InternLM/InternLM/assets/22529082/f80a2a58-5ddf-471a-8da4-32ab65c8fd3b)](https://github.com/internLM/OpenCompass/)

[💻Github Repo](https://github.com/InternLM/InternLM) • [🤔Reporting Issues](https://github.com/InternLM/InternLM/issues/new) • [📜Technical Report](https://arxiv.org/abs/2403.17297)

</div>


## Introduction
InternLM2-1.8B is the 1.8 billion parameter version of the second generation InternLM series. In order to facilitate user use and research, InternLM2-1.8B has three versions of open-source models. They are:

- InternLM2-1.8B: Foundation models with high quality and high adaptation flexibility, which serve as a good starting point for downstream deep adaptations.
- InternLM2-Chat-1.8B-SFT: Chat model after supervised fine-tuning (SFT) on InternLM2-1.8B. 
- InternLM2-Chat-1.8B: Further aligned on top of InternLM2-Chat-1.8B-SFT through online RLHF. InternLM2-Chat-1.8B exhibits better instruction following, chat experience, and function calling, which is recommended for downstream applications.

The InternLM2 has the following technical features:

- Effective support for ultra-long contexts of up to 200,000 characters: The model nearly perfectly achieves "finding a needle in a haystack" in long inputs of 200,000 characters. It also leads among open-source models in performance on long-text tasks such as LongBench and L-Eval.
- Comprehensive performance enhancement: Compared to the previous generation model, it shows significant improvements in various capabilities, including reasoning, mathematics, and coding.


## InternLM2-1.8B

### Performance Evaluation

We have evaluated InternLM2 on several important benchmarks using the open-source evaluation tool [OpenCompass](https://github.com/open-compass/opencompass). Some of the evaluation results are shown in the table below. You are welcome to visit the [OpenCompass Leaderboard](https://rank.opencompass.org.cn) for more evaluation results.

| Dataset\Models | InternLM2-1.8B | InternLM2-Chat-1.8B-SFT | InternLM2-7B | InternLM2-Chat-7B |
| :---: | :---: | :---: | :---: | :---: |
| MMLU | 46.9 | 47.1 | 65.8 | 63.7 |
| AGIEval | 33.4 | 38.8 | 49.9 | 47.2 |
| BBH | 37.5 | 35.2 | 65.0 | 61.2 |
| GSM8K | 31.2 | 39.7 | 70.8 | 70.7 |
| MATH | 5.6 | 11.8 | 20.2 | 23.0 |
| HumanEval | 25.0 | 32.9 | 43.3 | 59.8 |
| MBPP(Sanitized) | 22.2 | 23.2 | 51.8 | 51.4 |


- The evaluation results were obtained from [OpenCompass](https://github.com/open-compass/opencompass) , and evaluation configuration can be found in the configuration files provided by [OpenCompass](https://github.com/open-compass/opencompass). 
- The evaluation data may have numerical differences due to the version iteration of [OpenCompass](https://github.com/open-compass/opencompass), so please refer to the latest evaluation results of [OpenCompass](https://github.com/open-compass/opencompass).



**Limitations:** Although we have made efforts to ensure the safety of the model during the training process and to encourage the model to generate text that complies with ethical and legal requirements, the model may still produce unexpected outputs due to its size and probabilistic generation paradigm. For example, the generated responses may contain biases, discrimination, or other harmful content. Please do not propagate such content. We are not responsible for any consequences resulting from the dissemination of harmful information.

### Import from Transformers

To load the InternLM2 1.8B Chat model using Transformers, use the following code:

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("internlm/internlm2-chat-1_8b", trust_remote_code=True)
# Set `torch_dtype=torch.float16` to load model in float16, otherwise it will be loaded as float32 and cause OOM Error.
model = AutoModelForCausalLM.from_pretrained("internlm/internlm2-chat-1_8b", torch_dtype=torch.float16, trust_remote_code=True).cuda()
model = model.eval()
response, history = model.chat(tokenizer, "hello", history=[])
print(response)
# Hello! How can I help you today?
response, history = model.chat(tokenizer, "please provide three suggestions about time management", history=history)
print(response)
```

The responses can be streamed using `stream_chat`:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "internlm/internlm2-chat-1_8b"
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, trust_remote_code=True).cuda()
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

model = model.eval()
length = 0
for response, history in model.stream_chat(tokenizer, "Hello", history=[]):
    print(response[length:], flush=True, end="")
    length = len(response)
```

## Deployment

### LMDeploy

LMDeploy is a toolkit for compressing, deploying, and serving LLM, developed by the MMRazor and MMDeploy teams.

```bash
pip install lmdeploy
```

You can run batch inference locally with the following python code:

```python
import lmdeploy
pipe = lmdeploy.pipeline("internlm/internlm2-chat-1_8b")
response = pipe(["Hi, pls intro yourself", "Shanghai is"])
print(response)
```

Or you can launch an OpenAI compatible server with the following command:

```bash
lmdeploy serve api_server internlm/internlm2-chat-1_8b --model-name internlm2-chat-1_8b --server-port 23333 
```

Then you can send a chat request to the server:

```bash
curl http://localhost:23333/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "internlm2-chat-1_8b",
    "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Introduce deep learning to me."}
    ]
    }'
```

Find more details in the [LMDeploy documentation](https://lmdeploy.readthedocs.io/en/latest/)

### vLLM

Launch OpenAI compatible server with `vLLM>=0.3.2`:

```bash
pip install vllm
```

```bash
python -m vllm.entrypoints.openai.api_server --model internlm/internlm2-chat-1_8b --served-model-name internlm2-chat-1_8b --trust-remote-code
```

Then you can send a chat request to the server:

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "internlm2-chat-1_8b",
    "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Introduce deep learning to me."}
    ]
    }'
```

Find more details in the [vLLM documentation](https://docs.vllm.ai/en/latest/index.html)

## Open Source License

The code is licensed under Apache-2.0, while model weights are fully open for academic research and also allow **free** commercial usage. To apply for a commercial license, please fill in the [application form (English)](https://wj.qq.com/s2/12727483/5dba/)/[申请表（中文）](https://wj.qq.com/s2/12725412/f7c1/). For other questions or collaborations, please contact <internlm@pjlab.org.cn>.

## Citation

```
@misc{cai2024internlm2,
      title={InternLM2 Technical Report},
      author={Zheng Cai and Maosong Cao and Haojiong Chen and Kai Chen and Keyu Chen and Xin Chen and Xun Chen and Zehui Chen and Zhi Chen and Pei Chu and Xiaoyi Dong and Haodong Duan and Qi Fan and Zhaoye Fei and Yang Gao and Jiaye Ge and Chenya Gu and Yuzhe Gu and Tao Gui and Aijia Guo and Qipeng Guo and Conghui He and Yingfan Hu and Ting Huang and Tao Jiang and Penglong Jiao and Zhenjiang Jin and Zhikai Lei and Jiaxing Li and Jingwen Li and Linyang Li and Shuaibin Li and Wei Li and Yining Li and Hongwei Liu and Jiangning Liu and Jiawei Hong and Kaiwen Liu and Kuikun Liu and Xiaoran Liu and Chengqi Lv and Haijun Lv and Kai Lv and Li Ma and Runyuan Ma and Zerun Ma and Wenchang Ning and Linke Ouyang and Jiantao Qiu and Yuan Qu and Fukai Shang and Yunfan Shao and Demin Song and Zifan Song and Zhihao Sui and Peng Sun and Yu Sun and Huanze Tang and Bin Wang and Guoteng Wang and Jiaqi Wang and Jiayu Wang and Rui Wang and Yudong Wang and Ziyi Wang and Xingjian Wei and Qizhen Weng and Fan Wu and Yingtong Xiong and Chao Xu and Ruiliang Xu and Hang Yan and Yirong Yan and Xiaogui Yang and Haochen Ye and Huaiyuan Ying and Jia Yu and Jing Yu and Yuhang Zang and Chuyu Zhang and Li Zhang and Pan Zhang and Peng Zhang and Ruijie Zhang and Shuo Zhang and Songyang Zhang and Wenjian Zhang and Wenwei Zhang and Xingcheng Zhang and Xinyue Zhang and Hui Zhao and Qian Zhao and Xiaomeng Zhao and Fengzhe Zhou and Zaida Zhou and Jingming Zhuo and Yicheng Zou and Xipeng Qiu and Yu Qiao and Dahua Lin},
      year={2024},
      eprint={2403.17297},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## 简介
书生·浦语-1.8B (InternLM2-1.8B) 是第二代浦语模型系列的18亿参数版本。为了方便用户使用和研究，书生·浦语-1.8B (InternLM2-1.8B) 共有三个版本的开源模型，他们分别是：

- InternLM2-1.8B: 具有高质量和高适应灵活性的基础模型，为下游深度适应提供了良好的起点。
- InternLM2-Chat-1.8B-SFT：在 InternLM2-1.8B 上进行监督微调 (SFT) 后得到的对话模型。
- InternLM2-Chat-1.8B：通过在线 RLHF 在 InternLM2-Chat-1.8B-SFT 之上进一步对齐。 InternLM2-Chat-1.8B表现出更好的指令跟随、聊天体验和函数调用，推荐下游应用程序使用。

InternLM2 模型具备以下的技术特点

- 有效支持20万字超长上下文：模型在20万字长输入中几乎完美地实现长文“大海捞针”，而且在 LongBench 和 L-Eval 等长文任务中的表现也达到开源模型中的领先水平。 
- 综合性能全面提升：各能力维度相比上一代模型全面进步，在推理、数学、代码等方面的能力提升显著。

## InternLM2-1.8B

### 性能评测

我们使用开源评测工具 [OpenCompass](https://github.com/internLM/OpenCompass/) 对 InternLM2 在几个重要的评测集进行了评测 ，部分评测结果如下表所示，欢迎访问[ OpenCompass 榜单 ](https://rank.opencompass.org.cn)获取更多的评测结果。

| 评测集 | InternLM2-1.8B | InternLM2-Chat-1.8B-SFT | InternLM2-7B | InternLM2-Chat-7B |
| :---: | :---: | :---: | :---: | :---: |
| MMLU | 46.9 | 47.1 | 65.8 | 63.7 |
| AGIEval | 33.4 | 38.8 | 49.9 | 47.2 |
| BBH | 37.5 | 35.2 | 65.0 | 61.2 |
| GSM8K | 31.2 | 39.7 | 70.8 | 70.7 |
| MATH | 5.6 | 11.8 | 20.2 | 23.0 |
| HumanEval | 25.0 | 32.9 | 43.3 | 59.8 |
| MBPP(Sanitized) | 22.2 | 23.2 | 51.8 | 51.4 |

- 以上评测结果基于 [OpenCompass](https://github.com/open-compass/opencompass) 获得（部分数据标注`*`代表数据来自原始论文），具体测试细节可参见 [OpenCompass](https://github.com/open-compass/opencompass) 中提供的配置文件。
- 评测数据会因 [OpenCompass](https://github.com/open-compass/opencompass) 的版本迭代而存在数值差异，请以 [OpenCompass](https://github.com/open-compass/opencompass) 最新版的评测结果为主。


**局限性：** 尽管在训练过程中我们非常注重模型的安全性，尽力促使模型输出符合伦理和法律要求的文本，但受限于模型大小以及概率生成范式，模型可能会产生各种不符合预期的输出，例如回复内容包含偏见、歧视等有害内容，请勿传播这些内容。由于传播不良信息导致的任何后果，本项目不承担责任。

### 通过 Transformers 加载

通过以下的代码加载 InternLM2 1.8B Chat 模型

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("internlm/internlm2-chat-1_8b", trust_remote_code=True)
# `torch_dtype=torch.float16` 可以令模型以 float16 精度加载，否则 transformers 会将模型加载为 float32，导致显存不足
model = AutoModelForCausalLM.from_pretrained("internlm/internlm2-chat-1_8b", torch_dtype=torch.float16, trust_remote_code=True).cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
# 你好！有什么我可以帮助你的吗？
response, history = model.chat(tokenizer, "请提供三个管理时间的建议。", history=history)
print(response)
```

如果想进行流式生成，则可以使用 `stream_chat` 接口：

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "internlm/internlm2-chat-1_8b"
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dype=torch.float16, trust_remote_code=True).cuda()
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

model = model.eval()
length = 0
for response, history in model.stream_chat(tokenizer, "你好", history=[]):
    print(response[length:], flush=True, end="")
    length = len(response)
```

## 部署

### LMDeploy

LMDeploy 由 MMDeploy 和 MMRazor 团队联合开发，是涵盖了 LLM 任务的全套轻量化、部署和服务解决方案。

```bash
pip install lmdeploy
```

你可以使用以下 python 代码进行本地批量推理:

```python
import lmdeploy
pipe = lmdeploy.pipeline("internlm/internlm2-chat-1_8b")
response = pipe(["Hi, pls intro yourself", "Shanghai is"])
print(response)
```

或者你可以使用以下命令启动兼容 OpenAI API 的服务:

```bash
lmdeploy serve api_server internlm/internlm2-chat-1_8b --server-port 23333
```

然后你可以向服务端发起一个聊天请求:

```bash
curl http://localhost:23333/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "internlm2-chat-1_8b",
    "messages": [
    {"role": "system", "content": "你是个友善的AI助手。"},
    {"role": "user", "content": "介绍一下深度学习。"}
    ]
    }'
```

更多信息请查看 [LMDeploy 文档](https://lmdeploy.readthedocs.io/en/latest/)

### vLLM

使用`vLLM>=0.3.2`启动兼容 OpenAI API 的服务:

```bash
pip install vllm
```

```bash
python -m vllm.entrypoints.openai.api_server --model internlm/internlm2-chat-1_8b --trust-remote-code
```

然后你可以向服务端发起一个聊天请求:

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "internlm2-chat-1_8b",
    "messages": [
    {"role": "system", "content": "你是个友善的AI助手。"},
    {"role": "user", "content": "介绍一下深度学习。"}
    ]
    }'
```

更多信息请查看 [vLLM 文档](https://docs.vllm.ai/en/latest/index.html)

## 开源许可证

本仓库的代码依照 Apache-2.0 协议开源。模型权重对学术研究完全开放，也可申请免费的商业使用授权（[申请表](https://wj.qq.com/s2/12725412/f7c1/)）。其他问题与合作请联系 <internlm@pjlab.org.cn>。

## 引用

```
@misc{cai2024internlm2,
      title={InternLM2 Technical Report},
      author={Zheng Cai and Maosong Cao and Haojiong Chen and Kai Chen and Keyu Chen and Xin Chen and Xun Chen and Zehui Chen and Zhi Chen and Pei Chu and Xiaoyi Dong and Haodong Duan and Qi Fan and Zhaoye Fei and Yang Gao and Jiaye Ge and Chenya Gu and Yuzhe Gu and Tao Gui and Aijia Guo and Qipeng Guo and Conghui He and Yingfan Hu and Ting Huang and Tao Jiang and Penglong Jiao and Zhenjiang Jin and Zhikai Lei and Jiaxing Li and Jingwen Li and Linyang Li and Shuaibin Li and Wei Li and Yining Li and Hongwei Liu and Jiangning Liu and Jiawei Hong and Kaiwen Liu and Kuikun Liu and Xiaoran Liu and Chengqi Lv and Haijun Lv and Kai Lv and Li Ma and Runyuan Ma and Zerun Ma and Wenchang Ning and Linke Ouyang and Jiantao Qiu and Yuan Qu and Fukai Shang and Yunfan Shao and Demin Song and Zifan Song and Zhihao Sui and Peng Sun and Yu Sun and Huanze Tang and Bin Wang and Guoteng Wang and Jiaqi Wang and Jiayu Wang and Rui Wang and Yudong Wang and Ziyi Wang and Xingjian Wei and Qizhen Weng and Fan Wu and Yingtong Xiong and Chao Xu and Ruiliang Xu and Hang Yan and Yirong Yan and Xiaogui Yang and Haochen Ye and Huaiyuan Ying and Jia Yu and Jing Yu and Yuhang Zang and Chuyu Zhang and Li Zhang and Pan Zhang and Peng Zhang and Ruijie Zhang and Shuo Zhang and Songyang Zhang and Wenjian Zhang and Wenwei Zhang and Xingcheng Zhang and Xinyue Zhang and Hui Zhao and Qian Zhao and Xiaomeng Zhao and Fengzhe Zhou and Zaida Zhou and Jingming Zhuo and Yicheng Zou and Xipeng Qiu and Yu Qiao and Dahua Lin},
      year={2024},
      eprint={2403.17297},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
