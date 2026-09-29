---
tags:
- Turkish
- turkish
- passage-retrieval
license: mit
language:
- tr
base_model: ytu-ce-cosmos/turkish-base-bert-uncased
pipeline_tag: sentence-similarity
---
# Turkish-ColBERT
This is a Turkish passage retrieval model based on the [ColBERT](https://doi.org/10.48550/arXiv.2112.01488) architecture.

The [Cosmos Turkish Base BERT](https://huggingface.co/ytu-ce-cosmos/turkish-base-bert-uncased) model was fine-tuned on 500k triplets (query, positive passage, negative passage) from a Turkish-translated version of the [MS MARCO dataset](https://huggingface.co/datasets/parsak/msmarco-tr).

#### ⚠ Uncased use requires manual lowercase conversion
Convert your text to lower case as follows: 
```python
text.replace("I", "ı").lower()
```
This is due to a [known issue](https://github.com/huggingface/transformers/issues/6680) with the tokenizer.

## Example Usage

```bash
!pip install ragatouille
```

```python
from ragatouille import RAGPretrainedModel

rag = RAGPretrainedModel.from_pretrained("ytu-ce-cosmos/turkish-colbert")

docs = [
    "Marie Curie, radyoaktivite üzerine yaptığı çalışmalarla bilim dünyasına büyük katkılar sağlamıştır. Polonyum ve radyum elementlerini keşfetmiştir. İki farklı dalda Nobel Ödülü alan ilk kişi olmuştur.",
    "Isaac Newton, fizik ve matematik alanında yaptığı çalışmalarla bilinir. Yerçekimi teorisi ve hareket yasaları, bilim dünyasında çığır açmıştır. Ayrıca, matematiksel analiz üzerinde de önemli katkıları vardır.",
    "Albert Einstein, izafiyet teorisini geliştirerek modern fiziğin temellerini atmıştır. 1921 yılında Nobel Fizik Ödülü'nü kazanmıştır. Kütle-enerji eşitliği (E=mc²) onun en ünlü formülüdür.",
    "Alexander Fleming, 1928 yılında penisilini keşfederek modern tıpta devrim yaratmıştır. Bu keşfi sayesinde 1945 yılında Nobel Tıp Ödülü kazanmıştır. Fleming'in çalışmaları antibiyotiklerin gelişimine öncülük etmiştir.",
    "Nikola Tesla, alternatif akım (AC) sistemini geliştirmiştir. Elektrik mühendisliği alanında devrim niteliğinde çalışmalar yapmıştır. Kablosuz enerji aktarımı üzerine projeleriyle tanınır."
]

docs = [doc.replace("I", "ı").lower() for doc in docs]

rag.index(docs, index_name="sampleTest")

query = "Birden fazla Nobel Ödülü alan bilim insanı kimdir?"
query = query.replace("I", "ı").lower()

results = rag.search(query, k= 1)
print(results[0]['content']) # "marie curie, radyoaktivite üzerine yaptığı çalışmalarla bilim dünyasına büyük katkılar sağlamıştır. polonyum ve radyum elementlerini keşfetmiştir. i̇ki farklı dalda nobel ödülü alan ilk kişi olmuştur."
```

# Evaluation
| Dataset     | R@1          | R@5          | R@10         | MRR@10        |
|-------------|--------------|--------------|--------------|---------------|
| [Scifact-tr](https://huggingface.co/datasets/AbdulkaderSaoud/scifact-tr)        | 48.38          | 67.85         | 75.52         | 56.88          |
| [WikiRAG-TR](https://huggingface.co/datasets/Metin/WikiRAG-TR)                  | 31.21         | 75.63          | 79.63          | 49.08         |

# Acknowledgments
- Research supported with Cloud TPUs from [Google's TensorFlow Research Cloud](https://sites.research.google/trc/about/) (TFRC). Thanks for providing access to the TFRC ❤️
- Thanks to the generous support from the Hugging Face team, it is possible to download models from their S3 storage 🤗

# Citations
```bibtex
@article{kesgin2023developing,
  title={Developing and Evaluating Tiny to Medium-Sized Turkish BERT Models},
  author={Kesgin, Himmet Toprak and Yuce, Muzaffer Kaan and Amasyali, Mehmet Fatih},
  journal={arXiv preprint arXiv:2307.14134},
  year={2023}
}
```

### Contact 
COSMOS AI Research Group, Yildiz Technical University Computer Engineering Department   <br>
https://cosmos.yildiz.edu.tr/ <br>
cosmos@yildiz.edu.tr <br>