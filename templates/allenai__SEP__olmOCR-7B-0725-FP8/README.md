---
language:
- en
license: apache-2.0
datasets:
- allenai/olmOCR-mix-0225
base_model:
- Qwen/Qwen2.5-VL-7B-Instruct
library_name: transformers
new_version: allenai/olmOCR-7B-0825-FP8
---

<img alt="olmOCR Logo" src="https://huggingface.co/datasets/allenai/blog-images/resolve/main/olmocr/olmocr.png" width="242px" style="margin-left:'auto' margin-right:'auto' display:'block'">

# olmOCR-7B-0725-FP8

Quantized to FP8 Version of [olmOCR-7B-0725](https://huggingface.co/allenai/olmOCR-7B-0725), using llmcompressor.

This is a release of the olmOCR model that's fine tuned from Qwen2.5-VL-7B-Instruct using the 
[olmOCR-mix-0225](https://huggingface.co/datasets/allenai/olmOCR-mix-0225) dataset.

Quick links:
- 📃 [Paper](https://olmocr.allenai.org/papers/olmocr.pdf)
- 🤗 [Dataset](https://huggingface.co/datasets/allenai/olmOCR-mix-0225)
- 🛠️ [Code](https://github.com/allenai/olmocr)
- 🎮 [Demo](https://olmocr.allenai.org/)

The best way to use this model is via the [olmOCR toolkit](https://github.com/allenai/olmocr).
The toolkit comes with an efficient inference setup via sglang that can handle millions of documents
at scale.

## Usage

This model expects as input a single document image, rendered such that the longest dimension is 1288 pixels.

The prompt must then contain the additional metadata from the document, and the easiest way to generate this
is to use the methods provided by the [olmOCR toolkit](https://github.com/allenai/olmocr).


## License and use

olmOCR is licensed under the Apache 2.0 license.
olmOCR is intended for research and educational use.
For more information, please see our [Responsible Use Guidelines](https://allenai.org/responsible-use).