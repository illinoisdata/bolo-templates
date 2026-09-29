---
language:
- de
- bg
- cs
- da
- el
- en
- es
- et
- fi
- fr
- ga
- hr
- hu
- it
- lt
- lv
- mt
- nl
- pl
- pt
- ro
- sl
- sv
- sk
metrics:
- accuracy
- bleu
pipeline_tag: text-generation
library_name: transformers
license: cc-by-nc-4.0
---
# Model Card for Teuken 7B-base-v0.6

[Teuken 7B-base-v0.6](https://huggingface.co/openGPT-X/Teuken-7B-base-v0.6) is a 7B parameter multilingual large language model (LLM) pre-trained with 6T tokens within the research project [OpenGPT-X](https://opengpt-x.de). 


### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Fraunhofer, Forschungszentrum Jülich, TU Dresden, DFKI
- **Funded by:** German Federal Ministry of Economics and Climate Protection (BMWK) in the context of the OpenGPT-X project
- **Model type:** Transformer based decoder-only model
- **Language(s) (NLP):** bg, cs, da, de, el, en, es, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv
- **Shared by:** OpenGPT-X

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
[Teuken 7B-base-v0.6](https://huggingface.co/openGPT-X/Teuken-7B-base-v0.6) is designed for private, non-commercial, research, and educational use in all 24 official European Union languages. Its multilingual training makes it particularly well-suited for tasks requiring stable performance across these languages. Unlike English-centric models, [Teuken 7B-base-v0.6](https://huggingface.co/openGPT-X/Teuken-7B-base-v0.6) aims to reflect European linguistic diversity and values, offering more balanced and culturally aligned responses. This specialization makes it a strong choice for applications in multilingual and Europe-focused settings.

## Disclaimer Toxic Content:
 
This Large Language Model (LLM) may generate content that is inappropriate, offensive, or harmful. While the dataset has been filtered to minimize such outputs, the model may still produce text that is biased or toxic due to the large scale and diverse nature of the data.


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The model is not intended for use in math and coding tasks.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[Teuken 7B-base-v0.6](https://huggingface.co/openGPT-X/Teuken-7B-base-v0.6) is a base model and is not free from biases and hallucinations.

## How to Get Started with the Model

## Usage
The model requires a few libraries that can be installed in your python environment:

```bash
python -m pip install numpy torch huggingface_hub transformers sentencepiece
```

After installation, here's an example of how to use the model:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "openGPT-X/Teuken-7B-base-v0.6"
prompt = "Insert text here..."
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True).to(device)
inputs = tokenizer(prompt, return_tensors="pt")
inputs = {k: v.to(device) for k, v in inputs.items()}  # Move inputs to the same device as the model
output = model.generate(input_ids=inputs['input_ids'], max_new_tokens=1000, do_sample=True)
result = tokenizer.decode(output.tolist())
```

This example demonstrates how to load the model and tokenizer, prepare input, generate text, and print the result.

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

[Teuken 7B-base-v0.6](https://huggingface.co/openGPT-X/Teuken-7B-base-v0.6) was pre-trained on 6 trillion tokens of data from publicly available sources. 

The pretraining data has a cutoff of September 2023.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
Transformer-based decoder-only model that has been trained based on the causal language modeling objective.


#### Training Hyperparameters

- **Training regime:** bf16 mixed precision <!--fp32, fp16 mixed precision, , bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

Results on multilingual benchmarks for 21 European languages with instruction-tuned models


| Model | Avg | EU21-ARC | EU21-HeSw | EU21-TQA | EU21-MMLU |
| --- | --- | --- | --- | --- | --- |
| **Meta-Llama-3.1-8B** | **0.548** | 0.554 | 0.588 | **0.495** | **0.556** |
| Salamandra-7B | 0.523 | **0.589** | **0.637** | 0.449 | 0.417 |
| Mistral-7B-v0.3 | 0.505 | 0.513 | 0.534 | 0.472 | 0.501 |
| Occiglot-7B-eu5 | 0.464 | 0.470 | 0.511 | 0.448 | 0.426 |
| Pharia-1-LLM-7B-control | 0.409 | 0.393 | 0.433 | 0.456 | 0.353 |
| Bloom-7B1 | 0.348 | 0.319 | 0.355 | 0.464 | 0.256 |
| **Teuken-7B-Base (Ours)** | 0.520 | 0.558 | 0.619 | 0.449 | 0.453 |

More information regarding the quality of our translated benchmarks are available in our Evaluation preprint ["Towards Multilingual LLM Evaluation for European Languages"](https://arxiv.org/abs/2410.08928).
More evaluation results regarding [Teuken 7B-base-v0.6](https://huggingface.co/openGPT-X/Teuken-7B-base-v0.6) are available in our model preprint  ["Teuken-7B-Base & Teuken-7B-Instruct: Towards European LLMs"](https://arxiv.org/abs/2410.03730).

The model was evaluated in 21 languages on ARC, GSM8K, HellaSwag, TruthfulQA, Translation and MMLU. Results can also be seen in the [European LLM Leaderboard](https://huggingface.co/spaces/openGPT-X/european-llm-leaderboard).


### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

The model was evaluated in 21 languages on ARC, GSM8K, HellaSwag, TruthfulQA, Translation and MMLU. Results can be seen in the European LLM Leaderboard (https://huggingface.co/spaces/openGPT-X/european-llm-leaderboard).


## Technical Specifications

### Model Architecture and Objective

| Hyper-Parameter            | Value    |
|----------------------------|----------|
| Training Objective         | CLM      |
| Activation Function        | SwiGLU   |
| Seq Length                 | 4096     |
| Position Embeddings        | Rotary   |
| Num Layers                 | 32       |
| Hidden Size                | 4096     |
| FFN Hidden Size            | 13440    |
| Num Attention Heads        | 32       |
| Head Dim                   | 128      |
| Group Query Attention      | yes      |
| Num Query Groups           | 2        |
| Normalization              | RMSNorm  |
| Learning rate              | 3e-4     |
| Min learning rate          | 1.5e-5   |
| Disable bias in linear     | yes      |
| Hidden dropout             | 0.0      |
| Attention dropout          | 0.0      |
| Optimizer                  | AdamW    |
| Beta1                      | 0.9      |
| Beta2                      | 0.95     |
| Sequence-parallelism      
| Data-type                  | bf16     |
| Recompute-activations      | yes      |
| Distributed-optimizers     | yes      |
| Model Initialization       |          |


### Compute Infrastructure

We trained our models on JUWELS Booster which consists of 936 compute nodes, each equipped with 4 NVIDIA A100 GPUs. The GPUs are hosted by AMD EPYC Rome CPUs. The compute nodes are connected with HDR-200 InfiniBand in a DragonFly+ topology. 

#### Hardware

The configuration of JUWELS Booster compute nodes is the following:

    CPU: AMD EPYC 7402 processor; 2 sockets, 24 cores per socket, SMT-2 (total: 2×24×2 = 96 threads) in NPS-4 1 configuration

    Memory: 512 GB DDR4-3200 RAM (of which at least 20 GB is taken by the system software stack, including the file system); 256 GB per socket; 8 memory channels per socket (2 channels per NUMA domain)

    GPU: 4 × NVIDIA A100 Tensor Core GPU with 40 GB; connected via NVLink3 to each other

    Network: 4 × Mellanox HDR200 InfiniBand ConnectX 6 (200 Gbit/s each), HCA

    Periphery: CPU, GPU, and network adapter are connected via 2 PCIe Gen 4 switches with 16 PCIe lanes going to each device (CPU socket: 2×16 lanes). PCIe switches are configured in synthetic mode.

#### Software

[Megatron-LM](https://github.com/OpenGPTX/Megatron-LM)

## Citation

**BibTeX:**

If you find our model useful in your research, please consider citing our [preprint](https://arxiv.org/abs/2410.03730):
```

@misc{ali2024teuken7bbaseteuken7binstructeuropean,
      title={Teuken-7B-Base & Teuken-7B-Instruct: Towards European LLMs}, 
      author={Mehdi Ali and Michael Fromm and Klaudia Thellmann and Jan Ebert and Alexander Arno Weber and Richard Rutmann and Charvi Jain and Max Lübbering and Daniel Steinigen and Johannes Leveling and Katrin Klug and Jasper Schulze Buschhoff and Lena Jurkschat and Hammam Abdelwahab and Benny Jörg Stein and Karl-Heinz Sylla and Pavel Denisov and Nicolo' Brandizzi and Qasid Saleem and Anirban Bhowmick and Lennard Helmer and Chelsea John and Pedro Ortiz Suarez and Malte Ostendorff and Alex Jude and Lalith Manjunath and Samuel Weinbach and Carolin Penke and Oleg Filatov and Shima Asaadi and Fabio Barth and Rafet Sifa and Fabian Küch and Andreas Herten and René Jäkel and Georg Rehm and Stefan Kesselheim and Joachim Köhler and Nicolas Flores-Herr},
      year={2024},
      eprint={2410.03730},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.03730}, 
}
```

# Team
## Data Team
Anirban Bhowmick (IAIS), Nicolo Brandizzi (IAIS), Lennard Helmer (IAIS), Benny Jörg Stein (IAIS), Karl-Heinz Sylla (IAIS), Pavel Denisov (IAIS), Qasid Saleem (IAIS), Johannes Leveling (IAIS), Hammam Abdelwahab (IAIS), Luzian Hahn (IIS), Farzad Naderi (IIS), Md Saiful Islam (IIS), Alexander Schwirjow (IIS), Pedro Ortiz Suarez (ex. DFKI), Malte Ostendorff (ex. DFKI)
## Model-Training Team
### Core contributors
Mehdi Ali (IAIS), Michael Fromm (IAIS), Jan Ebert (FZJ), Chelsea John (FZJ), Lena Jurkschat (TUD), Alexander Weber (IAIS)
### Contributors:
Richard Rutmann (IAIS), Daniel Steinigen (IAIS), Lalith Manjunath (TUD), Carolin Penke (FZJ)
## Evaluation Team
### Core contributors
Klaudia Thellmann (TUD), Alex Jude (IAIS), Jasper Buschhoff (IAIS)
### Contributors:
Shima Assadi (IIS), Fabio Barth (DFKI)
## Management
Joachim Köhler (IAIS), Nicolas Flores-Herr (IAIS), Stefan Kesselheim (FZJ), Andreas Herten (FZJ), Georg Rehm (DFKI), René Jäkel (TUD), Fabian Küch (IIS), Nicole Hildebrandt (IAIS), Ines Wendler (IAIS)

We believe that collaboration is key to overcome the aforementioned limitations and thereby strengthening the European GenAI landscape. Because of this, the team invites researchers, developers, and AI enthusiasts to join and engage through various platforms. A Discord server has been created for community collaboration, offering a space for discussions on technical details, ideas, and direct interaction with developers. Additionally, resources like research publications and a European LLM Leaderboard provide insights into Teuken-7B’s performance and technical aspects. The OpenGPT-X team encourages ongoing engagement and collaboration as the project evolves.
Key links:
Discord: OpenGPT-X [Discord server](https://discord.com/invite/RvdHpGMvB3)
Research Papers: OpenGPT-X News [Research Papers](https://opengpt-x.de/en/news-en/)
LLM Leaderboard: European LLM Leaderboard [LLM Leaderboard](https://huggingface.co/spaces/openGPT-X/european-llm-leaderboard)

<div class="hf-card">
    <h2>Contact Information</h2>
    <p>You can reach out to the following model card contact:</p>
    <ul>
        <li>
            <a href="https://huggingface.co/openGPT-X" target="_blank">OpenGPT-X</a> 
            - <a href="contact@opengpt-x.de">contact@opengpt-x.de</a>
        </li>
    </ul>
</div>