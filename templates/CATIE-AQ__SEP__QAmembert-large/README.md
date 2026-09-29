---
language: fr
datasets:
- etalab-ia/piaf
- fquad
- lincoln/newsquadfr
- pragnakalp/squad_v2_french_translated
widget:
- text: Combien de personnes utilisent le français tous les jours ?
  context: >-
    Le français est une langue indo-européenne de la famille des langues romanes
    dont les locuteurs sont appelés francophones. Elle est parfois surnommée la
    langue de Molière.  Le français est parlé, en 2023, sur tous les continents
    par environ 321 millions de personnes : 235 millions l'emploient
    quotidiennement et 90 millions en sont des locuteurs natifs. En 2018, 80
    millions d'élèves et étudiants s'instruisent en français dans le monde.
    Selon l'Organisation internationale de la francophonie (OIF), il pourrait y
    avoir 700 millions de francophones sur Terre en 2050.
license: mit
metrics:
- f1
- exact_match
library_name: transformers
pipeline_tag: question-answering
co2_eq_emissions: 200
new_version: CATIE-AQ/QAmemberta
---

# Model Card for QAmembert-large

## Model Description

We present **QAmemBERT**, which is a [CamemBERT large](https://huggingface.co/camembert/camembert-large) fine-tuned for the Question-Answering task for the French language on four French Q&A datasets composed of contexts and questions with their answers inside the context (= SQuAD 1.0 format) but also contexts and questions with their answers not inside the context (= SQuAD 2.0 format).
All these datasets were concatenated into a single dataset that we called [frenchQA](https://huggingface.co/datasets/CATIE-AQ/frenchQA).
This represents a total of over **221,348 context/question/answer triplets used to finetune this model and 6,376 to test it**.  
Our methodology is described in a blog post available in [English](https://blog.vaniila.ai/en/QA_en/) or [French](https://blog.vaniila.ai/QA/).

## Datasets

| Dataset     | Format      | Train split | Dev split   | Test split  |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| [piaf](https://www.data.gouv.fr/en/datasets/piaf-le-dataset-francophone-de-questions-reponses/)| SQuAD 1.0    | 9 224 Q & A  | X  | X  |  
| piaf_v2| SQuAD 2.0    | 9 224 Q & A  | X  | X  |         
| [fquad](https://fquad.illuin.tech/)| SQuAD 1.0    | 20 731 Q & A | 3 188 Q & A  (not used in training because it serves as a test dataset) | 2 189 Q & A (not used in our work because not freely available)|         
| fquad_v2 | SQuAD 2.0    | 20 731 Q & A | 3 188 Q & A  (not used in training because it serves as a test dataset) | X |         
| [lincoln/newsquadfr](https://huggingface.co/datasets/lincoln/newsquadfr) | SQuAD 1.0    | 1 650 Q & A  | 455 Q & A (not used in our work) | X |           
| lincoln/newsquadfr_v2 | SQuAD 2.0    | 1 650 Q & A  | 455 Q & A (not used in our work) | X |         
| [pragnakalp/squad_v2_french_translated](https://huggingface.co/datasets/pragnakalp/squad_v2_french_translated)| SQuAD 2.0    | 79 069 Q & A  | X  | X  |         
| pragnakalp/squad_v2_french_translated_v2| SQuAD 2.0    | 79 069 Q & A  | X  | X  |

All these datasets were concatenated into a single dataset that we called [frenchQA](https://huggingface.co/datasets/CATIE-AQ/frenchQA).


## Evaluation results

The evaluation was carried out using the [**evaluate**](https://pypi.org/project/evaluate/) python package.

### FQuaD 1.0 (validation)

The metric used is SQuAD 1.0.

| Model       | Exact_match | F1-score    |
| ----------- | ----------- | ----------- |
| [etalab-ia/camembert-base-squadFR-fquad-piaf](https://huggingface.co/etalab-ia/camembert-base-squadFR-fquad-piaf) | 53.60       | 78.09       |
| QAmembert (previous version)   | 54.26       | 77.87       |
| [QAmembert (version on HF)](https://huggingface.co/CATIE-AQ/QAmembert)   | 53.98       | 78.00       |
| QAmembert-large  | **55.95**       | **81.05**       |


### qwant/squad_fr (validation)

The metric used is SQuAD 1.0.

| Model       | Exact_match | F1-score    |
| ----------- | ----------- | ----------- |
| [etalab-ia/camembert-base-squadFR-fquad-piaf](https://huggingface.co/etalab-ia/camembert-base-squadFR-fquad-piaf) | 60.17       | 78.27       |
| QAmembert (previous version)   | 60.40       | 77.27       |
| [QAmembert (version on HF)](https://huggingface.co/CATIE-AQ/QAmembert)   |  60.95       | 77.30       |
| QAmembert-large  | **65.58**       | **81.74**       |


### frenchQA

This dataset includes question with no answers in the context. The metric used is SQuAD 2.0.

| Model       | Exact_match | F1-score    | Answer_f1 | NoAnswer_f1 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| [etalab-ia/camembert-base-squadFR-fquad-piaf](https://huggingface.co/etalab-ia/camembert-base-squadFR-fquad-piaf) | n/a       | n/a       | n/a       | n/a       |
| QAmembert (previous version)   | 60.28       | 71.29       | 75.92 | 66.65
| [QAmembert (version on HF)](https://huggingface.co/CATIE-AQ/QAmembert)   |  **77.14**       | 86.88       | 75.66 | 98.11
| QAmembert-large  | **77.14**       | **88.74**       | **78.83** | **98.65**


## Usage
### Example with answer in the context

```python
from transformers import pipeline

qa = pipeline('question-answering', model='CATIE-AQ/QAmembert-large', tokenizer='CATIE-AQ/QAmembert-large')

result = qa({
    'question': "Combien de personnes utilisent le français tous les jours ?",
    'context': "Le français est une langue indo-européenne de la famille des langues romanes dont les locuteurs sont appelés francophones. Elle est parfois surnommée la langue de Molière.  Le français est parlé, en 2023, sur tous les continents par environ 321 millions de personnes : 235 millions l'emploient quotidiennement et 90 millions en sont des locuteurs natifs. En 2018, 80 millions d'élèves et étudiants s'instruisent en français dans le monde. Selon l'Organisation internationale de la francophonie (OIF), il pourrait y avoir 700 millions de francophones sur Terre en 2050."
})

if result['score'] < 0.01:
    print("La réponse n'est pas dans le contexte fourni.")
else :
    print(result['answer'])
```
```python
235 millions
```
```python
# details
result
{'score': 0.9876325726509094,
 'start': 268,
 'end': 281,
 'answer': ' 235 millions'}
```


### Example with answer not in the context
```python
from transformers import pipeline

qa = pipeline('question-answering', model='CATIE-AQ/QAmembert-large', tokenizer='CATIE-AQ/QAmembert-large')

result = qa({
    'question': "Quel est le meilleur vin du monde ?",
    'context': "La tour Eiffel est une tour de fer puddlé de 330 m de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.  
Construite en deux ans par Gustave Eiffel et ses collaborateurs pour l'Exposition universelle de Paris de 1889, célébrant le centenaire de la Révolution française, et initialement nommée « tour de 300 mètres », elle est devenue le symbole de la capitale française et un site touristique de premier plan : il s’agit du quatrième site culturel français payant le plus visité en 2016, avec 5,9 millions de visiteurs. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs."
})

if result['score'] < 0.01:
    print("La réponse n'est pas dans le contexte fourni.")
else :
    print(result['answer'])
```
```python
La réponse n'est pas dans le contexte fourni.
```
```python
# details
result
{'score': 1.1262776822285048e-10,
 'start': 735,
 'end': 746,
 'answer': 'visiteurs.'}
```


## Environmental Impact

*Carbon emissions were estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). The hardware, runtime, cloud provider, and compute region were utilized to estimate the carbon impact.*

- **Hardware Type:** A100 PCIe 40/80GB
- **Hours used:** 11h and 12min
- **Cloud Provider:** Private Infrastructure
- **Carbon Efficiency (kg/kWh):** 0.076kg (estimated from [electricitymaps](https://app.electricitymaps.com/zone/FR) ; we take the average carbon intensity in France for the month of March 2023, as we are unable to use the data for the day of training, which are not available.)
- **Carbon Emitted** *(Power consumption x Time x Carbon produced based on location of power grid)*: 0.20 kg eq. CO2


## Citations

### QAmemBERT
```
@misc {qamembert2023,  
    author       = { {ALBAR, Boris and BEDU, Pierre and BOURDOIS, Loïck} },  
    organization  = { {Centre Aquitain des Technologies de l'Information et Electroniques} },  
    title        = { QAmembert (Revision 9685bc3) },  
    year         = 2023,  
    url          = { https://huggingface.co/CATIE-AQ/QAmembert-large },  
    doi          = { 10.57967/hf/0821 },  
    publisher    = { Hugging Face }  
}
```

### PIAF
```
@inproceedings{KeraronLBAMSSS20,
  author    = {Rachel Keraron and
               Guillaume Lancrenon and
               Mathilde Bras and
               Fr{\'{e}}d{\'{e}}ric Allary and
               Gilles Moyse and
               Thomas Scialom and
               Edmundo{-}Pavel Soriano{-}Morales and
               Jacopo Staiano},
  title     = {Project {PIAF:} Building a Native French Question-Answering Dataset},
  booktitle = {{LREC}},
  pages     = {5481--5490},
  publisher = {European Language Resources Association},
  year      = {2020}
}

```

### FQuAD
```
@article{dHoffschmidt2020FQuADFQ,
  title={FQuAD: French Question Answering Dataset},
  author={Martin d'Hoffschmidt and Maxime Vidal and Wacim Belblidia and Tom Brendl'e and Quentin Heinrich},
  journal={ArXiv},
  year={2020},
  volume={abs/2002.06071}
}
```

### lincoln/newsquadfr
```
Hugging Face repository: https://hf.co/datasets/lincoln/newsquadfr
```

### pragnakalp/squad_v2_french_translated
```
Hugging Face repository: https://hf.co/datasets/pragnakalp/squad_v2_french_translated
```

### CamemBERT
```
@inproceedings{martin2020camembert,
  title={CamemBERT: a Tasty French Language Model},
  author={Martin, Louis and Muller, Benjamin and Su{\'a}rez, Pedro Javier Ortiz and Dupont, Yoann and Romary, Laurent and de la Clergerie, {\'E}ric Villemonte and Seddah, Djam{\'e} and Sagot, Beno{\^\i}t},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  year={2020}
}
```

## License
MIT