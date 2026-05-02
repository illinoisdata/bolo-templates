---
license: apache-2.0
---

Fine-tuned T5 base model for use as a frame semantic parser in the [Frame Semantic Transformer](https://github.com/chanind/frame-semantic-transformer) project. This model is trained on data from [FrameNet 1.7](https://framenet2.icsi.berkeley.edu/).

### Usage
This is meant to be used a part of [Frame Semantic Transformer](https://github.com/chanind/frame-semantic-transformer). See that project for usage instructions.

### Tasks

This model is trained to perform 3 tasks related to semantic frame parsing:
1. Identify frame trigger locations in the text
2. Classify the frame given a trigger location
3. Extract frame elements in the sentence

### Performance

This model is trained and evaluated using the same train/dev/test splits from FrameNet 1.7 annotated corpora as used by [Open Sesame](https://github.com/swabhs/open-sesame). 

| Task                   | F1 Score (Dev) | F1 Score (Test) |
| ---------------------- | -------------- | --------------- |
| Trigger identification | 0.78           | 0.74            |
| Frame Classification   | 0.91           | 0.89            |
| Argument Extraction    | 0.78           | 0.75            |