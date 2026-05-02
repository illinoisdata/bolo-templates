---
language:
- it
license: apache-2.0
datasets:
- ARTeLab/fanpage
- ARTeLab/ilpost
tags:
- italian
- sequence-to-sequence
- fanpage
- ilpost
- summarization
widget:
- text: "Non lo vuole sposare. E’ quanto emerge all’interno dell’ultima intervista di Raffaella Fico che, ringraziando Mancini per i buoni consigli elargiti al suo fidanzato, rimanda l’idea del matrimonio per qualche anno ancora. La soubrette, che è stata recentemente protagonista di una dedica di Supermario, non ha ancora intenzione di accasarsi perché è sicura che per mettersi la fede al dito ci sia ancora tempo. Nonostante il suo Mario sia uno degli sportivi più desiderati al mondo, l’ex protagonista del Grande Fratello non ha alcuna intenzione di cedere seriamente alla sua corte. Solo qualche giorno fa, infatti, dopo l’ultima bravata di Balotelli, Mancini gli aveva consigliato di sposare la sua Raffaella e di mettere la testa a posto. Chi pensava che sarebbe stato Mario a rispondere, però, si è sbagliato. A mettere le cose bene in chiaro è la Fico che, intervistata dall’emittente radiofonica Rtl 102.5, dice: È presto per sposarsi, siamo ancora molto giovani. È giusto che prima uno si realizzi nel proprio lavoro. E poi successivamente perché no, ci si può anche pensare. Quando si è giovani capita di fare qualche pazzia, quindi ci sta. Comunque i tabloid inglesi sono totalmente accaniti sulla sua vita privata quando poi dovrebbero interessarsi di più di quello che fa sul campo. Lui non fa le cose con cattiveria, ma quando si è giovani si fanno determinate cose senza stare a pensare se sono giuste o sbagliate. Mario ha gli obiettivi puntati addosso: più per la sua vita privata che come giocatore. Per me può anche andare in uno strip club, se non fa niente di male, con gli amici, però devo dire che alla fine torna sempre da me, sono la sua preferita."
- text: "Valerio è giovanissimo ma già una star. Fuori dall’Ariston ragazzine e meno ragazzine passano ore anche sotto la pioggia per vederlo. Lui è forte del suo talento e sicuro. Partecipa in gara tra i “big” di diritto, per essere arrivato in finalissima nel programma Amici di Maria De Filippi e presenta il brano Per tutte le volte che scritta per lui da Pierdavide Carone. Valerio Scanu è stato eliminato. Ma non è detta l'ultima parola: il duetto di questa sera con Alessandra Amoroso potrebbe risollevarlo e farlo rientrare in gara. Che cosa è successo alla giuria visto che sei stato eliminato anche se l’esibizione era perfetta? Nn lo so. Sono andate bene le esibizioni, ero emozionato ma tranquillo. Ero contento ma ho cantato bene. Non sono passato e stasera ci sarà il ballottaggio… Quali sono le differenze tra Amici e Sanremo? Sono due cose diverse. Amici ti prepara a salire sul palco di amici. A Sanremo ci devi arrivare… ho fatto più di sessanta serate nel tour estivo, poi promozione del secondo disco. Una bella palestra. Sono cresciuto anche umanamente. Sono riuscito a percepire quello che il pubblico trasmette. L’umiltà? Prima di tutto. Sennò non sarei qui."
- text: "L’azienda statunitense Broadcom, uno dei più grandi produttori di semiconduttori al mondo, ha presentato un’offerta per acquisire Qualcomm, altra grande società degli Stati Uniti conosciuta soprattutto per la sua produzione di microprocessori Snapdragon (ARM), utilizzati in centinaia di milioni di smartphone in giro per il mondo. Broadcom ha proposto di acquistare ogni azione di Qualcomm al prezzo di 70 dollari, per un valore complessivo di circa 105 miliardi di dollari (130 miliardi se si comprendono 25 miliardi di debiti netti) . Se l’operazione dovesse essere approvata, sarebbe una delle più grandi acquisizioni di sempre nella storia del settore tecnologico degli Stati Uniti. Broadcom ha perfezionato per mesi la sua proposta di acquisto e, secondo i media statunitensi, avrebbe già preso contatti con Qualcomm per trovare un accordo. Secondo gli analisti, Qualcomm potrebbe comunque opporsi all’acquisizione perché il prezzo offerto è di poco superiore a quello dell’attuale valore delle azioni dell’azienda. Ci potrebbero essere inoltre complicazioni sul piano dell’antitrust da valutare, prima di un’eventuale acquisizione."
- text: "Dal 31 maggio è infine partita la piattaforma ITsART, a più di un anno da quando – durante il primo lockdown – il ministro della Cultura Dario Franceschini ne aveva parlato come di «una sorta di Netflix della cultura», pensata per «offrire a tutto il mondo la cultura italiana a pagamento». È presto per dare giudizi definitivi sulla piattaforma, e di certo sarà difficile farlo anche più avanti senza numeri precisi. Al momento, l’unica cosa che si può fare è guardare com’è fatto il sito, contare quanti contenuti ci sono (circa 700 “titoli”, tra film, documentari, spettacoli teatrali e musicali e altri eventi) e provare a dare un giudizio sul loro valore e sulla loro varietà. Intanto, una cosa notata da più parti è che diversi contenuti di ITsART sono a pagamento sulla piattaforma sebbene altrove, per esempio su RaiPlay, siano invece disponibili gratuitamente."
metrics:
- rouge
model-index:
- name: it5-base-news-summarization
  results:
  - task: 
      type: news-summarization
      name: "News Summarization"
    dataset:
      type: newssum-it
      name: "NewsSum-IT"
    metrics:
      - type: rouge1
        value: 0.339
        name: "Test Rouge1"
      - type: rouge2
        value: 0.160
        name: "Test Rouge2"
      - type: rougeL
        value: 0.263
        name: "Test RougeL"
