---
language: "eng"
tags:
- wikihow
- t5-small
- pytorch
- lm-head
- seq2seq
- t5
- pipeline:summarization
- summarization
datasets:
- Wikihow 
widget:
- text: "Lack of fluids can lead to dry mouth, which is a leading cause of bad breath. Water
can also dilute any chemicals in your mouth or gut that are causing bad breath., Studies show that
eating 6 ounces of yogurt a day reduces the level of odor-causing compounds in the mouth. In
particular, look for yogurt containing the active bacteria Streptococcus thermophilus or
Lactobacillus bulgaricus., The abrasive nature of fibrous fruits and vegetables helps to clean
teeth, while the vitamins, antioxidants, and acids they contain improve dental health.Foods that can
be particularly helpful include:Apples — Apples contain vitamin C, which is necessary for health
gums, as well as malic acid, which helps to whiten teeth.Carrots — Carrots are rich in vitamin A,
which strengthens tooth enamel.Celery — Chewing celery produces a lot of saliva, which helps to
neutralize bacteria that cause bad breath.Pineapples — Pineapples contain bromelain, an enzyme that
cleans the mouth., These teas have been shown to kill the bacteria that cause bad breath and
plaque., An upset stomach can lead to burping, which contributes to bad breath. Don’t eat foods that
upset your stomach, or if you do, use antacids. If you are lactose intolerant, try lactase tablets.,
They can all cause bad breath. If you do eat them, bring sugar-free gum or a toothbrush and
toothpaste to freshen your mouth afterwards., Diets low in carbohydrates lead to ketosis — a state
in which the body burns primarily fat instead of carbohydrates for energy. This may be good for your
waistline, but it also produces chemicals called ketones, which contribute to bad breath.To stop the
problem, you must change your diet. Or, you can combat the smell in one of these ways:Drink lots of
water to dilute the ketones.Chew sugarless gum or suck on sugarless mints.Chew mint leaves."
- text: " Bring 1/2 cup water to the boil.Add the fresh or dried rosemary to the water.Remove
from the heat. Set aside for 1/2 an hour to infuse. Added flavour can be released by pressing down
on the rosemary leaves with a spoon. Add the pieces to the blender or food processor with the
elderflower cordial. Blend or process to a purée.,, Add the lemon or lime juice and stir to
combine., Add a cover and place in the freezer.After 2 hours, remove from the freezer and break up
with a fork. This helps the ice crystals to form properly.Continue doing this every hour until the
granita freezes properly. Scoop the granita into dessert bowls and serve. Garnish with a cucumber
curl or a small sprig of rosemary."
metrics:
- Rouge1: 31.2
- RougeL: 24.5
---

# Model name
Wikihow T5-small

## Model description

This is a T5-small model trained on Wikihow All data set. The model was trained for 3 epochs using a batch size of 16 and learning rate of 3e-4. Max_input_lngth is set as 512 and max_output_length is 150. Model attained a Rouge1 score of 31.2 and RougeL score of 24.5. 
We have written a blog post that covers the training procedure. Please find it [here](https://medium.com/@priya.dwivedi/fine-tuning-a-t5-transformer-for-any-summarization-task-82334c64c81). 

## Usage

```
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("deep-learning-analytics/wikihow-t5-small")
model = AutoModelWithLMHead.from_pretrained("deep-learning-analytics/wikihow-t5-small")

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = model.to(device)

text = """"
Lack of fluids can lead to dry mouth, which is a leading cause of bad breath. Water
can also dilute any chemicals in your mouth or gut that are causing bad breath., Studies show that
eating 6 ounces of yogurt a day reduces the level of odor-causing compounds in the mouth. In
particular, look for yogurt containing the active bacteria Streptococcus thermophilus or
Lactobacillus bulgaricus., The abrasive nature of fibrous fruits and vegetables helps to clean
teeth, while the vitamins, antioxidants, and acids they contain improve dental health.Foods that can
be particularly helpful include:Apples — Apples contain vitamin C, which is necessary for health
gums, as well as malic acid, which helps to whiten teeth.Carrots — Carrots are rich in vitamin A,
which strengthens tooth enamel.Celery — Chewing celery produces a lot of saliva, which helps to
neutralize bacteria that cause bad breath.Pineapples — Pineapples contain bromelain, an enzyme that
cleans the mouth., These teas have been shown to kill the bacteria that cause bad breath and
plaque., An upset stomach can lead to burping, which contributes to bad breath. Don’t eat foods that
upset your stomach, or if you do, use antacids. If you are lactose intolerant, try lactase tablets.,
They can all cause bad breath. If you do eat them, bring sugar-free gum or a toothbrush and
toothpaste to freshen your mouth afterwards., Diets low in carbohydrates lead to ketosis — a state
in which the body burns primarily fat instead of carbohydrates for energy. This may be good for your
waistline, but it also produces chemicals called ketones, which contribute to bad breath.To stop the
problem, you must change your diet. Or, you can combat the smell in one of these ways:Drink lots of
water to dilute the ketones.Chew sugarless gum or suck on sugarless mints.Chew mint leaves.
"""

preprocess_text = text.strip().replace("\n","")
tokenized_text = tokenizer.encode(preprocess_text, return_tensors="pt").to(device)

summary_ids = model.generate(
            tokenized_text,
            max_length=150, 
            num_beams=2,
            repetition_penalty=2.5, 
            length_penalty=1.0, 
            early_stopping=True
        )

output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print ("\n\nSummarized text: \n",output)
```