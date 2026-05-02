---
tags:
- summarization
- news
language: fr
datasets:
- mlsum
widget:
- text: "Un nuage de fumée juste après l’explosion, le 1er juin 2019. Une déflagration dans une importante usine d’explosifs du centre de la Russie a fait au moins 79 blessés samedi 1er juin. L’explosion a eu lieu dans l’usine Kristall à Dzerzhinsk, une ville située à environ 400 kilomètres à l’est de Moscou, dans la région de Nijni-Novgorod. « Il y a eu une explosion technique dans l’un des ateliers, suivie d’un incendie qui s’est propagé sur une centaine de mètres carrés », a expliqué un porte-parole des services d’urgence. Des images circulant sur les réseaux sociaux montraient un énorme nuage de fumée après l’explosion. Cinq bâtiments de l’usine et près de 180 bâtiments résidentiels ont été endommagés par l’explosion, selon les autorités municipales. Une enquête pour de potentielles violations des normes de sécurité a été ouverte. Fragments de shrapnel Les blessés ont été soignés après avoir été atteints par des fragments issus de l’explosion, a précisé une porte-parole des autorités sanitaires citée par Interfax. « Nous parlons de blessures par shrapnel d’une gravité moyenne et modérée », a-t-elle précisé. Selon des représentants de Kristall, cinq personnes travaillaient dans la zone où s’est produite l’explosion. Elles ont pu être évacuées en sécurité. Les pompiers locaux ont rapporté n’avoir aucune information sur des personnes qui se trouveraient encore dans l’usine."
---
# French RoBERTa2RoBERTa (shared) fine-tuned on MLSUM FR for summarization
## Model
[camembert-base](https://huggingface.co/camembert-base) (RoBERTa Checkpoint)
## Dataset
**MLSUM** is the first large-scale MultiLingual SUMmarization dataset. Obtained from online newspapers, it contains 1.5M+ article/summary pairs in five different languages -- namely, **French**, German, Spanish, Russian, Turkish. Together with English newspapers from the popular CNN/Daily mail dataset, the collected data form a large scale multilingual dataset which can enable new research directions for the text summarization community. We report cross-lingual comparative analyses based on state-of-the-art systems. These highlight existing biases which motivate the use of a multi-lingual dataset.
[MLSUM fr](https://huggingface.co/datasets/viewer/?dataset=mlsum)
## Results
|Set|Metric| # Score|
|----|------|------|
| Test  |Rouge2 - mid -precision | **14.47**|
| Test | Rouge2 - mid - recall | **12.90**|
| Test | Rouge2 - mid - fmeasure | **13.30**|
## Usage
 ```python
 import torch
 from transformers import RobertaTokenizerFast, EncoderDecoderModel
 device = 'cuda' if torch.cuda.is_available() else 'cpu'
 ckpt = 'mrm8488/camembert2camembert_shared-finetuned-french-summarization'
 tokenizer = RobertaTokenizerFast.from_pretrained(ckpt)
model = EncoderDecoderModel.from_pretrained(ckpt).to(device)
def generate_summary(text):
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)
    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)
    
text = "Un nuage de fumée juste après l’explosion, le 1er juin 2019. Une déflagration dans une importante usine d’explosifs du centre de la Russie a fait au moins 79 blessés samedi 1er juin. L’explosion a eu lieu dans l’usine Kristall à Dzerzhinsk, une ville située à environ 400 kilomètres à l’est de Moscou, dans la région de Nijni-Novgorod. « Il y a eu une explosion technique dans l’un des ateliers, suivie d’un incendie qui s’est propagé sur une centaine de mètres carrés », a expliqué un porte-parole des services d’urgence. Des images circulant sur les réseaux sociaux montraient un énorme nuage de fumée après l’explosion. Cinq bâtiments de l’usine et près de 180 bâtiments résidentiels ont été endommagés par l’explosion, selon les autorités municipales. Une enquête pour de potentielles violations des normes de sécurité a été ouverte. Fragments de shrapnel Les blessés ont été soignés après avoir été atteints par des fragments issus de l’explosion, a précisé une porte-parole des autorités sanitaires citée par Interfax. « Nous parlons de blessures par shrapnel d’une gravité moyenne et modérée », a-t-elle précisé. Selon des représentants de Kristall, cinq personnes travaillaient dans la zone où s’est produite l’explosion. Elles ont pu être évacuées en sécurité. Les pompiers locaux ont rapporté n’avoir aucune information sur des personnes qui se trouveraient encore dans l’usine."

generate_summary(text)

# Output: L’explosion a eu lieu dans l’usine Kristall à Dzerzhinsk, une ville située à environ 400 kilomètres à l’est de Moscou.

```
> Created by [Manuel Romero/@mrm8488](https://twitter.com/mrm8488) with the support of [Narrativa](https://www.narrativa.com/)
> Made with <span style="color: #e25555;">&hearts;</span> in Spain