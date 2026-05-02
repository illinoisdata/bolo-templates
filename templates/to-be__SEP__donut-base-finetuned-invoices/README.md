---
license: cc-by-nc-sa-4.0
tags:
- donut
- image-to-text
- vision
- invoices
---

# Donut finetuned on invoices 

Based on Donut base model (introduced in the paper [OCR-free Document Understanding Transformer](https://arxiv.org/abs/2111.15664) by Geewok et al. and first released in [this repository](https://github.com/clovaai/donut).

The model was trained with a few thousand of annotated invoices and non-invoices (for those the doctype will be 'Other'). They span across different countries and languages. They are always one page only. The dataset is proprietary unfortunately. Model is set to input resolution of 1280x1920 pixels. So any sample you want to try with higher dpi than 150 has no added value.
It was trained for about 4 hours on a NVIDIA RTX A4000 for 20k steps with a val_metric of 0.03413819904382196 at the end.
The following indexes were included in the train set:

DocType
Currency
DocumentDate
GrossAmount
InvoiceNumber
NetAmount
TaxAmount
OrderNumber
CreditorCountry

[Demo space can be found here](https://huggingface.co/spaces/to-be/invoice_document_headers_extraction_with_donut)

## Model description

Donut consists of a vision encoder (Swin Transformer) and a text decoder (BART). Given an image, the encoder first encodes the image into a tensor of embeddings (of shape batch_size, seq_len, hidden_size), after which the decoder autoregressively generates text, conditioned on the encoding of the encoder. 

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/donut_architecture.jpg)

## Intended uses & limitations

This model is meant as a research in how well it fares with multilanguage invoices.
See my observations in the [demo space](https://huggingface.co/spaces/to-be/invoice_document_headers_extraction_with_donut).

### How to use

Look at the [documentation](https://huggingface.co/docs/transformers/main/en/model_doc/donut) which includes code examples.