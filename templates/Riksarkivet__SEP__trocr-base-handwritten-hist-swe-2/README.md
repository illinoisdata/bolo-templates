---
tags:
- trocr
- image-to-text
- swedish lion libre
- htr
- transformers
- swedish
- historical
- handwriting
widget:
- src: https://fki.tic.heia-fr.ch/static/img/a01-122-02.jpg
  example_title: Note 1
- src: >-
    https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoolxi9yWGAT5SLZShv8vVd0bz47UWRzQC19fDTeE8GmGv_Rn-PCF1pP1rrUx8kOjA4gg&usqp=CAU
  example_title: Note 2
- src: >-
    https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNYtTuSBpZPV_nkBYPMFwVVD9asZOPgHww4epu9EqWgDmXW--sE2o8og40ZfDGo87j5w&usqp=CAU
  example_title: Note 3
datasets:
- Riksarkivet/goteborgs_poliskammare_fore_1900_lines
- Riksarkivet/krigshovrattens_dombocker_lines
- Riksarkivet/svea_hovratt_lines
- Riksarkivet/bergskollegium_relationer_och_skrivelser_lines
- Riksarkivet/frihetstidens_utskottshandlingar_lines
- Riksarkivet/carl_fredrik_pahlmans_resejournaler_lines
- Riksarkivet/trolldomskommissionen_lines
- Riksarkivet/gota_hovratt_lines
- Riksarkivet/bergmastaren_i_nora_htr_lines
- Riksarkivet/alvsborgs_losen_lines
- Riksarkivet/jonkopings_radhusratt_och_magistrat_lines
language:
- sv
metrics:
- cer
- wer
base_model:
- microsoft/trocr-base-handwritten
pipeline_tag: image-to-text
library_name: htrflow
license: apache-2.0
---

# Swedish Lion Libre

An HTR model for historical swedish developed by the Swedish National Archives in collaboration with the Stockholm City Archives, the Finnish National Archives and Jämtlands Fornskriftsällskap. The model is trained on Swedish handwriting dating from ca 1600-1900

## Model Details

### Model Description

- **Developed by:** The Swedish National Archives
- **Model type:** TrOCR base handwritten
- **Language(s) (NLP):** Historical Swedish handwriting
- **License:** apache-2.0
- **Finetuned from model:** trocr-base-handwritten

## Uses

The model is trained on Swedish running-text handwriting dating from the start of the 17th century to the end of the 19th century. Like most current HTR-models 
it operates on a text-line level, so it's intended use is within an HTR-pipeline that segments the text into text-lines, which are transcribed by the model.

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

The model can be used without fine-tuning on all handwriting but performs best on the type of handwriting it was trained on, which is Swedish handwriting from 1600-1900.
See below for detailed test and evaluation results.

### Downstream Use

The model can be fine-tuned on other types of handwriting, or if you plan to use it to transcribe some specific material that is within it's domain but not included in the training data, for instance if you got a large letter collection dating from the 17th century, it can be fine-tuned on a small amount of manually transcribed in-domain data, say 20-50 letters, and then used to transcribe the entire collection.

### Out-of-Scope Use

The model wont work well out-of-the-box for other languages than Swedish, and it wont work well for printed text.

## How to Get Started with the Model

Use the code below to get started with the model, but bare in mind that the image has to be a single text-line.

```python
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

img_path = 'path/to/image'
image = Image.open(img_path)

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained('Riksarkivet/trocr-base-handwritten-hist-swe-2')
pixel_values = processor(images=image, return_tensors="pt").pixel_values

generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

If you want to transcribe entire pages, consider using HTRflow, a package developed by The Swedish National Archives and intended for streamlining large and small scale HTR/OCR-projects. Install the package, write a pipeline config yaml, where you specify the models to use by their huggingface id, add preprocessing or post-processing steps, and then run the pipeline with `htrflow pipeline <path/to/yaml> <path/to/image/images>`. A .yaml file for an entire pipeline, transcribing full pages, could look like this:

```yaml

# Demo pipeline for running text

steps:

# Region segmentation
- step: Segmentation
  settings:
    model: yolo
    model_settings:
       model: Riksarkivet/yolov9-regions-1
    generation_settings:
       conf: 0.3
       batch_size: 32

# Line segmentation
- step: Segmentation
  settings:
    model: yolo
    model_settings:
       model: Riksarkivet/yolov9-lines-within-regions-1
    generation_settings:
       conf: 0.3
       batch_size: 16

- step: TextRecognition
  settings:
    model: WordLevelTrocr
    model_settings:
       model: Riksarkivet/trocr-base-handwritten-hist-swe-2
    generation_settings:
       batch_size: 16
       num_beams: 1

- step: ReadingOrderMarginalia
  settings:
    two_page: always

- step: RemoveLowTextConfidencePages
  settings:
    threshold: 0.95

- step: RemoveLowTextConfidenceLines
  settings:
    threshold: 0.95

# Export to Alto and Page XML 
- step: Export
  settings:
    dest: outputs/new_models/alto
    format: alto

