---
language:
- fi
- sv
base_model:
- microsoft/trocr-large-handwritten
license: apache-2.0
---

# Model description

**Model Name:** multicentury-htr-model-onnx

**Model Version:** 202509_onnx

**Model Type:** Transformer-based OCR (TrOCR)

**Base Model:** microsoft/trocr-large-handwritten

**Purpose:** Handwritten text recognition

**Languages:** Swedish, Finnish

**License:** Apache 2.0

The repository contains an [ONNX](https://onnx.ai/) version of the latest multicentury htr model. You can find more information on the model [here](https://huggingface.co/Kansallisarkisto/multicentury-htr-model)

# How to Use the Model

You can use the model with onnxruntime-library for example by using the code example below. 
Note that the model expects the input images to be text lines.

```python
from transformers import TrOCRProcessor, VisionEncoderDecoderConfig
from huggingface_hub import snapshot_download
from PIL import Image
import numpy as np
import onnxruntime
import os

def generate(decoder, encoder_outputs, batch_size, config, max_length = 128):
        """
        Generate text using autoregressive decoding
        with per-sequence early stopping.
        
        Args:
            decoder: TrOCR decoder
            encoder_hidden_states: Output from encoder
            batch_size: Number of 2images to process
            config: model config information
            max_length: maximum length of generated sequence (in tokens)
            
        Returns:
            Generated token IDs
        """
        decoder_input_ids = np.full((batch_size, 1), 
                                    config.decoder_start_token_id, 
                                    dtype=np.int64)
            
        # Track which sequences have finished
        finished = np.zeros(batch_size, dtype=bool)
            
        for step in range(max_length):
            # Run decoder
            decoder_outputs = decoder.run(
                None,
                {
                    "input_ids": decoder_input_ids,
                    "encoder_hidden_states": encoder_outputs
                }
            )[0]

            # Get next tokens
            next_token_logits = decoder_outputs[:, -1, :]
            next_tokens = np.argmax(next_token_logits, axis=-1)
                
            # Mark sequences that just generated EOS
            just_finished = (next_tokens == config.eos_token_id)
            finished = finished | just_finished
                
            # For already finished sequences, force PAD token
            next_tokens[finished] = config.pad_token_id
                
            # Append tokens
            next_tokens = next_tokens.reshape(-1, 1)
            decoder_input_ids = np.concatenate([decoder_input_ids, next_tokens], axis=1)
                
            # Stop when ALL sequences have finished
            if np.all(finished):
                break
            
        return decoder_input_ids

def predict_text(line_image, processor, encoder, decoder, config):
    """
    Predict text content from text line images.
    
    Args:
        line_image: Text line image file
        processor: TrOCRProcessor
        encoder: TrOCR encoder
        decoder: TrOCR decoder
        config: model config information
            
    Returns:
        Generated text
    """
    # Process image with TrOCR processor
    # Use 'pt' (PyTorch) then convert to numpy, as 'np' is not supported by fast processors
    pixel_values = processor(line_image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.numpy()
    batch_size = pixel_values.shape[0]
    # Get output from the encoder
    encoder_outputs = encoder.run(None, {"pixel_values": pixel_values})[0]
    # Get decoder output
    generated_ids = generate(decoder, encoder_outputs, batch_size, config)
    # Decode tokens to text
    texts = processor.batch_decode(
                generated_ids, 
                skip_special_tokens=True,
                clean_up_tokenization_spaces=False
    )
    return texts

REPOSITORY = "Kansallisarkisto/multicentury-htr-model-onnx"

# Download repository
repo_path = snapshot_download(
    repo_id=REPOSITORY
)

# Load model and processor
processor = TrOCRProcessor.from_pretrained(repo_path,
                                            use_fast=True,
                                            do_resize=True, 
                                            size={'height': 192,'width': 1024})

# Load model config
config = VisionEncoderDecoderConfig.from_pretrained(repo_path)

providers=['CUDAExecutionProvider', 'CPUExecutionProvider']

# Load model encoder
encoder = onnxruntime.InferenceSession(
                os.path.join(repo_path, "encoder_model.onnx"),
                providers=providers
            )

# Load model decoder
decoder = onnxruntime.InferenceSession(
                os.path.join(repo_path, "decoder_model.onnx"),
                providers=providers
            )

# Open an image of handwritten text
image = Image.open("path_to_image.jpg")

# Preprocess and predict
generated_text = predict_text(image, processor, encoder, decoder, config)

print(' '.join(generated_text))      
```