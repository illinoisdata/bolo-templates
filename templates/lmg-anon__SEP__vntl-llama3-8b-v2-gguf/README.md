---
license: llama3
datasets:
- lmg-anon/VNTL-v5-1k
language:
- ja
- en
base_model: rinna/llama-3-youko-8b
pipeline_tag: translation
---

# Summary

This is a [LLaMA 3 Youko](https://huggingface.co/rinna/llama-3-youko-8b) qlora fine-tune, created using a new version of the VNTL dataset. The purpose of this fine-tune is to improve performance of LLMs at translating Japanese visual novels to English.

Unlike the previous version, this one doesn't includes the "chat mode".

## Notes

For this new version of VNTL 8B, I've rebuilt and expanded VNTL's dataset from the groud up, and I'm happy to say it performs really well, outperforming the previous version when it comes to accuracy and stability, it makes far fewer mistakes than it even when running at high temperatures (though I still recommend temperature 0 for the best accuracy).

Some major changes in this version:
- **Switched to the default LLaMA3 prompt format since people had trouble with the custom one**
- **Added proper support for multi-line translations** (the old version only handled single lines)
- Overall better translation accuracy

One thing to note: while the translations are more accurate, they tend to be more literal compared to the previous version.


## Sampling Recommendations

For optimal results, it's highly recommended to use neutral sampling parameters (temperature 0 with no repetition penalty) when using this model.

## Training Details

This fine-tune was done using similar hyperparameters as the [previous version](https://huggingface.co/lmg-anon/vntl-llama3-8b-qlora). The only difference is the dataset, which is a brand-new one.

- Rank: 128
- Alpha: 32
- Effective Batch Size: **45**
- Warmup Ratio: 0.02
- Learning Rate: **6e-5**
- Embedding Learning Rate: **1e-5**
- Optimizer: **grokadamw**
- LR Schedule: cosine
- Weight Decay: 0.01

**Train Loss**: 0.42

## Translation Prompt

This fine-tune uses the LLaMA 3 prompt format, this is an prompt example for translation:
```
<|begin_of_text|><|start_header_id|>Metadata<|end_header_id|>

[character] Name: Uryuu Shingo (瓜生 新吾) | Gender: Male | Aliases: Onii-chan (お兄ちゃん)
[character] Name: Uryuu Sakuno (瓜生 桜乃) | Gender: Female<|eot_id|><|start_header_id|>Japanese<|end_header_id|>

[桜乃]: 『……ごめん』<|eot_id|><|start_header_id|>English<|end_header_id|>

[Sakuno]: 『... Sorry.』<|eot_id|><|start_header_id|>Japanese<|end_header_id|>

[新吾]: 「ううん、こう言っちゃなんだけど、迷子でよかったよ。桜乃は可愛いから、いろいろ心配しちゃってたんだぞ俺」<|eot_id|><|start_header_id|>English<|end_header_id|>

[Shingo]: "Nah, I know it’s weird to say this, but I’m glad you got lost. You’re so cute, Sakuno, so I was really worried about you."<|eot_id|>
```

The generated translation for that prompt, with temperature 0, is:
```
[Shingo]: "Nah, I know it’s weird to say this, but I’m glad you got lost. You’re so cute, Sakuno, so I was really worried about you."
```

### Trivia

The Metadata section isn't limited to character information - you can also add trivia and teach the model the correct way to pronounce words it struggles with.

Here's an example:
```
<|begin_of_text|><|start_header_id|>Metadata<|end_header_id|>

[character] Name: Uryuu Shingo (瓜生 新吾) | Gender: Male | Aliases: Onii-chan (お兄ちゃん)
[character] Name: Uryuu Sakuno (瓜生 桜乃) | Gender: Female
[element] Name: Murasamemaru (叢雨丸) | Type: Quality<|eot_id|><|start_header_id|>Japanese<|end_header_id|>

[桜乃]: 『……ごめん』<|eot_id|><|start_header_id|>English<|end_header_id|>

[Sakuno]: 『... Sorry.』<|eot_id|><|start_header_id|>Japanese<|end_header_id|>

[新吾]: 「ううん、こう言っちゃなんだけど、迷子でよかったよ。桜乃は叢雨丸いから、いろいろ心配しちゃってたんだぞ俺」<|eot_id|><|start_header_id|>English<|end_header_id|>
```

The generated translation for that prompt, with temperature 0, is:
```
[Shingo]: "Nah, I know it’s not the best thing to say, but I’m glad you got lost. Sakuno’s Murasamemaru, so I was really worried about you, you know?"
```