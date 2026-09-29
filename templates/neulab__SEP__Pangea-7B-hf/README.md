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

### Uses
The hf version is intended so that you could use Pangea-7B with the huggingface generate function.
If you want to use it with the Llava-Next codebase, please refer to our [original checkpoint](https://huggingface.co/neulab/Pangea-7B).

```python
# Assuming that you have text_input and image_path
from transformers import LlavaNextForConditionalGeneration, AutoProcessor
import torch
from PIL import Image

image_input = Image.open(image_path)

model = LlavaNextForConditionalGeneration.from_pretrained(
            "neulab/Pangea-7B-hf", 
            torch_dtype=torch.float16
        ).to(0)
processor = AutoProcessor.from_pretrained("neulab/Pangea-7B-hf")
model.resize_token_embeddings(len(processor.tokenizer))

text_input = f"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n<image>\n{text_input}<|im_end|>\n<|im_start|>assistant\n"
model_inputs = processor(images=image_input, text=text_input, return_tensors='pt').to("cuda", torch.float16)
output = model.generate(**model_inputs, max_new_tokens=1024, min_new_tokens=32, temperature=1.0, top_p=0.9, do_sample=True)
output = output[0]
result = processor.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=False)

print(result)
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