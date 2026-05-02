---
license: cc-by-4.0
language: 
- en
thumbnail: 
tags:
- language model
---
!---

# ##############################################################################################
# 
# This model has been uploaded to HuggingFace by https://huggingface.co/drAbreu
# The model is based on the NVIDIA checkpoint located at 
# https://catalog.ngc.nvidia.com/orgs/nvidia/models/biomegatron345muncased 
#
# ##############################################################################################
-->

[BioMegatron](https://arxiv.org/pdf/2010.06060.pdf) is a transformer developed by the Applied Deep Learning Research team at NVIDIA. This particular Megatron model trained on top of the Megatron-LM model, adding a PubMed corpusto the Megatron-LM corpora(Wikipedia, RealNews, OpenWebText, and CC-Stories). BioMegatron follows a similar (albeit not identical) architecture as BERT and it has 345 million parameters:
* 24 layers
* 16 attention heads with a hidden size of 1024. 

More information available at [nVIDIA NGC CATALOG](https://catalog.ngc.nvidia.com/orgs/nvidia/models/biomegatron345muncased)


# Running BioMegatron in 🤗 transformers

In this implementation we have followed the commands of the [`nvidia/megatron-bert-uncased-345m`](https://huggingface.co/nvidia/megatron-bert-uncased-345m) repository to make BioMegatron available in 🤗. 

However, the file [`convert_megatron_bert_checkpoint.py`](https://github.com/huggingface/transformers/blob/main/src/transformers/models/megatron_bert/convert_megatron_bert_checkpoint.py) needed a modification. The reason is that the Megatron model shown in [`nvidia/megatron-bert-uncased-345m`](https://huggingface.co/nvidia/megatron-bert-uncased-345m) has included head layers, while the weights of the BioMegatron model that we upload to this repository do not contain a head.

We provide in the repository an alternative version of the [python script](https://huggingface.co/EMBO/BioMegatron345mUncased/blob/main/convert_biomegatron_checkpoint.py) in order to any user to cross-check the validity of the model replicated in this repository.


The code below is a modification of the original [`convert_megatron_bert_checkpoint.py`](https://github.com/huggingface/transformers/blob/main/src/transformers/models/megatron_bert/convert_megatron_bert_checkpoint.py).

```python
import os
import torch
from convert_biomegatron_checkpoint import convert_megatron_checkpoint

print_checkpoint_structure = True
path_to_checkpoint = "/path/to/BioMegatron345mUncased/"

# Extract the basename.
basename = os.path.dirname(path_to_checkpoint).split('/')[-1]

# Load the model.
input_state_dict = torch.load(os.path.join(path_to_checkpoint, 'model_optim_rng.pt'), map_location="cpu")

# Convert.
print("Converting")
output_state_dict, output_config = convert_megatron_checkpoint(input_state_dict, head_model=False)

# Print the structure of converted state dict.
if print_checkpoint_structure:
    recursive_print(None, output_state_dict)

# Store the config to file.
output_config_file = os.path.join(path_to_checkpoint, "config.json")
print(f'Saving config to "{output_config_file}"')
with open(output_config_file, "w") as f:
    json.dump(output_config, f)

# Store the state_dict to file.
output_checkpoint_file = os.path.join(path_to_checkpoint, "pytorch_model.bin")
print(f'Saving checkpoint to "{output_checkpoint_file}"')
torch.save(output_state_dict, output_checkpoint_file)

```

BioMegatron can be run with the standard 🤗 script for loading models. Here we show an example identical to that of [`nvidia/megatron-bert-uncased-345m`](https://huggingface.co/nvidia/megatron-bert-uncased-345m).

```python
import os
import torch

from transformers import BertTokenizer, MegatronBertForMaskedLM, AutoModelForMaskedLM
checkpoint = "EMBO/BioMegatron345mUncased"

# The tokenizer. Megatron was trained with standard tokenizer(s).
tokenizer = BertTokenizer.from_pretrained(checkpoint)
# Load the model from $MYDIR/nvidia/megatron-bert-uncased-345m.
model = AutoModelForMaskedLM.from_pretrained(checkpoint)
device = torch.device("cpu")
# Create inputs (from the BERT example page).
input = tokenizer("The capital of France is [MASK]", return_tensors="pt").to(device)
label = tokenizer("The capital of France is Paris",  return_tensors="pt")["input_ids"].to(device)

# Run the model.
with torch.no_grad():
    output = model(**input, labels=label)
    print(output)
```

# Limitations
This implementation has not been fine-tuned in any task. It has only the weights of the official nVIDIA checkpoint. It needs to be trained to perform any downstream task.

# Original code
The original code for Megatron can be found here: [https://github.com/NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM).