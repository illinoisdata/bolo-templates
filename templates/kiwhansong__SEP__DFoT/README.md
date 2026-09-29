---
license: mit
pipeline_tag: image-to-video
---

<h1 align="center">Diffusion Forcing Transformer</h1>
<p align="center">
  <p align="center">
    <a href="https://kiwhan.dev/">Kiwhan Song*<sup>1</sup></a>
    ·
    <a href="https://boyuan.space/">Boyuan Chen*<sup>1</sup></a>
    ·
    <a href="https://msimchowitz.github.io/">Max Simchowitz<sup>2</sup></a>
    ·
    <a href="https://yilundu.github.io/">Yilun Du<sup>3</sup></a>
    ·
    <a href="https://groups.csail.mit.edu/locomotion/russt.html">Russ Tedrake<sup>1</sup></a>
    ·
    <a href="https://www.vincentsitzmann.com/">Vincent Sitzmann<sup>1</sup></a>
    <br/>
    *Equal contribution <sup>1</sup>MIT <sup>2</sup>CMU <sup>3</sup>Harvard
  </p>
  <h3 align="center"><a href="https://arxiv.org/abs/2502.06764">Paper</a> | <a href="https://boyuan.space/history-guidance">Website</a> | <a href="https://huggingface.co/spaces/kiwhansong/diffusion-forcing-transformer">HuggingFace Demo</a> | <a href="https://github.com/kwsong0113/diffusion-forcing-transformer">GitHub Code</a></h3>
</p>

This is the official model hub for the paper [**_History-guided Video Diffusion_**](https://arxiv.org/abs/2502.06764). We introduce the **Diffusion Forcing Tranformer (DFoT)**, a novel video diffusion model that designed to generate videos conditioned on an arbitrary number of context frames.  Additionally, we present **History Guidance (HG)**, a family of guidance methods uniquely enabled by DFoT. These methods significantly enhance video generation quality, temporal consistency, and motion dynamics, while also unlocking new capabilities such as compositional video generation and the stable rollout of extremely long videos.


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6613663bcfbba5e761a69531/OcsBrHWZXQidH7YxGCMtS.png)


## 🤗 Try generating videos with DFoT!

We provide an [_interactive_ demo](https://huggingface.co/spaces/kiwhansong/diffusion-forcing-transformer) on HuggingFace Spaces, where you can generate videos with DFoT and History Guidance. On the RealEstate10K dataset, you can generate:
- Any Number of Images → Short 2-second Video
- Single Image → Long 10-second Video
- Single Image → Endless Navigation Video (like the teaser above!)

Please check it out and have fun generating videos with DFoT!


## 🚀 Usage

All pretrained models can be automatically loaded from [our GitHub codebase](https://github.com/kwsong0113/diffusion-forcing-transformer). Please visit our repository for further instructions!



## 📌 Citation

If our work is useful for your research, please consider citing our paper:

```bibtex
@misc{song2025historyguidedvideodiffusion,
  title={History-Guided Video Diffusion}, 
  author={Kiwhan Song and Boyuan Chen and Max Simchowitz and Yilun Du and Russ Tedrake and Vincent Sitzmann},
  year={2025},
  eprint={2502.06764},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2502.06764}, 
}
```