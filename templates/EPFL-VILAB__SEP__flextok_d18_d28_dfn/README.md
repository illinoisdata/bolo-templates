---
license: apple-amlr
---

# FlexTok: Resampling Images into 1D Token Sequences of Flexible Length

[`Website`](https://flextok.epfl.ch) | [`arXiv`](https://arxiv.org/abs/2502.13967) | [`GitHub`](https://github.com/apple/ml-flextok) | [`🤗 Demo`](https://huggingface.co/spaces/EPFL-VILAB/FlexTok) | [`BibTeX`](#citation)

Official implementation and pre-trained models for: <br>
[**FlexTok: Resampling Images into 1D Token Sequences of Flexible Length**](https://arxiv.org/abs/2502.13967), arXiv 2025 <br>
*[Roman Bachmann](https://roman-bachmann.github.io/)\*, [Jesse Allardice](https://github.com/JesseAllardice)\*, [David Mizrahi](https://dmizrahi.com/)\*, [Enrico Fini](https://scholar.google.com/citations?user=OQMtSKIAAAAJ), [Oğuzhan Fatih Kar](https://ofkar.github.io/), [Elmira Amirloo](https://elamirloo.github.io/), [Alaaeldin El-Nouby](https://aelnouby.github.io/), [Amir Zamir](https://vilab.epfl.ch/zamir/), [Afshin Dehghan](https://scholar.google.com/citations?user=wcX-UW4AAAAJ)*


## Installation
For install instructions, please see https://github.com/apple/ml-flextok. 


## Usage

To load the `FlexTok d18-d28 DFN` model directly from HuggingFace Hub, call:
```python
from flextok.flextok_wrapper import FlexTokFromHub
model = FlexTokFromHub.from_pretrained('EPFL-VILAB/flextok_d18_d28_dfn').eval()
```

The model can also be loaded by downloading the `model.safetensors` checkpoint in this repository manually and loading it using our helper functions:
```python
from hydra.utils import instantiate
from flextok.utils.checkpoint import load_safetensors

ckpt, config = load_safetensors('/path/to/model.safetensors')
model = instantiate(config).eval()
model.load_state_dict(ckpt)
```

After loading a FlexTok model, image batches can be encoded using:
```python
from flextok.utils.demo import imgs_from_urls
# Load example images of shape (B, 3, 256, 256), normalized to [-1,1]
imgs = imgs_from_urls(urls=['https://storage.googleapis.com/flextok_site/nb_demo_images/0.png'])

# tokens_list is a list of [1, 256] discrete token sequences
tokens_list = model.tokenize(imgs)
```

The list of token sequences can be truncated in a nested fashion:
```python
k_keep = 64 # For example, only keep the first 64 out of 256 tokens
tokens_list = [t[:,:k_keep] for t in tokens_list]
```

To decode the tokens with FlexTok's rectified flow decoder, call:
```python
# tokens_list is a list of [1, l] discrete token sequences, with l <= 256
# reconst is a [B, 3, 256, 256] tensor, normalized to [-1,1]
reconst = model.detokenize(
    tokens_list,
    timesteps=20, # Number of denoising steps
    guidance_scale=7.5, # Classifier-free guidance scale
    perform_norm_guidance=True, # See https://arxiv.org/abs/2410.02416
)
```


## Citation

If you find this repository helpful, please consider citing our work:
```
@article{flextok,
    title={{FlexTok}: Resampling Images into 1D Token Sequences of Flexible Length},
    author={Roman Bachmann and Jesse Allardice and David Mizrahi and Enrico Fini and O{\u{g}}uzhan Fatih Kar and Elmira Amirloo and Alaaeldin El-Nouby and Amir Zamir and Afshin Dehghan},
    journal={arXiv 2025},
    year={2025},
}
```

## License

The model weights in this repository are released under the Apple Model License for Research.