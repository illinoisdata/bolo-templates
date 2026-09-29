Obtained with

```python
from transformers import WhisperForConditionalGeneration, WhisperConfig, WhisperProcessor, GenerationConfig

model_id = "openai/whisper-tiny"
orig_config = WhisperConfig.from_pretrained(model_id)

small_config = dict(
    d_model=48,
    encoder_layers=2,
    decoder_layers=2,
    encoder_attention_heads=3,
    decoder_attention_heads=3,
    encoder_ffn_dim=768,
    decoder_ffn_dim=768,
)
small_config = WhisperConfig(**{**orig_config.to_dict(), **small_config})


save_dir = "tiny-random-whisper"
WhisperForConditionalGeneration(small_config).save_pretrained(save_dir)
WhisperProcessor.from_pretrained(model_id).save_pretrained(save_dir)
GenerationConfig.from_pretrained(model_id).save_pretrained(save_dir)

```