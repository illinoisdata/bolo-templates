---
license: mit
---

This repo includes a Version of Phi-3 that was quantized to AWQ using AutoAWQ.
Currently hosting via the TGI docker image fails due to its fallback on AutoModel and that not being compatible with AWQ.
Hosting on vLLM is recommended.

To run the model you need to set the trust-remote-code (or similar) flag.
While the remote code comes from microsoft (see LICENSE information in the file) you should validate the code yourself before deployment.