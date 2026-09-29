---
license: apache-2.0
language:
- it
- en
pipeline_tag: text-generation
datasets:
- DeepMount00/o1-ITA-REASONING
- DeepMount00/GPT-4o-ITA-INSTRUCT
- DeepMount00/Sonnet-3.5-ITA-INSTRUCT
- DeepMount00/open-perfectblend-ita
- HuggingFaceTB/cosmopedia
- DeepMount00/pretraining_multi
---

---

**💡 Found this resource helpful?** Creating and maintaining open source AI models and datasets requires significant computational resources. If this work has been valuable to you, consider [supporting my research](https://buymeacoffee.com/michele.montebovi) to help me continue building tools that benefit the entire AI community. Every contribution directly funds more open source innovation! ☕

---

<p align="center">
  <img src="alireo.webp" style="width: 500px; height:500px;"/>
</p>

<h2 style="font-size: 32px; text-align: center;">Alireo-400M 🤖 🇮🇹</h2>
<p style="font-size: 21px; text-align: center;">A Lightweight Italian Language Model</p>

<h3 style="font-size: 21px; color: #2980b9;">Model Description 📝</h3>

Alireo-400M is a lightweight yet powerful Italian language model with 400M parameters, designed to provide efficient natural language processing capabilities while maintaining a smaller footprint compared to larger models.

<h3 style="font-size: 21px; color: #2980b9;">Key Features ✨</h3>

* **Architecture**: Transformer-based language model 🏗️
* **Parameters**: 400M 📊
* **Context Window**: 8K tokens 🪟
* **Training Data**: Curated Italian text corpus (books, articles, web content) 📚
* **Model Size**: ~800MB 💾

<h3 style="font-size: 21px; color: #2980b9;">Performance 📈</h3>

Despite its compact size, Alireo-400M demonstrates impressive performance:

* **Benchmark Results**: Outperforms Qwen 0.5B across multiple benchmarks 🏆
* **Language Understanding**: Maintains high accuracy in Italian language understanding tasks 🎯
* **Speed**: Efficient inference speed due to optimized architecture ⚡

<h3 style="font-size: 21px; color: #2980b9;">Limitations ⚠️</h3>

* Limited context window compared to larger models
* May struggle with highly specialized technical content
* Performance may vary on dialectal variations
* Not suitable for multilingual tasks

<h3 style="font-size: 21px; color: #2980b9;">Hardware Requirements 💻</h3>

* **Minimum RAM**: 2GB
* **Recommended RAM**: 4GB
* **GPU**: Optional, but recommended for faster inference
* **Disk Space**: ~1GB (including model and dependencies)

<h3 style="font-size: 21px; color: #2980b9;">Citation 📄</h3>

```bibtex
@software{alireo2024,
  author = {[Michele Montebovi]},
  title = {Alireo-400M: A Lightweight Italian Language Model},
  year = {2024},
}
```