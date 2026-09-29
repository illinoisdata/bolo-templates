---
metrics:
- precision - 0.9734840613846838
- recall - 0.9733370365227052
- f1 - 0.9732910950552367
- accuracy - 0.9733370365227052
pipeline_tag: text-classification
license: mit
datasets:
- hac541309/open-lid-dataset
language:
- en
- fr
- de
- es
- ar
- el
tags:
- detection
- classification
- language
- text
---
# Language Detection Model

A **BERT-based** language detection model trained on [hac541309/open-lid-dataset](https://huggingface.co/datasets/hac541309/open-lid-dataset), which includes **121 million sentences across 200 languages**. This model is optimized for **fast and accurate** language identification in text classification tasks.

## Model Details

- **Architecture**: [BertForSequenceClassification](https://huggingface.co/transformers/model_doc/bert.html)
- **Hidden Size**: 384  
- **Number of Layers**: 4  
- **Attention Heads**: 6  
- **Max Sequence Length**: 512  
- **Dropout**: 0.1  
- **Vocabulary Size**: 50,257  

## Training Process

- **Dataset**:
  - Used the [open-lid-dataset](https://huggingface.co/datasets/hac541309/open-lid-dataset)  
  - Split into train (90%) and test (10%)
- **Tokenizer**: A custom `BertTokenizerFast` with special tokens for `[UNK]`, `[CLS]`, `[SEP]`, `[PAD]`, `[MASK]`
- **Hyperparameters**:  
  - Learning Rate: 2e-5  
  - Batch Size: 256 (training) / 512 (testing)  
  - Epochs: 1  
  - Scheduler: Cosine  
- **Trainer**: Leveraged the Hugging Face [Trainer API](https://huggingface.co/docs/transformers/main_classes/trainer) with Weights & Biases for logging

## Data Augmentation

To improve model generalization and robustness, a **new text augmentation strategy** was introduced. This includes:

- **Removing digits** (random probability)
- **Shuffling words** to introduce variation
- **Removing words** selectively
- **Adding random digits** to simulate noise
- **Modifying punctuation** to handle different text formats

### Impact of Augmentation

Adding these augmentations **improved overall model performance**, as seen in the latest evaluation results:

## Evaluation

### Updated Performance Metrics:

- **Accuracy**: 0.9733  
- **Precision**: 0.9735  
- **Recall**: 0.9733  
- **F1 Score**: 0.9733  

### Detailed Evaluation (~12 millions texts)

|      |          support |   precision |   recall |       f1 |   size |
|:-----|-----------------:|------------:|---------:|---------:|-------:|
| Arab | 502886           |    0.908169 | 0.91335  | 0.909868 |     21 |
| Latn |      4.86532e+06 |    0.973172 | 0.972221 | 0.972646 |    125 |
| Ethi |  88564           |    0.996634 | 0.996459 | 0.996546 |      2 |
| Beng | 100502           |    0.995    | 0.992859 | 0.993915 |      3 |
| Deva | 260227           |    0.950405 | 0.942772 | 0.946355 |     10 |
| Cyrl | 510229           |    0.991342 | 0.989693 | 0.990513 |     12 |
| Tibt |  21863           |    0.992792 | 0.993665 | 0.993222 |      2 |
| Grek |  80445           |    0.998758 | 0.999391 | 0.999074 |      1 |
| Gujr |  53237           |    0.999981 | 0.999925 | 0.999953 |      1 |
| Hebr |  61576           |    0.996375 | 0.998904 | 0.997635 |      2 |
| Armn |  41146           |    0.999927 | 0.999927 | 0.999927 |      1 |
| Jpan |  53963           |    0.999147 | 0.998721 | 0.998934 |      1 |
| Knda |  40989           |    0.999976 | 0.999902 | 0.999939 |      1 |
| Geor |  43399           |    0.999977 | 0.999908 | 0.999942 |      1 |
| Khmr |  24348           |    1        | 0.999959 | 0.999979 |      1 |
| Hang |  66447           |    0.999759 | 0.999955 | 0.999857 |      1 |
| Laoo |  18353           |    1        | 0.999837 | 0.999918 |      1 |
| Mlym |  41899           |    0.999976 | 0.999976 | 0.999976 |      1 |
| Mymr |  62067           |    0.999898 | 0.999207 | 0.999552 |      2 |
| Orya |  27626           |    1        | 0.999855 | 0.999928 |      1 |
| Guru |  40856           |    1        | 0.999902 | 0.999951 |      1 |
| Olck |  13646           |    0.999853 | 1        | 0.999927 |      1 |
| Sinh |  41437           |    1        | 0.999952 | 0.999976 |      1 |
| Taml |  46832           |    0.999979 | 1        | 0.999989 |      1 |
| Tfng |  25238           |    0.849058 | 0.823968 | 0.823808 |      2 |
| Telu |  38251           |    1        | 0.999922 | 0.999961 |      1 |
| Thai |  51428           |    0.999922 | 0.999961 | 0.999942 |      1 |
| Hant |  94042           |    0.993966 | 0.995907 | 0.994935 |      2 |
| Hans |  57006           |    0.99007  | 0.986405 | 0.988234 |      1 |

### Comparison with Previous Performance

After introducing text augmentations, the model's performance improved on the same evaluation dataset, with accuracy increasing from 0.9695 to 0.9733, along with similar improvements in average precision, recall, and F1 score.

## Conclusion

The integration of **new text augmentation techniques** has led to a measurable improvement in model accuracy and robustness. These enhancements allow for better generalization across diverse language scripts, improving the model’s usability in real-world applications.


A detailed per-script classification report is also provided in the repository for further analysis.

---

### How to Use

You can quickly load and run inference with this model using the [Transformers pipeline](https://huggingface.co/docs/transformers/main_classes/pipelines):

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("alexneakameni/language_detection")
model = AutoModelForSequenceClassification.from_pretrained("alexneakameni/language_detection")

language_detection = pipeline("text-classification", model=model, tokenizer=tokenizer)

text = "Hello world!"
predictions = language_detection(text)
print(predictions)
```

This will output the predicted language code or label with the corresponding confidence score.

---

**Note**: The model’s performance may vary depending on text length, language variety, and domain-specific vocabulary. Always validate results against your own datasets for critical applications. 

For more information, see the [repository documentation](https://github.com/KameniAlexNea/learning_language). 

Thank you for using this model—feedback and contributions are welcome!