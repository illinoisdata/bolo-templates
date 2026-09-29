---
license: mit
tags:
- generated_from_trainer
base_model: camembert-base
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: french_emotion_camembert
  results: []
language:
- fr
---


# french_emotion_camembert

This model, french_emotion_camembert, is a fine-tuned version of the [camembert-base](https://huggingface.co/camembert-base) transformer model, adapted specifically for emotion classification in French text. The original camembert-base model, which is extensively trained on a diverse range of French text from the Allociné dataset, has been repurposed and further trained on an enriched dataset tailored to capture a spectrum of emotional responses.
It achieves the following results on the evaluation set:
- Loss: 0.5368
- Accuracy: 0.8295
- Precision: 0.8265
- Recall: 0.8295
- F1: 0.8269

## Model description

This model, fine-tuned on CamemBERT, is designed for the specific task of emotion classification from text. It aims to classify text inputs into various emotional categories such as joy, sadness, anger, etc., based on the dataset it was trained on. The fine-tuning process has optimized the model for better understanding and processing of French language texts.
## Intended uses & limitations

Intended Uses

This model is intended for use in applications involving the classification of emotions in French text. Suitable applications include:

Sentiment Analysis: Analyzing customer feedback, user reviews, or any form of user-generated content to gauge the prevailing emotional tones.
Content Moderation: Assisting in the moderation of text to flag potentially harmful content based on the emotional tone.
Market Research: Understanding consumer sentiments in different market segments by analyzing social media posts, comments, or discussions.
Human-Computer Interaction: Enhancing user interfaces that adapt dynamically based on the emotional context of user inputs.
The model is designed to be used by developers, data scientists, or researchers who are working on natural language processing tasks that require emotion detection in French-language text.

Limitations

While the model has been trained to perform well across various texts, it has several limitations:

Language Specificity: The model is trained on French text and may not perform well on texts in other languages.
Contextual Understanding: It may misinterpret texts where emotions are implied rather than explicitly expressed, due to the subtleties and complexities of human emotions.
Training Data Bias: The training data may not encompass a sufficiently wide variety of text sources, which can lead to biased predictions against certain demographics or topics.
Ethical Considerations: Care should be taken when using the model in scenarios where misclassification of emotional tone could lead to adverse consequences, such as filtering content in sensitive contexts.
Generalization: The model may not generalize well to very different or specialized domains or jargons not well represented in the training data.
Recommended Precautions

## Modal architecture

The model is based on the CamemBERT architecture, which is itself a variant of the BERT model adapted for French text. CamemBERT is a transformer-based model that has shown state-of-the-art performance on a range of natural language processing tasks in French.

## Training and evaluation data

The model was trained on a custom dataset comprising several thousand French language reviews, labeled with emotions. Each text was manually annotated to reflect one of six emotional states, which include but are not limited to disgust, sadness, and happiness.

## Training procedure

Preprocessing: Text inputs were cleaned and preprocessed to remove any non-relevant characters and tokenized using CamemBERT’s default tokenizer.
Configuration: The model was trained with a batch size of 16, using a learning rate of 2e-5 with the Adam optimizer. Training was conducted for 3 epochs to avoid overfitting.
Environment: Training was performed on a single GPU setup, ensuring efficient use of resources.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Example of USE

Here's a Python snippet demonstrating how to use this model:

from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "your_huggingface_username/french_emotion_camembert"
tokenizer = AutoTokenizer.from_pretrained(model_answer)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Je suis très heureux de votre service rapide et efficace."
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
outputs = model(**inputs)

# Decode and print the predicted emotion
prediction = torch.nn.functional.softmax(outputs.logits, dim=-1)
predicted_emotion = prediction.argmax().item()
print("Predicted emotion:", predicted_emotion)

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.5249        | 1.0   | 2825 | 0.4866          | 0.8196   | 0.8079    | 0.8196 | 0.8073 |
| 0.3751        | 2.0   | 5650 | 0.4891          | 0.8215   | 0.8222    | 0.8215 | 0.8210 |
| 0.2689        | 3.0   | 8475 | 0.5368          | 0.8295   | 0.8265    | 0.8295 | 0.8269 |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.19.2
- Tokenizers 0.19.1