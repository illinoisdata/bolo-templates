---
pipeline_tag: image-to-text
tags:
  - image-captioning
  - visual-question-answering
datasets:
  - sbu_captions
  - visual_genome
  - HuggingFaceM4/VQAv2
  - ChristophSchuhmann/MS_COCO_2017_URL_TEXT
language:
  - en
license: apache-2.0
base_model: unum-cloud/uform-vl-english
widget:
  - src: preview-interior.png
    output:
      text: "The living room is cozy, featuring a red leather chair and a white table. The chair is in the center, and the table is on the left side. A lamp on the left side illuminates the space. A large picture hangs on the wall, adding artistic flair. A vase on the table adds a decorative touch. The room is well-lit, creating a warm and inviting atmosphere."
  - src: preview-girl.png
    output:
      text: "A young girl stands in a grassy field, holding an umbrella to shield herself from the rain. She dons a yellow dress and seems to relish her time outdoors. The umbrella is open, offering protection from the rain. The field is bordered by trees, fostering a tranquil and natural ambiance"
---
<Gallery />

<h1 align="center">UForm</h1>
<h3 align="center">
Pocket-Sized Multimodal AI<br/>
For Content Understanding and Generation<br/>
</h3>

## Description 

UForm-Gen is a small generative vision-language model primarily designed for Image Captioning and Visual Question Answering. The model consists of two parts: 

1. [`uform-vl-english`](https://huggingface.co/unum-cloud/uform-vl-english) visual encoder,
2. [`Sheared-LLaMA-1.3B`](https://huggingface.co/princeton-nlp/Sheared-LLaMA-1.3B) language model tuned on instruction datasets.

The model was pre-trained on: MSCOCO, SBU Captions, Visual Genome, VQAv2, GQA and a few internal datasets.

### Usage

```bash
pip install uform
```

The generative model can be used to caption images, summarize their content, or answer questions about them.
The exact behavior is controlled by prompts.

```python
from uform.gen_model import VLMForCausalLM, VLMProcessor

model = VLMForCausalLM.from_pretrained("unum-cloud/uform-gen")
processor = VLMProcessor.from_pretrained("unum-cloud/uform-gen")

# [cap] Narrate the contents of the image with precision.
# [cap] Summarize the visual content of the image.
# [vqa] What is the main subject of the image?
prompt = "[cap] Summarize the visual content of the image."
image = Image.open("zebra.jpg")

inputs = processor(texts=[prompt], images=[image], return_tensors="pt")
with torch.inference_mode():
     output = model.generate(
        **inputs,
        do_sample=False,
        use_cache=True,
        max_new_tokens=128,
        eos_token_id=32001,
        pad_token_id=processor.tokenizer.pad_token_id
    )

prompt_len = inputs["input_ids"].shape[1]
decoded_text = processor.batch_decode(output[:, prompt_len:])[0]
```


## Evaluation

For captioning evaluation we measure CLIPScore and RefCLIPScore¹.

| Model                               | Size | Caption Length | CLIPScore | RefCLIPScore |
| :---------------------------------- | ---: | -------------: | --------: | -----------: |
| `llava-hf/llava-1.5-7b-hf`          |   7B |           Long |     0.878 |        0.529 |
| `llava-hf/llava-1.5-7b-hf`          |   7B |          Short |     0.886 |        0.531 |
|                                     |
| `Salesforce/instructblip-vicuna-7b` |   7B |           Long |     0.902 |        0.534 |
| `Salesforce/instructblip-vicuna-7b` |   7B |          Short |     0.848 |        0.523 |
|                                     |                                                  |
| `unum-cloud/uform-gen`              | 1.5B |           Long |     0.847 |        0.523 |
| `unum-cloud/uform-gen`              | 1.5B |          Short |     0.842 |        0.522 |

Results for VQAv2 evaluation.

| Model                      | Size | Accuracy |
| :------------------------- | ---: | -------: |
| `llava-hf/llava-1.5-7b-hf` |   7B |     78.5 |
| `unum-cloud/uform-gen`     | 1.5B |     66.5 |

¹ We used `apple/DFN5B-CLIP-ViT-H-14-378` CLIP model.


## Speed

On RTX 3090, the following performance is expected on text token generation using `float16`, equivalent PyTorch settings, and greedy decoding.

| Model                               | Size |               Speed |   Speedup |
| :---------------------------------- | ---: | ------------------: | --------: |
| `llava-hf/llava-1.5-7b-hf`          |   7B |  ~ 40 tokens/second |           |
| `Salesforce/instructblip-vicuna-7b` |   7B |  ~ 40 tokens/second |           |
| `unum-cloud/uform-gen`              | 1.5B | ~ 140 tokens/second | __x 3.5__ |