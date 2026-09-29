---
license: other
inference: false
base_model: CohereForAI/aya-34-8B
license_link: LICENSE
quantized_by: jartine
prompt_template: |
  <BOS_TOKEN>
  <|START_OF_TURN_TOKEN|>
  <|USER_TOKEN|>{{prompt}}<|END_OF_TURN_TOKEN|>
  <|START_OF_TURN_TOKEN|>
  <|CHATBOT_TOKEN|>
tags:
- llamafile
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
---

# aya-34-8B - llamafile

This repository contains executable weights (which we call
[llamafiles](https://github.com/Mozilla-Ocho/llamafile)) that run on
Linux, MacOS, Windows, FreeBSD, OpenBSD, and NetBSD for AMD64 and ARM64.

- Model creator: [CohereForAI](https://huggingface.co/CohereForAI)
- Original model: [CohereForAI/aya-23-8B](https://huggingface.co/CohereForAI/aya-23-8B)

This is multilingual model, with a focus on Arabic.

## Quickstart

You can run the following commands which download, concatenate, and
execute the model.

```
wget https://huggingface.co/jartine/aya-23-8B-llamafile/resolve/main/aya-23-8B.Q6_K.llamafile
chmod +x aya-23-8B.Q6_K.llamafile
./aya-23-8B.Q6_K.llamafile --help   # view manual
./aya-23-8B.Q6_K.llamafile          # launch web gui + oai api
./aya-23-8B.Q6_K.llamafile -p ...   # cli interface (scriptable)
```

Alternatively, you may download an official `llamafile` executable from
Mozilla Ocho on GitHub, in which case you can use the Mixtral llamafiles
as a simple weights data file.

```
llamafile -m ./aya-23-8B.Q6_K.llamafile ...
```

For further information, please see the [llamafile
README](https://github.com/mozilla-ocho/llamafile/).

Having **trouble?** See the ["Gotchas"
section](https://github.com/mozilla-ocho/llamafile/?tab=readme-ov-file#gotchas)
of the README.

## Prompting

Command-line instruction example:

```
./aya-23-8B.Q6_K.llamafile --log-disable --silent-prompt -p '<BOS_TOKEN>
<|START_OF_TURN_TOKEN|>
<|USER_TOKEN|>Who is the president?<|END_OF_TURN_TOKEN|>
<|START_OF_TURN_TOKEN|>
<|CHATBOT_TOKEN|>'
```

"Prompt Template" (copy and paste this into the web GUI):

```
<BOS_TOKEN>
<|SYSTEM_TOKEN|>{{prompt}}<|END_OF_TURN_TOKEN|>
{{history}}
<|START_OF_TURN_TOKEN|>
<|CHATBOT_TOKEN|>
```

"Chat history template" (copy and paste this into the web GUI):

```
<|START_OF_TURN_TOKEN|>
<|USER_TOKEN|>{{message}}<|END_OF_TURN_TOKEN|>
```

The maximum context size of this model is 8192 tokens. These llamafiles
use a default context size of 512 tokens. Whenever you need the maximum
context size to be available with llamafile for any given model, you can
pass the `-c 0` flag. The temperature on these llamafiles is set to zero
by default, because it helps. This can be changed, e.g. `--temp 0.8`.

## License

The aya-34-8B license requires:

- You can't use these weights for commercial purposes

- You have to give Cohere credit if you share or fine tune it

- You can't use it for purposes they consider unacceptable, such as
  spam, misinformation, etc. The license says they can change the
  definition of acceptable use at will.

- The CC-BY-NC 4.0 stipulates no downstream restrictions, so you can't
  tack on your own list of unacceptable uses too if you create and
  distribute a fine-tuned version.

This special license only applies to the LLM weights (i.e. the .gguf
file inside .llamafile). The llamafile software itself is permissively
licensed, having only components licensed under terms like Apache 2.0,
MIT, BSD, ISC, zlib, etc.

## About llamafile

llamafile is a new format introduced by Mozilla Ocho on Nov 20th 2023.
It uses Cosmopolitan Libc to turn LLM weights into runnable llama.cpp
binaries that run on the stock installs of six OSes for both ARM64 and
AMD64.

In addition to being executables, llamafiles are also zip archives. Each
llamafile contains a GGUF file, which you can extract using the `unzip`
command. If you want to change or add files to your llamafiles, then the
`zipalign` command (distributed on the llamafile github) should be used
instead of the traditional `zip` command.

---

# Model Card for Aya-23-8B

**Try Aya 23**

You can try out Aya 23 (35B) before downloading the weights in our hosted Hugging Face Space [here](https://huggingface.co/spaces/CohereForAI/aya-23).

## Model Summary

Aya 23 is an open weights research release of an instruction fine-tuned model with highly advanced multilingual capabilities. Aya 23 focuses on pairing a highly performant pre-trained [Command family](https://huggingface.co/CohereForAI/c4ai-command-r-plus) of models with the recently released [Aya Collection](https://huggingface.co/datasets/CohereForAI/aya_collection). The result is a powerful multilingual large language model serving 23 languages.

This model card corresponds to the 8-billion version of the Aya 23 model. We also released a 35-billion version which you can find [here](https://huggingface.co/CohereForAI/aya-23-35B).

We cover 23 languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese

Developed by: [Cohere For AI](https://cohere.for.ai) and [Cohere](https://cohere.com/) 

- Point of Contact: Cohere For AI: [cohere.for.ai](https://cohere.for.ai/)
- License: [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license), requires also adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)
- Model: aya-23-8B
- Model Size: 8 billion parameters

### Usage

Please install transformers from the source repository that includes the necessary changes for this model

```python
# pip install transformers==4.41.1
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereForAI/aya-23-8B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Format message with the command-r-plus chat template
messages = [{"role": "user", "content": "Anneme onu ne kadar sevdiğimi anlatan bir mektup yaz"}]
input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
## <BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Anneme onu ne kadar sevdiğimi anlatan bir mektup yaz<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>

gen_tokens = model.generate(
    input_ids, 
    max_new_tokens=100, 
    do_sample=True, 
    temperature=0.3,
    )

gen_text = tokenizer.decode(gen_tokens[0])
print(gen_text)
```

### Example Notebook

[This notebook](https://huggingface.co/CohereForAI/aya-23-8B/blob/main/Aya_23_notebook.ipynb) showcases a detailed use of Aya 23 (8B) including inference and fine-tuning with [QLoRA](https://huggingface.co/blog/4bit-transformers-bitsandbytes). 

## Model Details

**Input**: Models input text only.

**Output**: Models generate text only.

**Model Architecture**: Aya-23-8B is an auto-regressive language model that uses an optimized transformer architecture. After pretraining, this model is fine-tuned (IFT) to follow human instructions.

**Languages covered**: The model is particularly optimized for multilinguality and supports the following languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese

**Context length**: 8192

### Evaluation

<img src="benchmarks.png" alt="multilingual benchmarks" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="winrates.png" alt="average win rates" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

Please refer to the [Aya 23 technical report](https://cohere.com/research/papers/aya-command-23-8b-and-35b-technical-report-2024-05-23) for further details about the base model, data, instruction tuning, and evaluation.

### Model Card Contact

For errors or additional questions about details in this model card, contact info@for.ai.

### Terms of Use

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant multilingual model to researchers all over the world. This model is governed by a [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license) License with an acceptable use addendum, and also requires adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy).

### Try the model today

You can try Aya 23 in the Cohere [playground](https://dashboard.cohere.com/playground/chat) here. You can also use it in our dedicated Hugging Face Space [here](https://huggingface.co/spaces/CohereForAI/aya-23).

### Citation info
```bibtex
@misc{aya23technicalreport,
  title={Aya 23: Open Weight Releases to Further Multilingual Progress},
  author={Viraat Aryabumi, John Dang, Dwarak Talupuru, Saurabh Dash, David Cairuz, Hangyu Lin, Bharat Venkitesh, Madeline Smith, Kelly Marchisio, Sebastian Ruder, Acyr Locatelli, Julia Kreutzer, Nick Frosst, Phil Blunsom, Marzieh Fadaee, Ahmet Üstün, and Sara Hooker},
  url={https://cohere.com/research/papers/aya-command-23-8b-and-35b-technical-report-2024-05-23},
  year={2024}
}

```