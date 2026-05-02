---

language:
- en

tags:
- retrieval
- entity-retrieval
- named-entity-disambiguation
- entity-disambiguation
- named-entity-linking
- entity-linking
- text2text-generation
---


# GENRE


The GENRE (Generative ENtity REtrieval) system as presented in [Autoregressive Entity Retrieval](https://arxiv.org/abs/2010.00904) implemented in pytorch.

In a nutshell, GENRE uses a sequence-to-sequence approach to entity retrieval (e.g., linking), based on fine-tuned [BART](https://arxiv.org/abs/1910.13461) architecture. GENRE performs retrieval generating the unique entity name conditioned on the input text using constrained beam search to only generate valid identifiers. The model was first released in the [facebookresearch/GENRE](https://github.com/facebookresearch/GENRE) repository using `fairseq` (the `transformers` models are obtained with a conversion script similar to [this](https://github.com/huggingface/transformers/blob/master/src/transformers/models/bart/convert_bart_original_pytorch_checkpoint_to_pytorch.py).

This model was trained on the full training set of [BLINK](https://arxiv.org/abs/1911.03814) (i.e., 9M datapoints for entity-disambiguation grounded on Wikipedia).

## BibTeX entry and citation info

**Please consider citing our works if you use code from this repository.**

```bibtex
@inproceedings{decao2020autoregressive,
  title={Autoregressive Entity Retrieval},
  author={Nicola {De Cao} and Gautier Izacard and Sebastian Riedel and Fabio Petroni},
  booktitle={International Conference on Learning Representations},
  url={https://openreview.net/forum?id=5k8F6UU39V},
  year={2021}
}
```

## Usage

Here is an example of generation for Wikipedia page disambiguation:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# OPTIONAL: load the prefix tree (trie), you need to additionally download
# https://huggingface.co/facebook/genre-linking-blink/blob/main/trie.py and 
# https://huggingface.co/facebook/genre-linking-blink/blob/main/kilt_titles_trie_dict.pkl
# import pickle
# from trie import Trie
# with open("kilt_titles_trie_dict.pkl", "rb") as f:
#     trie = Trie.load_from_dict(pickle.load(f))

tokenizer = AutoTokenizer.from_pretrained("facebook/genre-linking-blink")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/genre-linking-blink").eval()

sentences = ["Einstein was a [START_ENT] German [END_ENT] physicist."]

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
['Germans',
 'Germany',
 'German Empire',
 'Weimar Republic',
 'Greeks']
```