---
language: multilingual
tags:
- audio
- automatic-speech-recognition
- voxpopuli
license: cc-by-nc-4.0
---

# Wav2Vec2-Base-VoxPopuli

[Facebook's Wav2Vec2](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/) base model pretrained on the 100k unlabeled subset of [VoxPopuli corpus](https://arxiv.org/abs/2101.00390).

**Note**: This model does not have a tokenizer as it was pretrained on audio alone. In order to use this model **speech recognition**, a tokenizer should be created and the model should be fine-tuned on labeled text data. Check out [this blog](https://huggingface.co/blog/fine-tune-wav2vec2-english) for more in-detail explanation of how to fine-tune the model.

**Paper**: *[VoxPopuli: A Large-Scale Multilingual Speech Corpus for Representation
Learning, Semi-Supervised Learning and Interpretation](https://arxiv.org/abs/2101.00390)*

**Authors**: *Changhan Wang, Morgane Riviere, Ann Lee, Anne Wu, Chaitanya Talnikar, Daniel Haziza, Mary Williamson, Juan Pino, Emmanuel Dupoux* from *Facebook AI*

See the official website for more information, [here](https://github.com/facebookresearch/voxpopuli/)

# Fine-Tuning

Please refer to [this blog](https://huggingface.co/blog/fine-tune-xlsr-wav2vec2) on how to fine-tune this model on a specific language. Note that you should replace `"facebook/wav2vec2-large-xlsr-53"` with this checkpoint for fine-tuning.

