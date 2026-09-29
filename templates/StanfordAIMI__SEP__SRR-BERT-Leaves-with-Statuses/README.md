Usage:
```python
import json
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from datasets import load_dataset
import requests

# Configuration
MODEL_PATH = "StanfordAIMI/SRR-BERT-Leaves-with-Statuses"
MAPPING_URL = "https://raw.githubusercontent.com/jbdel/StructEval/refs/heads/main/structeval/leaves_with_statuses_mapping.json"
MAX_LENGTH = 128
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Fetch mapping from GitHub
resp = requests.get(MAPPING_URL)
resp.raise_for_status()
label_map = resp.json()
idx2label = {v: k for k, v in label_map.items()}

# Load tokenizer & model
tokenizer = BertTokenizer.from_pretrained("microsoft/BiomedVLP-CXR-BERT-general")
model = BertForSequenceClassification.from_pretrained(MODEL_PATH, num_labels=len(label_map))
model.to(DEVICE).eval()

# Grab one test sentence
dataset = load_dataset("StanfordAIMI/StructUtterances", split="test_reviewed")
sentence = dataset[35]["utterance"]

# Tokenize and infer
inputs = tokenizer(
    sentence,
    padding="max_length",
    truncation=True,
    max_length=MAX_LENGTH,
    return_tensors="pt"
).to(DEVICE)

with torch.no_grad():
    logits = model(**inputs).logits
    preds = (torch.sigmoid(logits)[0].cpu().numpy() > 0.5).astype(int)

pred_labels = [idx2label[i] for i, flag in enumerate(preds) if flag]

print(f"Sentence: {sentence}")
print("Predicted labels:", pred_labels)
```

Output:
```
Sentence: Patchy consolidation in the left retrocardiac area, suggestive of atelectasis or early airspace disease.
Predicted labels: ['Atelectasis (Uncertain)', 'Air space opacity–multifocal (Uncertain)']
```


