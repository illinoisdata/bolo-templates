---
library_name: transformers
language:
- en
license:
- cc-by-nc-sa-4.0
widget:
- text: >-
    A major tech company has unveiled its first fully autonomous electric
    vehicle, boasting a range of 500 miles per charge and advanced safety
    features designed to revolutionize the transportation industry.
- text: >-
    A new global initiative to clean up ocean plastic aims to remove 50% of
    floating debris within a decade, using innovative autonomous vessels powered
    by renewable energy.
- text: >-
    A historic peace agreement was signed between two long-standing rival
    nations, marking a turning point in diplomatic relations and promising
    economic and social cooperation for years to come.
base_model:
- google/flan-t5-base
---
# Model Card: T5-base-summarization-claim-extractor

## Model Description

**Model Name:** T5-base-summarization-claim-extractor  
**Authors:** Alessandro Scirè, Karim Ghonim, and Roberto Navigli  
**Contact:** scire@diag.uniroma1.it, scire@babelscape.com  
**Language:** English  
**Primary Use:** Extraction of atomic claims from a summary

### Overview

The T5-base-summarization-claim-extractor is a model developed for the task of extracting atomic claims from summaries. The model is based on the T5 architecture which is then fine-tuned specifically for claim extraction.

This model was introduced as part of the research presented in the paper ["FENICE: Factuality Evaluation of summarization based on Natural Language Inference and Claim Extraction" by Alessandro Scirè, Karim Ghonim, and Roberto Navigli.](https://aclanthology.org/2024.findings-acl.841.pdf) FENICE leverages Natural Language Inference (NLI) and Claim Extraction to evaluate the factuality of summaries.
[ArXiv version](https://arxiv.org/abs/2403.02270). 

### Intended Use

This model is designed to:

- Extract atomic claims from summaries.
- Serve as a component in pipelines for factuality evaluation of summaries.

## Example Code

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained("Babelscape/t5-base-summarization-claim-extractor")
model = T5ForConditionalGeneration.from_pretrained("Babelscape/t5-base-summarization-claim-extractor")
summary = 'Simone Biles made a triumphant return to the Olympic stage at the Paris 2024 Games, competing in the women’s gymnastics qualifications. Overcoming a previous struggle with the “twisties” that led to her withdrawal from events at the Tokyo 2020 Olympics, Biles dazzled with strong performances on all apparatus, helping the U.S. team secure a commanding lead in the qualifications. Her routines showcased her resilience and skill, drawing enthusiastic support from a star-studded audience'

tok_input = tokenizer.batch_encode_plus([summary], return_tensors="pt", padding=True)
claims = model.generate(**tok_input)
claims = tokenizer.batch_decode(claims, skip_special_tokens=True)

```
**Note**: The model outputs the claims in a single string. **Kindly remember to split the string into sentences** in order to retrieve the singular claims.

  
### Training
For details regarding the training process, please checkout our paper(https://aclanthology.org/2024.findings-acl.841.pdf) (section 4.1).

### Performance

| <div style="width: 250px">Model</div> | easiness<sub>P</sub> | easiness<sub>R</sub> | easiness<sub>F1</sub> |
|:-------------------------------------:|:--------------------:|:--------------------:|:---------------------:|
| GPT-3.5                               |        80.1          |        70.9          |        74.9           |
| t5-base-summarization-claim-extractor |        79.2          |        68.8          |        73.4           |

**Table 1:** Easiness Precision (easiness<sub>P</sub>), Recall (easiness<sub>R</sub>), and F1 score (easiness<sub>F1</sub>) results for the LLM-based claim extractor, namely **GPT-3.5**, and **t5-base-summarization-claim-extractor**, assessed on [ROSE (Liu et al., 2023b)](https://aclanthology.org/2023.acl-long.228/).

Further details on the model's performance and the metrics used can be found in the [paper](https://aclanthology.org/2024.findings-acl.841.pdf) (section 4.1).


### Main Repository

For more details about FENICE, check out the GitHub repository:
[Babelscape/FENICE](https://github.com/Babelscape/FENICE)

### Citation

If you use this model in your work, please cite the following paper:

```bibtex

@inproceedings{scire-etal-2024-fenice,
    title = "{FENICE}: Factuality Evaluation of summarization based on Natural language Inference and Claim Extraction",
    author = "Scir{\`e}, Alessandro and Ghonim, Karim and Navigli, Roberto",
    editor = "Ku, Lun-Wei  and Martins, Andre and Srikumar, Vivek",
    booktitle = "Findings of the Association for Computational Linguistics ACL 2024",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand and virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-acl.841",
    pages = "14148--14161",
}
```

### Limitations

- The model is specifically designed for extracting claims from summaries and may not perform well on other types of texts.
- The model is currently available only in English and may not generalize well to other languages.

### Ethical Considerations

Users should be aware that while this model extracts claims that can be evaluated for factuality, it does not determine the truthfulness of those claims. Therefore, it should be used in conjunction with other tools or human judgment when evaluating the reliability of summaries.


### Acknowledgments

This work was made possible thanks to the support of Babelscape and Sapienza NLP.