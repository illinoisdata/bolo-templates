---
language: pt
license: cc-by-nc-sa-4.0
tags:
- t5
- pytorch
- pt
- pt-br
- summarization
- abstractive summarization
datasets:
- csebuetnlp/xlsum
inference:
  parameters:
    min_length: 32
    max_length: 256
    top_k: 5
widget:
- text: 'O homem, Wilmer Antonio Marin, conhecido como Hugo, seria um alto comandante das Forças Armadas Revolucionárias da Colômbia (Farc), o maior grupo rebelde do país. Ele é acusado de ter perpetrado um ataque num clube noturno em fevereiro que matou 35 pessoas e feriu 160. Hugo também estaria envolvido no assassinato do empresário japonês Chikao Muramatsu que foi encontrado morto a tiros em novembro, quase três anos depois de ter sido seqüestrado. Golpe O resgate de US$ 19 milhões (R$ 55 milhões) tinha sido pedido para a libertação de Muramatsu. As autoridades colombianas acreditam que a detenção de Hugo representa um grande golpe na estrutura da Farc em Bogotá. Wilmer Antonio Marin é acusado de administrar uma rede de seqüestros que teria, como alvo, empresários ricos e estrangeiros. Ele seria reponsável por seqüestrá-los no meio da rua e levá-los para as montanhas onde a guerrilha tem suas bases.'
  example_title: "Notícia 1"
- text: 'Terminou a rebelião de presos no Centro de Custódia de Presos de Justiça (CCPJ), em São Luís, no começo da tarde desta quarta-feira (17). Os presos entregaram as armas e a polícia faz uma revista dentro da unidade. O motim começou durante a festa do Dia das Crianças, realizada na terça-feira (16). As 16 crianças e 14 adultos foram libertados. Segundo informações da polícia, o líder da rebelião foi transferido para o Presídio de Pedrinhas, na capital maranhense. Os presos receberam garantias, por parte do diretor da unidade, de que não haveria represálias e novas transferências. Os presos tentaram fugir durante a festa, mas o plano foi descoberto. No começo da rebelião quatro pessoas ficaram feridas, entre elas uma auxiliar de enfermagem e um agente de polícia que trabalham no presídio. A unidade ficou sem luz e água e as negociações para a libertação dos reféns foi retomada na manhã desta quarta-feira. Segundo informações da polícia, os presos temiam uma transferência em massa depois de terem iniciado uma outra rebelião durante a greve de policiais no estado, na semana passada. A CCPJ tem capacidade para cerca de 80 presos, mas abriga 203 homens.'
  example_title: "Notícia 2"
---

# Portuguese T5 for Abstractive Summarization (PTT5 Summ)

