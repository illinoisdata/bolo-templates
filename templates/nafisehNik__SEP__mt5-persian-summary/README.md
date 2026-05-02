---
license: mit
language: fa
tags:
- summarization
widget:
- text: "به گزارش شانا به نقل از شرکت پالایش گاز شهید هاشمی نژاد، جمعی از کارشناسان\nاین پالایشگاه با هدف معرفی محصول کود گوگرد بنتونیتی به کشاورزان در\nشانزدهمین نمایشگاه تخصصی کشاورزی، دام، طیور، ماشین آلات و صنایع وابسته در\nاردبیل حضور پیدا کردند و به معرفی دستاوردهای این شرکت پرداختند. بر اساس\nاین گزارش، دشت مغان قطب کشاورزی در منطقه اردبیل است و بیش از ۸۵ هزار هکتار\nزمین کشاورزی دارد که همه آنها نیاز به استفاده از کود گوگرد بنتونیتی دارند،\nبه همین دلیل، کارشناسان پالایشگاه گاز هاشمی نژاد در راستای توسعه بازار و\nمعرفی محصولات جانبی پالایشگاه (کود گوگرد بنتونیتی) به بازار داخلی در این\nنمایشگاه حضور یافتند. شرکت در این نمایشگاه سبب شد تعداد زیادی از بازرگانان\nایرانی فعال در حوزه گوگرد ضمن دیدار از غرفه شرکت پالایش گاز شهید هاشمی\nنژاد خواستار خرید محصول کود گوگرد بنتونیتی این مجتمع گازی شوند. شرکت\nپالایش گاز شهید هاشمی نژاد در کنار رسالت اصلی خود مبنی بر تامین گاز\nمشترکان شمال و شمال شرق کشور، محصولات جانبی ارزشمند مانند گوگرد را تولید\nمی کند، به گونه ای که اکنون با تولید روزانه بیش از ۲ هزار تن گوگرد مذاب،\nتولید روزانه ۶۰۰ تن گوگرد بنتونیتی (مطابق نیاز بازار) و تولید سالانه بیش\nاز ۲۰ هزار تن گوگرد بنتونیتی، بزرگ ترین تولیدکننده گوگرد در کشور است. کود\nگوگرد بنتونیتی نیز در راستای ارتقای کیفی خاک و تامین عناصر مورد نیاز رشد\nگیاهان تاثیری بسزا در بازده تولید محصولات کشاورزی دارد. کود گوگرد بنتونیتی\nتولیدی پالایشگاه هاشمی نژاد، با استانداردهای جهانی تولید شده و جایگاه خود\nرا در بازارهای داخلی و خارجی کسب کرده است. مطابق برنامه ریزی های انجام شده\nو بررسی روند رو به رشد مصرف این کود در بازار، پیش بینی می شود میزان مصرف\nکود گوگرد بنتونیتی تا پنج سال آینده به ۱۰۰ هزار تن در سال برسد.\t\n"
  example_title: Example 1
datasets:
- pn_summary
- csebuetnlp/xlsum
metrics:
- bleu
- rouge
- bertscore
---


# mT5 Persian Summary

This model is fine-tuned to generate summaries based on the input provided. It has been fine-tuned on a wide range of Persian news data, including [BBC news](https://huggingface.co/datasets/csebuetnlp/xlsum) and [pn_summary](https://huggingface.co/datasets/pn_summary).

## Usage

```python
from transformers import  AutoModelForSeq2SeqLM, MT5Tokenizer

model = AutoModelForSeq2SeqLM.from_pretrained('nafisehNik/mt5-persian-summary')

tokenizer = MT5Tokenizer.from_pretrained("nafisehNik/mt5-persian-summary")


# method for summary generation, using the global model and tokenizer
def generate_summary(model, abstract, num_beams = 2, repetition_penalty = 1.0,
                    length_penalty = 2.0, early_stopping = True, max_output_length = 120):
    source_encoding=tokenizer(abstract, max_length=1000, padding="max_length", truncation=True, return_attention_mask=True, add_special_tokens=True, return_tensors="pt")

    generated_ids=model.generate(
        input_ids=source_encoding["input_ids"],
        attention_mask=source_encoding["attention_mask"],
        num_beams=num_beams,
        max_length=max_output_length,
        repetition_penalty=repetition_penalty,
        length_penalty=length_penalty,
        early_stopping=early_stopping,
        use_cache=True
        )

    preds=[tokenizer.decode(gen_id, skip_special_tokens=True, clean_up_tokenization_spaces=True) 
         for gen_id in generated_ids]

    return "".join(preds)

text = "YOUR INPUT TEXT"
result = generate_summary(model=model, abstract=text, num_beams=2, max_output_length=120)
```


## Citation

If you find this model useful, make a link to the huggingface model.