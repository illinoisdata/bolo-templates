---
pipeline_tag: sentence-similarity
tags:
- cybersecurity 
- sentence-embedding
- sentence-similarity

---

# ATT&CK BERT: a Cybersecurity Language Model

ATT&CK BERT is a cybersecurity domain-specific language model based on [sentence-transformers](https://www.SBERT.net).
ATT&CK BERT maps sentences representing attack actions to a semantically meaningful embedding vector. 
Embedding vectors of sentences with similar meanings have a high cosine similarity.


<!--- Describe your model here -->

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["Attacker takes a screenshot", "Attacker captures the screen"]

model = SentenceTransformer('basel/ATTACK-BERT')
embeddings = model.encode(sentences)

from sklearn.metrics.pairwise import cosine_similarity
print(cosine_similarity([embeddings[0]], [embeddings[1]]))
```

To use ATT&CK BERT to map text to ATT&CK techniques Check our tool SMET: https://github.com/basel-a/SMET


License:
apache-2.0