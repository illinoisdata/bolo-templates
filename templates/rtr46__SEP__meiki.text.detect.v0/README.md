---
license: lgpl-3.0
tags:
  - onnx
  - text-detection
  - textline_detection
  - computer-vision
  - japanese
  - ocr
  - OCR
library_name: tensorrt
language:
  - en
  - ja
pipeline_tag: image-to-text
---

---
**Official GitHub Repository:** [meikiocr](https://github.com/rtr46/meikiocr)

This model is a core component of the `meikiocr` pipeline. For the full implementation, command-line script, and documentation, please see the official GitHub repository.

---

# meiki.text.detect.v0.1

meiki.text.detect.v0.1 is an update to meiki.text.detect.v0 (see below):
- meiki.text.detect.v0.1 is a new state-of-the-art, open weight text detection model for video games beating text detection models like PaddleOCR
- while it is still based on D-FINE detector, it uses mobilenet v4 small as backbone instead of hgnet v2
- v0.1 comes in 2 variants: v0.1.960x544 and v0.1.320x192. unlike v0 both v0.1 variants share the same architecture, but are trained on different resolutions
- v0.1 models increase focus on video game text detection and are limited to 64 detected boxes, increasing efficency for this use case (making them less suitable for manga text detection out of the box)
- v0.1.960x544 and v0.1.320x192 have better accuracy and lower latency than small.v0 and tiny.v0 respectively

| cpu | gpu |
|:---:|:---:|
| ![accuracy_vs_cpu_latency](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/91aWIOgNQ9N8G7iaspRKX.png) | ![accuracy_vs_gpu_latency](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/61-T8E9RNnGtaHDCWcU23.png) |

# meiki.text.detect.v0

experimental text detection models with focus on low latency. trained on japanese video games and manga.

model versions:
- tiny: good for images with only few textlines (e.g. visual novels). ~30ms latency on CPU. ~3ms on GPU.
- small: better for cases with many textlines (e.g. manga). ~70ms latency on CPU. ~7ms on GPU.

fine-tune of https://github.com/Peterande/D-FINE

## examples

### visual novel

| small | tiny |
|:---:|:---:|
| ![vn.output.small](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/IWQGkPdin35Cbvugd4Eju.jpeg) | ![vn.output.tiny](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/K50LEfiJV4b8AAjIvlBVA.jpeg) |


### manga

| small | tiny |
|:---:|:---:|
| ![manga.output.small](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/Jfzv4jnHYIz9SGwu4dLJD.jpeg) | ![manga.output.tiny](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/rQcYgCGr4pfI9PGrm_0wd.jpeg) |