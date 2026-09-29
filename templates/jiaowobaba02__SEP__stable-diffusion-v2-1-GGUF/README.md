---
pipeline_tag: text-to-image
tags:
- art
- stable-diffusion
---

# Stable-diffusion-GGUF

There are some files quantitated to q8_0 , q5_0 , q5_1 , q4_1 .
To run these models, you can go to [this page](https://github.com/leejet/stable-diffusion.cpp) to download the code or run this command 
```
git clone --recursive https://github.com/leejet/stable-diffusion.cpp.git
```
\
And then compile it just as the instructions on the github page. \
Finally,run 
```
./sd -m '/model/stable_diffusion-ema-pruned-v2-1_768.q8_0.gguf'  -p "a lovely cat" -s -1
``` 
. Then you can see the 'output.png'.