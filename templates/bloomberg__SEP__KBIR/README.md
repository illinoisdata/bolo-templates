---
license: apache-2.0
---
# Keyphrase Boundary Infilling with Replacement (KBIR)
The KBIR model as described in "Learning Rich Representations of Keyphrases from Text" from Findings of NAACL 2022 (https://aclanthology.org/2022.findings-naacl.67.pdf) builds on top of the RoBERTa architecture by adding an Infilling head and a Replacement Classification head that is used during pre-training. However, these heads are not used during the downstream evaluation of the model and we only leverage the pre-trained embeddings. Discarding the heads thereby allows us to be compatible with all AutoModel classes that RoBERTa supports.

We provide examples on how to perform downstream evaluation on some of the tasks reported in the paper.

## Downstream Evaluation

### Keyphrase Extraction
```
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("bloomberg/KBIR")
model = AutoModelForTokenClassification.from_pretrained("bloomberg/KBIR")

from datasets import load_dataset

dataset = load_dataset("midas/semeval2017_ke_tagged")
```

Reported Results:

| Model                 | Inspec | SE10  | SE17  |
|-----------------------|--------|-------|-------|
| RoBERTa+BiLSTM-CRF    | 59.5   | 27.8  | 50.8  |
| RoBERTa+TG-CRF        | 60.4   | 29.7  | 52.1  |
| SciBERT+Hypernet-CRF  | 62.1   | 36.7  | 54.4  |
| RoBERTa+Hypernet-CRF  | 62.3   | 34.8  | 53.3  |
| RoBERTa-extended-CRF* | 62.09  | 40.61 | 52.32 |
| KBI-CRF*              | 62.61  | 40.81 | 59.7  |
| KBIR-CRF*             | 62.72  | 40.15 | 62.56 |

### Named Entity Recognition
```
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("bloomberg/KBIR")
model = AutoModelForTokenClassification.from_pretrained("bloomberg/KBIR")

from datasets import load_dataset

dataset = load_dataset("conll2003")
```

Reported Results:

| Model                           | F1    |
|---------------------------------|-------|
| LSTM-CRF (Lample et al., 2016)  | 91.0  |
| ELMo (Peters et al., 2018)      | 92.2  |
| BERT (Devlin et al., 2018)      | 92.8  |
| (Akbik et al., 2019)            | 93.1  |
| (Baevski et al., 2019)          | 93.5  |
| LUKE (Yamada et al., 2020)      | 94.3  |
| LUKE w/o entity attention       | 94.1  |
| RoBERTa (Yamada et al., 2020)   | 92.4  |
| RoBERTa-extended*               | 92.54 |
| KBI*                            | 92.73 |
| KBIR*                           | 92.97 |

### Question Answering
```
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("bloomberg/KBIR")
model = AutoModelForQuestionAnswering.from_pretrained("bloomberg/KBIR")

from datasets import load_dataset

dataset = load_dataset("squad")
```
Reported Results:

| Model                  | EM    | F1    |
|------------------------|-------|-------|
| BERT                   | 84.2  | 91.1  |
| XLNet                  | 89.0  | 94.5  |
| ALBERT                 | 89.3  | 94.8  |
| LUKE                   | 89.8  | 95.0  |
| LUKE w/o entity attention | 89.2  | 94.7  |
| RoBERTa                | 88.9  | 94.6  |
| RoBERTa-extended*      | 88.88 | 94.55 |
| KBI*                   | 88.97 | 94.7  |
| KBIR*                  | 89.04 | 94.75 |

## Any other classification task
As mentioned above since KBIR is built on top of the RoBERTa architecture, it is compatible with any AutoModel setting that RoBERTa is also compatible with. 

We encourage you to try fine-tuning KBIR on different datasets and report the downstream results.

## Citation

Please cite this work using the following BibTeX entry:

```
@inproceedings{kulkarni-etal-2022-learning,
    title = "Learning Rich Representation of Keyphrases from Text",
    author = "Kulkarni, Mayank  and
      Mahata, Debanjan  and
      Arora, Ravneet  and
      Bhowmik, Rajarshi",
    booktitle = "Findings of the Association for Computational Linguistics: NAACL 2022",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-naacl.67",
    doi = "10.18653/v1/2022.findings-naacl.67",
    pages = "891--906",
    abstract = "In this work, we explore how to train task-specific language models aimed towards learning rich representation of keyphrases from text documents. We experiment with different masking strategies for pre-training transformer language models (LMs) in discriminative as well as generative settings. In the discriminative setting, we introduce a new pre-training objective - Keyphrase Boundary Infilling with Replacement (KBIR), showing large gains in performance (upto 8.16 points in F1) over SOTA, when the LM pre-trained using KBIR is fine-tuned for the task of keyphrase extraction. In the generative setting, we introduce a new pre-training setup for BART - KeyBART, that reproduces the keyphrases related to the input text in the CatSeq format, instead of the denoised original input. This also led to gains in performance (upto 4.33 points in F1@M) over SOTA for keyphrase generation. Additionally, we also fine-tune the pre-trained language models on named entity recognition (NER), question answering (QA), relation extraction (RE), abstractive summarization and achieve comparable performance with that of the SOTA, showing that learning rich representation of keyphrases is indeed beneficial for many other fundamental NLP tasks.",
}
```

## Contact
For any questions contact dmahata@bloomberg.net