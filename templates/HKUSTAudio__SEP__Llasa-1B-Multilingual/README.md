---
license: cc-by-nc-4.0
language:
- zh
- en
- de
- fr
- ja
- ko
- nl
- es
- it
- pt
- pl
base_model:
- meta-llama/Llama-3.2-1B-Instruct
tags:
- Text-to-Speech
pipeline_tag: text-to-speech
---

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2502.04128)

**Update (2025-02-13):** Add [Llasa finetune instruction](https://github.com/zhenye234/LLaSA_training/tree/main/finetune).

We recommend reading [this blog post](https://huggingface.co/blog/Steveeeeeeen/llasagna) for more insights.

**Main Idea:**  
This model enhances previous  Llasa TTS by incorporating multilingual data. The approach leverages the LLAMA-initialized text BPE tokenizer,
which can handle multilingual text without the need to design language-specific G2P (grapheme-to-phoneme) systems.
Although the multilingual training data is limited—using only the MLS (En/Fr/De/Nl/Es/It/Pt/Pl) and Emilia  (En/Zh/De/Fr/Ja/Ko) datasets—resulting in potentially less optimal performance for some languages due to data scarcity, 
our model can serve as a  base TTS model. It is particularly suitable for fine-tuning for a specific language, as texts in various languages can be uniformly processed using the BPE tokenizer from Llama.

This model is not mentioned in the paper, but it follows the same methodology.

LLaSA: Scaling Train-Time and Inference-Time Compute for LLaMA-based Speech Synthesis 


- **Train from Scratch**: If you want to train the model from scratch, use the [LLaSA Training Repository](https://github.com/zhenye234/LLaSA_training).

- **Scale for Test-Time Computation**: If you want to experiment with scaling for test-time computation, use the [LLaSA Testing Repository](https://github.com/zhenye234/LLaSA_inference).

 

## How to use
Install [XCodec2](https://huggingface.co/HKUSTAudio/xcodec2).  

**1. Speech synthesis solely from input text**
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import soundfile as sf

llasa_1b ='HKUSTAudio/Llasa-1B-Multilingual'

tokenizer = AutoTokenizer.from_pretrained(llasa_1b)
model = AutoModelForCausalLM.from_pretrained(llasa_1b)
model.eval() 
model.to('cuda')

from xcodec2.modeling_xcodec2 import XCodec2Model
 
model_path = "HKUSTAudio/xcodec2"  
 
Codec_model = XCodec2Model.from_pretrained(model_path)
Codec_model.eval().cuda()   

input_text = 'Auch das unter Schirmherrschaft der Vereinten Nationen ausgehandelte Klimaschutzabkommen von Pariswollen die USA verlassen.'
# input_text = '言いなりにならなきゃいけないほど後ろめたい事をしたわけでしょ。'
def ids_to_speech_tokens(speech_ids):
 
    speech_tokens_str = []
    for speech_id in speech_ids:
        speech_tokens_str.append(f"<|s_{speech_id}|>")
    return speech_tokens_str

def extract_speech_ids(speech_tokens_str):
 
    speech_ids = []
    for token_str in speech_tokens_str:
        if token_str.startswith('<|s_') and token_str.endswith('|>'):
            num_str = token_str[4:-2]

            num = int(num_str)
            speech_ids.append(num)
        else:
            print(f"Unexpected token: {token_str}")
    return speech_ids

#TTS start!
with torch.no_grad():
 
    formatted_text = f"<|TEXT_UNDERSTANDING_START|>{input_text}<|TEXT_UNDERSTANDING_END|>"

    # Tokenize the text
    chat = [
        {"role": "user", "content": "Convert the text to speech:" + formatted_text},
        {"role": "assistant", "content": "<|SPEECH_GENERATION_START|>"}
    ]

    input_ids = tokenizer.apply_chat_template(
        chat, 
        tokenize=True, 
        return_tensors='pt', 
        continue_final_message=True
    )
    input_ids = input_ids.to('cuda')
    speech_end_id = tokenizer.convert_tokens_to_ids('<|SPEECH_GENERATION_END|>')

    # Generate the speech autoregressively
    outputs = model.generate(
        input_ids,
        max_length=2048,  # We trained our model with a max length of 2048
        eos_token_id= speech_end_id ,
        do_sample=True,    
        top_p=1,           #  Adjusts the diversity of generated content
        temperature=0.8,   #  Controls randomness in output
    )
    # Extract the speech tokens
    generated_ids = outputs[0][input_ids.shape[1]:-1]

    speech_tokens = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)   

    # Convert  token <|s_23456|> to int 23456 
    speech_tokens = extract_speech_ids(speech_tokens)

    speech_tokens = torch.tensor(speech_tokens).cuda().unsqueeze(0).unsqueeze(0)

    # Decode the speech tokens to speech waveform
    gen_wav = Codec_model.decode_code(speech_tokens) 
 

sf.write("gen.wav", gen_wav[0, 0, :].cpu().numpy(), 16000)
```

**2. Speech synthesis utilizing a given speech prompt**

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import soundfile as sf

llasa_1b ='HKUSTAudio/Llasa-1B-Multilingual'

tokenizer = AutoTokenizer.from_pretrained(llasa_1b)
model = AutoModelForCausalLM.from_pretrained(llasa_1b)
model.eval() 
model.to('cuda')

from xcodec2.modeling_xcodec2 import XCodec2Model
 
model_path = "HKUST-Audio/xcodec2"  
 
Codec_model = XCodec2Model.from_pretrained(model_path)
Codec_model.eval().cuda()   
# only 16khz speech support!
prompt_wav, sr = sf.read("太乙真人.wav")   # you can find wav in Files
#prompt_wav, sr = sf.read("Anna.wav") # English prompt
prompt_wav = torch.from_numpy(prompt_wav).float().unsqueeze(0)  

prompt_text ="对，这就是我万人敬仰的太乙真人，虽然有点婴儿肥，但也掩不住我逼人的帅气。"
#promt_text = "A chance to leave him alone, but... No. She just wanted to see him again. Anna, you don't know how it feels to lose a sister. Anna, I'm sorry, but your father asked me not to tell you anything."
target_text = '突然，身边一阵笑声。我看着他们，意气风发地挺直了胸膛，甩了甩那稍显肉感的双臂，轻笑道："我身上的肉，是为了掩饰我爆棚的魅力，否则，岂不吓坏了你们呢？"'
#target_text = "Dealing with family secrets is never easy. Yet, sometimes, omission is a form of protection, intending to safeguard some from the harsh truths. One day, I hope you understand the reasons behind my actions. Until then, Anna, please, bear with me."
input_text = prompt_text   + target_text

def ids_to_speech_tokens(speech_ids):
 
    speech_tokens_str = []
    for speech_id in speech_ids:
        speech_tokens_str.append(f"<|s_{speech_id}|>")
    return speech_tokens_str

def extract_speech_ids(speech_tokens_str):
 
    speech_ids = []
    for token_str in speech_tokens_str:
        if token_str.startswith('<|s_') and token_str.endswith('|>'):
            num_str = token_str[4:-2]

            num = int(num_str)
            speech_ids.append(num)
        else:
            print(f"Unexpected token: {token_str}")
    return speech_ids

#TTS start!
with torch.no_grad():
    # Encode the prompt wav
    vq_code_prompt = Codec_model.encode_code(input_waveform=prompt_wav)
    print("Prompt Vq Code Shape:", vq_code_prompt.shape )   

    vq_code_prompt = vq_code_prompt[0,0,:]
    # Convert int 12345 to token <|s_12345|>
    speech_ids_prefix = ids_to_speech_tokens(vq_code_prompt)

    formatted_text = f"<|TEXT_UNDERSTANDING_START|>{input_text}<|TEXT_UNDERSTANDING_END|>"

    # Tokenize the text and the speech prefix
    chat = [
        {"role": "user", "content": "Convert the text to speech:" + formatted_text},
        {"role": "assistant", "content": "<|SPEECH_GENERATION_START|>" + ''.join(speech_ids_prefix)}
    ]

    input_ids = tokenizer.apply_chat_template(
        chat, 
        tokenize=True, 
        return_tensors='pt', 
        continue_final_message=True
    )
    input_ids = input_ids.to('cuda')
    speech_end_id = tokenizer.convert_tokens_to_ids('<|SPEECH_GENERATION_END|>')

    # Generate the speech autoregressively
    outputs = model.generate(
        input_ids,
        max_length=2048,  # We trained our model with a max length of 2048
        eos_token_id= speech_end_id ,
        do_sample=True,
        top_p=1,           
        temperature=0.8,
    )
    # Extract the speech tokens
    generated_ids = outputs[0][input_ids.shape[1]-len(speech_ids_prefix):-1]

    speech_tokens = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)   

    # Convert  token <|s_23456|> to int 23456 
    speech_tokens = extract_speech_ids(speech_tokens)

    speech_tokens = torch.tensor(speech_tokens).cuda().unsqueeze(0).unsqueeze(0)

    # Decode the speech tokens to speech waveform
    gen_wav = Codec_model.decode_code(speech_tokens) 

    # if only need the generated part
    # gen_wav = gen_wav[:,:,prompt_wav.shape[1]:]

sf.write("gen.wav", gen_wav[0, 0, :].cpu().numpy(), 16000)
```


## Disclaimer

This model is licensed under the CC BY-NC  4.0 License, which prohibits free commercial use because of ethics and privacy concerns; detected violations will result in legal consequences.

This codebase is strictly prohibited from being used for any illegal purposes in any country or region. Please refer to your local laws about DMCA and other related laws.