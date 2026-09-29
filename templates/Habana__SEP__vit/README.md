---
license: apache-2.0
---

[Optimum Habana](https://github.com/huggingface/optimum-habana) is the interface between the Hugging Face Transformers and Diffusers libraries and Habana's Gaudi processor (HPU).
It provides a set of tools enabling easy and fast model loading, training and inference on single- and multi-HPU settings for different downstream tasks.
Learn more about how to take advantage of the power of Habana HPUs to train and deploy Transformers and Diffusers models at [hf.co/hardware/habana](https://huggingface.co/hardware/habana).

## ViT model HPU configuration

This model only contains the `GaudiConfig` file for running the [ViT](https://huggingface.co/google/vit-base-patch16-224-in21k) model on Habana's Gaudi processors (HPU).

**This model contains no model weights, only a GaudiConfig.**

This enables to specify:
- `use_fused_adam`: whether to use Habana's custom AdamW implementation
- `use_fused_clip_norm`: whether to use Habana's fused gradient norm clipping operator
- `use_torch_autocast`: whether to use Torch Autocast for managing mixed precision

## Usage

The model is instantiated the same way as in the Transformers library.
The only difference is that there are a few new training arguments specific to HPUs.\
It is strongly recommended to train this model doing bf16 mixed-precision training for optimal performance and accuracy.

[Here](https://github.com/huggingface/optimum-habana/blob/main/examples/image-classification/run_image_classification.py) is an image classification example script to fine-tune a model. You can run it with ViT with the following command:
```bash
python run_image_classification.py \
    --model_name_or_path google/vit-base-patch16-224-in21k \
    --dataset_name cifar10 \
    --output_dir /tmp/outputs/ \
    --remove_unused_columns False \
    --do_train \
    --do_eval \
    --learning_rate 2e-5 \
    --num_train_epochs 5 \
    --per_device_train_batch_size 64 \
    --per_device_eval_batch_size 64 \
    --evaluation_strategy epoch \
    --save_strategy epoch \
    --load_best_model_at_end True \
    --save_total_limit 3 \
    --seed 1337 \
    --use_habana \
    --use_lazy_mode \
    --gaudi_config_name Habana/vit \
    --throughput_warmup_steps 3 \
    --bf16
```

Check the [documentation](https://huggingface.co/docs/optimum/habana/index) out for more advanced usage and examples.