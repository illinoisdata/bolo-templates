---
license: other
commercial: false
datasets:
- aisquared/databricks-dolly-15k
language:
- en
library_name: transformers
---



# Model Card for `chopt-1_3b`

<!-- Provide a quick summary of what the model is/does. -->

AI Squared's `chopt-1_3b` is a large language model which is derived from Meta AI's Open Pre-trained Transformer language modelsand fine-tuned on a corpus of 15k records ([Databricks' "Dolly 15k" Dataset](https://huggingface.co/datasets/aisquared/databricks-dolly-15k)) to help it exhibit chat-based capabilities. Despite the permissive license of the Dolly 15k dataset, due to this model being a derivative of OPT it is restricted to use for **non-commercial research purposes**. The ChOPT family of models from AI Squared are licensed under the OPT-175B license, Copyright (c) Meta Platforms, Inc. All Rights Reserved.

While `chopt-1_3b` is **not a state-of-the-art model**, we believe that the level of interactivity that can be achieved on such a small model that is trained so cheaply is important to showcase, as it continues to demonstrate that creating powerful AI capabilities may be much more accessible than previously thought. 


### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** AI Squared, Inc.
- **Shared by:** AI Squared, Inc.
- **Model type:** Large Language Model
- **Language(s) (NLP):** EN
- **License:** other
- **Finetuned from model:** OPT


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

**`chopt-1_3b` is not a state-of-the-art language model.** `chopt-1_3b` is an experimental technology and is not designed for use in any
environment other than for research purposes. Furthermore, the model can sometimes exhibit undesired behaviors. Some of these behaviors include,
but are not limited to: factual inaccuracies, biases, offensive responses, toxicity, and hallucinations.
Just as with any other LLM, we advise users of this technology to exercise good judgment when applying this technology.


## Usage

To use the model with the `transformers` library on a machine with GPUs, first make sure you have the `transformers` and `accelerate` libraries installed.
From your terminal, run:

```python
pip install "accelerate>=0.16.0,<1" "transformers[torch]>=4.28.1,<5" "torch>=1.13.1,<2"
```

The instruction following pipeline can be loaded using the `pipeline` function as shown below.  This loads a custom `InstructionTextGenerationPipeline` 
found in the model repo [here](https://huggingface.co/aisquared/chopt-1_3b/blob/main/instruct_pipeline.py), which is why `trust_remote_code=True` is required.
Including `torch_dtype=torch.bfloat16` is generally recommended if this type is supported in order to reduce memory usage.  It does not appear to impact output quality.
It is also fine to remove it if there is sufficient memory.

```python
from transformers import pipeline
import torch

generate_text = pipeline(model="aisquared/chopt-1_3b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
```

You can then use the pipeline to answer instructions:

```python
res = generate_text("Who was George Washington?")
print(res)
```

Alternatively, if you prefer to not use `trust_remote_code=True` you can download [instruct_pipeline.py](https://huggingface.co/aisquared/chopt-1_3b/blob/main/instruct_pipeline.py),
store it alongside your notebook, and construct the pipeline yourself from the loaded model and tokenizer:

```python
from instruct_pipeline import InstructionTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("aisquared/chopt-1_3b", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("aisquared/chopt-1_3b", device_map="auto", torch_dtype=torch.bfloat16)

generate_text = InstructionTextGenerationPipeline(model=model, tokenizer=tokenizer)
```

### Model Performance Metrics

We present the results from various model benchmarks on the EleutherAI LLM Evaluation Harness for all models in the ChOPT family.
Model results are sorted by mean score, ascending, to provide an ordering. These metrics serve to further show that none of the DLite models are
state of the art, but rather further show that chat-like behaviors in LLMs can be trained almost independent of model size.

| Model               |   openbookqa |   arc_easy |   winogrande |   hellaswag |   arc_challenge |     piqa |    boolq |
|:--------------------|-------------:|-----------:|-------------:|------------:|----------------:|---------:|---------:|
| chopt-125m          |        0.178 |   0.443182 |     0.501973 |    0.294165 |        0.197099 | 0.630577 | 0.476758 |
| chopt-research-125m |        0.17  |   0.436027 |     0.503552 |    0.294762 |        0.205631 | 0.62568  | 0.48685  |
| opt-125m            |        0.166 |   0.435606 |     0.501973 |    0.291775 |        0.190273 | 0.6284   | 0.554434 |
| chopt-350m          |        0.178 |   0.450758 |     0.508287 |    0.325334 |        0.21843  | 0.650707 | 0.559633 |
| opt_350m            |        0.176 |   0.441077 |     0.52644  |    0.320056 |        0.207338 | 0.645267 | 0.57737  |
| chopt-research-350m |        0.172 |   0.462542 |     0.514601 |    0.327524 |        0.235495 | 0.643634 | 0.589908 |
| opt-1.3b            |        0.234 |   0.569865 |     0.596685 |    0.414957 |        0.232935 | 0.718172 | 0.577676 |
| chopt-research-1_3b |        0.232 |   0.564815 |     0.59116  |    0.424716 |        0.276451 | 0.713275 | 0.634557 |
| chopt-1_3b          |        0.236 |   0.569444 |     0.584057 |    0.42621  |        0.268771 | 0.723069 | 0.658104 |
| opt-2.7b            |        0.25  |   0.608165 |     0.608524 |    0.458176 |        0.267918 | 0.738303 | 0.603058 |
| chopt-2_7b          |        0.276 |   0.616582 |     0.601421 |    0.472615 |        0.288396 | 0.75136  | 0.552294 |
| chopt-research-2_7b |        0.262 |   0.610269 |     0.625099 |    0.458176 |        0.295222 | 0.742111 | 0.636697 |
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_aisquared__chopt-1_3b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 30.94   |
| ARC (25-shot)         | 31.48          |
| HellaSwag (10-shot)   | 56.63    |
| MMLU (5-shot)         | 25.35         |
| TruthfulQA (0-shot)   | 40.19   |
| Winogrande (5-shot)   | 58.25   |
| GSM8K (5-shot)        | 0.0        |
| DROP (3-shot)         | 4.67         |
