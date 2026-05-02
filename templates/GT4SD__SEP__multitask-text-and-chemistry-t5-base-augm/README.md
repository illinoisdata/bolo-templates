---
license: mit
language:
- en
---

# Multitask Text and Chemistry T5

Multitask Text and Chemistry T5 : a multi-domain, multi-task language model to solve a wide range of tasks in both the chemical and natural language domains. Published by [Christofidellis et al.](https://arxiv.org/pdf/2301.12586.pdf)

**Model Details**: The Multitask Text and Chemistry T5 variant trained using <em>t5-small</em> as its pretrained based and the <em>augmented dataset</em>. 

**Developers**: Dimitrios Christofidellis*, Giorgio Giannone*, Jannis Born, Teodoro Laino and Matteo Manica from IBM Research and Ole Winther from Technical University of Denmark.

**Distributors**: Model natively integrated into GT4SD.

**Model date**: 2023.

**Model type**: A Transformer-based language model that is trained on a multi-domain and a multi-task dataset by aggregating available datasets
for the tasks of Forward reaction prediction, Retrosynthesis, Molecular captioning, Text-conditional de novo generation and Paragraph to actions. 

**Information about training algorithms, parameters, fairness constraints or other applied approaches, and features**: 
N.A.

**Paper or other resource for more information**: 
The Multitask Text and Chemistry T5 [Christofidellis et al.(2023)](https://proceedings.mlr.press/v202/christofidellis23a.html)


**License**: MIT

**Where to send questions or comments about the model**: Open an issue on [GT4SD repository](https://github.com/GT4SD/gt4sd-core).

## Citation
```bib
@inproceedings{christofidellis2023unifying,
  title = 	 {Unifying Molecular and Textual Representations via Multi-task Language Modelling},
  author =       {Christofidellis, Dimitrios and Giannone, Giorgio and Born, Jannis and Winther, Ole and Laino, Teodoro and Manica, Matteo},
  booktitle = 	 {Proceedings of the 40th International Conference on Machine Learning},
  pages = 	 {6140--6157},
  year = 	 {2023},
  volume = 	 {202},
  series = 	 {Proceedings of Machine Learning Research},
  publisher =    {PMLR},
  pdf = 	 {https://proceedings.mlr.press/v202/christofidellis23a/christofidellis23a.pdf},
  url = 	 {https://proceedings.mlr.press/v202/christofidellis23a.html},
}
```

*equal contribution