This model is trained for conversational question rewriting.

Usage:

Source text format: ${HISTORY} ||| ${CURRENT_QUESTION}

example from [CANARD](https://sites.google.com/view/qanta/projects/canard):
Frank Zappa ||| Disbandment ||| What group disbanded ||| Zappa and the Mothers of Invention ||| When did they disband?

Target text:
When did Zappa and the Mothers of Invention disband?


You can find our guide to reproduce the training in this [repo](https://github.com/castorini/chatty-goose/blob/c7d0cd8c45354b09b5fb930ab0b5af8be2e5772b/docs/t5_finetuning.md).