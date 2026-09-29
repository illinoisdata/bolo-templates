---
license: unknown
tags:
- summarization
- Seq2Seq
- PyTorch
model-index:
- name: bart-base-finetuned-poems
  results:
  - task:
      type: summarization
      name: Summarization
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 0.32955500483066247
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 0.13833204028540397
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 0.27404767245323625
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 0.2747326116711135
      verified: true
base_model: facebook/bart-base
metrics:
- rouge
pipeline_tag: summarization
---

# bart-base-job-info-summarizer

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the private dataset of job offer information scraped from job offer websites and the summary result of the job info.
- Rouge1: 0.32955500483066247
- Rouge2: 0.13833204028540397
- Rougel: 0.27404767245323625
- Rougelsum: 0.2747326116711135

## Intended use and limitations:
This model can be used to summarize company and job offer information in such persuasive way

## How to use:
```python
!pip install transformers

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("avisena/bart-base-job-info-summarizer")
model = AutoModelForSeq2SeqLM.from_pretrained("avisena/bart-base-job-info-summarizer")

input_text = """About Four Seasons
Four Seasons is powered by our people. We are a collective of individuals who crave to become better, to push ourselves to new heights and to treat each other as we wish to be treated in return. Our team members around the world create amazing experiences for our guests, residents, and partners through a commitment to luxury with genuine heart. We know that the best way to enable our people to deliver these exceptional guest experiences is through a world-class employee experience and company culture.
At Four Seasons, we believe in recognizing a familiar face, welcoming a new one and treating everyone we meet the way we would want to be treated ourselves. Whether you work with us, stay with us, live with us or discover with us, we believe our purpose is to create impressions that will stay with you for a lifetime. It comes from our belief that life is richer when we truly connect to the people and the world around us.
About the location:
Four Seasons Hotels and Resorts is a global, luxury hotel management company. We manage over 120 hotels and resorts and 50 private residences in 47 countries around the world and growing. Central to Four Seasons employee experience and social impact programming is the company’s commitment to supporting cancer research, and the advancement of diversity, inclusion, equality and belonging at Four Seasons corporate offices and properties worldwide. At Four Seasons, we are powered by people and our culture enables everything we do.
Staff Accountant
The Staff Accountant is responsible for transaction processing, accounting analysis, reporting, balance sheet reconciliations and other administrative duties in the Corporate Finance Department. The Staff Accountant is also involved with continuous process improvements and department projects.
The Staff Accountant may be assigned to various functions, including Accounts Payable, Accounts Receivable, General Ledger/Reconciliation, Global Programs, Payroll or Global Entities. As development opportunities arise, the Staff Accountant may rotate through one or more Corporate Finance functions listed above.
"""

inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=1024, truncation='do_not_truncate')

summary_ids = model.generate(
    inputs, 
    max_length=200,  # Maximum length of the summary
    min_length=30,   # Minimum length of the summary
    length_penalty=0.98,  # Penalty for longer sequences
    num_beams=6,     # Number of beams for beam search
    top_p=3.7,
    early_stopping=True,
    temperature=1.4,
    do_sample=True
)

summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, max_length=512, truncation='do_not_truncate')

print(f"Generated Summary: {summary}")
```