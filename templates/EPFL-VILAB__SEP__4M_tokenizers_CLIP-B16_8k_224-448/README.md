---
license: other
license_name: sample-code-license
license_link: LICENSE
library_name: ml-4m
---

# 4M: Massively Multimodal Masked Modeling

*A framework for training any-to-any multimodal foundation models. <br>Scalable. Open-sourced. Across tens of modalities and tasks.*

[`Website`](https://4m.epfl.ch) | [`GitHub`](https://github.com/apple/ml-4m) | [`BibTeX`](#citation)  

Official implementation and pre-trained models for :

[**4M: Massively Multimodal Masked Modeling**](https://arxiv.org/abs/2312.06647), NeurIPS 2023 (Spotlight) <br>
*[David Mizrahi](https://dmizrahi.com/)\*, [Roman Bachmann](https://roman-bachmann.github.io/)\*, [Oğuzhan Fatih Kar](https://ofkar.github.io/), [Teresa Yeo](https://aserety.github.io/), [Mingfei Gao](https://fly6464.github.io/), [Afshin Dehghan](https://www.afshindehghan.com/), [Amir Zamir](https://vilab.epfl.ch/zamir/)*

[**4M-21: An Any-to-Any Vision Model for Tens of Tasks and Modalities**](https://arxiv.org/abs/2406.09406), arXiv 2024 <br>
*[Roman Bachmann](https://roman-bachmann.github.io/)\*, [Oğuzhan Fatih Kar](https://ofkar.github.io/)\*, [David Mizrahi](https://dmizrahi.com/)\*, [Ali Garjani](https://garjania.github.io/), [Mingfei Gao](https://fly6464.github.io/), [David Griffiths](https://www.dgriffiths.uk/), [Jiaming Hu](https://scholar.google.com/citations?user=vm3imKsAAAAJ&hl=en), [Afshin Dehghan](https://www.afshindehghan.com/), [Amir Zamir](https://vilab.epfl.ch/zamir/)*

4M is a framework for training "any-to-any" foundation models, using tokenization and masking to scale to many diverse modalities. 
Models trained using 4M can perform a wide range of vision tasks, transfer well to unseen tasks and modalities, and are flexible and steerable multimodal generative models. 
We are releasing code and models for "4M: Massively Multimodal Masked Modeling" (here denoted 4M-7), as well as "4M-21: An Any-to-Any Vision Model for Tens of Tasks and Modalities" (here denoted 4M-21).


## Installation
For install instructions, please see https://github.com/apple/ml-4m. 


## Usage

The CLIP-B/16 tokenizer can be loaded from Hugging Face Hub as follows:
```python
from fourm.vq.vqvae import VQVAE
tok_rgb = VQVAE.from_pretrained('EPFL-VILAB/4M_tokenizers_CLIP-B16_8k_224-448')
```

Please see https://github.com/apple/ml-4m/blob/main/README_TOKENIZATION.md for more detailed instructions and https://github.com/apple/ml-4m for other tokenizer and 4M model checkpoints.

## Citation

If you find this repository helpful, please consider citing our work:
```
@inproceedings{4m,
    title={{4M}: Massively Multimodal Masked Modeling},
    author={David Mizrahi and Roman Bachmann and O{\u{g}}uzhan Fatih Kar and Teresa Yeo and Mingfei Gao and Afshin Dehghan and Amir Zamir},
    booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
    year={2023},
}

@article{4m21,
    title={{4M-21}: An Any-to-Any Vision Model for Tens of Tasks and Modalities},
    author={Roman Bachmann and O{\u{g}}uzhan Fatih Kar and David Mizrahi and Ali Garjani and Mingfei Gao and David Griffiths and Jiaming Hu and Afshin Dehghan and Amir Zamir},
    journal={arXiv 2024},
    year={2024},
}
```

## License

The model weights in this repository are released under the Sample Code license as found in the [LICENSE](LICENSE) file.