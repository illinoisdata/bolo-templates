---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
pipeline_tag: image-text-to-text
tags:
- liquid
- lfm2
- lfm2-vl
- edge
new_version: LiquidAI/LFM2.5-VL-450M
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/chat?model=lfm2.5-vl-1.6b"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>
</center>

<br>

# LFM2‑VL-450M

LFM2‑VL is [Liquid AI](https://www.liquid.ai/)'s first series of multimodal models, designed to process text and images with variable resolutions. 
Built on the [LFM2](https://huggingface.co/collections/LiquidAI/lfm2-686d721927015b2ad73eaa38) backbone, it is optimized for low-latency and edge AI applications. 

We're releasing the weights of two post-trained checkpoints with [450M](https://huggingface.co/LiquidAI/LFM2-VL-450M) (for highly constrained devices) and [1.6B](https://huggingface.co/LiquidAI/LFM2-VL-1.6B) (more capable yet still lightweight) parameters.

* **2× faster inference speed** on GPUs compared to existing VLMs while maintaining competitive accuracy
* **Flexible architecture** with user-tunable speed-quality tradeoffs at inference time
* **Native resolution processing** up to 512×512 with intelligent patch-based handling for larger images, avoiding upscaling and distortion

Find more about our vision-language model in the [LFM2-VL post](https://www.liquid.ai/blog/lfm2-vl-efficient-vision-language-models) and its language backbone in the [LFM2 blog post](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models).

## 📄 Model details

Due to their small size, **we recommend fine-tuning LFM2-VL models on narrow use cases** to maximize performance. 
They were trained for instruction following and lightweight agentic flows. 
Not intended for safety‑critical decisions.

| Property | [**LFM2-VL-450M**](https://huggingface.co/LiquidAI/LFM2-VL-450M) | [**LFM2-VL-1.6B**](https://huggingface.co/LiquidAI/LFM2-VL-1.6B) |
|---|---:|---:|
| **Parameters (LM only)** | 350M | 1.2B |
| **Vision encoder** | SigLIP2 NaFlex base (86M) | SigLIP2 NaFlex shape‑optimized (400M) |
| **Backbone layers** | hybrid conv+attention | hybrid conv+attention |
| **Context (text)** | 32,768 tokens | 32,768 tokens |
| **Image tokens** | dynamic, user‑tunable | dynamic, user‑tunable |
| **Vocab size** | 65,536 | 65,536 |
| **Precision** | bfloat16 | bfloat16 |
| **License** | LFM Open License v1.0 | LFM Open License v1.0 |

**Supported languages:** English

**Generation parameters**: We recommend the following parameters:
- Text: `temperature=0.1`, `min_p=0.15`, `repetition_penalty=1.05`
- Vision: `min_image_tokens=64` `max_image_tokens=256`, `do_image_splitting=True`

**Chat template**: LFM2-VL uses a ChatML-like chat template as follows:  

```
<|startoftext|><|im_start|>system
You are a helpful multimodal assistant by Liquid AI.<|im_end|>
<|im_start|>user
<image>Describe this image.<|im_end|>
<|im_start|>assistant
This image shows a Caenorhabditis elegans (C. elegans) nematode.<|im_end|>
```

Images are referenced with a sentinel (`<image>`), which is automatically replaced with the image tokens by the processor.

You can apply it using the dedicated [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) function from Hugging Face transformers.

**Architecture**
- **Hybrid backbone**: Language model tower (LFM2-1.2B or LFM2-350M) paired with SigLIP2 NaFlex vision encoders (400M shape-optimized or 86M base variant)
- **Native resolution processing**: Handles images up to 512×512 pixels without upscaling and preserves non-standard aspect ratios without distortion
- **Tiling strategy**: Splits large images into non-overlapping 512×512 patches and includes thumbnail encoding for global context (in 1.6B model)
- **Efficient token mapping**: 2-layer MLP connector with pixel unshuffle reduces image tokens (e.g., 256×384 image → 96 tokens, 1000×3000 → 1,020 tokens)
- **Inference-time flexibility**: User-tunable maximum image tokens and patch count for speed/quality tradeoff without retraining

**Training approach**
- Builds on the LFM2 base model with joint mid-training that fuses vision and language capabilities using a gradually adjusted text-to-image ratio
- Applies joint SFT with emphasis on image understanding and vision tasks
- Leverages large-scale open-source datasets combined with in-house synthetic vision data, selected for balanced task coverage
- Follows a progressive training strategy: base model → joint mid-training → supervised fine-tuning

## 🏃 How to run LFM2-VL

You can run LFM2-VL with Hugging Face [`transformers`](https://github.com/huggingface/transformers) v4.57 or more recent as follows:

```bash
pip install -U transformers pillow
```

Here is an example of how to generate an answer with transformers in Python:

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
from transformers.image_utils import load_image

# Load model and processor
model_id = "LiquidAI/LFM2-VL-450M"
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    device_map="auto",
    dtype="bfloat16"
)
processor = AutoProcessor.from_pretrained(model_id)

# Load image and create conversation
url = "https://www.ilankelman.org/stopsigns/australia.jpg"
image = load_image(url)
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "What is in this image?"},
        ],
    },
]

