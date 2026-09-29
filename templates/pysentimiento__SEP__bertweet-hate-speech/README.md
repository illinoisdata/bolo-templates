---
language: 
  - en
library_name: pysentimiento

tags:
  - twitter
  - hate-speech

---
# Hate Speech detection in English
## bertweet-hate-speech

Repository: [https://github.com/pysentimiento/pysentimiento/](https://github.com/finiteautomata/pysentimiento/)



Model trained with SemEval 2019 Task 5: HatEval (SubTask B) corpus for Hate Speech detection in English. Base model is [BERTweet](https://huggingface.co/vinai/bertweet-base), a RoBERTa model trained in English tweets.

It is a multi-classifier model, with the following classes:

- **HS**: is it hate speech?
- **TR**: is it targeted to a specific individual?
- **AG**: is it aggressive?


## License

`pysentimiento` is an open-source library for non-commercial use and scientific research purposes only. Please be aware that models are trained with third-party datasets and are subject to their respective licenses. 

1. [TASS Dataset license](http://tass.sepln.org/tass_data/download.php)
2. [SEMEval 2017 Dataset license]()

## Citation

If you use this model in your work, please cite the following papers:

```
@misc{perez2021pysentimiento,
      title={pysentimiento: A Python Toolkit for Sentiment Analysis and SocialNLP tasks},
      author={Juan Manuel Pérez and Juan Carlos Giudici and Franco Luque},
      year={2021},
      eprint={2106.09462},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@inproceedings{nguyen2020bertweet,
  title={BERTweet: A pre-trained language model for English Tweets},
  author={Nguyen, Dat Quoc and Vu, Thanh and Nguyen, Anh Tuan},
  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
  pages={9--14},
  year={2020}
}

@inproceedings{basile2019semeval,
  title={Semeval-2019 task 5: Multilingual detection of hate speech against immigrants and women in twitter},
  author={Basile, Valerio and Bosco, Cristina and Fersini, Elisabetta and Nozza, Debora and Patti, Viviana and Pardo, Francisco Manuel Rangel and Rosso, Paolo and Sanguinetti, Manuela},
  booktitle={Proceedings of the 13th international workshop on semantic evaluation},
  pages={54--63},
  year={2019}
}
```
Enjoy! 🤗