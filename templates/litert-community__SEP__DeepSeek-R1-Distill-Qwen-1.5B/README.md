---
license: mit
base_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
pipeline_tag: text-generation
library_name: litert-lm
tags:
- chat
---

# litert-community/DeepSeek-R1-Distill-Qwen-1.5B

This model provides a few variants of
[deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) that are ready for
deployment on Android using the
[LiteRT (fka TFLite) stack](https://ai.google.dev/edge/litert),
[MediaPipe LLM Inference API](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference) and
[LiteRt-LM](https://github.com/google-ai-edge/LiteRT-LM).

## Use the models

### Colab

*Disclaimer: The target deployment surface for the LiteRT models is
Android/iOS/Web and the stack has been optimized for performance on these
targets. Trying out the system in Colab is an easier way to familiarize yourself
with the LiteRT stack, with the caveat that the performance (memory and latency)
on Colab could be much worse than on a local device.*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https://huggingface.co/litert-community/DeepSeek-R1-Distill-Qwen-1.5B/blob/main/notebook.ipynb)

### Android

#### Edge Gallery App

*   Download or build the [app](https://github.com/google-ai-edge/gallery?tab=readme-ov-file#-get-started-in-minutes) from GitHub.

*   Install the [app](https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery&pli=1) from Google Play

*   Follow the instructions in the app.

#### LLM Inference API

*   Download and install
    [the apk](https://github.com/google-ai-edge/mediapipe-samples/releases/latest/download/llm_inference-debug.apk).
*   Follow the instructions in the app.

To build the demo app from source, please follow the
[instructions](https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/llm_inference/android/README.md)
from the GitHub repository.

## Performance

### Android

Note that all benchmark stats are from a Samsung S24 Ultra with 
1280 KV cache size with multiple prefill signatures enabled.

<table border="1">
  <tr>
   <th>Backend</th>
   <th>Quantization</th>
   <th>Context Length</th>
   <th>Prefill (tokens/sec)</th>
   <th>Decode (tokens/sec)</th>
   <th>Time-to-first-token (sec)</th>
   <th>Model size (MB)</th>
   <th>Peak RSS Memory (MB)</th>
   <th>GPU Memory (MB)</th>
  </tr>
  <tr>
<td><p style="text-align: right">CPU</p></td>
<td><p style="text-align: right">dynamic_int8</p></td>
<td><p style="text-align: right">4096</p></td>
<td><p style="text-align: right">166.50 tk/s</p></td>
<td><p style="text-align: right">26.35 tk/s</p></td>
<td><p style="text-align: right">6.41 s</p></td>
<td><p style="text-align: right">1831.43 MB</p></td>
<td><p style="text-align: right">2221 MB</p></td>
<td><p style="text-align: right">N/A</p></td>
</tr>
<tr>
<td><p style="text-align: right">GPU</p></td>
<td><p style="text-align: right">dynamic_int8</p></td>
<td><p style="text-align: right">4096</p></td>
<td><p style="text-align: right">927.54 tk/s</p></td>
<td><p style="text-align: right">26.98 tk/s</p></td>
<td><p style="text-align: right">5.46 s</p></td>
<td><p style="text-align: right">1831.43 MB</p></td>
<td><p style="text-align: right">2096 MB</p></td>
<td><p style="text-align: right">1659 MB</p></td>
</tr>

</table>

*   Model Size: measured by the size of the .tflite flatbuffer (serialization
    format for LiteRT models)
*   Memory: indicator of peak RAM usage
*   The inference on CPU is accelerated via the LiteRT
    [XNNPACK](https://github.com/google/XNNPACK) delegate with 4 threads
*   Benchmark is done assuming XNNPACK cache is enabled
*   Benchmark is run with cache enabled and initialized. During the first run, the time to first token may differ.
*   dynamic_int8: quantized model with int8 weights and float activations.