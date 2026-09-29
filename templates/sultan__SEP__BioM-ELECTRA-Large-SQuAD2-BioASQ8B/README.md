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
- This model is fine-tuned on the SQuAD2.0 dataset and then on the BioASQ8B-Factoid training dataset. We convert the BioASQ8B-Factoid training dataset to SQuAD1.1 format and train and evaluate our model (BioM-ELECTRA-Base-SQuAD2) on this dataset.

- You can use this model to make a prediction (inference) directly without fine-tuning it. Try to enter a PubMed abstract in the context box in this model card and try out a couple of biomedical questions within the given context and see how it performs compared to ELECTRA original model. This model should also be useful for creating a pandemic QA system (e.g., COVID-19) . 

- Please note that this version (PyTorch) is different than what we used in our participation in BioASQ9B (TensorFlow with Layer-Wise Decay). We combine all five batches of the BioASQ8B testing dataset as one dev.json file.


- Below is unofficial results of our models against the original ELECTRA base and large :


| Model | Exact Match (EM) | F1 Score  | 
| ---  | --- | --- |
| ELECTRA-Base-SQuAD2-BioASQ8B | 61.89 | 74.39 |
| BioM-ELECTRA-Base-SQuAD2-BioASQ8B  | 70.31 | 80.90 |
| ELECTRA-Large-SQuAD2-BioASQ8B | 67.36 | 78.90 |
| **BioM-ELECTRA-Large-SQuAD2-BioASQ8B** | **74.31** | **84.72** |



Training script

```python
python3 run_squad.py --model_type electra --model_name_or_path sultan/BioM-ELECTRA-Large-SQuAD2 \
--train_file BioASQ8B/train.json \
--predict_file BioASQ8B/dev.json \
--do_lower_case \
--do_train \
--do_eval \
--threads 20 \
--version_2_with_negative \
--num_train_epochs 3 \
--learning_rate 5e-5 \
--max_seq_length 512 \
--doc_stride 128 \
--per_gpu_train_batch_size 8 \
--gradient_accumulation_steps 2  \
--per_gpu_eval_batch_size 128   \
--logging_steps 50 \
--save_steps 5000 \
--fp16 \
--fp16_opt_level O1 \
--overwrite_output_dir \
--output_dir BioM-ELECTRA-Large-SQuAD-BioASQ \
--overwrite_cache
```

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