# BioM-Transformers: Building Large Biomedical Language Models with BERT, ALBERT and ELECTRA

# Abstract


The impact of design choices on the performance
of biomedical language models recently
has been a subject for investigation. In
this paper, we empirically study biomedical
domain adaptation with large transformer models
using different design choices. We evaluate
the performance of our pretrained models
against other existing biomedical language
models in the literature. Our results show that
we achieve state-of-the-art results on several
biomedical domain tasks despite using similar
or less computational cost compared to other
models in the literature. Our findings highlight
the significant effect of design choices on
improving the performance of biomedical language
models.

# Model Description

We fine-tuned BioM-ELECTRA-Large, which was pre-trained on PubMed Abstracts, on the SQuAD2.0 dataset. Fine-tuning the biomedical language model on the SQuAD dataset helps improve the score on the BioASQ challenge. If you plan to work with BioASQ or biomedical QA tasks, it's better to use this model over BioM-ELECTRA-Large. This model (TensorFlow version ) took the lead in the BioASQ9b-Factoid challenge (Batch 5) under the name of (UDEL-LAB2). To see the full details of BioASQ9B results, please check this link http://participants-area.bioasq.org/results/9b/phaseB/ ( you need to register). 

Huggingface library doesn't implement Layer-Wise decay feature, which affects the performance on SQuAD task. The reported result of BioM-ELECTRA-SQuAD in our paper is 88.3 (F1) since we use ELECTRA open-source code with TF checkpoint, which uses Layer-Wise decay. 


Training Script

```python
run_qa.py --model_name_or_path sultan/BioM-ELECTRA-Large-Discriminator \
--dataset_name squad_v2 \
--do_train \
--do_eval \
--dataloader_num_workers 20 \
--preprocessing_num_workers 20 \
--version_2_with_negative \
--num_train_epochs 2 \
--learning_rate 5e-5 \
--max_seq_length 512 \
--doc_stride 128 \
--per_device_train_batch_size 8 \
--gradient_accumulation_steps 6 \
--per_device_eval_batch_size 128 
--fp16 \
--fp16_opt_level O1 \
--logging_steps 50 \
--save_steps 1000 \
--overwrite_output_dir \
--output_dir out
```

Evaluation results on SQuAD2.0 Dev Dataset
```
exact = 84.33420365535248
f1 = 87.49354241889522
total = 11873
HasAns_exact = 80.43184885290148
HasAns_f1 = 86.75958656200127
HasAns_total = 5928
NoAns_exact = 88.22539949537426
NoAns_f1 = 88.22539949537426
NoAns_total = 5945
best_exact = 84.33420365535248
best_exact_thresh = 0.0
best_f1 = 87.49354241889522
best_f1_thresh = 0.0
epoch = 2.0

```

To reproduce results in Google Colab:
- Make sure you have GPU enabled.
- Clone and install required libraries through this code

!git  clone https://github.com/huggingface/transformers

!pip3 install -e transformers

!pip3 install sentencepiece

!pip3 install -r /content/transformers/examples/pytorch/question-answering/requirements.txt

- Run this python code:

```python
python /content/transformers/examples/pytorch/question-answering/run_qa.py --model_name_or_path sultan/BioM-ELECTRA-Large-SQuAD2 \
--do_eval \
--version_2_with_negative \
--per_device_eval_batch_size 8 \
--dataset_name squad_v2 \
--overwrite_output_dir \
--fp16 \
--output_dir out
```

- You don't need to download the SQuAD2 dataset. The code will download it from the HuggingFace datasets hub.

- Check our GitHub repo at https://github.com/salrowili/BioM-Transformers for TensorFlow and GluonNLP checkpoints. 

- We added examples to fine-tune BioM-ELECTRA-Large on SQuAD and BioASQ7B using TensorFlow and TPU here https://github.com/salrowili/BioM-Transformers/tree/main/examples .  In this example we show that we achieve 88.22 score in SQuAD2.0 since Tensor Flow code has Layer-wise decay feature.

# Acknowledgment

We would like to acknowledge the support we have from Tensorflow Research Cloud (TFRC) team to grant us access to TPUv3 units.

# Citation


```bibtex
@inproceedings{alrowili-shanker-2021-biom,
title = "{B}io{M}-Transformers: Building Large Biomedical Language Models with {BERT}, {ALBERT} and {ELECTRA}",
author = "Alrowili, Sultan and
Shanker, Vijay",
booktitle = "Proceedings of the 20th Workshop on Biomedical Language Processing",
month = jun,
year = "2021",
address = "Online",
publisher = "Association for Computational Linguistics",
url = "https://www.aclweb.org/anthology/2021.bionlp-1.24",
pages = "221--227",
abstract = "The impact of design choices on the performance of biomedical language models recently has been a subject for investigation. In this paper, we empirically study biomedical domain adaptation with large transformer models using different design choices. We evaluate the performance of our pretrained models against other existing biomedical language models in the literature. Our results show that we achieve state-of-the-art results on several biomedical domain tasks despite using similar or less computational cost compared to other models in the literature. Our findings highlight the significant effect of design choices on improving the performance of biomedical language models.",
}
```