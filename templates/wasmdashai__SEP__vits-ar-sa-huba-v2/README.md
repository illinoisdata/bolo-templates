---
language:
- ar
library_name: transformers
pipeline_tag: text-to-speech
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

An advanced text-to-speech (TTS) system specifically designed for the Saudi dialect, built on the VITS architecture and utilizing the pre-trained weights from Facebook's vits ara model. The model is capable of:

Generating natural and realistic speech: Producing high-quality Saudi dialect speech that closely mimics human voices, preserving intonation and linguistic nuances.
Understanding colloquial text: Processing text written in the Saudi dialect, including idiomatic expressions and local vocabulary.
Controlling voice characteristics: Adjusting various aspects of the generated speech, such as pitch and speaking rate.
Providing ease of use: Offering a simple and user-friendly interface for converting text to speech with high quality.
Model Details
VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech) is an end-to-end speech synthesis model that predicts a speech waveform conditional on an input text sequence. It is a conditional variational autoencoder (VAE) comprised of a posterior encoder, decoder, and conditional prior.

A set of spectrogram-based acoustic features are predicted by the flow-based module, which is formed of a Transformer-based text encoder and multiple coupling layers. The spectrogram is decoded using a stack of transposed convolutional layers, much in the same style as the HiFi-GAN vocoder. Motivated by the one-to-many nature of the TTS problem, where the same text input can be spoken in multiple ways, the model also includes a stochastic duration predictor, which allows the model to synthesise speech with different rhythms from the same input text.

## Usage

MMS-TTS is available in the 🤗 Transformers library from version 4.33 onwards. To use this checkpoint, 
first install the latest version of the library:

```
pip install  transformers[torch]
```

Then, run inference with the following code-snippet:

