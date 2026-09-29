---
language:
- en
tags:
- interaction
- babylm-submission
- babylm-2025
---
# Model Card for BabyLM submission to the Interaction Track

<!-- Provide a quick summary of what the model is/does. [Optional] -->
A 124M model with the GPT-2 architecture trained with the next token prediction loss for 10 epochs (~900 M words) **on 90% of the BabyLM corpus** and an additional **1 M words of PPO RL** training as submission for the Interaction track of the 2025 BabyLM challenge.

This model card is based on the model card of the BabyLM [100M GPT-2 baseline](https://huggingface.co/BabyLM-community/babylm-baseline-100m-gpt2/edit/main/README.md).

#  Table of Contents

- [Model Card for Storytelling Submission Model](#model-card-for--model_id-)
- [Table of Contents](#table-of-contents)
- [Model Details](#model-details)
  - [Model Description](#model-description)
- [Uses](#uses)
- [Training Details](#training-details)
  - [Training Data](#training-data)
  - [Hyperparameters](#hyperparameters)
  - [Training Procedure](#training-procedure)
    - [Size and Checkpoints](#size-and-checkpoints)
- [Evaluation](#evaluation)
  - [Testing Data & Metrics](#testing-data-factors--metrics)
    - [Testing Data](#testing-data)
    - [Metrics](#metrics)
  - [Results](#results)
- [Technical Specifications](#technical-specifications-optional)
  - [Model Architecture and Objective](#model-architecture-and-objective)
  - [Compute Infrastructure](#compute-infrastructure)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Training Time](#training-time)
- [Citation](#citation)
- [Model Card Authors](#model-card-authors-optional)
- [Bibliography](#bibliography)


# Model Details

## Model Description

<!-- Provide a longer summary of what this model is/does. -->
This is the RL storytelling model, based on a [pretrained GPT-2 model](https://huggingface.co/llm-slice/blm-gpt2s-90M-s42), for the Interaction Track of the 2025 BabyLM challenge.

- **Developed by:** Jonas Mayer Martins, Ali Hamza Bashir, Muhammad Rehan Khalid
- **Model type:** Causal language model
- **Language(s) (NLP):** eng
- **Resources for more information:**
    - [GitHub Repo](https://github.com/malihamza/babylm-interactive-learning)


# Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
This is a pre-trained language model.
It can be used to evaluate tasks in a zero-shot manner and also can be fine-tuned for downstream tasks.
It can be used for language generation but given its small size and low number of words trained on, do not expect LLM-level performance.

# Training Details

## Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

We used the BabyLM 100M (Strict) dataset for training. **We trained the tokenizer and model on randomly selected 90% of the corpus**, which is composed of the following:

| Source | Weight | Domain | Citation | Website | License |
| --- | --- | --- | --- | --- | --- |
| BNC | 8% | Dialogue | BNC Consortium (2007) | [link](http://www.natcorp.ox.ac.uk/) | [link](http://www.natcorp.ox.ac.uk/docs/licence.html) <sup>1</sup> |
| CHILDES | 29% | Dialogue, Child-Directed | MacWhinney (2000) | | [link](https://talkbank.org/share/rules.html) |
| Project Gutenberg | 26% | Fiction, Nonfiction | Gerlach & Font-Clos (2020) | [link](https://github.com/pgcorpus/gutenberg) | [link](https://www.gutenberg.org/policy/license.html) |
| OpenSubtitles | 20% | Dialogue, Scripted | Lison & Tiedermann (2016) | [link](https://opus.nlpl.eu/OpenSubtitles-v2018.php) | Open source |
| Simple English Wikipedia | 15% | Nonfiction | -- | [link](https://dumps.wikimedia.org/simplewiki/20221201/) | [link](https://dumps.wikimedia.org/legal.html) |
| Switchboard | 1% | Dialogue | Godfrey et al. (1992), Stolcke et al., (2000) | [link](http://compprag.christopherpotts.net/swda.html) | [link](http://compprag.christopherpotts.net/swda.html) |

<sup>1</sup> Our distribution of part of the BNC Texts is permitted under the fair dealings provision of copyright law (see term (2g) in the BNC license).

## Hyperparameters PPO RL training

| **Parameter**                   | **Value**           |
|----------------------------------|---------------------|
| Student context length           | 512                 |
| seed                             | 42                  |
| batch size                       | 360                 |
| Student sampling temperature     | 1                   |
| top_k                            | 0                   |
| top_p                            | 1                   |
| max_new_tokens (student)         | 90                  |
| Teacher model                    | Llama 3.1 8B Instr. |
| Teacher context length           | 1024                |
| max_new_tokens (teacher)         | 6                   |
| gradient_accumulation_steps      | 1                   |
| adap_kl_ctrl                     | True                |
| init_kl_coef                     | 0.2                 |
| learning_rate                    | 1×10⁻⁶              |
| Student input limit              | 1 M words           |

## Hyperparameters Pretraining

| Hyperparameter | Value |
| --- | --- |
| Number of epochs | 10 |
| Datapoint length | 512 |
| Batch size | 16 |
| Gradient accumulation steps | 4 |
| Learning rate | 0.0005 |
| Number of steps | 211650 |
| Warmup steps | 2116 |
| Gradient clipping | 1 |
| Optimizer | AdamW |
| Optimizer Beta_1 | 0.9 |
| Optimizer Beta_2 | 0.999 |
| Optimizer Epsilon | 10<sup>-8</sup>|
| Tokenizer | BytePairBPE |
| Vocab Size | 16000 |

## Training Procedure

The model is trained with next token prediction loss for 10 epochs.

### Size and checkpoints

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

The model has 124M parameters.
In total we train on around 901 M words and provide multiple checkpoints from the training.
Specifically we provode:
- Checkpoints every 1 M words for the first 10 M words
- Checkpoints every 10 M words first 100 M words
- Checkpoints every 100 M words until 900 M words
- Checkpoints every 100 K words until 901 M words

 
# Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

This model is evaluated in two ways:
1. We do zero-shot evaluation on 7 tasks.
2. We do fine-tuning on a subset of the (Super)GLUE tasks (Wang et al., ICLR 2019; Wang et al., NeurIPS 2019) .

## Testing Data & Metrics

### Testing Data

<!-- This should link to a Data Card if possible. -->

For the BLiMP, BLiMP supplement, and EWoK tasks, we use a filtered version of the dataset to only include examples with words found in the BabyLM dataset.
For the Finetuning task, we both filter and sample down to a maximum 10 000 train examples.

*Validation Data*

*Zero-shot Tasks*

- **BLiMP**: The Benchmark of Linguistic Minimal Pairs evaluates the model's linguistic ability by seeing if it can recognize the grammatically correct sentence from a pair of minimally different sentences. It tests various grammatical phenomena.(Warstadt et al., TACL 2020)
- **BLiMP Supplement**: A supplement to BLiMP introduced in the first edition of the BabyLM challenge. More focused on dialogue and questions. (Warstadt et al., CoNLL-BabyLM 2023)
- **EWoK**: Works similarly to BLiMP but looks the model's internal world knowledge. Looking at both whter a model has physical and social knowledge. (Ivanova et al., 2024)
- **Eye Tracking and Self-paced Reading**: Looks at whether the model can mimick the eye tracking and reading time of a human but using surprisal of a word as a proxy for time spent reading a word. (de Varda et al., BRM 2024)
- **Entity Tracking**: Checks whether a model can keep track of the changes to the states of entities as text/dialogue unfolds. (Kim & Schuster, ACL 2023)
- **WUGs**: Tests morphological generalization in LMs through an adjective nominalization and past tense task. (Hofmann et al., 2024) (Weissweiler et al., 2023)
- **COMPS**: Property knowledge. (Misra et al., 2023)

*Finetuning Tasks*

- **BoolQ**: A yes/no QA dataset with unprompted and unconstrained questions. (Clark et al., NAACL 2019)
- **MNLI**: The Multi-Genre Natural Language Inference corpus tests the language understanding of a model by seeing wehther it can recognize textual entailment. (Williams et al., NAACL 2018)
- **MRPC**: The Microsoft Research Paraphrase Corpus contains pairs of sentences that are either paraphrases/semntically equivalent to each other or unrelated.(Dolan & Brockett, IJCNLP 2005)
- **QQP**<sup>2</sup>: Similarly to MRPC, the Quora Question Pairs corpus tests the models ability to determine whether a pair of questions are sematically similar to each other. These questions are sourced from Quora.
- **MultiRC**: The Multi-Sentence Reading Comprehension corpus is a QA task that evaluates the model's ability to the correct answer from a list of answers given a question and context paragraph. In this version the data is changed to a binary classification judging whether the answer to a question, context pair is correct. (Khashabi et al., NAACL 2018)
- **RTE**: Similar the Recognizing Text Entailement tests the model's ability to recognize text entailement. (Dagan et al., Springer 2006; Bar et al., 2006; Giampiccolo et al., 2007; Bentivogli et al., TAC 2009)
- **WSC**: The Winograd Schema Challenge tests the models ability to do coreference resolution on sentences with a pronoun and a list of noun phrases found in the sentence. This version edits it to be a binary classification on examples consisting of a pronoun and noun phrase.(Levesque et al., PKRR 2012)

<sup>2</sup> https://www.quora.com/profile/Ricky-Riche-2/First-Quora-Dataset-Release-Question-Pairs

### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

The metrics used to evaluate the model are the following:
- Zero-shot
  - Accuracy on predicting the correct completion/sentence for BLiMP, BLiMP Supplement, EWoK, Entity Tracking, and WUGs
  - Change in R^2 prediction from baseline for Eye Tracking (with no spillover) and Self-paced Reading (1-word spillover)
- Finetuning
  - 3 class Accuracy for MNLI
  - Binary Accuracy for BoolQ, MultiRC, and WSC
  - F1-score for MRPC and QQP

The metrics were chosen based on the advice of the papers the tasks come from.

### Hyperparameters

| Hyperparameter | MNLI, RTE, QQP, MRPC, BoolQ, MultiRC | WSC |
| --- | --- | --- |
| Learning Rate | 3\*10<sup>-5</sup> | 3\*10<sup>-5</sup> |
| Batch Size | 16 | 16 |
| Epochs | 10 | 30 |
| Weight decay | 0.01  | 0.01 |
| Optimizer | AdamW | AdamW |
| Scheduler | cosine | cosine |
| Warmup percentage | 6% | 6% |
| Dropout | 0.1 | 0.1 |

## Results

We compare our student model against two official baselines from the 2025 BabyLM Challenge<sup>1</sup>:

- **1000M-pre:** The standard *pretraining* baseline, using a GPT-2-small model trained on 100M unique words from the BabyLM dataset (10 epochs, next-word prediction).
- **SimPO:** A baseline first trained for 7 epochs with next-word prediction, then 2 epochs *interleaving* prediction and reinforcement learning. Here, the RL reward encourages the student to generate completions similar to the teacher’s output.
- **900M-pre:** Our model, using the same GPT-2-small architecture, pretrained on 90% of the BabyLM dataset (yielding approximately 91M unique words, 10 epochs).
- **900M-RL:** Our model after additional PPO-based reinforcement learning with the teacher, using about 1M words as input for the interactive (RL) phase.

---

### Evaluation Results

| **Task**      | **1000M-pre** | **SimPO** | **900M-pre** | **900M-RL** |
|:------------- | ------------: | ---------:| ------------:| -----------:|
| BLiMP         | 74.88         | 72.16     | 77.52        | **77.53**   |
| Suppl.        | **63.32**     | 61.22     | 56.62        | 56.72       |
| EWOK          | 51.67         | **51.92** | 51.36        | 51.41       |
| COMPS         | **56.17**     | 55.05     | 55.20        | 55.18       |
| ET            | 31.51         | 28.06     | 30.34        | **33.11**   |
| GLUE          | 52.18         | 50.35     | **53.14**    | 52.46       |

#### Model descriptions:
- **1000M-pre:** Baseline pretrained on 100M words (BabyLM challenge baseline).
- **SimPO:** Baseline using a hybrid of pretraining and RL with a similarity-based reward.
- **900M-pre:** Our GPT-2-small model, pretrained on 90M words (similar settings as baseline, but less data).
- **900M-RL:** The same model as 900M-pre, further trained with PPO using teacher feedback on 1M words of input.
- 
See: [BabyLM Challenge](https://huggingface.co/BabyLM-community) for the baselines. 

# Technical Specifications

### Hardware

- 4 A100 GPUs were used to train this model.

### Software

PyTorch

### Training Time

The model took 20 hours to train and consumed 53560 core hours (with 4 GPUs and 32 CPUs).

# Citation

```latex
@misc{MayerMartinsBKB2025,
      title={ToDo}, 
      author={Jonas Mayer Martins, Ali Hamza Bashir, Muhammad Rehan Khalid, Lisa Beinborn},
      year={2025},
      eprint={2502.TODO},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={ToDo}, 
}
```

# Model Card Authors

Jonas Mayer Martins

# Bibliography

[GLUE: A multi-task benchmark and analysis platform for natural language understanding](https://openreview.net/pdf?id=rJ4km2R5t7) (Wang et al., ICLR 2019)

[SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems](https://proceedings.neurips.cc/paper_files/paper/2019/file/4496bf24afe7fab6f046bf4923da8de6-Paper.pdf) (Wang et al., NeurIPS 2019)

[BLiMP: The Benchmark of Linguistic Minimal Pairs for English](https://aclanthology.org/2020.tacl-1.25/) (Warstadt et al., TACL 2020)

[Findings of the BabyLM Challenge: Sample-Efficient Pretraining on Developmentally Plausible Corpora](https://aclanthology.org/2023.conll-babylm.1/) (Warstadt et al., CoNLL-BabyLM 2023)

[🌏 Elements of World Knowledge (EWoK): A cognition-inspired framework for evaluating basic world knowledge in language models](https://arxiv.org/pdf/2405.09605v1) (Ivanova et al., 2024)

[Cloze probability, predictability ratings, and computational estimates for 205 English sentences, aligned with existing EEG and reading time data](https://link.springer.com/article/10.3758/s13428-023-02261-8) (de Varda et al., BRM 2024)

[Entity Tracking in Language Models](https://aclanthology.org/2023.acl-long.213/) (Kim & Schuster, ACL 2023)

[Derivational Morphology Reveals Analogical Generalization in Large Language Models](https://arxiv.org/pdf/2411.07990) (Hofmann et al., 2024)

[Automatically Constructing a Corpus of Sentential Paraphrases](https://aclanthology.org/I05-5002/) (Dolan & Brockett, IJCNLP 2005)

[A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference](https://aclanthology.org/N18-1101/) (Williams et al., NAACL 2018)

[The Winograd Schema Challenge]( http://dl.acm.org/citation.cfm?id=3031843.3031909) (Levesque et al., PKRR 2012)

[The PASCAL Recognising Textual Entailment Challenge](https://link.springer.com/chapter/10.1007/11736790_9) (Dagan et al., Springer 2006)

[The Second PASCAL Recognising Textual Entailment Challenge]() (Bar et al., 2006)

[The Third PASCAL Recognizing Textual Entailment Challenge](https://aclanthology.org/W07-1401/) (Giampiccolo et al., 2007)

[The Fifth PASCAL Recognizing Textual Entailment Challenge](https://tac.nist.gov/publications/2009/additional.papers/RTE5_overview.proceedings.pdf) (Bentivogli et al., TAC 2009)

[BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions](https://aclanthology.org/N19-1300/) (Clark et al., NAACL 2019)

[Looking Beyond the Surface: A Challenge Set for Reading Comprehension over Multiple Sentences](https://aclanthology.org/N18-1023/) (Khashabi et al., NAACL 2018)