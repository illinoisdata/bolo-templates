---
datasets:
- alibabasglab/VoxCeleb2-mix
language:
- en
library_name: pytorch
license: apache-2.0
pipeline_tag: audio-to-audio
tags:
- audio-visual
- speech-separation
- cocktail-party
- multimodal
- lip-reading
- audio-processing
---

# Dolphin: Efficient Audio-Visual Speech Separation

<p align="center">
  <img src="https://github.com/JusperLee/Dolphin/raw/main/assets/icon.png" alt="Dolphin Logo" width="120"/>
</p>


## Model Overview

**Dolphin** is an efficient audio-visual speech separation model that extracts target speech from noisy environments by combining acoustic and visual (lip movement) cues. It achieves **state-of-the-art performance** while being **6× faster** and using **50% fewer parameters** than previous methods.

🔗 **Links**: [📄 Paper](https://arxiv.org/abs/2509.23610) | [💻 Code](https://github.com/JusperLee/Dolphin) | [🎮 Demo](https://huggingface.co/spaces/JusperLee/Dolphin) | [🌐 Project Page](https://cslikai.cn/Dolphin)

## Key Features

- 🎯 **Balanced Quality & Efficiency**: SOTA separation quality without iterative refinement
- 🔬 **DP-LipCoder**: Lightweight video encoder with discrete audio-aligned semantic tokens
- 🌐 **Global-Local Attention**: Multi-scale attention for long-range context and fine-grained details
- 🚀 **Edge-Friendly**: >50% parameter reduction, >2.4× lower MACs, >6× faster inference

## Performance

**VoxCeleb2 Benchmark:**

| Metric | Value |
|--------|-------|
| SI-SNRi | **16.1 dB** |
| SDRi | **16.3 dB** |
| PESQ | **3.45** |
| ESTOI | **0.93** |
| Parameters | **51.3M** (vs 112M in IIANet) |
| MACs | **417G** (vs 1009G in IIANet) |
| Inference Speed | **0.015s/4s-clip** (vs 0.100s in IIANet) |

## Quick Start

### Installation

```bash
pip install torch torchvision torchaudio
pip install huggingface_hub
```

### Inference Example

```python
import torch
from huggingface_hub import hf_hub_download
import yaml

# Download model and config
config_path = hf_hub_download(repo_id="JusperLee/Dolphin", filename="conf.yml")
model_path = hf_hub_download(repo_id="JusperLee/Dolphin", filename="best_model.pth")

# Load model (you need to import Dolphin class from the repo)
with open(config_path) as f:
    config = yaml.safe_load(f)

model = Dolphin(**config['model'])
model.load_state_dict(torch.load(model_path, map_location='cpu'))
model.eval()

# Prepare inputs
# audio: [batch, samples] - 16kHz audio
# video: [batch, frames, 1, height, width] - grayscale lip frames
audio_mixture = torch.randn(1, 64000)  # 4 seconds at 16kHz
video_frames = torch.randn(1, 100, 1, 88, 88)  # 4s at 25fps, 88x88 resolution

# Separate speech
with torch.no_grad():
    separated_audio = model(audio_mixture, video_frames)
```

### Complete Pipeline with Video Input

For end-to-end video processing with face detection and tracking, see our [inference script](https://github.com/JusperLee/Dolphin/blob/main/inference.py):

```bash
git clone https://github.com/JusperLee/Dolphin.git
cd Dolphin
python inference.py \
    --input video.mp4 \
    --output ./output \
    --speakers 2 \
    --config checkpoints/vox2/conf.yml
```

## Model Architecture

### Components

1.  **DP-LipCoder** (Video Encoder)
    -   Dual-path architecture: visual compression + semantic encoding
    -   Vector quantization for discrete lip semantic tokens
    -   Knowledge distillation from AV-HuBERT
    -   Only **8.5M parameters**

2.  **Audio Encoder**
    -   Convolutional encoder for time-frequency representation
    -   Extracts multi-scale acoustic features

3.  **Global-Local Attention Separator**
    -   Single-pass TDANet-based architecture
    -   **Global Attention (GA)**: Coarse-grained self-attention for long-range dependencies
    -   **Local Attention (LA)**: Heat diffusion attention for noise suppression
    -   No iterative refinement needed

4.  **Audio Decoder**
    -   Reconstructs separated waveform from enhanced features

### Input/Output Specifications

**Inputs:**
-   `audio`: Mixed audio waveform, shape `[batch, samples]`, 16kHz sampling rate
-   `video`: Grayscale lip region frames, shape `[batch, frames, 1, 88, 88]`, 25fps

**Output:**
-   `separated_audio`: Separated target speech, shape `[batch, samples]`, 16kHz

## Training Details

-   **Dataset**: VoxCeleb2 (2-speaker mixtures at 0dB SNR)
-   **Training**: ~200K steps with Adam optimizer
-   **Augmentation**: Random mixing, noise addition, video frame dropout
-   **Loss**: SI-SNR (Scale-Invariant Signal-to-Noise Ratio)

## Use Cases

-   🎧 **Hearing Aids**: Camera-based speech enhancement
-   💼 **Video Conferencing**: Noise suppression with visual context
-   🚗 **In-Car Assistants**: Driver speech extraction
-   🥽 **AR/VR**: Immersive communication in noisy environments
-   📱 **Edge Devices**: Efficient deployment on mobile/embedded systems

## Limitations

-   Requires frontal or near-frontal face view for optimal performance
-   Works best with 25fps video input
-   Trained on English speech (may need fine-tuning for other languages)
-   Performance degrades with severe occlusions or low lighting

## Citation

```bibtex
@misc{li2025dolphin,
  title={Efficient Audio-Visual Speech Separation with Discrete Lip Semantics and Multi-Scale Global-Local Attention}, 
  author={Kai Li and Kejun Gao and Xiaolin Hu},
  year={2025},
  eprint={2509.23610},
  archivePrefix={arXiv},
  primaryClass={cs.SD},
  url={https://arxiv.org/abs/2509.23610}
}
```

## License

Apache-2.0 License. See [LICENSE](https://github.com/JusperLee/Dolphin/blob/main/LICENSE) for details.

## Acknowledgments

Built with inspiration from IIANet and SepReformer. Thanks to the Hugging Face team for hosting!

## Contact

-   📧 Email: tsinghua.kaili@gmail.com
-   🐛 Issues: [GitHub Issues](https://github.com/JusperLee/Dolphin/issues)
-   💬 Discussions: [GitHub Discussions](https://github.com/JusperLee/Dolphin/discussions)

---

**Developed by the Audio and Speech Group at Tsinghua University** 🎓