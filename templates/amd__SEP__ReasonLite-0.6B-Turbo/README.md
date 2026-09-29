---
license: openrail
datasets:
- amd/ReasonLite-Dataset
---



<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/66a056d0229269a861ac1245/9xXXms4ub9dzbcsN1IGqq.png" alt="ReasonLite" width="200">
</p>

<p align="center">
<a href="https://github.com/AMD-AGI/ReasonLite"><b>GitHub</b></a> |
<a href="https://huggingface.co/datasets/amd/ReasonLite-Dataset"><b>Dataset</b></a> |
<a href="https://www.amd.com/en/developer/resources/technical-articles/2026/introducing-reasonlite-0-6b.html"><b>Blog</b></a> 

</p>


**ReasonLite is an ultra-lightweight math reasoning model.** With only 0.6B parameters, it leverages **high-quality data distillation** to achieve performance comparable to models over 10× its size, such as Qwen3-8B, **reaching 75.2 on AIME24 and extending the scaling law of small models.**

* 🔥 **Best-performing 0.6B math reasoning model**
* 🔓 Fully open-source — weights, scripts, datasets, synthesis pipeline
* ⚙️ Distilled in two stages to balance **efficiency** and **high performance**, using **6.1M** high-quality samples.


<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/66a056d0229269a861ac1245/MCLe1ttoeHc_8181gKRPy.png"" alt="ReasonLite" height="500">
</p>

---

# 🚀 Model

The model is trained in **two progressive distillation stages**.
First, short-CoT data is used to distill **Qwen3-0.6B** into **ReasonLite-0.6B-Turbo**, improving **AIME24 accuracy from 11.0 → 57.1**.
Then, long-CoT data is used to obtain **ReasonLite-0.6B**, further boosting accuracy to **75.2**.

| Model                     | Description                                   | AIME24 | Link |
| ------------------------- | ----------------------------------------------| ------ | ---- |
| **amd/ReasonLite-0.6B-Turbo** | Short CoT balancing performance and efficiency | 57.1  | [🤗 HuggingFace](https://huggingface.co/amd/ReasonLite-0.6B-Turbo) |
| **amd/ReasonLite-0.6B**       | Long CoT for high performance                  | 75.2  | [🤗 HuggingFace](https://huggingface.co/amd/ReasonLite-0.6B) |

---

# 📊 Evaluation Results

**Metrics**

* **avg@16** — average accuracy from 16 sampled answers
* **pass@8** — probability at least one correct answer appears among 8 samples

| Model                     | Parameters | AMC23 avg@16 | AMC23 pass@8 | AIME25 avg@16 | AIME25 pass@8 | AIME24 avg@16 | AIME24 pass@8 |
|---------------------------|------------|-------------|-------------|---------------|---------------|---------------|---------------|
| Qwen2.5-14B               | 14B        | 58.3        | 82.3        | 12.3          | 32.3          | 12.7          | 32.4          |
| Deepseek-qwen-14B         | 14B        | 93.9        | 98.7        | 50.2          | 71.0          | 65.0          | 83.0          |
| Qwen3-0.6B                | 0.6B       | 52.7        | 85.0        | 16.0          | 33.0          | 11.0          | 31.5          |
| Qwen3-1.7B                | 1.7B       | 83.4        | 96.3        | 36.0          | 55.1          | 47.3          | 73.9          |
| Qwen3-4B                  | 4B         | 96.1        | 100         | 63.5          | 85.4          | 72.7          | 85.1          |
| Qwen3-8B                  | 8B         | 94.8        | 100         | 68.3          | 84.2          | 74.6          | 85.0          |
| Qwen3-14B                 | 14B        | 98.6        | 98.7        | 71.5          | 84.1          | 78.3          | 88.4          |
| DeepscaleR-1.5B           | 1.5B       | 83.8        | 95.0        | 29.0          | 48.9          | 40.4          | 69.0          |
| POLARIS-1.7B-Preview      | 1.7B       | 92.2        | 97.4        | 52.3          | 80.2          | 65.0          | 76.7          |
| OpenMath-Nemotron-1.5B    | 1.5B       | 88.8        | 96.7        | 39.8          | 65.8          | 61.5          | 81.3          |
| ReasonLite-0.6B-Turbo     | 0.6B       | 81.6        | 99.3        | 42.7          | 69.2          | 57.1          | 79.6          |
| **ReasonLite-0.6B**       | **0.6B**   | **95.2**    | **100**     | **62.9**      | **84.1**      | **75.2**      | **90.2**      |


---

# 📚 Dataset

We collected 343K math problems from Polaris and OpenMathReasoning. Using GPT-OSS as the teacher, we generated 9.1M raw answers under medium and high reasoning modes. We then produced pseudo-labels via majority voting, and finally retained 6.1M samples.

| Dataset                | Description | Size | Link |
| ---------------------- | ------      |---- | ---- |
| **amd/ReasonLite-Dataset** | Short CoT | 4.3M  | [🤗 HuggingFace](https://huggingface.co/datasets/amd/ReasonLite-Dataset/viewer/default/medium) |
| **amd/ReasonLite-Dataset**  | Long Cot | 1.8M  | [🤗 HuggingFace](https://huggingface.co/datasets/amd/ReasonLite-Dataset/viewer/default/high) |

---

# 📌 Citation

```bibtex
@misc{reasonlite2025,
  title    = {ReasonLite: An Ultra-Lightweight 0.6B Reasoning Model},
  author   = {An, Zihao and Chen, Chushi and Liu, Ziqiong and Li, Dong and Barsoum, Emad},
  year     = {2025},
  url      = {https://github.com/AMD-AGI/ReasonLite},
  note     = {Open-source project}
}
```