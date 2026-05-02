---
library_name: transformers
pipeline_tag: robotics
---

# Nora-Long

<!-- Provide a quick summary of what the model is/does. -->

Nora-Long is an open vision-language-action model trained on robot manipulation episodes from the [Open X-Embodiment](https://robotics-transformer-x.github.io/) dataset. The model takes language instructions and camera images as input and generates robot actions. Nora-Lonf is trained directly from Qwen 2.5 VL-3B.
All Nora checkpoints, as well as our [training codebase](https://github.com/declare-lab/nora) are released under an MIT License.


**Unlike Nora, Nora-Long is pretrained with an action horizon of 5**. We observe worse performance on WidowX robot task with Nora-Long, but superior performance in libero simulation. Please feel free to finetune this model!

### Model Description

<!-- Provide a longer summary of what this model is. -->



- **Model type:**  Vision-language-action (language, image => robot actions)
- **Language(s) (NLP):** english
- **License:** MIT
- **Finetuned from model :** Qwen 2.5 VL-3B

### Model Sources 

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/declare-lab/nora
- **Paper :** https://www.arxiv.org/abs/2504.19854
- **Demo:** https://declare-lab.github.io/nora

## Usage

Nora take a language instruction and a camera image of a robot workspace as input, and predict (normalized) robot actions consisting of 7-DoF end-effector deltas of the form (x, y, z, roll, pitch, yaw, gripper). 
To execute on an actual robot platform, actions need to be un-normalized subject to statistics computed on a per-robot, per-dataset basis. 
Instructions on how to run Nora is available on https://github.com/declare-lab/nora.