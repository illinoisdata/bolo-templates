---
language: zh-tw
datasets: DRCD
tasks: Question Answering
---


# BERT DRCD 384

This model is a fine-tune checkpoint of [bert-base-chinese](https://huggingface.co/bert-base-chinese), fine-tuned on DRCD dataset.
This model reaches a F1 score of 86.
This model reaches a EM score of 83.

Training Arguments:

- length: 384

- stride: 128

- learning_rate: 3e-5

- batch_size: 10

- epoch: 3

[Colab for detailed](https://colab.research.google.com/drive/1kZv7ZRmvUdCKEhQg8MBrKljGWvV2X3CP?usp=sharing)

## Deployment

Deploy [BERT-DRCD-QuestionAnswering](https://github.com/pleomax0730/BERT-DRCD-QuestionAnswering) model using `FastAPI` and containerized using `Docker`.

## Usage

### In Transformers

```python
text = "鴻海科技集團是由臺灣企業家郭台銘創辦的跨國企業，總部位於臺灣新北市土城區，主要生產地則在中國大陸，以富士康做為商標名稱。其專注於電子產品的代工服務，研發生產精密電氣元件、機殼、準系統、系統組裝、光通訊元件、液晶顯示件等3C產品上、下游產品及服務。"
query = "鴻海集團總部位於哪裡？"
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
tokenizer = BertTokenizerFast.from_pretrained("nyust-eb210/braslab-bert-drcd-384")
model = BertForQuestionAnswering.from_pretrained("nyust-eb210/braslab-bert-drcd-384").to(device)
encoded_input = tokenizer(text, query, return_tensors="pt").to(device)
qa_outputs = model(**encoded_input)

start = torch.argmax(qa_outputs.start_logits).item()
end = torch.argmax(qa_outputs.end_logits).item()
answer = encoded_input.input_ids.tolist()[0][start : end + 1]
answer = "".join(tokenizer.decode(answer).split())

start_prob = torch.max(torch.nn.Softmax(dim=-1)(qa_outputs.start_logits)).item()
end_prob = torch.max(torch.nn.Softmax(dim=-1)(qa_outputs.end_logits)).item()
confidence = (start_prob + end_prob) / 2
print(answer, confidence) # 臺灣新北市土城區, 0.92
```