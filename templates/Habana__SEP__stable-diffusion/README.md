---
license: apache-2.0
---

[Optimum Habana](https://github.com/huggingface/optimum-habana) is the interface between the Hugging Face Transformers and Diffusers libraries and Habana's Gaudi processor (HPU).
It provides a set of tools enabling easy and fast model loading, training and inference on single- and multi-HPU settings for different downstream tasks.
Learn more about how to take advantage of the power of Habana HPUs to train and deploy Transformers and Diffusers models at [hf.co/hardware/habana](https://huggingface.co/hardware/habana).

## Stable Diffusion HPU configuration

This model only contains the `GaudiConfig` file for running **Stable Diffusion v1** (e.g. [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)) on Habana's Gaudi processors (HPU).

**This model contains no model weights, only a GaudiConfig.**

This enables to specify:
- `use_torch_autocast`: whether to use Torch Autocast for managing mixed precision

## Usage

The `GaudiStableDiffusionPipeline` (`GaudiDDIMScheduler`) is instantiated the same way as the `StableDiffusionPipeline` (`DDIMScheduler`) in the 🤗 Diffusers library.
The only difference is that there are a few new training arguments specific to HPUs.\
It is strongly recommended to train this model doing bf16 mixed-precision training for optimal performance and accuracy.

Here is an example with one prompt:
```python
from optimum.habana import GaudiConfig
from optimum.habana.diffusers import GaudiDDIMScheduler, GaudiStableDiffusionPipeline


model_name = "runwayml/stable-diffusion-v1-5"

scheduler = GaudiDDIMScheduler.from_pretrained(model_name, subfolder="scheduler")

pipeline = GaudiStableDiffusionPipeline.from_pretrained(
    model_name,
    scheduler=scheduler,
    use_habana=True,
    use_hpu_graphs=True,
    gaudi_config="Habana/stable-diffusion",
)

outputs = pipeline(
    ["An image of a squirrel in Picasso style"],
    num_images_per_prompt=16,
    batch_size=4,
)
```

Check out the [documentation](https://huggingface.co/docs/optimum/habana/usage_guides/stable_diffusion) and [this example](https://github.com/huggingface/optimum-habana/tree/main/examples/stable-diffusion) for more advanced usage.