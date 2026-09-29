---
license: other
widget:
- text: Ḣ Q V Q [MASK] E
tags:
- biology
- medical
---

## AntiBERTa2 🧬

AntiBERTa2 is an antibody-specific language model based on the [RoFormer model](https://arxiv.org/abs/2104.09864) - it is pre-trained using masked language modelling.
We also provide a multimodal version of AntiBERTa2, AntiBERTa2-CSSP, that has been trained using a contrastive objective, similar to the [CLIP method](https://arxiv.org/abs/2103.00020).
Further details on both AntiBERTa2 and AntiBERTa2-CSSP are described in our [paper](https://www.mlsb.io/papers_2023/Enhancing_Antibody_Language_Models_with_Structural_Information.pdf) accepted at the NeurIPS MLSB Workshop 2023.

Both AntiBERTa2 models are only available for non-commercial use. Output antibody sequences (e.g. from infilling via masked language models) can only be used for
non-commercial use. For any users seeking commercial use of our model and generated antibodies, please reach out to us at [info@alchemab.com](mailto:info@alchemab.com).

| Model variant | Parameters | Config |
| ------------- | ---------- | ------ |
| [AntiBERTa2](https://huggingface.co/alchemab/antiberta2)  | 202M       | 16L, 16H, 1024d |
| [AntiBERTa2-CSSP](https://huggingface.co/alchemab/antiberta2-cssp) | 202M       | 16L, 16H, 1024d |

## Example usage

```
>>> from transformers import (
        RoFormerForMaskedLM, 
        RoFormerTokenizer, 
        pipeline, 
        RoFormerForSequenceClassification
    )
>>> tokenizer = RoFormerTokenizer.from_pretrained("alchemab/antiberta2")
>>> model = RoFormerForMaskedLM.from_pretrained("alchemab/antiberta2")

>>> filler = pipeline(model=model, tokenizer=tokenizer)
>>> filler("Ḣ Q V Q ... C A [MASK] D ... T V S S") # fill in the mask

>>> new_model = RoFormerForSequenceClassification.from_pretrained(
            "alchemab/antiberta2") # this will of course raise warnings 
                                   # that a new linear layer will be added 
                                   # and randomly initialized

```