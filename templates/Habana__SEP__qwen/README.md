---
license: apache-2.0
---

[Optimum Habana](https://github.com/huggingface/optimum-habana) is the interface between the Hugging Face Transformers and Diffusers libraries and Habana's Gaudi processor (HPU).
It provides a set of tools enabling easy and fast model loading, training and inference on single- and multi-HPU settings for different downstream tasks.
Learn more about how to take advantage of the power of Habana HPUs to train and deploy Transformers and Diffusers models at [hf.co/hardware/habana](https://huggingface.co/hardware/habana).

## Qwen model HPU configuration

This model only contains the `GaudiConfig` file for running [Qwen models](https://huggingface.co/Qwen) on Habana's Gaudi processors (HPU).

**This model contains no model weights, only a GaudiConfig.**

This enables to specify:
- `use_fused_adam`: whether to use Habana's custom AdamW implementation
- `use_fused_clip_norm`: whether to use Habana's fused gradient norm clipping operator
- `use_torch_autocast`: whether to use PyTorch's autocast mixed precision

## Usage

The model is instantiated the same way as in the Transformers library.
The only difference is that there are a few new training arguments specific to HPUs.

[Here](https://github.com/huggingface/optimum-habana/blob/main/examples/language-modeling/run_clm.py) is a causal language modeling example script to pre-train/fine-tune a model. You can run it with Qwen with the following command:
```bash
python3 run_lora_clm.py \
    --model_name_or_path Qwen/Qwen2-7B \
    --dataset_name tatsu-lab/alpaca \
    --bf16 True \
    --output_dir ./model_lora_qwen \
    --num_train_epochs 3 \
    --per_device_train_batch_size 16 \
    --evaluation_strategy "no" \
    --save_strategy "no" \
    --learning_rate 1e-4 \
    --warmup_ratio  0.03 \
    --lr_scheduler_type "constant" \
    --max_grad_norm  0.3 \
    --logging_steps 1 \
    --do_train \
    --do_eval \
    --use_habana \
    --use_lazy_mode \
    --throughput_warmup_steps 3 \
    --lora_rank=8 \
    --lora_alpha=16 \
    --lora_dropout=0.05 \
    --lora_target_modules "q_proj" "v_proj" \
    --dataset_concatenation \
    --max_seq_length 512 \
    --low_cpu_mem_usage True \
    --validation_split_percentage 4 \
    --adam_epsilon 1e-08
```

You will need to install the [PEFT](https://huggingface.co/docs/peft/index) library with `pip install peft` to run the command above.

Check the [documentation](https://huggingface.co/docs/optimum/habana/index) out for more advanced usage and examples.