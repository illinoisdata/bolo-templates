---
language:
- en
license: mit
tags:
- chemistry
- SMILES
- yield
datasets:
- ORD
metrics:
- r_squared
---

# Model Card for ReactionT5v2-yield

This is a ReactionT5 pre-trained to predict yields of reactions. You can use the demo [here](https://huggingface.co/spaces/sagawa/ReactionT5_task_yield).

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/sagawatatsuya/ReactionT5v2
- **Paper:** https://jcheminf.biomedcentral.com/articles/10.1186/s13321-025-01075-4
- **Demo:** https://huggingface.co/spaces/sagawa/ReactionT5

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

## How to Get Started with the Model

Use the code below to get started with the model.

```python
import torch
import torch.nn as nn
from transformers import AutoTokenizer, T5ForConditionalGeneration, AutoConfig, PreTrainedModel
import logging
logging.getLogger('transformers').setLevel(logging.ERROR)

class ReactionT5Yield(PreTrainedModel):
    config_class  = AutoConfig
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.model = T5ForConditionalGeneration.from_pretrained(self.config._name_or_path)
        self.model.resize_token_embeddings(self.config.vocab_size)
        self.fc1 = nn.Linear(self.config.hidden_size, self.config.hidden_size//2)
        self.fc2 = nn.Linear(self.config.hidden_size, self.config.hidden_size//2)
        self.fc3 = nn.Linear(self.config.hidden_size//2*2, self.config.hidden_size)
        self.fc4 = nn.Linear(self.config.hidden_size, self.config.hidden_size)
        self.fc5 = nn.Linear(self.config.hidden_size, 1)

        self._init_weights(self.fc1)
        self._init_weights(self.fc2)
        self._init_weights(self.fc3)
        self._init_weights(self.fc4)
        self._init_weights(self.fc5)

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            module.weight.data.normal_(mean=0.0, std=0.01)
            if module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.Embedding):
            module.weight.data.normal_(mean=0.0, std=0.01)
            if module.padding_idx is not None:
                module.weight.data[module.padding_idx].zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)

    def forward(self, inputs):
        encoder_outputs = self.model.encoder(**inputs)
        encoder_hidden_states = encoder_outputs[0]
        outputs = self.model.decoder(input_ids=torch.full((inputs['input_ids'].size(0),1),
                                            self.config.decoder_start_token_id,
                                            dtype=torch.long), encoder_hidden_states=encoder_hidden_states)
        last_hidden_states = outputs[0]
        output1 = self.fc1(last_hidden_states.view(-1, self.config.hidden_size))
        output2 = self.fc2(encoder_hidden_states[:, 0, :].view(-1, self.config.hidden_size))
        output = self.fc3(torch.hstack((output1, output2)))
        output = self.fc4(output)
        output = self.fc5(output)
        return output*100


model = ReactionT5Yield.from_pretrained('sagawa/ReactionT5v2-yield')
tokenizer = AutoTokenizer.from_pretrained('sagawa/ReactionT5v2-yield')
inp = tokenizer(['REACTANT:CC(C)n1ncnc1-c1cn2c(n1)-c1cnc(O)cc1OCC2.CCN(C(C)C)C(C)C.Cl.NC(=O)[C@@H]1C[C@H](F)CN1REAGENT: PRODUCT:O=C(NNC(=O)C(F)(F)F)C(F)(F)F'], return_tensors='pt')
print(model(inp)) # tensor([[19.1666]], grad_fn=<MulBackward0>)
```

## Training Details

### Training Procedure 

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
We used [Open Reaction Database (ORD) dataset](https://drive.google.com/file/d/1JozA2OlByfZ-ILt5H5YrTjLJvSvD8xdL/view?usp=drive_link) for model training. In addition, we used palladium-catalyzed Buchwald-Hartwig [C-N cross-coupling reactions dataset](https://yzhang.hpc.nyu.edu/T5Chem/index.html)'s test split to prevent data leakage.
The command used for training is the following. For more information about data preprocessing and training, please refer to the paper and GitHub repository.

```python
python train.py \
    --train_data_path='../data/preprocessed_ord_train.csv' \
    --valid_data_path='../data/preprocessed_ord_valid.csv' \
    --test_data_path='../data/preprocessed_ord_test.csv' \
    --CN_test_data_path='../data/C_N_yield/MFF_Test1/test.csv' \
    --epochs=100 \
    --batch_size=32 \
    --output_dir='./'
```

### Results

| **R^2**       | **DFT**       | **MFF**       | **Yield-BERT**| **T5Chem**    | **CompoundT5**| **ReactionT5** (without finetuning)    | **ReactionT5** |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Random 70/30  | 0.92          | 0.927 ± 0.007 | 0.951 ± 0.005 | 0.970 ± 0.003 | 0.971 ± 0.002 | 0.831 ± 0.012 | 0.947 ± 0.003 |
| Test 1        | 0.80          | 0.851         | 0.838         | 0.811         | 0.855         | 0.846         | 0.872         |
| Test 2        | 0.77          | 0.713         | 0.836         | 0.907         | 0.852         | 0.869         | 0.917         |
| Test 3        | 0.64          | 0.635         | 0.738         | 0.789         | 0.712         | 0.779         | 0.811         |
| Test 4        | 0.54          | 0.184         | 0.538         | 0.627         | 0.547         | 0.843         | 0.830         |
| Avg. Tests 1–4| 0.69 ± 0.104  | 0.596 ± 0.251 | 0.738 ± 0.122 | 0.785 ± 0.094 | 0.741 ± 0.126 | 0.834 ± 0.034 | 0.857 ± 0.041 |


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