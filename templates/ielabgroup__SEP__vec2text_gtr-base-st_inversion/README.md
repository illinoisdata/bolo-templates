---
license: apache-2.0
---

To use the model, check vec2text repo [https://github.com/jxmorris12/vec2text](https://github.com/jxmorris12/vec2text)

# Example:
```python
from sentence_transformers import SentenceTransformer
import vec2text
import transformers


inversion_model = vec2text.models.InversionModel.from_pretrained(
    "ielabgroup/vec2text_gtr-base-st_inversion"
)
model = vec2text.models.CorrectorEncoderModel.from_pretrained(
    "ielabgroup/vec2text_gtr-base-st_corrector"
)

inversion_trainer = vec2text.trainers.InversionTrainer(
    model=inversion_model,
    train_dataset=None,
    eval_dataset=None,
    data_collator=transformers.DataCollatorForSeq2Seq(
        inversion_model.tokenizer,
        label_pad_token_id=-100,
    ),
)

model.config.dispatch_batches = None
corrector = vec2text.trainers.Corrector(
    model=model,
    inversion_trainer=inversion_trainer,
    args=None,
    data_collator=vec2text.collator.DataCollatorForCorrection(
        tokenizer=inversion_trainer.model.tokenizer
    ),
)

model = SentenceTransformer('sentence-transformers/gtr-t5-base')
embeddings = model.encode([
       "Jack Morris is a PhD student at Cornell Tech in New York City",
       "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity"
], convert_to_tensor=True,).to('mps')

vec2text.invert_embeddings(
    embeddings=embeddings,
    corrector=corrector,
    num_steps=20,
)

['         Jack Morris is a PhD student at Cornell Tech in New York', 'It was the best of times, it was the worst of times, it was the epoch of incredulity, it was age of']
```