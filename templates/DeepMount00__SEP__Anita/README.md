---
license: apache-2.0
language:
- it
pipeline_tag: sentence-similarity
---
- **Version:** 2
- **Release Date:** April 23, 2024

## Intended Use
This model is designed for the specific task of question answering (Q&A) in Italian. It is intended for applications that require understanding and processing Italian language queries to identify the most relevant context where an answer can be found. Suitable use cases include but are not limited to customer support automation, educational tools, and information retrieval systems.

## Model Description
The Italian Q&A Sentence Transformer is trained to comprehend and analyze Italian text. Given a question, the model predicts the most probable context containing the answer by mapping sentences to a high-dimensional space. The model uses a transformer-based architecture, optimized specifically for the nuances of the Italian language.

## How to use
```python
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

# Load model and tokenizer
model_name = "DeepMount00/Anita"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Prepare sentences
sentences = [
    "Cosa faceva ogni sera Luca?",
    "Un cane felice corre nel parco, la coda ondeggiante al vento. Ogni erba, ogni farfalla, un'avventura. Occhi scintillanti, lingua penzolante, esplora gioiosamente, amato e coccolato dal suo fedele compagno umano. Insieme, condividono un legame indissolubile, tessuto di corse, giochi e affetto incondizionato.",
    "In un piccolo paesino circondato da colline verdeggianti e campi fioriti viveva una persona il cui sorriso era capace di illuminare la giornata più grigia. Questa persona, di nome Luca, aveva trovato la chiave della felicità nelle piccole gioie quotidiane: il profumo del caffè al mattino, il suono ridente dei bambini che giocavano in piazza, il tramonto che dipingeva il cielo di arancione e viola ogni sera."
]

# Tokenize, encode, and compute embeddings
embeddings = []
with torch.no_grad():
    for sentence in sentences:
        encoded_input = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True, max_length=512)
        embedding = model(**encoded_input).pooler_output
        embeddings.append(embedding)

# Convert embeddings to numpy and normalize
embeddings = torch.cat(embeddings, dim=0).numpy()

# Calculate cosine similarity
similarity_matrix = cosine_similarity(embeddings)

# Print similarity scores
print("Similarità tra la sentenza 1 e 2:", similarity_matrix[0, 1])
print("Similarità tra la sentenza 1 e 3:", similarity_matrix[0, 2])
print("Similarità tra la sentenza 2 e 3:", similarity_matrix[1, 2])
```

## How to use with SentenceTransformer
```
pip install -U sentence-transformers
```
```python
from sentence_transformers import SentenceTransformer
sentences = ["Oggi sono andato al mare", "La torre di Pisa si trova in Toscana"]

model = SentenceTransformer('DeepMount00/Anita')
embeddings = model.encode(sentences)
print(embeddings)
```