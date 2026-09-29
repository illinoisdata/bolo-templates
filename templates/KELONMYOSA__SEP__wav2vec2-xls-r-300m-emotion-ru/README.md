---
license: apache-2.0
datasets:
- KELONMYOSA/dusha_emotion_audio
language:
- ru
pipeline_tag: audio-classification
tags:
  - audio
  - audio-classification
metrics:
- accuracy
widget:
- example_title: Emotion - "Neurtal"
  src: https://huggingface.co/KELONMYOSA/wav2vec2-xls-r-300m-emotion-ru/resolve/main/neutral.mp3
- example_title: Emotion - "Positive"
  src: https://huggingface.co/KELONMYOSA/wav2vec2-xls-r-300m-emotion-ru/resolve/main/positive.mp3
- example_title: Emotion - "Angry"
  src: https://huggingface.co/KELONMYOSA/wav2vec2-xls-r-300m-emotion-ru/resolve/main/angry.mp3
- example_title: Emotion - "Sad"
  src: https://huggingface.co/KELONMYOSA/wav2vec2-xls-r-300m-emotion-ru/resolve/main/sad.mp3
- example_title: Emotion - "Other"
  src: https://huggingface.co/KELONMYOSA/wav2vec2-xls-r-300m-emotion-ru/resolve/main/other.mp3
---

# Speech Emotion Recognition

The model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) for a Speech Emotion Recognition (SER) task.

The dataset used to fine-tune the original pre-trained model is the [DUSHA dataset](https://huggingface.co/datasets/KELONMYOSA/dusha_emotion_audio). The dataset consists of about 125 000 audio recordings in Russian with four basic emotions that usually appear in a dialog with a virtual assistant: Happiness (Positive), Sadness, Anger and Neutral emotion.

```python
emotions = ['neutral', 'positive', 'angry', 'sad', 'other']
```

# How to use
## Pipeline
```python
from transformers.pipelines import pipeline

pipe = pipeline(model="KELONMYOSA/wav2vec2-xls-r-300m-emotion-ru", trust_remote_code=True)

# The pipeline input can be a file, path or link
result = pipe("speech.wav")
print(result)
```
~~~
[{'label': 'neutral', 'score': 0.00318}, {'label': 'positive', 'score': 0.00376}, {'label': 'sad', 'score': 0.00145}, {'label': 'angry', 'score': 0.98984}, {'label': 'other', 'score': 0.00176}]
~~~
## AutoModel
```python
import librosa
import torch
import torch.nn.functional as F
from transformers import AutoConfig, Wav2Vec2Processor, AutoModelForAudioClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name_or_path = "KELONMYOSA/wav2vec2-xls-r-300m-emotion-ru"
config = AutoConfig.from_pretrained(model_name_or_path)
processor = Wav2Vec2Processor.from_pretrained(model_name_or_path)
sampling_rate = processor.feature_extractor.sampling_rate
model = AutoModelForAudioClassification.from_pretrained(model_name_or_path, trust_remote_code=True).to(device)


def predict(path):
    speech, sr = librosa.load(path, sr=sampling_rate)
    features = processor(speech, sampling_rate=sampling_rate, return_tensors="pt", padding=True)

    input_values = features.input_values.to(device)
    attention_mask = features.attention_mask.to(device)

    with torch.no_grad():
        logits = model(input_values, attention_mask=attention_mask).logits

    scores = F.softmax(logits, dim=1).detach().cpu().numpy()[0]
    outputs = [{"label": config.id2label[i], "score": round(score, 5)} for i, score in
               enumerate(scores)]
    return outputs


print(predict("speech.wav"))
```
~~~
[{'label': 'neutral', 'score': 0.00318}, {'label': 'positive', 'score': 0.00376}, {'label': 'sad', 'score': 0.00145}, {'label': 'angry', 'score': 0.98984}, {'label': 'other', 'score': 0.00176}]
~~~
# Evaluation

It achieves the following results:
- Training Loss: 0.528700
- Validation Loss: 0.349617
- Accuracy: 0.901369

| emotion      | precision | recall | f1-score | support |
|--------------|:---------:|:------:|:--------:|:-------:|
| neutral      | 0.92      | 0.94   | 0.93     | 15886   |
| positive     | 0.85      | 0.79   | 0.82     | 2481    |
| sad          | 0.77      | 0.82   | 0.79     | 2506    |
| angry        | 0.89      | 0.83   | 0.86     | 3072    |
| other        | 0.99      | 0.74   | 0.85     | 226     |
|              |           |        |          |         |
| accuracy     |           |        | 0.90     | 24171   |
| macro avg    | 0.89      | 0.82   | 0.85     | 24171   |
| weighted avg | 0.90      | 0.90   | 0.90     | 24171   |