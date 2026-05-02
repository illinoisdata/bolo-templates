---
tags:
- summarization
- news
language: de
datasets:
- mlsum
widget:
- text: 'Wie geht man nach schrecklichen Ereignissen ambesten auf die Ängste und Sorgen von Kindern ein?Therapeuten haben eine klare Botschaft. Die Weltist voller Gefahren, Verbrechen und Schrecken -Krieg, Terrorismus, Umweltzerstörung und eben auchKindesmissbrauch. Soll man mit Kindern darüberreden, und wie? Die Antwort hängt auch vom Alterdes Kindes ab. Kinder, gerade kleine Kinder,brauchen Sicherheit, man muss sie nicht mitabstrakten Bedrohungen konfrontieren, die sieohnehin noch nicht ganz verstehen können. Ihreeigenen Ängste sollten Eltern lieber bei sichbehalten, raten Psychologen. Etwas anderes ist es,wenn Kinder schreckliche Ereignisse wie denaktuellen Fall in München mitbekommen. Dann sollteman natürlich auf die Ängste und Sorgen der Kindereingehen und mit ihnen sprechen. Man sollte aberklarmachen: Ja, es gibt kranke Menschen, die Bösestun, aber das ist die Ausnahme. Der Verbrecher istgefasst, er läuft nicht mehr frei herum,Polizisten passen auf. Die Botschaft sollte sein:Das ist nicht nah an dir dran, das bedroht dichnicht, empfehlen Familientherapeuten zum Umgangmit Ängsten von Kindern. Natürlich können auchVerhaltensregeln nicht schaden: Nein sagen, lautwerden und nicht mit Fremden mitgehen. AuchBilderbücher können helfen, solches Verhalten frühzu vermitteln, etwa "Das große und das kleineNein!" von Gisela Braun und Dorothee Wolters oder"Ich geh doch nicht mit Jedem mit!" von DagmarGeisler. Aber auch wenn jeder Vater, jede Mutterbeim Gedanken an derartige Verbrechen insSchlottern kommt: Die Statistik zeigt eindeutig,dass solche Fälle sehr selten sind.Kindesmissbrauch findet vor allem im nahensozialen Umfeld statt, in der Familie, in Vereinenoder bei älteren vermeintlichen "Freunden". Werseine Kinder davor beschützen will, muss ihnenzuhören, sie ernst nehmen, Fragen stellen, genauhinschauen.'
---

# German BERT2BERT fine-tuned on MLSUM DE for summarization


## Model
[bert-base-german-cased](https://huggingface.co/bert-base-german-cased) (BERT Checkpoint)
## Dataset
**MLSUM** is the first large-scale MultiLingual SUMmarization dataset. Obtained from online newspapers, it contains 1.5M+ article/summary pairs in five different languages -- namely, French, **German**, Spanish, Russian, Turkish. Together with English newspapers from the popular CNN/Daily mail dataset, the collected data form a large scale multilingual dataset which can enable new research directions for the text summarization community. We report cross-lingual comparative analyses based on state-of-the-art systems. These highlight existing biases which motivate the use of a multi-lingual dataset.
[MLSUM de](https://huggingface.co/datasets/viewer/?dataset=mlsum)
## Results
|Set|Metric| # Score|
|----|------|------|
| Test  |Rouge2 - mid -precision | **33.04**|
| Test | Rouge2 - mid - recall | **33.83**|
| Test | Rouge2 - mid - fmeasure | **33.15**|
## Usage
 ```python
 import torch
 from transformers import BertTokenizerFast, EncoderDecoderModel
 device = 'cuda' if torch.cuda.is_available() else 'cpu'
 ckpt = 'mrm8488/bert2bert_shared-german-finetuned-summarization'
 tokenizer = BertTokenizerFast.from_pretrained(ckpt)
model = EncoderDecoderModel.from_pretrained(ckpt).to(device)
def generate_summary(text):
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)
    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)
    
text = "Your text here..."

generate_summary(text)

```
> Created by [Manuel Romero/@mrm8488](https://twitter.com/mrm8488) with the support of [Narrativa](https://www.narrativa.com/)
> Made with <span style="color: #e25555;">&hearts;</span> in Spain