Label Mapping:
```{
  "Lung Lesion (Present)": 0,
  "Edema (Present)": 1,
  "Pneumonia (Present)": 2,
  "Atelectasis (Present)": 3,
  "Aspiration (Present)": 4,
  "Lung collapse (Present)": 5,
  "Perihilar airspace opacity (Present)": 6,
  "Air space opacity\u2013multifocal (Present)": 7,
  "Mass/Solitary lung mass (Present)": 8,
  "Nodule/Solitary lung nodule (Present)": 9,
  "Cavitating mass with content (Present)": 10,
  "Cavitating masses (Present)": 11,
  "Emphysema (Present)": 12,
  "Fibrosis (Present)": 13,
  "Pulmonary congestion (Present)": 14,
  "Hilar lymphadenopathy (Present)": 15,
  "Bronchiectasis (Present)": 16,
  "Simple pneumothorax (Present)": 17,
  "Loculated pneumothorax (Present)": 18,
  "Tension pneumothorax (Present)": 19,
  "Simple pleural effusion (Present)": 20,
  "Loculated pleural effusion (Present)": 21,
  "Pleural scarring (Present)": 22,
  "Hydropneumothorax (Present)": 23,
  "Pleural Other (Present)": 24,
  "Cardiomegaly (Present)": 25,
  "Pericardial effusion (Present)": 26,
  "Inferior mediastinal mass (Present)": 27,
  "Superior mediastinal mass (Present)": 28,
  "Tortuous Aorta (Present)": 29,
  "Calcification of the Aorta (Present)": 30,
  "Enlarged pulmonary artery (Present)": 31,
  "Hernia (Present)": 32,
  "Pneumomediastinum (Present)": 33,
  "Tracheal deviation (Present)": 34,
  "Acute humerus fracture (Present)": 35,
  "Acute rib fracture (Present)": 36,
  "Acute clavicle fracture (Present)": 37,
  "Acute scapula fracture (Present)": 38,
  "Compression fracture (Present)": 39,
  "Shoulder dislocation (Present)": 40,
  "Subcutaneous Emphysema (Present)": 41,
  "Suboptimal central line (Present)": 42,
  "Suboptimal endotracheal tube (Present)": 43,
  "Suboptimal nasogastric tube (Present)": 44,
  "Suboptimal pulmonary arterial catheter (Present)": 45,
  "Pleural tube (Present)": 46,
  "PICC line (Present)": 47,
  "Port catheter (Present)": 48,
  "Pacemaker (Present)": 49,
  "Implantable defibrillator (Present)": 50,
  "LVAD (Present)": 51,
  "Intraaortic balloon pump (Present)": 52,
  "Pneumoperitoneum (Present)": 53,
  "Lung Lesion (Uncertain)": 54,
  "Edema (Uncertain)": 55,
  "Pneumonia (Uncertain)": 56,
  "Atelectasis (Uncertain)": 57,
  "Aspiration (Uncertain)": 58,
  "Lung collapse (Uncertain)": 59,
  "Perihilar airspace opacity (Uncertain)": 60,
  "Air space opacity\u2013multifocal (Uncertain)": 61,
  "Mass/Solitary lung mass (Uncertain)": 62,
  "Nodule/Solitary lung nodule (Uncertain)": 63,
  "Cavitating mass with content (Uncertain)": 64,
  "Cavitating masses (Uncertain)": 65,
  "Emphysema (Uncertain)": 66,
  "Fibrosis (Uncertain)": 67,
  "Pulmonary congestion (Uncertain)": 68,
  "Hilar lymphadenopathy (Uncertain)": 69,
  "Bronchiectasis (Uncertain)": 70,
  "Simple pneumothorax (Uncertain)": 71,
  "Loculated pneumothorax (Uncertain)": 72,
  "Tension pneumothorax (Uncertain)": 73,
  "Simple pleural effusion (Uncertain)": 74,
  "Loculated pleural effusion (Uncertain)": 75,
  "Pleural scarring (Uncertain)": 76,
  "Hydropneumothorax (Uncertain)": 77,
  "Pleural Other (Uncertain)": 78,
  "Cardiomegaly (Uncertain)": 79,
  "Pericardial effusion (Uncertain)": 80,
  "Inferior mediastinal mass (Uncertain)": 81,
  "Superior mediastinal mass (Uncertain)": 82,
  "Tortuous Aorta (Uncertain)": 83,
  "Calcification of the Aorta (Uncertain)": 84,
  "Enlarged pulmonary artery (Uncertain)": 85,
  "Hernia (Uncertain)": 86,
  "Pneumomediastinum (Uncertain)": 87,
  "Tracheal deviation (Uncertain)": 88,
  "Acute humerus fracture (Uncertain)": 89,
  "Acute rib fracture (Uncertain)": 90,
  "Acute clavicle fracture (Uncertain)": 91,
  "Acute scapula fracture (Uncertain)": 92,
  "Compression fracture (Uncertain)": 93,
  "Shoulder dislocation (Uncertain)": 94,
  "Subcutaneous Emphysema (Uncertain)": 95,
  "Suboptimal central line (Uncertain)": 96,
  "Suboptimal endotracheal tube (Uncertain)": 97,
  "Suboptimal nasogastric tube (Uncertain)": 98,
  "Suboptimal pulmonary arterial catheter (Uncertain)": 99,
  "Pleural tube (Uncertain)": 100,
  "PICC line (Uncertain)": 101,
  "Port catheter (Uncertain)": 102,
  "Pacemaker (Uncertain)": 103,
  "Implantable defibrillator (Uncertain)": 104,
  "LVAD (Uncertain)": 105,
  "Intraaortic balloon pump (Uncertain)": 106,
  "Pneumoperitoneum (Uncertain)": 107,
  "Lung Lesion (Absent)": 108,
  "Edema (Absent)": 109,
  "Pneumonia (Absent)": 110,
  "Atelectasis (Absent)": 111,
  "Aspiration (Absent)": 112,
  "Lung collapse (Absent)": 113,
  "Perihilar airspace opacity (Absent)": 114,
  "Air space opacity\u2013multifocal (Absent)": 115,
  "Mass/Solitary lung mass (Absent)": 116,
  "Nodule/Solitary lung nodule (Absent)": 117,
  "Cavitating mass with content (Absent)": 118,
  "Cavitating masses (Absent)": 119,
  "Emphysema (Absent)": 120,
  "Fibrosis (Absent)": 121,
  "Pulmonary congestion (Absent)": 122,
  "Hilar lymphadenopathy (Absent)": 123,
  "Bronchiectasis (Absent)": 124,
  "Simple pneumothorax (Absent)": 125,
  "Loculated pneumothorax (Absent)": 126,
  "Tension pneumothorax (Absent)": 127,
  "Simple pleural effusion (Absent)": 128,
  "Loculated pleural effusion (Absent)": 129,
  "Pleural scarring (Absent)": 130,
  "Hydropneumothorax (Absent)": 131,
  "Pleural Other (Absent)": 132,
  "Cardiomegaly (Absent)": 133,
  "Pericardial effusion (Absent)": 134,
  "Inferior mediastinal mass (Absent)": 135,
  "Superior mediastinal mass (Absent)": 136,
  "Tortuous Aorta (Absent)": 137,
  "Calcification of the Aorta (Absent)": 138,
  "Enlarged pulmonary artery (Absent)": 139,
  "Hernia (Absent)": 140,
  "Pneumomediastinum (Absent)": 141,
  "Tracheal deviation (Absent)": 142,
  "Acute humerus fracture (Absent)": 143,
  "Acute rib fracture (Absent)": 144,
  "Acute clavicle fracture (Absent)": 145,
  "Acute scapula fracture (Absent)": 146,
  "Compression fracture (Absent)": 147,
  "Shoulder dislocation (Absent)": 148,
  "Subcutaneous Emphysema (Absent)": 149,
  "Suboptimal central line (Absent)": 150,
  "Suboptimal endotracheal tube (Absent)": 151,
  "Suboptimal nasogastric tube (Absent)": 152,
  "Suboptimal pulmonary arterial catheter (Absent)": 153,
  "Pleural tube (Absent)": 154,
  "PICC line (Absent)": 155,
  "Port catheter (Absent)": 156,
  "Pacemaker (Absent)": 157,
  "Implantable defibrillator (Absent)": 158,
  "LVAD (Absent)": 159,
  "Intraaortic balloon pump (Absent)": 160,
  "Pneumoperitoneum (Absent)": 161,
  "No Finding": 162
}
```

