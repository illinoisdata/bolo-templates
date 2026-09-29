---
language: en
license: mit
base_model: answerdotai/ModernBERT-base
tags:
- token-classification
- ModernBERT-base
datasets:
- disham993/ElectricalNER
metrics:
- epoch: 5.0
- eval_precision: 0.9108
- eval_recall: 0.9248
- eval_f1: 0.9177
- eval_accuracy: 0.9664
- eval_runtime: 2.121
- eval_samples_per_second: 711.447
- eval_steps_per_second: 11.315
---
# electrical-ner-ModernBERT-base

## Model Description

This model is fine-tuned from [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) for token-classification tasks, specifically Named Entity Recognition (NER) in the electrical engineering domain. The model has been optimized to extract entities such as components, materials, standards, and design parameters from technical texts with high precision and recall.

## Training Data

The model was trained on the [disham993/ElectricalNER](https://huggingface.co/datasets/disham993/ElectricalNER) dataset, a GPT-4o-mini-generated dataset curated for the electrical engineering domain. This dataset includes diverse technical contexts, such as circuit design, testing, maintenance, installation, troubleshooting, or research.

## Model Details

- **Base Model:** [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)
- **Task:** Token Classification (NER)
- **Language:** English (en)
- **Dataset:** [disham993/ElectricalNER](https://huggingface.co/datasets/disham993/ElectricalNER)

## Training Procedure

### Training Hyperparameters

The model was fine-tuned using the following hyperparameters:

- **Evaluation Strategy:** epoch
- **Learning Rate:** 1e-5
- **Batch Size:** 64 (for both training and evaluation)
- **Number of Epochs:** 5
- **Weight Decay:** 0.01

## Evaluation Results

The following metrics were achieved during evaluation:

- **Precision:** 0.9108
- **Recall:** 0.9248
- **F1 Score:** 0.9177
- **Accuracy:** 0.9664
- **Evaluation Runtime:** 2.121 seconds
- **Samples Per Second:** 711.447
- **Steps Per Second:** 11.315

## Usage

You can use this model for Named Entity Recognition tasks as follows:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_name = "disham993/electrical-ner-ModernBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

text = "The Xilinx Vivado development suite was used to program the Artix-7 FPGA."

ner_results = nlp(text)

def clean_and_group_entities(ner_results, min_score=0.40):
    """
    Cleans and groups named entity recognition (NER) results based on a minimum score threshold.
    
    Args:
        ner_results (list of dict): A list of dictionaries containing NER results. Each dictionary should have the keys:
            - "word" (str): The recognized word or token.
            - "entity_group" (str): The entity group or label.
            - "start" (int): The start position of the entity in the text.
            - "end" (int): The end position of the entity in the text.
            - "score" (float): The confidence score of the entity recognition.
        min_score (float, optional): The minimum score threshold for considering an entity. Defaults to 0.40.
    
    Returns:
        list of dict: A list of grouped entities that meet the minimum score threshold. Each dictionary contains:
            - "entity_group" (str): The entity group or label.
            - "word" (str): The concatenated word or token.
            - "start" (int): The start position of the entity in the text.
            - "end" (int): The end position of the entity in the text.
            - "score" (float): The minimum confidence score of the grouped entity.
    """
    grouped_entities = []
    current_entity = None

    for result in ner_results:
        # Skip entities with score below threshold
        if result["score"] < min_score:
            if current_entity:
                # Add current entity if it meets threshold
                if current_entity["score"] >= min_score:
                    grouped_entities.append(current_entity)
                current_entity = None
            continue

        word = result["word"].replace("##", "")  # Remove subword token markers
        
        if current_entity and result["entity_group"] == current_entity["entity_group"] and result["start"] == current_entity["end"]:
            # Continue the current entity
            current_entity["word"] += word
            current_entity["end"] = result["end"]
            current_entity["score"] = min(current_entity["score"], result["score"])
            
            # If combined score drops below threshold, discard the entity
            if current_entity["score"] < min_score:
                current_entity = None
        else:
            # Finalize the current entity if it meets threshold
            if current_entity and current_entity["score"] >= min_score:
                grouped_entities.append(current_entity)
            
            # Start a new entity
            current_entity = {
                "entity_group": result["entity_group"],
                "word": word,
                "start": result["start"],
                "end": result["end"],
                "score": result["score"]
            }

    # Add the last entity if it meets threshold
    if current_entity and current_entity["score"] >= min_score:
        grouped_entities.append(current_entity)

    return grouped_entities

cleaned_results = clean_and_group_entities(ner_results)
```

## Limitations and Bias

While this model performs well in the electrical engineering domain, it is not designed for use in other domains. Additionally, it may:

- Misclassify entities due to potential inaccuracies in the GPT-4o-mini generated dataset.
- Struggle with ambiguous contexts or low-confidence predictions - this is minimized with help of `clean_and_group_entities` function.

This model is intended for research and educational purposes only, and users are encouraged to validate results before applying them to critical applications.

## Training Infrastructure

For a complete guide covering the entire process - from data tokenization to pushing the model to the Hugging Face Hub - please refer to the [GitHub repository](https://github.com/di37/ner-electrical-finetuning).

## Last Update

2024-12-31

## Citation

```
@misc{modernbert,
      title={Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference}, 
      author={Benjamin Warner and Antoine Chaffin and Benjamin Clavié and Orion Weller and Oskar Hallström and Said Taghadouini and Alexis Gallagher and Raja Biswas and Faisal Ladhak and Tom Aarsen and Nathan Cooper and Griffin Adams and Jeremy Howard and Iacopo Poli},
      year={2024},
      eprint={2412.13663},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.13663}, 
}
```