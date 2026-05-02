---
language: en
tags:
- summarization
metrics:
- rouge
- precision
inference: false
license: mit
---

## PEGASUS for legal document summarization
**legal-pegasus** is a finetuned version of ([**google/pegasus-cnn_dailymail**](https://huggingface.co/google/pegasus-cnn_dailymail)) for the **legal domain**, trained to perform **abstractive summarization** task. The maximum length of input sequence is 1024 tokens.

## Training data

This model was trained on [**sec-litigation-releases**](https://www.sec.gov/litigation/litreleases.htm) dataset consisting more than 2700 litigation releases and complaints.

## How to use
```Python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("nsi319/legal-pegasus")  
model = AutoModelForSeq2SeqLM.from_pretrained("nsi319/legal-pegasus")


text = """On March 5, 2021, the Securities and Exchange Commission charged AT&T, Inc. with repeatedly violating Regulation FD, and three of its Investor Relations executives with aiding and abetting AT&T's violations, by selectively disclosing material nonpublic information to research analysts. According to the SEC's complaint, AT&T learned in March 2016 that a steeper-than-expected decline in its first quarter smartphone sales would cause AT&T's revenue to fall short of analysts' estimates for the quarter. The complaint alleges that to avoid falling short of the consensus revenue estimate for the third consecutive quarter, AT&T Investor Relations executives Christopher Womack, Michael Black, and Kent Evans made private, one-on-one phone calls to analysts at approximately 20 separate firms. On these calls, the AT&T executives allegedly disclosed AT&T's internal smartphone sales data and the impact of that data on internal revenue metrics, despite the fact that internal documents specifically informed Investor Relations personnel that AT&T's revenue and sales of smartphones were types of information generally considered "material" to AT&T investors, and therefore prohibited from selective disclosure under Regulation FD. The complaint further alleges that as a result of what they were told on these calls, the analysts substantially reduced their revenue forecasts, leading to the overall consensus revenue estimate falling to just below the level that AT&T ultimately reported to the public on April 26, 2016. The SEC's complaint, filed in federal district court in Manhattan, charges AT&T with violations of the disclosure provisions of Section 13(a) of the Securities Exchange Act of 1934 and Regulation FD thereunder, and charges Womack, Evans and Black with aiding and abetting these violations. The complaint seeks permanent injunctive relief and civil monetary penalties against each defendant. The SEC's investigation was conducted by George N. Stepaniuk, Thomas Peirce, and David Zetlin-Jones of the SEC's New York Regional Office. The SEC's litigation will be conducted by Alexander M. Vasilescu, Victor Suthammanont, and Mr. Zetlin-Jones. The case is being supervised by Sanjay Wadhwa."""

input_tokenized = tokenizer.encode(text, return_tensors='pt',max_length=1024,truncation=True)
summary_ids = model.generate(input_tokenized,
                                  num_beams=9,
                                  no_repeat_ngram_size=3,
                                  length_penalty=2.0,
                                  min_length=150,
                                  max_length=250,
                                  early_stopping=True)
summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids][0]
### Summary Output

# The Securities and Exchange Commission today charged AT&T, Inc. and three of its Investor Relations executives with aiding and abetting the company's violations of the antifraud provisions of Section 10(b) of the Securities Exchange Act of 1934 and Rule 10b-5 thereunder. According to the SEC's complaint, the company learned in March 2016 that a steeper-than-expected decline in its first quarter smartphone sales would cause its revenue to fall short of analysts' estimates for the quarter. The complaint alleges that to avoid falling short of the consensus revenue estimate for the third consecutive quarter, the executives made private, one-on-one phone calls to analysts at approximately 20 separate firms. On these calls, the SEC alleges that Christopher Womack, Michael Black, and Kent Evans allegedly disclosed internal smartphone sales data and the impact of that data on internal revenue metrics. The SEC further alleges that as a result of what they were told, the analysts substantially reduced their revenue forecasts, leading to the overall consensus Revenue Estimate falling to just below the level that AT&t ultimately reported to the public on April 26, 2016. The SEC is seeking permanent injunctive relief and civil monetary penalties against each defendant.
```
## Evaluation results

| Model |  rouge1  |  rouge1-precision  |  rouge2   |  rouge2-precision  | rougeL   |  rougeL-precision  |
|:-----------:|:-----:|:-----:|:------:|:-----:|:------:|:-----:|
| legal-pegasus        | **57.39** |  **62.97** | **26.85**  | **28.42** | **30.91**  | **33.22** | 
| pegasus-cnn_dailymail          | 43.16  |  45.68  | 13.75  | 14.56 | 18.82  | 20.07 |