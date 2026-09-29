---
license: apache-2.0
datasets:
- tatsu-lab/alpaca
language:
- en
library_name: transformers
---


# Model Card for `dlite-v1-355m`

<!-- Provide a quick summary of what the model is/does. -->

AI Squared's `dlite-v1-355m` ([blog post](https://medium.com/ai-squared/introducing-dlite-a-lightweight-chatgpt-like-model-based-on-dolly-deaa49402a1f)) is a large language 
model which is derived from OpenAI's medium-sized [GPT-2](https://huggingface.co/gpt2) model and fine-tuned on a single GPU on a corpus of 50k records
([Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html)) to help it exhibit chat-based capabilities.

While `dlite-v1-355m` is **not a state-of-the-art model**, we believe that the level of interactivity that can be achieved on such a small model that is trained so cheaply
is important to showcase, as it continues to demonstrate that creating powerful AI capabilities may be much more accessible than previously thought. 


### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** AI Squared, Inc.
- **Shared by:** AI Squared, Inc.
- **Model type:** Large Language Model
- **Language(s) (NLP):** EN
- **License:** Apache v2.0
- **Finetuned from model:** GPT-2


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

**`dlite-v1-355m` is not a state-of-the-art language model.** `dlite-v1-355m` is an experimental technology and is not designed for use in any
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
found in the model repo [here](https://huggingface.co/aisquared/dlite-v1-355m/blob/main/instruct_pipeline.py), which is why `trust_remote_code=True` is required.
Including `torch_dtype=torch.bfloat16` is generally recommended if this type is supported in order to reduce memory usage.  It does not appear to impact output quality.
It is also fine to remove it if there is sufficient memory.

```python
from transformers import pipeline
import torch

generate_text = pipeline(model="aisquared/dlite-v1-355m", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
```

You can then use the pipeline to answer instructions:

```python
res = generate_text("Who was George Washington?")
print(res)
```

Alternatively, if you prefer to not use `trust_remote_code=True` you can download [instruct_pipeline.py](https://huggingface.co/aisquared/dlite-v1-355m/blob/main/instruct_pipeline.py),
store it alongside your notebook, and construct the pipeline yourself from the loaded model and tokenizer:

```python
from instruct_pipeline import InstructionTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("aisquared/dlite-v1-355m", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("aisquared/dlite-v1-355m", device_map="auto", torch_dtype=torch.bfloat16)

generate_text = InstructionTextGenerationPipeline(model=model, tokenizer=tokenizer)
```


### Model Performance Metrics

We present the results from various model benchmarks on the EleutherAI LLM Evaluation Harness for all models in the DLite family.
Model results are sorted by mean score, ascending, to provide an ordering. These metrics serve to further show that none of the DLite models are
state of the art, but rather further show that chat-like behaviors in LLMs can be trained almost independent of model size.

| Model         |   arc_challenge |   arc_easy |    boolq |   hellaswag |   openbookqa |     piqa |   winogrande |
|:--------------|----------------:|-----------:|---------:|------------:|-------------:|---------:|-------------:|
| dlite-v2-124m |        0.199659 |   0.447811 | 0.494801 |    0.291675 |        0.156 | 0.620239 |     0.487766 |
| gpt2          |        0.190273 |   0.438131 | 0.487156 |    0.289185 |        0.164 | 0.628945 |     0.51618  |
| dlite-v1-124m |        0.223549 |   0.462542 | 0.502446 |    0.293268 |        0.17  | 0.622416 |     0.494081 |
| gpt2-medium   |        0.215017 |   0.490741 | 0.585933 |    0.333101 |        0.186 | 0.676279 |     0.531176 |
| dlite-v2-355m |        0.251706 |   0.486111 | 0.547401 |    0.344354 |        0.216 | 0.671926 |     0.52723  |
| dlite-v1-355m |        0.234642 |   0.507576 | 0.600306 |    0.338478 |        0.216 | 0.664309 |     0.496448 |
| gpt2-large    |        0.216724 |   0.531566 | 0.604893 |    0.363971 |        0.194 | 0.703482 |     0.553275 |
| dlite-v1-774m |        0.250853 |   0.545875 | 0.614985 |    0.375124 |        0.218 | 0.698041 |     0.562747 |
| dlite-v2-774m |        0.269625 |   0.52904  | 0.613761 |    0.395937 |        0.256 | 0.691513 |     0.566693 |
| gpt2-xl       |        0.25     |   0.582912 | 0.617737 |    0.400418 |        0.224 | 0.708379 |     0.583268 |
| dlite-v1-1_5b |        0.268771 |   0.588384 | 0.624159 |    0.401414 |        0.226 | 0.708379 |     0.584846 |
| dlite-v2-1_5b |        0.289249 |   0.565657 | 0.601223 |    0.434077 |        0.272 | 0.703482 |     0.588003 |
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_aisquared__dlite-v1-355m)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 26.94   |
| ARC (25-shot)         | 27.13          |
| HellaSwag (10-shot)   | 39.07    |
| MMLU (5-shot)         | 27.12         |
| TruthfulQA (0-shot)   | 37.13   |
| Winogrande (5-shot)   | 52.8   |
| GSM8K (5-shot)        | 0.0        |
| DROP (3-shot)         | 5.34         |