co2_eq_emissions:
      emissions: 17
      source: "Google Cloud Platform Carbon Footprint"
      training_type: "fine-tuning"
      geographical_location: "Eemshaven, Netherlands, Europe"
      hardware_used: "1 TPU v3-8 VM"
thumbnail: https://gsarti.com/publication/it5/featured.png
---
# IT5 Base for News Summarization ✂️🗞️ 🇮🇹

This repository contains the checkpoint for the [IT5 Base](https://huggingface.co/gsarti/it5-base) model fine-tuned on news summarization on the [Fanpage](https://huggingface.co/datasets/ARTeLab/fanpage) and [Il Post](https://huggingface.co/datasets/ARTeLab/ilpost) corpora as part of the experiments of the paper [IT5: Large-scale Text-to-text Pretraining for Italian Language Understanding and Generation](https://arxiv.org/abs/2203.03759) by [Gabriele Sarti](https://gsarti.com) and [Malvina Nissim](https://malvinanissim.github.io). 

A comprehensive overview of other released materials is provided in the [gsarti/it5](https://github.com/gsarti/it5) repository. Refer to the paper for additional details concerning the reported scores and the evaluation approach.

## Using the model

Model checkpoints are available for usage in Tensorflow, Pytorch and JAX. They can be used directly with pipelines as:

```python
from transformers import pipelines

newsum = pipeline("summarization", model='it5/it5-base-news-summarization')
newsum("Dal 31 maggio è infine partita la piattaforma ITsART, a più di un anno da quando – durante il primo lockdown – il ministro della Cultura Dario Franceschini ne aveva parlato come di «una sorta di Netflix della cultura», pensata per «offrire a tutto il mondo la cultura italiana a pagamento». È presto per dare giudizi definitivi sulla piattaforma, e di certo sarà difficile farlo anche più avanti senza numeri precisi. Al momento, l’unica cosa che si può fare è guardare com’è fatto il sito, contare quanti contenuti ci sono (circa 700 “titoli”, tra film, documentari, spettacoli teatrali e musicali e altri eventi) e provare a dare un giudizio sul loro valore e sulla loro varietà. Intanto, una cosa notata da più parti è che diversi contenuti di ITsART sono a pagamento sulla piattaforma sebbene altrove, per esempio su RaiPlay, siano invece disponibili gratuitamente.")
>>> [{"generated_text": "ITsART, la Netflix della cultura italiana, parte da maggio. Film, documentari, spettacoli teatrali e musicali disponibili sul nuovo sito a pagamento."}]
```

or loaded using autoclasses:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("it5/it5-base-news-summarization")
model = AutoModelForSeq2SeqLM.from_pretrained("it5/it5-base-news-summarization")
```

If you use this model in your research, please cite our work as:

```bibtex
@article{sarti-nissim-2022-it5,
    title={{IT5}: Large-scale Text-to-text Pretraining for Italian Language Understanding and Generation},
    author={Sarti, Gabriele and Nissim, Malvina},
    journal={ArXiv preprint 2203.03759},
    url={https://arxiv.org/abs/2203.03759},
    year={2022},
	month={mar}
}
```