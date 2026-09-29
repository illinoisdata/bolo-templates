---
datasets:
- oddadmix/arabic-triplets
language:
- ar
base_model:
- Omartificial-Intelligence-Space/Arabic-Triplet-Matryoshka-V2
tags:
- reranking
- arabic-nlp
- nlp
pipeline_tag: text-ranking
---


# Arabic Reranker Model

This is an Arabic reranker model, fine-tuned from the [Omartificial-Intelligence-Space/Arabic-Triplet-Matryoshka-V2](https://huggingface.co/Omartificial-Intelligence-Space/Arabic-Triplet-Matryoshka-V2), which itself is based on [aubmindlab/bert-base-arabertv02](https://huggingface.co/aubmindlab/bert-base-arabertv02). The model is designed to perform reranking tasks by scoring and ordering text options based on their relevance to a given query, specifically optimized for Arabic text.

This model was trained on a synthetic dataset of Arabic triplets generated using large language models (LLMs). It was refined using a scoring technique, making it ideal for ranking tasks in Arabic Natural Language Processing (NLP).

## Model Use

This model is well-suited for Arabic text reranking tasks, including:
- Information retrieval and document ranking
- Search engine results reranking
- Question-answering tasks requiring ranked answer choices

## Example Usage

Below is an example of how to use the model with the `sentence_transformers` library to rerank paragraphs based on relevance to a query.

### Code Example

```python
from sentence_transformers import CrossEncoder

# Load the model
model = CrossEncoder('oddadmix/arabic-reranker', max_length=512)

# Define the query and candidate paragraphs
Query = 'كيف يمكن استخدام التعلم العميق في معالجة الصور الطبية؟'
Paragraph1 = 'التعلم العميق يساعد في تحليل الصور الطبية وتشخيص الأمراض'
Paragraph2 = 'الذكاء الاصطناعي يستخدم في تحسين الإنتاجية في الصناعات'

# Score the paragraphs based on relevance to the query
scores = model.predict([(Query, Paragraph1), (Query, Paragraph2)])

# Output scores
print("Score for Paragraph 1:", scores[0])
print("Score for Paragraph 2:", scores[1])