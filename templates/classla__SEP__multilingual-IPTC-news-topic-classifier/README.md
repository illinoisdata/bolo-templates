---
license: cc-by-sa-4.0
language:
- multilingual
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
tags:
- text-classification
- IPTC
- news
- news topic
- IPTC topic
- IPTC NewsCode
- topic categorization
widget:
- text: >-
    Moment dog sparks house fire after chewing power bank An indoor monitoring
    camera shows the moment a dog unintentionally caused a house fire after
    chewing on a portable lithium-ion battery power bank.
  example_title: English
- text: >-
    Ministarstvo unutarnjih poslova posljednjih mjeseci radilo je na izradi
    Nacrta prijedloga Zakona o strancima. Naime, važeći Zakon o strancima
    usklađen je s 22 direktive, preporuke, odluke i rezolucije, te s obzirom da
    je riječ o velikom broju odredaba potrebno ih je jasnije propisati, a sve u
    cilju poboljšanja transparentnosti i preglednosti.
  example_title: Croatian
- text: >-
    V okviru letošnjega praznovanja spominskega dneva občine Trebnje Baragov dan
    je v soboto, 28. junija 2014, na obvezni god Marijinega Srca v župnijski
    cerkvi v Trebnjem daroval mašo za domovino apostolski nuncij v Republiki
    Sloveniji Njegova ekselenca Nadškof msgr. Juliusz Janusz.
  example_title: Slovenian
base_model:
- FacebookAI/xlm-roberta-large
pipeline_tag: text-classification
---

# Multilingual IPTC Media Topic Classifier 

