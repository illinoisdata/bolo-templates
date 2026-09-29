---
license: mit
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
datasets:
- agentlans/en-translations
base_model:
- agentlans/multilingual-e5-small-aligned
pipeline_tag: text-classification
tags:
- multilingual
- sentiment-assessment
---

# multilingual-e5-small-aligned-sentiment

This model is a fine-tuned version of [agentlans/multilingual-e5-small-aligned](https://huggingface.co/agentlans/multilingual-e5-small-aligned) designed for assessing text sentiment across multiple languages.

## Key Features

- Multilingual support
- Sentiment assessment for text
- Based on E5 small model architecture

## Intended Uses & Limitations

This model is intended for:
- Assessing the sentiment of multilingual text
- Filtering multilingual content
- Comparative analysis of corpus text sentiment across different languages

Limitations:
- Performance may vary for languages not well-represented in the training data
- Should not be used as the sole criterion for sentiment assessment

## Usage Example

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "agentlans/multilingual-e5-small-aligned-sentiment"

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def sentiment(text):
    """Assess the sentiment of the input text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        logits = model(**inputs).logits.squeeze().cpu()
    return logits.tolist()

# Example usage
score = sentiment("Your text here.")
print(f"Sentiment score: {score}")
```

## Performance Results

The model was evaluated on a diverse set of multilingual text samples:

- 10 English text samples of varying sentiment were translated into Arabic, Chinese, French, Russian, and Spanish.
- The model demonstrated consistent sentiment assessment across different languages for the same text.

<details>
<summary>Click here for the 10 original texts and their translations.</summary>

| **Text** | **English** | **French** | **Spanish** | **Chinese** | **Russian** | **Arabic** |
|---|---|---|---|---|---|---|
| A | Nothing seems to go right, and I'm constantly frustrated. | Rien ne semble aller bien et je suis constamment frustré. | Nada parece ir bien y me siento constantemente frustrado. | 一切似乎都不顺利，我总是感到很沮丧。 | Кажется, все идет не так, как надо, и я постоянно расстроен. | يبدو أن لا شيء يسير على ما يرام، وأنا أشعر بالإحباط باستمرار. |
| B | Everything is falling apart, and I can't see any way out. | Tout s’effondre et je ne vois aucune issue. | Todo se está desmoronando y no veo ninguna salida. | 一切都崩溃了，我看不到任何出路。 | Все рушится, и я не вижу выхода. | كل شيء ينهار، ولا أستطيع أن أرى أي مخرج. |
| C | I feel completely overwhelmed by the challenges I face. | Je me sens complètement dépassé par les défis auxquels je suis confronté. | Me siento completamente abrumado por los desafíos que enfrento. | 我感觉自己完全被所面临的挑战压垮了。 | Я чувствую себя совершенно подавленным из-за проблем, с которыми мне приходится сталкиваться. | أشعر بأنني غارق تمامًا في التحديات التي أواجهها. |
| D | There are some minor improvements, but overall, things are still tough. | Il y a quelques améliorations mineures, mais dans l’ensemble, les choses restent difficiles. | Hay algunas mejoras menores, pero en general las cosas siguen siendo difíciles. | 虽然有一些小的改进，但是总的来说，事情仍然很艰难。 | Есть некоторые незначительные улучшения, но в целом ситуация по-прежнему сложная. | هناك بعض التحسينات الطفيفة، ولكن بشكل عام، لا تزال الأمور صعبة. |
| E | I can see a glimmer of hope amidst the difficulties I encounter. | Je vois une lueur d’espoir au milieu des difficultés que je rencontre. | Puedo ver un rayo de esperanza en medio de las dificultades que encuentro. | 我在遇到的困难中看到了一线希望。 | Среди трудностей, с которыми я сталкиваюсь, я вижу проблеск надежды. | أستطيع أن أرى بصيص أمل وسط الصعوبات التي أواجهها. |
| F | Things are starting to look up, and I'm cautiously optimistic. | Les choses commencent à s’améliorer et je suis prudemment optimiste. | Las cosas están empezando a mejorar y me siento cautelosamente optimista. | 事情开始好转，我持谨慎乐观的态度。 | Ситуация начинает улучшаться, и я настроен осторожно и оптимистично. | بدأت الأمور تتجه نحو التحسن، وأنا متفائل بحذر. |
| G | I'm feeling more positive about my situation than I have in a while. | Je me sens plus positif à propos de ma situation que je ne l’ai été depuis un certain temps. | Me siento más positivo sobre mi situación que en mucho tiempo. | 我对自己处境的感觉比以前更加乐观了。 | Я чувствую себя более позитивно относительно своей ситуации, чем когда-либо за последнее время. | أشعر بإيجابية أكبر تجاه وضعي مقارنة بأي وقت مضى. |
| H | There are many good things happening, and I appreciate them. | Il se passe beaucoup de bonnes choses et je les apprécie. | Están sucediendo muchas cosas buenas y las aprecio. | 有很多好事发生，我对此表示感谢。 | Происходит много хорошего, и я это ценю. | هناك الكثير من الأشياء الجيدة التي تحدث، وأنا أقدرها. |
| I | Every day brings new joy and possibilities; I feel truly blessed. | Chaque jour apporte de nouvelles joies et possibilités ; je me sens vraiment béni. | Cada día trae nueva alegría y posibilidades; me siento verdaderamente bendecida. | 每天都有新的快乐和可能性；我感到非常幸福。 | Каждый день приносит новую радость и возможности; я чувствую себя по-настоящему благословенной. | كل يوم يجلب فرحة وإمكانيات جديدة؛ أشعر بأنني محظوظة حقًا. |
| J | Life is full of opportunities, and I'm excited about the future. | La vie est pleine d’opportunités et je suis enthousiaste quant à l’avenir. | La vida está llena de oportunidades y estoy entusiasmado por el futuro. | 生活充满机遇，我对未来充满兴奋。 | Жизнь полна возможностей, и я с нетерпением жду будущего. | الحياة مليئة بالفرص، وأنا متحمس للمستقبل. |

</details>

<img src="Sentiment.svg" alt="Scatterplot of predicted sentiment scores grouped by text sample and language" width="100%"/>

## Training Data

The model was trained on the [Multilingual Parallel Sentences dataset](https://huggingface.co/datasets/agentlans/en-translations), which includes:

- Parallel sentences in English and various other languages
- Semantic similarity scores calculated using LaBSE
- Additional sentiment metrics
- Sources: JW300, Europarl, TED Talks, OPUS-100, Tatoeba, Global Voices, and News Commentary

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 128
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Mse    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.1946        | 1.0   | 7813  | 0.1647          | 0.1647 |
| 0.1385        | 2.0   | 15626 | 0.1528          | 0.1528 |
| 0.1121        | 3.0   | 23439 | 0.1455          | 0.1455 |


### Framework versions

- Transformers 4.46.3
- Pytorch 2.5.1+cu124
- Datasets 3.1.0
- Tokenizers 0.20.3