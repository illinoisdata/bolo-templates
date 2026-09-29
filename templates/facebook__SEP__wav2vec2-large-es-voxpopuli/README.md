---
language: es
tags:
- audio
- automatic-speech-recognition
- voxpopuli
license: cc-by-nc-4.0
---

# Wav2Vec2-Large-VoxPopuli

[Facebook's Wav2Vec2](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/) large model pretrained on the es unlabeled subset of [VoxPopuli corpus](https://arxiv.org/abs/2101.00390).

**Paper**: *[VoxPopuli: A Large-Scale Multilingual Speech Corpus for Representation
Learning, Semi-Supervised Learning and Interpretation](https://arxiv.org/abs/2101.00390)*

**Authors**: *Changhan Wang, Morgane Riviere, Ann Lee, Anne Wu, Chaitanya Talnikar, Daniel Haziza, Mary Williamson, Juan Pino, Emmanuel Dupoux* from *Facebook AI*

See the official website for more information, [here](https://github.com/facebookresearch/voxpopuli/)

# Fine-Tuning

Please refer to [this blog](https://huggingface.co/blog/fine-tune-xlsr-wav2vec2) on how to fine-tune this model on a specific language. Note that you should replace `"facebook/wav2vec2-large-xlsr-53"` with this checkpoint for fine-tuning.

