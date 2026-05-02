---
license: apache-2.0
datasets:
- autoflow
---

# Perceiver IO for optical flow

Perceiver IO model trained on [AutoFlow](https://autoflow-google.github.io/). It was introduced in the paper [Perceiver IO: A General Architecture for Structured Inputs & Outputs](https://arxiv.org/abs/2107.14795) by Jaegle et al. and first released in [this repository](https://github.com/deepmind/deepmind-research/tree/master/perceiver). 

Optical flow is a decades-old open problem in computer vision. Given two images of the same scene (e.g. two consecutive frames of a video), the task is to estimate the 2D displacement for each pixel in the first image. This has many broader applications, such as navigation and visual odometry in robots, estimation of 3D geometry, and even to aid transfer of more complex, learned inference such as 3D human pose estimation from synthetic to real images.

Disclaimer: The team releasing Perceiver IO did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

Perceiver IO is a transformer encoder model that can be applied on any modality (text, images, audio, video, ...). The core idea is to employ the self-attention mechanism on a not-too-large set of latent vectors (e.g. 256 or 512), and only use the inputs to perform cross-attention with the latents. This allows for the time and memory requirements of the self-attention mechanism to not depend on the size of the inputs. 

To decode, the authors employ so-called decoder queries, which allow to flexibly decode the final hidden states of the latents to produce outputs of arbitrary size and semantics. For optical flow, the output is a tensor containing the predicted flow of shape (batch_size, height, width, 2).

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/perceiver_architecture.jpg" alt="drawing" width="600"/>

<small> Perceiver IO architecture.</small>

As the time and memory requirements of the self-attention mechanism don't depend on the size of the inputs, the Perceiver IO authors can train the model on raw pixel values, by concatenating a pair of images and extracting a 3x3 patch around each pixel. 

The model obtains state-of-the-art results on important optical flow benchmarks, including [Sintel](http://sintel.is.tue.mpg.de/) and [KITTI](http://www.cvlibs.net/datasets/kitti/eval_scene_flow.php?benchmark=flow).

## Intended uses & limitations

You can use the raw model for predicting optical flow between a pair of images. See the [model hub](https://huggingface.co/models?search=deepmind/perceiver) to look for other versions on a task that may interest you.

### How to use

We refer to the [tutorial notebook](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/Perceiver/Perceiver_for_Optical_Flow.ipynb) regarding using the Perceiver for optical flow.

## Training data

This model was trained on [AutoFlow](https://autoflow-google.github.io/), a synthetic dataset consisting of 400,000 annotated image pairs. 

## Training procedure

### Preprocessing

Frames are resized to a resolution of 368x496. The authors concatenate the frames along the channel dimension and extract a 3x3 patch around each pixel (leading to 3x3x3x2 = 54 values for each pixel).

### Pretraining

Hyperparameter details can be found in Appendix E of the [paper](https://arxiv.org/abs/2107.14795).

## Evaluation results

The model achieves a average end-point error (EPE) of 1.81 on Sintel.clean,  2.42 on Sintel.final and 4.98 on KITTI. For evaluation results, we refer to table 4 of the [paper](https://arxiv.org/abs/2107.14795).

### BibTeX entry and citation info

```bibtex
@article{DBLP:journals/corr/abs-2107-14795,
  author    = {Andrew Jaegle and
               Sebastian Borgeaud and
               Jean{-}Baptiste Alayrac and
               Carl Doersch and
               Catalin Ionescu and
               David Ding and
               Skanda Koppula and
               Daniel Zoran and
               Andrew Brock and
               Evan Shelhamer and
               Olivier J. H{\'{e}}naff and
               Matthew M. Botvinick and
               Andrew Zisserman and
               Oriol Vinyals and
               Jo{\~{a}}o Carreira},
  title     = {Perceiver {IO:} {A} General Architecture for Structured Inputs {\&}
               Outputs},
  journal   = {CoRR},
  volume    = {abs/2107.14795},
  year      = {2021},
  url       = {https://arxiv.org/abs/2107.14795},
  eprinttype = {arXiv},
  eprint    = {2107.14795},
  timestamp = {Tue, 03 Aug 2021 14:53:34 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2107-14795.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```