News topic classification model based on [`xlm-roberta-large`](https://huggingface.co/FacebookAI/xlm-roberta-large)
and fine-tuned on a [news corpus in 4 languages](http://hdl.handle.net/11356/1991) (Croatian, Slovenian, Catalan and Greek), annotated with the [top-level IPTC
Media Topic NewsCodes labels](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html).
The development and evaluation of the model is described in the paper
[LLM Teacher-Student Framework for Text Classification With No Manually Annotated Data: A Case Study in IPTC News Topic Classification](https://doi.org/10.1109/ACCESS.2025.3544814) (Kuzman and Ljubešić, 2025).

The model can be used for classification into topic labels from the 
[IPTC NewsCodes schema](https://iptc.org/std/NewsCodes/guidelines/#_what_are_the_iptc_newscodes) and can be
 applied to any news text in a language, supported by the `xlm-roberta-large`.

Based on a manually-annotated test set (in Croatian, Slovenian, Catalan and Greek),
the model achieves macro-F1 score of 0.746, micro-F1 score of 0.734, and accuracy of 0.734,
and outperforms the GPT-4o model (version `gpt-4o-2024-05-13`) used in a zero-shot setting.
 If we use only labels that are predicted with a confidence score equal or higher than 0.90, 
 the model achieves micro-F1 and macro-F1 of 0.80.

## Intended use and limitations

For reliable results, the classifier should be applied to documents of sufficient length (the rule of thumb is at least 75 words).


Use example:

```python
from transformers import pipeline

# Load a multi-class classification pipeline - if the model runs on CPU, comment out "device"
classifier = pipeline("text-classification", model="classla/multilingual-IPTC-news-topic-classifier", device=0, max_length=512, truncation=True)

# Example texts to classify
texts = [
    """Slovenian handball team makes it to Paris Olympics semifinal Lille, 8 August - Slovenia defeated Norway 33:28 in the Olympic men's handball tournament in Lille late on Wednesday to advance to the semifinal where they will face Denmark on Friday evening. This is the best result the team has so far achieved at the Olympic Games and one of the best performances in the history of Slovenia's team sports squads.""",
	"""Moment dog sparks house fire after chewing power bank An indoor monitoring camera shows the moment a dog unintentionally caused a house fire after chewing on a portable lithium-ion battery power bank. In the video released by Tulsa Fire Department in Oklahoma, two dogs and a cat can be seen in the living room before a spark started the fire that spread within minutes. Tulsa Fire Department public information officer Andy Little said the pets escaped through a dog door, and according to local media the family was also evacuated safely. "Had there not been a dog door, they very well could have passed away," he told CBS affiliate KOTV."""]

# Classify the texts
results = classifier(texts)

# Output the results
for result in results:
    print(result)

## Output
## {'label': 'sport', 'score': 0.9985264539718628}
## {'label': 'disaster, accident and emergency incident', 'score': 0.9957459568977356}

```

The code for massive corpora annotation with topic labels is available [here](https://colab.research.google.com/drive/1IYDNsr8E5Nj6ehxLaa4v4RfOqwGWPYB7?usp=sharing).

## IPTC Media Topic categories

The classifier uses the top-level of the [IPTC Media Topic NewsCodes](https://iptc.org/std/NewsCodes/guidelines/#_what_are_the_iptc_newscodes) schema, consisting of 17 labels.

### List of labels

```
labels_list=['education', 'human interest', 'society', 'sport', 'crime, law and justice',
'disaster, accident and emergency incident', 'arts, culture, entertainment and media', 'politics',
'economy, business and finance', 'lifestyle and leisure', 'science and technology',
'health', 'labour', 'religion', 'weather', 'environment', 'conflict, war and peace'],

labels_map={0: 'education', 1: 'human interest', 2: 'society', 3: 'sport', 4: 'crime, law and justice',
5: 'disaster, accident and emergency incident', 6: 'arts, culture, entertainment and media',
7: 'politics', 8: 'economy, business and finance', 9: 'lifestyle and leisure', 10: 'science and technology',
11: 'health', 12: 'labour', 13: 'religion', 14: 'weather', 15: 'environment', 16: 'conflict, war and peace'}
```

### Description of labels

The descriptions of the labels are based on the descriptions provided in the [IPTC Media Topic NewsCodes schema](https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html)
and enriched with information which specific subtopics belong to the top-level topics, based on the IPTC Media Topic label hierarchy.

| Label                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| disaster, accident and emergency incident | Man-made or natural events resulting in injuries, death or damage, e.g., explosions, transport accidents, famine, drowning, natural disasters, emergency planning and response.                                                                                                                                                                                                                                                                                                                                                                                |
| human interest                            | News about life and behavior of royalty and celebrities, news about obtaining awards, ceremonies (graduation, wedding, funeral, celebration of launching something), birthdays and anniversaries, and news about silly or stupid human errors.                                                                                                                                                                                                                                                                                                                 |
| politics                                  | News about local, regional, national and international exercise of power, including news about election, fundamental rights, government, non-governmental organisations, political crises, non-violent international relations, public employees, government policies.                                                                                                                                                                                                                                                                                         |
| education                                 | All aspects of furthering knowledge, formally or informally, including news about schools, curricula, grading, remote learning, teachers and students.                                                                                                                                                                                                                                                                                                                                                                                                         |
| crime, law and justice                    | News about committed crime and illegal activities, the system of courts, law and law enforcement (e.g., judges, lawyers, trials, punishments of offenders).                                                                                                                                                                                                                                                                                                                                                                                                    |
| economy, business and finance             | News about companies, products and services, any kind of industries, national economy, international trading, banks, (crypto)currency, business and trade societies, economic trends and indicators (inflation, employment statistics, GDP, mortgages, ...), international economic institutions, utilities (electricity, heating, waste management, water supply).                                                                                                                                                                                            |
| conflict, war and peace                   | News about terrorism, wars, wars victims, cyber warfare, civil unrest (demonstrations, riots, rebellions), peace talks and other peace activities.                                                                                                                                                                                                                                                                                                                                                                                                             |
| arts, culture, entertainment and media    | News about cinema, dance, fashion, hairstyle, jewellery, festivals, literature, music, theatre, TV shows, painting, photography, woodworking, art exhibitions, libraries and museums, language, cultural heritage, news media, radio and television, social media, influencers, and disinformation.                                                                                                                                                                                                                                                            |
| labour                                    | News about employment, employment legislation, employees and employers, commuting, parental leave, volunteering, wages, social security, labour market, retirement, unemployment, unions.                                                                                                                                                                                                                                                                                                                                                                      |
| weather                                   | News about weather forecasts, weather phenomena and weather warning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| religion                                  | News about religions, cults, religious conflicts, relations between religion and government, churches, religious holidays and festivals, religious leaders and rituals, and religious texts.                                                                                                                                                                                                                                                                                                                                                                   |
| society                                   | News about social interactions (e.g., networking), demographic analyses, population census, discrimination, efforts for inclusion and equity, emigration and immigration, communities of people and minorities (LGBTQ, older people, children, indigenous people, etc.), homelessness, poverty, societal problems (addictions, bullying), ethical issues (suicide, euthanasia, sexual behavior) and social services and charity, relationships (dating, divorce, marriage), family (family planning, adoption, abortion, contraception, pregnancy, parenting). |
| health                                    | News about diseases, injuries, mental health problems, health treatments, diets, vaccines, drugs, government health care, hospitals, medical staff, health insurance.                                                                                                                                                                                                                                                                                                                                                                                          |
| environment                               | News about climate change, energy saving, sustainability, pollution, population growth, natural resources, forests, mountains, bodies of water, ecosystem, animals, flowers and plants.                                                                                                                                                                                                                                                                                                                                                                        |
| lifestyle and leisure                     | News about hobbies, clubs and societies, games, lottery, enthusiasm about food or drinks, car/motorcycle lovers, public holidays, leisure venues (amusement parks, cafes, bars, restaurants, etc.), exercise and fitness, outdoor recreational activities (e.g., fishing, hunting), travel and tourism, mental well-being, parties, maintaining and decorating house and garden.                                                                                                                                                                               |
| science and technology                    | News about natural sciences and social sciences, mathematics, technology and engineering, scientific institutions, scientific research, scientific publications and innovation.                                                                                                                                                                                                                                                                                                                                                                                |
| sport                                     | News about sports that can be executed in competitions, e.g., basketball, football, swimming, athletics, chess, dog racing, diving, golf, gymnastics, martial arts, climbing, etc.; sport achievements, sport events, sport organisation, sport venues (stadiums, gymnasiums, ...), referees, coaches, sport clubs, drug use in sport.                                                                                                                                                                                                                        |

## Training data

The model was fine-tuned on the training split of the [EMMediaTopic 1.0 dataset](http://hdl.handle.net/11356/1991) consisting of 15,000 news in four languages (Croatian, Slovenian, Catalan and Greek).
The news texts were extracted from the [MaCoCu-Genre web corpora](http://hdl.handle.net/11356/1969) based on the "News" genre label, predicted with the [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier).
The training dataset was automatically annotated with the IPTC Media Topic labels by
the [GPT-4o](https://platform.openai.com/docs/models/gpt-4o) model (yielding 0.72 micro-F1 and 0.73 macro-F1 on the test dataset).

The code for the development and evaluation of the model is available on [this GitHub repository](https://github.com/TajaKuzman/IPTC-Media-Topic-Classification).

Label distribution in the training dataset:

| labels                                    |   count |   proportion |
|:------------------------------------------|--------:|-------------:|
| sport                                     |    2300 |   0.153333   |
| arts, culture, entertainment and media    |    2117 |   0.141133   |
| politics                                  |    2018 |   0.134533   |
| economy, business and finance             |    1670 |   0.111333   |
| human interest                            |    1152 |   0.0768     |
| education                                 |     990 |   0.066      |
| crime, law and justice                    |     884 |   0.0589333  |
| health                                    |     675 |   0.045      |
| disaster, accident and emergency incident |     610 |   0.0406667  |
| society                                   |     481 |   0.0320667  |
| environment                               |     472 |   0.0314667  |
| lifestyle and leisure                     |     346 |   0.0230667  |
| science and technology                    |     340 |   0.0226667  |
| conflict, war and peace                   |     311 |   0.0207333  |
| labour                                    |     288 |   0.0192     |
| religion                                  |     258 |   0.0172     |
| weather                                   |      88 |   0.00586667 |

## Performance

The model was evaluated on a manually-annotated test set in four languages (Croatian, Slovenian, Catalan and Greek),
 consisting of 1,129 instances.
The test set contains similar amounts of texts from the four languages and is more or less balanced across labels.

The model was shown to achieve micro-F1 score of 0.734, and macro-F1 score of 0.746. The results for the entire test set and per language:

|    |   Micro-F1 |   Macro-F1 |   Accuracy | No. of instances |
|:---|-----------:|-----------:|-----------:|-----------:|
| All (combined)    |   0.734278 |   0.745864 | 0.734278 |  1129 |
| Croatian |  0.728522 |   0.733725 |   0.728522 | 291 |
| Catalan |   0.715356 |   0.722304 |   0.715356 | 267 |
| Slovenian |   0.758865 |   0.764784 |   0.758865 | 282 |
| Greek |    0.733564 |   0.747129 |   0.733564 | 289 |


Performance per label:

|                                           |   precision |   recall |   f1-score |     support |
|:------------------------------------------|------------:|---------:|-----------:|------------:|
| arts, culture, entertainment and media    |    0.602151 | 0.875    |   0.713376 |   64        |
| conflict, war and peace                   |    0.611111 | 0.916667 |   0.733333 |   36        |
| crime, law and justice                    |    0.861538 | 0.811594 |   0.835821 |   69        |
| disaster, accident and emergency incident |    0.691176 | 0.886792 |   0.77686  |   53        |
| economy, business and finance             |    0.779221 | 0.508475 |   0.615385 |  118        |
| education                                 |    0.847458 | 0.735294 |   0.787402 |   68        |
| environment                               |    0.589041 | 0.754386 |   0.661538 |   57        |
| health                                    |    0.79661  | 0.79661  |   0.79661  |   59        |
| human interest                            |    0.552239 | 0.672727 |   0.606557 |   55        |
| labour                                    |    0.855072 | 0.830986 |   0.842857 |   71        |
| lifestyle and leisure                     |    0.773585 | 0.476744 |   0.589928 |   86        |
| politics                                  |    0.568182 | 0.735294 |   0.641026 |   68        |
| religion                                  |    0.842105 | 0.941176 |   0.888889 |   51        |
| science and technology                    |    0.637681 | 0.8      |   0.709677 |   55        |
| society                                   |    0.918033 | 0.5      |   0.647399 |  112        |
| sport                                     |    0.824324 | 0.968254 |   0.890511 |   63        |
| weather                                   |    0.953488 | 0.931818 |   0.942529 |   44        |


For downstream tasks, **we advise you to use only labels that were predicted with confidence score
higher or equal to 0.90 which further improves the performance**.

When we remove instances predicted with lower confidence (229 instances - 20%), the model yields micro-F1 of 0.798 and macro-F1 of 0.80.

|    |   Micro-F1 |   Macro-F1 |   Accuracy |
|:---|-----------:|-----------:|-----------:|
| All (combined)    |   0.797777 |   0.802403 | 0.797777 |
| Croatian |   0.773504 |   0.772084 |   0.773504 |
| Catalan |   0.811224 |   0.806885 |   0.811224 |
| Slovenian |   0.805085 |   0.804491 |   0.805085 |
| Greek |   0.803419 |   0.809598 |   0.803419 |

## Fine-tuning hyperparameters

Fine-tuning was performed with `simpletransformers`. 
Beforehand, a brief hyperparameter optimization was performed and the presumed optimal hyperparameters are:

```python
model_args = ClassificationArgs()

model_args ={
             "num_train_epochs": 5,
             "learning_rate": 8e-06,
             "train_batch_size": 32,
             "max_seq_length": 512,
             }   
      
```

## Citation

If you use the model, please cite [this paper](https://doi.org/10.1109/ACCESS.2025.3544814) and the model itself:

```
@ARTICLE{10900365,
  author={Kuzman, Taja and Ljubešić, Nikola},
  journal={IEEE Access}, 
  title={LLM Teacher-Student Framework for Text Classification With No Manually Annotated Data: A Case Study in IPTC News Topic Classification}, 
  year={2025},
  volume={},
  number={},
  pages={1-1},
  keywords={Data models;Annotations;Media;Manuals;Multilingual;Computational modeling;Training;Training data;Transformers;Text categorization;Multilingual text classification;IPTC;large language models;LLMs;news topic;topic classification;training data preparation;data annotation},
  doi={10.1109/ACCESS.2025.3544814}}

@misc{iptc_topic_model,
	author       = { Kuzman, Taja and Ljube{\v s}i{\'c}, Nikola },
	title        = {{ Multilingual IPTC News Topic Classifier}},
	year         = 2025,
	url          = { https://huggingface.co/classla/multilingual-IPTC-news-topic-classifier },
	doi          = { 10.57967/hf/4709 },
	publisher    = { Hugging Face }
}
```

## Funding

This work was supported by the Slovenian Research and Innovation Agency research project [Embeddings-based techniques for Media Monitoring Applications](https://emma.ijs.si/en/about-project/) (L2-50070, co-funded by the Kliping d.o.o. agency).