Classification Report:
```
                                                    precision    recall  f1-score   support

                             Lung Lesion (Present)       0.68      0.57      0.62       207
                                   Edema (Present)       0.94      0.94      0.94      5563
                               Pneumonia (Present)       0.84      0.76      0.80      2149
                             Atelectasis (Present)       0.91      0.92      0.92      9074
                              Aspiration (Present)       0.83      0.78      0.80        87
                           Lung collapse (Present)       0.86      0.86      0.86       792
              Perihilar airspace opacity (Present)       0.76      0.73      0.74       819
            Air space opacity-multifocal (Present)       0.71      0.78      0.74      2561
                 Mass/Solitary lung mass (Present)       0.89      0.91      0.90       716
             Nodule/Solitary lung nodule (Present)       0.92      0.82      0.87      1326
            Cavitating mass with content (Present)       0.88      0.89      0.89        83
                       Cavitating masses (Present)       0.81      0.65      0.72        40
                               Emphysema (Present)       0.87      0.95      0.91      1434
                                Fibrosis (Present)       0.87      0.75      0.81      1188
                    Pulmonary congestion (Present)       0.86      0.92      0.89      1746
                   Hilar lymphadenopathy (Present)       0.86      0.84      0.85       359
                          Bronchiectasis (Present)       0.96      0.97      0.96       352
                     Simple pneumothorax (Present)       0.98      0.98      0.98      2616
                  Loculated pneumothorax (Present)       0.66      0.94      0.78        88
                    Tension pneumothorax (Present)       0.83      0.87      0.85        39
                 Simple pleural effusion (Present)       0.96      0.98      0.97     11496
              Loculated pleural effusion (Present)       0.93      0.91      0.92       887
                        Pleural scarring (Present)       0.86      0.89      0.87      1733
                       Hydropneumothorax (Present)       0.96      0.99      0.97       341
                           Pleural Other (Present)       0.68      0.41      0.51       115
                            Cardiomegaly (Present)       0.97      0.97      0.97      4178
                    Pericardial effusion (Present)       0.81      0.95      0.87        55
               Inferior mediastinal mass (Present)       0.29      0.12      0.17        16
               Superior mediastinal mass (Present)       0.80      0.81      0.80       121
                          Tortuous Aorta (Present)       0.90      0.96      0.93      1514
              Calcification of the Aorta (Present)       0.96      0.94      0.95      1389
               Enlarged pulmonary artery (Present)       0.88      0.93      0.90       297
                                  Hernia (Present)       0.95      0.93      0.94       499
                       Pneumomediastinum (Present)       0.87      0.97      0.92       167
                      Tracheal deviation (Present)       0.80      0.91      0.85       400
                  Acute humerus fracture (Present)       0.85      0.97      0.90        88
                      Acute rib fracture (Present)       0.94      0.93      0.94       968
                 Acute clavicle fracture (Present)       0.89      0.96      0.92       175
                  Acute scapula fracture (Present)       0.92      0.96      0.94        56
                    Compression fracture (Present)       0.78      0.97      0.86       677
                    Shoulder dislocation (Present)       0.77      0.89      0.83        38
                  Subcutaneous Emphysema (Present)       0.98      0.99      0.98      1050
                 Suboptimal central line (Present)       0.72      0.20      0.31       246
            Suboptimal endotracheal tube (Present)       0.57      0.76      0.65       872
             Suboptimal nasogastric tube (Present)       0.58      0.41      0.48       691
  Suboptimal pulmonary arterial catheter (Present)       0.20      0.02      0.03        65
                            Pleural tube (Present)       0.62      0.70      0.66      1432
                               PICC line (Present)       0.72      0.92      0.81      2207
                           Port catheter (Present)       0.74      0.56      0.64       685
                               Pacemaker (Present)       0.82      0.90      0.86      2178
               Implantable defibrillator (Present)       0.65      0.73      0.69       515
                                    LVAD (Present)       0.81      0.82      0.81       127
                Intraaortic balloon pump (Present)       0.77      0.96      0.85       116
                        Pneumoperitoneum (Present)       0.92      0.96      0.94       217
                           Lung Lesion (Uncertain)       0.62      0.36      0.45       319
                                 Edema (Uncertain)       0.89      0.89      0.89      3348
                             Pneumonia (Uncertain)       0.88      0.92      0.90     10935
                           Atelectasis (Uncertain)       0.93      0.90      0.91      8325
                            Aspiration (Uncertain)       0.98      0.99      0.99      2437
                         Lung collapse (Uncertain)       0.82      0.71      0.76       270
            Perihilar airspace opacity (Uncertain)       0.70      0.34      0.46       614
          Air space opacity-multifocal (Uncertain)       0.70      0.50      0.58      2222
               Mass/Solitary lung mass (Uncertain)       0.82      0.82      0.82       458
           Nodule/Solitary lung nodule (Uncertain)       0.85      0.88      0.86      1323
          Cavitating mass with content (Uncertain)       0.88      0.84      0.86        76
                     Cavitating masses (Uncertain)       0.60      0.21      0.32        14
                             Emphysema (Uncertain)       0.85      0.65      0.74       494
                              Fibrosis (Uncertain)       0.79      0.65      0.71      1235
                  Pulmonary congestion (Uncertain)       0.79      0.65      0.72      1044
                 Hilar lymphadenopathy (Uncertain)       0.86      0.80      0.83       770
                        Bronchiectasis (Uncertain)       0.96      0.77      0.85       125
                   Simple pneumothorax (Uncertain)       0.93      0.89      0.91       542
                Loculated pneumothorax (Uncertain)       0.96      0.80      0.88        61
                  Tension pneumothorax (Uncertain)       0.83      0.77      0.80        13
               Simple pleural effusion (Uncertain)       0.93      0.87      0.90      3668
            Loculated pleural effusion (Uncertain)       0.89      0.77      0.83       254
                      Pleural scarring (Uncertain)       0.83      0.86      0.84      1365
                     Hydropneumothorax (Uncertain)       0.84      0.67      0.74        39
                         Pleural Other (Uncertain)       0.84      0.51      0.63       260
                          Cardiomegaly (Uncertain)       0.84      0.75      0.79      1155
                  Pericardial effusion (Uncertain)       0.94      0.94      0.94       262
             Inferior mediastinal mass (Uncertain)       0.79      0.44      0.56        62
             Superior mediastinal mass (Uncertain)       0.73      0.79      0.76       382
                        Tortuous Aorta (Uncertain)       0.75      0.86      0.80       269
            Calcification of the Aorta (Uncertain)       0.73      0.37      0.49       145
             Enlarged pulmonary artery (Uncertain)       0.75      0.87      0.81       189
                                Hernia (Uncertain)       0.94      0.81      0.87       144
                     Pneumomediastinum (Uncertain)       0.81      0.87      0.84        54
                    Tracheal deviation (Uncertain)       0.67      0.53      0.60        58
                Acute humerus fracture (Uncertain)       0.85      0.49      0.62        35
                    Acute rib fracture (Uncertain)       0.82      0.78      0.80       255
               Acute clavicle fracture (Uncertain)       0.65      0.71      0.68        28
                Acute scapula fracture (Uncertain)       0.67      0.67      0.67        12
                  Compression fracture (Uncertain)       0.87      0.71      0.78       110
                  Shoulder dislocation (Uncertain)       0.71      0.38      0.50        13
                Subcutaneous Emphysema (Uncertain)       0.86      0.63      0.73        19
               Suboptimal central line (Uncertain)       0.50      0.04      0.07        84
          Suboptimal endotracheal tube (Uncertain)       0.50      0.03      0.05        39
           Suboptimal nasogastric tube (Uncertain)       0.60      0.04      0.07        78
Suboptimal pulmonary arterial catheter (Uncertain)       0.00      0.00      0.00         8
                          Pleural tube (Uncertain)       1.00      0.20      0.33        15
                             PICC line (Uncertain)       0.54      0.33      0.41        21
                         Port catheter (Uncertain)       0.00      0.00      0.00         0
                             Pacemaker (Uncertain)       0.00      0.00      0.00         5
             Implantable defibrillator (Uncertain)       0.00      0.00      0.00         3
                                  LVAD (Uncertain)       0.00      0.00      0.00         0
              Intraaortic balloon pump (Uncertain)       0.67      1.00      0.80         2
                      Pneumoperitoneum (Uncertain)       0.82      0.84      0.83        82
                              Lung Lesion (Absent)       0.36      0.57      0.44         7
                                    Edema (Absent)       0.77      0.90      0.83      1138
                                Pneumonia (Absent)       0.88      0.87      0.88      1083
                              Atelectasis (Absent)       0.89      0.83      0.86       154
                               Aspiration (Absent)       0.77      0.79      0.78        42
                            Lung collapse (Absent)       0.92      0.34      0.50        35
               Perihilar airspace opacity (Absent)       0.47      1.00      0.64         9
             Air space opacity-multifocal (Absent)       0.44      0.35      0.39        34
                  Mass/Solitary lung mass (Absent)       0.80      0.60      0.69        40
              Nodule/Solitary lung nodule (Absent)       0.78      0.75      0.76       110
             Cavitating mass with content (Absent)       1.00      0.25      0.40         4
                        Cavitating masses (Absent)       0.00      0.00      0.00         1
                                Emphysema (Absent)       0.50      0.33      0.40         3
                                 Fibrosis (Absent)       1.00      0.78      0.88         9
                     Pulmonary congestion (Absent)       0.64      0.67      0.65       171
                    Hilar lymphadenopathy (Absent)       0.54      0.54      0.54        41
                           Bronchiectasis (Absent)       0.00      0.00      0.00         3
                      Simple pneumothorax (Absent)       0.72      0.76      0.74      2188
                   Loculated pneumothorax (Absent)       0.71      0.50      0.59        10
                     Tension pneumothorax (Absent)       0.82      0.56      0.67        32
                  Simple pleural effusion (Absent)       0.72      0.74      0.73      1014
               Loculated pleural effusion (Absent)       0.75      0.75      0.75         8
                         Pleural scarring (Absent)       0.00      0.00      0.00         1
                        Hydropneumothorax (Absent)       1.00      0.81      0.90        16
                            Pleural Other (Absent)       0.00      0.00      0.00         2
                             Cardiomegaly (Absent)       0.63      0.76      0.69       131
                     Pericardial effusion (Absent)       0.73      0.65      0.69        17
                Inferior mediastinal mass (Absent)       0.00      0.00      0.00         5
                Superior mediastinal mass (Absent)       1.00      0.09      0.17        11
                           Tortuous Aorta (Absent)       0.00      0.00      0.00         0
               Calcification of the Aorta (Absent)       0.00      0.00      0.00         8
                Enlarged pulmonary artery (Absent)       0.00      0.00      0.00         0
                                   Hernia (Absent)       0.91      0.71      0.80        14
                        Pneumomediastinum (Absent)       0.84      0.78      0.81        49
                       Tracheal deviation (Absent)       0.00      0.00      0.00         5
                   Acute humerus fracture (Absent)       0.69      0.72      0.71        83
                       Acute rib fracture (Absent)       0.74      0.84      0.78       765
                  Acute clavicle fracture (Absent)       0.69      0.83      0.75       132
                   Acute scapula fracture (Absent)       0.67      0.17      0.27        12
                     Compression fracture (Absent)       0.00      0.00      0.00         7
                     Shoulder dislocation (Absent)       0.00      0.00      0.00         4
                   Subcutaneous Emphysema (Absent)       0.81      0.96      0.88        46
                  Suboptimal central line (Absent)       0.00      0.00      0.00        63
             Suboptimal endotracheal tube (Absent)       0.00      0.00      0.00       103
              Suboptimal nasogastric tube (Absent)       0.00      0.00      0.00        66
   Suboptimal pulmonary arterial catheter (Absent)       0.00      0.00      0.00         7
                             Pleural tube (Absent)       0.00      0.00      0.00        11
                                PICC line (Absent)       0.44      0.24      0.31        46
                            Port catheter (Absent)       0.00      0.00      0.00         1
                                Pacemaker (Absent)       0.67      0.33      0.44         6
                Implantable defibrillator (Absent)       0.00      0.00      0.00         2
                                     LVAD (Absent)       0.00      0.00      0.00         0
                 Intraaortic balloon pump (Absent)       0.33      1.00      0.50         2
                         Pneumoperitoneum (Absent)       0.72      0.72      0.72        43
                                        No Finding       0.92      0.91      0.92     59962

                                         micro avg       0.89      0.88      0.88    178346
                                         macro avg       0.67      0.61      0.62    178346
                                      weighted avg       0.89      0.88      0.88    178346
                                       samples avg       0.88      0.88      0.88    178346
```