# Generate Answer
inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
    tokenize=True,
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=64)
processor.batch_decode(outputs, skip_special_tokens=True)[0]

# This image depicts a vibrant street scene in what appears to be a Chinatown or similar cultural area. The focal point is a large red stop sign with white lettering, mounted on a pole.
```

You can directly run and test the model with this [Colab notebook](https://colab.research.google.com/drive/11EMJhcVB6OTEuv--OePyGK86k-38WU3q?usp=sharing).


## 🔧 How to fine-tune

We recommend fine-tuning LFM2-VL models on your use cases to maximize performance.

| Notebook  | Description                                                          | Link |
|-----------|----------------------------------------------------------------------|------|
| SFT (TRL) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using TRL. | <a href="https://colab.research.google.com/drive/1csXCLwJx7wI7aruudBp6ZIcnqfv8EMYN?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |


## 📈 Performance

| Model             | RealWorldQA | MM-IFEval | InfoVQA (Val) | OCRBench | BLINK | MMStar | MMMU (Val) | MathVista | SEEDBench_IMG | MMVet | MME      | MMLU  |
|-------------------|-------------|-----------|---------------|----------|-------|--------|------------|-----------|---------------|-------|----------|-------|
| InternVL3-2B      | 65.10       | 38.49     | 66.10         | 831      | 53.10 | 61.10  | 48.70      | 57.60     | 75.00         | 67.00 | 2186.40  | 64.80 |
| InternVL3-1B      | 57.00       | 31.14     | 54.94         | 798      | 43.00 | 52.30  | 43.20      | 46.90     | 71.20         | 58.70 | 1912.40  | 49.80 |
| SmolVLM2-2.2B     | 57.50       | 19.42     | 37.75         | 725      | 42.30 | 46.00  | 41.60      | 51.50     | 71.30         | 34.90 | 1792.50  | -     |
| LFM2-VL-1.6B      | 65.75       | 46.35     | 58.35         | 729      | 44.50 | 49.87  | 39.67      | 51.70     | 72.00         | 47.75 | 1756.72  | 50.99 |

| Model             | RealWorldQA | MM-IFEval | InfoVQA (Val) | OCRBench | BLINK | MMStar | MMMU (Val) | MathVista | SEEDBench_IMG | MMVet | MME      | MMLU  |
|-------------------|-------------|-----------|---------------|----------|-------|--------|------------|-----------|---------------|-------|----------|-------|
| SmolVLM2-500M     | 49.90       | 11.27     | 24.64         | 609      | 40.70 | 38.20  | 34.10      | 37.50     | 62.20         | 29.90 | 1448.30  | -     |
| LFM2-VL-450M      | 52.03       | 33.09     | 44.56         | 657      | 42.61 | 40.87  | 34.44      | 45.30     | 63.62         | 33.85 | 1229.91  | 40.16 |

We obtained MM-IFEval and InfoVQA (Val) scores for InternVL 3 and SmolVLM2 models using VLMEvalKit.

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).

## Citation

```
@article{liquidai2025lfm2,
 title={LFM2 Technical Report},
 author={Liquid AI},
 journal={arXiv preprint arXiv:2511.23404},
 year={2025}
}
```