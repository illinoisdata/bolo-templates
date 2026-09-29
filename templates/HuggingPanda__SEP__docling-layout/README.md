---
language:
- en
base_model:
- ds4sd/docling-models
pipeline_tag: object-detection
---
# Docling Model for Layout

This is the **Docling model for layout detection**, designed to facilitate easy importing and usage like any other Hugging Face model.

This model is part of the [Docling repository](https://huggingface.co/ds4sd/docling-models), which provides document layout analysis tools.

## **Usage Example**
Here's how you can load and use the model:

```python
import torch
from PIL import Image
from transformers import RTDetrForObjectDetection, RTDetrImageProcessor

# Load the model and processor
image_processor = RTDetrImageProcessor.from_pretrained("HuggingPanda/docling-layout")
model = RTDetrForObjectDetection.from_pretrained("HuggingPanda/docling-layout")

# Load an image
image = Image.open("hocr_output_page-0001.jpg")

# Preprocess the image
resize = {"height":640, "width":640}
inputs = image_processor(
    images=image,
    return_tensors="pt",
    size=resize,
)

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)

# Post-process results
results = image_processor.post_process_object_detection(
    outputs, 
    target_sizes=torch.tensor([image.size[::-1]]), 
    threshold=0.3
)

# Print detected objects
for result in results:
    for score, label_id, box in zip(result["scores"], result["labels"], result["boxes"]):
        score, label = score.item(), label_id.item()
        box = [round(i, 2) for i in box.tolist()]
        print(f"{model.config.id2label[label+1]}: {score:.2f} {box}")

```


## **Model Information**
- **Base Model:** RT-DETR (Robust Transformer-based Object Detector)
- **Intended Use:** Layout detection for documents
- **Framework:** [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- **Dataset Used:** Internal dataset for document structure recognition
- **License:** Apache 2.0

## **Citing This Model**
If you use this model in your work, please cite the main **Docling repository**:

```
@misc{docling2024, title={Docling Models for Document Layout Analysis}, author={DS4SD Team}, year={2024}, howpublished={Hugging Face Repository}, url={https://huggingface.co/ds4sd/docling-models} }
```

For more details, visit the main repo: [ds4sd/docling-models](https://huggingface.co/ds4sd/docling-models).

## **Contact**
For questions or issues, please open a discussion on Hugging Face or contact [pandahd75@gmail.com].