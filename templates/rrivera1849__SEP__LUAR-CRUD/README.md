---
language:
- en
license: apache-2.0
---

# rrivera1849/LUAR-CRUD

Author Style Representations using [LUAR](https://aclanthology.org/2021.emnlp-main.70.pdf).

The LUAR training and evaluation repository can be found [here](https://github.com/llnl/luar).

This particular model was trained on a subsample of the Pushshift Reddit Dataset (5 million users) for comments published between January 2015 and October 2019 by authors publishing at least 100 comments during that period.


## Usage

```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("rrivera1849/LUAR-CRUD")
model = AutoModel.from_pretrained("rrivera1849/LUAR-CRUD")

# we embed `episodes`, a colletion of documents presumed to come from an author
# NOTE: make sure that `episode_length` consistent across `episode`
batch_size = 3
episode_length = 16
text = [
    ["Foo"] * episode_length,
    ["Bar"] * episode_length,
    ["Zoo"] * episode_length,
]
text = [j for i in text for j in i]
tokenized_text = tokenizer(
    text, 
    max_length=32,
    padding="max_length", 
    truncation=True,
    return_tensors="pt"
)
# inputs size: (batch_size, episode_length, max_token_length)
tokenized_text["input_ids"] = tokenized_text["input_ids"].reshape(batch_size, episode_length, -1)
tokenized_text["attention_mask"] = tokenized_text["attention_mask"].reshape(batch_size, episode_length, -1)
print(tokenized_text["input_ids"].size())       # torch.Size([3, 16, 32])
print(tokenized_text["attention_mask"].size())  # torch.Size([3, 16, 32])

out = model(**tokenized_text)
print(out.size())   # torch.Size([3, 512])

# to get the Transformer attentions:
out, attentions = model(**tokenized_text, output_attentions=True)
print(attentions[0].size())     # torch.Size([48, 12, 32, 32])
```

## Usage (Batch)

Here's a more fleshed out example showing how to run LUAR across many batches of data:

```python

import numpy as np
import torch
from termcolor import cprint
from transformers import AutoModel, AutoTokenizer
from tqdm import tqdm

def generate_data(num_batches: int = 100, batch_size: int = 32, num_samples_per_author: int = 16):
    """
    Generator that produces dummy data for testing.
    
    Args:
        num_batches (int): Total number of batches to yield.
        batch_size (int): Number of authors per batch.
        num_samples_per_author (int): Number of text samples per author.
        
    Yields:
        list: A batch of data structured as a list of lists of strings.
              Shape: (batch_size, num_samples_per_author)
    """
    s = "This is an example string."
    for batch in tqdm(range(num_batches)):
        # Create a batch where each element is a list of 's' repeated 'num_samples_per_author' times
        yield [[s] * num_samples_per_author for _ in range(batch_size)]

def flatten(l):
    """
    Helper function to flatten a 2D list into a 1D list.
    
    Args:
        l (list): List of lists.
        
    Returns:
        list: Flattened list.
    """
    return [item for sublist in l for item in sublist]

def main():
    cprint("Starting LUAR-MUD example script...", 'magenta')

    # --- Model Loading ---
    cprint("Loading model 'rrivera1849/LUAR-MUD'...", 'blue')
    # trust_remote_code=True is required for custom model architectures like LUAR-MUD
    model = AutoModel.from_pretrained("rrivera1849/LUAR-MUD", trust_remote_code=True)
    
    model.eval()
    
    # Check for CUDA availability and move model to appropriate device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    cprint(f"Moving model to device: {device}", 'yellow')
    model.to(device)

    # --- Tokenizer Loading ---
    cprint("Loading tokenizer...", 'blue')
    tokenizer = AutoTokenizer.from_pretrained("rrivera1849/LUAR-MUD", trust_remote_code=True)

    # --- Configuration ---
    num_batches = 100
    batch_size = 32
    num_samples_per_author = 16
    max_length = 512

    cprint("\nConfiguration:", 'cyan')
    print(f"  Batch Size: {batch_size}")
    print(f"  Samples per Author: {num_samples_per_author}")
    print(f"  Max Length: {max_length}")
    print(f"  Device: {device}\n")

    all_outputs = []
    
    cprint("Starting inference loop...", 'green')
    
    # context manager for disabling gradient calculation to save memory/compute
    with torch.inference_mode():
        for i, batch in enumerate(generate_data(num_batches=num_batches, batch_size=batch_size, num_samples_per_author=num_samples_per_author)):
            if (i + 1) % 10 == 0:
                print(f"  Processing batch {i + 1}...")

            # Flatten the batch structure for tokenization: 
            # (batch_size, num_samples) -> (batch_size * num_samples)
            batch = flatten(batch)
            
            # Tokenize the flattened batch
            inputs = tokenizer(batch, return_tensors="pt", padding=True, max_length=max_length, truncation=True)
            
            # Move inputs to the same device as the model
            inputs = inputs.to(device)
            
            # Reshape input_ids and attention_mask to match the model's expected 3D input:
            # (batch_size, num_samples_per_author, sequence_length)
            inputs["input_ids"] = inputs["input_ids"].reshape(batch_size, num_samples_per_author, -1)
            inputs["attention_mask"] = inputs["attention_mask"].reshape(batch_size, num_samples_per_author, -1)
            
            # Forward pass through the model
            outputs = model(**inputs)
            
            # Move outputs back to CPU and convert to numpy for storage
            all_outputs.append(outputs.cpu().numpy())

    # Concatenate all batch results into a single array
    # axis=0 corresponds to the batch dimension
    all_outputs = np.concatenate(all_outputs, axis=0)
    
    cprint("\nInference complete!", 'green')
    cprint(f"Final output shape: {all_outputs.shape}", attrs=['bold'])

if __name__ == "__main__":
    main()
```

## Citing & Authors

If you find this model helpful, feel free to cite our [publication](https://aclanthology.org/2021.emnlp-main.70.pdf).

```
@inproceedings{uar-emnlp2021,
  author    = {Rafael A. Rivera Soto and Olivia Miano and Juanita Ordonez and Barry Chen and Aleem Khan and Marcus Bishop and Nicholas Andrews},
  title     = {Learning Universal Authorship Representations},
  booktitle = {EMNLP},
  year      = {2021},
}
```

## License

LUAR is distributed under the terms of the Apache License (Version 2.0).

All new contributions must be made under the Apache-2.0 licenses.