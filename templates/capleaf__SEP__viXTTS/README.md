---
license: other
license_name: coqui-public-model-license
license_link: https://coqui.ai/cpml
pipeline_tag: text-to-speech
datasets:
- capleaf/viVoice
language:
- vi
---

# viⓍTTS

viⓍTTS là mô hình tạo sinh giọng nói cho phép bạn sao chép giọng nói sang các ngôn ngữ khác nhau chỉ bằng cách sử dụng một đoạn âm thanh nhanh dài 6 giây. Mô hình này được tiếp tục đào tạo từ mô hình [XTTS-v2.0.3](https://huggingface.co/coqui/XTTS-v2) bằng cách mở rộng tokenizer sang tiếng Việt và huấn luyện trên tập dữ liệu [viVoice](https://huggingface.co/datasets/thinhlpg/viVoice).

viⓍTTS is a voice generation model that lets you clone voices into different languages by using just a quick 6-second audio clip. This model is fine-tuned from the [XTTS-v2.0.3](https://huggingface.co/coqui/XTTS-v2) model by expanding the tokenizer to Vietnamese and fine-tuning on the [viVoice](https://huggingface.co/datasets/thinhlpg/viVoice) dataset.

### Languages

viXTTS supports 18 languages: English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt),
Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko)
Hindi (hi), **Vietnamese (vi)**.

### Known Limitations

- Incompatibility with the [original TTS library](https://github.com/coqui-ai/TTS) (a pull request will be made later).
- Subpar performance for input sentences under 10 words in Vietnamese language (yielding inconsistent output and odd trailing sounds).
- This model is only fine-tuned in Vietnamese. The model's effectiveness with languages other than Vietnamese hasn't been tested, potentially reducing quality.
  
### Demo

Please checkout [this repo](https://github.com/thinhlpg/vixtts-demo)

### Usage

For a quick usage, please checkout [this notebook](https://colab.research.google.com/drive/1q9vA7mDyvK_u0ijDDNuycDoUUbryM3p3?usp=sharing)

### License

This model is licensed under [Coqui Public Model License](https://coqui.ai/cpml).

### Contact

Fine-tuned by Thinh Le at FPT University HCMC, as a component of [Non La](https://huggingface.co/capleaf)'s graduation thesis.
Contact:

- You can message me directly on Facebook: <https://fb.com/thinhlpg/> (preferred 🤗)
- GitHub: <https://github.com/thinhlpg>
- Email: <thinhlpg@gmail.com> or <thinhlpgse161384@fpt.edu.vn>