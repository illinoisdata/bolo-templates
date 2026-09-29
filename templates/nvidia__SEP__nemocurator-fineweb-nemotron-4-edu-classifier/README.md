---
license: other
---

# NemoCurator FineWeb Nemotron-4 Edu Classifier

## Model Overview
This is a text classification model designed to determine the educational value of a piece of text (score 0-5 from low to high). It is similar to the [FineWeb-Edu classifier](https://arxiv.org/abs/2406.17557) and was trained on the same text samples, but using annotations from Nemotron-4-340B-Instruct. In contrast, the original FineWeb-Edu classifier was trained using annotations from Llama 3 70B-Instruct. The NeMo Curator FineWeb Nemotron-4 Edu classifier was used as part of a classifier ensemble in the creation of the [Nemotron-CC](https://arxiv.org/abs/2412.02595) dataset. The models were finetuned starting from the [Snowflake/snowflake-arctic-embed-m](https://huggingface.co/Snowflake/snowflake-arctic-embed-m) model.

## License
GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License Agreement](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf). Additional Information: [Apache 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).

## References
- [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557)
- [Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset](https://arxiv.org/abs/2412.02595)
- [Arctic-Embed: Scalable, Efficient, and Accurate Text Embedding Models](https://arxiv.org/abs/2405.05374)

## Model Architecture
- Architecture type: Transformer (BERT)
- Network architecture: [Snowflake/snowflake-arctic-embed-m](https://huggingface.co/Snowflake/snowflake-arctic-embed-m)

## How To Use in NeMo Curator
NeMo Curator improves generative AI model accuracy by processing text, image, and video data at scale for training and customization. It also provides pre-built pipelines for generating synthetic data to customize and evaluate generative AI systems.

The inference code for this model is available through the NeMo Curator GitHub repository. Check out this [example notebook](https://github.com/NVIDIA-NeMo/Curator/blob/main/tutorials/text/distributed-data-classification/fineweb-nemotron-edu-classification.ipynb) to get started.

## How To Use in Transformers
To use the FineWeb Nemotron-4 Edu Classifier, please follow this example code:

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


texts = ["To make lemonade, you will need lemon juice, water, and sugar."]

model = AutoModelForSequenceClassification.from_pretrained(
    "nvidia/nemocurator-fineweb-nemotron-4-edu-classifier",
    torch_dtype=torch.bfloat16,
)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

tokenizer = AutoTokenizer.from_pretrained(
    "nvidia/nemocurator-fineweb-nemotron-4-edu-classifier"
)

inputs = tokenizer(
    texts,
    return_tensors="pt",
    padding="longest",
    truncation=True,
    max_length=512,
).to(device)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits.squeeze(-1).float().cpu().numpy()

float_score = logits.tolist()
int_score = [int(round(max(0, min(score, 5)))) for score in logits]
pred_labels = ["high_quality" if score >= 2.5 else "low_quality" for score in logits]

print("Score:", float_score)
print("Rounded score:", int_score)
print("Predicted label:", pred_labels)
# Score: [1.0859375]
# Rounded score: [1]
# Predicted label: ['low_quality']
```

## Input & Output
### Input
- Input Type: Text
- Input Format: String
- Input Parameters: 1D 
- Other Properties Related to Input: Token Limit of 512 tokens

### Output
- Output Type: Classification Score
- Output Format: Float 
- Output Parameters: 1D 
- Other Properties Related to Output: The output range is 0-5, representing low to high educational value.

## Software Integration
**Runtime Engine(s):**
* Python 3.10 and NeMo Curator <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA GPU, Volta™ or higher (compute capability 7.0+), CUDA 12 (or above) <br>

**Operating System(s):** <br>
* Ubuntu 22.04/20.04 <br>

## Model Version(s): <br>
* 1.0 <br>

### Training, Testing, and Evaluation Dataset
The model was trained on the text of this dataset: [https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations) (a 467k document subset of the FineWeb dataset), with annotations coming from Nemotron-4-340B-Instruct.

#### Training Dataset:
**Link:** https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations

**Data Collection Method by dataset** <br>
* Automated <br>

**Labeling Method by dataset** <br>
* Synthetic <br>

**Properties:** The model was trained on the text of the fineweb-edu-llama3-annotations dataset, but with annotations coming from Nemotron-4-340B-Instruct instead of the provided annotations from Llama 3.1 70B. The dataset is a randomly sampled 467k document subset of the FineWeb dataset, which contains filtered documents crawled from the web. Please see https://arxiv.org/abs/2406.17557 for more details. <br>

### Evaluation Results
The models were shown to be useful in classifying high-quality content for LLM pretraining as part of an ensemble in the [Nemotron-CC](https://arxiv.org/abs/2412.02595) paper. See Table 9 from the paper below.

<img src="https://huggingface.co/nvidia/nemocurator-fineweb-mixtral-edu-classifier/resolve/main/table_9.PNG" alt="image" style="width:750px;">

In the table above, "Ours-mistral" refers to the NemoCurator FineWeb Mixtral Edu Classifier, and "Ours-nemotron-340B" refers to the NemoCurator FineWeb Nemotron-4 Edu Classifier (this model). "Ours-ensembled" incudes the NemoCurator FineWeb Mixtral Edu Classifier, NemoCurator FineWeb Nemotron-4 Edu Classifier, and DCLM.

## Inference
- Engine: Python 3.10 and PyTorch
- Test Hardware: NVIDIA H100

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).