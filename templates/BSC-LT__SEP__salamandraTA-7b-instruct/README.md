---
license: apache-2.0
library_name: transformers
pipeline_tag: translation
language:
- bg
- ca
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fi
- fr
- ga
- gl
- hr
- hu
- it
- lt
- lv
- mt
- nl
- nb
- 'no'
- nn
- oc
- pl
- pt
- ro
- ru
- sl
- sk
- sr
- sv
- uk
- ast
- an
base_model:
- BSC-LT/salamandra-7b
---


![](./images/salamandra_header.png)

# SalamandraTA Model Card

SalamandraTA-7b-instruct is a translation LLM that has been instruction-tuned from SalamandraTA-7b-base. 
The base model results from continually pre-training [Salamandra-7b](https://huggingface.co/BSC-LT/salamandra-7b) on parallel data and has not been published, 
but is reserved for internal use. 
SalamandraTA-7b-instruct is proficient in 35 European languages (plus 3 varieties) and supports translation-related tasks, namely: sentence-level-translation, 
paragraph-level-translation, document-level-translation, automatic post-editing, grammar checking, machine translation evaluation, alternative translations, 
named-entity-recognition and context-aware translation.

> [!WARNING]
> **DISCLAIMER:** This version of Salamandra is tailored exclusively for translation tasks. It lacks chat capabilities and has not been trained with any chat instructions.


---

## Model Details

### Description

SalamandraTA-7b-base is a continual pre-training of [Salamandra-7b](https://huggingface.co/BSC-LT/salamandra-7b) using parallel data, resulting in a total of 424B tokens processed during training.


### Architecture

|                         |               |
|-------------------------|:--------------|
| Total Parameters        | 7,768,117,248 |
| Embedding Parameters    | 1,048,576,000 |
| Layers                  | 32            |
| Hidden size             | 4,096         |
| Attention heads         | 32            |
| Context length          | 8,192         |
| Vocabulary size         | 256,000       |
| Precision               | bfloat16      |
| Embedding type          | RoPE          |
| Activation Function     | SwiGLU        |
| Layer normalization     | RMS Norm      |
| Flash attention         | ✅            |
| Grouped Query Attention | ✅            |
| Num. query groups       | 8             |


---

## Intended Use

### Direct Use

The model is intended for both research and commercial use in any of the languages included in the training data for general machine translation tasks.

### Out-of-scope Use

The model is not intended for malicious activities, such as harming others or violating human rights. 
Any downstream application must comply with current laws and regulations. 
Irresponsible usage in production environments without proper risk assessment and mitigation is also discouraged. 

---


## Hardware and Software

### Training Framework

SalamandraTA-7b-base was continually pre-trained using NVIDIA’s [NeMo Framework](https://docs.nvidia.com/nemo-framework/index.html), 
which leverages PyTorch Lightning for efficient model training in highly distributed settings.

SalamandraTA-7b-instruct was produced with [FastChat](https://github.com/lm-sys/FastChat).

### Compute Infrastructure

All models were trained on [MareNostrum 5](https://www.bsc.es/ca/marenostrum/marenostrum-5), a pre-exascale EuroHPC supercomputer hosted and
operated by Barcelona Supercomputing Center.

The accelerated partition is composed of 1,120 nodes with the following specifications:
- 4x Nvidia Hopper GPUs with 64GB HBM2 memory
- 2x Intel Sapphire Rapids 8460Y+ at 2.3Ghz and 32c each (64 cores)
- 4x NDR200 (BW per node 800Gb/s)
- 512 GB of Main memory (DDR5)
- 460GB on NVMe storage

---


## How to use

You can translate between the following **35 languages** (and 3 varieties):

Aragonese, Asturian, Basque, Bulgarian, Catalan (and Catalan-Valencian variety), Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hungarian, 
Irish, Italian, Latvian, Lithuanian, Maltese, Norwegian (Bokmål and Nynorsk varieties), Occitan (and Aranese variety), Polish, Portuguese, Romanian, Russian, Serbian, Slovak, 
Slovenian, Spanish, Swedish, Ukrainian, Welsh.

The instruction-following model uses the commonly adopted ChatML template:

```
<|im_start|>system
{SYSTEM PROMPT}<|im_end|>
<|im_start|>user
{USER PROMPT}<|im_end|>
<|im_start|>assistant
{MODEL RESPONSE}<|im_end|>
<|im_start|>user
[...]
```

The easiest way to apply it is by using the tokenizer's built-in functions, as shown in the following snippet.

```python
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model_id = "BSC-LT/salamandraTA-7b-instruct"

source = 'Spanish'
target = 'Catalan'
sentence = "Ayer se fue, tomó sus cosas y se puso a navegar. Una camisa, un pantalón vaquero y una canción, dónde irá, dónde irá. Se despidió, y decidió batirse en duelo con el mar. Y recorrer el mundo en su velero. Y navegar, nai-na-na, navegar"
 
text = f"Translate the following text from {source} into {target}.\n{source}: {sentence} \n{target}:"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16
  )

message = [ { "role": "user", "content": text } ]
date_string = datetime.today().strftime('%Y-%m-%d')

prompt = tokenizer.apply_chat_template(
    message,
    tokenize=False,
    add_generation_prompt=True,
    date_string=date_string
)

inputs = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
input_length = inputs.shape[1]
outputs = model.generate(input_ids=inputs.to(model.device), 
                         max_new_tokens=400,
                         early_stopping=True,
                         num_beams=5)

print(tokenizer.decode(outputs[0, input_length:], skip_special_tokens=True))
# Ahir se'n va anar, va recollir les seves coses i es va fer a la mar. Una camisa, uns texans i una cançó, on anirà, on anirà. Es va acomiadar i va decidir batre's en duel amb el mar. I fer la volta al món en el seu veler. I navegar, nai-na-na, navegar
```

Using this template, each turn is preceded by a `<|im_start|>` delimiter and the role of the entity 
(either `user`, for content supplied by the user, or `assistant` for LLM responses), and finished with the `<|im_end|>` token.

#### General translation

For machine translation tasks, you can use the following prompt template:

```
Translate the following text from {source} into {target}.
{source}: {source sentence}
{target}:
```
<details>
<summary>Show an example</summary>

```python
source = 'Catalan'
target = 'Galician'
source_sentence = "Als antics egipcis del període de l'Imperi Nou els fascinaven els monuments dels seus predecessors, que llavors tenien més de mil anys."

text = f"Translate the following text from {source} into {target}.\n{source}: {source_sentence} \n{target}:"
# Os antigos exipcios do período do Imperio Novo estaban fascinados polos monumentos dos seus predecesores, que entón tiñan máis de mil anos de antigüidade.
```

</details>

### Post-editing

For post-editing tasks, you can use the following prompt template:

```
Please fix any mistakes in the following {source}-{target} machine translation or keep it unedited if it's correct.
Source: {source_sentence}
MT: {machine_translation}
Corrected:"
```

<details>
<summary>Show an example</summary>

```python
source = 'Catalan'
target = 'English'
source_sentence = 'Rafael Nadal i Maria Magdalena van inspirar a una generació sencera.'
machine_translation = 'Rafael Christmas and Maria the Muffin inspired an entire generation each in their own way.'

text = f"Please fix any mistakes in the following {source}-{target} machine translation or keep it unedited if it's correct.\nSource: {source_sentence} \nMT: {machine_translation} \nCorrected:"

# Rafael Nadal and Maria Magdalena inspired an entire generation.
```

</details>

### Document-level translation

For document-level translation tasks, you can use the following prompt template:

```
Please translate this text from {source} into {target}.
{source}: {1st paragraph of the document}
{2nd paragraph of the document}
{Nth paragraph of the document}
{target}:
```

<details>
<summary>Show an example</summary>
  
```python
source = 'English'
target = 'Asturian'

text = """Please translate this text from {} into {}.\n{}: President Donald Trump, who campaigned on promises to crack down on illegal immigration, has raised alarms in the U.S. dairy industry with his threat to impose 25% tariffs on Mexico and Canada by February 2025. This move is part of a broader strategy to declare a national emergency at the southern border to halt illegal migration completely.
However, the implications for the agriculture sector, particularly dairy, are significant. Approximately half of the U.S. dairy industry's workforce consists of immigrant labor, many of whom are undocumented. The National Milk Producers Federation estimates that removing immigrant workers could decimate the dairy herd by 2.1 million cows and slash milk production by nearly 50 billion pounds, leading to a dramatic 90.4% increase in milk prices.
The complex perspectives of Americans on undocumented workers were highlighted in a Pew Research Center study. While 64% of U.S. adults support legal pathways for undocumented immigrants, 35% oppose it—a gap that has been narrowing recently. Factors influencing public opinion include the belief that immigrants should have jobs and pass security checks, contrasted by concerns about lawbreakers being rewarded, fairness for legal migrants, and resource allocation.
According to Zach Rutledge, an agricultural economist at Michigan State University, as nations grow wealthier, their labor forces transition away from agriculture toward sectors like services and manufacturing. This shift has led to the U.S. relying heavily on immigrant labor for agricultural work. Domestic workers, even with employment taxes, may cost $15 to $25 an hour, while H-2A visa program workers might cost $25 to $30 an hour, accounting for additional housing expenses.
The National Milk Producers Federation has been vocal in advocating for changes to the H-2A visa program, which outside of its current seasonal limitations, does not support the dairy industry's year-round labor needs. Executive vice-president Jaime Castaneda reiterated the need for legislative clarity to address the undocumented workforce issues in dairy farming.
The Farm Workforce Modernization Act of 2023, which could grant legal status to certain undocumented farmworkers, has been stalled in Congress, despite acknowledgment of the sector's importance to feeding America. The need for coordinated legislative efforts to ensure both border security and labor market stability is imperative moving forward.
{}:""".format(source, target, source, target)
```

</details>

### Named-entity recognition

For named-entity recognition tasks, you can use the following prompt template:

```
Analyse the following tokenized text and mark the tokens containing named entities.
Use the following annotation guidelines with these tags for named entities:
- ORG (Refers to named groups or organizations)
- PER (Refers to individual people or named groups of people)
- LOC (Refers to physical places or natural landmarks)
- MISC (Refers to entities that don't fit into standard categories).
Prepend B- to the first token of a given entity and I- to the remaining ones if they exist.
If a token is not a named entity, label it as O.
Input: {list of words in a sentence}
Marked: 
```

<details>
<summary>Show an example</summary>
  
```python
text = """Analyse the following tokenized text and mark the tokens containing named entities.
Use the following annotation guidelines with these tags for named entities: 
- ORG (Refers to named groups or organizations)
- PER (Refers to individual people or named groups of people)
- LOC (Refers to physical places or natural landmarks)
- MISC (Refers to entities that don't fit into standard categories).
Prepend B- to the first token of a given entity and I- to the remaining ones if they exist.
If a token is not a named entity, label it as O.
Input: ['La', 'defensa', 'del', 'antiguo', 'responsable', 'de', 'la', 'RFEF', 'confirma', 'que', 'interpondrá', 'un', 'recurso.']
Marked: """

# [('La', 'O'), ('defensa', 'O'), ('del', 'O'), ('antiguo', 'O'), ('responsable', 'O'), ('de', 'O'), ('la', 'O'), ('RFEF', 'B-ORG'), ('confirma', 'O'), ('que', 'O'), ('interpondrá', 'O'), ('un', 'O'), ('recurso.', 'O')]
```
</details>


### Grammar checker

For fixing any mistakes in grammar, you can use the following prompt template:

```
Please fix any mistakes in the following {source} sentence or keep it unedited if it's correct.
Sentence: {sentence}
Corrected:
```

<details>
<summary>Show an example</summary>

```python
source = 'Catalan'
sentence = 'Entonses, el meu jefe m’ha dit que he de treballar els fins de setmana.'

text = f"Please fix any mistakes in the following {source} sentence or keep it unedited if it's correct.\nSentence: {sentence} \nCorrected:"

# Llavors, el meu cap m'ha dit que he de treballar els caps de setmana.
```
</details>


## Data

### Pretraining Data

The pretraining corpus consists of 424 billion tokens of Catalan-centric, Spanish-centric, and English-centric parallel data, 
including all of the official European languages plus Catalan, Basque, Galician, Asturian, Aragonese and Aranese. 
It amounts to 6,574,251,526 parallel sentence pairs. 

This highly multilingual corpus is predominantly composed of data sourced from [OPUS](https://opus.nlpl.eu/), 
with additional data taken from the [NTEU Project](https://nteu.eu/), [Aina Project](https://projecteaina.cat/), and other sources 
(see: [Data Sources](#pre-data-sources) and [References](#pre-references)). 
Where little parallel Catalan <-> xx data could be found, synthetic Catalan data was generated from the Spanish side of the collected Spanish <-> xx corpora using 
[Projecte Aina’s Spanish-Catalan model](https://huggingface.co/projecte-aina/aina-translator-es-ca). The final distribution of languages was as below:

![](./images/treemap.png)

Click the expand button below to see the full list of corpora included in the training data.

<details id="pre-data-sources">
<summary>Data Sources</summary>
 
| Dataset                                   	| Ca-xx Languages                                                                                                	|  Es-xx Langugages                             | En-xx Languages |
|-----------------------------------------------|----------------------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------|
|[AINA](https://huggingface.co/collections/projecte-aina/mt-datasets-655f33d9f4be8787c8e7486b) | en     |       |       |
|ARANESE-SYNTH-CORPUS-BSC                         | arn   |      |         |
|BOUA-SYNTH-BSC             |     | val |        |
|[BOUMH](https://github.com/transducens/PILAR/tree/main/valencian/BOUMH) |          | val   |           |
|[BOUA-PILAR](https://github.com/transducens/PILAR/tree/main/valencian/BOUA)  |          | val |       |
|[CCMatrix](https://opus.nlpl.eu/CCMatrix/corpus/version/CCMatrix)		|eu			|		| ga | 
|[DGT](https://opus.nlpl.eu/DGT/corpus/version/DGT)			|			|bg,cs,da,de,el	,et,fi,fr,ga,hr,hu,lt,lv,mt,nl,pl,pt,ro,sk,sl,sv	|    da,et,ga,hr,hu,lt,lv,mt,sh,sl|
|DOGV-SYNTH-BSC                 |      |  val    |         |
|[DOGV-PILAR](https://github.com/transducens/PILAR/tree/main/valencian/DOGV-html) |           | val |            | 
|[ELRC-EMEA](https://opus.nlpl.eu/ELRC-EMEA/corpus/version/ELRC-EMEA)		|			|bg,cs,da,hu,lt,lv,mt,pl,ro,sk,sl		| et,hr,lv,ro,sk,sl |
|[EMEA](https://opus.nlpl.eu/EMEA/corpus/version/EMEA)			|			|bg,cs,da,el,fi,hu,lt,mt,nl,pl,ro,sk,sl,sv		|    et,mt  |
|[EUBookshop](https://opus.nlpl.eu/EUbookshop/corpus/version/EUbookshop)		|lt,pl,pt			|cs,da,de,el,fi,fr,ga,it,lv,mt,nl,pl,pt,ro,sk,sl,sv		|cy,ga|
|[Europarl](https://opus.nlpl.eu/Europarl/corpus/version/Europarl)		|			|bg,cs,da,el,en,fi,fr,hu,lt,lv,nl,pl,pt	,ro,sk,sl,sv	| |
|[Europat](https://opus.nlpl.eu/EuroPat/corpus/version/EuroPat)		|			|en,hr		| no  |
|[GAITU Corpus](https://gaitu.eus/) | | | eu|
|[KDE4](https://opus.nlpl.eu/KDE4/corpus/version/KDE4)			|bg,cs,da,de,el	,et,eu,fi,fr,ga,gl,hr,it,lt,lv,nl,pl,pt,ro,sk,sl,sv	|bg,ga,hr	|cy,ga,nn,oc |
|[GlobalVoices](https://opus.nlpl.eu/GlobalVoices/corpus/version/GlobalVoices)		| bg,de,fr,it,nl,pl,pt	|bg,de,fr,pt		|  |
|[GNOME](https://opus.nlpl.eu/GNOME/corpus/version/GNOME)		|eu,fr,ga,gl,pt		|ga		|cy,ga,nn|  
|[JRC-Arquis](https://opus.nlpl.eu/JRC-Acquis/corpus/version/JRC-Acquis)		|			|cs,da,et,fr,lt,lv,mt,nl,pl	,ro,sv|	 et  |
|LES-CORTS-VALENCIANES-SYNTH-BSC  |            | val            |           |
|[MaCoCu](https://opus.nlpl.eu/MaCoCu/corpus/version/MaCoCu)                    | en     |     | hr,mt,uk   |
|[MultiCCAligned](https://opus.nlpl.eu/JRC-Acquis/corpus/version/JRC-Acquis)	|bg,cs,de,el,et,fi,fr,hr,hu,it,lt,lv,nl,pl,ro,sk,sv	|bg,fi,fr,hr,it,lv,nl,pt		|bg,cy,da,et,fi,hr,hu,lt,lv,no,sl,sr,uk|
|[MultiHPLT](https://opus.nlpl.eu/MultiHPLT/corpus/version/MultiHPLT)		|en, et,fi,ga,hr,mt		|		|fi,ga,gl,hr,mt,nn,sr |
|[MultiParaCrawl](https://opus.nlpl.eu/MultiParaCrawl/corpus/version/MultiParaCrawl)	|bg,da		|de,en,fr,ga,hr,hu,it,mt,pt		|bg,cs,da,de,el,et,fi,fr,ga,hr,hu,lt,lv,mt,nn,pl,ro,sk,sl,uk|
|[MultiUN](https://opus.nlpl.eu/MultiUN/corpus/version/MultiUN)		|			|fr	|	|	
|[News-Commentary](https://opus.nlpl.eu/News-Commentary/corpus/version/News-Commentary) 	|		|fr		|  |
|[NLLB](https://opus.nlpl.eu/NLLB/corpus/version/NLLB)			|bg,da,el,en,et,fi,fr,gl,hu,it	,lt,lv,pt,ro,sk,sl	|bg,cs,da,de,el	,et,fi,fr,hu,it,lt,lv,nl,pl,pt	,ro,sk,sl,sv| bg,cs,cy,da,de,el,et,fi,fr,ga,hr,hu,it,lt,lv,mt,nl,no,oc,pl,pt,ro,ru,sk,sl,sr,sv,uk|
|[NÓS Authentic Corpus](https://zenodo.org/records/7675110)                 |               |               |    gl      |
|[NÓS Synthetic Corpus](https://zenodo.org/records/7685180)            |                |               |   gl       |
|[NTEU](https://www.elrc-share.eu/repository/search/?q=NTEU)			|			|bg,cs,da,de,el,en,et,fi,fr,ga,hr,hu,it,lt,lv,mt,nl,pl,pt,ro,sk,sl,sv	|        da,et,ga,hr,lt,lv,mt,ro,sk,sl,sv     |	 
|[OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles/corpus/version/OpenSubtitles) 	|bg,cs,da,de,el	,et,eu,fi,gl,hr,hu,lt,lv,nl,pl,pt,ro,sk,sl,sv	|da,de,fi,fr,hr,hu,it,lv,nl		| bg,cs,de,el,et,hr,fi,fr,hr,hu,no,sl,sr|
|[OPUS-100](https://opus.nlpl.eu/opus-100.php)   | en |  | gl |
|[StanfordNLP-NMT](https://opus.nlpl.eu/StanfordNLP-NMT/corpus/version/StanfordNLP-NMT) | | |cs |
|[Tatoeba](https://opus.nlpl.eu/Tatoeba/corpus/version/Tatoeba)		|de,pt			|pt		|   |
|[TildeModel](https://opus.nlpl.eu/TildeMODEL/corpus/version/TildeMODEL)		|			|bg		| et,hr,lt,lv,mt |
|[UNPC](https://opus.nlpl.eu/UNPC/corpus/version/UNPC)			|			|en,fr		| ru  |	
|[PILAR-VALENCIAN-AUTH](https://github.com/transducens/PILAR/tree/main/valencian/Generalitat)  |          |    val     |          |
|[PILAR-VALENCIAN-SYNTH](https://github.com/transducens/PILAR/tree/main/valencian/Generalitat)  |      | val |     |
|[WikiMatrix](https://opus.nlpl.eu/WikiMatrix/corpus/version/WikiMatrix)		|bg,cs,da,de,el	,et,eu,fi,fr,gl,hr,hu,it,lt,nl,pl,pt,ro,sk,sl,sv	|bg,en,fr,hr,it,pt		| oc,sh |
|[Wikimedia](https://opus.nlpl.eu/wikimedia/corpus/version/wikimedia) | | |cy,nn |
|[XLENT](https://opus.nlpl.eu/XLEnt/corpus/version/XLEnt)		|eu,ga,gl			|ga		|cy,et,ga,gl,hr,oc,sh|


Datasets with "-BSC" in their names (e.g., BOUA-SYNTH-BSC, DOGV-SYNTH-BSC) are synthetic datasets obtained by machine translating 
pre-existing monolingual corpora with our own seq-to-seq models. These datasets were generated internally for model training and are not published.

To consult the data summary document with the respective licences, please send an e-mail to ipr@bsc.es. 



</details>



<details id="pre-references">
<summary>References</summary>

- Aulamo, M., Sulubacak, U., Virpioja, S., & Tiedemann, J. (2020). OpusTools and Parallel Corpus Diagnostics. In N. Calzolari, F. Béchet, P. Blache, K. Choukri, C. Cieri, T. Declerck, S. Goggi, H. Isahara, B. Maegaard, J. Mariani, H. Mazo, A. Moreno, J. Odijk, & S. Piperidis (Eds.), Proceedings of the Twelfth Language Resources and Evaluation Conference (pp. 3782–3789). European Language Resources Association. https://aclanthology.org/2020.lrec-1.467
- Chaudhary, V., Tang, Y., Guzmán, F., Schwenk, H., & Koehn, P. (2019). Low-Resource Corpus Filtering Using Multilingual Sentence Embeddings. In O. Bojar, R. Chatterjee, C. Federmann, M. Fishel, Y. Graham, B. Haddow, M. Huck, A. J. Yepes, P. Koehn, A. Martins, C. Monz, M. Negri, A. Névéol, M. Neves, M. Post, M. Turchi, & K. Verspoor (Eds.), Proceedings of the Fourth Conference on Machine Translation (Volume 3: Shared Task Papers, Day 2) (pp. 261–266). Association for Computational Linguistics. https://doi.org/10.18653/v1/W19-5435
- DGT-Translation Memory—European Commission. (n.d.). Retrieved November 4, 2024, from https://joint-research-centre.ec.europa.eu/language-technology-resources/dgt-translation-memory_en
- Eisele, A., & Chen, Y. (2010). MultiUN: A Multilingual Corpus from United Nation Documents. In N. Calzolari, K. Choukri, B. Maegaard, J. Mariani, J. Odijk, S. Piperidis, M. Rosner, & D. Tapias (Eds.), Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC’10). European Language Resources Association (ELRA). http://www.lrec-conf.org/proceedings/lrec2010/pdf/686_Paper.pdf
- El-Kishky, A., Chaudhary, V., Guzmán, F., & Koehn, P. (2020). CCAligned: A Massive Collection of Cross-Lingual Web-Document Pairs. Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), 5960–5969. https://doi.org/10.18653/v1/2020.emnlp-main.480
- El-Kishky, A., Renduchintala, A., Cross, J., Guzmán, F., & Koehn, P. (2021). XLEnt: Mining a Large Cross-lingual Entity Dataset with Lexical-Semantic-Phonetic Word Alignment. Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, 10424–10430. https://doi.org/10.18653/v1/2021.emnlp-main.814
- Fan, A., Bhosale, S., Schwenk, H., Ma, Z., El-Kishky, A., Goyal, S., Baines, M., Celebi, O., Wenzek, G., Chaudhary, V., Goyal, N., Birch, T., Liptchinsky, V., Edunov, S., Grave, E., Auli, M., & Joulin, A. (2020). Beyond English-Centric Multilingual Machine Translation (No. arXiv:2010.11125). arXiv. https://doi.org/10.48550/arXiv.2010.11125
- García-Martínez, M., Bié, L., Cerdà, A., Estela, A., Herranz, M., Krišlauks, R., Melero, M., O’Dowd, T., O’Gorman, S., Pinnis, M., Stafanovič, A., Superbo, R., & Vasiļevskis, A. (2021). Neural Translation for European Union (NTEU). 316–334. https://aclanthology.org/2021.mtsummit-up.23
- Gibert, O. de, Nail, G., Arefyev, N., Bañón, M., Linde, J. van der, Ji, S., Zaragoza-Bernabeu, J., Aulamo, M., Ramírez-Sánchez, G., Kutuzov, A., Pyysalo, S., Oepen, S., & Tiedemann, J. (2024). A New Massive Multilingual Dataset for High-Performance Language Technologies (No. arXiv:2403.14009). arXiv. http://arxiv.org/abs/2403.14009
- Koehn, P. (2005). Europarl: A Parallel Corpus for Statistical Machine Translation. Proceedings of Machine Translation Summit X: Papers, 79–86. https://aclanthology.org/2005.mtsummit-papers.11
- Kreutzer, J., Caswell, I., Wang, L., Wahab, A., Van Esch, D., Ulzii-Orshikh, N., Tapo, A., Subramani, N., Sokolov, A., Sikasote, C., Setyawan, M., Sarin, S., Samb, S., Sagot, B., Rivera, C., Rios, A., Papadimitriou, I., Osei, S., Suarez, P. O., … Adeyemi, M. (2022). Quality at a Glance: An Audit of Web-Crawled Multilingual Datasets. Transactions of the Association for Computational Linguistics, 10, 50–72. https://doi.org/10.1162/tacl_a_00447
- Rozis, R.,Skadiņš, R (2017). Tilde MODEL - Multilingual Open Data for EU Languages. https://aclanthology.org/W17-0235
- Schwenk, H., Chaudhary, V., Sun, S., Gong, H., & Guzmán, F. (2019). WikiMatrix: Mining 135M Parallel Sentences in 1620 Language Pairs from Wikipedia (No. arXiv:1907.05791). arXiv. https://doi.org/10.48550/arXiv.1907.05791
- Schwenk, H., Wenzek, G., Edunov, S., Grave, E., & Joulin, A. (2020). CCMatrix: Mining Billions of High-Quality Parallel Sentences on the WEB (No. arXiv:1911.04944). arXiv. https://doi.org/10.48550/arXiv.1911.04944
- Steinberger, R., Pouliquen, B., Widiger, A., Ignat, C., Erjavec, T., Tufiş, D., & Varga, D. (n.d.). The JRC-Acquis: A Multilingual Aligned Parallel Corpus with 20+ Languages. http://www.lrec-conf.org/proceedings/lrec2006/pdf/340_pdf
- Subramani, N., Luccioni, S., Dodge, J., & Mitchell, M. (2023). Detecting Personal Information in Training Corpora: An Analysis. In A. Ovalle, K.-W. Chang, N. Mehrabi, Y. Pruksachatkun, A. Galystan, J. Dhamala, A. Verma, T. Cao, A. Kumar, & R. Gupta (Eds.), Proceedings of the 3rd Workshop on Trustworthy Natural Language Processing (TrustNLP 2023) (pp. 208–220). Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.trustnlp-1.18
- Tiedemann, J. (23-25). Parallel Data, Tools and Interfaces in OPUS. In N. C. (Conference Chair), K. Choukri, T. Declerck, M. U. Doğan, B. Maegaard, J. Mariani, A. Moreno, J. Odijk, & S. Piperidis (Eds.), Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC’12). European Language Resources Association (ELRA). http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper
- Ziemski, M., Junczys-Dowmunt, M., & Pouliquen, B. (n.d.). The United Nations Parallel Corpus v1.0. https://aclanthology.org/L16-1561



</details>


### Instruction Tuning Data

This model has been fine-tuned on ~135k instructions, primarily targeting machine translation performance for Catalan, English, and Spanish. 
Additional instruction data for other European and closely related Iberian languages was also included, as it yielded a positive impact on the languages of interest. 
That said, the performance in these additional languages is not guaranteed due to the limited amount of available data and the lack of resources for thorough testing.

A portion of our fine-tuning data comes directly from, or is sampled from [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2). 
We also created additional datasets for our main languages of interest. 
While tasks relating to machine translation are included, it’s important to note that no chat data was used in the fine-tuning process.
The final distribution of tasks was as below:

![](./images/chart.png)


Click the expand button below to see the full list of tasks included in the finetuning data.

<details id="instr-data-sources">
<summary>Data Sources</summary>



| Task                             | Source                                                                                   | Languages                                                      | Count  |
|----------------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------|
| Multi-reference Translation      | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [Tatoeba Dev (filtered)](https://github.com/Helsinki-NLP/Tatoeba-Challenge)                      | mixed                                                          | 10000  |
| Paraphrase 		           | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [PAWS-X Dev](https://github.com/google-research-datasets/paws)                     | mixed                                                          | 3521   |
| Named-entity Recognition         | [AnCora-Ca-NER](https://huggingface.co/datasets/projecte-aina/ancora-ca-ner)                | ca                                                             | 12059  |
| Named-entity Recognition         | [BasqueGLUE](https://huggingface.co/datasets/orai-nlp/basqueGLUE), [EusIE](https://huggingface.co/datasets/HiTZ/EusIE) | eu                                                             | 4304   |
| Named-entity Recognition         | [SLI NERC Galician Gold Corpus](https://github.com/xavier-gz/SLI_Galician_Corpora)          | gl                                                             | 6483   |
| Named-entity Recognition         | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MultiCoNER 2022 and 2023 Dev](https://registry.opendata.aws/multiconer/)                     | pt                                                             | 854    |
| Named-entity Recognition         | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MultiCoNER 2022 and 2023 Dev](https://registry.opendata.aws/multiconer/)                     | nl                                                             | 800    |
| Named-entity Recognition         | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MultiCoNER 2022 and 2023 Dev](https://registry.opendata.aws/multiconer/)                     | es                                                             | 1654   |
| Named-entity Recognition         | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MultiCoNER 2022 and 2023 Dev](https://registry.opendata.aws/multiconer/)                     | en                                                             | 1671   |
| Named-entity Recognition         | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MultiCoNER 2022 and 2023 Dev](https://registry.opendata.aws/multiconer/)                     | ru                                                             | 800    |
| Named-entity Recognition         | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MultiCoNER 2022 and 2023 Dev](https://registry.opendata.aws/multiconer/)                     | it                                                             | 858    |
| Named-entity Recognition         | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MultiCoNER 2022 and 2023 Dev](https://registry.opendata.aws/multiconer/)                     | fr                                                             | 857    |
| Named-entity Recognition         | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MultiCoNER 2022 and 2023 Dev](https://registry.opendata.aws/multiconer/)                     | de                                                             | 1312   |
| Terminology-aware Translation    | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [WMT21 Terminology Dev (filtered)](https://www.statmt.org/wmt21/terminology-task.html)                     | en-ru                                                          | 50     |
| Terminology-aware Translation    | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [WMT21 Terminology Dev (filtered)](https://www.statmt.org/wmt21/terminology-task.html)                     | en-fr                                                          | 29     |
| Automatic Post Editing           | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [QT21](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2390), [ApeQuest](https://apequest.wordpress.com/)                     | en-fr                                                          | 6133   |
| Automatic Post Editing           | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [QT21](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2390), [ApeQuest](https://apequest.wordpress.com/)                     | en-nl                                                          | 9077   |
| Automatic Post Editing           | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [QT21](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2390), [ApeQuest](https://apequest.wordpress.com/)                     | en-pt                                                          | 5762   |
| Automatic Post Editing           | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [QT21](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2390), [ApeQuest](https://apequest.wordpress.com/)                     | de-en                                                          | 10000  |
| Automatic Post Editing           | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [QT21](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2390), [ApeQuest](https://apequest.wordpress.com/)                     | en-de                                                          | 10000  |
| Machine Translation Evaluation   | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2)-sample: [WMT20 to WMT22 Metrics MQM](https://www.statmt.org/wmt22/results.html), [WMT17 to WMT22 Metrics Direct Assessments](https://www.statmt.org/wmt22/results.html)                                                                       | en-ru, en-pl, ru-en, en-de, en-ru, de-fr, de-en, en-de             | 353    |
| Machine Translation Evaluation   | Non-public                                                                                     | four pivot languages (eu, es, ca, gl) paired with European languages (bg, cs, da, de, el, en, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv)                                   | 9700   |
| General Machine Translation      | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [WMT14 to WMT21](https://www.statmt.org/wmt22/results.html), [NTREX](https://github.com/MicrosoftTranslator/NTREX), [Flores Dev](https://github.com/facebookresearch/flores), [FRMT](https://github.com/google-research/google-research/tree/master/frmt), [QT21](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2390), [ApeQuest](https://apequest.wordpress.com/), [OPUS (Quality Filtered)](https://opus.nlpl.eu/), [MT-GenEval](https://github.com/amazon-science/machine-translation-gender-eval)                     | nl-en, en-ru, it-en, fr-en, es-en, en-fr, ru-en, fr-de, en-nl, de-fr  | 500    |
| General Machine Translation      | Non-public                                                                                    | three pivot languages (es, ca, en) paired with European languages (ast, arn, arg, bg, cs, cy, da, de, el, et, fi, ga, gl, hr, it, lt, lv, mt, nb, nn, nl, oc, pl, pt, ro, ru, sk, sl, sr, sv, uk, eu)                                    | 9350   |
| Fill-in-the-Blank                | Non-public                                                                                     | five pivot languages (ca, es, eu, gl, en) paired with European languages (cs, da, de, el, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv)                                     | 11500  |
| Document-level Translation       | Non-public                                                                                      | two pivot languages (es, en) paired with European languages (bg, cs, da, de, el, et, fi, fr, hu, it, lt, lv, nl, pl, pt, ro, ru, sk, sv)                                                             | 7600   |
| Paragraph-level Translation      | Non-public                                                                                      | two pivot languages (es, en) paired with European languages (bg, cs, da, de, el, et, fi, fr, hu, it, lt, lv, nl, pl, pt, ro, ru, sk, sv)                                                              | 7600   |
| Context-Aware Translation   | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MT-GenEval](https://github.com/amazon-science/machine-translation-gender-eval)                     | en-it                                                          | 348    |
| Context-Aware Translation   | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MT-GenEval](https://github.com/amazon-science/machine-translation-gender-eval)                     | en-ru                                                          | 454    |
| Context-Aware Translation   | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MT-GenEval](https://github.com/amazon-science/machine-translation-gender-eval)                     | en-fr                                                          | 369    |
| Context-Aware Translation   | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MT-GenEval](https://github.com/amazon-science/machine-translation-gender-eval)                     | en-nl                                                          | 417    |
| Context-Aware Translation   | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MT-GenEval](https://github.com/amazon-science/machine-translation-gender-eval)                     | en-es                                                          | 431    |
| Context-Aware Translation   | [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.2): [MT-GenEval](https://github.com/amazon-science/machine-translation-gender-eval)                     | en-de                                                          | 558    |
|**Total**                  |                    |          |     **135,404**       |

The non-public portion of this dataset was jointly created by the [ILENIA](https://proyectoilenia.es/) partners: BSC-LT, [HiTZ](http://hitz.ehu.eus/es), 
and [CiTIUS](https://citius.gal/es/). For further information regarding the instruction-tuning data, 
please contact <langtech@bsc.es>.

</details>

<details id="instr-references">
<summary>References</summary>

- Alves, D. M., Pombal, J., Guerreiro, N. M., Martins, P. H., Alves, J., Farajian, A., Peters, B., Rei, R., Fernandes, P., Agrawal, S., Colombo, P., de Souza, J. G. C., & Martins, A. F. T. (2024). Tower: An open multilingual large language model for translation-related tasks (No. arXiv: 2402.17733). arXiv. https://arxiv.org/abs/2402.17733
- Armengol-Estapé, J., Carrino, C. P., Rodriguez-Penagos, C., de Gibert Bonet, O., Armentano-Oller, C., Gonzalez-Agirre, A., Melero, M., & Villegas, M. (2021). Are multilingual models the best choice for moderately under-resourced languages? A comprehensive assessment for Catalan. Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021, 4933–4946. Association for Computational Linguistics. https://doi.org/10.18653/v1/2021.findings-acl.437
- Currey, A., Nadejde, M., Pappagari, R. R., Mayer, M., Lauly, S., Niu, X., Hsu, B., & Dinu, G. (2022). MT-GenEval: A counterfactual and contextual dataset for evaluating gender accuracy in machine translation. In Y. Goldberg, Z. Kozareva, & Y. Zhang (Eds.), Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (pp. 4287–4299). Association for Computational Linguistics. https://doi.org/10.18653/v1/2022.emnlp-main.288
- Federmann, C., Kocmi, T., & Xin, Y. (2022). NTREX-128 – News test references for MT evaluation of 128 languages. Proceedings of the First Workshop on Scaling Up Multilingual Evaluation, 21–24. Association for Computational Linguistics. https://aclanthology.org/2022.sumeval-1.4
- Ive, J., Specia, L., Szoc, S., Vanallemeersch, T., Van den Bogaert, J., Farah, E., Maroti, C., Ventura, A., & Khalilov, M. (2020). A post-editing dataset in the legal domain: Do we underestimate neural machine translation quality? In N. Calzolari, F. Béchet, P. Blache, K. Choukri, C. Cieri, T. Declerck, S. Goggi, H. Isahara, B. Maegaard, J. Mariani, H. Mazo, A. Moreno, J. Odijk, & S. Piperidis (Eds.), Proceedings of the Twelfth Language Resources and Evaluation Conference (pp. 3692–3697). European Language Resources Association. https://aclanthology.org/2020.lrec-1.455/
- Malmasi, S., Fang, A., Fetahu, B., Kar, S., & Rokhlenko, O. (2022). MultiCoNER: A large-scale multilingual dataset for complex named entity recognition. Proceedings of the 29th International Conference on Computational Linguistics, 3798–3809. International Committee on Computational Linguistics. https://aclanthology.org/2022.coling-1.334/
- NLLB Team, Costa-jussà, M. R., Cross, J., Çelebi, O., Elbayad, M., Heafield, K., Heffernan, K., Kalbassi, E., Lam, J., Licht, D., Maillard, J., Sun, A., Wang, S., Wenzek, G., Youngblood, A., Akula, B., Barrault, L., Mejia Gonzalez, G., Hansanti, P., Hoffman, J., Jarrett, S., Sadagopan, K. R., Rowe, D., Spruit, S., Tran, C., Andrews, P., Ayan, N. F., Bhosale, S., Edunov, S., Fan, A., Gao, C., Goswami, V., Guzmán, F., Koehn, P., Mourachko, A., Ropers, C., Saleem, S., Schwenk, H., & Wang, J. (2022). No language left behind: Scaling human-centered machine translation (No. arXiv: 2207.04672). arXiv. https://arxiv.org/abs/2207.04672
- Riley, P., Dozat, T., Botha, J. A., Garcia, X., Garrette, D., Riesa, J., Firat, O., & Constant, N. (2022). FRMT: A benchmark for few-shot region-aware machine translation (No. arXiv: 2210.00193). arXiv. https://doi.org/10.48550/ARXIV.2210.00193
- Specia, L., Harris, K., Blain, F., Burchardt, A., Macketanz, V., Skadiņa, I., Negri, M., & Turchi, M. (2017). Translation quality and productivity: A study on rich morphology languages. Proceedings of Machine Translation Summit XVI, 55–71. Nagoya, Japan.
- Tiedemann, J. (2020). The Tatoeba translation challenge – Realistic data sets for low-resource and multilingual MT. Proceedings of the Fifth Conference on Machine Translation, 1174–1182. Association for Computational Linguistics. https://www.aclweb.org/anthology/2020.wmt-1.139
- Urbizu, G., San Vicente, I., Saralegi, X., Agerri, R., & Soroa, A. (2022). BasqueGLUE: A natural language understanding benchmark for Basque. Proceedings of the Language Resources and Evaluation Conference, 1603–1612. European Language Resources Association. https://aclanthology.org/2022.lrec-1.172
- Yang, Y., Zhang, Y., Tar, C., & Baldridge, J. (2019). PAWS-X: A cross-lingual adversarial dataset for paraphrase identification. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) (pp. 3687–3692). Association for Computational Linguistics. https://doi.org/10.18653/v1/D19-1382
- Zubillaga, M., Sainz, O., Estarrona, A., Lopez de Lacalle, O., & Agirre, E. (2024). Event extraction in Basque: Typologically motivated cross-lingual transfer-learning analysis (No. arXiv: 2404.06392). arXiv. https://arxiv.org/abs/2404.06392



</details>

## Evaluation

Below are the evaluation results on the [Flores+200 devtest set](https://huggingface.co/datasets/openlanguagedata/flores_plus), 
compared against the state-of-the-art [MADLAD400-7B-mt model](https://huggingface.co/google/madlad400-7b-mt) ([Kudugunta, S., et al.](https://arxiv.org/abs/2309.04662)) and SalamandraTA-7b-base model. 
These results cover the translation directions CA-XX, ES-XX, EN-XX, as well as XX-CA, XX-ES, and XX-EN. 
The metrics have been computed excluding Asturian, Aranese, and Aragonese, as we report them separately. 
The evaluation was conducted using [MT-Lens](https://github.com/langtech-bsc/mt-evaluation), following the standard setting (beam search with beam size 5, limiting the translation length to 500 tokens). We report the following metrics:

<details>
<summary>Click to show metrics details</summary>

- `BLEU`: Sacrebleu implementation. Signature: nrefs:1— case:mixed— eff:no— tok:13a— smooth:exp—version:2.3.1
- `TER`: Sacrebleu implementation.
- `ChrF`: Sacrebleu implementation.
- `Comet`: Model checkpoint: "Unbabel/wmt22-comet-da".
- `Comet-kiwi`: Model checkpoint: "Unbabel/wmt22-cometkiwi-da".
- `Bleurt`: Model checkpoint: "lucadiliello/BLEURT-20".
- `MetricX`: Model checkpoint: "google/metricx-23-xl-v2p0".
- `MetricX-QE`: Model checkpoint: "google/metricx-23-qe-xl-v2p0".

</details>


<details>
<summary>English evaluation</summary>
  
### English

This section presents the evaluation metrics for English translation tasks.


|                       |   Bleu↑ |   Ter↓ |   ChrF↑ |   Comet↑ |   Comet-kiwi↑ |   Bleurt↑ |   MetricX↓ |   MetricX-QE↓ |
|:---------------------------------|-------:|------:|-------:|--------:|-------------:|---------:|----------:|-------------:|
| **EN-XX** | | | | | | | | |
| SalamandraTA-7b-instruct | 35.20     | 53.40     | 61.58     | **0.89** | **0.86**     | 0.78     | **0.96**  | **0.81**     |
| MADLAD400-7B             | **35.73** | **51.87** | **63.46** | 0.88     | 0.85         | **0.79** | 1.16      | 1.10         |
| SalamandraTA-7b-base     | 34.99     | 52.64     | 62.58     | 0.87     | 0.84         | 0.77     | 1.45      | 1.23         |
| **XX-EN** | | | | | | | | |
| SalamandraTA-7b-instruct | **44.37** | **42.49** | 68.29     | **0.89** | **0.86**     | **0.80** | **1.05**  | **0.99**     |
| MADLAD400-7B             | 43.20     | 43.33     | 67.98     | **0.89** | **0.86**     | **0.80** | 1.13      | 1.15         |
| SalamandraTA-7b-base     | 44.12     | 43.00     | **68.43** | **0.89** | 0.85         | **0.80** | 1.13      | 1.22         |





<img src="./images/bleu_en.png" alt="English" width="100%"/>

</details>

<details>
<summary>Spanish evaluation</summary>
  
### Spanish

This section presents the evaluation metrics for Spanish translation tasks.


|                       |   Bleu↑ |   Ter↓ |   ChrF↑ |   Comet↑ |   Comet-kiwi↑ |   Bleurt↑ |   MetricX↓ |   MetricX-QE↓ |
|:---------------------------------|-------:|------:|-------:|--------:|-------------:|---------:|----------:|-------------:|
| **ES-XX** | | | | | | | | |
| SalamandraTA-7b-instruct | **23.68** | **67.31** | **53.98** | **0.87** | **0.83**     | **0.76** | **0.93**  | **0.80**     |
| MADLAD400-7B             | 22.48     | 68.91     | 53.93     | 0.86     | **0.83**     | 0.75     | 1.09      | 1.14         |
| SalamandraTA-7b-base     | 21.63     | 70.08     | 52.98     | 0.86     | **0.83**     | 0.74     | 1.24      | 1.12         |
| **XX-ES** | | | | | | | | |
| SalamandraTA-7b-instruct | **26.40** | 62.27     | **53.54** | **0.85** | **0.84**     | **0.74** | **0.80**  | **1.07**     |
| MADLAD400-7B             | 24.85     | **61.82** | 53.00     | **0.85** | **0.84**     | **0.74** | 1.05      | 1.50         |
| SalamandraTA-7b-base     | 24.71     | 62.33     | 52.96     | **0.85** | **0.84**     | 0.73     | 1.06      | 1.37         |



<img src="./images/bleu_es.png" alt="English" width="100%"/>

<img src="./images/es_xx_bars.png" alt="ESXX" width="100%"/>

</details>

<details>
<summary>Catalan evaluation</summary>
  
### Catalan

This section presents the evaluation metrics for Catalan translation tasks.


|                       |   Bleu↑ |   Ter↓ |   ChrF↑ |   Comet↑ |   Comet-kiwi↑ |   Bleurt↑ |   MetricX↓ |   MetricX-QE↓ |
|:---------------------------------|-------:|------:|-------:|--------:|-------------:|---------:|----------:|-------------:|
| **CA-XX** | | | | | | | | |
| SalamandraTA-7b-instruct | **29.50** | 59.26     | 58.21     | **0.88** | **0.81**     | **0.77** | **0.97**  | **0.98**     |
| MADLAD400-7B             | 29.37     | **59.01** | **58.47** | 0.87     | **0.81**     | **0.77** | 1.08      | 1.31         |
| SalamandraTA-7b-base     | 29.06     | 59.32     | 58.00     | 0.87     | **0.81**     | 0.76     | 1.23      | 1.28         |
| **XX-CA** | | | | | | | | |
| SalamandraTA-7b-instruct | **34.51** | **54.21** | **60.10** | **0.86** | **0.81**     | **0.76** | **0.90**  | **1.29**     |
| MADLAD400-7B             | 33.02     | 55.01     | 59.38     | **0.86** | **0.81**     | 0.75     | 1.18      | 1.79         |
| SalamandraTA-7b-base     | 32.75     | 55.78     | 59.42     | **0.86** | **0.81**     | 0.75     | 1.17      | 1.63         |



<img src="./images/bleu_ca.png" alt="English" width="100%"/>

</details>

<details>
<summary>Galician evaluation</summary>

### Galician

This section presents the evaluation metrics for Galician translation tasks.


|                        |   Bleu↑ |   Ter↓ |   ChrF↑ |   Comet↑ |   Comet-kiwi↑ |   Bleurt↑ |   MetricX↓ |   MetricX-QE↓ |
|:---------------------------------|-------:|------:|-------:|--------:|-------------:|---------:|----------:|-------------:|
| **GL-XX** | | | | | | | | |
| SalamandraTA-7b-instruct | **36.95** | **50.12** | **62.55** | **0.88** | **0.85**     | **0.77** | **0.86**  | **0.98**     |
| MADLAD400-7B             | 26.43     | 64.30     | 55.99     | 0.86     | **0.85**     | 0.76     | 1.35      | 2.06         |
| SalamandraTA-7b-base     | 27.47     | 61.39     | 56.96     | 0.87     | 0.82         | 0.76     | 1.23      | 1.29         |
| **XX-GL** | | | | | | | | |
| SalamandraTA-7b-instruct | **34.37** | **52.49** | **60.99** | **0.88** | **0.85**     | **0.73** | **0.75**  | **0.92**     |
| MADLAD400-7B             | 27.77     | 59.46     | 54.92     | 0.84     | **0.85**     | 0.67     | 1.42      | 2.72         |
| SalamandraTA-7b-base     | 28.22     | 59.52     | 56.28     | 0.85     | 0.82         | 0.69     | 1.27      | 1.78         |

<img src="./images/bleu_gl.png" alt="English" width="100%"/>

</details>

<details>
<summary>Basque evaluation</summary>
  
### Basque

This section presents the evaluation metrics for Basque translation tasks.



|                        |   Bleu↑ |   Ter↓ |   ChrF↑ |   Comet↑ |   Comet-kiwi↑ |   Bleurt↑ |   MetricX↓ |   MetricX-QE↓ |
|:---------------------------------|-------:|------:|-------:|--------:|-------------:|---------:|----------:|-------------:|
| **EU-XX** | | | | | | | | |
| SalamandraTA-7b-instruct | **29.89** | **58.54** | **56.66** | **0.87** | **0.85**     | **0.76** | **0.90**  | **0.89**     |
| MADLAD400-7B             | 21.26     | 69.75     | 49.80     | 0.85     | 0.82         | 0.72     | 1.54      | 2.71         |
| SalamandraTA-7b-base     | 22.87     | 67.38     | 52.19     | 0.86     | 0.79         | 0.74     | 1.19      | 1.61         |
| **XX-EU** | | | | | | | | |
| SalamandraTA-7b-instruct | **18.89** | **71.74** | **57.16** | **0.87** | **0.84**     | **0.82** | **0.58**  | **0.44**     |
| MADLAD400-7B             | 13.64     | 85.01     | 50.96     | 0.82     | 0.80         | 0.78     | 2.09      | 3.58         |
| SalamandraTA-7b-base     | 17.01     | 75.92     | 55.22     | 0.85     | 0.77         | 0.80     | 1.04      | 1.17         |


<img src="./images/bleu_eu.png" alt="English" width="100%"/>

</details>

### Low-Resource Languages of Spain

The tables below summarize the performance metrics for English, Spanish, and Catalan to Asturian, Aranese and Aragonese compared 
against [Transducens/IbRo-nllb](https://huggingface.co/Transducens/IbRo-nllb) [(Galiano Jimenez, et al.)](https://aclanthology.org/2024.wmt-1.85/), 
[NLLB-200-3.3B](https://huggingface.co/facebook/nllb-200-3.3B) ([Costa-jussà et al., 2022](https://arxiv.org/abs/2207.04672)) and [SalamandraTA-2B](https://huggingface.co/BSC-LT/salamandraTA-2B).

<details>
<summary>English evaluation</summary>
  
#### English-XX

|                | source   | target   | Bleu ↑      | Ter ↓       | ChrF ↑      |
|:-------------------------|:---------|:---------|:----------|:----------|:----------|
| SalamandraTA-7b-instruct | en       | ast      | **31.79** | **54.07** | **61.78** |
| SalamandraTA-7b-base     | en       | ast      | 26.40     | 64.02     | 57.35     |
| Transducens/IbRo-nllb    | en       | ast      | 20.56     | 63.92     | 53.32     |
| | | | | | |
| SalamandraTA-7b-instruct | en       | arn      | **22.77** | **66.06** | **52.61** |
| SalamandraTA-7b-base     | en       | arn      | 14.13     | 74.05     | 46.17     |
| Transducens/IbRo-nllb    | en       | arn      | 12.81     | 73.21     | 45.76     |
| | | | | | |
| SalamandraTA-7b-instruct | en       | arg      | **19.74** | 71.58     | **51.08** |
| Transducens/IbRo-nllb    | en       | arg      | 14.07     | **70.37** | 46.89     |
| SalamandraTA-7b-base     | en       | arg      | 12.24     | 73.48     | 44.75     |


</details>


<details>
<summary>Spanish evaluation</summary>
  
#### Spanish-XX

|                | source   | target   | Bleu ↑      | Ter ↓       | ChrF ↑      |
|:-------------------------|:---------|:---------|:----------|:----------|:----------|
| SalamandraTA-7b-instruct | es       | ast      | **20.66** | **71.81** | **53.14** |
| SalamandraTA-7b-base     | es       | ast      | 17.65     | 75.78     | 51.05     |
| Transducens/IbRo-nllb    | es       | ast      | 16.79     | 76.36     | 50.89     |
| | | | | | |
| SalamandraTA-7b-base     | es       | arn      | **51.59** | **35.51** | **73.50** |
| Transducens/IbRo-nllb    | es       | arn      | 50.20     | 36.60     | 73.16     |
| SalamandraTA-7b-instruct | es       | arn      | 47.37     | 39.29     | 70.65     |
| | | | | | |
| Transducens/IbRo-nllb    | es       | arg      | **59.75** | **28.01** | **78.73** |
| SalamandraTA-7b-base     | es       | arg      | 53.96     | 31.51     | 76.08     |
| SalamandraTA-7b-instruct | es       | arg      | 44.10     | 39.98     | 71.12     |

</details>


<details>
<summary>Catalan evaluation</summary>

  
#### Catalan-XX


|                | source   | target   | Bleu ↑      | Ter ↓       | ChrF ↑      |
|:-------------------------|:---------|:---------|:----------|:----------|:----------|
| SalamandraTA-7b-instruct | ca       | ast      | **28.13** | **58.84** | **58.98** |
| SalamandraTA-7b-base     | ca       | ast      | 26.11     | 63.63     | 58.08     |
| Transducens/IbRo-nllb    | ca       | ast      | 24.77     | 61.60     | 57.49     |
| | | | | | |
| SalamandraTA-7b-base     | ca       | arn      | **31.76** | **53.71** | **60.71** |
| Transducens/IbRo-nllb    | ca       | arn      | 31.22     | 54.30     | 60.30     |
| SalamandraTA-7b-instruct | ca       | arn      | 30.89     | 54.70     | 59.78     |
| | | | | | |
| Transducens/IbRo-nllb    | ca       | arg      | **24.44** | **60.79** | **55.51** |
| SalamandraTA-7b-base     | ca       | arg      | 22.53     | 62.37     | 54.32     |
| SalamandraTA-7b-instruct | ca       | arg      | 20.96     | 65.64     | 52.41     |


</details>


### Gender Aware Translation

Below are the evaluation results for gender aware translation evaluated on the [MT-GenEval](https://github.com/amazon-science/machine-translation-gender-eval?tab=readme-ov-file#mt-geneval) 
dataset ([Currey, A. et al.](https://github.com/amazon-science/machine-translation-gender-eval?tab=readme-ov-file#mt-geneval)). 
These have been calculated for translation from English into German, Spanish, French, Italian, Portuguese and Russian and are compared 
against [MADLAD400-7B-mt](https://huggingface.co/google/madlad400-7b-mt), [TowerInstruct-7B-v0.2](https://huggingface.co/Unbabel/TowerInstruct-7B-v0.2) 
and the SalamandraTA-7b-base model.
Evaluation was conducted using [MT-Lens](https://github.com/langtech-bsc/mt-evaluation) and is reported as accuracy computed using the accuracy metric 
provided with MT-GenEval.

<details>

|  | Source | Target | Masc | Fem | Pair |
|:--|:--|:--|:--|:--|:--|
| MADLAD400-7B | en | de | **0.877** | 0.823 | 0.713 |
| SalamandraTA-7b-base | en | de | 0.857 | 0.770 | 0.660 |
| SalamandraTA-7b-instruct | en | de | 0.863 | **0.867** | **0.740** |
| TowerInstruct-7B-v0.2 | en | de | 0.863 | 0.840 | 0.727 |
| | | | | | |
| MADLAD400-7B | en | es | 0.887 | 0.780 | 0.687 |
| SalamandraTA-7b-base | en | es | **0.890** | 0.733 | 0.643 |
| SalamandraTA-7b-instruct | en | es | 0.860 | **0.837** | **0.710** |
| TowerInstruct-7B-v0.2 | en | es | 0.850 | 0.823 | 0.693 |
| | | | | | |
| MADLAD400-7B | en | fr | 0.873 | 0.777 | 0.663 |
| SalamandraTA-7b-base | en | fr | 0.887 | 0.710 | 0.617 |
| SalamandraTA-7b-instruct | en | fr | **0.900** | 0.813 | **0.730** |
| TowerInstruct-7B-v0.2 | en | fr | 0.880 | **0.823** | 0.717 |
| | | | | | |
| MADLAD400-7B | en | it | 0.907 | 0.663 | 0.597 |
| SalamandraTA-7b-base | en | it | 0.893 | 0.593 | 0.513 |
| SalamandraTA-7b-instruct | en | it | 0.913 | **0.780** | 0.707 |
| TowerInstruct-7B-v0.2 | en | it | **0.947** | 0.747 | **0.713** |
| | | | | | |
| MADLAD400-7B | en | pt | 0.923 | 0.687 | 0.627 |
| SalamandraTA-7b-base | en | pt | 0.923 | 0.650 | 0.597 |
| SalamandraTA-7b-instruct | en | pt | **0.933** | **0.797** | **0.747** |
| TowerInstruct-7B-v0.2 | en | pt | 0.907 | 0.730 | 0.670 |
| | | | | | |
| MADLAD400-7B | en | ru | 0.940 | 0.797 | 0.740 |
| SalamandraTA-7b-base | en | ru | 0.933 | 0.713 | 0.653 |
| SalamandraTA-7b-instruct | en | ru | **0.950** | **0.830** | **0.783** |
| TowerInstruct-7B-v0.2 | en | ru | 0.933 | 0.797 | 0.733 |
| | | | | | |

</details>

## Ethical Considerations and Limitations

Detailed information on the work done to examine the presence of unwanted social and cognitive biases in the base model can be found 
at [Salamandra-7B model card](https://huggingface.co/BSC-LT/salamandra-7b).
With regard to MT models, the only analysis related to bias which we have conducted is the MT-GenEval evaluation. 
No specific analysis has yet been carried out in order to evaluate potential biases or limitations in translation 
accuracy across different languages, dialects, or domains. However, we recognize the importance of identifying and addressing any harmful stereotypes, 
cultural inaccuracies, or systematic performance discrepancies that may arise in Machine Translation. As such, we plan to continue performing more analyses 
as we implement the necessary metrics and methods within our evaluation framework [MT-Lens](https://github.com/langtech-bsc/mt-evaluation).
Note that the model has only undergone preliminary instruction tuning. 
We urge developers to consider potential limitations and conduct safety testing and tuning tailored to their specific applications.

## Additional information

### Author
The Language Technologies Unit from Barcelona Supercomputing Center.

### Contact
For further information, please send an email to <langtech@bsc.es>.

### Copyright
Copyright(c) 2025 by Language Technologies Unit, Barcelona Supercomputing Center.

### Funding
This work has been promoted and financed by the Government of Catalonia through the [Aina Project](https://projecteaina.cat/).

This work is funded by the _Ministerio para la Transformación Digital y de la Función Pública_ - Funded by EU – NextGenerationEU 
within the framework of [ILENIA Project](https://proyectoilenia.es/) with reference 2022/TL22/00215337.

### Acknowledgements

The success of this project has been made possible thanks to the invaluable contributions of our partners in the [ILENIA Project](https://proyectoilenia.es/): 
[HiTZ](http://hitz.ehu.eus/es), and [CiTIUS](https://citius.gal/es/).
Their efforts have been instrumental in advancing our work, and we sincerely appreciate their help and support. 



### Disclaimer


### Disclaimer
Be aware that the model may contain biases or other unintended distortions. 
When third parties deploy systems or provide services based on this model, or use the model themselves, 
they bear the responsibility for mitigating any associated risks and ensuring compliance with applicable regulations, 
including those governing the use of Artificial Intelligence.

The Barcelona Supercomputing Center, as the owner and creator of the model, shall not be held liable for any outcomes resulting from third-party use.

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)


### Citation

If you find our model useful, we would appreciate if you could cite our work as follows:

```
@misc{gilabert2025salamandrasalamandratabscsubmission,
      title={From SALAMANDRA to SALAMANDRATA: BSC Submission for WMT25 General Machine Translation Shared Task}, 
      author={Javier Garcia Gilabert and Xixian Liao and Severino Da Dalt and Ella Bohman and Audrey Mash and Francesca De Luca Fornaciari and Irene Baucells and Joan Llop and Miguel Claramunt Argote and Carlos Escolano and Maite Melero},
      year={2025},
      eprint={2508.12774},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.12774}, 
}
```