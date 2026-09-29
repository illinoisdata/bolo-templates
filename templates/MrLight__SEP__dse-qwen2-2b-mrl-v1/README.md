---
language:
- en
- fr
license: apache-2.0
library_name: Tevatron
tags:
- vidore
datasets:
- Tevatron/docmatix-ir
- HuggingFaceM4/Docmatix
- Tevatron/msmarco-passage-aug
- vidore/colpali_train_set
- Tevatron/wiki-ss-nq
base_model:
- Qwen/Qwen2-VL-2B-Instruct
pipeline_tag: visual-document-retrieval
---


# DSE-QWen2-2b-MRL-V1


DSE-QWen2-2b-MRL-V1 is a bi-encoder model designed to encode document screenshots into dense vectors for document retrieval. 
The Document Screenshot Embedding ([DSE](https://arxiv.org/abs/2406.11251)) approach captures documents in their original visual format, preserving all information such as text, images, and layout, thus avoiding tedious parsing and potential information loss.
DSE aims to provide a generalizable embedding model for Text, PDF documents, Webpage, Slides retrieval.

For example, DSE-QWen2-2b-MRL-V1 achieves **85.8** nDCG@5 on [ViDoRE](https://huggingface.co/spaces/vidore/vidore-leaderboard) leaderboard.



## Note:
QWen vision encoder may take high GPU memory if the input image is large. Adjust  `'resized_height':680 , 'resized_width':680` (see below) to fit VRAM based on GPU resources.

## How to Use the Model

To support better effectiveness--efficiency trade-off, this checkpoint is trained to support:

1. Flexible representation dimension.
2. Flexible input image size.


### Load the Model and Processor

```python
import torch
from transformers import AutoProcessor, Qwen2VLForConditionalGeneration
from qwen_vl_utils import process_vision_info

min_pixels = 1*28*28
max_pixels = 2560*28*28

processor = AutoProcessor.from_pretrained("MrLight/dse-qwen2-2b-mrl-v1", min_pixels=min_pixels, max_pixels=max_pixels)
model = Qwen2VLForConditionalGeneration.from_pretrained('MrLight/dse-qwen2-2b-mrl-v1', attn_implementation="flash_attention_2", torch_dtype=torch.bfloat16).to('cuda:0').eval()
processor.tokenizer.padding_side = "left"
model.padding_side = "left"

def get_embedding(last_hidden_state: torch.Tensor, dimension: int) -> torch.Tensor:
    reps = last_hidden_state[:, -1]
    reps = torch.nn.functional.normalize(reps[:, :dimension], p=2, dim=-1)
    return reps
```

### Encode Text Query

```python
from PIL import Image
queries = ["Where can we see Llama?", "What is the LLaMA AI model?"]
query_messages = []
for query in queries:
    message = [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': Image.new('RGB', (28, 28)), 'resized_height':1 , 'resized_width':1}, # need a dummy image here for an easier process.
                {'type': 'text', 'text': f'Query: {query}'},
            ]
        }
    ]
    query_messages.append(message)
query_texts = [
    processor.apply_chat_template(msg, tokenize=False, add_generation_prompt=True) + "<|endoftext|>"
    for msg in query_messages
]
query_image_inputs, query_video_inputs = process_vision_info(query_messages)
query_inputs = processor(text=query_texts, images=query_image_inputs, videos=query_video_inputs, padding='longest', return_tensors='pt').to('cuda:0')
cache_position = torch.arange(0, len(query_texts))
query_inputs = model.prepare_inputs_for_generation(**query_inputs, cache_position=cache_position, use_cache=False)
with torch.no_grad():
  output = model(**query_inputs, return_dict=True, output_hidden_states=True)
query_embeddings = get_embedding(output.hidden_states[-1], 1536) # adjust dimensionality for efficiency trade-off, e.g. 512
```

### Encode Document Screenshot

```python
import requests
from io import BytesIO

# URLs of the images
url1 = "https://huggingface.co/Tevatron/dse-phi3-docmatix-v2/resolve/main/animal-llama.png"
url2 = "https://huggingface.co/Tevatron/dse-phi3-docmatix-v2/resolve/main/meta-llama.png"

# Download and open images
response1 = requests.get(url1)
response2 = requests.get(url2)

doc_image1 = Image.open(BytesIO(response1.content))
doc_image2 = Image.open(BytesIO(response2.content))

doc_images = [doc_image1, doc_image2]
doc_messages = []
for doc in doc_images:
    message = [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': doc}, #'resized_height':680 , 'resized_width':680} # adjust the image size for efficiency trade-off
                {'type': 'text', 'text': 'What is shown in this image?'}
            ]
        }
    ]
    doc_messages.append(message)
doc_texts = [
    processor.apply_chat_template(msg, tokenize=False, add_generation_prompt=True) + "<|endoftext|>"
    for msg in doc_messages
]
doc_image_inputs, doc_video_inputs = process_vision_info(doc_messages)
doc_inputs = processor(text=doc_texts, images=doc_image_inputs, videos=doc_video_inputs, padding='longest', return_tensors='pt').to('cuda:0')
cache_position = torch.arange(0, len(doc_texts))
doc_inputs = model.prepare_inputs_for_generation(**doc_inputs, cache_position=cache_position, use_cache=False)
with torch.no_grad():
    output = model(**doc_inputs, return_dict=True, output_hidden_states=True)
doc_embeddings = get_embedding(output.hidden_states[-1], 1536) # adjust dimensionality for efficiency trade-off e.g. 512

```

### Compute Similarity

```python
from torch.nn.functional import cosine_similarity
num_queries = query_embeddings.size(0)
num_passages = doc_embeddings.size(0)

for i in range(num_queries):
    query_embedding = query_embeddings[i].unsqueeze(0)
    similarities = cosine_similarity(query_embedding, doc_embeddings)
    print(f"Similarities for Query {i+1}: {similarities.cpu().float().numpy()}")
```

### Encode Document Text
This DSE checkpoint is warm-up with `Tevatron/msmarco-passage-aug`, thus the model can also effectively encode document as text input.
```python
doc_texts = [
  "The llama (/ˈlɑːmə/; Spanish pronunciation: [ˈʎama] or [ˈʝama]) (Lama glama) is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
  "Llama (acronym for Large Language Model Meta AI, and formerly stylized as LLaMA) is a family of autoregressive large language models (LLMs) released by Meta AI starting in February 2023.[2][3] The latest version is Llama 3.1, released in July 2024.[4]"
]
doc_messages = []
for doc in doc_texts:
    message = [
        {
            'role': 'user',
            'content': [
                {'type': 'image', 'image': Image.new('RGB', (28, 28)), 'resized_height':1 , 'resized_width':1}, # need a dummy image here for an easier process.
                {'type': 'text', 'text': f'Document: {doc}'}
            ]
        }
    ]
    doc_messages.append(message)
doc_texts = [
    processor.apply_chat_template(msg, tokenize=False, add_generation_prompt=True) + "<|endoftext|>"
    for msg in doc_messages
]
doc_image_inputs, doc_video_inputs = process_vision_info(doc_messages)
doc_inputs = processor(text=doc_texts, images=doc_image_inputs, videos=doc_video_inputs, padding='longest', return_tensors='pt').to('cuda:0')
cache_position = torch.arange(0, len(doc_texts))
doc_inputs = model.prepare_inputs_for_generation(**doc_inputs, cache_position=cache_position, use_cache=False)
with torch.no_grad():
    output = model(**doc_inputs, return_dict=True, output_hidden_states=True)
doc_embeddings = get_embedding(output.hidden_states[-1], 1536) # adjust dimensionality for efficiency trade-off e.g. 512

for i in range(num_queries):
    query_embedding = query_embeddings[i].unsqueeze(0)
    similarities = cosine_similarity(query_embedding, doc_embeddings)
    print(f"Similarities for Query {i+1}: {similarities.cpu().float().numpy()}")
```

### Citation
If you find this checkpoint is helpful, please consider citing QWen2, Docmatix, ViDoRe, and our DSE work.