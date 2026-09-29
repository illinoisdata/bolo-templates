---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/blob/main/LICENSE
language:
- ja
- en
tags:
- vila
- nvila
- conversational
- multimodal
base_model:
- Qwen/Qwen2.5-0.5B-Instruct
- Efficient-Large-Model/paligemma-siglip-so400m-patch14-448
pipeline_tag: image-text-to-text
---
# Heron-NVILA-Lite-1B-hf

Heron-NVILA-Lite-1B-hf is a vision language model trained for Japanese, based on the [NVILA](https://arxiv.org/abs/2412.04468)-Lite architecture.
This implementation is compatible with [transformers.AutoModelForImageTextToText](https://huggingface.co/docs/transformers/main/en/tasks/image_text_to_text).

## Model Overview

* **Developer**: [Turing Inc.](https://www.turing-motors.com/)
* **Vision Encoder**: [paligemma-siglip-so400m-patch14-448](https://huggingface.co/Efficient-Large-Model/paligemma-siglip-so400m-patch14-448)
* **Projector**: mlp_downsample_2x2_fix
* **LLM**: [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)
* **Supported Languages**: Japanese, English

## Setup

```bash
# We have developed this implementation with `transformers==4.57.1`. Other versions of transformers may also work, but we have not tested them.
pip install "transformers[torch]==4.57.1" pillow
```

## Usage

```python
from transformers import AutoConfig, AutoModelForImageTextToText, AutoProcessor

MODEL_NAME = "turing-motors/Heron-NVILA-Lite-1B-hf"

# you can use config
config = AutoConfig.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForImageTextToText.from_config(config, trust_remote_code=True)

# or directly from_pretrained
model = AutoModelForImageTextToText.from_pretrained(MODEL_NAME, trust_remote_code=True, device_map="auto")

# load processor
processor = AutoProcessor.from_pretrained(MODEL_NAME, trust_remote_code=True)

# show chat_template
print(processor.tokenizer.chat_template)

def generate_content(content: str, images: list | None = None, **kwargs) -> str:
    conversation = [{"role": "user", "content": content}]
    text = processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=False)
    encoding = processor(text=text, images=images, return_tensors="pt").to(model.device)
    output = model.generate(**encoding, **kwargs)
    return processor.decode(output[0, len(encoding["input_ids"][0]):], skip_special_tokens=True)

# examples generate with raw text
response = generate_content("こんにちは")
print(response)
print("---" * 40)

# examples generate with text + image
from PIL import Image
import requests
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
response = generate_content("<image>\n画像を説明してください。", images=[image])
print(response)
print("---" * 40)

# examples generate using generation_config
from PIL import Image
import requests
from transformers import GenerationConfig
generation_config = {
    "max_new_tokens": 512,
    "temperature": 0.5,
    "do_sample": True,
}
generation_config = GenerationConfig(**generation_config)
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
response = generate_content(
    "<image>\n画像を説明してください。",
    images=[image],
    generation_config=generation_config
)
print(response)
print("---" * 40)

# examples generate with text + image + text + image + text
from PIL import Image
import requests
url_list = [
    "https://images.unsplash.com/photo-1694831404826-3400c48c188d?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1693240876439-473af88b4ed7?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
]
images = [
   Image.open(requests.get(url, stream=True).raw).convert("RGB") for url in url_list
]
response = generate_content("".join([
    "<image>\n",
    "これは日本の画像です",
    "<image>\n",
    "これはオーストリアの画像です",
    "各画像の違いを説明して"]), images)
print(response)
print("---" * 40)
```

## Training Summary

| Stage  | Training                      | Data Sources                  | Samples     |
|--------|-------------------------------|-------------------------------|-------------|
| Stage1 | Projector                     | [Japanese image text pairs](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-japanese-image-text-pairs), [LLaVA-Pretrain](https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain)                          | 1.1M      |
| Stage2 | Projector, LLM                | Filtered [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) (CC-MAIN-2024-46, CC-MAIN-2024-51, CC-MAIN-2025-05)  | 13M     |
|        |                               | [Japanese image text pairs (subset)](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-japanese-image-text-pairs), [Japanese interleaved data (subset)](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-japanese-interleaved-data), [mmc4-core (subset)](https://github.com/allenai/mmc4), [coyo-700m (subset)](https://huggingface.co/datasets/kakaobrain/coyo-700m), [wikipedia_ja](https://huggingface.co/datasets/turing-motors/Wikipedia-Vision-JA), [llava_pretrain_ja](https://huggingface.co/datasets/turing-motors/LLaVA-Pretrain-JA), [stair_captions](http://captions.stair.center/)  | 20M     |
| Stage3 | Vision Encoder, Projector, LLM | [llava-instruct-v1_5-en-subset-358k](https://huggingface.co/datasets/llm-jp/llava-instruct-v1_5-en-subset-358k), [llava-instruct-ja](https://huggingface.co/datasets/llm-jp/llava-instruct-ja), [japanese-photos-conv](https://huggingface.co/datasets/llm-jp/japanese-photos-conversation), [ja-vg-vqa](https://huggingface.co/datasets/llm-jp/ja-vg-vqa-conversation), [synthdog-ja (subset)](https://huggingface.co/datasets/naver-clova-ix/synthdog-ja), [ai2d](https://huggingface.co/datasets/lmms-lab/ai2d), [synthdog-en](https://huggingface.co/datasets/naver-clova-ix/synthdog-en), [sherlock](https://github.com/allenai/sherlock)    | 1.1M      |

## Evaluation

I used [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) for this evaluation. Scores for models other than Heron-NVILA-Lite and Sarashina2-Vision-14B were taken from [llm-jp-eval-mm leaderboard](https://llm-jp.github.io/llm-jp-eval-mm/) as of March 2025 and the [Asagi website](https://uehara-mech.github.io/asagi-vlm?v=1). Heron-NVILA-Lite and Sarashina2-Vision-14B were evaluated using llm-as-a-judge with "gpt-4o-2024-05-13". Sarashina2-Vision-14B was evaluated on the [official blog](https://www.sbintuitions.co.jp/blog/entry/2025/03/17/111703) using "gpt-4o-2024-08-06"; please note that due to differing evaluation conditions, the results for Sarashina2-Vision-14B should be treated as reference only.


| Model                          | LLM Size | Heron-Bench overall LLM (%) | JA-VLM-Bench-In-the-Wild LLM (/5.0) | JA-VG-VQA-500 LLM (/5.0) |
|--------------------------------|----------|------------------------------|-------------------------------------|--------------------------|
| **Heron-NVILA-Lite-1B**        | 0.5B     | 45.9                         | 2.92                                | 3.16                     |
| **[Heron-NVILA-Lite-2B](https://huggingface.co/turing-motors/Heron-NVILA-Lite-2B)**        | 1.5B     | 52.8                         | 3.52                                | 3.50                     |
| **[Heron-NVILA-Lite-15B](https://huggingface.co/turing-motors/Heron-NVILA-Lite-15B)**       | 14B      | 59.6                         | 4.2                                 | 3.82                     |
| [LLaVA-CALM2-SigLIP](https://huggingface.co/cyberagent/llava-calm2-siglip)             | 7B      | 43.3                        | 3.15                                | 3.21                     |
| [Llama-3-EvoVLM-JP-v2](https://huggingface.co/SakanaAI/Llama-3-EvoVLM-JP-v2)           | 8B      | 39.3                        | 2.92                                | 2.96                     |
| [VILA-jp](https://huggingface.co/llm-jp/llm-jp-3-vila-14b)                        | 13B     | 57.2                        | 3.69                                | 3.62                     |
| [Asagi-14B](https://huggingface.co/MIL-UT/Asagi-14B)                      | 13B     | 55.8                        | 3.44                                | 3.84                     |
| [Sarashina2-Vision-14B](https://huggingface.co/sbintuitions/sarashina2-vision-14b)                      | 13B     | 50.9                        | 4.1                                | 3.43                     |
| [Qwen2-VL 7B Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)                         | 7B       | 55.5                        | 3.61                                | 3.6                     |
| GPT-4o                         | -       | 87.6                        | 3.85                                | 3.58                     |

## Risks and Limitations

This model is experimental and has not been thoroughly calibrated for ethical compliance or legal standards. Caution is advised for sensitive applications.

## License

- Model weights are licensed under [Apache License 2.0](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/blob/main/LICENSE).
- Users must comply with  [OpenAI terms of use](https://openai.com/policies/terms-of-use) due to the inclusion of GPT-4-generated synthetic data.

## Acknowledgements

This model is based on results obtained from a project, JPNP20017, subsidized by the New Energy and Industrial Technology Development Organization (NEDO).

I would like to acknowledge the use of the following open-source repositories:

- [VILA](https://github.com/NVlabs/VILA)
- [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm)