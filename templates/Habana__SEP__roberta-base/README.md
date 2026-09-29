---
license: apache-2.0
---

[Optimum Habana](https://github.com/huggingface/optimum-habana) is the interface between the Hugging Face Transformers and Diffusers libraries and Habana's Gaudi processor (HPU).
It provides a set of tools enabling easy and fast model loading, training and inference on single- and multi-HPU settings for different downstream tasks.
Learn more about how to take advantage of the power of Habana HPUs to train and deploy Transformers and Diffusers models at [hf.co/hardware/habana](https://huggingface.co/hardware/habana).

## RoBERTa Base model HPU configuration

This model only contains the `GaudiConfig` file for running the [roberta-base](https://huggingface.co/roberta-base) model on Habana's Gaudi processors (HPU).

**This model contains no model weights, only a GaudiConfig.**

This enables to specify:
- `use_torch_autocast`: whether to use PyTorch's autocast mixed precision
- `use_fused_adam`: whether to use Habana's custom AdamW implementation
- `use_fused_clip_norm`: whether to use Habana's fused gradient norm clipping operator

## Usage

The model is instantiated the same way as in the Transformers library.
The only difference is that there are a few new training arguments specific to HPUs.

[Here](https://github.com/huggingface/optimum-habana/blob/main/examples/question-answering/run_qa.py) is a question-answering example script to fine-tune a model on SQuAD. You can run it with RoBERTa with the following command:
```bash
python run_qa.py \
  --model_name_or_path roberta-base \
  --gaudi_config_name Habana/roberta-base \
  --dataset_name squad \
  --do_train \
  --do_eval \
  --per_device_train_batch_size 12 \
  --per_device_eval_batch_size 8 \
  --learning_rate 3e-5 \
  --num_train_epochs 2 \
  --max_seq_length 384 \
  --output_dir /tmp/squad/ \
  --use_habana \
  --use_lazy_mode \
  --throughput_warmup_steps 3 \
  --bf16
```

Check the [documentation](https://huggingface.co/docs/optimum/habana/index) out for more advanced usage and examples.