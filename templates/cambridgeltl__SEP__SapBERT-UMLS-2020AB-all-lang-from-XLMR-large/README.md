---
language: multilingual

tags:
- biomedical
- lexical-semantics
- cross-lingual

datasets:
- UMLS

**[news]** A cross-lingual extension of SapBERT will appear in the main onference of **ACL 2021**! <br>
**[news]** SapBERT will appear in the conference proceedings of **NAACL 2021**!

### SapBERT-XLMR
SapBERT [(Liu et al. 2021)](https://arxiv.org/pdf/2010.11784.pdf) trained with [UMLS](https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html) 2020AB, using [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) as the base model. Please use [CLS] as the representation of the input.


#### Extracting embeddings from SapBERT

The following script converts a list of strings (entity names) into embeddings.
```python
import numpy as np
import torch
from tqdm.auto import tqdm
from transformers import AutoTokenizer, AutoModel  

tokenizer = AutoTokenizer.from_pretrained("cambridgeltl/SapBERT-from-PubMedBERT-fulltext")  
model = AutoModel.from_pretrained("cambridgeltl/SapBERT-from-PubMedBERT-fulltext").cuda()

# replace with your own list of entity names
all_names = ["covid-19", "Coronavirus infection", "high fever", "Tumor of posterior wall of oropharynx"] 

bs = 128 # batch size during inference
all_embs = []
for i in tqdm(np.arange(0, len(all_names), bs)):
    toks = tokenizer.batch_encode_plus(all_names[i:i+bs], 
                                       padding="max_length", 
                                       max_length=25, 
                                       truncation=True,
                                       return_tensors="pt")
    toks_cuda = {}
    for k,v in toks.items():
        toks_cuda[k] = v.cuda()
    cls_rep = model(**toks_cuda)[0][:,0,:] # use CLS representation as the embedding
    all_embs.append(cls_rep.cpu().detach().numpy())

all_embs = np.concatenate(all_embs, axis=0)
```

For more details about training and eval, see SapBERT [github repo](https://github.com/cambridgeltl/sapbert).

### Citation

```bibtex
@inproceedings{liu2021learning,
	title={Learning Domain-Specialised Representations for Cross-Lingual Biomedical Entity Linking},
	author={Liu, Fangyu and Vuli{\'c}, Ivan and Korhonen, Anna and Collier, Nigel},
	booktitle={Proceedings of ACL-IJCNLP 2021},
	month = aug,
	year={2021}
}
```
