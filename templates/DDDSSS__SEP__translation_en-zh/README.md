---
language:
- en
- zh
tags:
- translation
license: apache-2.0
datasets:
- DDDSSS/en-zh-dataset
metrics:
- bleu
- sacrebleu
---
该模型主要的训练数据是opus100和CodeAlpaca_20K中的英文作为翻译内容，采用chatglm作为翻译器翻译成中文，并将脏数据筛选后得到DDDSSS/en-zh-dataset数据集，
缺点是这个模型的sentence len 较短，需要自己进行分句，要不然可能会出现，少翻或者不翻译的情况出现
!注意，如果是pretrain方法下载模型的话，可能部分参数会随机初始化，建议直接下载模型，并从本地读取。


    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
    parser.add_argument('--device', default="cpu", type=str, help='"cuda:1"、"cuda:2"……')
    mode_name = opt.model
    device = opt.device
    model = AutoModelForSeq2SeqLM.from_pretrained(mode_name)
    tokenizer = AutoTokenizer.from_pretrained(mode_name)
    translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer,
                           torch_dtype="float", device_map=True,device=device)
    x=["If nothing is detected and there is a config.json file, it’s assumed the library is transformers.","By looking into the presence of files such as *.nemo or *saved_model.pb*, the Hub can determine if a model is from NeMo or Keras."]
    re = translation(x, max_length=450)
    print('翻译为：' ,re)


微调：

    import numpy as np
    from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer
    import torch
    # books =  load_from_disk("")
    books = load_dataset("json", data_files=".json")
    books = books["train"].train_test_split(test_size=0.2)
    checkpoint = "./opus-mt-en-zh"
    # checkpoint = "./model/checkpoint-19304"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    source_lang = "en"
    target_lang = "zh"
    def preprocess_function(examples):
        inputs = [example[source_lang] for example in examples["translation"]]
        targets = [example[target_lang] for example in examples["translation"]]
        model_inputs = tokenizer(inputs, text_target=targets, max_length=512, truncation=True)
        return model_inputs
    tokenized_books = books.map(preprocess_function, batched=True)
    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=checkpoint)
    metric = evaluate.load("sacrebleu")
    
    def postprocess_text(preds, labels):
        preds = [pred.strip() for pred in preds]
        labels = [[label.strip()] for label in labels]
        return preds, labels
    
    def compute_metrics(eval_preds):
        preds, labels = eval_preds
        if isinstance(preds, tuple):
            preds = preds[0]
        decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    
        labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
        decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    
        decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)
    
        result = metric.compute(predictions=decoded_preds, references=decoded_labels)
        result = {"bleu": result["score"]}
    
        prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
        result["gen_len"] = np.mean(prediction_lens)
        result = {k: round(v, 4) for k, v in result.items()}
        return result
        model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
        batchsize=4
        training_args = Seq2SeqTrainingArguments(
    
        output_dir="./my_awesome_opus_books_model",
        evaluation_strategy="epoch",
        learning_rate=2e-4,
        per_device_train_batch_size=batchsize,
        per_device_eval_batch_size=batchsize,
        weight_decay=0.01,
        # save_total_limit=3,
        num_train_epochs=4,
        predict_with_generate=True,
        fp16=True,
        push_to_hub=False,
        save_strategy="epoch",
        jit_mode_eval=True
    )
    
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_books["train"],
        eval_dataset=tokenized_books["test"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )
    trainer.train()