---
language:
- pt
tags:
- albertina-pt*
- albertina-ptpt
- albertina-ptbr
- albertina-ptpt-base
- albertina-ptbr-base
- fill-mask
- bert
- deberta
- portuguese
- encoder
- foundation model
license: mit
datasets:
- dlb/plue
- oscar-corpus/OSCAR-2301
- PORTULAN/glue-ptpt
widget:
- text: >-
    A culinária brasileira é rica em sabores e [MASK], tornando-se um dos maiores patrimônios do país.
---

---
<img align="left" width="40" height="40" src="https://github.githubassets.com/images/icons/emoji/unicode/1f917.png">
<p style="text-align: center;">&nbsp;&nbsp;&nbsp;&nbsp;This is the model card for Albertina 100M PTBR. 
  You may be interested in some of the other models in the <a href="https://huggingface.co/PORTULAN">Albertina (encoders) and Gervásio (decoders) families</a>.
</p>

---

# Albertina 100M PTBR

**Albertina 100M PTBR** is a foundation, large language model for American **Portuguese** from **Brazil**.

It is an **encoder** of the BERT family, based on the neural architecture Transformer and 
developed over the DeBERTa model, with most competitive performance for this language. 
It is distributed free of charge and under a most permissible license.

| Albertina's Family of Models                                                                             | 
|----------------------------------------------------------------------------------------------------------|
| [**Albertina 1.5B PTPT**](https://huggingface.co/PORTULAN/albertina-1b5-portuguese-ptpt-encoder)        |
| [**Albertina 1.5B PTBR**](https://huggingface.co/PORTULAN/albertina-1b5-portuguese-ptbr-encoder)        |
| [**Albertina 1.5B PTPT 256**](https://huggingface.co/PORTULAN/albertina-1b5-portuguese-ptpt-encoder-256)|
| [**Albertina 1.5B PTBR 256**](https://huggingface.co/PORTULAN/albertina-1b5-portuguese-ptbr-encoder-256)|
| [**Albertina 900M PTPT**](https://huggingface.co/PORTULAN/albertina-900m-portuguese-ptpt-encoder)       |
| [**Albertina 900M PTBR**](https://huggingface.co/PORTULAN/albertina-900m-portuguese-ptbr-encoder)       |
| [**Albertina 100M PTPT**](https://huggingface.co/PORTULAN/albertina-100m-portuguese-ptpt-encoder)       |
| [**Albertina 100M PTBR**](https://huggingface.co/PORTULAN/albertina-100m-portuguese-ptbr-encoder)       |


**Albertina 100M PTBR base** is developed by a joint team from the University of Lisbon and the University of Porto, Portugal. 
For further details, check the respective [publication](https://arxiv.org/abs/2403.01897):

``` latex
@misc{albertina-pt-fostering,
      title={Fostering the Ecosystem of Open Neural Encoders
            for Portuguese with Albertina PT-* family}, 
      author={Rodrigo Santos and João Rodrigues and Luís Gomes
              and João Silva and António Branco
              and Henrique Lopes Cardoso and Tomás Freitas Osório
              and Bernardo Leite},
      year={2024},
      eprint={2403.01897},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

Please use the above canonical reference when using or citing this model.

<br>


# Model Description

**This model card is for Albertina 100M PTBR**, with 100M parameters, 12 layers and a hidden size of 768.

Albertina-PT-BR base is distributed under an [MIT license](https://huggingface.co/PORTULAN/albertina-ptpt/blob/main/LICENSE).

DeBERTa is distributed under an [MIT license](https://github.com/microsoft/DeBERTa/blob/master/LICENSE).


<br>

# Training Data


[**Albertina P100M PTBR**](https://huggingface.co/PORTULAN/albertina-ptbr-base) was trained over a 3.7 billion token curated selection of documents from the [OSCAR](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301) data set.
The OSCAR data set includes documents in more than one hundred languages, including Portuguese, and it is widely used in the literature. It is the result of a selection performed over the [Common Crawl](https://commoncrawl.org/) data set, crawled from the Web, that retains only pages whose metadata indicates permission to be crawled, that performs deduplication, and that removes some boilerplate, among other filters.
Given that it does not discriminate between the Portuguese variants, we performed extra filtering by retaining only documents whose meta-data indicate the Internet country code top-level domain of Brazil. We used the January 2023 version of OSCAR, which is based on the November/December 2022 version of Common Crawl.


## Preprocessing

We filtered the PT-BR corpora using the [BLOOM pre-processing](https://github.com/bigscience-workshop/data-preparation) pipeline.
We skipped the default filtering of stopwords since it would disrupt the syntactic structure, and also the filtering for language identification given the corpus was pre-selected as Portuguese.


## Training

As codebase, we resorted to the [DeBERTa V1 base](https://huggingface.co/microsoft/deberta-base), for English.


To train [**Albertina 100M PTBR**](https://huggingface.co/PORTULAN/albertina-ptpt-base), the data set was tokenized with the original DeBERTa tokenizer with a 128 token sequence truncation and dynamic padding.
The model was trained using the maximum available memory capacity resulting in a batch size of 3072 samples (192 samples per GPU).
We opted for a learning rate of 1e-5 with linear decay and 10k warm-up steps. 
The model was trained with a total of 150 training epochs resulting in approximately 180k steps.
The model was trained for one day on a2-megagpu-16gb Google Cloud A2 VMs with 16 GPUs, 96 vCPUs and 1.360 GB of RAM.


<br>

# Evaluation

The base model versions was evaluated on downstream tasks, namely the translations into PTBR of the English data sets used for a few of the tasks in the widely-used [GLUE benchmark](https://huggingface.co/datasets/glue).


## GLUE tasks translated

We resort to [PLUE](https://huggingface.co/datasets/dlb/plue) (Portuguese Language Understanding Evaluation), a data set that was obtained by automatically translating GLUE into **PT-BR**.
We address four tasks from those in PLUE, namely:
- two similarity tasks: MRPC, for detecting whether two sentences are paraphrases of each other, and STS-B, for semantic textual similarity;
- and two inference tasks: RTE, for recognizing textual entailment and WNLI, for coreference and natural language inference.
  

| Model                         | RTE (Accuracy) | WNLI (Accuracy)| MRPC (F1) | STS-B (Pearson) |
|------------------------------|----------------|----------------|-----------|-----------------|
| **Albertina 900M PTBR No-brWaC** | **0.7798**     | 0.5070         | **0.9167**| 0.8743 
| **Albertina 900M PTBR**          | 0.7545         | 0.4601         | 0.9071    | **0.8910**      | 
| **Albertina 100M PTBR**     | 0.6462         | **0.5493**     | 0.8779    | 0.8501          |


<br>

# How to use

You can use this model directly with a pipeline for masked language modeling:

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='PORTULAN/albertina-ptbr-base')
>>> unmasker("A culinária brasileira é rica em sabores e [MASK], tornando-se um dos maiores patrimônios do país.")

[{'score': 0.9391396045684814, 'token': 14690, 'token_str': ' costumes', 'sequence': 'A culinária brasileira é rica em sabores e costumes, tornando-se um dos maiores patrimônios do país.'},
{'score': 0.04568921774625778, 'token': 29829, 'token_str': ' cores', 'sequence': 'A culinária brasileira é rica em sabores e cores, tornando-se um dos maiores patrimônios do país.'},
{'score': 0.004134135786443949, 'token': 6696, 'token_str': ' drinks', 'sequence': 'A culinária brasileira é rica em sabores e drinks, tornando-se um dos maiores patrimônios do país.'},
{'score': 0.0009097770671360195, 'token': 33455, 'token_str': ' nuances', 'sequence': 'A culinária brasileira é rica em sabores e nuances, tornando-se um dos maiores patrimônios do país.'},
{'score': 0.0008549498743377626, 'token': 606, 'token_str': ' comes', 'sequence': 'A culinária brasileira é rica em sabores e comes, tornando-se um dos maiores patrimônios do país.'}]


```

The model can be used by fine-tuning it for a specific task:

```python
>>> from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
>>> from datasets import load_dataset

>>> model = AutoModelForSequenceClassification.from_pretrained("PORTULAN/albertina-ptbr-base", num_labels=2)
>>> tokenizer = AutoTokenizer.from_pretrained("PORTULAN/albertina-ptbr-base")
>>> dataset = load_dataset("PORTULAN/glue-ptpt", "rte")

>>> def tokenize_function(examples):
...     return tokenizer(examples["sentence1"], examples["sentence2"], padding="max_length", truncation=True)

>>> tokenized_datasets = dataset.map(tokenize_function, batched=True)

>>> training_args = TrainingArguments(output_dir="albertina-ptpt-rte", evaluation_strategy="epoch")
>>> trainer = Trainer(
...     model=model,
...     args=training_args,
...     train_dataset=tokenized_datasets["train"],
...     eval_dataset=tokenized_datasets["validation"],
... )

>>> trainer.train()

```

<br>

# Citation

When using or citing this model, kindly cite the following [publication](https://arxiv.org/abs/2403.01897):

``` latex
@misc{albertina-pt-fostering,
      title={Fostering the Ecosystem of Open Neural Encoders
            for Portuguese with Albertina PT-* family}, 
      author={Rodrigo Santos and João Rodrigues and Luís Gomes
              and João Silva and António Branco
              and Henrique Lopes Cardoso and Tomás Freitas Osório
              and Bernardo Leite},
      year={2024},
      eprint={2403.01897},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

<br>

# Acknowledgments

The research reported here was partially supported by: PORTULAN CLARIN—Research Infrastructure for the Science and Technology of Language,
funded by Lisboa 2020, Alentejo 2020 and FCT—Fundação para a Ciência e Tecnologia under the
grant PINFRA/22117/2016; research project ALBERTINA - Foundation Encoder Model for Portuguese and AI, funded by FCT—Fundação para a Ciência e Tecnologia under the
grant CPCA-IAC/AV/478394/2022; innovation project ACCELERAT.AI - Multilingual Intelligent Contact Centers, funded by IAPMEI, I.P. - Agência para a Competitividade e Inovação under the grant C625734525-00462629, of Plano de Recuperação e Resiliência, call RE-C05-i01.01 – Agendas/Alianças Mobilizadoras para a Reindustrialização; and LIACC - Laboratory for AI and Computer Science, funded by FCT—Fundação para a Ciência e Tecnologia under the grant FCT/UID/CEC/0027/2020.