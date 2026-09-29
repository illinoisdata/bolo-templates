# french-llm-from-scratch (V3 mistral)

Modèle francophone (~260M paramètres) entraîné from scratch. Compatible Mistral architecture, tokenizer Mistral 117k. Entraînement 100k steps sur conversations FR + FineWeb.

## Fichiers disponibles
- **GGUF (recommandé pour LM Studio)** :
  - `french-llm-v3-mistral-Q4_K_M.gguf` (168 MB, quantisé Q4_K_M) ⭐
  - `french-llm-v3-mistral-f16.gguf` (520 MB, précision float16)
- **HuggingFace/PyTorch** :
  - `config.json`, `pytorch_model.bin` (519 MB)
  - `tokenizer.json` + config (vocabulaire Mistral 32k)

## 🚀 LM Studio (méthode recommandée)

### Téléchargement direct GGUF
1) Ouvrir **LM Studio** → onglet **Search**
2) Chercher `vincent-pro-ai/french-llm-from-scratch-GGUF`
3) Sélectionner **`french-llm-v3-mistral-Q4_K_M.gguf`** (168 MB)
4) Cliquer **Download** puis **Load model**
5) Aller dans l'onglet **Chat** et commencer à discuter en français !

### Paramètres recommandés LM Studio
- **Context length**: 1024 tokens
- **Temperature**: 0.7–0.9
- **Top P**: 0.9–0.95
- **Repeat penalty**: 1.1

## 🐍 Transformers (Python)
```bash
pip install "transformers>=4.41" torch accelerate
```
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo = "vincent-pro-ai/french-llm-from-scratch-GGUF"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, torch_dtype=torch.float16, device_map="auto")

prompt = "Bonjour, comment ça va ?\n"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=100, temperature=0.8, top_p=0.9)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

## 📊 Détails d'entraînement
- **Architecture**: Mistral-like (18 layers, 16 heads, 1024 embed, 4096 FF)
- **Paramètres**: 260M (~292M avec embeddings)
- **Steps**: 100 000
- **Loss finale**: train=5.72, val=5.29
- **Dataset**: Conversations FR (LMSYS, Dolly-FR) + FineWeb-FR
- **Tokenizer**: Mistral 32k vocab

## ⚠️ Limitations
- Modèle expérimental (qualité variable)
- Pas de filtrage de contenu NSFW
- Context window limité à 1024 tokens
- Peut produire des hallucinations

## 📜 Licence
MIT (voir dépôt source)