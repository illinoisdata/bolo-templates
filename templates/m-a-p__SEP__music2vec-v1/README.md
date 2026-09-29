---
license: cc-by-nc-4.0
inference: false
tags:
- music
---
# Introduction to our series work

The development log of our Music Audio Pre-training (m-a-p) model family:
- 17/03/2023: we release two advanced music understanding models, [MERT-v1-95M](https://huggingface.co/m-a-p/MERT-v1-95M) and [MERT-v1-330M](https://huggingface.co/m-a-p/MERT-v1-330M) , trained with new paradigm and dataset. They outperform the previous models and can better generalize to more tasks.
- 14/03/2023: we retrained the MERT-v0 model with open-source-only music dataset [MERT-v0-public](https://huggingface.co/m-a-p/MERT-v0-public)
- 29/12/2022: a music understanding model [MERT-v0](https://huggingface.co/m-a-p/MERT-v0) trained with **MLM** paradigm, which performs better at downstream tasks.
- 29/10/2022: a pre-trained MIR model [music2vec](https://huggingface.co/m-a-p/music2vec-v1) trained with **BYOL** paradigm.



Here is a table for quick model pick-up:

| Name                                                         | Pre-train Paradigm | Training Data (hour) | Pre-train Context   (second) | Model Size | Transformer Layer-Dimension | Feature Rate | Sample Rate | Release Date |
| ------------------------------------------------------------ | ------------------ | -------------------- | ---------------------------- | ---------- | --------------------------- | ------------ | ----------- | ------------ |
| [MERT-v1-330M](https://huggingface.co/m-a-p/MERT-v1-330M)    | MLM                | 160K                 | 5                            | 330M       | 24-1024                     | 75 Hz        | 24K Hz      | 17/03/2023   |
| [MERT-v1-95M](https://huggingface.co/m-a-p/MERT-v1-95M)      | MLM                | 20K                  | 5                            | 95M        | 12-768                      | 75 Hz        | 24K Hz      | 17/03/2023   |
| [MERT-v0-public](https://huggingface.co/m-a-p/MERT-v0-public) | MLM                | 900                  | 5                            | 95M        | 12-768                      | 50 Hz        | 16K Hz      | 14/03/2023   |
| [MERT-v0](https://huggingface.co/m-a-p/MERT-v0)              | MLM                | 1000                 | 5                            | 95 M       | 12-768                      | 50 Hz        | 16K Hz      | 29/12/2022   |
| [music2vec-v1](https://huggingface.co/m-a-p/music2vec-v1)    | BYOL               | 1000                 | 30                           | 95 M       | 12-768                      | 50 Hz        | 16K Hz      | 30/10/2022   |

## Explanation

The m-a-p models share the similar model architecture and the most distinguished difference is the paradigm in used pre-training. Other than that, there are several nuance technical configuration needs to know before using:

- **Model Size**: the number of parameters that would be loaded to memory. Please select the appropriate size fitting your hardware.
- **Transformer Layer-Dimension**: The number of transformer layers and the corresponding feature dimensions can be outputted from our model. This is marked out because features extracted by **different layers could have various performance depending on tasks**.
- **Feature Rate**: Given a 1-second audio input, the number of features output by the model.
- **Sample Rate**: The frequency of audio that the model is trained with.


# Introduction to Music2Vec

**Music2Vec** is accepted as 2-page abstract in Late Breaking Demos (LBD) at the ISMIR 2022.
It is a completely unsupervised model trained on 1000 hour music audios. 
We release the **crop5s** version base model as music2vec-v1. 
Our base model is SOTA-comparable on multiple MIR tasks even under probing settings, while keeping fine-tunable on a single 2080Ti. 
Larger models trained with more data are on the way~

For a more recent pretrained model with better performance, please refer to [m-a-p/MERT-v0](https://huggingface.co/m-a-p/MERT-v0).

# Model Architecture

Music2Vec Framework. During pre-training, the student model aims to
reconstruct the masked music audio by taking the contextualized representations provided by the teacher model as prediction targets.
![Model Architecture](music2vec.png)

# Performance Comparison

With 95M parameters and relatively small training data (1k hr), our base Music2Vec representation achieves comparable performance to the SOTA Jukebox-5B representation. 
Note that our base model size is **<2%** of Jukebox-5B.
![Performance Comparison](music2vec_performance.png)

# Model Usage

```python
from transformers import Wav2Vec2Processor, Data2VecAudioModel
import torch
from torch import nn
from datasets import load_dataset

# load demo audio and set processor
dataset = load_dataset("hf-internal-testing/librispeech_asr_demo", "clean", split="validation")
dataset = dataset.sort("id")
sampling_rate = dataset.features["audio"].sampling_rate
processor = Wav2Vec2Processor.from_pretrained("facebook/data2vec-audio-base-960h")

# loading our model weights
model = Data2VecAudioModel.from_pretrained("m-a-p/music2vec-v1")


# audio file is decoded on the fly
inputs = processor(dataset[0]["audio"]["array"], sampling_rate=sampling_rate, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs, output_hidden_states=True)

# take a look at the output shape, there are 13 layers of representation
# each layer performs differently in different downstream tasks, you should choose empirically
all_layer_hidden_states = torch.stack(outputs.hidden_states).squeeze()
print(all_layer_hidden_states.shape) # [13 layer, 292 timestep, 768 feature_dim]

# for utterance level classification tasks, you can simply reduce the representation in time
time_reduced_hidden_states = all_layer_hidden_states.mean(-2)
print(time_reduced_hidden_states.shape) # [13, 768]

# you can even use a learnable weighted average representation
aggregator = nn.Conv1d(in_channels=13, out_channels=1, kernel_size=1)
weighted_avg_hidden_states = aggregator(time_reduced_hidden_states).squeeze()
print(weighted_avg_hidden_states.shape) # [768]
```

Our model is based on the [data2vec audio model](https://huggingface.co/docs/transformers/model_doc/data2vec#transformers.Data2VecAudioModel).

# Citation

The paper can be found at [ISMIR](https://ismir2022program.ismir.net/lbd_410.html).

```shell
@article{li2022map,
  title={MAP-Music2Vec: A Simple and Effective Baseline for Self-Supervised Music Audio Representation Learning},
  author={Li, Yizhi and Yuan, Ruibin and Zhang, Ge and Ma, Yinghao and Lin, Chenghua and Chen, Xingran and Ragni, Anton and Yin, Hanzhi and Hu, Zhijie and He, Haoyu and others},
  journal={arXiv preprint arXiv:2212.02508},
  year={2022}
}

```