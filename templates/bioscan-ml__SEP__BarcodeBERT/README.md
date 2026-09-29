---
language:
- en
license: mit
pipeline_tag: feature-extraction
library_name: transformers
description: "Pretrained weights for BarcodeBERT, a transformer for insect DNA barcode inference."
---

# BarcodeBERT for Taxonomic Classification

A pre-trained transformer model for inference on insect DNA barcoding data, as presented in the paper [BarcodeBERT: Transformers for Biodiversity Analysis](https://huggingface.co/papers/2311.02401).

Code: https://github.com/bioscan-ml/BarcodeBERT

[Colab](https://colab.research.google.com/drive/1MUEQVHIOX2ks7tLsMoQtNlbvsbSuYgs1)

To use **BarcodeBERT** as a feature extractor:

```python
from transformers import AutoTokenizer, BertForTokenClassification

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "bioscan-ml/BarcodeBERT", trust_remote_code=True
)

# Load the model
model = BertForTokenClassification.from_pretrained("bioscan-ml/BarcodeBERT", trust_remote_code=True)

# Sample sequence
dna_seq = "ACGCGCTGACGCATCAGCATACGA"

# Tokenize
input_seq = tokenizer(dna_seq, return_tensors="pt")["input_ids"]

# Pass through the model
output = model(input_seq.unsqueeze(0))["hidden_states"][-1]

# Compute Global Average Pooling 
features = output.mean(1)
```

## Citation 

If you find BarcodeBERT useful in your research please consider citing:

    @misc{arias2023barcodebert,
      title={{BarcodeBERT}: Transformers for Biodiversity Analysis},
      author={Pablo Millan Arias
        and Niousha Sadjadi
        and Monireh Safari
        and ZeMing Gong
        and Austin T. Wang
        and Scott C. Lowe
        and Joakim Bruslund Haurum
        and Iuliia Zarubiieva
        and Dirk Steinke
        and Lila Kari
        and Angel X. Chang
        and Graham W. Taylor
      },
      year={2023},
      eprint={2311.02401},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      doi={10.48550/arxiv.2311.02401},
    }