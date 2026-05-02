---
language: en
datasets:
- tapaco
---
# T5-base for paraphrase generation

Google's T5-base fine-tuned on [TaPaCo](https://huggingface.co/datasets/tapaco) dataset for paraphrasing.

<!-- ## Model fine-tuning -->

<!-- The training script is a slightly modified version of [this Colab Notebook](https://github.com/patil-suraj/exploring-T5/blob/master/t5_fine_tuning.ipynb) created by [Suraj Patil](https://github.com/patil-suraj), so all credits to him! -->

## Model in Action 🚀

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained("hetpandya/t5-base-tapaco")
model = T5ForConditionalGeneration.from_pretrained("hetpandya/t5-base-tapaco")

def get_paraphrases(sentence, prefix="paraphrase: ", n_predictions=5, top_k=120, max_length=256,device="cpu"):
        text = prefix + sentence + " </s>"
        encoding = tokenizer.encode_plus(
            text, pad_to_max_length=True, return_tensors="pt"
        )
        input_ids, attention_masks = encoding["input_ids"].to(device), encoding[
            "attention_mask"
        ].to(device)

        model_output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_masks,
            do_sample=True,
            max_length=max_length,
            top_k=top_k,
            top_p=0.98,
            early_stopping=True,
            num_return_sequences=n_predictions,
        )

        outputs = []
        for output in model_output:
            generated_sent = tokenizer.decode(
                output, skip_special_tokens=True, clean_up_tokenization_spaces=True
            )
            if (
                generated_sent.lower() != sentence.lower()
                and generated_sent not in outputs
            ):
                outputs.append(generated_sent)
        return outputs

paraphrases = get_paraphrases("The house will be cleaned by me every Saturday.")

for sent in paraphrases:
  print(sent)
```

## Output
```
The house will get cleaned for a whole week.
The house is cleaning by me every weekend.
What was going to do not get do with the house from me every Thursday.
The house should be cleaned on Sunday--durse.
It's time that I would be cleaning her house in tomorrow.
```

Created by [Het Pandya/@hetpandya](https://github.com/hetpandya) | [LinkedIn](https://www.linkedin.com/in/het-pandya)

Made with <span style="color: red;">&hearts;</span> in India