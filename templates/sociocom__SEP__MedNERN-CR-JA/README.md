---
language:
  - ja
license:
  - cc-by-4.0
tags:
  - NER
  - medical documents
datasets:
  - MedTxt-CR-JA-training-v2.xml
metrics:
  - NTCIR-16 Real-MedNLP subtask 1
---

This is a model for named entity recognition of Japanese medical documents.

# Introduction

This repository contains the base model and a support predict script for using the model and providing a XML tagged text output.

The original model was trained on the [MedTxt-CR-JA](https://sociocom.naist.jp/medtxt/cr) dataset, so the provided prediction code outputs XML tags in the same format.

The script also provide the normalization method for the output entities, which is not embedded in the model.

If you want to re-train or update the model, we provide additional support scripts in [this GitHub repository](https://github.com/sociocom/MedNERN-CR-JA).
Issues and suggestions can also be submitted there.

### A note about loading the model using standard HuggingFace methods
This model should also be loadable using standard HuggingFace `from_pretrained` methods. However, the model by itself only outputs labels in the format "LABEL_0", "LABEL1", etc.

The conversion of model outputs to the actual labels ("<m-key>, "<m-val>", "<timex-3>" etc.) is not yet embedded into the model, so the extra `id_to_tags.pkl` file is necessary 
to make the conversion. It contains a mapping from the model output ids to the actual labels.

Such process can be done manually if needed, but the `predict.py` script already does that.

We are currently working to better standardize the model to HuggingFace's standards.

## How to use

Clone the repository and install the requirements:

``` 
pip install -r requirements.txt
```

The code has been developed tested with Python 3.9 in MacOS 14.1 (M1 MacBook Pro).

### Prediction

The prediction script will output the results in the same XML format as the input file. It can be run with the following
command:

```
python3 predict.py
```

The default parameters will take the model located in `pytorch_model.bin` and the input file `text.txt`.
The resulting predictions will be output to the screen.

To select a different model or input file, use the `-m` and `-i` parameters, respectively:

```
python3 predict.py -m <model_path> -i <your_input_file>.txt
```

The input file can be a single text file or a folder containing multiple `.txt` files, for batch processing. For example:

```
python3 predict.py -m <model_path> -i <your_input_folder>
```


### Entity normalization

This model supports entity normalization via dictionary matching. The dictionary is a list of medical terms or
drugs and their standard forms.

Two different dictionaries are used for drug and disease normalization, stored in the `dictionaries` folder as
`drug_dict.csv` and `disease_dict.csv`, respectively.

To enable normalization you can add the `--normalize` flag to the `predict.py` command.

```
python3 predict.py -m <model_path> --normalize
```

Normalization will add the `norm` attribute to the output XML tags. This attribute can be empty if a normalized form of
the term is not found.

The provided disease normalization dictionary (`dictionaties/disease_dict.csv`) is based on
the [Manbyo Dictionary](https://sociocom.naist.jp/manbyo-dic-en/) and provides normalization to the standard ICD code
for the diseases.

The default drug dictionary (`dictionaties/drug_dict.csv`) is based on
the [Hyakuyaku Dictionary](https://sociocom.naist.jp/hyakuyaku-dic-en/).

The dictionary is a CSV file with three columns: the first column is the surface form term and the third column contain
its standard form. The second column is not used.

### Replacing the default dictionaries

User can freely change the dictionary to fit their needs by passing the path to a custom dictionary file.
The dictionary file must have at least a column containing the list of surface forms and a column containing the list of
normalized forms.

The parameters `--drug_dict` and `--disease_dict` can be used to specify the path to the drug and disease dictionaries,
respectively.
When doing so, the respective parameters informing the column index of the surface form and normalized form must also be
provided.
You don't need to replace both dictionaries at the same time, you can replace only one of them.

E.g.:

```
python3 predict.py --normalize --drug_dict dictionaries/drug_dict.csv --drug_surface_form 0 --drug_norm_form 2 --disease_dict dictionaries/disease_dict.csv --disease_surface_form 0 --disease_norm_form 2
```

### Input Example

```
肥大型心筋症、心房細動に対してＷＦ投与が開始となった。
治療経過中に非持続性心室頻拍が認められたためアミオダロンが併用となった。
```

### Output Example

```
<d certainty="positive" norm="I422">肥大型心筋症、心房細動</d>に対して<m-key state="executed" norm="ワルファリンカリウム">ＷＦ</m-key>投与が開始となった。
<timex3 type="med">治療経過中</timex3>に<d certainty="positive" norm="I472">非持続性心室頻拍</d>が認められたため<m-key state="executed" norm="アミオダロン塩酸塩">アミオダロン</m-key>が併用となった。
```

## Publication

This model can be cited as:

```
@misc {social_computing_lab_2023,
	author       = { {Social Computing Lab} },
	title        = { MedNERN-CR-JA (Revision 13dbcb6) },
	year         = 2023,
	url          = { https://huggingface.co/sociocom/MedNERN-CR-JA },
	doi          = { 10.57967/hf/0620 },
	publisher    = { Hugging Face }
}
```
