<div align="center"><img src="https://github.com/FasterDecoding/Medusa/blob/main/assets/logo.png?raw=true" alt="Medusa" width="100" align="center"></div>
<div align="center"><h1>&nbsp;Medusa: Simple Framework for Accelerating LLM Generation with Multiple Decoding Heads</h1></div>

<p align="center">
| <a href="https://sites.google.com/view/
medusa-llm"><b>Blog</b></a> | <a href="https://github.com/FasterDecoding/Medusa"><b>Codebase</b></a> |
</p>

---

## Installation
### Method 1: With pip
```bash
pip install medusa-llm
```
### Method 2: From source
```bash
git clone https://github.com/FasterDecoding/Medusa.git
cd Medusa
pip install -e .
```

### Model Weights
| Size | Chat Command                                  | Hugging Face Repo                                                     |
| ---- | --------------------------------------------- | --------------------------------------------------------------------- |
| 7B   | `python -m medusa.inference.cli --model FasterDecoding/medusa-vicuna-7b-v1.3` | [FasterDecoding/medusa-vicuna-33b-v1.3](https://huggingface.co/FasterDecoding/medusa-vicuna-7b-v1.3)   |
| 13B  | `python -m medusa.inference.cli --model FasterDecoding/medusa-vicuna-13b-v1.3` | [FasterDecoding/medusa-vicuna-13b-v1.3](https://huggingface.co/FasterDecoding/medusa-vicuna-13b-v1.3) |
| 33B  | `python -m medusa.inference.cli --model FasterDecoding/medusa-vicuna-33b-v1.3` | [FasterDecoding/medusa-vicuna-33b-v1.3](https://huggingface.co/FasterDecoding/medusa-vicuna-33b-v1.3) |

### Inference
We currently support inference in the single GPU and batch size 1 setting, which is the most common setup for local model hosting. We are actively working to extend Medusa's capabilities by integrating it into other inference frameworks, please don't hesitate to reach out if you are interested in contributing to this effort.

You can use the following command for lauching a CLI interface:
```bash
python -m medusa.inference.cli --model [path of medusa model]
```
You can also pass `--load-in-8bit` or `--load-in-4bit` to load the base model in quantized format.