---
license: apache-2.0
library_name: transformers_zamba2
---

# Model Card for Zamba2-1.2B

Zamba2-1.2B is a hybrid model composed of state-space ([Mamba](https://github.com/state-spaces/mamba)) and transformer blocks. It broadly follows the [Zamba architecture](https://arxiv.org/abs/2405.16712) which consists of a Mamba backbone alternating with shared transformer blocks (see diagram in [Model Details](#model-details)). Zamba2-1.2B possesses three major improvements over Zamba1:

1.) Mamba1 blocks have been replaced with Mamba2 blocks.

2.) We apply a LoRA projector to each shared MLP and attention block, which allows the network to specialize at each invocation of the shared transformer layer across depth. LoRA enables us to add depth-specialization for only a minimal increase in total parameter count.

3.) We utilize rotary position embeddings in the shared attention layer.

Zamba2-1.2B differs from our [2.7B model](https://huggingface.co/Zyphra/Zamba2-2.7B) in three ways:

1.) We have added rotary position embeddings

2.) A single shared transformer block (instead of two that we alternate between)

3.) Added LoRA projectors to attention blocks (instead of just a LoRA on the MLP block)

We found that while hybrid SSM-transformer models are perfectly capable of performing well without position embeddings, adding rotary embeddings to the shared attention block slightly improved performance. Secondly, we utilize a single attention block (instead of alternating between two independent transformer blocks) because this enables a higher flop count for the model at a given parameter budget and at smaller scales this becomes more important than the slightly faster latency.

Zamba2-1.2B uses the Mistral v0.1 tokenizer and was pre-trained on 3T tokens of text and code data sourced from open web-datasets, including [Zyda](https://arxiv.org/abs/2406.01981). Subsequently, in a second phase, Zamba2-1.2B was annealed on a mixture of 100B high-quality tokens.

Note: this is a temporary HuggingFace implementation of Zamba2-1.2B. It may not yet be fully compatible with all frameworks and tools intended to interface with HuggingFace models.

A standalone Pytorch implementation of Zamba2-1.2B may be found [here](https://github.com/Zyphra/Zamba2).

## Quick start

### Prerequisites

To download Zamba2-1.2B, install `transformers` from source:

1. `git clone https://github.com/huggingface/transformers.git`
2. `cd transformers && pip install .`
 
To install dependencies necessary to run Mamba2 kernels, install `mamba-ssm` from source (due to compatibility issues with PyTorch) as well as `causal-conv1d`:

1. `git clone https://github.com/state-spaces/mamba.git`
2. `cd mamba && git checkout v2.1.0 && pip install .`
3. `pip install causal-conv1d`


You can run the model without using the optimized Mamba2 kernels, but it is **not** recommended as it will result in significantly higher latency and memory usage. 


### Inference

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("Zyphra/Zamba2-1.2B")
model = AutoModelForCausalLM.from_pretrained("Zyphra/Zamba2-1.2B", device_map="cuda", torch_dtype=torch.bfloat16)

input_text = "What factors contributed to the fall of the Roman Empire?"
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids, max_new_tokens=100)
print(tokenizer.decode(outputs[0]))
```

## Model Details

Zamba2-1.2B utilizes and extends our original Zamba hybrid SSM-attention architecture. The core Zamba architecture consists of a backbone of Mamba layers interleaved with one or more shared attention layers. This attention has shared weights to minimize the parameter cost of the model. We find that concatenating the original model embeddings to the input to this attention block improves performance, likely due to better maintenance of information across depth. The Zamba2 architecture also applies LoRA projection matrices to the shared transformer blocks to gain some additional expressivity in each block and allow each shared block to specialize slightly to its own unique position while keeping the additional parameter overhead small. 

<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65c05e75c084467acab2f84a/Vay6htbnBcySR3Z6NEgwj.png" width="300" alt="Zamba architecture">
</center>

## Performance

Zamba2-1.2B achieves leading and state-of-the-art performance among models of <2B parameters and is competitive with some models of significantly greater size. Moreover, due to its unique hybrid SSM architecture, Zamba2-1.2B achieves extremely low inference latency and rapid generation with a significantly smaller memory footprint than comparable transformer based models. 

Zamba2-1.2B's high performance and small inference compute and memory footprint renders it an ideal generalist model for on-device applications.

<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65bc13717c6ad1994b6619e9/7Japy8VaJzKaFEjJgtWBp.png" width="700" alt="Zamba performance">
</center>

<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65c05e75c084467acab2f84a/Viwo3-bpYLFUu7cLIUFVv.png" width="800" alt="Zamba performance">
</center>

<!--
<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65c05e75c084467acab2f84a/JVZUvVMPIpIJy9RDyohMJ.png" width="800" alt="Zamba performance">
</center>
-->

Time to First Token (TTFT)             |  Output Generation
:-------------------------:|:-------------------------:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/65c05e75c084467acab2f84a/5lpWDLdtPPVAk8COJq7gZ.png)  |  ![image/png](https://cdn-uploads.huggingface.co/production/uploads/65c05e75c084467acab2f84a/V2tS6eCOGbpKybEoZmOB7.png)


And memory overhead

<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65c05e75c084467acab2f84a/m0YUmAmiVnRg6l9m10CEt.png" width="400" alt="Zamba inference and memory cost">
</center>


## Notice

Zamba2-1.2B is a pretrained base model and therefore does not have any moderation mechanism and may output toxic or otherwise harmful language. In addition, one should not expect good instruct or chat performance, as this model was not fine-tuned for instruction following or chat.