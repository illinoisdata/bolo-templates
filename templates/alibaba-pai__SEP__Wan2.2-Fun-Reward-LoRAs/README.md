---
license: apache-2.0
base_model:
- alibaba-pai/Wan2.2-Fun-A14B-InP
- Wan-AI/Wan2.2-T2V-A14B
library_name: videox_fun
pipeline_tag: text-to-video
---
# Wan2.2-Fun-Reward-LoRAs
## Introduction
We explore the Reward Backpropagation technique <sup>[1](#ref1) [2](#ref2)</sup> to optimized the generated videos by [Wan2.2-Fun](https://github.com/aigc-apps/VideoX-Fun) for better alignment with human preferences.
We provide the following pre-trained models (i.e. LoRAs) along with [the training script](https://github.com/aigc-apps/VideoX-Fun/blob/main/scripts/wan2.2_fun/train_reward_lora.py). You can use these LoRAs to enhance the corresponding base model as a plug-in or train your own reward LoRA.

For more details, please refer to our [GitHub repo](https://github.com/aigc-apps/VideoX-Fun).

| Name | Base Model | Reward Model | Hugging Face | Description |
|--|--|--|--|--|
| Wan2.2-Fun-A14B-InP-high-noise-HPS2.1.safetensors | [Wan2.2-Fun-A14B-InP (high noise)](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP/tree/main/high_noise_model) | [HPS v2.1](https://github.com/tgxs002/HPSv2) | [🤗Link](https://huggingface.co/alibaba-pai/Wan2.2-Fun-Reward-LoRAs/resolve/main/Wan2.2-Fun-A14B-InP-high-noise-HPS2.1.safetensors) | Official HPS v2.1 reward LoRA (`rank=128` and `network_alpha=64`) for Wan2.2-Fun-A14B-InP (high noise). It is trained with a batch size of 8 for 5,000 steps.|
| Wan2.2-Fun-A14B-InP-low-noise-HPS2.1.safetensors | [Wan2.2-Fun-A14B-InP (low noise)](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP/tree/main/low_noise_model) | [MPS](https://github.com/Kwai-Kolors/MPS) | [🤗Link](https://huggingface.co/alibaba-pai/Wan2.2-Fun-Reward-LoRAs/resolve/main/Wan2.2-Fun-A14B-InP-low-noise-HPS2.1.safetensors) | Official HPS v2.1 reward LoRA (`rank=128` and `network_alpha=64`) for Wan2.2-Fun-A14B-InP (low noise). It is trained with a batch size of 8 for 2,700 steps.|
| Wan2.2-Fun-A14B-InP-high-noise-MPS.safetensors | [Wan2.2-Fun-A14B-InP (high noise)](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP/tree/main/high_noise_model) | [HPS v2.1](https://github.com/tgxs002/HPSv2) | [🤗Link](https://huggingface.co/alibaba-pai/Wan2.2-Fun-Reward-LoRAs/resolve/main/Wan2.2-Fun-A14B-InP-high-noise-MPS.safetensors) | Official MPS reward LoRA (`rank=128` and `network_alpha=64`) for Wan2.2-Fun-A14B-InP (high noise). It is trained with a batch size of 8 for 5,000 steps.|
| Wan2.2-Fun-A14B-InP-low-noise-MPS.safetensors | [Wan2.2-Fun-A14B-InP (low noise)](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP/tree/main/low_noise_model) | [MPS](https://github.com/Kwai-Kolors/MPS) | [🤗Link](https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs/resolve/main/Wan2.2-Fun-A14B-InP-low-noise-MPS.safetensors) | Official MPS reward LoRA (`rank=128` and `network_alpha=64`) for Wan2.2-Fun-A14B-InP (low noise). It is trained with a batch size of 8 for 4,500 steps.|

> [!NOTE]
> We found that, MPS reward LoRA for the low-noise model converges significantly more slowly than on the other models, and may not deliver satisfactory results. Therefore, for the low-noise model, we recommend using HPSv2.1 reward LoRA.

## Demo

### Wan2.2-Fun-A14B-InP

<table border="0" style="width: 100%; text-align: center; margin-top: 20px;">
    <thead>
        <tr>
            <th style="text-align: center;" width="10%">Prompt</sup></th>
            <th style="text-align: center;" width="30%">Wan2.2-Fun-A14B-InP</th>
            <th style="text-align: center;" width="30%">Wan2.2-Fun-A14B-InP <br> high + low HPSv2.1 Reward LoRA</th>
            <th style="text-align: center;" width="30%">Wan2.2-Fun-A14B-InP <br> high MPS + low HPSv2.1 Reward LoRA</th>
        </tr>
    </thead>
    <tr>
        <td>
            A panda eats bamboo while a monkey swings from branch to branch
            <details>
                <summary>Expanded</summary>
                <p>In a lush green forest, a panda sits comfortably against a tree, leisurely munching on bamboo stalks. Nearby, a lively monkey swings energetically from branch to branch, its tail curling around the limbs. Sunlight filters through the canopy, casting dappled shadows on the forest floor.</p>
            </details>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_baseline_00000001.mp4" width="100%" controls autoplay loop></video>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_high_hpsv2.1%2Blow_hps2.1_00000001.mp4" width="100%" controls autoplay loop></video>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_high_mps%2Blow_hpsv2.1_00000001.mp4" width="100%" controls autoplay loop></video>
        </td>
    </tr>
    <tr>
        <td>
            A dog runs through a field while a cat climbs a tree
            <details>
                <summary>Expanded</summary>
                <p>In a sunlit, expansive green field surrounded by tall trees, a playful golden retriever sprints energetically across the grass, its fur gleaming in the afternoon sun. Nearby, a nimble tabby cat gracefully climbs a sturdy tree, its claws gripping the bark effortlessly. The sky is clear blue with occasional birds flying.</p>
            </details>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_baseline_00000002.mp4" width="100%" controls autoplay loop></video>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_high_hpsv2.1%2Blow_hps2.1_00000002.mp4" width="100%" controls autoplay loop></video>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_high_mps%2Blow_hpsv2.1_00000002.mp4" width="100%" controls autoplay loop></video>
        </td>
    </tr>
    <tr>
        <td>
            A penguin waddles on the ice, a camel treks by
            <details>
                <summary>Expanded</summary>
                <p>A small penguin waddles slowly across a vast, icy surface under a clear blue sky. The penguin's short, flipper-like wings sway at its sides as it moves. Nearby, a camel treks steadily, its long legs navigating the snowy terrain with ease. The camel's fur is thick, providing warmth in the cold environment.</p>
            </details>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_baseline_00000004.mp4" width="100%" controls autoplay loop></video>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_high_hpsv2.1%2Blow_hps2.1_00000004.mp4" width="100%" controls autoplay loop></video>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_high_mps%2Blow_hpsv2.1_00000004.mp4" width="100%" controls autoplay loop></video>
        </td>
    </tr>
    <tr>
        <td>
            Pig with wings flying above a diamond mountain
            <details>
                <summary>Expanded</summary>
                <p>A whimsical pig, complete with delicate feathered wings, soars gracefully above a shimmering diamond mountain. The pig's pink skin glistens in the sunlight as it flaps its wings. The mountain below sparkles with countless facets, reflecting brilliant rays of light into the clear blue sky.</p>
            </details>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_baseline_00000008.mp4" width="100%" controls autoplay loop></video>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_high_hpsv2.1%2Blow_hps2.1_00000008.mp4" width="100%" controls autoplay loop></video>
        </td>
        <td>
            <video src="https://pai-aigc-photog.oss-cn-hangzhou.aliyuncs.com/wan_fun/asset_Wan2_2/reward_lora/14B_high_mps%2Blow_hpsv2.1_00000008.mp4" width="100%" controls autoplay loop></video>
        </td>
    </tr>
</table>


> [!NOTE]
> The above test prompts are from <a href="https://github.com/KaiyueSun98/T2V-CompBench">T2V-CompBench</a> and expanded into detailed prompts by Llama-3.3.
> Videos are generated with HPSv2.1 Reward LoRA weight 0.5 and MPS Reward LoRA weight 0.5.

## Quick Start
Set `lora_path` along with `lora_weight` for the low noise reward LoRA, while specifying `lora_high_path` and `lora_high_weight` for high noise reward LoRA in [examples/wan2.2_fun/predict_t2v.py](https://github.com/aigc-apps/VideoX-Fun/blob/main/examples/wan2.2_fun/predict_t2v.py).

## Training
Please refer to [README_TRAIN_REWARD.md](https://github.com/aigc-apps/VideoX-Fun/blob/main/scripts/wan2.2_fun/README_TRAIN_REWARD.md)

## Limitations
1. We observe after training to a certain extent, the reward continues to increase, but the quality of the generated videos does not further improve. 
   The model trickly learns some shortcuts (by adding artifacts in the background, i.e., adversarial patches) to increase the reward.
2. Currently, there is still a lack of suitable preference models for video generation. Directly using image preference models cannot 
   evaluate preferences along the temporal dimension (such as dynamism and consistency). Further more, We find using image preference models leads to a decrease 
   in the dynamism of generated videos. Although this can be mitigated by computing the reward using only the first frame of the decoded video, the impact still persists.

## Reference
<ol>
  <li id="ref1">Clark, Kevin, et al. "Directly fine-tuning diffusion models on differentiable rewards.". In ICLR 2024.</li>
  <li id="ref2">Prabhudesai, Mihir, et al. "Aligning text-to-image diffusion models with reward backpropagation." arXiv preprint arXiv:2310.03739 (2023).</li>
</ol>