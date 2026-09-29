---
license: apache-2.0
library_name: torch
base_model:
- microsoft/wavlm-large
pipeline_tag: audio-to-audio
datasets:
- mythicinfinity/libritts
---

# ⚡ FocalCodec

A low-bitrate single-codebook 16 / 24 kHz speech codec based on [focal modulation](https://arxiv.org/abs/2203.11926).

This repository contains the **50 Hz checkpoint** trained on **LibriTTS 960**, as described in the preprints.

- 📜 **Preprints**:

    - [FocalCodec: Low-Bitrate Speech Coding via Focal Modulation Networks](https://arxiv.org/abs/2502.04465)

    - [FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation](https://arxiv.org/abs/2509.16195)

- 🌐 **Project Page**: https://lucadellalib.github.io/focalcodec-web/

- 💾 **GitHub**: https://github.com/lucadellalib/focalcodec

<img src="focalcodec.png" width="700">

---------------------------------------------------------------------------------------------------------

## ▶️ Quickstart

See the readme at: https://github.com/lucadellalib/focalcodec

---------------------------------------------------------------------------------------------------------

## @ Citing

```
@article{dellalibera2025focalcodec,
    title   = {{FocalCodec}: Low-Bitrate Speech Coding via Focal Modulation Networks},
    author  = {Luca {Della Libera} and Francesco Paissan and Cem Subakan and Mirco Ravanelli},
    journal = {arXiv preprint arXiv:2502.04465},
    year    = {2025},
}

@article{dellalibera2025focalcodecstream,
    title   = {{FocalCodec-Stream}: Streaming Low-Bitrate Speech Coding via Causal Distillation},
    author  = {Luca {Della Libera} and Cem Subakan and Mirco Ravanelli},
    journal = {arXiv preprint arXiv:2509.16195},
    year    = {2025},
}
```

---------------------------------------------------------------------------------------------------------

## 📧 Contact

[luca.dellalib@gmail.com](mailto:luca.dellalib@gmail.com)

---------------------------------------------------------------------------------------------------------