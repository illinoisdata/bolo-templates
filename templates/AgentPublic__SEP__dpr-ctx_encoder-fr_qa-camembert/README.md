---
language: fr
datasets:
- piaf
- FQuAD
- SQuAD-FR
---

# dpr-ctx_encoder-fr_qa-camembert

## Description

French [DPR model](https://arxiv.org/abs/2004.04906) using [CamemBERT](https://arxiv.org/abs/1911.03894) as base and then fine-tuned on a combo of three French Q&A 
## Data
### French Q&A 
We use a combination of three French Q&A datasets: 

1. [PIAFv1.1](https://www.data.gouv.fr/en/datasets/piaf-le-dataset-francophone-de-questions-reponses/)
2. [FQuADv1.0](https://fquad.illuin.tech/)
3. [SQuAD-FR (SQuAD automatically translated to French)](https://github.com/Alikabbadj/French-SQuAD)

### Training


We are using 90 562 random questions for `train` and 22 391 for `dev`. No question in `train` exists in `dev`. For each question, we have a single `positive_context` (the paragraph where the answer to this question is found) and around 30 `hard_negtive_contexts`. Hard negative contexts are found by querying an ES instance (via bm25 retrieval) and getting the top-k candidates **that do not contain the answer**. 

The files are over [here](https://drive.google.com/file/d/1W5Jm3sqqWlsWsx2sFpA39Ewn33PaLQ7U/view?usp=sharing). 

### Evaluation


We use FQuADv1.0 and French-SQuAD evaluation sets.


## Training Script
We use the official [Facebook DPR implentation](https://github.com/facebookresearch/DPR) with a slight modification: by default, the code can work with Roberta models, still we changed a single line to make it easier to work with Camembert. This modification can be found [over here](https://github.com/psorianom/DPR).

### Hyperparameters

```shell
python -m torch.distributed.launch --nproc_per_node=8 train_dense_encoder.py \
 --max_grad_norm 2.0 \
 --encoder_model_type fairseq_roberta \
 --pretrained_file data/camembert-base \
 --seed 12345 \
 --sequence_length 256 \
 --warmup_steps 1237 \
 --batch_size 16 \
 --do_lower_case \
 --train_file ./data/DPR_FR_train.json \
 --dev_file  ./data/DPR_FR_dev.json \
 --output_dir ./output/ \
 --learning_rate 2e-05 \
 --num_train_epochs 35 \
 --dev_batch_size 16 \
 --val_av_rank_start_epoch 30 \
 --pretrained_model_cfg ./data/camembert-base/
```

### 

## Evaluation results
We obtain the following evaluation by using FQuAD and SQuAD-FR evaluation (or validation) sets. To obtain these results, we use [haystack's evaluation script](https://github.com/deepset-ai/haystack/blob/db4151bbc026f27c6d709fefef1088cd3f1e18b9/tutorials/Tutorial5_Evaluation.py) (**we report Retrieval results only**).

### DPR

#### FQuAD v1.0 Evaluation
```shell
For 2764 out of 3184 questions (86.81%), the answer was in the top-20 candidate passages selected by the retriever.
Retriever Recall: 0.87
Retriever Mean Avg Precision: 0.57
```
#### SQuAD-FR Evaluation  
```shell
For 8945 out of 10018 questions (89.29%), the answer was in the top-20 candidate passages selected by the retriever.
Retriever Recall: 0.89
Retriever Mean Avg Precision: 0.63
```

### BM25


For reference, BM25 gets the results shown below. As in the original paper, regarding SQuAD-like datasets, the results of DPR are consistently superseeded by BM25. 

#### FQuAD v1.0 Evaluation
```shell
For 2966 out of 3184 questions (93.15%), the answer was in the top-20 candidate passages selected by the retriever.
Retriever Recall: 0.93
Retriever Mean Avg Precision: 0.74
```
#### SQuAD-FR Evaluation
```shell
For 9353 out of 10018 questions (93.36%), the answer was in the top-20 candidate passages selected by the retriever.
Retriever Recall: 0.93
Retriever Mean Avg Precision: 0.77
```

## Usage

The results reported here are obtained with the `haystack` library. To get to similar embeddings using exclusively HF `transformers` library, you can do the following:

```python
from transformers import AutoTokenizer, AutoModel
query = "Salut, mon chien est-il mignon ?"
tokenizer = AutoTokenizer.from_pretrained("etalab-ia/dpr-ctx_encoder-fr_qa-camembert",  do_lower_case=True)
input_ids = tokenizer(query, return_tensors='pt')["input_ids"]
model = AutoModel.from_pretrained("etalab-ia/dpr-ctx_encoder-fr_qa-camembert", return_dict=True)
embeddings = model.forward(input_ids).pooler_output
print(embeddings)
```

And with `haystack`, we use it as a retriever:
```
retriever = DensePassageRetriever(
    document_store=document_store,
    query_embedding_model="etalab-ia/dpr-question_encoder-fr_qa-camembert",
    passage_embedding_model="etalab-ia/dpr-ctx_encoder-fr_qa-camembert",
    model_version=dpr_model_tag,
    infer_tokenizer_classes=True,
)
```

## Acknowledgments

This work was performed using HPC resources from GENCI–IDRIS (Grant 2020-AD011011224). 


## Citations

### Datasets

#### PIAF
```
@inproceedings{KeraronLBAMSSS20,
  author    = {Rachel Keraron and
               Guillaume Lancrenon and
               Mathilde Bras and
               Fr{\'{e}}d{\'{e}}ric Allary and
               Gilles Moyse and
               Thomas Scialom and
               Edmundo{-}Pavel Soriano{-}Morales and
               Jacopo Staiano},
  title     = {Project {PIAF:} Building a Native French Question-Answering Dataset},
  booktitle = {{LREC}},
  pages     = {5481--5490},
  publisher = {European Language Resources Association},
  year      = {2020}
}

```

#### FQuAD
```
@article{dHoffschmidt2020FQuADFQ,
  title={FQuAD: French Question Answering Dataset},
  author={Martin d'Hoffschmidt and Maxime Vidal and Wacim Belblidia and Tom Brendl'e and Quentin Heinrich},
  journal={ArXiv},
  year={2020},
  volume={abs/2002.06071}
}
```

#### SQuAD-FR
```
 @MISC{kabbadj2018,
   author =       "Kabbadj, Ali",
   title =        "Something new in French Text Mining and Information Extraction (Universal Chatbot): Largest Q&A French training dataset (110 000+) ",
   editor =       "linkedin.com",
   month =        "November",
   year =         "2018",
   url =          "\url{https://www.linkedin.com/pulse/something-new-french-text-mining-information-chatbot-largest-kabbadj/}",
   note =         "[Online; posted 11-November-2018]",
 }
 ```
### Models

#### CamemBERT
HF model card : [https://huggingface.co/camembert-base](https://huggingface.co/camembert-base)

```
@inproceedings{martin2020camembert,
  title={CamemBERT: a Tasty French Language Model},
  author={Martin, Louis and Muller, Benjamin and Su{\'a}rez, Pedro Javier Ortiz and Dupont, Yoann and Romary, Laurent and de la Clergerie, {\'E}ric Villemonte and Seddah, Djam{\'e} and Sagot, Beno{\^\i}t},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  year={2020}
}
```

#### DPR

```
@misc{karpukhin2020dense,
    title={Dense Passage Retrieval for Open-Domain Question Answering},
    author={Vladimir Karpukhin and Barlas Oğuz and Sewon Min and Patrick Lewis and Ledell Wu and Sergey Edunov and Danqi Chen and Wen-tau Yih},
    year={2020},
    eprint={2004.04906},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```