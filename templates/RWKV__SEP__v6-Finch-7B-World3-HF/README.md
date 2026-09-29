---
license: apache-2.0
---
### Huggingface RWKV Finch 7B World 3 Model

> HF compatible model for Finch-7B World 3.

![Finch Bird](./imgs/finch.jpg)


> **! Important Note !**
>
> The following is the HF transformers implementation of the Finch 7B World 3 model. This is meant to be used with the huggingface transformers
>
>


## Quickstart with the hugging face transformer library

```
model = AutoModelForCausalLM.from_pretrained("RWKV/v6-Finch-7B-World3-HF", trust_remote_code=True).to(torch.float32)
tokenizer = AutoTokenizer.from_pretrained("RWKV/v6-Finch-7B-World3-HF", trust_remote_code=True)
```

## Evaluation

The following demonstrates the improvements from Eagle 7B to Finch 14B

|  | [Eagle 7B](https://huggingface.co/RWKV/v6-Finch-7B-HF) | [Finch 7B](https://huggingface.co/RWKV/v6-Finch-7B-HF) | [Finch 14B](https://huggingface.co/RWKV/v6-Finch-14B-HF) |
| --- | --- | --- | --- |
| [ARC](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/arc) | 39.59% | 41.47% | 46.33% |
| [HellaSwag](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/hellaswag) | 53.09% | 55.96% | 57.69% |
| [MMLU](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/mmlu) | 30.86% | 41.70% | 56.05% |
| [Truthful QA](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/truthfulqa) | 33.03% | 34.82% | 39.27% |
| [Winogrande](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/winogrande) | 67.56% | 71.19% | 74.43% |

#### Running on CPU via HF transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_prompt(instruction, input=""):
    instruction = instruction.strip().replace('\r\n','\n').replace('\n\n','\n')
    input = input.strip().replace('\r\n','\n').replace('\n\n','\n')
    if input:
        return f"""Instruction: {instruction}

Input: {input}

Response:"""
    else:
        return f"""User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: {instruction}

Assistant:"""


model = AutoModelForCausalLM.from_pretrained("RWKV/v6-Finch-7B-World3-HF", trust_remote_code=True).to(torch.float32)
tokenizer = AutoTokenizer.from_pretrained("RWKV/v6-Finch-7B-World3-HF", trust_remote_code=True)

text = "请介绍北京的旅游景点"
prompt = generate_prompt(text)

inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(inputs["input_ids"], max_new_tokens=333, do_sample=True, temperature=1.0, top_p=0.3, top_k=0, )
print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))
```

output:

```shell
User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: 请介绍北京的旅游景点

Assistant: 北京是中国的首都，拥有众多的旅游景点，以下是其中一些著名的景点：
1. 故宫：位于北京市中心，是明清两代的皇宫，内有大量的文物和艺术品。
2. 天安门广场：是中国最著名的广场之一，是中国人民政治协商会议的旧址，也是中国人民政治协商会议的中心。
3. 颐和园：是中国古代皇家园林之一，有着悠久的历史和丰富的文化内涵。
4. 长城：是中国古代的一道长城，全长约万里，是中国最著名的旅游景点之一。
5. 北京大学：是中国著名的高等教育机构之一，有着悠久的历史和丰富的文化内涵。
6. 北京动物园：是中国最大的动物园之一，有着丰富的动物资源和丰富的文化内涵。
7. 故宫博物院：是中国最著名的博物馆之一，收藏了大量的文物和艺术品，是中国最重要的文化遗产之一。
8. 天坛：是中国古代皇家
```

#### Running on GPU via HF transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_prompt(instruction, input=""):
    instruction = instruction.strip().replace('\r\n','\n').replace('\n\n','\n')
    input = input.strip().replace('\r\n','\n').replace('\n\n','\n')
    if input:
        return f"""Instruction: {instruction}

Input: {input}

Response:"""
    else:
        return f"""User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: {instruction}

Assistant:"""


model = AutoModelForCausalLM.from_pretrained("RWKV/v6-Finch-7B-World3-HF", trust_remote_code=True, torch_dtype=torch.float16).to(0)
tokenizer = AutoTokenizer.from_pretrained("RWKV/v6-Finch-7B-World3-HF", trust_remote_code=True)

text = "介绍一下大熊猫"
prompt = generate_prompt(text)

inputs = tokenizer(prompt, return_tensors="pt").to(0)
output = model.generate(inputs["input_ids"], max_new_tokens=128, do_sample=True, temperature=1.0, top_p=0.3, top_k=0, )
print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))
```

