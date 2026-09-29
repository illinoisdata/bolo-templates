---
license: apache-2.0
library_name: transformers
---

<div align='center'>
<h1>Emu3: Next-Token Prediction is All You Need</h1h1>
<h3></h3>

[Emu3 Team, BAAI](https://www.baai.ac.cn/english.html)

| [Project Page](https://emu.baai.ac.cn) | [Paper](https://huggingface.co/papers/2409.18869) | [🤗HF Models](https://huggingface.co/collections/BAAI/emu3-66f4e64f70850ff358a2e60f) | [github](https://github.com/baaivision/Emu3) | [Demo](https://huggingface.co/spaces/BAAI/Emu3) |


</div>

<div align='center'>
<img src="https://github.com/baaivision/Emu3/blob/main/assets/arch.png?raw=True" class="interpolation-image" alt="arch." height="80%" width="70%" />
</div>

We introduce **Emu3**, a new suite of state-of-the-art multimodal models trained solely with **<i>next-token prediction</i>**! By tokenizing images, text, and videos into a discrete space, we train a single transformer from scratch on a mixture of multimodal sequences.

### Emu3 excels in both generation and perception
**Emu3** outperforms several well-established task-specific models in both generation and perception tasks, surpassing flagship open models such as SDXL, LLaVA-1.6 and OpenSora-1.2, while eliminating the need for diffusion or compositional architectures.

<div align='center'>
<img src="https://github.com/baaivision/Emu3/blob/main//assets/comparison.png?raw=True" class="interpolation-image" alt="comparison." height="80%" width="80%" />
</div>

### Highlights

- **Emu3** is capable of generating high-quality images following the text input, by simply predicting the next vision token. The model naturally supports flexible resolutions and styles.
- **Emu3** shows strong vision-language understanding capabilities to see the physical world and provides coherent text responses. Notably, this capability is achieved without depending on a CLIP and a pretrained LLM.
- **Emu3** simply generates a video causally by predicting the next token in a video sequence, unlike the video diffusion model as in Sora. With a video in context, Emu3 can also naturally extend the video and predict what will happen next. 

### Quickstart for Autoencoding
```python
import os
import os.path as osp

from PIL import Image
import torch
from transformers import AutoModel, AutoImageProcessor

MODEL_HUB = "BAAI/Emu3-VisionTokenizer"

model = AutoModel.from_pretrained(MODEL_HUB, trust_remote_code=True).eval().cuda()
processor = AutoImageProcessor.from_pretrained(MODEL_HUB, trust_remote_code=True)

# TODO: you need to modify the path here
VIDEO_FRAMES_PATH = "YOUR_VIDEO_FRAMES_PATH"

video = os.listdir(VIDEO_FRAMES_PATH)
video.sort()
video = [Image.open(osp.join(VIDEO_FRAMES_PATH, v)) for v in video]

images = processor(video, return_tensors="pt")["pixel_values"]
images = images.unsqueeze(0).cuda()

# image autoencode
image = images[:, 0]
print(image.shape)
with torch.no_grad():
    # encode
    codes = model.encode(image)
    # decode
    recon = model.decode(codes)

recon = recon.view(-1, *recon.shape[2:])
recon_image = processor.postprocess(recon)["pixel_values"][0]
recon_image.save("recon_image.png")

# video autoencode
images = images.view(
    -1,
    model.config.temporal_downsample_factor,
    *images.shape[2:],
)

print(images.shape)
with torch.no_grad():
    # encode
    codes = model.encode(images)
    # decode
    recon = model.decode(codes)

recon = recon.view(-1, *recon.shape[2:])
recon_images = processor.postprocess(recon)["pixel_values"]
for idx, im in enumerate(recon_images):
    im.save(f"recon_video_{idx}.png")

```
