---
license: apache-2.0
---

[Optimum Habana](https://github.com/huggingface/optimum-habana) is the interface between the Hugging Face Transformers and Diffusers libraries and Habana's Gaudi processor (HPU).
It provides a set of tools enabling easy and fast model loading, training and inference on single- and multi-HPU settings for different downstream tasks.
Learn more about how to take advantage of the power of Habana HPUs to train and deploy Transformers and Diffusers models at [hf.co/hardware/habana](https://huggingface.co/hardware/habana).

## Whisper model HPU configuration

This model only contains the `GaudiConfig` file for running the [Whisper](https://huggingface.co/openai/whisper-small) model on Habana's Gaudi processors (HPU).

**This model contains no model weights, only a GaudiConfig.**

This enables to specify:
- `use_fused_adam`: whether to use Habana's custom AdamW implementation
- `use_fused_clip_norm`: whether to use Habana's fused gradient norm clipping operator
- `use_torch_autocast`: whether to use Torch Autocast for managing mixed precision

## Usage

The model is instantiated the same way as in the Transformers library.
The only difference is that there are a few new training arguments specific to HPUs.\
It is strongly recommended to train this model doing bf16 mixed-precision training for optimal performance and accuracy.

[Here](https://github.com/huggingface/optimum-habana/blob/main/examples/speech-recognition/run_speech_recognition_seq2seq.py) is a sequence-to-sequence speech recognition example script to fine-tune a model. You can run it with Whisper with the following command:
```bash
python run_speech_recognition_seq2seq.py \
	--model_name_or_path="openai/whisper-small" \
	--dataset_name="mozilla-foundation/common_voice_11_0" \
	--dataset_config_name="hi" \
	--language="hindi" \
	--train_split_name="train+validation" \
	--eval_split_name="test" \
	--gaudi_config_name="Habana/whisper" \
	--max_steps="5000" \
	--output_dir="/tmp/whisper-small-hi" \
	--per_device_train_batch_size="48" \
	--per_device_eval_batch_size="2" \
	--logging_steps="25" \
	--learning_rate="1e-5" \
	--warmup_steps="500" \
	--evaluation_strategy="steps" \
	--eval_steps="1000" \
	--save_strategy="steps" \
	--save_steps="1000" \
	--generation_max_length="225" \
	--preprocessing_num_workers="1" \
	--length_column_name="input_length" \
	--max_duration_in_seconds="30" \
	--text_column_name="sentence" \
	--freeze_feature_encoder="False" \
	--group_by_length \
	--bf16 \
	--overwrite_output_dir \
	--do_train \
	--do_eval \
	--predict_with_generate \
	--use_habana \
	--use_hpu_graphs_for_inference \
	--label_features_max_length 128 \
	--dataloader_num_workers 8 \
    --throughput_warmup_steps 3
```

Check the [documentation](https://huggingface.co/docs/optimum/habana/index) out for more advanced usage and examples.