```python
from transformers import VitsModel, AutoTokenizer
import torch

model = VitsModel.from_pretrained("wasmdashai/vits-ar-sa-huba")
tokenizer = AutoTokenizer.from_pretrained("wasmdashai/vits-ar-sa-huba")

text = "السلام عليكم  كيفك  عساك بخير  "
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
  full_generation =model(**inputs)
full_generation_waveform = full_generation.waveform.cpu().numpy().reshape(-1)

from IPython.display import Audio

Audio(full_generation_waveform, rate=model.config.sampling_rate)

```
### Output  full_generation_waveform
![pareto](https://huggingface.co/wasmdashai/vits-ar-sa-huba/blob/main/1f730f47-903a-4262-a063-eca4d85e5afe.flac)
## Contact
You can also email us at modelasg@gmail.com



## مجموعة نماذج توليد اللهجات العربية

### مقدمة

يسرنا أن نعلن عن إصدار مجموعة من نماذج توليد اللهجات العربية قريبًا. تم تصميم هذه النماذج باستخدام تقنيات الذكاء الاصطناعي المتقدمة لتقديم تجربة طبيعية وواقعية في تحويل النص إلى كلام (Text-to-Speech) بمختلف اللهجات العربية.

### جدول النماذج
| **اللهجة**        | **اسم النموذج**                                                                  | **الوصف**                                                                 | **تاريخ الإصدار المتوقع** | **مستوى جودة الصوت** |
|-------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------|----------------------------|----------------------|
|  اللغة العربية       | [vits-ar](https://huggingface.co/wasmdashai/vits-ar)                      | نموذج لتحويل النص إلى كلام باللهجة اليمنية بتفاصيل دقيقة.                  | متوفر                     | متوسط                |
| اللهجة اليمنية      | [vits-ar-ye](https://huggingface.co/wasmdashai/vits-ar-ye)                      | نموذج لتحويل النص إلى كلام باللهجة اليمنية بتفاصيل دقيقة.                  | قريباً                     | متوسط                |
| اللهجة السعودية    | [vits-ar-sa](https://huggingface.co/wasmdashai/vits-ar-sa-huba)                      | نموذج لتحويل النص إلى كلام باللهجة السعودية بجودة عالية وتفاصيل دقيقة.     | متوفر                     | متوسط                |
| اللهجة المصرية     | [vits-ar-eg](https://huggingface.co/wasmdashai/vits-ar-eg)                      | نموذج لتحويل النص إلى كلام باللهجة المصرية بأسلوب طبيعي وسلس.              | قريباً                     | متوسط                |
| اللهجة اللبنانية   | [vits-ar-lb](https://huggingface.co/wasmdashai/vits-ar-lb)                      | نموذج متخصص في اللهجة اللبنانية لتوليد كلام بتفاصيل دقيقة وواقعية.         | قريباً                     | متوسط                |
| اللهجة المغربية    | [vits-ar-ma](https://huggingface.co/wasmdashai/vits-ar-ma)                      | نموذج لتحويل النص إلى كلام باللهجة المغربية بقدرة على فهم المصطلحات المحلية.| قريباً                     | متوسط                |
| اللهجة الإماراتية  | [vits-ar-ae](https://huggingface.co/wasmdashai/vits-ar-ae)                      | نموذج لتحويل النص إلى كلام باللهجة الإماراتية بواقعية وتفاصيل دقيقة.        | قريباً                     | متوسط                |
| اللهجة الأردنية     | [vits-ar-jo](https://huggingface.co/wasmdashai/vits-ar-jo)                      | نموذج لتحويل النص إلى كلام باللهجة الأردنية بإتقان للتفاصيل الصوتية.        | قريباً                     | متوسط                |
| اللهجة العراقية     | [vits-ar-iq](https://huggingface.co/wasmdashai/vits-ar-iq)                      | نموذج لتوليد الكلام باللهجة العراقية بدقة في نطق الكلمات والتعابير الشائعة.  | قريباً                     | متوسط                |
| اللهجة السورية      | [vits-ar-sy](https://huggingface.co/wasmdashai/vits-ar-sy)                      | نموذج لتحويل النص إلى كلام باللهجة السورية بوضوح وصوت طبيعي.               | قريباً                     | متوسط                |
| اللهجة الفلسطينية  | [vits-ar-ps](https://huggingface.co/wasmdashai/vits-ar-ps)                      | نموذج لتحويل النص إلى كلام باللهجة الفلسطينية بتفاصيل دقيقة.               | قريباً                     | متوسط                |
| اللهجة السودانية    | [vits-ar-sd](https://huggingface.co/wasmdashai/vits-ar-sd)                      | نموذج لتحويل النص إلى كلام باللهجة السودانية مع فهم المفردات المحلية.       | قريباً                     | متوسط                |
| اللهجة الجزائرية    | [vits-ar-dz](https://huggingface.co/wasmdashai/vits-ar-dz)                      | نموذج لتحويل النص إلى كلام باللهجة الجزائرية بدقة وجودة عالية.              | قريباً                     | متوسط                |
| اللهجة التونسية     | [vits-ar-tn](https://huggingface.co/wasmdashai/vits-ar-tn)                      | نموذج لتحويل النص إلى كلام باللهجة التونسية بإتقان للتفاصيل المحلية.         | قريباً                     | متوسط                |
| اللهجة الليبية      | [vits-ar-ly](https://huggingface.co/wasmdashai/vits-ar-ly)                      | نموذج لتحويل النص إلى كلام باللهجة الليبية بدقة وواقعية في النطق.           | قريباً                     | متوسط                |
| اللهجة البحرينية    | [vits-ar-bh](https://huggingface.co/wasmdashai/vits-ar-bh)                      | نموذج لتحويل النص إلى كلام باللهجة البحرينية بجودة صوت عالية.               | قريباً                     | متوسط                |
| اللهجة العمانية     | [vits-ar-om](https://huggingface.co/wasmdashai/vits-ar-om)                      | نموذج لتحويل النص إلى كلام باللهجة العمانية بدقة ووضوح في النطق.             | قريباً                     | متوسط                |
| اللهجة القطرية      | [vits-ar-qa](https://huggingface.co/wasmdashai/vits-ar-qa)                      | نموذج لتحويل النص إلى كلام باللهجة القطرية بتفاصيل دقيقة وواقعية.           | قريباً                     | متوسط                |
| اللهجة الكويتية     | [vits-ar-kw](https://huggingface.co/wasmdashai/vits-ar-kw)                      | نموذج لتحويل النص إلى كلام باللهجة الكويتية بجودة عالية ووضوح.              | قريباً                     | متوسط                |
| اللهجة الموريتانية  | [vits-ar-mr](https://huggingface.co/wasmdashai/vits-ar-mr)                      | نموذج لتحويل النص إلى كلام باللهجة الموريتانية بتفاصيل دقيقة وواقعية.       | قريباً                     | متوسط                |

### التفاصيل الفنية

تعتمد جميع النماذج على بنية VITS، وهي نموذج شامل لتحويل النص إلى كلام يتيح توليد موجات صوتية واقعية بناءً على المدخلات النصية. تحتوي النماذج على محولات لتحليل النص وتوليد الكلام بناءً على خصائص الصوت المحلية لكل لهجة.

### الترقيات المستقبلية

سيتم تقديم تحديثات منتظمة لتحسين جودة الصوت وزيادة كفاءة فهم اللهجات المختلفة. تابعونا لمعرفة المزيد حول تواريخ الإطلاق الدقيقة لكل نموذج.



## Acknowledgements



This implementation is based on [tts-arabic](https://github.com/nipponjo/tts-arabic-pytorch), [VITS](https://github.com/jaywalnut310/vits), [Finetune VITS](https://github.com/ylacombe/finetune-hf-vits) and [Bert-VITS2](https://github.com/fishaudio/Bert-VITS2). We appreciate their awesome work.