---
language:
- en
license: mit
tags:
- chemistry
- SMILES
- product
datasets:
- ORD
metrics:
- accuracy
---

# Model Card for ReactionT5v2-forward

This is a ReactionT5 pre-trained to predict the products of reactions. You can use the demo [here](https://huggingface.co/spaces/sagawa/ReactionT5_task_forward).
This is a ReactionT5 pre-trained to predict the products of reactions and fine-tuned on USPOT_50k's train split. Base model before fine-tuning is [here](https://huggingface.co/sagawa/ReactionT5v2-forward).


### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/sagawatatsuya/ReactionT5v2
- **Paper:** https://jcheminf.biomedcentral.com/articles/10.1186/s13321-025-01075-4
- **Demo:** https://huggingface.co/spaces/sagawa/ReactionT5

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
You can use this model for forward reaction prediction or fine-tune this model with your dataset.


## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("sagawa/ReactionT5v2-forward", return_tensors="pt")
model = AutoModelForSeq2SeqLM.from_pretrained("sagawa/ReactionT5v2-forward")

inp = tokenizer('REACTANT:COC(=O)C1=CCCN(C)C1.O.[Al+3].[H-].[Li+].[Na+].[OH-]REAGENT:C1CCOC1', return_tensors='pt')
output = model.generate(**inp, num_beams=1, num_return_sequences=1, return_dict_in_generate=True, output_scores=True)
output = tokenizer.decode(output['sequences'][0], skip_special_tokens=True).replace(' ', '').rstrip('.')
output # 'CN1CCC=C(CO)C1'
```

## Training Details

### Training Procedure 

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
We used the [USPTO_MIT dataset](https://drive.google.com/file/d/1NEb5DSwqFfg4gm0P2lPb19cqPt96-OSC/view?usp=drive_link) for model finetuning.
The command used for training is the following. For more information, please refer to the paper and GitHub repository.

```python
cd task_forward
python finetune.py \
    --output_dir='t5' \
    --epochs=50 \
    --lr=2e-5 \
    --batch_size=32 \
    --input_max_len=200 \
    --target_max_len=150 \
    --evaluation_strategy='epoch' \
    --save_strategy='epoch' \
    --logging_strategy='epoch' \
    --save_total_limit=10 \
    --train_data_path='../data/USPTO_MIT/MIT_separated/train.csv' \
    --valid_data_path='../data/USPTO_MIT/MIT_separated/val.csv' \
    --disable_tqdm \
    --model_name_or_path='sagawa/ReactionT5v2-forward'
```

### Results


| Model                | Training set              | Test set | Top-1 [% acc.] | Top-2 [% acc.] | Top-3 [% acc.] | Top-5 [% acc.] |
|----------------------|---------------------------|----------|----------------|----------------|----------------|----------------|
| Sequence-to-sequence | USPTO_MIT                     | USPTO_MIT    | 80.3           | 84.7           | 86.2           | 87.5           |
| WLDN                 | USPTO_MIT                     | USPTO_MIT    | 80.6 (85.6)    | 90.5           | 92.8           | 93.4           |
| Molecular Transformer| USPTO_MIT                     | USPTO_MIT    | 88.8           | 92.6           | –              | 94.4           |
| T5Chem               | USPTO_MIT                     | USPTO_MIT    | 90.4           | 94.2           | –              | 96.4           |
| CompoundT5           | USPTO_MIT                     | USPTO_MIT    | 86.6           | 89.5           | 90.4           | 91.2           |
| [ReactionT5](https://huggingface.co/sagawa/ReactionT5v2-forward)          | -                       | USPTO_MIT    | 92.8     | 95.6     | 96.4     | 97.1     |
| [ReactionT5 (This model)](https://huggingface.co/sagawa/ReactionT5v2-forward-USPTO_MIT)           | USPTO_MIT                       | USPTO_MIT    | 97.5     | 98.6     | 98.8     | 99.0     |

Performance comparison of Compound T5, ReactionT5, and other models in product prediction.

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->
```
@article{Sagawa2025,
  title   = {ReactionT5: a pre-trained transformer model for accurate chemical reaction prediction with limited data},
  author  = {Sagawa, Tatsuya and Kojima, Ryosuke},
  journal = {Journal of Cheminformatics},
  year    = {2025},
  volume  = {17},
  number  = {1},
  pages   = {126},
  doi     = {10.1186/s13321-025-01075-4},
  url     = {https://doi.org/10.1186/s13321-025-01075-4}
}
```