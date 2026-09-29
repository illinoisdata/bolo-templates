---
license: lgpl-3.0
tags:
- onnx
- text-recognition
- textline_recognition
- computer-vision
- japanese
- ocr
- OCR
library_name: tensorrt
language:
- en
- ja
pipeline_tag: image-to-text
---

---
**Official GitHub Repository:** [meikiocr](https://github.com/rtr46/meikiocr)

This model is a core component of the `meikiocr` pipeline. For the full implementation, command-line script, and documentation, please see the official GitHub repository.

---

# meiki.text.recognition.v0

pareto-optimal text recognition model. trained on japanese video games.

meiki.text.recognition achieves state-of-the-art text recognition accuracy as well as latency by redefining "text recognition" as "character detection". the model is a fine-tune of https://github.com/Peterande/D-FINE object detecor combined with a mobilenetv4 CNN backbone. to my knowledge there is no existing, open weight text recognition model with a better accuracy/latency tradeoff for japanese text recognition.

## intended use and constraints
- it is specifically trained on japanese video games, therefore performance may vary outside of this use case
- input needs to be resized and padded to be 960x32px
- outputs detection results as characters + bbox + confidence. check the inference.py script for a suggested post processing algorithms
- can detect up to 48 characters
- only works on horizontal text

## benchmarks

| cpu | gpu |
|:---:|:---:|
| ![accuracy_vs_cpu_latency](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/NoTZVOLPhHMFW-O3fmgif.png) | ![accuracy_vs_gpu_latency](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/UQdnt0dN4qSpvBKLrkRZE.png) |

## how to use

please refer to this demo inference script: https://huggingface.co/rtr46/meiki.txt.recognition.v0/blob/main/inference.py

## examples

![input](https://cdn-uploads.huggingface.co/production/uploads/68f7a26cfcf6939fd30fb19f/TZeaJio7k9gZYnqXF4G0w.jpeg)

```
その一つの実情が、第一層の一画、空気には黴臭さと変に饐えた甘
```

```json
{
	"text":"その一つの実情が、第一層の一画、空気には黴臭さと変に饐えた甘",
	"chars":[
		{"char":"そ","bbox":[2,0,33,32]},
		{"char":"の","bbox":[33,0,65,32]},
		{"char":"一","bbox":[65,0,96,32]},
		{"char":"つ","bbox":[97,0,128,32]},
		{"char":"の","bbox":[129,0,160,32]},
		{"char":"実","bbox":[161,0,193,32]},
		{"char":"情","bbox":[192,0,224,32]},
		{"char":"が","bbox":[225,0,256,32]},
		{"char":"、","bbox":[258,0,288,32]},
		{"char":"第","bbox":[288,0,319,32]},
		{"char":"一","bbox":[321,0,352,32]},
		{"char":"層","bbox":[352,0,384,32]},
		{"char":"の","bbox":[384,0,415,32]},
		{"char":"一","bbox":[416,0,448,32]},
		{"char":"画","bbox":[448,0,479,32]},
		{"char":"、","bbox":[481,0,512,32]},
		{"char":"空","bbox":[513,0,544,32]},
		{"char":"気","bbox":[544,0,575,32]},
		{"char":"に","bbox":[576,0,608,32]},
		{"char":"は","bbox":[609,0,640,32]},
		{"char":"黴","bbox":[640,0,672,32]},
		{"char":"臭","bbox":[672,0,704,32]},
		{"char":"さ","bbox":[705,0,737,32]},
		{"char":"と","bbox":[738,0,767,32]},
		{"char":"変","bbox":[769,0,800,32]},
		{"char":"に","bbox":[800,0,832,32]},
		{"char":"饐","bbox":[833,0,864,32]},
		{"char":"え","bbox":[864,0,895,32]},
		{"char":"た","bbox":[897,0,928,32]},
		{"char":"甘","bbox":[929,0,960,32]}
	]
}
```