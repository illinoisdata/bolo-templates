---
license: mit
base_model: pyannote/segmentation-3.0
tags:
- speaker-diarization
- speaker-segmentation
- generated_from_trainer
datasets:
- diarizers-community/callhome
model-index:
- name: speaker-segmentation-fine-tuned-callhome-jpn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# speaker-segmentation-fine-tuned-callhome-jpn

This model is a fine-tuned version of [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0) on the diarizers-community/callhome jpn dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7653
- Der: 0.2311
- False Alarm: 0.0477
- Missed Detection: 0.1352
- Confusion: 0.0482

## Model description


This segmentation model has been trained on Japanese data (Callhome) using [diarizers](https://github.com/huggingface/diarizers/tree/main). 
It can be loaded with two lines of code:  

```python
from diarizers import SegmentationModel

segmentation_model = SegmentationModel().from_pretrained('diarizers-community/speaker-segmentation-fine-tuned-callhome-jpn')
```

To use it within a pyannote speaker diarization pipeline, load the [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1) pipeline, and convert the model to a pyannote compatible format: 

```python

from pyannote.audio import Pipeline
import torch

device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")

# load the pre-trained pyannote pipeline
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1")
pipeline.to(device)

# replace the segmentation model with your fine-tuned one
segmentation_model = segmentation_model.to_pyannote_model()
pipeline._segmentation.model = segmentation_model.to(device)
```

You can now use the pipeline on audio examples: 

```python
from datasets import load_dataset
# load dataset example
dataset = load_dataset("diarizers-community/callhome", "jpn", split="data")
sample = dataset[0]["audio"]

# pre-process inputs
sample["waveform"] = torch.from_numpy(sample.pop("array")[None, :]).to(device, dtype=model.dtype)
sample["sample_rate"] = sample.pop("sampling_rate")

# perform inference
diarization = pipeline(sample)

# dump the diarization output to disk using RTTM format
with open("audio.rttm", "w") as rttm:
    diarization.write_rttm(rttm)
```

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Der    | False Alarm | Missed Detection | Confusion |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-----------:|:----------------:|:---------:|
| 0.5917        | 1.0   | 328  | 0.7859          | 0.2409 | 0.0507      | 0.1369           | 0.0533    |
| 0.5616        | 2.0   | 656  | 0.7738          | 0.2350 | 0.0530      | 0.1350           | 0.0471    |
| 0.5364        | 3.0   | 984  | 0.7737          | 0.2358 | 0.0484      | 0.1368           | 0.0506    |
| 0.5121        | 4.0   | 1312 | 0.7626          | 0.2317 | 0.0483      | 0.1358           | 0.0475    |
| 0.5166        | 5.0   | 1640 | 0.7653          | 0.2311 | 0.0477      | 0.1352           | 0.0482    |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.2+cu121
- Datasets 2.18.0
- Tokenizers 0.19.1