## Introduction
PTT5 Summ is a fine-tuned [PTT5](https://github.com/unicamp-dl/PTT5) model to perform Abstractive Summarization in Brazilian Portuguese texts. This model was fine-tuned on the datasets: [RecognaSumm](https://huggingface.co/datasets/recogna-nlp/recognasumm), [WikiLingua](https://github.com/esdurmus/Wikilingua), [XL-Sum](https://github.com/csebuetnlp/xl-sum), [TeMário](http://www.nilc.icmc.usp.br/nilc/download/NILCTR0706-MazieroEtAl(2).pdf) and [CSTNews](http://nilc.icmc.usp.br/CSTNews/login/?next=/CSTNews/).

For further information, please go to [PTT5 Summ repository](https://github.com/pedropaiola/ptt5-summ).

## Available models
| Model                                                                                                | Dataset used in fine-tuning| 
| :-:                                                                                                  | :-:                        | 
| [recogna-nlp/ptt5-base-summ](https://huggingface.co/recogna-nlp/ptt5-base-summ)                            | [RecognaSumm](https://huggingface.co/datasets/recogna-nlp/recognasumm) |
| [recogna-nlp/ptt5-base-summ-wikilingua](https://huggingface.co/recogna-nlp/ptt5-base-summ-wikilingua)      | WikiLingua |
| [recogna-nlp/ptt5-base-summ-xlsum](https://huggingface.co/recogna-nlp/ptt5-base-summ-xlsum)                | XL-Sum     |
| [recogna-nlp/ptt5-base-summ-temario](https://huggingface.co/recogna-nlp/ptt5-base-summ-temario)            | 1st phase: WikiLingua. 2nd phase: TeMario |
| [recogna-nlp/ptt5-base-summ-cstnews](https://huggingface.co/recogna-nlp/ptt5-base-summ-cstnews)            | 1st phase: WikiLingua. 2nd phase: CSTNews|

## Usage example
```python
# Tokenizer 
from transformers import T5Tokenizer

# PyTorch model 
from transformers import T5Model, T5ForConditionalGeneration

token_name = 'unicamp-dl/ptt5-base-portuguese-vocab'
model_name = 'phpaiola/ptt5-base-summ-xlsum'

tokenizer = T5Tokenizer.from_pretrained(token_name )
model_pt = T5ForConditionalGeneration.from_pretrained(model_name)

text = '''
“A tendência de queda da taxa de juros no Brasil é real, é visível”, disse Meirelles, que participou na capital americana de uma série de reuniões e encontros com banqueiros e investidores que aconteceram paralelamente às reuniões do Fundo Monetário Internacional (FMI) e do Banco Mundial (Bird) no fim de semana.
Para o presidente do BC, a atual política econômica do governo e a manutenção da taxa de inflação dentro da meta são fatores que garantem queda na taxa de juros a longo prazo.
“Mas é importante que nós não olhemos para isso apenas no curto prazo. Temos que olhar no médio e longo prazos”, disse Meirelles.
Para ele, o trabalho que o Banco Central tem feito para conter a inflação dentro da meta vai gerar queda gradual da taxa de juros.
BC do ano
Neste domingo, Meirelles participou da cerimônia de entrega do prêmio “Banco Central do ano”, oferecido pela revista The Banker à instituição que preside.
“Este é um sinal importante de reconhecimento do nosso trabalho, de que o Brasil está indo na direção correta”, disse ele.
Segundo Meirelles, o Banco Central do Brasil está sendo percebido como uma instituição comprometida com a meta de inflação.
“Isso tem um ganho importante, na medida em que os agentes formadores de preços começam a apostar que a inflação vai estar na meta, que isso é levado a sério no Brasil”, completou.
O presidente do Banco Central disse ainda que a crise política brasileira não foi um assunto de interesse prioritário dos investidores que encontrou no fim de semana.
'''

inputs = tokenizer.encode(text, max_length=512, truncation=True, return_tensors='pt')
summary_ids = model_pt.generate(inputs, max_length=256, min_length=32, num_beams=5, no_repeat_ngram_size=3, early_stopping=True)
summary = tokenizer.decode(summary_ids[0])
print(summary)
#<pad> O presidente do Banco Central, Henrique Meirelles, disse neste domingo, em Washington, que a taxa de juros no Brasil é real, mas que o Brasil está indo na direção correta.</s>

```

# Citation

    @aInProceedings{ptt5summ_bracis,
      author="Paiola, Pedro H.
        and de Rosa, Gustavo H.
        and Papa, Jo{\~a}o P.",
      editor="Xavier-Junior, Jo{\~a}o Carlos
        and Rios, Ricardo Ara{\'u}jo",
      title="Deep Learning-Based Abstractive Summarization for Brazilian Portuguese Texts",
      booktitle="BRACIS 2022: Intelligent Systems",
      year="2022",
      publisher="Springer International Publishing",
      address="Cham",
      pages="479--493",
      isbn="978-3-031-21689-3"}

![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)

# 📢 Licensing Notice

**This model was fine-tuned using the [XL-Sum dataset](https://github.com/csebuetnlp/xl-sum), which is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). As a result, this model is also distributed under the same license.**

- **Commercial use is NOT permitted.**
- **Any derivative work must be licensed under CC BY-NC-SA 4.0.**
- **Proper attribution to the XL-Sum dataset authors is required.**

If you intend to use this model for commercial purposes, you must retrain it using datasets with compatible licenses.

### Attribution (XL-SUM)

Hasan, Tahmid; Bhattacharjee, Abhik; Islam, Md. Saiful; Mubasshir, Kazi; Li, Yuan-Fang; Kang, Yong-Bin; Rahman, M. Sohel; Shahriyar, Rifat.  
**XL-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages.**  
In: *Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021*, pages 4693–4703, Online, August 2021.  
[https://aclanthology.org/2021.findings-acl.413](https://aclanthology.org/2021.findings-acl.413)

BibTeX:

```bibtex
@inproceedings{hasan-etal-2021-xl,
    title = "{XL}-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages",
    author = "Hasan, Tahmid  and
      Bhattacharjee, Abhik  and
      Islam, Md. Saiful  and
      Mubasshir, Kazi  and
      Li, Yuan-Fang  and
      Kang, Yong-Bin  and
      Rahman, M. Sohel  and
      Shahriyar, Rifat",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.413",
    pages = "4693--4703",
}