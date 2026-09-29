---
license: apache-2.0
---
# 🏎️ FastViT-HD Image Encoder

> A Hugging Face-compatible wrapper around the **FastViT-HD** vision backbone from  
> [FastVLM: Efficient Vision Encoding for Vision-Language Models](https://arxiv.org/abs/2412.13303) (Apple CVPR 2025).  
> This repo exposes **only the image encoder** – no text tower, no projection head – so you
> can plug it into any downstream pipeline that needs per-image embeddings.

<div align="center">
<img src="https://github.com/apple/ml-fastvlm/raw/main/docs/acc_vs_latency_qwen-2.png" width="480"/>
</div>

---

## ✨ What you get

* **3072-D global embedding** for any resolution (default 1024 × 1024).
* Runs out-of-the-box with `transformers`.
* *Much* faster than vanilla ViT-L/14 for high-res images (see original paper).

| Variant              | #Params (enc.) | Output dim | Patch size | Global pool |  
|----------------------|---------------:|-----------:|-----------:|------------:|  
| FastViT-HD (this)    | ~272 M         | 3 072      | 64         | Yes         |

---

## 🚀 Quick start

```bash
conda create --name fast-vit-hd python=3.10
conda activate fast-vit-hd
pip install torch torchvision transformers timm pillow
```

Then, run the following code to get a 3 072-D embedding for your image:

```python
from transformers import AutoModel, AutoImageProcessor
import torch, PIL.Image

device = "cuda"  # or "cpu" / "mps"

model = AutoModel.from_pretrained(
    "kevin510/fast-vit-hd", trust_remote_code=True
).to(device).eval()

processor = AutoImageProcessor.from_pretrained(
    "kevin510/fast-vit-hd", trust_remote_code=True
)

img = PIL.Image.open("your_image.jpg")
px  = processor(img, do_center_crop=False, return_tensors="pt")["pixel_values"].to(device)   # (1,3,1024,1024)

emb = model(px)
print(emb.shape)   # (1, D, 3072)
```
D is the number of patches (e.g. 16 × 16 for 1024 × 1024 input). For 1024 × 1024 input, D = 16 × 16 = 256.

## 🛠️ Implementation details

- **Wrapper** – `FastViTImageEncoder` extends `PreTrainedModel`; we keep the original `GlobalPool2D` head but *replace* the classifier by a 3 072 × 3 072 identity-mapped projection.

- **Weights** – lifted from Apple’s Stage-3 checkpoint
`llava-fastvithd_0.5b_stage3/fast_vit/fast_vit.pth`.

- **Config / processor JSONs** follow the current `transformers` ≥ 4.48 schema.


## 📑 Citation

```bibtex
@inproceedings{fastvlm2025,
  title     = {FastVLM: Efficient Vision Encoding for Vision Language Models},
  author    = {Vasu, Pavan Kumar Anasosalu and Faghri, Fartash and Li, Chun-Liang et al.},
  booktitle = {CVPR},
  year      = {2025}
}
```

If you find this wrapper useful, please consider citing the upstream work above.


## ⚖️ License

The `mci.py` code implementation is licensed according to Apple's [LICENSE](https://github.com/apple/ml-fastvlm/blob/main/LICENSE); it is a modified version of the original `mci.py` from the FastVLM repo. The underlying weights inherit the license provided by Apple in their [LICENSE_MODEL](https://github.com/apple/ml-fastvlm/blob/main/LICENSE_MODEL); review that file before use. All other code in this repo is licensed according to Apache 2.0.

## 🙏 Acknowledgements

- Original FastViT implementation and checkpoints by Apple ML Research – see
[https://github.com/apple/ml-fastvlm](https://github.com/apple/ml-fastvlm.).
- Wrapper inspired by the CLIP / SigLIP integrations in 🤗 `Transformers`.