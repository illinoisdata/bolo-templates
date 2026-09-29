---
license: apache-2.0
datasets:
- nateraw/fairface
metrics:
- accuracy
- f1
base_model:
- google/vit-base-patch16-224-in21k
pipeline_tag: image-classification
---
Detects gender with about 93.4% accuracy based on an image.

See https://www.kaggle.com/code/dima806/gender-image-classification-vit for details.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6449300e3adf50d864095b90/OOerkHOqKZsJ4F4CZsZEW.png)

```
Classification report:

              precision    recall  f1-score   support

      Female     0.9531    0.9051    0.9285      4720
        Male     0.9188    0.9602    0.9391      5280

    accuracy                         0.9342     10000
   macro avg     0.9360    0.9327    0.9338     10000
weighted avg     0.9350    0.9342    0.9341     10000
```