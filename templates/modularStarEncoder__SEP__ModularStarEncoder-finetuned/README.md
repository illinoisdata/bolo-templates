---
library_name: transformers
datasets:
- bigcode/the-stack-v2
- modularStarEncoder/SynthCode2Code2NL-neardedup
license: bigcode-openrail-m
base_model:
- modularStarEncoder/ModularStarEncoder
---

# ModularStarEncoder-1B Fine-Tuned model

<!-- Provide a quick summary of what the model is/does. -->

ModularStarEncoder-finetuned (MoSE) is an encoder built on top of [ModularStarEncoder-1B Pre-trained](https://huggingface.co/andreagurioli1995/ModularStarEncoder) on [SynthCoNL](https://huggingface.co/datasets/andreagurioli1995/SynthCode2Code2NL-neardedup). 
ModularStarEncoder, fine-tuned, is an encoder for code-to-code and text-to-code retrieval tasks, enabling the end user to select the model size that meets their memory and computational constraints.
We built ModularStarEncoder on top of [StarCoder-2](https://huggingface.co/bigcode/starcoder2-15b), reducing its size from 15B to 1B parameters in bfloat16.

The model is finetuned with [CLIP objective](https://github.com/mlfoundations/open_clip/blob/main/src/open_clip/loss.py).
ModularStarEncoder fine-tuned works with instruction prompts; to get the most out of the model, embed the task in the input. The How to Use section below provides more details.

- **Paper:** [MoSE: Hierarchical Self-Distillation Enhances Early Layer Embeddings](https://arxiv.org/abs/2503.03008)
- **Languages:** English, Go, Ruby, Python, Java, C++, PHP, C, JavaScript
- **Different sizes:**  [Layer 4](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned-4), [Layer 9](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned-9), [Layer 18](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned-18), [Layer 27](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned-27), [Layer 36](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned)  

### How to use
```python
from transformers import AutoModel
from transformers import AutoTokenizer

#import the model
model = AutoModel.from_pretrained("andreagurioli1995/ModularStarEncoder-finetuned", trust_remote_code=True)

#import the tokenizer, the tokenizer applies LEFT padding!
tokenizer = AutoTokenizer.from_pretrained("andreagurioli1995/ModularStarEncoder-finetuned")

 
language = "yourlanguagelowercased"

#instruction in case of code embedding in a code language
instruction_code = f"Represent this {language} code snippet for retrieval:"

#instruction in case of code embedding in English
instruction_natural_language = "Represent this code description for retrieving supporting snippets of code:"

code_snippet = "your code to embed here"

#You should follow this pattern to embed a snippet of code or natural language queries 
sentence =  f"{tokenizer.sep_token}{instruction_code}{tokenizer.sep_token}{code_snippet}{tokenizer.cls_token}"

#Tokenizing your sentence
tokenized_sentence = tokenizer(sentence, return_tensors="pt",truncation=True, max_length=2048)

#Embedding the tokenized sentence
embedded_sentence = model(**tokenized_sentence)
```

You will get as an output three elements:

- projected_pooled_normalized: a list of the projected, pooled, and normalized embeddings from the five exit points (respectively from layers [4,9,18,27,36], the last element of the list corresponds to the final layer projected representation);
- raw_hidden_states: raw representation from all the hidden states of the model, without pooling, normalization, and projection
- attentions: attention scores from the encoder
  
  
### Training

<!-- Provide a longer summary of what this model is. -->
We fine-tuned ModularStarEncoder with a batch size of 2048 contrastive samples for 20,000 training steps.
The pre-training and fine-tuning were conducted on 512 NVIDIA Ampere (64GB) GPUs using the [Leonardo](https://arxiv.org/abs/2307.16885) supercomputer, requiring 450,000 GPU working hours.

| Hyperparameter           | Value     |
|--------------------------|-----------|
| Hidden size              | 1024      |
| Max. position embeddings | 2048      |
| Num. of attention heads  | 12        |
| Num. of key values heads | 4         |
| Num. of hidden layers    | 36        |
| Attention                | GQA       |
| Num. of parameters       | ≈1B       |
|Loss function             |CLIP loss  |
|Multi-layer loss          | yes       |


### Evaluation

Here we briefly show our codeSearchNet (codeXGLUE) results between different layers; for full results over text-to-code and code-to-code refer to the article:

| Layer           | Avg. MRR     |
|--------------------------|-----------|
| [Layer 4](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned-4)*              | 73.2     |
| [Layer 9](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned-9)*              |    77.3  |
| [Layer 18](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned-18)*              |  81.0    |
| [Layer 27](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned-27)*            |   80.3   |
| [Layer 36](https://huggingface.co/modularStarEncoder/ModularStarEncoder-finetuned)*              |   79.6   |

- (* size and corresponding projection head present in this model)

## Licence 
The model is licensed under the BigCode OpenRAIL-M v1 license agreement. You can find the full agreement [here](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement).


# Citation
```
@article{gurioli2025mosehierarchicalselfdistillationenhances,
      title={MoSE: Hierarchical Self-Distillation Enhances Early Layer Embeddings}, 
      author={Andrea Gurioli and Federico Pennino and João Monteiro and Maurizio Gabbrielli},
      year={2025},
      eprint={2503.03008},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.03008}, 
}
```