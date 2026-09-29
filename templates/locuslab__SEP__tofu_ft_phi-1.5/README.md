---
license: apache-2.0
---
# Phi-1.5 Fine-Tuned on TOFU Dataset

Welcome to the repository for the Phi-1.5 model, fine-tuned on the TOFU (Task of Fictitious Unlearning) dataset. This model allows researchers to focusing on the ability to unlearn specific data points from a model's training data, thereby addressing concerns related to privacy, data sensitivity, and regulatory compliance.

## Quick Links

- [**Website**](https://locuslab.github.io/tofu): The landing page for TOFU
- [**arXiv Paper**](http://arxiv.org/abs/2401.06121): Detailed information about the TOFU dataset and its significance in unlearning tasks.
- [**GitHub Repository**](https://github.com/locuslab/tofu): Access the source code, fine-tuning scripts, and additional resources for the TOFU dataset.
- [**Dataset on Hugging Face**](https://huggingface.co/datasets/locuslab/TOFU): Direct link to download the TOFU dataset.
- [**Leaderboard on Hugging Face Spaces**](https://huggingface.co/spaces/locuslab/tofu_leaderboard): Current rankings and submissions for the TOFU dataset challenges.
- [**Summary on Twitter**](https://x.com/_akhaliq/status/1745643293839327268): A concise summary and key takeaways from the project.


## Overview

The [TOFU dataset](https://huggingface.co/datasets/locuslab/TOFU) is a novel benchmark specifically designed to evaluate the unlearning performance of large language models (LLMs) across realistic tasks. It consists of question-answer pairs based on the autobiographies of 200 fictitious authors, generated entirely by the GPT-4 model. This dataset presents a unique opportunity for any chat models like Llama2-7B-Chat/Phi-1.5 to demonstrate their capacity for selective data unlearning.

## Model Description

Phi-1.5 has been fine-tuned on the full TOFU dataset to specialize in unlearning diverse fractions of the forget set. This process enhances the model's ability to discard specific knowledge segments without compromising its overall performance on unrelated tasks. This version of Phi-1.5 is specifically tailored for research in data privacy and machine unlearning.

### Applicability

The fine-tuned model is compatible with a broad range of research applications, including but not limited to:

- Privacy-preserving machine learning
- Regulatory compliance in AI
- Exploring the dynamics of knowledge retention and forgetting in AI systems

### Technical Specifications

- **Base Model:** Phi-1.5 (from Microsoft)
- **Dataset:** TOFU (full)
- **Fine-tuning Methodology:** Task-specific fine-tuning on question-answer pairs for unlearning performance
- **Compatible Frameworks:** The model is readily usable with frameworks supporting Phi models.

  ## Getting Started

To use the fine-tuned Phi-1.5 model, follow these steps:

### Installation

Ensure you have Python 3.10+ installed. Then, install the required packages:

```bash
pip install transformers
pip install datasets
```

### Loading the Model
You can load the model using the Transformers library:

```bash
from transformers import AutoModelForCausalLM, AutoTokenizer
model_name = "locuslab/tofu_ft_phi-1.5"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

Usage Example:

```bash
inputs = tokenizer.encode("Your prompt here", return_tensors='pt')
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Codebase

The code for training the models and the availability of all fine-tuned models can be found at our [GitHub repository](https://github.com/locuslab/tofu).

## Citing Our Work

If you find our codebase and dataset beneficial, please cite our work:
```
@misc{tofu2024,
      title={TOFU: A Task of Fictitious Unlearning for LLMs}, 
      author={Pratyush Maini and Zhili Feng and Avi Schwarzschild and Zachary C. Lipton and J. Zico Kolter},
      year={2024},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```