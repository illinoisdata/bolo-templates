---
license: apache-2.0
language:
- en
---

This classifier is trained on LLM responses designed to capture a model refuting a false claim. 

They're prompt results of OpenAI gpt-3.5-turbo run on June 1 2023. 
Prompts are constructed by prepending "Explain why" to claims made in the True-False dataset provided alongside [The Internal State of an LLM Knows When its Lying](https://arxiv.org/abs/2304.13734).
Only the first sentence of the response is included (from nltk.sent_tokenize).
The original labels are used, where 0 corresponds to a false claim.
That is, the 0 labels should be almost all refutations.
Spurious and missing refutations were removed by hand, corresponding to about 10% of the data.
This were caused by either an incorrect model assertion, or errors in the source data.