```
@inproceedings{delbrouck-etal-2025-automated,
    title = "Automated Structured Radiology Report Generation",
    author = "Delbrouck, Jean-Benoit  and
      Xu, Justin  and
      Moll, Johannes  and
      Thomas, Alois  and
      Chen, Zhihong  and
      Ostmeier, Sophie  and
      Azhar, Asfandyar  and
      Li, Kelvin Zhenghao  and
      Johnston, Andrew  and
      Bluethgen, Christian  and
      Reis, Eduardo Pontes  and
      Muneer, Mohamed S  and
      Varma, Maya  and
      Langlotz, Curtis",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.1301/",
    doi = "10.18653/v1/2025.acl-long.1301",
    pages = "26813--26829",
    ISBN = "979-8-89176-251-0",
    abstract = "Automated radiology report generation from chest X-ray (CXR) images has the potential to improve clinical efficiency and reduce radiologists' workload. However, most datasets, including the publicly available MIMIC-CXR and CheXpert Plus, consist entirely of free-form reports, which are inherently variable and unstructured. This variability poses challenges for both generation and evaluation: existing models struggle to produce consistent, clinically meaningful reports, and standard evaluation metrics fail to capture the nuances of radiological interpretation. To address this, we introduce Structured Radiology Report Generation (SRRG), a new task that reformulates free-text radiology reports into a standardized format, ensuring clarity, consistency, and structured clinical reporting. We create a novel dataset by restructuring reports using large language models (LLMs) following strict structured reporting desiderata. Additionally, we introduce SRR-BERT, a fine-grained disease classification model trained on 55 labels, enabling more precise and clinically informed evaluation of structured reports. To assess report quality, we propose F1-SRR-BERT, a metric that leverages SRR-BERT{'}s hierarchical disease taxonomy to bridge the gap between free-text variability and structured clinical reporting. We validate our dataset through a reader study conducted by five board-certified radiologists and extensive benchmarking experiments."
}
```