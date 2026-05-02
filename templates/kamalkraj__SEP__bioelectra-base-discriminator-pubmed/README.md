## BioELECTRA:Pretrained Biomedical text Encoder using Discriminators

Recent advancements in pretraining strategies in NLP have shown a significant improvement in the performance of models on various text mining tasks. In this paper, we introduce BioELECTRA, a biomedical domain-specific language encoder model that adapts ELECTRA (Clark et al., 2020) for the Biomedical domain. BioELECTRA outperforms the previous models and achieves state of the art (SOTA) on all the 13 datasets in BLURB benchmark and on all the 4 Clinical datasets from BLUE Benchmark across 7 NLP tasks. BioELECTRA pretrained on PubMed and PMC full text articles performs very well on Clinical datasets as well. BioELECTRA achieves new SOTA 86.34%(1.39% accuracy improvement) on MedNLI and 64% (2.98% accuracy improvement) on PubMedQA dataset.

For a detailed description and experimental results, please refer to our paper [BioELECTRA:Pretrained Biomedical text Encoder using Discriminators](https://www.aclweb.org/anthology/2021.bionlp-1.16/).

Cite our paper using below citation 
```
@inproceedings{kanakarajan-etal-2021-bioelectra,
    title = "{B}io{ELECTRA}:Pretrained Biomedical text Encoder using Discriminators",
    author = "Kanakarajan, Kamal raj  and
      Kundumani, Bhuvana  and
      Sankarasubbu, Malaikannan",
    booktitle = "Proceedings of the 20th Workshop on Biomedical Language Processing",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.bionlp-1.16",
    doi = "10.18653/v1/2021.bionlp-1.16",
    pages = "143--154",
    abstract = "Recent advancements in pretraining strategies in NLP have shown a significant improvement in the performance of models on various text mining tasks. We apply {`}replaced token detection{'} pretraining technique proposed by ELECTRA and pretrain a biomedical language model from scratch using biomedical text and vocabulary. We introduce BioELECTRA, a biomedical domain-specific language encoder model that adapts ELECTRA for the Biomedical domain. WE evaluate our model on the BLURB and BLUE biomedical NLP benchmarks. BioELECTRA outperforms the previous models and achieves state of the art (SOTA) on all the 13 datasets in BLURB benchmark and on all the 4 Clinical datasets from BLUE Benchmark across 7 different NLP tasks. BioELECTRA pretrained on PubMed and PMC full text articles performs very well on Clinical datasets as well. BioELECTRA achieves new SOTA 86.34{\%}(1.39{\%} accuracy improvement) on MedNLI and 64{\%} (2.98{\%} accuracy improvement) on PubMedQA dataset.",
}
```


## How to use the discriminator in `transformers`

```python
from transformers import ElectraForPreTraining, ElectraTokenizerFast
import torch

discriminator = ElectraForPreTraining.from_pretrained("kamalkraj/bioelectra-base-discriminator-pubmed")
tokenizer = ElectraTokenizerFast.from_pretrained("kamalkraj/bioelectra-base-discriminator-pubmed")

sentence = "The quick brown fox jumps over the lazy dog"
fake_sentence = "The quick brown fox fake over the lazy dog"

fake_tokens = tokenizer.tokenize(fake_sentence)
fake_inputs = tokenizer.encode(fake_sentence, return_tensors="pt")
discriminator_outputs = discriminator(fake_inputs)
predictions = torch.round((torch.sign(discriminator_outputs[0]) + 1) / 2)

[print("%7s" % token, end="") for token in fake_tokens]

[print("%7s" % int(prediction), end="") for prediction in predictions[0].tolist()]
```