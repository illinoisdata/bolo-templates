---
language:
- ja
tags:
- sentence-similarity
- feature-extraction
base_model: cl-nagoya/ruri-pt-small
widget: []
pipeline_tag: sentence-similarity
license: apache-2.0
datasets:
- cl-nagoya/ruri-dataset-ft
---

# Ruri: Japanese General Text Embeddings

**Notes: v3 models are out!**  
We recommend using the following v3 models going forward.

|ID| #Param.|Max Len.|Avg. JMTEB|
|-|-|-|-|
|[cl-nagoya/ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m)|37M|8192|74.51|
|[cl-nagoya/ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m)|70M|8192|75.48|
|[cl-nagoya/ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m)|132M|8192|76.55|
|[cl-nagoya/ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m)|315M|8192|77.24|



## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers fugashi sentencepiece unidic-lite
```

Then you can load this model and run inference.
```python
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("cl-nagoya/ruri-small", trust_remote_code=True)

# Don't forget to add the prefix "クエリ: " for query-side or "文章: " for passage-side texts.
sentences = [
    "クエリ: 瑠璃色はどんな色？",
    "文章: 瑠璃色（るりいろ）は、紫みを帯びた濃い青。名は、半貴石の瑠璃（ラピスラズリ、英: lapis lazuli）による。JIS慣用色名では「こい紫みの青」（略号 dp-pB）と定義している[1][2]。",
    "クエリ: ワシやタカのように、鋭いくちばしと爪を持った大型の鳥類を総称して「何類」というでしょう?",
    "文章: ワシ、タカ、ハゲワシ、ハヤブサ、コンドル、フクロウが代表的である。これらの猛禽類はリンネ前後の時代(17~18世紀)には鷲類・鷹類・隼類及び梟類に分類された。ちなみにリンネは狩りをする鳥を単一の目(もく)にまとめ、vultur(コンドル、ハゲワシ)、falco(ワシ、タカ、ハヤブサなど)、strix(フクロウ)、lanius(モズ)の4属を含めている。",
]

embeddings = model.encode(sentences, convert_to_tensor=True)
print(embeddings.size())
# [4, 768]

similarities = F.cosine_similarity(embeddings.unsqueeze(0), embeddings.unsqueeze(1), dim=2)
print(similarities)
# [[1.0000, 0.9453, 0.6860, 0.7225],
#  [0.9453, 1.0000, 0.6852, 0.7005],
#  [0.6860, 0.6852, 1.0000, 0.8567],
#  [0.7225, 0.7005, 0.8567, 1.0000]]
```

## Benchmarks

### JMTEB
Evaluated with [JMTEB](https://github.com/sbintuitions/JMTEB).

|Model|#Param.|Avg.|Retrieval|STS|Classfification|Reranking|Clustering|PairClassification|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|[cl-nagoya/sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base)|111M|68.56|49.64|82.05|73.47|91.83|51.79|62.57|
|[cl-nagoya/sup-simcse-ja-large](https://huggingface.co/cl-nagoya/sup-simcse-ja-large)|337M|66.51|37.62|83.18|73.73|91.48|50.56|62.51|
|[cl-nagoya/unsup-simcse-ja-base](https://huggingface.co/cl-nagoya/unsup-simcse-ja-base)|111M|65.07|40.23|78.72|73.07|91.16|44.77|62.44|
|[cl-nagoya/unsup-simcse-ja-large](https://huggingface.co/cl-nagoya/unsup-simcse-ja-large)|337M|66.27|40.53|80.56|74.66|90.95|48.41|62.49|
|[pkshatech/GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja)|133M|70.44|59.02|78.71|76.82|91.90|49.78|66.39|
||||||||||
|[sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE)|472M|64.70|40.12|76.56|72.66|91.63|44.88|62.33|
|[intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small)|118M|69.52|67.27|80.07|67.62|93.03|46.91|62.19|
|[intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base)|278M|70.12|68.21|79.84|69.30|92.85|48.26|62.26|
|[intfloat/multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large)|560M|71.65|70.98|79.70|72.89|92.96|51.24|62.15|
||||||||||
|OpenAI/text-embedding-ada-002|-|69.48|64.38|79.02|69.75|93.04|48.30|62.40|
|OpenAI/text-embedding-3-small|-|70.86|66.39|79.46|73.06|92.92|51.06|62.27|
|OpenAI/text-embedding-3-large|-|73.97|74.48|82.52|77.58|93.58|53.32|62.35|
||||||||||
|[**Ruri-Small**](https://huggingface.co/cl-nagoya/ruri-small) (this model)|68M|71.53|69.41|82.79|76.22|93.00|51.19|62.11|
|[Ruri-Base](https://huggingface.co/cl-nagoya/ruri-base)|111M|71.91|69.82|82.87|75.58|92.91|54.16|62.38|
|[Ruri-Large](https://huggingface.co/cl-nagoya/ruri-large)|337M|73.31|73.02|83.13|77.43|92.99|51.82|62.29|


## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [cl-nagoya/ruri-pt-small](https://huggingface.co/cl-nagoya/ruri-pt-small) 
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768
- **Similarity Function:** Cosine Similarity
- **Language:** Japanese
- **License:** Apache 2.0
- **Paper:** https://arxiv.org/abs/2409.07737
<!-- - **Training Dataset:** Unknown -->


### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: DistilBertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```


## Training Details


### Framework Versions
- Python: 3.10.13
- Sentence Transformers: 3.0.0
- Transformers: 4.41.2
- PyTorch: 2.3.1+cu118
- Accelerate: 0.30.1
- Datasets: 2.19.1
- Tokenizers: 0.19.1

## Citation

```bibtex
@misc{
  Ruri,
  title={{Ruri: Japanese General Text Embeddings}}, 
  author={Hayato Tsukagoshi and Ryohei Sasano},
  year={2024},
  eprint={2409.07737},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2409.07737}, 
}
```

## License
This model is published under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).