---
library_name: metamotivo
license: cc-by-nc-4.0
tags:
- facebook
- meta
- pytorch
seed: 1
repo_url: https://github.com/facebookresearch/metamotivo
docs_url: https://metamotivo.metademolab.com/
---
# Meta Motivo S

Meta Motivo is a behavioral foundation model pre-trained with a novel unsupervised reinforcement learning algorithm to control the movements of a complex virtual humanoid agent. At test time, our model can be prompted to solve unseen tasks such as motion tracking, pose reaching, and reward optimization without any additional learning or fine-tuning.

This model is as described in ["Zero-shot Whole-Body Humanoid Control via Behavioral Foundation Models"](https://metamotivo.metademolab.com/) and corresponds to seed number 1 out of 5 evaluated in the paper.

**Model Developer:** Meta

# Model Details

Meta Motivo is composed by multiple networks
- forward net \\(F(s,a,z)\\)
- backward net \\(B(s)\\)
- actor net \\(\pi(s,z)\\)
- discriminator net \\(D(s,z)\\)
- critic net \\(Q(s,a,z)\\)

### Network architectures

**Forward, actor, and critic.** All these networks are MLPs with ReLU activations, except for the first hidden layer which uses a layernorm followed by tanh. The networks have two initial "embedding layers", one processing `(s,z)`, and the other processing `s` alone. The second embedding layer has half the hidden units of the first layer, and their outputs are concatenated and fed into the main MLP. We use 2 embedding layers and 2 hidden layers for the main MLP, each with 1024 hidden units. The actor network outputs the mean of a Gaussian distribution with fixed standard deviation, while the forward and critic networks output a d-dimensional vector and a scalar, respectively. The two latter networks use an ensemble of two networks.

**Backward.** The backward map is a simple MLP composed of a layernorm operation, a linear layer with 256 hidden units, a tanh activation function, and another linear layer which outputs a d-dimensional vector that is then normalized in l2-norm.

**Discriminator.** The discriminator is an MLP with 3 hidden layers of 1024 units and ReLU activations, except for the first hidden layer which uses a layernorm followed by tanh. It takes as input a state observation `s` and a latent variable `z`, and has a sigmoidal unit at the output. 


See the `config.json` file for more details.

## How to use

```bash
> pip install "metamotivo[all] @ git+https://github.com/facebookresearch/metamotivo.git"
```
and then
```python
from metamotivo.fb_cpr.huggingface import FBcprModel

model = FBcprModel.from_pretrained("facebook/metamotivo-S-1")
```

# Citation

If you find our code useful for your research, please consider citing:

    @article{tirinzoni2024metamotivo,
        title={Zero-shot Whole-Body Humanoid Control via Behavioral Foundation Models},
        author={Tirinzoni, Andrea and Touati, Ahmed and Farebrother, Jesse and Guzek, Mateusz and Kanervisto, Anssi and Xu, Yingchen and Lazaric, Alessandro and Pirotta, Matteo},
    }

# License

Meta Motivo is CC-BY-NC 4.0 licensed as of now.