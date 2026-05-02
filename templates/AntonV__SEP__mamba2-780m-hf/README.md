---
tags:
- mamba2
license: mit
library_name: transformers
---

# mamba2-780m-hf

Converted files of the original model at [mamba2-780m](https://huggingface.co/state-spaces/mamba2-780m) to HF transformers compatible formats. 
Not affiliated with both the original authors or hf.

## Usage
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("AntonV/mamba2-780m-hf")
model = AutoModelForCausalLM.from_pretrained("AntonV/mamba2-780m-hf")

input_ids = tokenizer("Hey how are you doing?", return_tensors="pt")["input_ids"]
out = model.generate(input_ids, max_new_tokens=10)
print(tokenizer.batch_decode(out))
```


## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```bibtex
@inproceedings{mamba2,
 title={Transformers are {SSM}s: Generalized Models and Efficient Algorithms Through Structured State Space Duality},
 author={Dao, Tri and Gu, Albert},
 booktitle={International Conference on Machine Learning (ICML)},
 year={2024}
}
```