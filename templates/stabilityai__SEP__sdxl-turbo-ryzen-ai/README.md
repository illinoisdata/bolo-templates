---
base_model:
- stabilityai/sdxl-turbo
pipeline_tag: text-to-image
license: other
license_name: stabilityai-ai-community
license_link: LICENSE.md
language:
- en
tags:
- text-to-image
- AMD
- sdxl
- sdxl-turbo
---


## **SDXL Turbo AMD RyzenAI**

This repository hosts the AMD [Ryzen™ AI](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html) optimized version of SDXL-Turbo created in collaboration with [AMD](https://huggingface.co/amd). This ONNX-ported model is the world’s first Block FP16 model with the UNET and VAE decoder completely in Block FP16. Built for the AMD XDNA™ 2 based NPU, this model combines the accuracy of FP16 with the performance of INT8. 

### **Usage**

This model can be demoed using the Amuse AI application: [Amuse](https://www.amuse-ai.com/)

Amuse settings: Open in "EZ Mode", Toggle: Balanced Mode, AMD XDNA™ 2 Stable Diffusion Offload: checked. 

Please note: This model is released under the [Stability Community License](https://stability.ai/community-license-agreement). Visit [Stability AI](https://stability.ai/license) to learn or [contact us](https://stability.ai/enterprise) for commercial licensing details.

### **Model Description**

Refer to the [SDXL-Turbo Model card](https://huggingface.co/stabilityai/sdxl-turbo#model-details) for more details.

### **License**

* Community License: Free for research, non-commercial, and commercial use for organizations or individuals with less than $1M in total annual revenue. More details can be found in the [Community License Agreement](https://stability.ai/community-license-agreement). Read more at [https://stability.ai/license](https://stability.ai/license).  
* For individuals and organizations with annual revenue above $1M: please [contact us](https://stability.ai/enterprise) to get an Enterprise License.

### **Model Sources**

For research purposes, we recommend our generative-models Github repository ([https://github.com/Stability-AI/generative-models](https://github.com/Stability-AI/generative-models)), which implements the most popular diffusion frameworks (both training and inference).

Repository: [https://github.com/Stability-AI/generative-models](https://github.com/Stability-AI/generative-models)

SDXL Turbo Paper: [https://stability.ai/research/adversarial-diffusion-distillation](https://stability.ai/research/adversarial-diffusion-distillation)

## **File Structure**

## **Uses**

### **Intended Uses**

Intended uses include the following:

* Generation of artworks and use in design and other artistic processes.  
* Applications in educational or creative tools.  
* Research on generative models, including understanding the limitations of generative models.

All uses of the model must be in accordance with our [Acceptable Use Policy](https://stability.ai/use-policy).

### **Out-of-Scope Uses**

The model was not trained to be factual or true representations of people or events. As such, using the model to generate such content is out-of-scope of the abilities of this model.

## **Safety**

As part of our safety-by-design and responsible AI deployment approach, we take deliberate measures to ensure Integrity starts at the early stages of development. We implement safety measures throughout the development of our models. We have implemented safety mitigations that are intended to reduce the risk of certain harms, however we recommend that developers conduct their own testing and apply additional mitigations based on their specific use cases.  
For more about our approach to Safety, please visit our [Safety page](https://stability.ai/safety).

### **Integrity Evaluation**

Our integrity evaluation methods include structured evaluations and red-teaming testing for certain harms. Testing was conducted primarily in English and may not cover all possible harms.

### **Risks identified and mitigations:**

* Harmful content: We have used filtered data sets when training our models and implemented safeguards that attempt to strike the right balance between usefulness and preventing harm. However, this does not guarantee that all possible harmful content has been removed. TAll developers and deployers should exercise caution and implement content safety guardrails based on their specific product policies and application use cases.  
* Misuse: Technical limitations and developer and end-user education can help mitigate against malicious applications of models. All users are required to adhere to our [Acceptable Use Policy](https://stability.ai/use-policy), including when applying fine-tuning and prompt engineering mechanisms. Please reference the Stability AI Acceptable Use Policy for information on violative uses of our products.  
* Privacy violations: Developers and deployers are encouraged to adhere to privacy regulations with techniques that respect data privacy.

### **Contact**

Please report any issues with the model or contact us:

* Safety issues: safety@stability.ai  
* Security issues: security@stability.ai  
* Privacy issues: privacy@stability.ai  
* License and general: [https://stability.ai/license](https://stability.ai/license)  
* Enterprise license: [https://stability.ai/enterprise](https://stability.ai/enterprise)