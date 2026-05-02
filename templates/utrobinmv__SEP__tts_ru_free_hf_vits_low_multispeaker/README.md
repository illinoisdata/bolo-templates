---
language:
- ru
tags:
- vits
license: apache-2.0
pipeline_tag: text-to-speech
widget:
  - example_title: text to speech
    text: >
      прив+ет, как дел+а? всё +очень хорош+о! а у тебя как?
---

# Text to Speech Russian free multispeaker UtrobinTTS model

This is a multiple speakers text-to-speech model UtrobinTTS for the Russian language. It works on plain text with punctuation separation, and does not require prior conversion of the text into phonemes.
The model with multiple speakers has two voices: 0 - woman, 1 - man.

The size of the model is only 15.1 million parameters.

The text accepts lowercase.

For better generation quality, we recommend putting accents in the text before the vowel letters.

We recommend using the "ruaccent" library for accentuation.

To install "ruaccent", use: 

```bash
pip install -y ruaccent
```



For test inference use Spaces:

https://huggingface.co/spaces/utrobinmv/tts_ru_free_hf_vits_low_multispeaker



Usage example using PyTorch:

```python
from transformers import VitsModel, AutoTokenizer, set_seed
import torch
import scipy
from ruaccent import RUAccent

device = 'cuda' #  'cpu' or 'cuda'

speaker = 0 # 0-woman, 1-man  

set_seed(555)  # make deterministic

# load model
model_name = "utrobinmv/tts_ru_free_hf_vits_low_multispeaker"

model = VitsModel.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.eval()

# load accentizer
accentizer = RUAccent()
accentizer.load(omograph_model_size='turbo', use_dictionary=True, device=device)

# text
text = """Ночью двадцать третьего июня начал извергаться самый высокий 
действующий вулкан в Евразии - Кл+ючевской. Об этом сообщила руководитель 
Камчатской группы реагирования на вулканические извержения, ведущий 
научный сотрудник Института вулканологии и сейсмологии ДВО РАН Ольга Гирина.
«Зафиксированное ночью не просто свечение, а вершинное эксплозивное 
извержение стромболианского типа. Пока такое извержение никому не опасно: 
ни населению, ни авиации» пояснила ТАСС госпожа Гирина."""

# the placement of accents
text = accentizer.process_all(text)
print(text)
# н+очью дв+адцать тр+етьего и+юня н+ачал изверг+аться с+амый выс+окий 
# д+ействующий вулк+ан в евр+азии - ключевск+ой. об +этом сообщ+ила 
# руковод+итель камч+атской гр+уппы реаг+ирования на вулкан+ические
# изверж+ения, вед+ущий на+учный сотр+удник инстит+ута вулканол+огии
# и сейсмол+огии дво ран +ольга г+ирина. « зафикс+ированное н+очью не
# пр+осто свеч+ение, а верш+инное эксплоз+ивное изверж+ение 
# стромболи+анского т+ипа. пок+а так+ое изверж+ение ником+у не оп+асно:
# ни насел+ению, ни ави+ации » поясн+ила тасс госпож+а г+ирина.

inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    output = model(**inputs.to(device), speaker_id=speaker).waveform
    output = output.detach().cpu().numpy()
    
scipy.io.wavfile.write("tts_audio.wav", rate=model.config.sampling_rate,
                       data=output[0])
```



For displayed in a Jupyter Notebook / Google Colab:

```python
from IPython.display import Audio

Audio(output, rate=model.config.sampling_rate)
```

##  

Usage example using ONNX:

First copy the model.onnx file to the folder "tts_ru_free_hf_vits_low_multispeaker".

```python
import numpy as np
import scipy
import onnxruntime
from ruaccent import RUAccent
from transformers import AutoTokenizer

speaker = 0 # 0-woman, 1-man

# load model
model_path = "tts_ru_free_hf_vits_low_multispeaker/model.onnx"

sess_options = onnxruntime.SessionOptions()
model = onnxruntime.InferenceSession(model_path, sess_options=sess_options)
tokenizer = AutoTokenizer.from_pretrained("utrobinmv/tts_ru_free_hf_vits_low_multispeaker")

# text
text = """Ночью двадцать третьего июня начал извергаться самый высокий 
действующий вулкан в Евразии - Кл+ючевской. Об этом сообщила руководитель 
Камчатской группы реагирования на вулканические извержения, ведущий 
научный сотрудник Института вулканологии и сейсмологии ДВО РАН Ольга Гирина.
«Зафиксированное ночью не просто свечение, а вершинное эксплозивное 
извержение стромболианского типа. Пока такое извержение никому не опасно: 
ни населению, ни авиации» пояснила ТАСС госпожа Гирина."""

# load accentizer
accentizer = RUAccent()
accentizer.load(omograph_model_size='turbo', use_dictionary=True)

# the placement of accents
text = accentizer.process_all(text)

# inference
inputs = tokenizer(text, return_tensors="np")
sid = np.array([speaker])
sampling_rate = 16000

output = model.run(
            None,
            {
                "input_ids": inputs['input_ids'],
                "attention_mask": inputs['attention_mask'],
                "sid": sid,
            },
        )[0]
        
scipy.io.wavfile.write("tts_audio.wav", rate=sampling_rate,
                       data=output[0])
```



For displayed in a Jupyter Notebook / Google Colab:

```python
from IPython.display import Audio

Audio(output, rate=sampling_rate)
```

##  



## Languages covered

Russian (ru_RU)