---
license: apache-2.0
language:
- en
---
<div align="center">

# KobbleTinyV2-1.1B
</div>

This is the GGUF quantization of https://huggingface.co/concedo/KobbleTiny

You can use [KoboldCpp](https://github.com/LostRuins/koboldcpp/releases/latest) to run this model. With only 1B parameters, this model is ideal for running on mobile or low-end devices.

Update: KobbleTiny has been upgraded to V2! The old V1 GGUF is [still available at this link](https://huggingface.co/concedo/KobbleTiny-GGUF/tree/f6220c3be52ea68583de08d6d8e292d6ff5c8828).

<video width="320" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/63cd4b6d1c8a5d1d7d76a778/zjHfohCnEu2Y9CWSWgf0n.mp4"></video>

Try it live now: https://concedo-koboldcpp-kobbletiny.hf.space/

## Dataset and Objectives

The Kobble Dataset is a semi-private aggregated dataset made from multiple online sources and web scrapes. 
It contains content chosen and formatted specifically to work with KoboldAI software and Kobold Lite.

#### Dataset Categories:
- Instruct: Single turn instruct examples presented in the Alpaca format, with an emphasis on uncensored and unrestricted responses.
- Chat: Two participant roleplay conversation logs in a multi-turn raw chat format that KoboldAI uses.
- Story: Unstructured fiction excerpts, including literature containing various erotic and provocative content.

<!-- prompt-template start -->
## Prompt template: Alpaca

```
### Instruction:
{prompt}

### Response:
```

<!-- prompt-template end -->

**Note:** *No assurances will be provided about the **origins, safety, or copyright status** of this model, or of **any content** within the Kobble dataset.*  
*If you belong to a country or organization that has strict AI laws or restrictions against unlabelled or unrestricted content, you are advised not to use this model.*