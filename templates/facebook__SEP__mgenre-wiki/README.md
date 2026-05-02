---

language:
- multilingual
- af
- am
- ar
- as
- az
- be
- bg
- bm
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- ff
- fi
- fr
- fy
- ga
- gd
- gl
- gn
- gu
- ha
- he
- hi
- hr
- ht
- hu
- hy
- id
- ig
- is
- it
- ja
- jv
- ka
- kg
- kk
- km
- kn
- ko
- ku
- ky
- la
- lg
- ln
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- no
- om
- or
- pa
- pl
- ps
- pt
- qu
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- ss
- su
- sv
- sw
- ta
- te
- th
- ti
- tl
- tn
- tr
- uk
- ur
- uz
- vi
- wo
- xh
- yo
- zh


tags:
- retrieval
- entity-retrieval
- named-entity-disambiguation
- entity-disambiguation
- named-entity-linking
- entity-linking
- text2text-generation
---


# mGENRE 


The mGENRE (multilingual Generative ENtity REtrieval) system as presented in [Multilingual Autoregressive Entity Linking](https://arxiv.org/abs/2103.12528) implemented in pytorch.

In a nutshell, mGENRE uses a sequence-to-sequence approach to entity retrieval (e.g., linking), based on fine-tuned [mBART](https://arxiv.org/abs/2001.08210) architecture. GENRE performs retrieval generating the unique entity name conditioned on the input text using constrained beam search to only generate valid identifiers. The model was first released in the [facebookresearch/GENRE](https://github.com/facebookresearch/GENRE) repository using `fairseq` (the `transformers` models are obtained with a conversion script similar to [this](https://github.com/huggingface/transformers/blob/master/src/transformers/models/bart/convert_bart_original_pytorch_checkpoint_to_pytorch.py).

This model was trained on 105 languages from Wikipedia.

## BibTeX entry and citation info

**Please consider citing our works if you use code from this repository.**

```bibtex
@article{decao2020multilingual,
    author = {De Cao, Nicola and Wu, Ledell and Popat, Kashyap and Artetxe, Mikel 
    and Goyal, Naman and Plekhanov, Mikhail and Zettlemoyer, Luke 
    and Cancedda, Nicola and Riedel, Sebastian and Petroni, Fabio},
    title = "{Multilingual Autoregressive Entity Linking}",
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {10},
    pages = {274-290},
    year = {2022},
    month = {03},
    issn = {2307-387X},
    doi = {10.1162/tacl_a_00460},
    url = {https://doi.org/10.1162/tacl\_a\_00460},
    eprint = {https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl\_a\_00460/2004070/tacl\_a\_00460.pdf},
}
```

## Usage

Here is an example of generation for Wikipedia page disambiguation:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# OPTIONAL: load the prefix tree (trie), you need to additionally download
# https://huggingface.co/facebook/mgenre-wiki/blob/main/trie.py and 
# https://huggingface.co/facebook/mgenre-wiki/blob/main/titles_lang_all105_trie_with_redirect.pkl
# that is fast but memory inefficient prefix tree (trie) -- it is implemented with nested python `dict`
# NOTE: loading this map may take up to 10 minutes and occupy a lot of RAM!
# import pickle
# from trie import Trie
# with open("titles_lang_all105_marisa_trie_with_redirect.pkl", "rb") as f:
#     trie = Trie.load_from_dict(pickle.load(f))

# or a memory efficient but a bit slower prefix tree (trie) -- it is implemented with `marisa_trie` from
# https://huggingface.co/facebook/mgenre-wiki/blob/main/titles_lang_all105_marisa_trie_with_redirect.pkl
# from genre.trie import MarisaTrie
# with open("titles_lang_all105_marisa_trie_with_redirect.pkl", "rb") as f:
#     trie = pickle.load(f)

tokenizer = AutoTokenizer.from_pretrained("facebook/mgenre-wiki")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/mgenre-wiki").eval()

sentences = ["[START] Einstein [END] era un fisico tedesco."]
# Italian for "[START] Einstein [END] was a German physicist."

outputs = model.generate(
    **tokenizer(sentences, return_tensors="pt"),
    num_beams=5,
    num_return_sequences=5,
    # OPTIONAL: use constrained beam search
    # prefix_allowed_tokens_fn=lambda batch_id, sent: trie.get(sent.tolist()),
)

tokenizer.batch_decode(outputs, skip_special_tokens=True)
```
which outputs the following top-5 predictions (using constrained beam search)
```
['Albert Einstein >> it',
 'Albert Einstein (disambiguation) >> en',
 'Alfred Einstein >> it',
 'Alberto Einstein >> it',
 'Einstein >> it']
```