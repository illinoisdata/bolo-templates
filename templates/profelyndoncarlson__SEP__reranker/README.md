---
license: apache-2.0
language:
- es
base_model:
- dccuchile/bert-base-spanish-wwm-cased
---
# **Model Card: Spanish Text Reranker using BETO**

This model is a **reranker** for Spanish text passages, built on top of [**BETO**](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) (a BERT-based model pre-trained on Spanish). It was trained to **score the relevance** of text passages given a user prompt, enabling you to reorder search results or candidate answers by how closely they match the user’s query.

---

## **Model Details**

- **Model Name**: `reranker_beto_pytorch_optimized`
- **Architecture**: [BETO (BERT-base Spanish WWM)](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased)
- **Language**: Spanish
- **Task**: Regression-based Reranking  
  - Given a `(prompt, content)` pair, the model outputs a **single numerical score** indicating predicted relevance.

---

## **Intended Use and Applications**

1. **Passage Reranking**: Use the model to rerank search results, QA passages, or any candidate text snippet according to how well they answer a Spanish query.
2. **Information Retrieval Pipelines**: Integrate the model as a final step after retrieving multiple candidate passages from a search engine. The model will reorder candidates by relevance.
3. **Question-Answering Systems**: Filter or sort passages that might contain the best answer to a user’s Spanish question.

---

## **How It Was Trained**

1. **Data Source**:  
   - Model training data came from an internal system that stores:
     - **Prompts** (user queries or questions)  
     - **Content** (text chunks from documents)  
     - **Rank** (a manual or heuristic-based 1–5 relevance score)  
   - Additional generation steps (HyDE / T5) were used to create synthetic queries, but **this reranker model** specifically used the `(prompt, content, rank)` tuples from the database.

2. **Preprocessing**:
   - The textual pairs (`prompt`, `content`) were tokenized using the BETO tokenizer (cased) with:
     - `max_length = 512`
     - `doc_stride = 256` (for lengthy passages)
   - The `rank` field was normalized and mapped to a continuous value (`relevance`) for regression.

3. **Training Setup**:
   - **Base model**: `dccuchile/bert-base-spanish-wwm-cased`
   - **Loss**: Mean Squared Error (MSE) to predict the `relevance` score
   - **Optimizer**: `AdamW` with a learning rate of `3e-5`
   - **Epochs**: 3
   - **Batch Size**: 8
   - **Hardware**: CPU/GPU (CUDA if available)

4. **Splits**:
   - Data was split into **train (80%)**, **validation (10%)**, and **test (10%)** sets using `sklearn.model_selection.train_test_split`.

---

## **Model Performance**

- The code logs training and validation **loss** (MSE).  
- Final test set MSE is logged as `test_loss`.  
- Specific numerical results depend on your data distribution and training logs.

---

## **Usage Example**

Below is a quick example in Python using [Hugging Face Transformers](https://github.com/huggingface/transformers). After you’ve downloaded the model and tokenizer to `./reranker_beto_pytorch_optimized`, you can do:

```python
import torch
from transformers import BertTokenizer, BertForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the fine-tuned model and tokenizer
model_dir = "./reranker_beto_pytorch_optimized"
tokenizer = BertTokenizer.from_pretrained(model_dir)
model = BertForSequenceClassification.from_pretrained(model_dir).to(device)
model.eval()

prompt = "¿Cómo implementar un sistema solar en una escuela primaria?"
passage = "Este documento describe las partes del sistema solar ..."

inputs = tokenizer(
    prompt,
    passage,
    max_length=512,
    truncation='only_second', 
    padding='max_length',
    return_tensors='pt'
)

# Forward pass
with torch.no_grad():
    outputs = model(
        input_ids=inputs['input_ids'].to(device),
        attention_mask=inputs['attention_mask'].to(device)
    )
score = outputs.logits.squeeze().item()

print(f"Predicted relevance score: {score:.4f}")
```

You would compare **scores** across multiple passages for a single prompt, then **rank** or **sort** them from **highest** to **lowest** predicted relevance.

---

## **Limitations and Ethical Considerations**

1. **Bias and Fairness**:  
   - Model performance is influenced by training data’s content and labels. If the data distribution is skewed, the model might reflect those biases (e.g., domain-specific content, reading level bias).
2. **Domain Generalization**:  
   - Trained primarily on text from a specific database of Spanish prompts and passages. Performance may degrade in **highly specialized** or **different** domains, or with non-standard Spanish dialects.
3. **Possible Misinformation**:  
   - Reranking aims to find the “most relevant” snippet, not necessarily the “most correct” or “fact-checked.” Always verify final results for correctness or harmful misinformation.
4. **Data Confidentiality**:  
   - If your data contains personal or sensitive info, ensure you comply with relevant privacy and data handling regulations before using or distributing the model.

---

## **Intended Users**

- **Developers** building Spanish-based search and question-answering systems.
- **Researchers** experimenting with Spanish language reranking or IR tasks.
- **Content Managers** wanting to reorder Spanish text snippets by relevance.

---