---
license: cc-by-nc-4.0
tags:
- CoTracker
- vision
- cotracker
---
# Point tracking with CoTracker3



**CoTracker3** is a fast transformer-based model that was introduced in [CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos](https://arxiv.org/abs/2410.11831).
It can track any point in a video and brings to tracking some of the benefits of Optical Flow. 
You could read more about the paper on our [webpage](https://cotracker3.github.io/). Code is available [here](https://github.com/facebookresearch/co-tracker).

CoTracker can track:

- **Any pixel** in a video
- A **quasi-dense** set of pixels together
- Points can be manually selected or sampled on a grid in any video frame



## How to use
Here is how to use this model in the **offline mode**:

```pip install imageio[ffmpeg]```, then:
```python
import torch
# Download the video
url = 'https://github.com/facebookresearch/co-tracker/raw/refs/heads/main/assets/apple.mp4'

import imageio.v3 as iio
frames = iio.imread(url, plugin="FFMPEG")  # plugin="pyav"

device = 'cuda'
grid_size = 10
video = torch.tensor(frames).permute(0, 3, 1, 2)[None].float().to(device)  # B T C H W

# Run Offline CoTracker:
cotracker = torch.hub.load("facebookresearch/co-tracker", "cotracker3_offline").to(device)
pred_tracks, pred_visibility = cotracker(video, grid_size=grid_size) # B T N 2,  B T N 1
```
and in the **online mode**:
```python
cotracker = torch.hub.load("facebookresearch/co-tracker", "cotracker3_online").to(device)

# Run Online CoTracker, the same model with a different API:
# Initialize online processing
cotracker(video_chunk=video, is_first_step=True, grid_size=grid_size)  

# Process the video
for ind in range(0, video.shape[1] - cotracker.step, cotracker.step):
    pred_tracks, pred_visibility = cotracker(
        video_chunk=video[:, ind : ind + cotracker.step * 2]
    )  # B T N 2,  B T N 1
```
Online processing is more memory-efficient and allows for the processing of longer videos or videos in real-time.

## BibTeX entry and citation info

```bibtex
@inproceedings{karaev24cotracker3,
  title     = {CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos},
  author    = {Nikita Karaev and Iurii Makarov and Jianyuan Wang and Natalia Neverova and Andrea Vedaldi and Christian Rupprecht},
  booktitle = {Proc. {arXiv:2410.11831}},
  year      = {2024}
}
```