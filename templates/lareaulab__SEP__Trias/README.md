---
license: mit
tags:
- biology
- mrna design
- codon optimization
pipeline_tag: translation
---

# Trias: an encoder-decoder model for generating synthetic eukaryotic mRNA sequences

Trias is an encoder-decoder language model trained to reverse-translate protein sequences into codon sequences. It learns codon usage patterns from 10 million mRNA coding sequences across 640 vertebrate species, enabling context-aware sequence generation without requiring handcrafted rules.


## Setup 

Trias is developed and tested with **Python 3.8.8**. 

To install directly from GitHub
```bash
pip install git+https://github.com/lareaulab/Trias.git
```


## Reverse Translation

Trias generates optimized codon sequences from protein input using a pretrained model. You can use the checkpoint hosted on Hugging Face (lareaulab/Trias) or a local model directory. It supports execution on both CPU and GPU (automatically detected). And we provide both greedy decoding and beam search for flexible output control.

Greedy decoding selects the most likely token at each step, it's faster and deterministic. Beam search explores multiple candidate paths and is better for longer or complex proteins, but is also slower.


```python
from transformers import AutoTokenizer, BartForConditionalGeneration
from trias import *

# Load model and tokenizer from the Hub
tokenizer = AutoTokenizer.from_pretrained("lareaulab/Trias", use_fast=True)
model = BartForConditionalGeneration.from_pretrained("lareaulab/Trias")

# Input sequence
species = "Homo sapiens"
protein_sequence = "MTEITAAMVKELRESTGAGMMDCKNALSETQ*"
input_seq = f">>{species}<< {protein_sequence}"

# Tokenize
input_ids = tokenizer.encode(input_seq, return_tensors="pt")

# Generate codon sequence (greedy)
outputs = model.generate(input_ids, max_length=tokenizer.model_max_length)
codon_sequence = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Codon sequence:", codon_sequence)
```

Beam search example 
```python
outputs = model.generate(
    input_ids,
    num_beams=5,
    early_stopping=True,
    max_length=tokenizer.model_max_length)

```


## Citation

If you use Trias, please cite our work:

```bibtex
@article{faizi2025,
  title={A generative language model decodes contextual constraints on codon choice for mRNA design},
  author={Marjan Faizi and Helen Sakharova and Liana F. Lareau},
  journal={bioRxiv},
  year={2025},
  url={https://doi.org/10.1101/2025.05.13.653614}
}
```