output:

```shell
User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: 介绍一下大熊猫

Assistant: 大熊猫是一种中国特有的哺乳动物，也是中国的国宝之一。它们的外貌特征是圆形的黑白相间的身体，有着黑色的毛发和白色的耳朵。大熊猫的食物主要是竹子，它们会在竹林中寻找竹子，并且会将竹子放在竹笼中进行储存。大熊猫的寿命约为20至30年，但由于栖息地的丧失和人类活动的
```

#### Batch Inference

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_prompt(instruction, input=""):
    instruction = instruction.strip().replace('\r\n', '\n').replace('\n\n', '\n')
    input = input.strip().replace('\r\n', '\n').replace('\n\n', '\n')
    if input:
        return f"""Instruction: {instruction}

Input: {input}

Response:"""
    else:
        return f"""User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: {instruction}

Assistant:"""

model = AutoModelForCausalLM.from_pretrained("RWKV/v6-Finch-7B-2411-World3-HF", trust_remote_code=True).to(torch.float32)
tokenizer = AutoTokenizer.from_pretrained("RWKV/v6-Finch-7B-2411-World3-HF", trust_remote_code=True)

texts = ["请介绍北京的旅游景点", "介绍一下大熊猫", "乌兰察布"]
prompts = [generate_prompt(text) for text in texts]

inputs = tokenizer(prompts, return_tensors="pt", padding=True)
outputs = model.generate(inputs["input_ids"], max_new_tokens=128, do_sample=True, temperature=1.0, top_p=0.3, top_k=0, )

for output in outputs:
    print(tokenizer.decode(output.tolist(), skip_special_tokens=True))

```

output:

```shell
User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: 请介绍北京的旅游景点

Assistant: 北京是中国的首都，拥有丰富的旅游资源和历史文化遗产。以下是一些北京的旅游景点：
1. 故宫：位于北京市中心，是明清两代的皇宫，是中国最大的古代宫殿建筑群之一。
2. 天安门广场：位于北京市中心，是中国最著名的城市广场之一，也是中国最大的城市广场。
3. 颐和
User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: 介绍一下大熊猫

Assistant: 大熊猫是一种生活在中国中部地区的哺乳动物，也是中国的国宝之一。它们的外貌特征是圆形的黑白相间的身体，有着黑色的毛发和圆圆的眼睛。大熊猫是一种濒危物种，目前只有在野外的几个保护区才能看到它们的身影。大熊猫的食物主要是竹子，它们会在竹子上寻找食物，并且可以通
User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: 乌兰察布

Assistant: 乌兰察布是中国新疆维吾尔自治区的一个县级市，位于新疆维吾尔自治区中部，是新疆的第二大城市。乌兰察布市是新疆的第一大城市，也是新疆的重要城市之一。乌兰察布市是新疆的经济中心，也是新疆的重要交通枢纽之一。乌兰察布市的人口约为2.5万人，其中汉族占绝大多数。乌
```

## Links
- [Our wiki](https://wiki.rwkv.com)
- [Recursal.AI Cloud Platform](https://recursal.ai)
- [Featherless Inference](https://featherless.ai/models/RWKV/Finch-14B)
- [Blog article, detailing our model launch](https://blog.rwkv.com/p/rwkv-v6-finch-7b-world3)

## Acknowledgement
We are grateful for the help and support from the following key groups:

- [Recursal.ai](https://recursal.ai) team for financing the GPU resources, and managing the training of this foundation model - you can run the Finch line of RWKV models on their cloud / on-premise platform today.
- EleutherAI for their support, especially in the v5/v6 Eagle/Finch paper
- Linux Foundation AI & Data group for supporting and hosting the RWKV project