---
license: mit
language:
- en
library_name: fasttext
pipeline_tag: text-classification
inference: false
datasets:
- kenhktsui/llm-data-textbook-quality-v2
---


# 📚llm-data-textbook-quality-fasttext-classifier-v2

[**Blog**](https://huggingface.co/blog/kenhktsui/edu-value-classifier-cpu) | [**Dataset**](https://huggingface.co/datasets/kenhktsui/llm-data-textbook-quality-v2)

## Update
2024-07-07: quantized model "model_quantized.bin" is released.
```
model = fasttext.load_model(hf_hub_download("kenhktsui/llm-data-textbook-quality-fasttext-classifer-v2", "model_quantized.bin"))
```

![image/png](https://cdn-uploads.huggingface.co/production/uploads/60e50ce5350d181892d5a636/acAPg-_NawdIfE2XXwcgc.png)


## **"Garbage in, garbage out. A language model is only as good as its training data irrespective of its parameter count."**

📚  The educational value classifier can classify if a text from web has high educational value (more explicitly defined then textbook quality).  It is deeply inspired by [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644), where a classifier was developed to predict the educational value of data, and was then used for data filtering. 
The model is trained on web/ raw text, not on data formatted as instruction dataset (yet).  
It can be used as a filter for pretraining data curation when training a LLM 🤖.  
There are 3 labels instead of 2 labels, as it offers higher granularity of educational value.
- High (Top 25% educational value)
- Mid (Middle 25-75% educational value)
- Low (Bottom 25% educational value)

A detailed report/ paper will follow when more downstream experiments of this classifier become available.   
About the validation of this classifier. See [**Analysis**](https://huggingface.co/kenhktsui/llm-data-textbook-quality-fasttext-classifer-v2#%F0%9F%93%88analysis).   
The classifier had been applied to various pretraining dataset. See [**Benchmark**](https://huggingface.co/kenhktsui/llm-data-textbook-quality-fasttext-classifer-v2#%F0%9F%93%8Abenchmark)  

⚡ Model is built on fasttext - it can classify more than 2000 examples per second in CPU, and so it can be used **on-the-fly** during pretraining.  

Please note textbook quality is a subset of high quality.

## 💬Feedback welcomed!
Please give a like and leave a comment if you find this model helpful. I am in a continual journey to make LLM data curation better and easier.


## ✏️Examples
Educational value is [0, 2]. Detailed formula is explained below.
```python
predict_educational_value(['''Logic is the study of correct reasoning. It includes both formal and informal logic. Formal logic is the study of deductively valid inferences or logical truths. It examines how conclusions follow from premises due to the structure of arguments alone, independent of their topic and content. Informal logic is associated with informal fallacies, critical thinking, and argumentation theory. It examines arguments expressed in natural language while formal logic uses formal language. When used as a countable noun, the term "a logic" refers to a logical formal system that articulates a proof system. Logic plays a central role in many fields, such as philosophy, mathematics, computer science, and linguistics.'''])
# Output [1.9266871362924576]
predict_educational_value(['''"Attention Is All You Need" is a landmark[1][2] 2017 research paper authored by eight scientists working at Google, responsible for expanding 2014 attention mechanisms proposed by Bahdanau et al. into a new deep learning architecture known as the transformer. The paper is considered by some to be a founding document for modern artificial intelligence, as transformers became the main architecture of large language models.[3][4] At the time, the focus of the research was on improving Seq2seq techniques for machine translation, but even in their paper the authors saw the potential for other tasks like question answering and for what is now called multimodal Generative AI.[5]'''])
# Output [1.8226698189973831]
predict_educational_value(['''A large language model (LLM) is a computational model notable for its ability to achieve general-purpose language generation and other natural language processing tasks such as classification. Based on language models, LLMs acquire these abilities by learning statistical relationships from text documents during a computationally intensive self-supervised and semi-supervised training process.[1] LLMs can be used for text generation, a form of generative AI, by taking an input text and repeatedly predicting the next token or word.[2]'''])
# Output [1.7609568238258362]
predict_educational_value(['''In Vapnik–Chervonenkis theory, the Vapnik–Chervonenkis (VC) dimension is a measure of the size (capacity, complexity, expressive power, richness, or flexibility) of a class of sets. The notion can be extended to classes of binary functions. It is defined as the cardinality of the largest set of points that the algorithm can shatter, which means the algorithm can always learn a perfect classifier for any labeling of at least one configuration of those data points. It was originally defined by Vladimir Vapnik and Alexey Chervonenkis.[1]'''])
# Output [1.589950144290924]
predict_educational_value(['''The query vector is compared (via dot product) with each word in the keys. This helps the model discover the most relevant word for the query word. In this case "girl" was determined to be the most relevant word for "that". The result (size 4 in this case) is run through the softmax function, producing a vector of size 4 with probabilities summing to 1. Multiplying this against the value matrix effectively amplifies the signal for the most important words in the sentence and diminishes the signal for less important words.[5] The structure of the input data is captured in the Wq and Wk weights, and the Wv weights express that structure in terms of more meaningful features for the task being trained for. For this reason, the attention head components are called Query (Wq), Key (Wk), and Value (Wv)—a loose and possibly misleading analogy with relational database systems.'''])
# Output [1.4657384157180786]
predict_educational_value(['''The Arsenal Football Club (commonly known as simply Arsenal) is an English professional football club based in Holloway, North London. Arsenal compete in the Premier League, the top flight of English football. In domestic football, Arsenal has won 13 league titles (including one unbeaten title), a record 14 FA Cups, two League Cups, 17 FA Community Shields, and a Football League Centenary Trophy. In European football, they have one European Cup Winners' Cup and one Inter-Cities Fairs Cup. In terms of trophies won, it is the third-most successful club in English football.[2]'''])
# Output [1.1015518307685852]
predict_educational_value(['''The 2003–04 season was Arsenal Football Club's 12th season in the Premier League and their 78th consecutive season in the top flight of English football.[3][4] It began on 1 July 2003 and concluded on 30 June 2004, with competitive matches played between August and May. The club ended the Premier League campaign as champions without a single defeat – a record of 26 wins and 12 draws. Arsenal fared less well in the cups, eliminated in the FA Cup and League Cup semi-finals to Manchester United and Middlesbrough respectively, and at the quarter-final stage of the UEFA Champions League to Chelsea.'''])
# Output [1.0146622359752655]
predict_educational_value(['''As both teams' first-choice kits featured a shade of red, Arsenal wore their yellow away strip, while Barcelona wore their traditional blue and maroon striped kit. Arsenal won the coin toss and Barcelona kicked off.[21] Barcelona almost immediately came under pressure when Thierry Henry shot straight at Barcelona goalkeeper Víctor Valdés, who conceded a corner. From the resulting corner Arsenal had another chance again courtesy of Henry, whose shot was again saved by Valdés. The next attack in the seventh minute resulted in Arsenal goalkeeper Jens Lehmann saving from Ludovic Giuly after he shot from a narrow angle. Four minutes later Barcelona were awarded a free-kick 35 yards from goal; Ronaldinho shot wide of the goal.'''])
# Output [0.7897453680634499]
```
From inspection, it can be noted that the model does like scientific knowledge.
It is also interested in Arsenal as a football club, however, it does not think a summary of a particular match has good educational value.


## 🛠️Usage
```python
from typing import List
import re
from huggingface_hub import hf_hub_download
import fasttext


model = fasttext.load_model(hf_hub_download("kenhktsui/llm-data-textbook-quality-fasttext-classifer-v2", "model.bin"))


def replace_newlines(text: str) -> str:
  return re.sub("\n+", " ", text)


score_dict = {
  '__label__': 0, 
  '__label__Low': 0, 
  '__label__Mid': 1,
  '__label__High': 2
}


def predict_educational_value(text_list):
  text_list = [replace_newlines(text) for text in text_list]
  pred = model.predict(text_list, k=-1)
  score_list = []
  for l, s in zip(*pred):
    score = 0
    for _l, _s in zip(l, s):
      score += score_dict[_l] * _s
    score_list.append(float(score))
  return score_list


predict_educational_value(["Hi"])
# Output: [3.0000010156072676e-05]

```
# 📊Benchmark
To make sure this classifier makes sense, it is applied to various datasets.   

Educational Value = 2 point * P(High) + 1 point * P(Mid) + 0 point * P(Low)

The score can be roughly interpreted as:
|Educational Value| Category |
|--------|----------|
|2 | High|
|1 | Mid|
|0 | Low|


|Dataset | Sampling | Average Educational Value | Type |
|--------------------------------------|---|-------------------|-------|
|[SciPhi/textbooks-are-all-you-need-lite](https://huggingface.co/datasets/SciPhi/textbooks-are-all-you-need-lite) |First 100,000 | 1.846 |Synthetic|
|[nampdn-ai/tiny-orca-textbooks](https://huggingface.co/datasets/nampdn-ai/tiny-orca-textbooks) |First 100,000 | 1.673 |Synthetic|
|[HuggingFaceTB/cosmopedia stanford](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) |First 100,000 | 1.673 |Synthetic|
|[vikp/textbook_quality_programming](https://huggingface.co/datasets/vikp/textbook_quality_programming) |First 100,000| 1.663|Synthetic|
|[HuggingFaceTB/cosmopedia web_samples_v1](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) |First 100,000 | 1.618 |Synthetic|
|[nampdn-ai/tiny-textbooks](https://huggingface.co/datasets/nampdn-ai/tiny-textbooks) |First 100,000 | 1.586 |Synthetic|Synthetic|
|[HuggingFaceTB/cosmopedia web_samples_v2](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) |First 100,000 | 1.562 |Synthetic|
|[HuggingFaceTB/cosmopedia openstax](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) |First 100,000 | 1.462 |Synthetic|
|[HuggingFaceTB/cosmopedia wikihow](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) |First 100,000 | 1.422 |Synthetic|
|[HuggingFaceTB/cosmopedia khanacademy](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) |First 100,000 | 1.419 |Synthetic|
|[HuggingFaceTB/cosmopedia auto_math_text](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) |First 100,000 | 1.347 |Synthetic|
|[armanc/scientific_papers pubmed](https://huggingface.co/datasets/armanc/scientific_papers) |First 100,000 | 1.260 |Real|
|[HuggingFaceTB/cosmopedia stories](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) |First 100,000 | 1.154 |Synthetic|
|[teknium/OpenHermes-2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5) |First 100,000 | 1.121 |Synthetic|
|[timdettmers/openassistant-guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco) |First 100,000 | 1.115 |Real|
|[open-web-math/open-web-math](https://huggingface.co/datasets/open-web-math/open-web-math) |First 100,000 | 1.089 |Real|
|[armanc/scientific_papers arxiv](https://huggingface.co/datasets/armanc/scientific_papers) |First 100,000 | 1.068 |Real|
|[HuggingFaceFW/fineweb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)| First 100,000 | 1.056 |Real|
|[NousResearch/dolma-v1_7-305B*](https://huggingface.co/datasets/NousResearch/dolma-v1_7-305B) |First 100,000 | 1.037 |Real|
|[tatsu-lab/alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca) |First 100,000 | 1.020 |Synthetic|
|[BEE-spoke-data/fineweb-100k_en-med](https://huggingface.co/datasets/BEE-spoke-data/fineweb-100k_en-med)| First 100,000 | 1.019 |Real|
|[JeanKaddour/minipile](https://huggingface.co/datasets/JeanKaddour/minipile)| First 100,000 | 0.998 |Real|
|[togethercomputer/RedPajama-Data-V2 en 2023-06](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-V2)| First 100,000 | 0.985|Real|
|[wikipedia en 20220301](https://huggingface.co/datasets/wikipedia) |First 100,000 | 0.975 |Real|
|[Replete-AI/code_bagel](https://huggingface.co/datasets/Replete-AI/code_bagel)| First 100,000 | 0.950 |Synthetic|
|[allenai/c4 en](https://huggingface.co/datasets/allenai/c4)| First 100,000| 0.934 |Real|
|[mattymchen/refinedweb-3m](https://huggingface.co/datasets/mattymchen/refinedweb-3m)| First 100,000 | 0.857 |Real|
|[iamtarun/python_code_instructions_18k_alpaca](https://huggingface.co/datasets/iamtarun/python_code_instructions_18k_alpaca)| First 100,000 | 0.849 |Synthetic|
|[tiiuae/falcon-refinedweb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)| First 100,000 | 0.835 |Real|
|[BEE-spoke-data/FineMeme-100k](https://huggingface.co/datasets/BEE-spoke-data/FineMeme-100k)| First 100,000 | 0.716 |Real|
|[neuralcatcher/hateful_memes](https://huggingface.co/datasets/neuralcatcher/hateful_memes)| First 100,000 | 0.070 |Real|
\* I encounted an [issue](https://huggingface.co/datasets/allenai/dolma/discussions/26) so that I cannot process the original [allenai/dolma](https://huggingface.co/datasets/allenai/dolma).

The classifier aligns with the expectation. 

- In general, the synthetic data has higher education value because they are created with a high educational value by design.
- For real data, [HuggingFaceFW/fineweb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) and [Dolma v1_7](https://huggingface.co/datasets/allenai/dolma), which applied quality filter described in [here](https://blog.allenai.org/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d), have the highest educational value across all real data.
- In general, the later a dataset is released, the higher the educational value it is because of increasing focus on data quality in the research community.
- Textbook category (mostly synethetic) scores the highest, becuase they are created for educational value, reflecting the effectiveness of this model.   
- Maths/ paper category scores the second highest, because of its density of knowledge.
- Wikipedia scores comparatively lower because it also contains information (e.g. result of a match, award of a movie star) that has smaller educational value.  
- Web scores low (if no filtering is applied) because it contains all domains.
- Meme scores the lowest as expected. Hateful memes almost got zero point.

Some instruction datasets are added for curiosity sake although model is not trained on instruction data. There are two possible interpretations:
- They score less than textbook because depth of knowledge in conversation is usually less dense in textbook, but they are in general more educative than unfiltered web.
- The model does not perform well enough to tell educational value in instruction datasets.

# 📈Analysis
## 🤖Model Training With And Without Classifier
The expectation is that the model trained with filter will outperform model trained without the filter.  
Fineweb is filtered on the fly with Educational Value >= 1.0.   

Test 1:  
Model params: 192M  
Training token: 3.1B training token, 6000 global steps  

|Task | Training on FineWeb With Filtering | Training on FineWeb Without Filtering | Training with [Cosmopedia](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia)|
|--------------------------------------|---|---|---|
|arc-easy | 37.37 | 34.97| 37.45 |
|arc-challenge | 23.55 |22.95| 23.21 | 
|Hellaswag | 28.02| 27.92 | 27.78|
|MMLU | 24.71 | 23.94 | 24.65 |
|TruthfulQA| 45.88 | 45.20| 45.97|
|Winogrande| 49.49 | 50.59 | 50.67 |

The reasoning and commensense reasoning seems to be better when filter is on, aligning with expectation. It is also close to Cosmopedia.  
MMLU is better also; however it is close to random due to limitation in compute (both training time and model size).  
Model of larger size will be trained to further validate this claim.  

(To be updated with a larger model soon)  

## 🌐Domain Name Analysis
The expectation is that most educational value comes from website of universities/ schools, research institutes and organisations.  
Since [HuggingFaceFW/fineweb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) contains the url of website crawled, the average educational value of each domain name is calculated.  
The first 10M records have been analysed.  Full file in [here](https://drive.google.com/file/d/1WnOEH7IwfLJba2CuY207JY6s5hcW1gZQ/view?usp=sharing).

Below is the top 100 domain names, with no of record >= 100.
![image/png](https://cdn-uploads.huggingface.co/production/uploads/60e50ce5350d181892d5a636/3QNYYVbFIqaAUh-574lED.png)

## 🧪Classifier Rank Ordering
Spearman rank-order correlation coefficient between Educational Value and that of test data is 0.7055, indicating a strong monotonic relationship. The Educational Value can be used for ranking.
![image/png](https://cdn-uploads.huggingface.co/production/uploads/60e50ce5350d181892d5a636/dKV2oXRv3WpEsfDXy0bl7.png)

# Citation
```
@misc{ktsui2024cpueduvalue,
      title={Low Latency CPU Based Educational Value Classifier With Generic Educational Value}, 
      author={Ken Tsui and Huu Nguyen},
      year={2024},
}
```