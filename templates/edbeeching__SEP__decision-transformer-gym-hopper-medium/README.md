---
tags:
- deep-reinforcement-learning
- reinforcement-learning
- decision-transformer
- gym-continous-control

pipeline_tag: reinforcement-learning

---
# Decision Transformer model trained on medium trajectories sampled from the Gym Hopper environment
This is a trained [Decision Transformer](https://arxiv.org/abs/2106.01345) model trained on medium trajectories sampled from the Gym Hopper environment.

The following normlization coefficients are required to use this model:

mean = [ 1.311279, -0.08469521, -0.5382719,  -0.07201576,  0.04932366,  2.1066856, -0.15017354,  0.00878345, -0.2848186,  -0.18540096, -0.28461286] 

std = [0.17790751, 0.05444621, 0.21297139, 0.14530419, 0.6124444, 0.85174465, 1.4515252,  0.6751696,  1.536239,   1.6160746,  5.6072536 ]


See our [Blog Post](https://colab.research.google.com/drive/1K3UuajwoPY1MzRKNkONNRS3gS5DxZ-qF?usp=sharing),  [Colab notebook](https://colab.research.google.com/drive/1K3UuajwoPY1MzRKNkONNRS3gS5DxZ-qF?usp=sharing) or [Example Script](https://github.com/huggingface/transformers/tree/main/examples/research_projects/decision_transformer) for usage.