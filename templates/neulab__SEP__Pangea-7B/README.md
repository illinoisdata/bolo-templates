---
license: apache-2.0
datasets:
- neulab/PangeaInstruct
language:
- am
- ar
- bg
- bn
- cs
- de
- el
- en
- es
- fa
- fr
- ga
- hi
- id
- ig
- it
- iw
- ja
- jv
- ko
- nl
- mn
- ms
- no
- pl
- pt
- ro
- ru
- si
- su
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
base_model:
- Qwen/Qwen2-7B-Instruct
---
# Pangea-7B Model Card

[Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://neulab.github.io/Pangea/)

🇪🇹 🇸🇦 🇧🇬 🇧🇩 🇨🇿 🇩🇪 🇬🇷 🇬🇧 🇺🇸 🇪🇸 🇮🇷 🇫🇷 🇮🇪 🇮🇳 🇮🇩 🇳🇬 🇮🇹 🇮🇱 🇯🇵 🇮🇩 🇰🇷 🇳🇱 🇲🇳 🇲🇾 🇳🇴 🇵🇱 🇵🇹 🇧🇷 🇷🇴 🇷🇺 🇱🇰 🇮🇩 🇰🇪 🇹🇿 🇱🇰 🇹🇭 🇹🇷 🇺🇦 🇵🇰 🇻🇳 🇨🇳 🇹🇼

[🏠 Homepage](https://neulab.github.io/Pangea/) | [🤖 Pangea-7B](https://huggingface.co/neulab/Pangea-7B) | [📊 PangeaIns](https://huggingface.co/datasets/neulab/PangeaInstruct) | [🧪 PangeaBench](https://huggingface.co/collections/neulab/pangea-6713c3b0d78a453906eb2ed8) | [💻 Github](https://github.com/neulab/Pangea/tree/main) | [📄 Arxiv](https://arxiv.org/abs/2410.16153) | [📕 PDF](https://arxiv.org/pdf/2410.16153) | [🖥️ Demo](https://huggingface.co/spaces/neulab/Pangea)

<img src="https://cdn-uploads.huggingface.co/production/uploads/6230d750d93e84e233882dbc/ZjVTKnIsyshWpo-PWg9gM.png" alt="description" style="width:300px;">


## Model details

 - **Model:** Pangea is a fully open-source Multilingual Multimodal Multicultural LLM.
 - **Date:** Pangea-7B was trained in 2024.
 - **Training Dataset:** [6M PangeaIns](https://huggingface.co/datasets/neulab/PangeaInstruct).
 - **Architecture:** Pangea-7B follows the architecture of [LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT), with a [Qwen2-7B-Instruct](https://huggingface.co/Qwen/Qwen2-7B-Instruct) backbone.

## Uses

Pangea-7B follows the architecture of [LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT). 

You could either (1) follow the same model loading procedures as of [LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT), an example of loading Pangea-7B directly is shown in the Python code below, or (2) use our hf version of Pangea-7B: [Pangea-7B-hf]https://huggingface.co/neulab/Pangea-7B-hf

### Direct Use
First you would need to clone and install [LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT).

```bash
git clone https://github.com/LLaVA-VL/LLaVA-NeXT
cd LLaVA-NeXT
pip install -e ".[train]"
```

Then, you could load Pangea-7B using the following code:
```python
from llava.model.builder import load_pretrained_model
model_path = 'neulab/Pangea-7B'
model_name = 'Pangea-7B-qwen'
args = {"multimodal": True}
tokenizer, model, image_processor, context_len = load_pretrained_model(model_path, None, model_name, **args)
```

Defining some helper functions for using the model:
```python
import torch
from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
from llava.utils import disable_torch_init
from llava.constants import IGNORE_INDEX, DEFAULT_IMAGE_TOKEN, IMAGE_TOKEN_INDEX
from typing import Dict
import transformers
import re
from PIL import Image

def preprocess_qwen(sources, tokenizer: transformers.PreTrainedTokenizer, has_image: bool = False, max_len=2048, system_message: str = "You are a helpful assistant.") -> Dict:
    roles = {"human": "<|im_start|>user", "gpt": "<|im_start|>assistant"}
    im_start, im_end = tokenizer.additional_special_tokens_ids
    nl_tokens = tokenizer("\n").input_ids
    _system = tokenizer("system").input_ids + nl_tokens
    _user = tokenizer("user").input_ids + nl_tokens
    _assistant = tokenizer("assistant").input_ids + nl_tokens
    input_ids = []
    source = sources
    if roles[source[0]["from"]] != roles["human"]: source = source[1:]
    input_id, target = [], []
    system = [im_start] + _system + tokenizer(system_message).input_ids + [im_end] + nl_tokens
    input_id += system
    target += [im_start] + [IGNORE_INDEX] * (len(system) - 3) + [im_end] + nl_tokens
    assert len(input_id) == len(target)
    for j, sentence in enumerate(source):
        role = roles[sentence["from"]]
        if has_image and sentence["value"] is not None and "<image>" in sentence["value"]:
            num_image = len(re.findall(DEFAULT_IMAGE_TOKEN, sentence["value"]))
            texts = sentence["value"].split('<image>')
            _input_id = tokenizer(role).input_ids + nl_tokens 
            for i,text in enumerate(texts):
                _input_id += tokenizer(text).input_ids 
                if i<len(texts)-1: _input_id += [IMAGE_TOKEN_INDEX] + nl_tokens
            _input_id += [im_end] + nl_tokens
            assert sum([i==IMAGE_TOKEN_INDEX for i in _input_id])==num_image
        else:
            if sentence["value"] is None: _input_id = tokenizer(role).input_ids + nl_tokens
            else: _input_id = tokenizer(role).input_ids + nl_tokens + tokenizer(sentence["value"]).input_ids + [im_end] + nl_tokens
        input_id += _input_id
    input_ids.append(input_id)
    return torch.tensor(input_ids, dtype=torch.long)

def generate_output(prompt, image=None, do_sample=False, temperature=0, top_p=0.5, num_beams=1, max_new_tokens=1024):
    image_tensors = []
    prompt = "<image>\n" + prompt
    image = Image.open(image)
    image_tensor = image_processor.preprocess(image, return_tensors='pt')['pixel_values']
    image_tensors.append(image_tensor.half().cuda())
    input_ids = preprocess_qwen([{'from': 'human', 'value': prompt},{'from': 'gpt','value': None}], tokenizer, has_image=True).cuda()
    with torch.inference_mode():
        output_ids = model.generate(
            input_ids,
            images=image_tensors,
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            num_beams=num_beams,
            max_new_tokens=max_new_tokens,
            use_cache=True
        )
    outputs = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
    outputs = outputs.strip()
    return outputs
```

Now, an example of using the model:
```python
prompt = "What did you see in the image?"
image = "image.png"
print(generate_output(prompt, image=image))
```

Note that the example above demonstrates multimodal usage. To use the model with text-only inputs, you would need to reload the model with :
```python
args = {"multimodal": True}
tokenizer, model, _, context_len = load_pretrained_model(model_path, None, model_name, **args)

def generate_output_text_only(prompt, do_sample=False, temperature=0, top_p=0.5, num_beams=1, max_new_tokens=1024):
    input_ids = preprocess_qwen([{'from': 'human', 'value': prompt},{'from': 'gpt','value': None}], tokenizer, has_image=False).cuda()
    with torch.inference_mode():
        generated_ids = model.generate(
            input_ids,
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            num_beams=num_beams,
            max_new_tokens=max_new_tokens,
            use_cache=True
        )
    generated_ids = [output_ids[len(input_ids) :] for input_ids, output_ids in zip(input_ids, generated_ids)]
    outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    outputs = outputs.strip()
    return outputs

prompt = "Write me a python function that could sort a input integer list by descending order"
print(generate_output_text_only(prompt))
```
## Citing the Model

**BibTeX Citation:**

```
@article{yue2024pangeafullyopenmultilingual,
  title={Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages},
  author={Xiang Yue and Yueqi Song and Akari Asai and Seungone Kim and Jean de Dieu Nyandwi and Simran Khanuja and Anjali Kantharuban and Lintang Sutawika and Sathyanarayanan Ramamoorthy and Graham Neubig},
  year={2024},
  journal={arXiv preprint arXiv:2410.16153},
  url={https://arxiv.org/abs/2410.16153}
}
```