- step: Export
  settings:
    dest: outputs/new_models/page
    format: page

# Sets label format to regionX_lineY_wordZ
labels:
  level_labels:
    - region
    - line
    - word
  sep: _
  template: "{label}{number}"
  ```

  See the documentation for the HTRflow package for further instructions on specific steps and customizations


## Training Details

### Training Data

We cannot publically release all data the model was trained on, since we ourselves haven't created all the data, but below are links to the datasets we can release publically:

[Göteborgs poliskammare 1850-1900](https://huggingface.co/datasets/Riksarkivet/goteborgs_poliskammare_fore_1900_lines)  
[Krigshovrättens domböcker](https://huggingface.co/datasets/Riksarkivet/krigshovrattens_dombocker_lines)  
[Svea hovrätt](https://huggingface.co/datasets/Riksarkivet/svea_hovratt_lines)  
[Bergskollegium](https://huggingface.co/datasets/Riksarkivet/bergskollegium_relationer_och_skrivelser_lines)  
[Frihetstidens utskottshandlingar](https://huggingface.co/datasets/Riksarkivet/frihetstidens_utskottshandlingar_lines)  
[Carl-Fredrik Påhlmans resejournaler](https://huggingface.co/datasets/Riksarkivet/carl_fredrik_pahlmans_resejournaler_lines)  
[Trolldomskommissionen](https://huggingface.co/datasets/Riksarkivet/trolldomskommissionen_lines)  
[Göta hovrätt](https://huggingface.co/datasets/Riksarkivet/gota_hovratt_lines)  
[Bergmästaren i Nora](https://huggingface.co/datasets/Riksarkivet/bergmastaren_i_nora_htr_lines)  
[Älvsborgs lösen](https://huggingface.co/datasets/Riksarkivet/alvsborgs_losen_lines)  
[Jönköpings rådhusrätt magistrat](https://huggingface.co/datasets/Riksarkivet/jonkopings_radhusratt_och_magistrat_lines)

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing

The text-line polygons were masked out and placed against a white backgroundy, with dimensions decided by the polygon's bounding box.


#### Training Hyperparameters

See config.json at [model repo](https://huggingface.co/Riksarkivet/trocr-base-handwritten-hist-swe-2/tree/main)  
**training regime**: bf16     
**learning rate**: 5e-5  
**weight decay**: 0.01  


## Evaluation

### In-Domain Evaluation Data (Sorted by CER)

These are the character and word error rates on evaluation data taken from the same archives that was included in the training set. Of course the evaluation samples aren't part of the training data. The number of samples included in the training-set give an indication of how the model improves by fine-tuning it on some specific material within the model's range.

| Dataset | WER | CER | Train Lines | Eval Lines |
|---------|-----|-----|-------------|------------|
| krigshovrattens_dombocker_lines | 0.0330 | 0.0075 | 16,887 | 1,877 |
| stockholms_stadsarkiv_allmana_barnhuset_1700_lines | 0.0647 | 0.0120 | 565 | 142 |
| stockholms_stadsarkiv_blandat_2_1700_lines | 0.0807 | 0.0170 | 25,024 | 2,781 |
| goteborgs_poliskammare_fore_1900_lines | 0.0800 | 0.0187 | 339,297 | 17,858 |
| stockholms_stadsarkiv_stockholms_domkapitel_1700_lines | 0.0948 | 0.0187 | 96,409 | 5,075 |
| stockholms_stadsarkiv_politikollegiet_1700_lines | 0.1108 | 0.0225 | 120,238 | 6,329 |
| bergskollegium_relationer_och_skrivelser_lines | 0.1056 | 0.0253 | 62,201 | 6,912 |
| stockholms_stadsarkiv_stadens_kamnarsratt_1700_lines | 0.1252 | 0.0278 | 38,330 | 4,259 |
| svea_hovratt_lines | 0.1484 | 0.0313 | 36,884 | 4,099 |
| stockholms_stadsarkiv_stockholms_domkapitel_1800_lines | 0.1400 | 0.0324 | 2,070 | 230 |
| stockholms_stadsarkiv_handelskollegiet_1600_1700_lines | 0.1785 | 0.0350 | 9,201 | 1,023 |
| frihetstidens_utskottshandlingar_lines | 0.1481 | 0.0362 | 13,490 | 1,499 |
| stockholms_stadsarkiv_kungliga_hovkonsistoriet_1700_lines | 0.1541 | 0.0364 | 5,753 | 640 |
| national_archives_finland_court_records_lines | 0.1607 | 0.0368 | 147,456 | 7,761 |
| stockholms_stadsarkiv_blandat_1600_1700_lines | 0.1505 | 0.0379 | 16,137 | 1,794 |
| stockholms_stadsarkiv_blandat_3_1600_lines | 0.1633 | 0.0400 | 43,142 | 4,794 |
| stockholms_stadsarkiv_norra_forstadens_kamnarsratt_1600_1700_lines | 0.1755 | 0.0463 | 18,474 | 2,053 |
| carl_fredrik_pahlmans_resejournaler_lines | 0.1768 | 0.0482 | 7,081 | 787 |
| stockholms_stadsarkiv_sollentuna_haradsratt_1700_1800_lines | 0.1921 | 0.0505 | 19,096 | 2,122 |
| stockholms_stadsarkiv_byggningskollegium_1600_lines | 0.2262 | 0.0514 | 3,104 | 345 |
| ra_enstaka_sidor_lines | 0.1991 | 0.0538 | 5,078 | 565 |
| trolldomskommissionen_lines | 0.2321 | 0.0600 | 33,498 | 3,722 |
| stockholms_stadsarkiv_stockholms_domkapitel_1600_lines | 0.2170 | 0.0607 | 11,619 | 1,292 |
| stockholms_stadsarkiv_botkyrka_kyrkoarkiv_1600_1800_lines | 0.2548 | 0.0627 | 3,617 | 402 |
| gota_hovratt_lines | 0.2450 | 0.0630 | 2,421 | 269 |
| bergmastaren_i_nora_htr_lines | 0.2558 | 0.0709 | 7,916 | 880 |
| bergskollegium_advokatfiskalkontoret_lines | 0.2906 | 0.0722 | 2,411 | 268 |
| jl_fornsallskap_jamtlands_domsaga_lines | 0.2585 | 0.0732 | 60,544 | 6,728 |
| alvsborgs_losen_lines | 0.1896 | 0.0806 | 5,632 | 626 |
| jonkopings_radhusratt_och_magistrat_lines | 0.2864 | 0.0853 | 1,179 | 131 |
| national_archives_finland_letters_recipes_lines | 0.3857 | 0.1360 | 651 | 163 |



### Testing Data

#### Out-of-Domain Test Data (Sorted by CER)

These are all test-sets taken from archives that we're not at all included in the training data. So these are the results one would expect if one uses this model out-of-the-box on just any running text document within the models time-span. The entire test-suite is available here: [test-suite for htr](https://huggingface.co/datasets/Riksarkivet/eval_htr_out_of_domain_lines)

| Dataset | WER | CER | Eval Lines |
|---------|-----|-----|-----------------|
| 1792_R0002231_eval_lines | 0.1190 | 0.0250 | 501 |
| 1794-1795_A0068546_eval_lines | 0.1503 | 0.0303 | 510 |
| 1775-1786_A0068551_eval_lines | 0.2203 | 0.0543 | 525 |
| 1841_Z0000017_eval_lines | 0.2247 | 0.0555 | 470 |
| 1690_A0066756_eval_lines | 0.2571 | 0.0611 | 249 |
| 1716_A0017151_eval_lines | 0.2517 | 0.0650 | 558 |
| 1824_H0000743_eval_lines | 0.2684 | 0.0674 | 260 |
| 1699-1700_C0113233_eval_lines | 0.2713 | 0.0691 | 394 |
| 1845-1857_B0000011_eval_lines | 0.2546 | 0.0706 | 153 |
| 1812_A0069332_eval_lines | 0.2868 | 0.0793 | 69 |
| 1659-1674_R0000568_eval_lines | 0.3278 | 0.0886 | 304 |
| 1755-1756_C0112394_eval_lines | 0.3440 | 0.0918 | 248 |
| 1723_H0000374_eval_lines | 0.3105 | 0.1140 | 378 |
| 1887-1892_A0002409_eval_lines | 0.3670 | 0.1297 | 784 |
| 1679_R0002397_eval_lines | 0.4768 | 0.1422 | 88 |
| 1800_C0101725_eval_lines | 0.4459 | 0.1767 | 37 |
| 1871_K0017448_eval_lines | 0.4504 | 0.1945 | 331 |
| 1654_R0001308_eval_lines | 0.5200 | 0.2179 | 199 |

#### Metrics

## Character Error Rate (CER)

Character Error Rate (CER) is a metric used to evaluate the performance of a Handwritten Text Recognition (HTR) system by comparing the recognized text to the reference (ground truth) text at the character level.

The CER is calculated using the following formula:

$$
CER = \frac{S + D + I}{N}
$$

Where:
- \( S \) = Number of substitutions (incorrect characters)
- \( D \) = Number of deletions (missing characters)
- \( I \) = Number of insertions (extra characters)
- \( N \) = Total number of characters in the reference text

A lower CER indicates better recognition accuracy.

## Word Error Rate (WER)

Word Error Rate (WER) is a metric used to assess the accuracy of an HTR system at the word level by comparing the recognized text to the reference text.

The WER is calculated using the following formula:

$$
WER = \frac{S + D + I}{N}
$$

Where:
- \( S \) = Number of substitutions (incorrect words)
- \( D \) = Number of deletions (missing words)
- \( I \) = Number of insertions (extra words)
- \( N \) = Total number of words in the reference text

Similar to CER, a lower WER indicates better word-level accuracy.


## Technical Specifications

### Model Architecture

See config.json at [model repo](https://huggingface.co/Riksarkivet/trocr-base-handwritten-hist-swe-2/tree/main)

## Citation

[TrOCR paper](https://arxiv.org/abs/2109.10282)

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->