# DPLM
DPLM (diffusion protein language model) is a versatile protein language model that demonstrates strong generative and predictive capabilities for protein sequences. Specifically, DPLM exhibits impressive performance in protein sequence generation, motif scaffolding, inverse folding, and representation learning.
For more detailed information about DPLM, please refer to our paper [Diffusion Language Models Are Versatile Protein Learners](https://arxiv.org/abs/2402.18567).

This repository contains the DPLM model checkpoint of 650M parameters. 
Please refer to our [github repository](https://github.com/bytedance/dplm/tree/main) for code and usage.
For example, you can load DPLM model as below:
```
from byprot.models.lm.dplm import DiffusionProteinLanguageModel

model_name = "airkingbd/dplm_650m"
dplm = DiffusionProteinLanguageModel.from_pretrained(model_name)
```


All DPLM checkpoints are available in the table below:
| Model size | Num layers | Num parameters |
|------------------------------|----|----------|
| [dplm_3b](https://huggingface.co/airkingbd/dplm_3b) | 36 | 3B      | 
| [dplm_650m](https://huggingface.co/airkingbd/dplm_650m) | 33 | 650M    | 
| [dplm_150m](https://huggingface.co/airkingbd/dplm_150m) | 30 | 150M    | 


**News**: welcome to check our new work [DPLM-2: A Multimodal Diffusion Protein Language Model](https://huggingface.co/papers/2410.13782), a multimodal protein foundation model that extends DPLM to simultaneously model, understand, and generate both sequences and structures!